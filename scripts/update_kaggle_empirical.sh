#!/bin/sh
set -eu

echo "=== Staging Kaggle Dataset Update (Validated DS05 + DS09 + Dictionary) ==="
mkdir -p kaggle/stage_release
cp -f data/public/ds05_umkm_economic_indicators.csv kaggle/stage_release/
cp -f data/public/ds09_legal_information_register.csv kaggle/stage_release/
cp -f data/synthetic/ds01_umkm_legal_disputes.csv kaggle/stage_release/ds01_synthetic_pilot.csv
cp -f data/synthetic/ds06_legal_information_access.csv kaggle/stage_release/ds06_synthetic_pilot.csv
cp -f data/synthetic/ds07_umkm_dispute_survey.csv kaggle/stage_release/ds07_synthetic_pilot.csv
cp -f schemas/data_dictionary.csv kaggle/stage_release/
cp -f kaggle/dataset-metadata.json kaggle/stage_release/

PYTHONPATH=. python3 processing/validation.py --data-dir data/public --schemas-dir schemas
PYTHONPATH=. python3 processing/privacy_review.py --data-dir kaggle/stage_release

echo "[OK] Staged in kaggle/stage_release/. Pushing new Kaggle dataset version..."
kaggle datasets version -p kaggle/stage_release -m "Add validated empirical DS05 (278 records) and DS09 (11 verified regulations)"
