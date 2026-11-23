"""DS05 Official UMKM Economic Indicators ingestion & harmonization pipeline.

Reads official CSV/XLSX files placed in data/raw/, normalizes numeric values
with strict zero-imputation (missing -> None), and writes validated DS05 output.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

import pandas as pd

from processing.normalization import normalize_idr_numeric, normalize_province_name


DS05_COLUMNS = [
    "economic_indicator_id",
    "indicator_name",
    "business_size",
    "business_sector",
    "province",
    "district",
    "reporting_period",
    "indicator_value",
    "unit",
    "population",
    "denominator",
    "source",
    "methodology",
    "validation_status",
]


def ingest_raw_ds05_csv(
    raw_csv: Path,
    source_label: str,
    reporting_period: str,
    indicator_name: str,
    unit: str,
    business_size: str = "all_umkm",
    population: str = "Indonesian UMKM",
    denominator: str = "total_registered_or_surveyed",
    methodology: str = "official_statistical_compilation",
) -> pd.DataFrame:
    """Ingest an official raw CSV table into the standardized DS05 schema."""
    raw_df = pd.read_csv(raw_csv, dtype=object)
    rows: List[dict] = []
    for idx, row in raw_df.iterrows():
        province = normalize_province_name(row.get("province") or row.get("provinsi"))
        district = row.get("district") or row.get("kabupaten_kota") or None
        sector = row.get("business_sector") or row.get("sektor") or "All Sectors"
        val = normalize_idr_numeric(row.get("indicator_value") or row.get("nilai") or row.get("jumlah"))
        rows.append({
            "economic_indicator_id": f"DS05-OFFICIAL-{idx + 1:05d}",
            "indicator_name": indicator_name,
            "business_size": business_size,
            "business_sector": sector,
            "province": province,
            "district": district,
            "reporting_period": reporting_period,
            "indicator_value": val,
            "unit": unit,
            "population": population,
            "denominator": denominator,
            "source": source_label,
            "methodology": methodology,
            "validation_status": "provisional",
        })
    return pd.DataFrame(rows, columns=DS05_COLUMNS)


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest raw official CSV into DS05 schema.")
    parser.add_argument("--input", required=True, help="Path to raw official CSV in data/raw/")
    parser.add_argument("--output", default="data/processed/ds05_umkm_economic_indicators.csv")
    parser.add_argument("--source", required=True)
    parser.add_argument("--period", required=True)
    parser.add_argument("--indicator", required=True)
    parser.add_argument("--unit", default="count")
    args = parser.parse_args()

    out_df = ingest_raw_ds05_csv(
        raw_csv=Path(args.input),
        source_label=args.source,
        reporting_period=args.period,
        indicator_name=args.indicator,
        unit=args.unit,
    )
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(out_path, index=False)
    out_df.to_parquet(out_path.with_suffix(".parquet"), index=False)
    print(f"Ingested {len(out_df)} DS05 records -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
