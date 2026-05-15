# Review closeout pattern

A review closeout is a final controlled pass after non-trivial local changes.

Its goal is not to obey every review finding automatically. Its goal is to separate real issues from speculative suggestions, fix only what is justified, and report the evidence clearly.

## Principles

- Review output is advisory.
- Findings must be verified against real code or real behavior.
- Small fixes are preferred over broad refactors.
- Tests should be targeted to the changed behavior.
- No claim of clean, ready, or complete should be made without evidence.

## Suggested loop

1. Read the diff and changed files.
2. Run or collect the review output.
3. Convert each finding into a decision: accepted, rejected, or not verified.
4. Accept only findings with concrete evidence.
5. Apply the smallest useful fix.
6. Run targeted tests or checks.
7. Repeat review only when the fix changes meaningful code.
8. Produce a final report.

## Finding decision table

```text
Finding | Evidence | Decision | Fix | Validation
--- | --- | --- | --- | ---
F-001 | file and behavior | accepted | small patch | targeted test
F-002 | speculative style preference | rejected | none | explanation
```

## Final report shape

A closeout report should include:

- scope reviewed;
- command or review source used;
- files read;
- files modified;
- findings accepted;
- findings rejected;
- tests or validations;
- limits;
- final state.
