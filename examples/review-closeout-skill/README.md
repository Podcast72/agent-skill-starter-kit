# Review closeout skill

This example shows a small skill for a final controlled review after local edits.

Use it when you want the agent to:

- read the changed surface;
- treat review findings as advisory;
- verify findings before accepting them;
- apply only small justified fixes;
- run targeted checks;
- produce a clear final report.

## Files

```text
review-closeout-skill/
├── SKILL.md
├── README.md
├── scripts/
│   └── review_report_check.py
└── templates/
    └── review-closeout-report.md
```

## Smoke test

```bash
python3 scripts/review_report_check.py templates/review-closeout-report.md
```
