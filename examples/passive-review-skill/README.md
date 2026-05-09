# Passive Review Skill Example

## What it does

This example shows a passive review pattern. The method is intentionally limited: optional metadata logging, manual review, no self-modification, and no hidden upgrade logic.

## What to change

- Change the skill name in `SKILL.md`.
- Change the activation line.
- Adjust which metadata fields matter to your workflow.
- Remove the script if you do not need logging at all.

## What to keep

- The rule that logging is optional.
- The rule that full prompts, secrets, personal data, and file contents must not be logged.
- The rule that review stays manual.
- The stop rules against self-modification and automatic upgrades.

## What it must not do

- It must not log full prompts.
- It must not log secrets, credentials, or personal data.
- It must not write outside this example folder.
- It must not modify itself or install anything automatically.

## Optional files

- `scripts/usage_log_example.py` is optional.
- Keep it only if minimal usage metadata is useful in your workflow.

## How to test it on a small task

1. Run the example logger with safe fake values.
2. Open the generated JSONL file.
3. Confirm that it contains only small metadata fields.
4. Confirm that no prompt text, file content, or secret-like values are stored.
