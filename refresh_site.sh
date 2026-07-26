#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
python3 generate_site.py

echo "Site refreshed successfully."
