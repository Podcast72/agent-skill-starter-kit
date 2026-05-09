# Agent Skill Starter Kit

![Agent Skill Starter Kit](./agent-skill-starter.png)

## Short description

A practical starter kit for turning repeated agent workflows into reusable local skills.

Instead of pasting the same long prompt again and again, this repository shows how to organize instructions, optional scripts, templates, checks, and guardrails into small skill folders that can be copied, renamed, inspected, and adapted.

This repository shares a practical working method for creating local skills that make coding agents more consistent, reusable, and easier to guide.

It publishes a copyable operating method, not only demo files. The reasoning, structure, rules, patterns, and optional supporting parts are part of what you can reuse.

## Why this exists

Long prompts can work well for one task, but they are harder to repeat consistently. This repository shows a simple way to keep recurring agent instructions, helper scripts, templates, and checks in a structure that can be copied and adapted.

It is designed to be downloaded or cloned, reviewed locally, and used manually.

The goal is not to hide the reasoning behind the skill. The reasoning, structure, guardrails, templates, checks, and optional scripts are the reusable part.

You can copy an example, rename the skill, adjust the preferences, and use it as a starting point for your own workflow.

## Origin of the method

This starter kit comes from a practical workflow: repeated agent tasks were first handled with long prompts, then gradually converted into reusable local skills.

The method was shaped by three sources:

- real local usage with coding agents;
- study of existing agent-skill patterns and public examples;
- practical lessons from prompt engineering, safety boundaries, templates, checks, and repeatable reports.

The result is not a copy of one specific system. It is a public, simplified, and adaptable method for turning recurring agent workflows into local skills.

The method uses a simple pattern:

- `SKILL.md` for operating instructions;
- optional scripts for repeatable mechanical steps;
- templates for consistent outputs;
- checks for minimum validation;
- optional hooks for guardrails;
- final reports to make the agent explain what changed, what was checked, and what was not checked.

The goal is to make agent work easier to repeat, inspect, and adapt.

This repository does not hide the reasoning behind the workflow. The reasoning is part of what you are meant to copy, rename, and adapt to your own local preferences.

## Use the method with your own skill name

The examples are designed so you can keep the operating method and change only what should be personal to your workflow.

In most cases, start by changing:

- the skill name;
- the activation line;
- the short description;
- the allowed scope;
- the preferred final report format;
- any local paths or project-specific references;
- optional scripts, checks, or templates you do not need.

The structure, reasoning pattern, safety rules, and reporting style can stay the same.

## Who this is for

This repository is for people who:

- use local coding agents for repeated tasks;
- want to turn their personal workflow into reusable local skills;
- want a clearer structure than pasting the same prompt every time;
- want a stronger starting point than an empty template;
- want small, readable examples they can copy and rename;
- want a shared method with room for different skill names and preferences;
- want optional scripts and templates without turning the setup into a large system.

## What you get

This repository gives you a copyable structure, not a closed system.

- a basic skill example built around `SKILL.md`;
- a documentation skill example with a reusable final report template;
- a safe build skill example with an optional path guard check;
- a passive review skill example with minimal usage logging;
- older examples that show additional script and helper patterns;
- reusable templates for new skills;
- prompt files for creating or extending your own skill setup;
- supporting documentation for structure, safety, and adaptation.

## What you are meant to copy

You are encouraged to copy and adapt:

- the `SKILL.md` structure;
- the activation pattern;
- the scope and stop rules;
- the final report format;
- the safety boundaries;
- the optional script pattern;
- the template pattern;
- the check pattern;
- the passive review pattern, when useful.

Do not copy blindly. Read the files, remove what you do not need, and test the skill on a small task first.

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

## Create your own skill in 7 steps

1. Download or clone this repository.
2. Fill in `templates/skill-config-template.md`.
3. Open `prompts/create-my-skill-from-config.md`.
4. Paste the prompt into your coding agent.
5. Let it generate your custom skill folder.
6. Review the generated files.
7. Test the skill on a small task.

Start here:
- [START_HERE.md](START_HERE.md)
- [Skill configuration template](templates/skill-config-template.md)
- [Create my skill prompt](prompts/create-my-skill-from-config.md)

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

1. Pick the closest example.
2. Copy the folder.
3. Rename the folder.
4. Open `SKILL.md`.
5. Change the skill name.
6. Change the activation line.
7. Adjust scope and preferences.
8. Remove unused scripts, templates, or checks.
9. Run a small test task.
10. Improve only after the first real use.

## Customize your skill

Customization should be small at first.

Start with:

- name;
- description;
- activation line;
- scope;
- forbidden actions;
- final report format;
- local paths, if any;
- scripts, only if they make a repeated step safer or easier;
- templates, only if you want consistent output;
- checks, only if the requirement is mechanically verifiable.

Keep the first version readable. A skill that is easy to inspect is better than a clever skill that nobody understands.

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
- [Create your own skill](docs/11-create-your-own-skill.md)

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
