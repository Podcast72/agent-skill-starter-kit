# Start here: create your own local skill

## What this does

This repository shares a practical working method for creating local skills that make coding agents more consistent, reusable, and easier to guide.

You can copy the method, choose your own skill name, adjust your preferences, and ask your coding agent to generate a custom skill folder.

This is not an installer, not a framework, and not a guaranteed system. It is a practical starting structure that you can inspect, adapt, and test locally.

## The simple workflow

1. Download or clone this repository.
2. Open `templates/skill-config-template.md`.
3. Fill in your skill name and preferences.
4. Open `prompts/create-my-skill-from-config.md`.
5. Paste that prompt into your coding agent.
6. Let the agent generate your custom skill folder.
7. Review the generated files.
8. Test the skill on a small local task.

## What you need to choose

- skill name;
- activation line;
- short description;
- main workflow;
- allowed scope;
- forbidden actions;
- preferred final report;
- whether to use optional scripts;
- whether to use optional templates;
- whether to use optional checks;
- whether to use passive review logging.

## What the agent should generate

A custom skill folder containing, depending on your configuration:

- `SKILL.md`;
- `README.md`;
- optional `scripts/`;
- optional `templates/`;
- optional `checks/`.

## What to review before using it

Before using the generated skill, check that it does not contain:

- secrets;
- personal paths unless you intentionally added them;
- destructive commands;
- broad filesystem scans;
- automatic `git push`;
- automatic global installs;
- self-modifying behavior;
- automatic hook installation.

Also check that the final report format is clear and that the skill can explain what it changed, what it checked, and what it did not check.

## First safe test

Use the generated skill on a small, local, low-risk task first.

Examples:

- ask it to review a short README;
- ask it to format a small documentation file;
- ask it to inspect one folder with a narrow scope;
- ask it to produce a final report without modifying files.

Do not start with a large project or destructive task.

## Important limits

This repository gives you a method and a starting structure. You still need to read the generated files, remove what you do not need, and test the skill in your own environment.
