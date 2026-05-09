---
name: basic-local-skill
description: Use this skill for simple local coding-agent tasks that need consistent instructions and a clear final report.
---

# Basic Local Skill

## What this skill does

Use this skill when you want the smallest reusable local skill with clear instructions, clear limits, and a short final report.

## Activation

Activate this skill for small local tasks that do not need helper scripts.

## Scope

- Local work only.
- Small and clear tasks.
- No network access by default.
- No global configuration changes.

## Rules

- Read the request carefully before changing files.
- Keep changes small and explain what changed.
- Do not use destructive commands by default.
- Do not use `sudo` or global installs.
- Report limits and missing verification clearly.

## Stop rules

- Stop if the request requires network access, secrets, or global changes.
- Stop if the task scope is unclear.
- Stop if the requested action becomes destructive.

## Final Report Format

```text
MODE:
TASK:
FILES CHANGED:
VALIDATION:
LIMITS:
STATUS:
```

No scripts are required for this example.
