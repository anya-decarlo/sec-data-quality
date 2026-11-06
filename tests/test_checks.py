"""Checks must catch the defects planted in the sample payload."""

import json
import tempfile
import unittest
from pathlib import Path

from sec_data_quality.checks import run_checks
from sec_data_quality.edgar import load_facts
from sec_data_quality.sample_data import build_payload


def _facts():
    with tempfile.NamedTemporaryFile(
        "w", suffix=".json", delete=False
    ) as fh:
        json.dump(build_payload(), fh)
    return load_facts(Path(fh.name))


class TestChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.facts = _facts()
        cls.findings = run_checks(cls.facts)
        cls.by_rule = {}
        for f in cls.findings:
            cls.by_rule.setdefault(f.rule_id, []).append(f)

    def test_missing_lineage_fields(self):
        self.assertEqual(len(self.by_rule.get("DQ001", [])), 1)

    def test_duplicate_fact(self):
        self.assertEqual(len(self.by_rule.get("DQ002", [])), 1)
        f = self.by_rule["DQ002"][0]
        self.assertEqual(f.context["count"], 2)

    def test_negative_revenue(self):
        neg = self.by_rule.get("DQ004", [])
        self.assertEqual(len(neg), 1)
        self.assertEqual(neg[0].severity, "ERROR")

    def test_unit_mix(self):
        units = self.by_rule.get("DQ005", [])
        self.assertEqual(len(units), 1)
        self.assertEqual(units[0].context["unit"], "USD")
        self.assertEqual(units[0].context["canonical"], "USD/shares")

    def test_no_false_period_flags(self):
        # all sample durations are consistent with their fp labels
        self.assertNotIn("DQ003", self.by_rule)


if __name__ == "__main__":
    unittest.main()
