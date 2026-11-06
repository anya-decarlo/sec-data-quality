"""Reconciliation must flag the restatement and the quarter-sum failure."""

import json
import tempfile
import unittest
from pathlib import Path

from sec_data_quality.edgar import load_facts
from sec_data_quality.reconcile import run_reconciliation
from sec_data_quality.sample_data import build_payload


def _facts():
    with tempfile.NamedTemporaryFile(
        "w", suffix=".json", delete=False
    ) as fh:
        json.dump(build_payload(), fh)
    return load_facts(Path(fh.name))


class TestReconcile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.findings = run_reconciliation(_facts())

    def test_restatement_detected(self):
        restated = [
            r for r in self.rows
            if r.kind == "CROSS_FILING" and r.verdict == "RESTATED"
        ]
        self.assertEqual(len(restated), 1)
        r = restated[0]
        self.assertEqual(r.left_val, 1_200_000)
        self.assertEqual(r.right_val, 1_210_000)
        self.assertEqual(r.delta, 10_000)

    def test_quarters_vs_annual_fails_2023(self):
        qva = {
            r.period: r for r in self.rows if r.kind == "QUARTERS_VS_ANNUAL"
        }
        row = qva["2023-01-01..2023-12-31"]
        self.assertEqual(row.verdict, "FAIL")
        self.assertEqual(row.delta, -10_000)

    def test_restatements_and_mismatches_raise_findings(self):
        rules = {f.rule_id for f in self.findings}
        self.assertIn("REC001", rules)   # restatement
        self.assertIn("REC003", rules)   # quarters don't tie


if __name__ == "__main__":
    unittest.main()
