#!/usr/bin/env python3
import json
import sys

REQUIRED = ['MODE', 'FILES MODIFIED', 'TESTS / CHECKS', 'LIMITS', 'STATUS']
text = sys.stdin.read().upper()
missing = [name for name in REQUIRED if name + ':' not in text]
print(json.dumps({'ok': not missing, 'missing': missing}, indent=2))
raise SystemExit(0 if not missing else 1)
