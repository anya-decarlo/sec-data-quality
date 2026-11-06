"""Output writers — the four portfolio deliverables.

  issue_log.csv            — every finding, severity, rule, affected facts
  lineage.csv / .jsonl     — where each emitted number came from (accn, form,
                             filed date, EDGAR endpoint) plus its fitness
  reconciliation.csv/.md   — cross-filing and quarters-vs-annual comparison
  fitness_summary.csv      — verdict counts per entity/tag
  summary.md               — human-readable run report tying it together
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

from .models import FIT, NOT_FIT, REVIEW, Fact, Finding, ReconRow, fmt_period

ISSUE_FIELDS = [
    "rule_id", "severity", "entity", "tag", "period", "message",
    "n_facts_affected", "context",
]

LINEAGE_FIELDS = [
    "entity", "cik", "taxonomy", "tag", "label", "period_start",
    "period_end", "fy", "fp", "value", "unit", "source_filing_accn",
    "source_form", "source_filed_date", "source_endpoint", "fitness",
    "notes",
]

RECON_FIELDS = [
    "kind", "entity", "tag", "unit", "period", "left_desc", "left_val",
    "right_desc", "right_val", "delta", "pct_delta", "verdict", "notes",
]

ENDPOINT = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"


def write_issue_log(findings: list[Finding], path: Path) -> None:
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=ISSUE_FIELDS)
        w.writeheader()
        for f in sorted(findings, key=lambda x: (x.severity, x.rule_id), reverse=True):
            w.writerow({
                "rule_id": f.rule_id,
                "severity": f.severity,
                "entity": f.entity,
                "tag": f.tag,
                "period": f.period,
                "message": f.message,
                "n_facts_affected": len(f.fact_ids),
                "context": json.dumps(f.context),
            })


def write_lineage(
    facts: list[Fact],
    verdicts: list[str],
    superseded: set[int],
    path_csv: Path,
    path_jsonl: Path,
) -> None:
    with path_csv.open("w", newline="") as fh, path_jsonl.open("w") as jf:
        w = csv.DictWriter(fh, fieldnames=LINEAGE_FIELDS)
        w.writeheader()
        for i, f in enumerate(facts):
            notes = "superseded by later filing" if i in superseded else ""
            fitness = NOT_FIT if i in superseded else verdicts[i]
            row = {
                "entity": f.entity,
                "cik": f.cik,
                "taxonomy": f.taxonomy,
                "tag": f.tag,
                "label": f.label,
                "period_start": f.start or "",
                "period_end": f.end or "",
                "fy": f.fy or "",
                "fp": f.fp or "",
                "value": f.val,
                "unit": f.unit,
                "source_filing_accn": f.accn or "",
                "source_form": f.form or "",
                "source_filed_date": f.filed or "",
                "source_endpoint": ENDPOINT.format(cik=f.cik),
                "fitness": fitness,
                "notes": notes,
            }
            w.writerow(row)
            jf.write(json.dumps(row, default=str) + "\n")


def write_recon_csv(rows: list[ReconRow], path: Path) -> None:
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=RECON_FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: getattr(r, k) for k in RECON_FIELDS})


def write_fitness_summary(
    facts: list[Fact], verdicts: list[str], superseded: set[int], path: Path
) -> None:
    counts: dict[tuple, Counter] = defaultdict(Counter)
    for i, f in enumerate(facts):
        v = NOT_FIT if i in superseded else verdicts[i]
        counts[(f.entity, f.tag)][v] += 1
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["entity", "tag", FIT, REVIEW, NOT_FIT, "total"])
        for (entity, tag), c in sorted(counts.items()):
            w.writerow([entity, tag, c[FIT], c[REVIEW], c[NOT_FIT], sum(c.values())])


def _fmt_num(v) -> str:
    if not isinstance(v, (int, float)):
        return str(v)
    return f"{v:,.0f}" if abs(v) >= 1e6 else f"{v:,.2f}"


def write_summary_md(
    facts: list[Fact],
    findings: list[Finding],
    recon_rows: list[ReconRow],
    verdicts: list[str],
    superseded: set[int],
    path: Path,
) -> None:
    entities = sorted({f.entity for f in facts})
    sev = Counter(f.severity for f in findings)
    verdict_counts = Counter(
        NOT_FIT if i in superseded else verdicts[i] for i in range(len(facts))
    )

    lines = [
        "# Data Quality & Reconciliation Report",
        "",
        f"- Entities: {', '.join(entities)}",
        f"- Facts examined: {len(facts):,}",
        f"- Findings: {len(findings):,} "
        f"(ERROR {sev.get('ERROR', 0)}, WARN {sev.get('WARN', 0)}, "
        f"INFO {sev.get('INFO', 0)})",
        f"- Reconciliations run: {len(recon_rows):,}",
        "",
        "## Fitness for use",
        "",
        f"| {FIT} | {REVIEW} | {NOT_FIT} |",
        "|---|---|---|",
        f"| {verdict_counts[FIT]:,} | {verdict_counts[REVIEW]:,} "
        f"| {verdict_counts[NOT_FIT]:,} |",
        "",
        "## Reconciliation detail",
        "",
    ]

    for kind in ("CROSS_FILING", "QUARTERS_VS_ANNUAL", "IMPLIED_Q4"):
        subset = [r for r in recon_rows if r.kind == kind]
        if not subset:
            continue
        # matches are bulk confirmation — the report highlights exceptions
        interesting = [r for r in subset if r.verdict not in ("MATCH", "PASS")]
        shown = interesting if interesting else subset
        lines += [
            f"### {kind.replace('_', ' ').title()}",
            "",
            f"({len(subset):,} comparisons; "
            f"{len(interesting):,} non-MATCH shown, capped at 100 — "
            f"full detail in reconciliation.csv)",
            "",
            "| Entity | Tag | Period | Left | Right | Δ | Verdict |",
            "|---|---|---|---|---|---|---|",
        ]
        for r in shown[:100]:
            delta = f"{r.delta:+,.0f}" if r.delta and abs(r.delta) >= 1e6 else (
                f"{r.delta:+,.2f}" if r.delta else "0"
            )
            lines.append(
                f"| {r.entity} | `{r.tag}` | {r.period} "
                f"| {r.left_desc}: {_fmt_num(r.left_val)} "
                f"| {r.right_desc}: {_fmt_num(r.right_val)} "
                f"| {delta} | {r.verdict} |"
            )
        lines.append("")

    lines += ["## Issue log (top 20 by severity)", ""]
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for f in sorted(findings, key=lambda x: order.get(x.severity, 9))[:20]:
        lines.append(
            f"- **[{f.severity}] {f.rule_id}** — {f.entity} `{f.tag}` "
            f"{f.period}: {f.message}"
        )
    if len(findings) > 20:
        lines.append(f"- … and {len(findings) - 20} more; see issue_log.csv")
    lines.append("")
    path.write_text("\n".join(lines))
