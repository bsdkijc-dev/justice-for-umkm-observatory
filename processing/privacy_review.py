"""Automated privacy & PII gatekeeper for public dataset candidates."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, List

import pandas as pd


PROHIBITED_COLUMNS = {
    "nik", "npwp", "ktp", "phone", "phone_number", "mobile", "email",
    "bank_account", "rekening", "home_address", "street_address",
    "full_name", "owner_name", "judge_name",
}

PII_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "indonesian_phone": re.compile(r"\b(?:\+62|62|08)\d{8,12}\b"),
    "nik_16_digit": re.compile(r"\b\d{16}\b"),
}


def scan_dataframe_for_pii(df: pd.DataFrame, filename: str) -> List[str]:
    """Check column names and string cells for prohibited PII or quasi-identifier risks."""
    findings: List[str] = []
    lower_cols = {c.lower(): c for c in df.columns}
    for bad in PROHIBITED_COLUMNS & set(lower_cols.keys()):
        findings.append(f"{filename}: prohibited column '{lower_cols[bad]}'")

    for col in df.select_dtypes(include=["object"]).columns:
        series = df[col].dropna().astype(str)
        for label, pattern in PII_PATTERNS.items():
            if series.str.contains(pattern, regex=True).any():
                findings.append(f"{filename} col '{col}': matched {label} pattern")
    return findings


def review_directory(data_dir: Path) -> Dict[str, List[str]]:
    """Run privacy review across all CSV files in target directory."""
    findings: Dict[str, List[str]] = {}
    for csv_file in sorted(data_dir.glob("*.csv")):
        df = pd.read_csv(csv_file, dtype=object)
        findings[csv_file.name] = scan_dataframe_for_pii(df, csv_file.name)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Run PII and privacy review on CSV datasets.")
    parser.add_argument("--data-dir", default="data/synthetic")
    args = parser.parse_args()

    results = review_directory(Path(args.data_dir))
    total = sum(len(v) for v in results.values())
    for name, issues in results.items():
        print(f"[{'PASS' if not issues else 'FAIL'}] {name}")
        for issue in issues:
            print(f"  - {issue}")
    return 1 if total > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
