# Safety Guidelines

This safety model is a practical example, not a formal security standard.

## SAFE

- read-only;
- audit;
- documentation;
- analysis;
- no file modifications.

## BUILD

- local controlled changes;
- small patches;
- new documentation;
- local checks;
- local tests;
- no destructive actions.

## POWER

- `sudo`;
- global installs;
- `git push`;
- `git reset`;
- `git clean`;
- `rm -rf`;
- `chmod` or `chown`;
- network access;
- secret handling;
- broad filesystem operations;
- global configuration changes.

## NEEDS CONFIRMATION

- unclear scope;
- ambiguous path;
- destructive request;
- missing success criteria;
- sensitive files involved.
