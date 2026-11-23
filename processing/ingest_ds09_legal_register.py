"""Populate verified DS09 Legal Information Register from JDIH BPK official records."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


VERIFIED_REGULATIONS = [
    {
        "legal_source_id": "LEG-001",
        "regulation_number": "20",
        "regulation_year": 2008,
        "title": "UU Nomor 20 Tahun 2008 tentang Usaha Mikro, Kecil, dan Menengah",
        "legal_topic": "UMKM Statutory Framework",
        "effective_date": "2008-07-04",
        "current_status": "amended",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/39653/uu-no-20-tahun-2008",
        "verification_status": "verified",
    },
    {
        "legal_source_id": "LEG-002",
        "regulation_number": "6",
        "regulation_year": 2023,
        "title": "UU Nomor 6 Tahun 2023 tentang Penetapan Perppu Nomor 2 Tahun 2022 tentang Cipta Kerja",
        "legal_topic": "Omnibus Job Creation & UMKM Licensing",
        "effective_date": None,
        "current_status": "active",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/246523/uu-no-6-tahun-2023",
        "verification_status": "verified",
    },
    {
        "legal_source_id": "LEG-003",
        "regulation_number": "7",
        "regulation_year": 2021,
        "title": "PP Nomor 7 Tahun 2021 tentang Kemudahan, Pelindungan, dan Pemberdayaan Koperasi dan UMKM",
        "legal_topic": "UMKM Classification (Pasal 35) & Empowerment",
        "effective_date": "2021-02-02",
        "current_status": "active",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/161837/pp-no-7-tahun-2021",
        "verification_status": "verified",
    },
    {
        "legal_source_id": "LEG-004",
        "regulation_number": "196",
        "regulation_year": 2024,
        "title": "Perpres Nomor 196 Tahun 2024 tentang Kementerian Usaha Mikro, Kecil, dan Menengah",
        "legal_topic": "Ministry of UMKM Mandate & Governance",
        "effective_date": "2024-11-08",
        "current_status": "active",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/306943/perpres-no-196-tahun-2024",
        "verification_status": "verified",
    },
    {
        "legal_source_id": "LEG-005",
        "regulation_number": "28",
        "regulation_year": 2025,
        "title": "PP Nomor 28 Tahun 2025 tentang Penyelenggaraan Perizinan Berusaha Berbasis Risiko",
        "legal_topic": "Risk-Based Business Licensing (OSS)",
        "effective_date": None,
        "current_status": "active",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/319773/pp-no-28-tahun-2025",
        "verification_status": "verified",
    },
    {
        "legal_source_id": "LEG-006",
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
        "legal_source_id": "LEG-007",
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
    {
        "legal_source_id": "LEG-008",
        "regulation_number": "30",
        "regulation_year": 1999,
        "title": "UU Nomor 30 Tahun 1999 tentang Arbitrase dan Alternatif Penyelesaian Sengketa",
        "legal_topic": "Arbitration & ADR",
        "effective_date": "1999-08-12",
        "current_status": "active",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/45348/uu-no-30-tahun-1999",
        "verification_status": "verified",
    },
    {
        "legal_source_id": "LEG-009",
        "regulation_number": "8",
        "regulation_year": 1999,
        "title": "UU Nomor 8 Tahun 1999 tentang Perlindungan Konsumen",
        "legal_topic": "Consumer Protection & BPSK Disputes",
        "effective_date": "2000-04-20",
        "current_status": "active",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/45288/uu-no-8-tahun-1999",
        "verification_status": "verified",
    },
    {
        "legal_source_id": "LEG-010",
        "regulation_number": "37",
        "regulation_year": 2004,
        "title": "UU Nomor 37 Tahun 2004 tentang Kepailitan dan Penundaan Kewajiban Pembayaran Utang",
        "legal_topic": "Bankruptcy & PKPU",
        "effective_date": "2004-10-18",
        "current_status": "active",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/40784/uu-no-37-tahun-2004",
        "verification_status": "verified",
    },
    {
        "legal_source_id": "LEG-011",
        "regulation_number": "4",
        "regulation_year": 2023,
        "title": "UU Nomor 4 Tahun 2023 tentang Pengembangan dan Penguatan Sektor Keuangan",
        "legal_topic": "Financial Sector & UMKM Financing",
        "effective_date": None,
        "current_status": "active",
        "official_source": "JDIH BPK",
        "source_url": "https://peraturan.bpk.go.id/Details/240203/uu-no-4-tahun-2023",
        "verification_status": "verified",
    },
]


def build_ds09(out_dir: Path) -> pd.DataFrame:
    out_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(VERIFIED_REGULATIONS)
    csv_path = out_dir / "ds09_legal_information_register.csv"
    df.to_csv(csv_path, index=False)
    df.to_parquet(csv_path.with_suffix(".parquet"), index=False)
    return df


if __name__ == "__main__":
    for target in [Path("data/processed"), Path("data/public")]:
        res = build_ds09(target)
        print(f"Wrote {len(res)} verified DS09 legal register entries -> {target}")
