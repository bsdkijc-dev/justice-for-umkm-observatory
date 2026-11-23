"""Generate deterministic synthetic test datasets (DS01-DS10) for pipeline & CI testing.

SYNTHETIC DATA ONLY: Never use or cite synthetic records as empirical findings.
"""

from __future__ import annotations

import hashlib
import random
from pathlib import Path

import pandas as pd


PROVINCES = [
    ("DKI Jakarta", "Jakarta Pusat"),
    ("Jawa Barat", "Kota Bandung"),
    ("Jawa Tengah", "Kota Semarang"),
    ("Jawa Timur", "Kota Surabaya"),
    ("DI Yogyakarta", "Kabupaten Sleman"),
    ("Sumatera Utara", "Kota Medan"),
    ("Sulawesi Selatan", "Kota Makassar"),
    ("Bali", "Kota Denpasar"),
]

CATEGORIES = ["CAT-01", "CAT-02", "CAT-03", "CAT-04", "CAT-05", "CAT-06", "CAT-07", "CAT-08", "UNKNOWN"]
SIZES = ["micro", "small", "medium", "unknown"]
SECTORS = ["Food & Beverage", "Retail Trade", "Manufacturing", "Digital Services", "Agriculture"]


def generate_all(out_dir: Path, seed: int = 2027) -> None:
    rng = random.Random(seed)
    out_dir.mkdir(parents=True, exist_ok=True)

    # DS01: UMKM Legal Dispute Metadata (120 synthetic records)
    ds01_rows = []
    for i in range(1, 121):
        prov, dist = rng.choice(PROVINCES)
        cat = rng.choice(CATEGORIES)
        size = rng.choices(SIZES, weights=[0.4, 0.3, 0.1, 0.2])[0]
        doc_hash = hashlib.sha256(f"SYNTH-DS01-{i}".encode()).hexdigest()
        ds01_rows.append({
            "record_id": f"SYNTH-DS01-{i:04d}",
            "case_number": f"{100 + i}/Pdt.G.S/2025/PN.Sby",
            "court_name": f"Pengadilan Negeri {dist}",
            "court_level": rng.choice(["first_instance", "appellate", "commercial"]),
            "decision_date": f"2025-{rng.randint(1, 12):02d}-{rng.randint(1, 28):02d}",
            "publication_date": f"2026-{rng.randint(1, 10):02d}-{rng.randint(1, 28):02d}",
            "dispute_category": cat,
            "dispute_subcategory": "synthetic_subcategory",
            "claimant_type": rng.choice(["micro_enterprise", "small_enterprise", "financial_institution", "unknown"]),
            "defendant_type": rng.choice(["micro_enterprise", "small_enterprise", "medium_enterprise", "unknown"]),
            "business_size": size,
            "business_sector": rng.choice(SECTORS),
            "province": prov,
            "district": dist,
            "claim_type": rng.choice(["gugatan_sederhana", "wanprestasi", "pmh", "pkpu"]),
            "judgment_outcome": rng.choice(["granted", "partially_granted", "rejected", "settled"]),
            "remedy_type": rng.choice(["monetary_compensation", "contract_performance", "none"]),
            "appeal_status": rng.choice(["final", "objection_filed", "cassation"]),
            "execution_status": rng.choice(["unknown", "voluntary_compliance", "pending_execution", "unenforced"]),
            "source_url": f"https://putusan3.mahkamahagung.go.id/synthetic/{i}",
            "retrieval_date": "2026-11-23",
            "document_hash": doc_hash,
            "extraction_confidence": round(rng.uniform(0.55, 0.95), 2),
            "validation_status": "synthetic",
        })
    pd.DataFrame(ds01_rows).to_csv(out_dir / "ds01_umkm_legal_disputes.csv", index=False)

    # DS02: UMKM Legal Access Barriers
    ds02_rows = [
        {
            "barrier_id": f"SYNTH-DS02-{i:03d}",
            "barrier_category": rng.choice(["cost", "information", "distance", "complexity", "trust"]),
            "business_size": rng.choice(["micro", "small", "medium"]),
            "business_sector": rng.choice(SECTORS),
            "geographic_area": rng.choice(["urban", "rural"]),
            "barrier_description": "Synthetic barrier record for pipeline testing",
            "evidence_type": "synthetic",
            "source": "synthetic_test_generator",
            "reporting_period": "2025",
            "validation_status": "synthetic",
        }
        for i in range(1, 31)
    ]
    pd.DataFrame(ds02_rows).to_csv(out_dir / "ds02_umkm_access_barriers.csv", index=False)

    # DS03: Dispute Resolution Costs
    ds03_rows = [
        {
            "observation_id": f"SYNTH-DS03-{i:03d}",
            "business_size": rng.choice(["micro", "small", "medium"]),
            "dispute_category": rng.choice(CATEGORIES[:8]),
            "resolution_channel": rng.choice(["negotiation", "mediation", "small_claims_court", "general_court"]),
            "direct_cost": rng.randint(250_000, 25_000_000),
            "indirect_cost": rng.randint(500_000, 15_000_000),
            "currency": "IDR",
            "observation_period": "2025",
            "methodology": "synthetic_test",
            "sample_size": rng.randint(10, 50),
            "source": "synthetic_test_generator",
            "validation_status": "synthetic",
        }
        for i in range(1, 41)
    ]
    pd.DataFrame(ds03_rows).to_csv(out_dir / "ds03_dispute_resolution_costs.csv", index=False)

    # DS04: Dispute Duration
    ds04_rows = [
        {
            "observation_id": f"SYNTH-DS04-{i:03d}",
            "dispute_category": rng.choice(CATEGORIES[:8]),
            "resolution_channel": rng.choice(["negotiation", "mediation", "small_claims_court", "general_court"]),
            "start_date": "2025-01-15",
            "end_date": "2025-04-20",
            "duration_days": rng.randint(14, 365),
            "measurement_method": "synthetic_filing_to_disposition",
            "source": "synthetic_test_generator",
            "validation_status": "synthetic",
        }
        for i in range(1, 41)
    ]
    pd.DataFrame(ds04_rows).to_csv(out_dir / "ds04_dispute_duration.csv", index=False)

    # DS05: UMKM Economic Indicators
    ds05_rows = [
        {
            "economic_indicator_id": f"SYNTH-DS05-{i:03d}",
            "indicator_name": rng.choice(["active_umkm_count", "umkm_credit_npl_pct", "formal_nib_share_pct"]),
            "business_size": rng.choice(["micro", "small", "medium", "all_umkm"]),
            "business_sector": rng.choice(SECTORS),
            "province": prov,
            "district": dist,
            "reporting_period": "2025",
            "indicator_value": round(rng.uniform(1.5, 95.0), 2),
            "unit": "percent",
            "population": "synthetic_umkm_population",
            "denominator": "synthetic_total",
            "source": "synthetic_test_generator",
            "methodology": "synthetic_test",
            "validation_status": "synthetic",
        }
        for i, (prov, dist) in enumerate(PROVINCES * 3, start=1)
    ]
    pd.DataFrame(ds05_rows).to_csv(out_dir / "ds05_umkm_economic_indicators.csv", index=False)

    # DS06: Legal Information Access
    ds06_rows = [
        {
            "access_id": f"SYNTH-DS06-{i:03d}",
            "information_type": rng.choice(["contract_template", "small_claims_guide", "legal_aid_directory", "oss_licensing"]),
            "provider": rng.choice(["BPHN", "Mahkamah Agung", "Kementerian UMKM", "OSS"]),
            "geographic_coverage": "National",
            "language": "Indonesian",
            "digital_channel": rng.choice(["web", "mobile_web", "in_person"]),
            "accessibility_features": "plain_language;free_access",
            "last_verified": "2026-11-23",
            "source": "https://umkm.go.id",
            "validation_status": "synthetic",
        }
        for i in range(1, 17)
    ]
    pd.DataFrame(ds06_rows).to_csv(out_dir / "ds06_legal_information_access.csv", index=False)

    # DS07: UMKM Dispute Experience Survey (100 synthetic respondents, zero PII)
    ds07_rows = []
    for i in range(1, 101):
        prov, dist = rng.choice(PROVINCES)
        has_dispute = rng.choices(["yes", "no"], weights=[0.65, 0.35])[0]
        ds07_rows.append({
            "respondent_code": f"RESP-SYNTH-{i:04d}",
            "business_size": rng.choices(["micro", "small", "medium"], weights=[0.55, 0.35, 0.10])[0],
            "business_sector": rng.choice(SECTORS),
            "province": prov,
            "district": dist,
            "business_age_group": rng.choice(["<1_year", "1_to_3_years", "3_to_5_years", "5_to_10_years", ">10_years"]),
            "dispute_experience": has_dispute,
            "dispute_category": rng.choice(CATEGORIES[:8]) if has_dispute == "yes" else "none",
            "resolution_channel": rng.choice(["negotiation", "mediation", "small_claims_court", "abandoned_unresolved"]) if has_dispute == "yes" else "none",
            "estimated_cost_band": rng.choice(["<1M_IDR", "1M_to_5M_IDR", "5M_to_25M_IDR"]) if has_dispute == "yes" else "not_applicable",
            "estimated_duration_band": rng.choice(["<1_month", "1_to_3_months", "3_to_6_months", ">12_months"]) if has_dispute == "yes" else "not_applicable",
            "business_impact": rng.choice(["minor_delay", "cash_flow_pressure", "temporary_halt"]) if has_dispute == "yes" else "none",
            "outcome_category": rng.choice(["settled_voluntarily", "judgment_enforced", "judgment_unenforced", "abandoned"]) if has_dispute == "yes" else "not_applicable",
            "consent_status": "consented_public_aggregate",
            "survey_date": "2026-11-23",
        })
    pd.DataFrame(ds07_rows).to_csv(out_dir / "ds07_umkm_dispute_survey.csv", index=False)

    # DS08: Data Quality Register
    pd.DataFrame([
        {
            "record_id": "SYNTH-QA-001",
            "dataset_name": "ds01_umkm_legal_disputes.csv",
            "source": "synthetic_test_generator",
            "missing_fields": "",
            "duplicate_status": "unique",
            "validation_status": "synthetic",
            "review_date": "2026-11-23",
            "reviewer": "DATA VALIDATION AGENT",
            "correction_notes": "Synthetic validation baseline",
        }
    ]).to_csv(out_dir / "ds08_data_quality_register.csv", index=False)

    # DS09: Legal Information Register (real verified statutory entries)
    pd.DataFrame([
        {
            "legal_source_id": "LEG-001",
            "regulation_number": "7",
            "regulation_year": 2021,
            "title": "PP Nomor 7 Tahun 2021 tentang Kemudahan, Pelindungan, dan Pemberdayaan Koperasi dan UMKM",
            "legal_topic": "UMKM Classification & Empowerment",
            "effective_date": "2021-02-02",
            "current_status": "active",
            "official_source": "JDIH BPK",
            "source_url": "https://peraturan.bpk.go.id/Details/161837/pp-no-7-tahun-2021",
            "verification_status": "verified",
        },
        {
            "legal_source_id": "LEG-002",
            "regulation_number": "4",
            "regulation_year": 2019,
            "title": "PERMA Nomor 4 Tahun 2019 tentang Perubahan atas PERMA 2/2015 Tata Cara Penyelesaian Gugatan Sederhana",
            "legal_topic": "Small Claims Court (max IDR 500M)",
            "effective_date": "2019-08-20",
            "current_status": "active",
            "official_source": "JDIH BPK / Mahkamah Agung",
            "source_url": "https://peraturan.bpk.go.id/Details/206070/perma-no-4-tahun-2019",
            "verification_status": "verified",
        },
        {
            "legal_source_id": "LEG-003",
            "regulation_number": "1",
            "regulation_year": 2016,
            "title": "PERMA Nomor 1 Tahun 2016 tentang Prosedur Mediasi di Pengadilan",
            "legal_topic": "Court-Annexed Mediation",
            "effective_date": "2016-02-04",
            "current_status": "active",
            "official_source": "JDIH BPK / Mahkamah Agung",
            "source_url": "https://peraturan.bpk.go.id/Details/209641/perma-no-1-tahun-2016",
            "verification_status": "verified",
        },
    ]).to_csv(out_dir / "ds09_legal_information_register.csv", index=False)

    # DS10: Policy Recommendations (draft candidates)
    pd.DataFrame([
        {
            "recommendation_id": "POL-DRAFT-001",
            "research_question": "RQ12",
            "evidence_base": "Pending empirical validation (DS01, DS06, DS07)",
            "identified_barrier": "Limited plain-language commercial contract templates for micro enterprises",
            "proposed_intervention": "Publish standardized Bahasa Indonesia B2B & invoice templates via Kementerian UMKM & OSS",
            "responsible_policy_area": "Kementerian UMKM RI",
            "expected_outcome": "Reduced avoidable contract ambiguity and payment disputes",
            "evaluation_method": "Pre/post uptake and dispute incidence tracking",
            "limitations": "Templates require local business association outreach for informal MSEs",
            "review_status": "draft",
        }
    ]).to_csv(out_dir / "ds10_policy_recommendations.csv", index=False)

    # Also export Parquet equivalents for DuckDB / PyArrow pipelines
    for csv_file in out_dir.glob("*.csv"):
        df = pd.read_csv(csv_file)
        df.to_parquet(csv_file.with_suffix(".parquet"), index=False)


if __name__ == "__main__":
    generate_all(Path("data/synthetic"))
    print("Generated DS01-DS10 synthetic CSV and Parquet files in data/synthetic/")
