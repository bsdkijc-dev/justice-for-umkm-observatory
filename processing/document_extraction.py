"""Document metadata extraction helpers (no size inference from title alone)."""

from __future__ import annotations

import re
from typing import Any, Dict

from processing.taxonomy import classify_dispute_text, classify_enterprise_pp7_2021


CASE_NUM_RE = re.compile(r"\b\d+/[A-Za-z.\-]+/\d{4}/[A-Za-z.\s]+\b")


def extract_dispute_metadata(raw_record: Dict[str, Any]) -> Dict[str, Any]:
    """Extract normalized judicial dispute metadata without fabricating missing fields."""
    text = f"{raw_record.get('summary_text', '')} {raw_record.get('claim_type', '')}"
    tax = classify_dispute_text(text)

    case_number = raw_record.get("case_number") or ""
    if not case_number and raw_record.get("summary_text"):
        match = CASE_NUM_RE.search(raw_record["summary_text"])
        if match:
            case_number = match.group(0).strip()

    # Strictly require explicit capital or sales evidence; never infer from case title
    business_size = classify_enterprise_pp7_2021(
        business_capital_idr=raw_record.get("verified_capital_idr"),
        annual_sales_idr=raw_record.get("verified_annual_sales_idr"),
    )

    return {
        "case_number": case_number,
        "dispute_category": ";".join(tax.categories),
        "business_size": business_size,
        "extraction_confidence": tax.confidence,
    }
