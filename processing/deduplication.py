"""Deduplication utilities for judicial and survey datasets."""

from __future__ import annotations

import pandas as pd


def deduplicate_records(df: pd.DataFrame, subset_cols: list[str]) -> tuple[pd.DataFrame, int]:
    """Remove exact duplicates on key columns while returning duplicate count."""
    if df.empty:
        return df.copy(), 0
    before = len(df)
    deduped = df.drop_duplicates(subset=subset_cols, keep="first").reset_index(drop=True)
    return deduped, before - len(deduped)
