"""SHA-256 provenance and audit logger for retrieved documents."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


def compute_sha256(content: bytes) -> str:
    """Compute SHA-256 hex digest for raw retrieved bytes."""
    return hashlib.sha256(content).hexdigest()


def record_provenance(
    log_path: str | Path,
    source_id: str,
    url: str,
    status_code: int,
    content_hash: str,
    notes: str = "",
) -> Dict[str, Any]:
    """Append a structured JSONL provenance entry."""
    entry = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_id": source_id,
        "url": url,
        "status_code": status_code,
        "document_hash": content_hash,
        "notes": notes,
    }
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry
