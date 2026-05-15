# Hook readiness pattern

A hook readiness pack is a prepared set of local scripts and disabled hook wrappers.

It is not an instruction to activate hooks immediately.

## What hooks are good for

Hooks can help with simple, repeated guardrails:

- detect whether a prompt looks read-only, build-oriented, or high-risk;
- check that a path is inside an allowed root;
- check that a final report has required sections;
- warn when prompt text appears to contain a token, password, credential, or `.env` reference.

## What hooks should not become

Hooks should not become a hidden runtime governance system.

Avoid hooks that:

- require broad filesystem scans;
- need secrets;
- run privileged commands;
- rewrite files automatically;
- make broad policy decisions without agent judgment;
- trigger automatic Git operations.

## Activation rules

If you decide to activate hooks later:

1. Start warning-only.
2. Enable one hook at a time.
3. Back up the local config first.
4. Verify local syntax before editing config.
5. Use fake payloads for smoke tests.
6. Keep the hook easy to disable.

## Readiness pack layout

```text
hook-readiness-pack/
├── scripts/
│   ├── mode_detect.py
│   └── report_check.py
└── hooks/
    ├── pre_prompt_mode_guard.sh
    ├── post_response_report_check.sh
    └── config.snippet.toml
```

The snippet should remain manual and disabled by default.
