"""End-to-end: sample payload -> deliverable files with expected content."""

import csv
import tempfile
import unittest
from pathlib import Path

from sec_data_quality.pipeline import run
from sec_data_quality.sample_data import write_sample


class TestPipeline(unittest.TestCase):
    def test_outputs_exist_and_have_content(self):
        with tempfile.TemporaryDirectory() as raw, tempfile.TemporaryDirectory() as out:
            path = write_sample(Path(raw))
            stats = run([path], Path(out), metrics=None)

            for name in (
                "issue_log.csv", "lineage.csv", "lineage.jsonl",
                "reconciliation.csv", "fitness_summary.csv", "summary.md",
            ):
                p = Path(out) / name
                self.assertTrue(p.exists(), name)
                self.assertGreater(p.stat().st_size, 0, name)

            with open(Path(out) / "lineage.csv") as fh:
                lineage = list(csv.DictReader(fh))
            self.assertEqual(len(lineage), stats["facts"])

            # the missing-accn fact must be visible in the lineage output
            self.assertTrue(any(r["source_filing_accn"] == "" for r in lineage))
            # and nothing should silently come out FIT that was flagged
            self.assertTrue(any(r["fitness"] != "FIT" for r in lineage))


if __name__ == "__main__":
    unittest.main()
