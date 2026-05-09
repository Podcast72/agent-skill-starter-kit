---
name: skill-with-scripts
description: Use this skill for local agent tasks that benefit from small helper scripts, templates and basic checks.
---

# Skill With Scripts

## Activation

Use this skill when a local task benefits from small repeatable helpers and a structured report.

## Scope

- Local agent tasks with clear boundaries.
- Small documentation or code changes.
- Optional checks before completion.

## Helpers

- `scripts/mode_detect.py` can classify the request into a simple working mode.
- `scripts/scope_guard.py` can validate whether a target path stays inside an allowed root.
- `scripts/report_check.py` can validate the final report structure.
- `templates/final_report.md` provides a reusable report shape.
- `checks/validate_skill.py` validates the example folder structure.

## Rules

- Scripts are helpers, not replacements for judgment.
- Use scripts for repeatable checks.
- Use the agent for reasoning, interpretation and decisions.
- Keep edits scoped to the approved folder.
- Report what was changed and what was not checked.

## Final Report

Use `templates/final_report.md` as the preferred report structure.
