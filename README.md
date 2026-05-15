# Agent Skill Starter Kit

![Agent Skill Starter Kit](./agent-skill-starter.png)

A practical starter kit for turning repeated agent workflows into reusable local skills.

`Local-first` · `Copyable` · `Small scripts` · `Optional hooks` · `MIT License`

## What this is

Agent Skill Starter Kit is a public, copyable repository for organizing repeated agent workflows into small local skill folders.

It shows a practical pattern for combining:

- `SKILL.md` instructions for behavior and scope;
- small scripts for repeatable mechanical work;
- templates for consistent output shape;
- checks for lightweight validation;
- optional hooks for local guardrails.

The goal is simple: stop pasting the same long prompt again and again, and turn the parts that repeat into files you can inspect, adapt, and test.

## What this is not

This is not an installer, framework, hosted service, security product, or production system.

It does not ask you to install global hooks, run privileged commands, or trust automation blindly. The examples are meant to be read, copied, reduced, renamed, and tested on small local tasks first.

## Why this exists

Long prompts are useful, but they become hard to maintain when the same workflow returns every week. Skills make that workflow easier to repeat because the instructions, scripts, templates, and checks live in a folder instead of inside one giant prompt.

This repository documents a general workflow evolution:

```text
Long prompt
-> local skill
-> skill with scripts
-> templates and checks
-> optional hooks, only when useful
```

## Core idea

```text
Skill = behavior
Scripts = repeatability
Templates = output shape
Checks = validation
Hooks = optional guardrails
Agent = judgment
```

A good skill does not remove judgment from the agent. It gives the agent a clearer operating surface: what to do, what not to do, what to verify, and how to report the result.

## How the workflow evolved

🧠 Repeated prompts became reusable instructions.

🧰 Repeated manual steps became small scripts.

📄 Repeated report shapes became templates.

✅ Repeated acceptance criteria became checks.

🪝 Repeated guardrails can become optional hooks, but only when they stay small, deterministic, and easy to disable.

🧾 The final report remains important: it should say what changed, what was checked, what was not checked, and what limits remain.

## Repository structure

```text
agent-skill-starter-kit/
├── README.md
├── START_HERE.md
├── docs/
├── examples/
├── templates/
├── prompts/
├── diagrams/
├── LICENSE
└── .gitignore
```

- `docs/` explains the concepts and patterns.
- `examples/` contains copyable skill folders and small add-on patterns.
- `templates/` contains reusable starting files.
- `prompts/` contains helper prompts for generating or extending skills.
- `diagrams/` contains a lightweight architecture overview.

## Quick start

1. Read [START_HERE.md](START_HERE.md).
2. Pick an example from [`examples/`](examples/).
3. Copy the example folder to your own local workspace.
4. Rename the skill and edit `SKILL.md`.
5. Remove anything you do not need.
6. Test the skill on a small, low-risk task.
7. Add scripts, templates, checks, or hooks only when they solve a repeated problem.

## Create your first skill

Start with the smallest useful version:

```text
my-skill/
├── SKILL.md
└── README.md
```

Then add folders only when they earn their place:

```text
my-skill/
├── SKILL.md
├── README.md
├── scripts/
├── templates/
├── checks/
└── examples/
```

A strong first skill usually contains:

- when to use it;
- what scope is allowed;
- what actions are forbidden;
- what output format is required;
- what validation should happen before final answer.

## What to copy

Copy patterns, not private context.

Good things to copy:

- skill folder structure;
- concise activation language;
- scope and stop rules;
- final report format;
- small helper scripts;
- report templates;
- smoke checks;
- optional hook snippets that are disabled by default.

Things to replace:

- personal paths;
- project names;
- private logs;
- local-only assumptions;
- prompts that mention sensitive or internal work.

## Example patterns

- [`examples/basic-skill`](examples/basic-skill/) shows a minimal skill.
- [`examples/skill-with-scripts`](examples/skill-with-scripts/) shows scripts, checks, and templates.
- [`examples/review-closeout-skill`](examples/review-closeout-skill/) shows a controlled final review pattern.
- [`examples/hook-readiness-pack`](examples/hook-readiness-pack/) shows optional local hooks that are not active by default.

## Optional hooks, carefully

Hooks can help enforce repeated guardrails, but they should stay rare.

Use optional hooks when:

- the check is deterministic;
- the output is easy to inspect;
- failure mode is understandable;
- the hook can run in warning-only mode first;
- one hook can be tested at a time.

Avoid hooks when:

- the logic requires judgment;
- the hook would scan broad directories;
- it needs secrets or elevated permissions;
- it would run `sudo`, global installs, or automatic `git push`;
- you cannot easily disable or explain it.

See [Hook readiness pattern](docs/13-hook-readiness-pattern.md).

## Safety rules

🛡️ Before sharing or publishing a skill repository:

- do not include secrets, tokens, passwords, credentials, or `.env` files;
- do not include personal filesystem paths;
- do not include private logs or internal project details;
- do not add automatic `sudo`, global installs, or `git push`;
- do not make broad filesystem scans the default;
- do not claim a skill is a security product or production system;
- run smoke tests for scripts when scripts exist.

See [Public repo safety checklist](docs/14-public-repo-safety-checklist.md).

## Documentation map

- [What are agent skills?](docs/01-what-are-agent-skills.md)
- [Why use skills?](docs/02-why-use-skills.md)
- [Basic architecture](docs/03-basic-architecture.md)
- [Skill folder structure](docs/04-skill-folder-structure.md)
- [Scripts, templates, checks](docs/05-scripts-templates-checks.md)
- [Optional hooks](docs/06-optional-hooks.md)
- [Safety guidelines](docs/08-safety-guidelines.md)
- [How to adapt](docs/09-how-to-adapt.md)
- [Create your own skill](docs/11-create-your-own-skill.md)
- [Workflow recap](docs/11-codex-workflow-recap.md)
- [Review closeout pattern](docs/12-review-closeout-pattern.md)
- [Hook readiness pattern](docs/13-hook-readiness-pattern.md)
- [Public repo safety checklist](docs/14-public-repo-safety-checklist.md)
- [From private workflow to public template](docs/15-from-private-workflow-to-public-template.md)

## Roadmap

🚀 Possible future improvements:

- more small examples;
- additional report templates;
- more smoke-test patterns;
- clearer diagrams;
- language-specific examples for common local workflows.

## License

MIT. See [LICENSE](LICENSE).

## Disclaimer

This repository is an educational starter kit. Review every file before using it. Adapt examples to your local environment. Keep hooks optional and disabled until you have tested them carefully.
