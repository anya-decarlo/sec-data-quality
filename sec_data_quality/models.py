"""Core data structures for the SEC data-quality pipeline.

A `Fact` is one reported number extracted from an SEC XBRL companyfacts
payload. Every Fact carries the filing accession number, form, and filed
date, which is what lets downstream outputs prove *where a number came from*.

A `Finding` is one observation produced by a quality or reconciliation
rule. Findings reference Facts by index into the fact list, which is how
the fitness engine attaches verdicts to individual numbers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass(frozen=True)
class Fact:
    """One XBRL fact as returned by the SEC companyfacts endpoint."""

    entity: str
    cik: int
    taxonomy: str          # us-gaap, dei, ...
    tag: str               # e.g. RevenueFromContractWithCustomerExcludingAssessedTax
    label: str
    unit: str              # USD, shares, USD/shares, ...
    val: Optional[float]
    start: Optional[str]   # ISO date; None for instant facts (balances)
    end: Optional[str]
    fy: Optional[int]
    fp: Optional[str]      # Q1..Q4, FY, or None
    form: Optional[str]    # 10-K, 10-Q, 8-K, ...
    filed: Optional[str]   # ISO date the filing hit EDGAR
    accn: Optional[str]    # accession number = the filing's unique ID
    frame: Optional[str] = None

    @property
    def period_key(self) -> tuple:
        """Canonical key for 'same reported period' across filings."""
        return (self.start, self.end)

    @property
    def is_duration(self) -> bool:
        return self.start is not None


@dataclass
class Finding:
    """One issue or observation from a quality/reconciliation rule."""

    rule_id: str           # e.g. DQ001, REC001
    severity: str          # INFO | WARN | ERROR
    entity: str
    tag: str
    period: str            # human-readable, e.g. "2024-09-28..2025-09-27"
    message: str
    fact_ids: tuple = ()   # indices into the fact list
    context: dict = field(default_factory=dict)


@dataclass
class ReconRow:
    """One line of the reconciliation report."""

    kind: str              # CROSS_FILING | QUARTERS_VS_ANNUAL
    entity: str
    tag: str
    unit: str
    period: str
    left_desc: str         # e.g. "10-K filed 2024-11-01 (accn ...)"
    left_val: Optional[float]
    right_desc: str
    right_val: Optional[float]
    delta: Optional[float]
    pct_delta: Optional[float]
    verdict: str           # MATCH | RESTATED | MISMATCH | PASS | FAIL
    fact_ids: tuple = ()
    notes: str = ""


SEVERITY_ORDER = {"INFO": 0, "WARN": 1, "ERROR": 2}

FIT = "FIT"
REVIEW = "REVIEW"
NOT_FIT = "NOT-FIT"


def worst_verdict(severities: list[str]) -> str:
    """Fitness verdict for a number given the severities attached to it."""
    if not severities:
        return FIT
    worst = max(severities, key=lambda s: SEVERITY_ORDER.get(s, 0))
    return REVIEW if worst == "WARN" else (NOT_FIT if worst == "ERROR" else FIT)


def fmt_period(fact: Fact) -> str:
    if fact.start:
        return f"{fact.start}..{fact.end}"
    return f"as of {fact.end}"
