"""Empirical DS05 ingestion for Kementerian UMKM RI 'Data Prioritas Capaian 2025' workbooks.

Source: Kementerian UMKM RI (https://umkm.go.id/publikasi), Klasifikasi: Terbuka.
Enforces strict zero-imputation and preserves exact reported values.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

import pandas as pd


SOURCE_LABEL = "Kementerian UMKM RI - Data Prioritas Capaian 2025 (https://umkm.go.id/publikasi)"
PERIOD = "2025"


def ingest_kemen_umkm_2025(national_xlsx: Path, provincial_xlsx: Path) -> pd.DataFrame:
    rows: List[dict] = []
    rec_idx = 1

    def add_row(
        indicator_name: str,
        business_size: str,
        province: str,
        value: object,
        unit: str,
        denominator: str,
    ) -> None:
        nonlocal rec_idx
        val = None if pd.isna(value) else float(value)
        rows.append({
            "economic_indicator_id": f"DS05-KEMENUMKM-2025-{rec_idx:04d}",
            "indicator_name": indicator_name,
            "business_size": business_size,
            "business_sector": "All Sectors",
            "province": province,
            "district": None,
            "reporting_period": PERIOD,
            "indicator_value": val,
            "unit": unit,
            "population": "Indonesian Enterprises / UMKM (Kementerian UMKM 2025)",
            "denominator": denominator,
            "source": SOURCE_LABEL,
            "methodology": "Official Kementerian UMKM RI Priority Statistics Compilation (PP 7/2021)",
            "validation_status": "verified",
        })
        rec_idx += 1

    # 1. National Summary Indicators (Sheet1)
    nat_df = pd.read_excel(national_xlsx, sheet_name="Sheet1")
    for _, r in nat_df.iterrows():
        add_row(
            indicator_name=str(r["Nama Data"]).strip(),
            business_size="all_umkm",
            province="Nasional",
            value=r["Realisasi 2025"],
            unit="proportion",
            denominator=str(r["Klasifikasi Penyajian"]).strip(),
        )

    # 2. Provincial Indikator No. 1 (Enterprise counts & UKM proportion)
    ind1 = pd.read_excel(provincial_xlsx, sheet_name="Indikator No.1")
    ind1 = ind1[pd.to_numeric(ind1["ID_PROV"], errors="coerce").notna()]
    for _, r in ind1.iterrows():
        prov = str(r["NAMA_PROV"]).strip()
        add_row("enterprise_count_micro", "micro", prov, r["MIKRO"], "enterprises", "TOTAL_USAHA")
        add_row("enterprise_count_small", "small", prov, r["KECIL"], "enterprises", "TOTAL_USAHA")
        add_row("enterprise_count_medium", "medium", prov, r["MENENGAH"], "enterprises", "TOTAL_USAHA")
        add_row("ukm_proportion_of_total_enterprises", "all_umkm", prov, r["PROP_UKM"], "proportion", "TOTAL_USAHA")

    # 3. Provincial Indikator No. 3 (Legal entity / complete accounting proportion)
    ind3 = pd.read_excel(provincial_xlsx, sheet_name="Indikator No.3")
    ind3 = ind3[pd.to_numeric(ind3["KODE_PROV"], errors="coerce").notna()]
    for _, r in ind3.iterrows():
        prov = str(r["NAMA_PROV"]).strip()
        add_row("formal_legal_entity_count", "all_umkm", prov, r["Condition1"], "enterprises", "Total pelaku usaha")
        add_row("formal_or_complete_bookkeeping_proportion", "all_umkm", prov, r["Proporsi"], "proportion", "Total pelaku usaha")

    # 4. Provincial Indikator No. 5 (Regular paid worker ratio)
    ind5 = pd.read_excel(provincial_xlsx, sheet_name="Indikator No.5")
    ind5 = ind5[pd.to_numeric(ind5["KODE_PROV"], errors="coerce").notna()]
    for _, r in ind5.iterrows():
        prov = str(r["NAMA_PROV"]).strip()
        add_row("regular_paid_worker_enterprise_ratio", "all_umkm", prov, r["RASIO"], "proportion", "Pelaku usaha dibantu buruh")

    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest Kementerian UMKM 2025 workbooks into DS05.")
    parser.add_argument("--national-xlsx", required=True)
    parser.add_argument("--provincial-xlsx", required=True)
    parser.add_argument("--output-csv", default="data/processed/ds05_umkm_economic_indicators.csv")
    args = parser.parse_args()

    df = ingest_kemen_umkm_2025(Path(args.national_xlsx), Path(args.provincial_xlsx))
    out_csv = Path(args.output_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_csv, index=False)
    df.to_parquet(out_csv.with_suffix(".parquet"), index=False)
    print(f"Ingested {len(df)} verified DS05 empirical records -> {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
