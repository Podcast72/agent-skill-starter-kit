# Codex workflow recap

This recap describes a generic workflow for turning repeated agent work into reusable local files.

It starts simple:

```text
Long prompt -> skill -> skill with scripts -> templates/checks -> optional hooks
```

The point is not to make a large system. The point is to move repeated instructions out of memory and into inspectable files.

## The formula

```text
Skill = behavior
Scripts = repeatability
Templates = output shape
Checks = validation
Hooks = optional guardrails
Agent = judgment
```

## Stage 1: long prompt

A long prompt is often the fastest way to discover a workflow. It can describe tone, scope, constraints, output format, and stop rules in one place.

The problem appears when the same prompt becomes a recurring operating procedure.

## Stage 2: skill

A skill moves repeated behavior into `SKILL.md`.

A useful skill should explain:

- when it should be used;
- what it is allowed to do;
- what it must not do;
- what evidence it should collect;
- how it should report the result.

## Stage 3: scripts

Scripts are useful when a step is mechanical and repeated.

Examples:

- detect a mode;
- check report sections;
- guard a path;
- summarize a log;
- validate a small JSON shape.

Scripts should stay small, local, readable, and dependency-light.

## Stage 4: templates and checks

Templates shape output. Checks validate minimum expectations.

A template can make the final report consistent. A check can ensure the report includes required sections before the work is considered complete.

## Stage 5: optional hooks

Hooks can call scripts automatically around an agent workflow. They should be treated carefully because automatic guardrails can become confusing if they are too broad or too clever.

Use hooks as optional local guardrails, not as a replacement for agent judgment.
