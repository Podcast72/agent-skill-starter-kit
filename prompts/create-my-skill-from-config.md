# Create my skill from config

```text
You are working inside a local copy of agent-skill-starter-kit.

Your task is to generate a custom local skill using the configuration file:

templates/skill-config-template.md

Read the filled configuration first.

Use the method in this repository as the operating pattern:
- SKILL.md for operating instructions;
- clear activation line;
- clear scope;
- explicit forbidden actions;
- small optional scripts only when useful;
- templates only when useful;
- checks only when mechanically verifiable;
- optional passive review logging only if requested;
- final report explaining what was generated, what was customized, what was checked, and what still needs review.

Use the examples in examples/ as references, but do not copy blindly.

Create a new skill folder using the configured skill name.

The generated skill should normally include:
- SKILL.md;
- README.md;
- optional scripts/;
- optional templates/;
- optional checks/.

Rules:
- Do not use secrets.
- Do not invent private paths.
- Do not use personal data.
- Do not run git push.
- Do not use sudo.
- Do not install global packages.
- Do not create destructive commands.
- Do not create self-modifying behavior.
- Do not install hooks automatically.
- Do not claim the skill is production-ready, verified, enterprise-ready, or a security product.
- Keep the generated skill readable and easy to inspect.

Before finishing, check:
- the skill name was replaced everywhere needed;
- the activation line is correct;
- the scope is clear;
- forbidden actions are present;
- optional components match the config;
- the final report format is present;
- there are no secrets or private paths.

Final response format:

GENERATED FILES
- ...

CUSTOMIZED FROM CONFIG
- ...

METHOD PARTS REUSED
- ...

OPTIONAL COMPONENTS INCLUDED
- ...

CHECKS RUN
- ...

LIMITS
- ...

FINAL STATUS
- CUSTOM_SKILL_READY_FOR_LOCAL_REVIEW or explain the problem.
```
