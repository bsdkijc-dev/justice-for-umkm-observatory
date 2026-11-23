"""Automated unit test suite for Justice for UMKM Observatory v1.0."""

from __future__ import annotations

import csv
import json
from pathlib import Path
import unittest

import pandas as pd

from processing.normalization import normalize_idr_numeric
from processing.privacy_review import review_directory, scan_dataframe_for_pii
from processing.taxonomy import classify_dispute_text, classify_enterprise_pp7_2021
from processing.validation import validate_directory


ROOT = Path(__file__).resolve().parent.parent


class TestObservatoryPipeline(unittest.TestCase):
    def test_statutory_pp7_2021_classification(self) -> None:
        self.assertEqual(classify_enterprise_pp7_2021(business_capital_idr=500_000_000), "micro")
        self.assertEqual(classify_enterprise_pp7_2021(business_capital_idr=2_500_000_000), "small")
        self.assertEqual(classify_enterprise_pp7_2021(business_capital_idr=8_000_000_000), "medium")
        self.assertEqual(classify_enterprise_pp7_2021(annual_sales_idr=1_500_000_000), "micro")
        self.assertEqual(classify_enterprise_pp7_2021(annual_sales_idr=10_000_000_000), "small")
        self.assertEqual(classify_enterprise_pp7_2021(annual_sales_idr=30_000_000_000), "medium")
        # Never infer from absence of evidence
        self.assertEqual(classify_enterprise_pp7_2021(), "unknown")

    def test_dispute_taxonomy_and_unknown_preservation(self) -> None:
        res_contract = classify_dispute_text("Gugatan wanprestasi atas tagihan invoice supplier")
        self.assertIn("CAT-01", res_contract.categories)
        self.assertGreaterEqual(res_contract.confidence, 0.5)

        res_multi = classify_dispute_text("Sengketa sewa ruko dan kredit jaminan fidusia")
        self.assertIn("CAT-02", res_multi.categories)
        self.assertIn("CAT-03", res_multi.categories)

        res_unknown = classify_dispute_text("Perkara tanpa rincian substansi")
        self.assertEqual(res_unknown.categories, ["UNKNOWN"])

    def test_zero_imputation_idr_normalization(self) -> None:
        self.assertIsNone(normalize_idr_numeric(None))
        self.assertIsNone(normalize_idr_numeric(""))
        self.assertIsNone(normalize_idr_numeric("-"))
        self.assertEqual(normalize_idr_numeric("Rp 1.500.000"), 1_500_000.0)

    def test_synthetic_schema_validation(self) -> None:
        results = validate_directory(ROOT / "data" / "synthetic", ROOT / "schemas")
        self.assertTrue(len(results) >= 4)
        for name, errs in results.items():
            self.assertEqual(errs, [], f"Schema errors in {name}: {errs}")

    def test_privacy_review_passes_synthetic_and_catches_pii(self) -> None:
        findings = review_directory(ROOT / "data" / "synthetic")
        for name, issues in findings.items():
            self.assertEqual(issues, [], f"Privacy issues in {name}: {issues}")

        bad_df = pd.DataFrame([{"nik": "3175012345678901", "email": "owner@example.com"}])
        caught = scan_dataframe_for_pii(bad_df, "bad.csv")
        self.assertTrue(len(caught) >= 2)

    def test_twelve_notebooks_valid_json(self) -> None:
        nb_dir = ROOT / "analysis" / "notebooks"
        nbs = sorted(nb_dir.glob("*.ipynb"))
        self.assertEqual(len(nbs), 12)
        for nb in nbs:
            data = json.loads(nb.read_text(encoding="utf-8"))
            self.assertEqual(data.get("nbformat"), 4)
            self.assertTrue(len(data.get("cells", [])) >= 2)

    def test_official_sources_registry(self) -> None:
        with (ROOT / "sources" / "official_sources.csv").open("r", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        self.assertGreaterEqual(len(rows), 10)
        for row in rows:
            self.assertTrue(row["official_url"].startswith("https://"))
            self.assertTrue(bool(row["data_limitations"]))


if __name__ == "__main__":
    unittest.main()
