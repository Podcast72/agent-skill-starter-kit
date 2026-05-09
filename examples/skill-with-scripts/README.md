# Skill With Scripts Example

This example shows how a skill can combine instructions with small helper scripts, one output template and one validation script.

The scripts are intentionally simple:

- `mode_detect.py` classifies a request.
- `scope_guard.py` checks whether a path stays inside an allowed root.
- `report_check.py` validates required report sections.
- `validate_skill.py` validates the example folder.

Use this example when you want more structure than a single `SKILL.md`, but still want the setup to remain easy to inspect.
