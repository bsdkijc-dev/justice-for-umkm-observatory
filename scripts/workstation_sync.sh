#!/usr/bin/env bash
set -euo pipefail

echo "=== Justice for UMKM Observatory — Workstation Sync ==="

# 1. Push repository to GitHub (requires SSH key configured for bsdkijc-dev)
echo "[1/3] Pushing main branch to git@github.com:bsdkijc-dev/justice-for-umkm-observatory.git ..."
git push -u origin main

# 2. Download official portal landing pages / catalogs into data/raw/
echo "[2/3] Fetching official source catalogs into data/raw/ ..."
mkdir -p data/raw/official_snapshots
curl -fsSL "https://umkm.go.id/publikasi" -o data/raw/official_snapshots/umkm_publikasi.html || echo "Note: Manual download from https://umkm.go.id/publikasi may be required."
curl -fsSL "https://jabar.bps.go.id/id/statistics-table/2/NzUyIzI=/banyaknya-usaha-mikro-dan-kecil-menurut-kabupaten-kota.html" -o data/raw/official_snapshots/bps_jabar_umk.html || echo "Note: Manual CSV/XLSX export from BPS Jabar may be required."
curl -fsSL "https://jambi.bps.go.id/id/statistics-table/2/MjEzMSMy/jumlah-usaha-mikro-kecil-dan-menengah.html" -o data/raw/official_snapshots/bps_jambi_umkm.html || echo "Note: Manual CSV/XLSX export from BPS Jambi may be required."

# 3. Run full test suite & data validation
echo "[3/3] Running test suite and validation ..."
PYTHONPATH=. python3 -m unittest discover -s tests -p "test_*.py" -v
PYTHONPATH=. python3 processing/validation.py --data-dir data/synthetic
PYTHONPATH=. python3 processing/privacy_review.py --data-dir data/synthetic

echo "=== Sync complete ==="
