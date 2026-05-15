#!/usr/bin/env bash
set -u
SCRIPT_DIR="$(cd "$(dirname "$0")/../scripts" && pwd)"
python3 "$SCRIPT_DIR/mode_detect.py"
