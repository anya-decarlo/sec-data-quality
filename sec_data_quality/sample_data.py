"""Synthetic companyfacts payload with planted defects.

Used by `python -m sec_data_quality sample` and by the test suite, so the
pipeline is demonstrable offline. Defects planted:

  * FY2023 revenue: annual 10-K says 1,000,000 but Q1-Q4 sum to
    1,010,000          -> REC003 (quarters don't tie to annual)
  * FY2024 revenue: 10-K says 1,200,000, next year's 10-K comparative
    says 1,210,000     -> REC001 (restatement)
  * Q2 2023 revenue reported twice identically in the same filing
                         -> DQ002 (duplicate)
  * Q3 2024 revenue reported as -90,000
                         -> DQ004 (impossible sign)
  * One EPS fact reported under unit "USD" instead of "USD/shares"
                         -> DQ005 (unit mix)
  * One fact missing its accession number
                         -> DQ001 (lineage gap)
"""

from __future__ import annotations

import json
from pathlib import Path

ENTITY = "Acme Synthetic Corp"
CIK = 9999999


def _f(start, end, val, fy, fp, form, filed, accn):
    return {
        "start": start, "end": end, "val": val, "fy": fy, "fp": fp,
        "form": form, "filed": filed, "accn": accn,
    }


def build_payload() -> dict:
    rev = []
    # FY2023 quarters (filed in four 10-Qs) — sum is 1,010,000
    rev += [
        _f("2023-01-01", "2023-03-31", 240_000, 2023, "Q1", "10-Q", "2023-04-28", "a-23-q1"),
        _f("2023-04-01", "2023-06-30", 250_000, 2023, "Q2", "10-Q", "2023-07-28", "a-23-q2"),
        _f("2023-04-01", "2023-06-30", 250_000, 2023, "Q2", "10-Q", "2023-07-28", "a-23-q2"),  # duplicate
        _f("2023-07-01", "2023-09-30", 260_000, 2023, "Q3", "10-Q", "2023-10-27", "a-23-q3"),
        _f("2023-10-01", "2023-12-31", 260_000, 2023, "Q4", "10-K", "2024-02-16", "a-23-10k"),
        # annual: 1,000,000 — does not tie to the quarters
        _f("2023-01-01", "2023-12-31", 1_000_000, 2023, "FY", "10-K", "2024-02-16", "a-23-10k"),
    ]
    # FY2024 quarters + a negative quarter + restated annual
    rev += [
        _f("2024-01-01", "2024-03-31", 270_000, 2024, "Q1", "10-Q", "2024-04-26", "a-24-q1"),
        _f("2024-04-01", "2024-06-30", 300_000, 2024, "Q2", "10-Q", "2024-07-26", "a-24-q2"),
        _f("2024-07-01", "2024-09-30", -90_000, 2024, "Q3", "10-Q", "2024-10-25", "a-24-q3"),
        _f("2024-10-01", "2024-12-31", 310_000, 2024, "Q4", "10-K", "2025-02-14", "a-24-10k"),
        _f("2024-01-01", "2024-12-31", 1_200_000, 2024, "FY", "10-K", "2025-02-14", "a-24-10k"),
        # prior-year comparative in the FY2025 10-K: restated value
        _f("2024-01-01", "2024-12-31", 1_210_000, 2025, "FY", "10-K", "2026-02-13", "a-25-10k"),
    ]
    # lineage gap: no accn
    rev.append(_f("2024-01-01", "2024-03-31", 270_000, 2024, "Q1", "10-Q", "2024-04-26", None))

    eps = [
        _f("2023-01-01", "2023-12-31", 1.25, 2023, "FY", "10-K", "2024-02-16", "a-23-10k"),
        _f("2024-01-01", "2024-12-31", 1.50, 2024, "FY", "10-K", "2025-02-14", "a-24-10k"),
    ]

    return {
        "cik": CIK,
        "entityName": ENTITY,
        "facts": {
            "us-gaap": {
                "Revenues": {"label": "Revenue", "units": {"USD": rev}},
                "EarningsPerShareDiluted": {
                    "label": "EPS (diluted)",
                    # planted mixed units: same tag under USD and USD/shares
                    "units": {"USD/shares": eps, "USD": eps[:1]},
                },
            }
        },
    }


def write_sample(raw_dir: Path) -> Path:
    raw_dir.mkdir(parents=True, exist_ok=True)
    path = raw_dir / f"CIK{CIK:010d}_ACME.json"
    path.write_text(json.dumps(build_payload(), indent=2))
    return path
