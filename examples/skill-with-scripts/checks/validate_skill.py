#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def main() -> int:
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]

    errors = []
    skill_file = target / "SKILL.md"

    if not skill_file.exists():
        errors.append("SKILL.md is missing")
    else:
        content = skill_file.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(content)
        if not match:
            errors.append("SKILL.md frontmatter is missing")
        else:
            frontmatter = match.group(1)
            if "name:" not in frontmatter:
                errors.append("frontmatter missing name")
            if "description:" not in frontmatter:
                errors.append("frontmatter missing description")

    for folder_name in ["scripts", "templates", "checks"]:
        if not (target / folder_name).is_dir():
            errors.append(f"{folder_name} folder is missing")

    print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
