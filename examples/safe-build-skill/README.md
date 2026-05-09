# Safe Build Skill Example

## What it does

This example shows a controlled build-style skill for small local edits. It combines scope rules, stop rules, and one optional path-check script to keep the workflow readable.

## What to change

- Change the skill name in `SKILL.md`.
- Change the activation line.
- Change the allowed root or the way your workflow defines it.
- Adjust the final report fields if you track different checks.

## What to keep

- The scoped edit model.
- The stop rules for unclear or unsafe requests.
- The rule that checks are supportive, not a replacement for judgment.
- The habit of reporting both changes and limits.

## What it must not do

- It must not edit files outside the approved working root.
- It must not use destructive commands by default.
- It must not use network access or global changes unless you explicitly redesign the skill for that.
- It must not assume that a path check is enough on its own.

## Optional files

- `checks/path_guard_example.py` is optional.
- Remove it if your workflow does not need path validation.
- Replace it if your environment needs a different guard.

## How to test it on a small task

1. Pick one safe local folder.
2. Ask the agent to create or edit one small file inside it.
3. Run the path guard example against that folder.
4. Check that the final report names the allowed root and the modified files.
