"""Data-quality checks over extracted facts.

Each rule is a small function that yields Findings. Rule IDs are stable
(DQxxx) so issue-log rows can be traced back to the code that raised them.
"""

from __future__ import annotations

from collections import defaultdict
from datetime import date
from typing import Iterable, Iterator

from .models import Fact, Finding, fmt_period

# Tags that can never legitimately be negative. (Note: *IncomeLoss tags
# are excluded — a loss is reported as a negative value by design.)
NON_NEGATIVE_TAGS = {
    "Revenues",
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    "Assets",
    "CashAndCashEquivalentsAtCarryingValue",
}

# Plausible bounds (days) for any duration fact — tighter than "positive"
# but loose enough for YTD periods and 52/53-week fiscal years.
MIN_DURATION_DAYS = 20
MAX_DURATION_DAYS = 400


def _days(start: str, end: str) -> int:
    s = date.fromisoformat(start)
    e = date.fromisoformat(end)
    return (e - s).days


def check_missing_fields(facts: list[Fact]) -> Iterator[Finding]:
    """DQ001 — a reported number missing the fields needed for lineage."""
    for i, f in enumerate(facts):
        missing = [k for k in ("end", "filed", "accn") if getattr(f, k) is None]
        if f.is_duration and f.start is None:
            missing.append("start")
        if missing:
            yield Finding(
                rule_id="DQ001",
                severity="ERROR",
                entity=f.entity,
                tag=f.tag,
                period=fmt_period(f),
                message=f"fact is missing lineage fields: {', '.join(missing)}",
                fact_ids=(i,),
                context={"missing": missing},
            )


def check_duplicates(facts: list[Fact]) -> Iterator[Finding]:
    """DQ002 — identical numbers reported twice in the same filing."""
    groups: dict[tuple, list[int]] = defaultdict(list)
    for i, f in enumerate(facts):
        if f.accn is None:
            continue
        key = (f.entity, f.tag, f.unit, f.start, f.end, f.val, f.accn)
        groups[key].append(i)
    for key, idxs in groups.items():
        if len(idxs) > 1:
            f = facts[idxs[0]]
            yield Finding(
                rule_id="DQ002",
                severity="WARN",
                entity=f.entity,
                tag=f.tag,
                period=fmt_period(f),
                message=f"{len(idxs)} identical facts for this period in filing {f.accn}",
                fact_ids=tuple(idxs),
                context={"accn": f.accn, "count": len(idxs)},
            )


def check_period_bounds(facts: list[Fact]) -> Iterator[Finding]:
    """DQ003 — implausible reporting period.

    `fp` in companyfacts describes the *filing's* fiscal period, not the
    fact's duration (a 9-month YTD figure in a Q3 10-Q is legitimately
    ~272 days), so we only flag durations no filing could plausibly cover.
    """
    for i, f in enumerate(facts):
        if not f.is_duration or f.end is None:
            continue
        days = _days(f.start, f.end)
        if days <= 0:
            yield Finding(
                rule_id="DQ003",
                severity="ERROR",
                entity=f.entity,
                tag=f.tag,
                period=fmt_period(f),
                message=f"period start {f.start} is not before end {f.end}",
                fact_ids=(i,),
                context={"days": days},
            )
        elif not (MIN_DURATION_DAYS <= days <= MAX_DURATION_DAYS):
            yield Finding(
                rule_id="DQ003",
                severity="WARN",
                entity=f.entity,
                tag=f.tag,
                period=fmt_period(f),
                message=f"duration {days} days is implausible for a reported period",
                fact_ids=(i,),
                context={"days": days},
            )


def check_sign(facts: list[Fact]) -> Iterator[Finding]:
    """DQ004 — negative value where the tag cannot legitimately be negative."""
    for i, f in enumerate(facts):
        if f.tag in NON_NEGATIVE_TAGS and f.val is not None and f.val < 0:
            yield Finding(
                rule_id="DQ004",
                severity="ERROR",
                entity=f.entity,
                tag=f.tag,
                period=fmt_period(f),
                message=f"{f.tag} reported as {f.val:,} (< 0 is impossible)",
                fact_ids=(i,),
                context={"val": f.val},
            )


def check_unit_consistency(facts: list[Fact]) -> Iterator[Finding]:
    """DQ005 — one tag reported under multiple units.

    Mixing units usually means scale confusion downstream (USD vs USD/shares
    is the classic one). The most-common unit is treated as canonical.
    """
    by_tag: dict[tuple[str, str], dict[str, list[int]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for i, f in enumerate(facts):
        by_tag[(f.entity, f.tag)][f.unit].append(i)
    for (entity, tag), units in by_tag.items():
        if len(units) <= 1:
            continue
        canonical = max(units, key=lambda u: len(units[u]))
        for unit, idxs in units.items():
            if unit == canonical:
                continue
            f = facts[idxs[0]]
            yield Finding(
                rule_id="DQ005",
                severity="WARN",
                entity=entity,
                tag=tag,
                period=f"n/a ({len(idxs)} facts)",
                message=(
                    f"tag also reported in unit {unit!r}; canonical unit "
                    f"is {canonical!r}"
                ),
                fact_ids=tuple(idxs),
                context={"unit": unit, "canonical": canonical},
            )


def check_magnitude(facts: list[Fact]) -> Iterator[Finding]:
    """DQ006 — implausible period-over-period magnitude change.

    A 20x+ swing on the same tag between consecutive annual periods usually
    means a units error (thousands vs dollars) rather than real movement.
    """
    by_period: dict[tuple, list[tuple[int, Fact]]] = defaultdict(list)
    for i, f in enumerate(facts):
        if f.val and f.start and f.fp == "FY":
            by_period[(f.entity, f.tag, f.unit)].append((i, f))
    for (entity, tag, unit), rows in by_period.items():
        # latest fact per fiscal year, sorted by fy
        latest: dict[int, tuple[int, Fact]] = {}
        for i, f in rows:
            if f.fy is None:
                continue
            if f.fy not in latest or (f.filed or "") > (latest[f.fy][1].filed or ""):
                latest[f.fy] = (i, f)
        ordered = [latest[fy] for fy in sorted(latest)]
        for (pi, prev), (ci, cur) in zip(ordered, ordered[1:]):
            if prev.val and cur.val and prev.val > 0 and cur.val > 0:
                ratio = cur.val / prev.val
                if ratio > 20 or ratio < 0.05:
                    yield Finding(
                        rule_id="DQ006",
                        severity="WARN",
                        entity=entity,
                        tag=tag,
                        period=f"FY{cur.fy}",
                        message=(
                            f"{tag} moved {ratio:.1f}x year over year "
                            f"({prev.val:,} -> {cur.val:,}); possible unit error"
                        ),
                        fact_ids=(pi, ci),
                        context={"ratio": ratio},
                    )


ALL_CHECKS = [
    check_missing_fields,
    check_duplicates,
    check_period_bounds,
    check_sign,
    check_unit_consistency,
    check_magnitude,
]


def run_checks(facts: list[Fact]) -> list[Finding]:
    findings: list[Finding] = []
    for check in ALL_CHECKS:
        findings.extend(check(facts))
    return findings
