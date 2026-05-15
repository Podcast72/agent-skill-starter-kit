#!/usr/bin/env python3
import argparse
import json
import sys

REQUIRED = [
    'MODE',
    'SCOPE REVIEW',
    'REVIEW SOURCE',
    'FILES READ',
    'FILES MODIFIED',
    'FINDINGS ACCEPTED',
    'FINDINGS REJECTED',
    'TESTS / CHECKS',
    'LIMITS',
    'STATUS',
]


def main():
    parser = argparse.ArgumentParser(description='Check required sections in a review closeout report.')
    parser.add_argument('report', nargs='?', help='Report path. Reads stdin when omitted.')
    args = parser.parse_args()
    if args.report:
        with open(args.report, 'r', encoding='utf-8') as handle:
            text = handle.read()
    else:
        text = sys.stdin.read()
    upper = text.upper()
    missing = [name for name in REQUIRED if name + ':' not in upper]
    print(json.dumps({'ok': not missing, 'missing': missing}, indent=2))
    return 0 if not missing else 1


if __name__ == '__main__':
    raise SystemExit(main())
