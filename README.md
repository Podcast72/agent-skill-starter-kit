# Agent Skill Starter Kit

A practical example repository for creating reusable local skills for coding agents.

This repository shows a simple way to organize agent skills using:
- a `SKILL.md` instruction file;
- optional scripts for repeatable tasks;
- templates for consistent outputs;
- checks for basic validation;
- optional hooks for guardrails;
- an experimental passive skill pattern for minimal, manual review signals.

It is not a framework, not a formal standard, and not a production system.
It is a starting point that you can copy, rename and adapt to your own workflow.

## What this repository is

This repository is a starter kit for organizing local agent skills in a way that is easy to read, copy and extend. It uses simple folders, Markdown instructions and small Python scripts to show how a repeatable local agent workflow can be documented.

## What this repository is not

- It is not a formal standard.
- It is not a production framework.
- It is not a security product.
- It is not an autonomous self-improving system.
- It is not tied to one private project.
- It is not a replacement for testing and review.

## Why skills are useful

A normal prompt is useful for one interaction.
A reusable skill can preserve instructions and workflow rules across repeated tasks.
Scripts, templates and checks can make repeatable work more stable.

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

- `docs/` explains concepts, safety notes and adaptation steps.
- `examples/` contains copyable skill examples with increasing structure.
- `templates/` provides reusable starting files.
- `prompts/` contains helper prompts for creating or extending skills.
- `diagrams/` contains a simple Mermaid workflow diagram.

## Quick start

1. Copy one example folder from `examples/`.
2. Rename the folder and the skill name.
3. Edit the `SKILL.md` frontmatter.
4. Adapt the instructions to your workflow.
5. Add scripts only where they help.
6. Run the checks.
7. Test with a small task before using it on real work.

## Safety guidelines

- Do not store secrets in skills.
- Do not scan broad filesystem paths by default.
- Do not run destructive commands by default.
- Do not use `sudo` by default.
- Do not install global packages by default.
- Do not run `git push` by default.
- Keep scripts small and readable.
- Keep hooks few and deterministic.
- Always report what was changed and what was not checked.

## Experimental passive skill pattern

The experimental passive skill pattern is a simple example of how a skill can record minimal usage metadata for later manual review.

It must not:
- store full prompts;
- store secrets;
- auto-upgrade;
- modify itself;
- modify global configuration;
- install hooks automatically;
- make automatic improvement decisions.

## Documentation

- [01 - What are agent skills](docs/01-what-are-agent-skills.md)
- [02 - Why use skills](docs/02-why-use-skills.md)
- [03 - Basic architecture](docs/03-basic-architecture.md)
- [04 - Skill folder structure](docs/04-skill-folder-structure.md)
- [05 - Scripts, templates, checks](docs/05-scripts-templates-checks.md)
- [06 - Optional hooks](docs/06-optional-hooks.md)
- [07 - Experimental passive skill](docs/07-experimental-passive-skill.md)
- [08 - Safety guidelines](docs/08-safety-guidelines.md)
- [09 - How to adapt](docs/09-how-to-adapt.md)
- [10 - FAQ](docs/10-faq.md)

## Disclaimer

This repository is an educational starter kit. Review and test every script before using it in your own environment.
