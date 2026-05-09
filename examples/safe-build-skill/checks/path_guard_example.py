#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def check_path(target_raw: str, allowed_root_raw: str) -> dict:
    if not target_raw.strip():
        return {"allowed": False, "reason": "target path is empty"}

    target = Path(target_raw).expanduser().resolve()
    allowed_root = Path(allowed_root_raw).expanduser().resolve()

    if not allowed_root.exists():
        return {"allowed": False, "reason": "allowed root does not exist"}

    if str(target) == "/":
        return {"allowed": False, "reason": "root path is not allowed"}

    if not target.exists():
        return {"allowed": False, "reason": "target path does not exist"}

    try:
        target.relative_to(allowed_root)
    except ValueError:
        return {"allowed": False, "reason": "target path is outside the allowed root"}

    return {"allowed": True, "reason": "target path is inside the allowed root"}


def main() -> int:
    if len(sys.argv) != 3:
        print(json.dumps({"allowed": False, "reason": "usage: path_guard_example.py <target_path> <allowed_root>"}, indent=2))
        return 1

    print(json.dumps(check_path(sys.argv[1], sys.argv[2]), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
