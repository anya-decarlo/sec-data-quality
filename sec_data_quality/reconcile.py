"""Reconciliation: does the same number agree wherever it appears?

Two reconciliations:

1. CROSS_FILING — the same tag for the same period reported in different
   filings (e.g. FY revenue in a 10-K vs. the comparative column of the
   next year's 10-K). Matches confirm the number; differences classify as
   RESTATED (later filing wins) or MISMATCH (can't decide).

2. QUARTERS_VS_ANNUAL — for flow tags, the sum of the four reported
   quarters should equal the reported annual figure. This is the classic
   analyst reconciliation and catches rounding and scope problems.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Optional

from .models import Fact, Finding, ReconRow, fmt_period

Q_SUM_TOLERANCE = 0.005  # 0.5% — absorbs normal presentation rounding


def _fmt(v: float) -> str:
    return f"{v:,.0f}" if abs(v) >= 1e6 else f"{v:.2f}"


def _filing_desc(f: Fact) -> str:
    return f"{f.form} filed {f.filed} (accn {f.accn})"


def cross_filing(facts: list[Fact]) -> tuple[list[ReconRow], list[Finding]]:
    """Compare the same (tag, period) across distinct filings."""
    rows: list[ReconRow] = []
    findings: list[Finding] = []
    groups: dict[tuple, list[tuple[int, Fact]]] = defaultdict(list)
    for i, f in enumerate(facts):
        if f.accn is None or f.val is None or f.end is None:
            continue
        groups[(f.entity, f.tag, f.unit, f.start, f.end)].append((i, f))

    for (entity, tag, unit, start, end), rows_for_period in groups.items():
        # one fact per filing (dedupe within a filing)
        by_accn: dict[str, tuple[int, Fact]] = {}
        for i, f in rows_for_period:
            if f.accn not in by_accn or (f.filed or "") > (by_accn[f.accn][1].filed or ""):
                by_accn[f.accn] = (i, f)
        if len(by_accn) < 2:
            continue

        filings = sorted(by_accn.values(), key=lambda t: (t[1].filed or ""))
        (_, oldest), (_, newest) = filings[0], filings[-1]
        period = f"{start}..{end}" if start else f"as of {end}"

        if oldest.val == newest.val:
            verdict = "MATCH"
            delta, pct = 0.0, 0.0
        else:
            delta = newest.val - oldest.val
            pct = delta / oldest.val if oldest.val else None
            # if every later filing agrees with the newest value, the
            # earlier number was superseded -> restatement, not ambiguity
            later_vals = {f.val for _, f in filings[1:]}
            verdict = "RESTATED" if later_vals == {newest.val} else "MISMATCH"

        rows.append(
            ReconRow(
                kind="CROSS_FILING",
                entity=entity,
                tag=tag,
                unit=unit,
                period=period,
                left_desc=_filing_desc(oldest),
                left_val=oldest.val,
                right_desc=_filing_desc(newest),
                right_val=newest.val,
                delta=delta,
                pct_delta=pct,
                verdict=verdict,
                fact_ids=tuple(i for i, _ in filings),
                notes=f"{len(by_accn)} filings report this period",
            )
        )

        if verdict == "RESTATED":
            findings.append(
                Finding(
                    rule_id="REC001",
                    severity="WARN",
                    entity=entity,
                    tag=tag,
                    period=period,
                    message=(
                        f"value restated: {oldest.val:,} in {oldest.form} "
                        f"({oldest.accn}) superseded by {newest.val:,} "
                        f"in {newest.form} ({newest.accn})"
                    ),
                    fact_ids=tuple(i for i, _ in filings),
                    context={"old": oldest.val, "new": newest.val},
                )
            )
        elif verdict == "MISMATCH":
            findings.append(
                Finding(
                    rule_id="REC002",
                    severity="ERROR",
                    entity=entity,
                    tag=tag,
                    period=period,
                    message=(
                        f"filings disagree on {tag}: values "
                        f"{sorted({f.val for _, f in filings})} across "
                        f"{len(by_accn)} filings"
                    ),
                    fact_ids=tuple(i for i, _ in filings),
                    context={"values": sorted({f.val for _, f in filings})},
                )
            )
    return rows, findings


# Duration bounds (days): fiscal years incl. 53-week years; one fiscal
# quarter with slack for companies on non-calendar quarters.
FY_DAYS = (350, 400)
Q_DAYS = (75, 105)


def _duration(f: Fact) -> Optional[int]:
    if f.start and f.end:
        return _days_between(f.start, f.end)
    return None


def _days_between(start: str, end: str) -> int:
    from datetime import date
    return (date.fromisoformat(end) - date.fromisoformat(start)).days


def quarters_vs_annual(facts: list[Fact]) -> tuple[list[ReconRow], list[Finding]]:
    """Tie reported quarters to the reported annual figure.

    For each annual (FY-duration) fact, gather same-tag facts with
    quarter-length durations inside the annual window (deduplicated by
    period, latest filing wins). Four quarters -> tie the sum to the
    annual number (PASS/FAIL). Three quarters -> derive the unreported
    fourth quarter as annual - Q1-Q3 (IMPLIED): companies almost never
    tag a standalone Q4 fact, so deriving it is the practical check.
    """
    rows: list[ReconRow] = []
    findings: list[Finding] = []
    annuals: dict[tuple, list[tuple[int, Fact]]] = defaultdict(list)
    quarters: dict[tuple, list[tuple[int, Fact]]] = defaultdict(list)

    for i, f in enumerate(facts):
        if f.val is None:
            continue
        d = _duration(f)
        if d is None:
            continue
        key = (f.entity, f.tag, f.unit)
        if FY_DAYS[0] <= d <= FY_DAYS[1]:
            annuals[key].append((i, f))
        elif Q_DAYS[0] <= d <= Q_DAYS[1]:
            quarters[key].append((i, f))

    for (entity, tag, unit), ann_list in annuals.items():
        # one annual figure per period, latest filing wins
        by_period: dict[tuple, tuple[int, Fact]] = {}
        for i, f in ann_list:
            if f.period_key not in by_period or (f.filed or "") > (
                by_period[f.period_key][1].filed or ""
            ):
                by_period[f.period_key] = (i, f)

        for annual_i, annual in by_period.values():
            in_year = [
                (i, f)
                for i, f in quarters[(entity, tag, unit)]
                if f.start >= annual.start and f.end <= annual.end
            ]
            # dedupe to latest per period, keep only non-overlapping facts
            q_by_period: dict[tuple, tuple[int, Fact]] = {}
            for i, f in in_year:
                if f.period_key not in q_by_period or (f.filed or "") > (
                    q_by_period[f.period_key][1].filed or ""
                ):
                    q_by_period[f.period_key] = (i, f)
            qs = sorted(q_by_period.values(), key=lambda t: t[1].start)
            non_overlap = []
            last_end = ""
            for i, f in qs:
                if f.start >= last_end:
                    non_overlap.append((i, f))
                    last_end = f.end

            period = f"{annual.start}..{annual.end}"
            if len(non_overlap) == 4:
                q_ids = tuple(i for i, _ in non_overlap)
                q_sum = sum(f.val for _, f in non_overlap)
                delta = annual.val - q_sum
                pct = delta / annual.val if annual.val else None
                ok = pct is not None and abs(pct) <= Q_SUM_TOLERANCE
                rows.append(
                    ReconRow(
                        kind="QUARTERS_VS_ANNUAL",
                        entity=entity, tag=tag, unit=unit, period=period,
                        left_desc=_filing_desc(annual), left_val=annual.val,
                        right_desc="sum of 4 quarterly facts",
                        right_val=q_sum, delta=delta, pct_delta=pct,
                        verdict="PASS" if ok else "FAIL",
                        fact_ids=(annual_i,) + q_ids,
                        notes=f"tolerance {Q_SUM_TOLERANCE:.1%}",
                    )
                )
                if not ok:
                    findings.append(
                        Finding(
                            rule_id="REC003", severity="ERROR",
                            entity=entity, tag=tag, period=period,
                            message=(
                                f"annual {annual.val:,} != sum of quarters "
                                f"{q_sum:,} (delta {delta:+,}, {pct:+.2%})"
                            ),
                            fact_ids=(annual_i,) + q_ids,
                            context={
                                "annual": annual.val, "q_sum": q_sum,
                                "delta": delta,
                            },
                        )
                    )
            elif len(non_overlap) == 3:
                covered = {(f.start, f.end) for _, f in non_overlap}
                implied = annual.val - sum(f.val for _, f in non_overlap)
                rows.append(
                    ReconRow(
                        kind="IMPLIED_Q4",
                        entity=entity, tag=tag, unit=unit, period=period,
                        left_desc=_filing_desc(annual), left_val=annual.val,
                        right_desc="sum of 3 reported quarters",
                        right_val=annual.val - implied,
                        delta=implied, pct_delta=None,
                        verdict="IMPLIED",
                        fact_ids=(annual_i,)
                        + tuple(i for i, _ in non_overlap),
                        notes=(
                            f"Q4 derived as annual - 3 quarters = "
                            f"{_fmt(implied)}; covered periods "
                            f"{sorted(covered)}"
                        ),
                    )
                )
    return rows, findings


def run_reconciliation(
    facts: list[Fact],
) -> tuple[list[ReconRow], list[Finding]]:
    rows_a, findings_a = cross_filing(facts)
    rows_b, findings_b = quarters_vs_annual(facts)
    return rows_a + rows_b, findings_a + findings_b
