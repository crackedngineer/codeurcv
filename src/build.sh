#!/usr/bin/env bash
set -euo pipefail

# ==============================
# Positional Arguments
# ==============================

OUT_DIR="${1:-output}"
CONFIG_FILE="${2:-config.yml}"

echo "📁 Output directory: $OUT_DIR"
echo "⚙️  Config file: $CONFIG_FILE"

# ==============================
# Ensure output directory exists
# ==============================

mkdir -p "$OUT_DIR"

# ==============================
# Render Template
# ==============================

python "$(dirname "$0")/render.py" \
  -f "$CONFIG_FILE" \
  --out_dir "$OUT_DIR"

echo "✅ Render completed"