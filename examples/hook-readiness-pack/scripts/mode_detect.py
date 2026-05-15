#!/usr/bin/env python3
import json
import re
import sys

TEXT = sys.stdin.read()

POWER = [r'\bsudo\b', r'\bgit\s+(push|reset|clean)\b', r'\btoken\b', r'\bpassword\b']
BUILD = [r'\bedit\b', r'\bcreate\b', r'\bupdate\b', r'\bfix\b', r'\bmodify\b']
SAFE = [r'\bread\b', r'\breview\b', r'\banalyze\b', r'\binspect\b']


def any_match(patterns):
    return [pattern for pattern in patterns if re.search(pattern, TEXT, re.I)]

power = any_match(POWER)
build = any_match(BUILD)
safe = any_match(SAFE)

if power:
    mode = 'POWER'
elif build:
    mode = 'BUILD'
elif safe:
    mode = 'SAFE'
else:
    mode = 'NEEDS_CONFIRMATION'

print(json.dumps({'ok': True, 'mode': mode, 'matches': {'power': power, 'build': build, 'safe': safe}}, indent=2))
