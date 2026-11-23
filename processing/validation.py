"""Schema and data quality validation for Justice for UMKM Observatory datasets."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List

import jsonschema
import pandas as pd


SCHEMA_MAP = {
    "ds01_umkm_legal_disputes.csv": "judicial_dispute_schema.json",
    "ds05_umkm_economic_indicators.csv": "economic_indicator_schema.json",
    "ds06_legal_information_access.csv": "legal_access_schema.json",
    "ds07_umkm_dispute_survey.csv": "survey_schema.json",
    "ds09_legal_information_register.csv": "legal_register_schema.json",
}


def validate_csv_against_schema(csv_path: Path, schema_path: Path) -> List[str]:
    """Validate every row of a CSV file against its JSON Schema."""
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors: List[str] = []
    df = pd.read_csv(csv_path, dtype=object)
    records = df.where(pd.notnull(df), None).to_dict(orient="records")

    float_fields = {
        k for k, v in schema.get("properties", {}).items()
        if "number" in (v.get("type") if isinstance(v.get("type"), list) else [v.get("type")])
    }
    int_fields = {
        k for k, v in schema.get("properties", {}).items()
        if "integer" in (v.get("type") if isinstance(v.get("type"), list) else [v.get("type")])
    }

    for idx, rec in enumerate(records, start=1):
        for ff in float_fields:
            if rec.get(ff) is not None:
                try:
                    rec[ff] = float(rec[ff])
                except (TypeError, ValueError):
                    pass
        for inf in int_fields:
            if rec.get(inf) is not None:
                try:
                    rec[inf] = int(float(rec[inf]))
                except (TypeError, ValueError):
                    pass
        try:
            jsonschema.validate(instance=rec, schema=schema)
        except jsonschema.ValidationError as exc:
            errors.append(f"{csv_path.name} row {idx}: {exc.message}")
    return errors


def validate_directory(data_dir: Path, schemas_dir: Path) -> Dict[str, List[str]]:
    """Validate all mapped CSV datasets in a directory."""
    report: Dict[str, List[str]] = {}
    for filename, schema_name in SCHEMA_MAP.items():
        csv_file = data_dir / filename
        schema_file = schemas_dir / schema_name
        if csv_file.exists() and schema_file.exists():
            report[filename] = validate_csv_against_schema(csv_file, schema_file)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Observatory CSVs against JSON schemas.")
    parser.add_argument("--data-dir", default="data/synthetic")
    parser.add_argument("--schemas-dir", default="schemas")
    args = parser.parse_args()

    results = validate_directory(Path(args.data_dir), Path(args.schemas_dir))
    total_errors = sum(len(errs) for errs in results.values())
    for name, errs in results.items():
        status = "PASS" if not errs else f"FAIL ({len(errs)} errors)"
        print(f"[{status}] {name}")
        for err in errs[:5]:
            print(f"  - {err}")
    return 1 if total_errors > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
