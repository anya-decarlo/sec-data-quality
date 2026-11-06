"""Pipeline orchestration: raw EDGAR JSON -> checks -> reconciliation ->
verdicts -> deliverables."""

from __future__ import annotations

from pathlib import Path

from . import report
from .checks import run_checks
from .edgar import load_facts
from .fitness import fact_verdicts, superseded_ids
from .models import Fact
from .reconcile import run_reconciliation

# Focus metrics for the default run — the classic analyst watchlist.
DEFAULT_METRICS = [
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    "NetIncomeLoss",
    "OperatingIncomeLoss",
    "Assets",
    "CashAndCashEquivalentsAtCarryingValue",
    "EarningsPerShareDiluted",
]


def run(
    raw_files: list[Path],
    out_dir: Path,
    metrics: list[str] | None = None,
) -> dict:
    """Execute the full pipeline; returns a dict of summary stats."""
    out_dir.mkdir(parents=True, exist_ok=True)
    metrics = metrics if metrics is not None else DEFAULT_METRICS

    facts: list[Fact] = []
    for path in sorted(raw_files):
        facts.extend(load_facts(Path(path)))
    if metrics:
        wanted = set(metrics)
        facts = [f for f in facts if f.tag in wanted]

    findings = run_checks(facts)
    recon_rows, recon_findings = run_reconciliation(facts)
    findings += recon_findings

    verdicts = fact_verdicts(len(facts), findings)
    superseded = superseded_ids(len(facts), facts, recon_rows)

    report.write_issue_log(findings, out_dir / "issue_log.csv")
    report.write_lineage(
        facts, verdicts, superseded,
        out_dir / "lineage.csv", out_dir / "lineage.jsonl",
    )
    report.write_recon_csv(recon_rows, out_dir / "reconciliation.csv")
    report.write_fitness_summary(
        facts, verdicts, superseded, out_dir / "fitness_summary.csv"
    )
    report.write_summary_md(
        facts, findings, recon_rows, verdicts, superseded,
        out_dir / "summary.md",
    )

    return {
        "facts": len(facts),
        "findings": len(findings),
        "recon_rows": len(recon_rows),
        "out_dir": str(out_dir),
    }
