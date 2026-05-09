# Skill Configuration Template

Copy this file, fill it in, and give it to your coding agent together with the prompt in `prompts/create-my-skill-from-config.md`.

The goal is simple: keep the method, change the name and preferences, and generate a local skill you can inspect and test.

## Skill name

Example: `my-review-skill`

Your skill name:

```text
CHANGE_ME
```

## Activation line

Example: `$my-review-skill`

Your activation line:

```text
$CHANGE_ME
```

## Short description

What should this skill help with?

```text
CHANGE_ME
```

## Main workflow

Describe the repeated workflow you want to turn into a skill.

```text
CHANGE_ME
```

## Allowed scope

What is the skill allowed to work on?

```text
CHANGE_ME
```

## Forbidden actions

Keep, remove, or add rules.

```text
- Do not run git push.
- Do not use sudo.
- Do not install global packages.
- Do not modify files outside the declared scope.
- Do not store secrets.
- Do not scan broad filesystem paths by default.
```

## Preferred final report

Choose the final report sections you want.

```text
FILES CHANGED
WHAT WAS DONE
CHECKS RUN
LIMITS
FINAL STATUS
```

## Optional scripts

Use scripts only for small repeatable helpers.

```text
yes/no
```

## Optional templates

Use templates only if you want consistent output.

```text
yes/no
```

## Optional checks

Use checks only for requirements that can be mechanically verified.

```text
yes/no
```

## Passive review logging

Experimental. Use only if you want minimal metadata for later manual review.

```text
yes/no
```

## Extra preferences

Add any personal preferences here.

```text
CHANGE_ME
```
