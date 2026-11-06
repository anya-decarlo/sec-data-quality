"""Fitness-for-use verdicts.

Every emitted number gets a verdict:

  FIT      — no findings, or INFO only: use it.
  REVIEW   — WARN attached (e.g. restated but resolved): a human should
             glance at it before relying on it.
  NOT-FIT  — ERROR attached (filings disagree, impossible value, missing
             lineage): do not put this number in front of anyone.

Verdicts attach to facts via the fact_ids that findings carry.
"""

from __future__ import annotations

from collections import defaultdict

from .models import FIT, NOT_FIT, REVIEW, Finding, worst_verdict


def fact_verdicts(n_facts: int, findings: list[Finding]) -> list[str]:
    """Verdict per fact index, from the worst severity touching that fact."""
    per_fact: dict[int, list[str]] = defaultdict(list)
    for finding in findings:
        for i in finding.fact_ids:
            per_fact[i].append(finding.severity)
    return [worst_verdict(per_fact.get(i, [])) for i in range(n_facts)]


def superseded_ids(n_facts: int, facts, recon_rows) -> set[int]:
    """Fact indices whose values were superseded by a later filing."""
    out = set()
    for row in recon_rows:
        if row.kind != "CROSS_FILING" or row.verdict != "RESTATED":
            continue
        for i in row.fact_ids:
            f = facts[i]
            # the superseded facts are the ones in the *older* filings —
            # i.e. any fact in the group whose value is not the newest one
            if f.val != row.right_val:
                out.add(i)
    return out
