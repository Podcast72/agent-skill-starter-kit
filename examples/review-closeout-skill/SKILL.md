---
name: review-closeout-skill
description: Use this skill for a controlled final review after non-trivial local edits. It helps evaluate advisory findings, apply only verified fixes, run targeted checks, and produce a final closeout report.
---

# Review Closeout Skill

## Activation

Respond with:

```text
SKILL: review-closeout-skill active
MODE: SAFE / BUILD / NEEDS_CONFIRMATION
```

## Mission

Run a disciplined final review pass after local changes.

Treat review output as advisory. Verify findings against real code or real behavior before accepting them. Apply only small fixes that are justified by evidence. Run targeted tests or checks after accepted fixes.

## Rules

- Do not apply findings blindly.
- Do not turn closeout into a broad refactor.
- Do not claim clean or ready without evidence.
- Keep patches small.
- Report accepted and rejected findings separately.

## Final report

```text
MODE:
SCOPE REVIEW:
REVIEW SOURCE:
FILES READ:
FILES MODIFIED:
FINDINGS ACCEPTED:
FINDINGS REJECTED:
TESTS / CHECKS:
LIMITS:
STATUS:
```
