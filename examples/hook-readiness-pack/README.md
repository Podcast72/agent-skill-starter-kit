# Hook readiness pack

This example shows optional local hooks as a readiness pack.

The hooks are not active by default. The config snippet is a commented example only.

## Files

```text
hook-readiness-pack/
├── README.md
├── scripts/
│   ├── mode_detect.py
│   └── report_check.py
└── hooks/
    ├── pre_prompt_mode_guard.sh
    ├── post_response_report_check.sh
    └── config.snippet.toml
```

## Recommended use

1. Run the scripts directly first.
2. Test hooks with fake payloads.
3. Keep hooks warning-only at first.
4. Enable one hook at a time if you decide to use them.
5. Keep a backup of your local config before manual edits.

## Smoke tests

```bash
printf 'read this file' | python3 scripts/mode_detect.py
printf 'MODE:
FILES MODIFIED:
TESTS / CHECKS:
LIMITS:
STATUS:
' | python3 scripts/report_check.py
```
