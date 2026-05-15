# Start here

Use this repository as a practical starting point for creating your own local agent skill.

## The recommended path

1. Read [README.md](README.md).
2. Pick one example from [`examples/`](examples/).
3. Copy the folder into your own local workspace.
4. Rename the skill folder.
5. Edit `SKILL.md` first.
6. Remove what you do not need.
7. Test on a small task.
8. Add scripts or checks only when they make repeated work easier to validate.
9. Treat hooks as optional guardrails, not as a required setup step.

## What to edit first

Start with the human-readable parts:

- skill name;
- short description;
- activation phrase;
- allowed scope;
- forbidden actions;
- final report format;
- examples that match your own workflow.

## What to remove

Remove anything you do not understand or do not need:

- unused scripts;
- unused templates;
- unused checks;
- hook snippets you are not ready to test;
- project-specific wording;
- personal paths;
- private logs.

## First safe test

Run the skill on a tiny local task first, such as:

- review one Markdown file;
- generate a short report;
- check one folder with a narrow scope;
- run one script with a fake payload.

Do not start with broad scans, destructive commands, private files, or automatic Git operations.

## When to add scripts

Add a script when the same step is mechanical and repeated. Good examples:

- check required report sections;
- classify a prompt into a small set of modes;
- validate that a path is inside an allowed folder;
- create a reusable receipt from a log.

## When to add hooks

Add hooks only after the script they call is already useful on its own.

Keep hooks:

- disabled by default;
- warning-only at first;
- small and deterministic;
- easy to remove;
- tested one at a time.

## Before sharing publicly

Read [docs/14-public-repo-safety-checklist.md](docs/14-public-repo-safety-checklist.md) before publishing your adapted skill repository.
