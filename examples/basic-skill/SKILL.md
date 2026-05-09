---
name: basic-local-skill
description: Use this skill for simple local coding-agent tasks that need consistent instructions and a clear final report.
---

# Basic Local Skill

## Activation

Use this skill when a local agent task needs consistent instructions and a short structured report.

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
