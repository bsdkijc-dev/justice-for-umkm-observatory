"""Source discovery registry loader for Justice for UMKM Observatory."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List


def load_official_sources(sources_csv: str | Path) -> List[Dict[str, str]]:
    """Load verified official source records from sources/official_sources.csv."""
    path = Path(sources_csv)
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def filter_automated_permitted(
    sources: List[Dict[str, str]], coverage_csv: str | Path
) -> List[Dict[str, str]]:
    """Return only sources where automated collection is explicitly permitted or conditional."""
    cov_path = Path(coverage_csv)
    with cov_path.open("r", encoding="utf-8", newline="") as fh:
        cov_map = {row["source_id"]: row for row in csv.DictReader(fh)}
    eligible: List[Dict[str, str]] = []
    for src in sources:
        cov = cov_map.get(src["source_id"], {})
        if cov.get("automated_collection_permitted") in {"yes_via_api", "conditional"}:
            eligible.append({**src, **cov})
    return eligible
