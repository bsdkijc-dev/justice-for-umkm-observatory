# Justice for UMKM Observatory (v1.0)

> **Justice for Small Business. Prosperity for Everyone.**

- **Research Director:** Cecep Mustafa, Ph.D.
- **Research Period:** 2027–2030
- **Core Research Question:** *How Does Access to Justice Affect the Survival and Growth of Indonesian Micro and Small Enterprises?*
- **Project Type:** Independent, evidence-based legal, economic, and judicial policy research initiative.
- **Platforms:** GitHub (`bsdkijc-dev/justice-for-umkm-observatory`) | Kaggle (`judicialcollege`) | GitHub Pages

## Project Independence

This is an independent research initiative. It does **not** claim official endorsement by Mahkamah Agung RI, the Government of Indonesia, Kementerian UMKM, or any other institution unless formal authorization exists. The Research Director does not speak on behalf of any government institution.

## Statutory Population Scope

The primary research population consists of Indonesian **micro and small enterprises (UMK)**, with **medium enterprises** as a secondary comparison population where reliable comparable data exist. Enterprise classification strictly follows **Peraturan Pemerintah (PP) Nomor 7 Tahun 2021** (Pasal 35) implementing UU Cipta Kerja (UU No. 11 Tahun 2020 / UU No. 6 Tahun 2023), rather than arbitrary thresholds. Business size is **never** inferred from a court case title alone.

## Repository Structure

```text
justice-for-umkm-observatory/
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── .gitignore
├── governance/        # Ethics, data governance, privacy, source-access, publication standards
├── research/          # Protocol, 14 RQs, methodology, 8-category taxonomy, hypotheses, limitations
├── schemas/           # JSON schemas & data_dictionary.csv for all 10 Observatory datasets
├── sources/           # Official judicial, economic, legal, & legal-aid source registries
├── crawler/           # Polite source discovery, rate-limited collector, provenance logger
├── processing/        # Extraction, normalization, deduplication, validation, privacy review
├── survey/            # Ethical UMKM dispute experience questionnaire, sampling plan, consent
├── analysis/notebooks/# 12 reproducible Jupyter notebooks (01–12)
├── reports/           # Technical, statistical, policy, and public education reports
├── data/              # raw/, staging/, processed/, public/, synthetic/ (raw/staging gitignored)
├── dashboard/         # Mobile-friendly GitHub Pages public dashboard (Bahasa Indonesia)
├── tests/             # Automated schema, taxonomy, privacy, and pipeline unit tests
├── kaggle/            # Kaggle dataset publication metadata and staging packages
└── .github/workflows/ # CI workflows for tests, data validation, and publication checks
```

## Quickstart

```bash
# Run automated test suite (standard library unittest; pytest compatible)
python3 -m unittest discover -s tests -p "test_*.py" -v

# Run synthetic data validation & privacy review
python3 processing/validation.py --data-dir data/synthetic
python3 processing/privacy_review.py --data-dir data/synthetic
```

## Complementary Scope

Employment disputes involving UMKM are tracked as an interconnected risk category (Category 05), while detailed Industrial Relations Court (PHI) labour adjudication analysis is cross-referenced to the **Indonesia Labour Justice Observatory (ILJO)** to avoid duplication.
