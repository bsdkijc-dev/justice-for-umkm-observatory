"""Normalization helpers enforcing zero-imputation and pure numeric formatting."""

from __future__ import annotations

import re
from typing import Optional


def normalize_idr_numeric(value: object) -> Optional[float]:
    """Parse IDR currency strings into pure numeric floats; return None when missing (never 0)."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text or text.lower() in {"nan", "none", "null", "na", "-"}:
        return None
    cleaned = re.sub(r"(?i)rp\.?|idr|\s", "", text)
    # Handle Indonesian thousand-separator dots when no decimal comma is present
    if "," in cleaned:
        cleaned = cleaned.replace(".", "").replace(",", ".")
    elif cleaned.count(".") > 1 or (cleaned.count(".") == 1 and len(cleaned.split(".")[1]) == 3):
        cleaned = cleaned.replace(".", "")
    try:
        return float(cleaned)
    except ValueError:
        return None


def normalize_province_name(name: Optional[str]) -> Optional[str]:
    """Standardize Indonesian province names while preserving None."""
    if not name or not str(name).strip():
        return None
    cleaned = " ".join(str(name).strip().split())
    aliases = {
        "DKI Jakarta": "DKI Jakarta",
        "Jakarta": "DKI Jakarta",
        "DIY": "DI Yogyakarta",
        "DI Yogyakarta": "DI Yogyakarta",
        "Jabar": "Jawa Barat",
        "Jateng": "Jawa Tengah",
        "Jatim": "Jawa Timur",
    }
    return aliases.get(cleaned, cleaned.title())
