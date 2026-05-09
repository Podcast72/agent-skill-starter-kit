---
name: passive-review-skill
description: Use this skill as an example of a local review-oriented skill that can optionally record minimal usage metadata for later manual review.
---

# Passive Review Skill

## What this skill does

Use this skill when you want a reusable local skill that can keep a small audit trail of usage events without storing sensitive content and without changing itself.

## Activation

Activate this skill when manual review matters more than automation and when logging, if used at all, should stay minimal.

## Scope

- Local skill use only.
- Minimal usage metadata only.
- Manual review only.
- No network access.
- No global configuration changes.
- No automatic self-modification.

## Optional script

`scripts/usage_log_example.py` is an optional example that appends small JSONL entries inside this example folder only.

## Rules

- Logging is optional and must be explicitly allowed by the user.
- Do not store full prompts.
- Do not store secrets, personal data, file contents, or credentials.
- Do not modify the skill automatically.
- Do not make automatic improvement decisions from the log.
- Use the log only to support later manual review.

## Stop rules

- Stop if the request asks for full prompt logging.
- Stop if the request asks for automatic upgrades or self-modification.
- Stop if the task would move logs outside the example folder.
- Stop if the user wants hidden or non-reviewable behavior.

## Final report format

```text
MODE:
TASK:
LOGGING USED:
FILES CHANGED:
VALIDATION:
LIMITS:
STATUS:
```
