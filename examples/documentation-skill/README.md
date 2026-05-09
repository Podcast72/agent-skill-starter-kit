# Documentation Skill Example

## What it does

This example shows a documentation-focused skill for repeated Markdown and guide-writing tasks. It keeps the method simple: read first, write clearly, keep scope narrow, and finish with a structured report.

## What to change

- Change the skill name in `SKILL.md`.
- Change the activation line to match your own trigger phrase.
- Adjust the allowed documentation scope.
- Adjust the final report fields if your workflow needs different checkpoints.

## What to keep

- The structure of `SKILL.md`.
- The rule that meaning should not change without an explicit request.
- The stop rules for unclear scope or unsupported claims.
- The short final report pattern.

## What it must not do

- It must not edit code unless you explicitly expand its scope.
- It must not use network access by default.
- It must not add unsupported marketing or product claims.
- It must not replace human review for important documentation changes.

## Optional files

- `templates/final-report.md` is optional.
- If you prefer a different completion format, replace it or remove it.

## How to test it on a small task

Try it on a small README or one short guide section:

1. Ask the agent to improve one heading or one usage section.
2. Confirm that the edits stay inside documentation files.
3. Check that the final report explains what changed and what was not checked.
