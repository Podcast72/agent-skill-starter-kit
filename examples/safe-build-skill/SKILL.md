---
name: safe-build-skill
description: Use this skill for controlled local build tasks that need clear scope, stop rules, and optional path validation before editing files.
---

# Safe Build Skill

## What this skill does

Use this skill for local file changes that are allowed inside a clearly defined project area.

Typical tasks:

- creating a new local file;
- editing a small set of approved files;
- patching documentation or code in one repository folder;
- running small local checks after the change.

## Activation

Activate this skill when the task requires controlled local changes with explicit boundaries.

## Scope

- Local work only.
- Changes must stay inside the approved working root.
- Small patches, documentation updates, or local file creation.
- No network access by default.
- No destructive commands.
- No global configuration changes.

## Optional check

`checks/path_guard_example.py` can be used as a small helper before editing paths. It is optional and meant as a readable example, not as a complete safety system.

## Rules

- Confirm the allowed working root before editing files.
- Keep the write scope as small as possible.
- Prefer small, inspectable changes.
- Run local validation when it is easy and relevant.
- Report what changed, what was checked, and what was not checked.

## Stop rules

- Stop if the target path is outside the allowed root.
- Stop if the task requires destructive actions.
- Stop if the request mixes local edits with network or secret-handling tasks.
- Stop if the allowed scope is not clear.

## Final report format

```text
MODE:
TASK:
ALLOWED ROOT:
FILES MODIFIED:
CHECKS RUN:
LIMITS:
STATUS:
```
