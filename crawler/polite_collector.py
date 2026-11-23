"""Polite, rate-limited, robots.txt-compliant collector.

Never bypasses authentication, CAPTCHA, WAF challenges, or rate limits.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests

from crawler.provenance import compute_sha256, record_provenance


USER_AGENT = "JusticeForUMKMObservatory/1.0 (+https://github.com/bsdkijc-dev/justice-for-umkm-observatory)"
MIN_DELAY_SECONDS = 3.0
STOP_STATUS_CODES = {401, 403, 407, 429, 451}


@dataclass
class FetchResult:
    url: str
    status: str  # "ok", "blocked_robots", "restricted_http", "error"
    status_code: Optional[int]
    document_hash: Optional[str]
    cache_path: Optional[Path]
    message: str


class PoliteCollector:
    """Rate-limited HTTP collector with robots.txt enforcement and local caching."""

    def __init__(
        self,
        cache_dir: str | Path = "data/raw/cache",
        provenance_log: str | Path = "data/raw/provenance.jsonl",
        min_delay: float = MIN_DELAY_SECONDS,
        max_retries: int = 2,
    ) -> None:
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.provenance_log = Path(provenance_log)
        self.min_delay = max(min_delay, MIN_DELAY_SECONDS)
        self.max_retries = max_retries
        self._last_request_ts: float = 0.0
        self._robots_cache: dict[str, RobotFileParser] = {}
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def _respect_delay(self) -> None:
        elapsed = time.monotonic() - self._last_request_ts
        if elapsed < self.min_delay:
            time.sleep(self.min_delay - elapsed)
        self._last_request_ts = time.monotonic()

    def can_fetch(self, url: str) -> bool:
        """Check robots.txt for the target URL; return False if disallowed or unreachable."""
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        if base not in self._robots_cache:
            rp = RobotFileParser()
            robots_url = f"{base}/robots.txt"
            try:
                resp = self.session.get(robots_url, timeout=10)
                if resp.status_code == 200:
                    rp.parse(resp.text.splitlines())
                else:
                    return False
            except requests.RequestException:
                return False
            self._robots_cache[base] = rp
        return self._robots_cache[base].can_fetch(USER_AGENT, url)

    def fetch(self, source_id: str, url: str) -> FetchResult:
        """Fetch a URL politely, stopping immediately on restrictions or instability."""
        if not self.can_fetch(url):
            return FetchResult(url, "blocked_robots", None, None, None, "Disallowed or unreachable robots.txt")

        for attempt in range(self.max_retries + 1):
            self._respect_delay()
            try:
                resp = self.session.get(url, timeout=15)
            except requests.RequestException as exc:
                if attempt < self.max_retries:
                    time.sleep(self.min_delay * (2 ** attempt))
                    continue
                return FetchResult(url, "error", None, None, None, f"Network error: {exc}")

            if resp.status_code in STOP_STATUS_CODES:
                return FetchResult(
                    url,
                    "restricted_http",
                    resp.status_code,
                    None,
                    None,
                    f"Stopped immediately due to HTTP {resp.status_code} access restriction.",
                )

            if resp.status_code >= 500:
                if attempt < self.max_retries:
                    time.sleep(self.min_delay * (2 ** attempt))
                    continue
                return FetchResult(url, "error", resp.status_code, None, None, f"Server error HTTP {resp.status_code}")

            if resp.status_code == 200:
                doc_hash = compute_sha256(resp.content)
                out_file = self.cache_dir / f"{source_id}_{doc_hash[:16]}.bin"
                out_file.write_bytes(resp.content)
                record_provenance(self.provenance_log, source_id, url, 200, doc_hash)
                return FetchResult(url, "ok", 200, doc_hash, out_file, "Cached successfully")

            return FetchResult(url, "error", resp.status_code, None, None, f"Unexpected HTTP {resp.status_code}")

        return FetchResult(url, "error", None, None, None, "Max retries exceeded")
