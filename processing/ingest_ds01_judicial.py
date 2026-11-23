"""DS01 Judicial Dispute Metadata ingestion & normalization pipeline.

Reads raw permitted judgment metadata records (JSON/JSONL/CSV) from data/raw/judicial/,
enforces PP 7/2021 statutory classification (never inferring size from case titles),
applies the 8-category dispute taxonomy, deduplicates, and writes validated DS01 outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from processing.deduplication import deduplicate_records
from processing.document_extraction import extract_dispute_metadata
from processing.normalization import normalize_province_name


DS01_COLUMNS = [
    "record_id", "case_number", "court_name", "court_level",
    "decision_date", "publication_date", "dispute_category",
    "dispute_subcategory", "claimant_type", "defendant_type",
    "business_size", "business_sector", "province", "district",
    "claim_type", "judgment_outcome", "remedy_type",
    "appeal_status", "execution_status", "source_url",
    "retrieval_date", "document_hash", "extraction_confidence",
    "validation_status",
]


def normalize_judicial_record(raw: Dict[str, Any], idx: int) -> Dict[str, Any]:
    """Normalize a raw judicial metadata dict into the DS01 schema."""
    extracted = extract_dispute_metadata(raw)
    payload_bytes = json.dumps(raw, sort_keys=True, ensure_ascii=False).encode("utf-8")
    doc_hash = raw.get("document_hash") or hashlib.sha256(payload_bytes).hexdigest()

    return {
        "record_id": raw.get("record_id") or f"DS01-JUD-{idx:06d}",
        "case_number": extracted["case_number"] or str(raw.get("case_number", "")).strip(),
        "court_name": str(raw.get("court_name") or "unknown").strip(),
        "court_level": raw.get("court_level") or "unknown",
        "decision_date": raw.get("decision_date") or None,
        "publication_date": raw.get("publication_date") or None,
        "dispute_category": extracted["dispute_category"],
        "dispute_subcategory": raw.get("dispute_subcategory") or "",
        "claimant_type": raw.get("claimant_type") or "unknown",
        "defendant_type": raw.get("defendant_type") or "unknown",
        "business_size": extracted["business_size"],
        "business_sector": raw.get("business_sector") or "",
        "province": normalize_province_name(raw.get("province")) or "",
        "district": str(raw.get("district") or "").strip(),
        "claim_type": str(raw.get("claim_type") or "").strip(),
        "judgment_outcome": str(raw.get("judgment_outcome") or "").strip(),
        "remedy_type": str(raw.get("remedy_type") or "").strip(),
        "appeal_status": str(raw.get("appeal_status") or "").strip(),
        "execution_status": str(raw.get("execution_status") or "unknown").strip(),
        "source_url": str(raw.get("source_url") or "https://putusan3.mahkamahagung.go.id").strip(),
        "retrieval_date": raw.get("retrieval_date") or date.today().isoformat(),
        "document_hash": doc_hash,
        "extraction_confidence": extracted["extraction_confidence"],
        "validation_status": raw.get("validation_status") or "provisional",
    }


def ingest_judicial_jsonl(input_path: Path, output_csv: Path) -> pd.DataFrame:
    """Ingest a JSONL file of raw judicial metadata into DS01 CSV + Parquet."""
    records: List[Dict[str, Any]] = []
    with input_path.open("r", encoding="utf-8") as fh:
        for idx, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            records.append(normalize_judicial_record(json.loads(line), idx))

    df = pd.DataFrame(records, columns=DS01_COLUMNS)
    deduped, _ = deduplicate_records(df, subset_cols=["case_number", "court_name"])
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    deduped.to_csv(output_csv, index=False)
    deduped.to_parquet(output_csv.with_suffix(".parquet"), index=False)
    return deduped


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest raw judicial metadata JSONL into DS01.")
    parser.add_argument("--input", required=True, help="Path to raw JSONL file")
    parser.add_argument("--output", default="data/processed/ds01_umkm_legal_disputes.csv")
    args = parser.parse_args()

    out_df = ingest_judicial_jsonl(Path(args.input), Path(args.output))
    print(f"Ingested {len(out_df)} DS01 judicial records -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
