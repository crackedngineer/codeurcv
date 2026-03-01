#!/usr/bin/env bash
set -euo pipefail

# ==============================
# Positional Arguments
# ==============================

OUT_DIR="${1:-output}"
CONFIG_FILE="${2:-config.yaml}"

echo "📁 Output directory: $OUT_DIR"
echo "⚙️  Config file: $CONFIG_FILE"

# ==============================
# Ensure output directory exists
# ==============================

mkdir -p "$OUT_DIR"

# ==============================
# Render Template
# ==============================

python render.py --out_dir "$OUT_DIR" --filename "$CONFIG_FILE"

echo "✅ Render completed"