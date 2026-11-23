#!/bin/sh
set -eu

echo "=== Justice for UMKM Observatory — Phase 2 Empirical & Pages Prep ==="

# 1. Stage Kaggle synthetic pilot directory (does NOT upload without human approval)
mkdir -p kaggle/stage_synthetic
cp -f data/synthetic/ds01_umkm_legal_disputes.csv kaggle/stage_synthetic/
cp -f data/synthetic/ds05_umkm_economic_indicators.csv kaggle/stage_synthetic/
cp -f data/synthetic/ds06_legal_information_access.csv kaggle/stage_synthetic/
cp -f data/synthetic/ds07_umkm_dispute_survey.csv kaggle/stage_synthetic/
cp -f schemas/data_dictionary.csv kaggle/stage_synthetic/
cp -f kaggle/dataset-metadata.json kaggle/stage_synthetic/
echo "[OK] Staged Kaggle synthetic pilot package in kaggle/stage_synthetic/"

# 2. Ingest any official DS05 CSV placed in data/raw/ds05_official_input.csv
if [ -f "data/raw/ds05_official_input.csv" ]; then
  PYTHONPATH=. python3 processing/ingest_ds05_official.py \
    --input data/raw/ds05_official_input.csv \
    --output data/processed/ds05_umkm_economic_indicators.csv \
    --source "Official BPS / Kementerian UMKM" \
    --period "2024-2025" \
    --indicator "umkm_population_count" \
    --unit "enterprises"
  PYTHONPATH=. python3 processing/validation.py --data-dir data/processed
  PYTHONPATH=. python3 processing/privacy_review.py --data-dir data/processed
else
  echo "[INFO] Place downloaded BPS/Kementerian UMKM CSV at data/raw/ds05_official_input.csv to run empirical DS05 ingestion."
fi

# 3. Run unit tests
PYTHONPATH=. python3 -m unittest discover -s tests -p "test_*.py" -v
echo "=== Done ==="
