# Research Protocol — Justice for UMKM Observatory v1.0

- **Title:** How Does Access to Justice Affect the Survival and Growth of Indonesian Micro and Small Enterprises?
- **Research Director:** Cecep Mustafa, Ph.D.
- **Research Period:** 2027–2030
- **Status:** Foundation Protocol (v1.0) — Independent Research Initiative

## 1. Research Population & Statutory Classification

Primary population: **Indonesian Micro and Small Enterprises (UMK)**.
Secondary comparison population: **Medium Enterprises**, where reliable comparable data exist.

Enterprise size classification strictly follows **Peraturan Pemerintah (PP) Nomor 7 Tahun 2021** tentang Kemudahan, Pelindungan, dan Pemberdayaan Koperasi dan Usaha Mikro, Kecil, dan Menengah ([JDIH BPK](https://peraturan.bpk.go.id/Details/161837/pp-no-7-tahun-2021)):

| Enterprise Size | Capital Threshold (*Modal Usaha*, excl. land & buildings) | Annual Sales Threshold (*Hasil Penjualan Tahunan*) |
| :--- | :--- | :--- |
| **Micro (Usaha Mikro)** | Up to IDR 1,000,000,000 | Up to IDR 2,000,000,000 |
| **Small (Usaha Kecil)** | > IDR 1,000,000,000 to IDR 5,000,000,000 | > IDR 2,000,000,000 to IDR 15,000,000,000 |
| **Medium (Usaha Menengah)** | > IDR 5,000,000,000 to IDR 10,000,000,000 | > IDR 15,000,000,000 to IDR 50,000,000,000 |

### Classification Rules
1. **No arbitrary thresholds:** Never classify enterprises using ad-hoc revenue or employee cutoffs.
2. **No title-based inference:** Never infer business size from a court case title alone; require explicit statutory or official registry evidence (e.g., OSS NIB scale, financial/capital facts in judgment text, or BPS/Kementerian UMKM classification).
3. **Preserve `unknown`:** When source evidence is insufficient to determine enterprise size, record `business_size = "unknown"`.

### Stratification Dimensions
Where lawful, ethical, and supported by data:
- Business size (`micro`, `small`, `medium`, `unknown`)
- Business sector (KBLI / BPS sector)
- Province and district/city (*kabupaten/kota*)
- Urban vs. rural location
- Business age
- Formal vs. informal status (e.g., NIB / OSS registration)
- Digital vs. non-digital business activity
- Gender of business owner (only where lawfully and ethically collected and appropriately aggregated)

## 2. Eight Analytical Dimensions

1. **A. Legal Accessibility:** Availability of legal information, understanding of legal rights, access to legal assistance, access to dispute resolution, geographic accessibility, digital accessibility.
2. **B. Affordability:** Legal consultation costs, court-related expenses, travel expenses, documentation costs, opportunity costs, business interruption costs.
3. **C. Contractual Security:** Contract clarity, payment disputes, unpaid invoices, contract termination, breach of agreement, enforcement of contractual obligations.
4. **D. Dispute Resolution:** Negotiation, mediation (including [PERMA No. 1 Tahun 2016](https://peraturan.bpk.go.id/Details/209641/perma-no-1-tahun-2016)), administrative settlement, arbitration (where applicable), litigation (including *Gugatan Sederhana* under [PERMA No. 4 Tahun 2019](https://peraturan.bpk.go.id/Details/206070/perma-no-4-tahun-2019)), and execution/compliance.
5. **E. Time and Operational Impact:** Dispute duration, delayed payments, working capital constraints, business interruption, lost business opportunities.
6. **F. Legal Certainty:** Predictability of legal procedures, availability of relevant legal information, consistency of applicable legal rules, enforceability of remedies.
7. **G. Business Resilience:** Continuity of operations, cash flow stability, asset protection, ability to retain workers, ability to maintain supplier relationships.
8. **H. Business Growth:** Revenue development, productivity, employment, market expansion, investment, business formalization.

> **Epistemic Guardrail:** Business resilience and growth must be measured using appropriate economic evidence. A court judgment alone is **never** proof of enterprise survival or business growth.

## 3. Mixed-Method Research Design

- **Method A — Judicial Document Analysis:** Permitted public judgment metadata from Mahkamah Agung RI ([Direktori Putusan](https://putusan3.mahkamahagung.go.id)). Analyze dispute types, court distribution, claim patterns, outcomes, remedies, processing duration, appeal patterns, and enforcement evidence.
- **Method B — Official Economic Data:** Aggregate data from [BPS](https://www.bps.go.id), [Kementerian UMKM](https://umkm.go.id), [OSS](https://oss.go.id), [Bank Indonesia](https://www.bi.go.id), and [OJK](https://www.ojk.go.id). Check reporting periods and definitions; never combine incompatible datasets without documenting adjustments.
- **Method C — Survey (Gated):** Optional UMKM dispute experience survey. **Do not launch** until instruments are reviewed, informed consent is established, ethical requirements are assessed, privacy safeguards are implemented, and sampling methodology is documented.
- **Method D — Interviews:** Voluntary participation of micro/small business owners, associations, legal aid providers, mediators, lawyers, researchers, and public officials. Never represent convenience samples as nationally representative.
- **Method E — Case Studies:** Transparent selection criteria; never expose individual businesses unnecessarily.
