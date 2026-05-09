#!/usr/bin/env python3
import json
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "MODE:",
    "TASK:",
    "FILES CREATED:",
    "FILES MODIFIED:",
    "SCRIPTS USED:",
    "CHECKS RUN:",
    "LIMITS:",
    "STATUS:",
]


def load_text() -> str:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    return sys.stdin.read()


def main() -> int:
    text = load_text()
    missing = [section for section in REQUIRED_SECTIONS if section not in text]
    print(json.dumps({"ok": not missing, "missing": missing}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
