# Basic Architecture

```text
User Request
  ↓
Skill Instructions
  ↓
Optional Mode / Scope Detection
  ↓
Scripts / Templates / Checks
  ↓
Optional Hooks
  ↓
Agent Judgment
  ↓
Final Report
```

## Layers

- `User Request` is the task that starts the workflow.
- `Skill Instructions` define the behavior, scope and reporting rules.
- `Optional Mode / Scope Detection` helps classify risk or allowed paths before work begins.
- `Scripts / Templates / Checks` support repeatable operations, output shape and validation.
- `Optional Hooks` can add small guardrails before or after key steps.
- `Agent Judgment` is still responsible for interpretation, tradeoffs and decisions.
- `Final Report` summarizes what happened, what changed and what was not checked.
