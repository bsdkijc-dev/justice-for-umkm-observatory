# Changelog

All notable changes to the **Justice for UMKM Observatory** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-23
### Added
- Initialized repository structure (`governance/`, `research/`, `schemas/`, `sources/`, `crawler/`, `processing/`, `survey/`, `analysis/notebooks/`, `reports/`, `data/`, `dashboard/`, `tests/`, `.github/workflows/`, `kaggle/`).
- Added governance, ethics, privacy, source-access, publication-standard, and survey-consent documentation.
- Added research protocol, 14 research questions, 8-dimension analytical framework, 8-category dispute taxonomy, 8-hypothesis register, and limitations register.
- Added JSON schemas (`judicial_dispute_schema.json`, `economic_indicator_schema.json`, `survey_schema.json`, `legal_access_schema.json`) and `data_dictionary.csv` covering all 10 Observatory datasets.
- Added statutory UMKM classification rules aligned with PP No. 7 Tahun 2021 (Pasal 35).
- Added polite collector (`crawler/polite_collector.py`), source discovery, provenance tracking, processing/validation/privacy-review pipeline, and synthetic test datasets (`data/synthetic/`).
- Added 12 reproducible analytical Jupyter notebooks (`analysis/notebooks/01`–`12`), pilot research report, policy intelligence brief, practical Indonesian legal guide, and mobile-friendly GitHub Pages dashboard (`dashboard/index.html`).
- Added automated test suite (`tests/`) and GitHub Actions CI workflows (`.github/workflows/`).
