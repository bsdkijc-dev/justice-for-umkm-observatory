"""Statutory UMKM classification (PP No. 7 Tahun 2021 Pasal 35) & Dispute Taxonomy."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


# PP Nomor 7 Tahun 2021 Pasal 35 thresholds (in IDR)
MICRO_MAX_CAPITAL_IDR = 1_000_000_000
SMALL_MAX_CAPITAL_IDR = 5_000_000_000
MEDIUM_MAX_CAPITAL_IDR = 10_000_000_000

MICRO_MAX_SALES_IDR = 2_000_000_000
SMALL_MAX_SALES_IDR = 15_000_000_000
MEDIUM_MAX_SALES_IDR = 50_000_000_000

TAXONOMY_CATEGORIES: Dict[str, Dict[str, object]] = {
    "CAT-01": {
        "name": "Commercial Contracts",
        "keywords": ["wanprestasi", "invoice", "tagihan", "kontrak", "supplier", "distributor", "perjanjian kerja sama", "breach of contract"],
        "exclusions": ["hubungan industrial", "phk", "konsumen akhir"],
    },
    "CAT-02": {
        "name": "Financial and Credit Disputes",
        "keywords": ["kredit", "kur", "pembiayaan", "pinjaman", "fidusia", "hak tanggungan", "jaminan", "fintech", "perbankan", "lelang agunan"],
        "exclusions": ["kepailitan", "pkpu"],
    },
    "CAT-03": {
        "name": "Land and Property",
        "keywords": ["sewa", "ruko", "kios", "tanah", "bangunan", "tempat usaha", "sertifikat hak milik", "pengosongan"],
        "exclusions": [],
    },
    "CAT-04": {
        "name": "Consumer and Marketplace",
        "keywords": ["konsumen", "bpsk", "e-commerce", "marketplace", "refund", "pengembalian dana", "cacat produk", "perlindungan konsumen"],
        "exclusions": [],
    },
    "CAT-05": {
        "name": "Employment",
        "keywords": ["upah", "phk", "pesangon", "bpjs ketenagakerjaan", "hubungan industrial", "pekerja", "buruh"],
        "exclusions": ["kontrak b2b"],
    },
    "CAT-06": {
        "name": "Administrative and Regulatory",
        "keywords": ["nib", "oss", "perizinan", "pajak", "retribusi", "tata usaha negara", "ptun", "sanksi administratif"],
        "exclusions": [],
    },
    "CAT-07": {
        "name": "Intellectual Property",
        "keywords": ["merek", "hak cipta", "paten", "desain industri", "pelanggaran merek", "lisensi merek"],
        "exclusions": [],
    },
    "CAT-08": {
        "name": "Insolvency and Business Failure",
        "keywords": ["pkpu", "pailit", "kepailitan", "kurator", "pengadilan niaga", "penundaan kewajiban pembayaran utang"],
        "exclusions": [],
    },
}


def classify_enterprise_pp7_2021(
    business_capital_idr: Optional[float] = None,
    annual_sales_idr: Optional[float] = None,
) -> str:
    """Classify enterprise size strictly under PP No. 7 Tahun 2021 Pasal 35.

    Never infers size from a case title. Returns 'unknown' if evidence is absent.
    """
    if business_capital_idr is not None and business_capital_idr > 0:
        if business_capital_idr <= MICRO_MAX_CAPITAL_IDR:
            return "micro"
        if business_capital_idr <= SMALL_MAX_CAPITAL_IDR:
            return "small"
        if business_capital_idr <= MEDIUM_MAX_CAPITAL_IDR:
            return "medium"
        return "unknown"

    if annual_sales_idr is not None and annual_sales_idr > 0:
        if annual_sales_idr <= MICRO_MAX_SALES_IDR:
            return "micro"
        if annual_sales_idr <= SMALL_MAX_SALES_IDR:
            return "small"
        if annual_sales_idr <= MEDIUM_MAX_SALES_IDR:
            return "medium"
        return "unknown"

    return "unknown"


@dataclass
class TaxonomyClassification:
    categories: List[str]
    confidence: float
    matched_terms: List[str]


def classify_dispute_text(text: str, min_confidence: float = 0.5) -> TaxonomyClassification:
    """Assign one or more dispute categories based on documented keyword rules, preserving UNKNOWN."""
    normalized = (text or "").lower()
    scores: List[Tuple[str, int, List[str]]] = []

    for code, spec in TAXONOMY_CATEGORIES.items():
        hits = [kw for kw in spec["keywords"] if kw in normalized]
        excluded = any(ex in normalized for ex in spec["exclusions"])
        if hits and not excluded:
            scores.append((code, len(hits), hits))

    if not scores:
        return TaxonomyClassification(categories=["UNKNOWN"], confidence=0.0, matched_terms=[])

    scores.sort(key=lambda item: item[1], reverse=True)
    top_hits = scores[0][1]
    confidence = min(0.5 + 0.15 * top_hits, 0.95)
    if confidence < min_confidence:
        return TaxonomyClassification(categories=["UNKNOWN"], confidence=confidence, matched_terms=[])

    selected = [code for code, _, _ in scores]
    all_terms = [term for _, _, terms in scores for term in terms]
    return TaxonomyClassification(categories=selected, confidence=round(confidence, 2), matched_terms=sorted(set(all_terms)))
