# Data Governance Standard

1. **Zero-Imputation Policy:** Missing values must remain null/empty with explicit completeness flags. Never convert missing figures into zeros.
2. **Preserve Source Truth:** Keep original reported figures separate from calculated or harmonized values. Log variances in `DATASET 08 — DATA QUALITY REGISTER`.
3. **Statutory Classification Integrity:** Classify enterprises strictly under PP No. 7 Tahun 2021 (Pasal 35). Never infer business size from a case title alone.
4. **Provenance & Traceability:** Every record must carry `source_url` (or `source`), `retrieval_date`, and `validation_status` (`verified`, `provisional`, `synthetic`, `rejected`).
5. **Segregated Storage Tiers:**
   - `data/raw/` (gitignored): Untouched retrieved source files.
   - `data/staging/` (gitignored): Parsed, unvalidated intermediate tables.
   - `data/processed/` (gitignored): Validated internal analytical tables.
   - `data/public/`: De-identified, license-cleared, human-approved datasets only.
   - `data/synthetic/`: Clearly labeled synthetic datasets for testing and CI only.
