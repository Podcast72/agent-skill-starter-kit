#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path


BLOCKED_PATHS = {"/", "/etc", "/System", "/Library"}


def result(allowed: bool, reason: str) -> int:
    print(json.dumps({"allowed": allowed, "reason": reason}, indent=2))
    return 0


def main() -> int:
    if len(sys.argv) != 3:
        return result(False, "usage: scope_guard.py <target_path> <allowed_root>")

    target_raw = sys.argv[1].strip()
    allowed_root_raw = sys.argv[2].strip()

    if not target_raw:
        return result(False, "target path is empty")

    if target_raw in BLOCKED_PATHS:
        return result(False, f"target path is blocked: {target_raw}")

    home_dir = str(Path.home().resolve())
    if os.path.abspath(target_raw) == home_dir:
        return result(False, "target path cannot be the user home directory")

    target_path = Path(target_raw).expanduser().resolve()
    allowed_root = Path(allowed_root_raw).expanduser().resolve()

    if not target_path.exists():
        return result(False, "target path does not exist")

    if not allowed_root.exists():
        return result(False, "allowed root does not exist")

    try:
        target_path.relative_to(allowed_root)
    except ValueError:
        return result(False, "target path is outside the allowed root")

    return result(True, "target path is inside the allowed root")


if __name__ == "__main__":
    raise SystemExit(main())
