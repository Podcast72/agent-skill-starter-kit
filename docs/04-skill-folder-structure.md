# Skill Folder Structure

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

- `SKILL.md` defines behavior and rules.
- `scripts/` contains helpers for repeatable tasks.
- `templates/` contains stable output formats.
- `checks/` contains validation helpers.
- `examples/` contains expected outputs or usage examples.
- `README.md` explains the folder for human readers.

Not every skill needs every folder. A small skill can start with only `SKILL.md` and `README.md`.
