# Agent Skill Starter Kit

![Agent Skill Starter Kit](./agent-skill-starter.png)

## Short description

A practical starter kit for turning repeated agent workflows into reusable local skills.

Instead of pasting the same long prompt again and again, this repository shows how to organize instructions, optional scripts, templates, checks, and guardrails into small skill folders that can be copied, renamed, inspected, and adapted.

## Why this exists

Long prompts can work well for one task, but they are harder to repeat consistently. This repository shows a simple way to keep recurring agent instructions, helper scripts, templates, and checks in a structure that can be copied and adapted.

It is designed to be downloaded or cloned, reviewed locally, and used manually.

## Who this is for

This repository is for people who:

- use local coding agents for repeated tasks;
- want a clearer structure than pasting the same prompt every time;
- want small, readable examples they can copy and rename;
- want optional scripts and templates without turning the setup into a large system.

## What you get

This repository gives you a copyable structure, not a closed system.

- a basic skill example built around `SKILL.md`;
- a skill example with optional scripts, templates, and checks;
- an experimental passive skill example with minimal usage logging;
- reusable templates for new skills;
- prompt files for creating or extending your own skill setup;
- supporting documentation for structure, safety, and adaptation.

## Core idea

```text
Skill = operational instructions
Scripts = repeatable execution
Templates = consistent output shape
Checks = basic validation
Hooks = optional guardrails
Agent = reasoning, judgment and adaptation
```

## How it works

```text
User activates or references a skill
-> The agent reads the skill instructions
-> Optional scripts handle repeatable tasks
-> Templates shape the output
-> Checks validate minimum requirements
-> Optional hooks add guardrails
-> The agent produces a final report
```

## Repository structure

```text
agent-skill-starter-kit/
├── README.md
├── docs/
├── examples/
├── templates/
├── prompts/
├── diagrams/
├── LICENSE
└── .gitignore
```

- `docs/` explains concepts, architecture, safety notes, and adaptation steps.
- `examples/` contains copyable skill examples with increasing structure.
- `templates/` provides reusable starting files for new skills.
- `prompts/` contains helper prompts for building or extending your own setup.
- `diagrams/` contains a simple visual overview of the workflow.

## Quick start

1. Clone or download this repository.

```bash
cd agent-skill-starter-kit
ls examples
```

2. Open the `examples/` folder.
3. Pick one example that matches your workflow.
4. Copy that example to a new folder.
5. Rename the skill and update `SKILL.md`.
6. Remove anything you do not need.
7. Test the skill on a small local task.

## Manual setup / installation

There is no installer and no required global package setup.

Basic manual setup:

1. Clone the repository:

```bash
git clone https://github.com/Podcast72/agent-skill-starter-kit.git
```

2. Or download the repository as a ZIP and extract it locally.
3. Review the example folders before using them.
4. Copy one example into your own local skill area or workspace.
5. Adapt names, instructions, templates, and optional scripts as needed.

You can also use the repository purely as a reference without copying the files directly.

## Create your first skill

1. Start from `examples/basic-skill/` if you want the smallest setup.
2. Copy the folder and rename it.
3. Update the `name` and `description` fields in `SKILL.md`.
4. Rewrite the activation line, scope, and rules for your own repeated task.
5. Keep the reporting format short and clear.
6. Add scripts only if a step is mechanical, repeated, or easy to validate.

## Skill anatomy

A skill can stay very small.

Recommended structure:

```text
skill-name/
├── SKILL.md
├── scripts/
├── templates/
├── checks/
├── examples/
└── README.md
```

- `SKILL.md` defines the behavior, scope, and reporting rules.
- `scripts/` contains optional helpers for repeatable tasks.
- `templates/` contains optional output formats.
- `checks/` contains minimum validation helpers.
- `examples/` can contain sample outputs or usage references.
- `README.md` documents the skill for human readers.

Not every skill needs every folder. A simple skill can be only `SKILL.md` and `README.md`.

## Example use cases

- a documentation skill that always returns the same final report format;
- a local review skill with consistent scope rules;
- a patching skill with a lightweight path guard;
- a research or notes skill that keeps outputs in a stable template;
- an experimental passive skill that records minimal usage metadata for later manual review.

## Safety guidelines

- Do not store secrets in skills.
- Do not scan broad filesystem paths by default.
- Do not run destructive commands by default.
- Do not use `sudo` by default.
- Do not install global packages by default.
- Do not run `git push` by default.
- Keep scripts small and readable.
- Keep hooks few and deterministic.
- Keep checks narrow and easy to inspect.
- Treat checks as minimum validation only, not as a replacement for review or testing.
- Always report what was changed and what was not checked.

## Experimental passive skill pattern

The experimental passive skill pattern is a simple example of how a skill can record minimal usage metadata for later manual review.

It is intentionally limited:

- logging is optional;
- full prompt text must not be stored;
- secrets and personal data must not be stored;
- file contents must not be stored;
- the skill must not modify itself;
- the skill must not change global configuration;
- hooks must not be installed automatically;
- no automatic improvement decisions should be made.

The goal is not automatic self-improvement. The goal is to make later manual review easier.

## Documentation

- [What are agent skills](docs/01-what-are-agent-skills.md)
- [Why use skills](docs/02-why-use-skills.md)
- [Basic architecture](docs/03-basic-architecture.md)
- [Skill folder structure](docs/04-skill-folder-structure.md)
- [Scripts, templates, checks](docs/05-scripts-templates-checks.md)
- [Optional hooks](docs/06-optional-hooks.md)
- [Experimental passive skill](docs/07-experimental-passive-skill.md)
- [Safety guidelines](docs/08-safety-guidelines.md)
- [How to adapt](docs/09-how-to-adapt.md)
- [FAQ](docs/10-faq.md)

## Roadmap

- Keep the examples small and easy to inspect.
- Improve documentation where recurring questions appear.
- Add more adaptation notes if new public examples stay generic and readable.
- Keep the passive example limited to manual-review patterns.

## License

This repository is available under the [MIT License](LICENSE).

## Disclaimer

This repository is an educational starter kit and reference example. Review and test every script before using it in your own environment.

It is not a framework, not a formal standard, not a security product, and not a production-ready system.
