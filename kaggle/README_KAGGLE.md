# Kaggle Publication Staging (`judicialcollege`)

> **Human Approval Gate:** Per `governance/publication-standard.md`, do **not** run `kaggle datasets create` until the Research Director approves publication.

## 1. Stage Synthetic Pilot Package
```bash
mkdir -p kaggle/stage_synthetic
cp data/synthetic/ds01_umkm_legal_disputes.csv kaggle/stage_synthetic/
cp data/synthetic/ds05_umkm_economic_indicators.csv kaggle/stage_synthetic/
cp data/synthetic/ds06_legal_information_access.csv kaggle/stage_synthetic/
cp data/synthetic/ds07_umkm_dispute_survey.csv kaggle/stage_synthetic/
cp schemas/data_dictionary.csv kaggle/stage_synthetic/
cp kaggle/dataset-metadata.json kaggle/stage_synthetic/
```

## 2. Publish After Explicit Human Approval
```bash
kaggle datasets create -p kaggle/stage_synthetic
```
