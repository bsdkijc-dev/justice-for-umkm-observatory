# Pilot Research Report — Justice for UMKM Observatory (v1.0 Foundation)

**Research Director:** Cecep Mustafa, Ph.D.  
**Date:** 2026-11-23  
**Status:** Foundation & Pipeline Verification Report (No Empirical Claims from Synthetic Data)

## 1. Executive Summary
The **Justice for UMKM Observatory (v1.0)** research infrastructure has been established to investigate how access to justice, legal uncertainty, dispute resolution costs, and remedy enforcement affect the survival and growth of Indonesian micro and small enterprises (UMK).

## 2. Verified Statutory & Institutional Baseline
- **Enterprise Classification:** Strictly anchored to **PP Nomor 7 Tahun 2021** Pasal 35 ([JDIH BPK](https://peraturan.bpk.go.id/Details/161837/pp-no-7-tahun-2021)), defining Micro (capital <= IDR 1B / sales <= IDR 2B), Small (capital > IDR 1B–5B / sales > IDR 2B–15B), and Medium (capital > IDR 5B–10B / sales > IDR 15B–50B) enterprises.
- **Small Claims & Mediation:** Court-annexed mediation is governed by **PERMA Nomor 1 Tahun 2016** ([JDIH BPK](https://peraturan.bpk.go.id/Details/209641/perma-no-1-tahun-2016)), and *Gugatan Sederhana* (max IDR 500 million) is governed by **PERMA Nomor 4 Tahun 2019** ([JDIH BPK](https://peraturan.bpk.go.id/Details/206070/perma-no-4-tahun-2019)).
- **Institutional Scope:** Reflects the 2024 establishment of **Kementerian UMKM RI** ([umkm.go.id](https://umkm.go.id/)) under Perpres Nomor 196 Tahun 2024, alongside [BPS](https://www.bps.go.id), [Bank Indonesia](https://www.bi.go.id), [OJK](https://www.ojk.go.id), [OSS](https://oss.go.id), [Mahkamah Agung RI](https://putusan3.mahkamahagung.go.id), and [BPHN](https://sidbankum.bphn.go.id).

## 3. Infrastructure & Validation Results
- **10 Datasets & 4 JSON Schemas:** All schemas (`DS01`–`DS10`) and `schemas/data_dictionary.csv` are implemented and verified against synthetic fixtures.
- **Zero-Imputation & Privacy Gates:** `processing/validation.py` and `processing/privacy_review.py` passed with `0` errors across all 10 synthetic datasets.
- **Analytical Readiness:** All 12 reproducible notebooks (`01`–`12`) are generated and ready for empirical ingestion once source-access clearances and human approvals are completed.

## 4. Next Steps Before Empirical Findings
1. Conduct manual/API verification of official bulk datasets from BPS, Kementerian UMKM, BI, and OJK.
2. Verify `putusan3.mahkamahagung.go.id` category URLs and rate-limit compliance before any metadata collection.
3. Complete ethical review and consent approval before launching the UMKM Dispute Experience Survey (`DS07`).
