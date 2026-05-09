#!/usr/bin/env python3
import json
import sys


POWER_TERMS = [
    "sudo",
    "npm install -g",
    "pip install --user",
    "pip install global",
    "git push",
    "git commit",
    "git reset",
    "git clean",
    "rm -rf",
    "chmod",
    "chown",
    "token",
    "secret",
    ".env",
    "credentials",
    "download",
    "network",
    "curl",
    "wget",
]

BUILD_TERMS = [
    "create file",
    "modify file",
    "patch",
    "write docs",
    "run test",
    "local script",
]

SAFE_TERMS = [
    "read",
    "review",
    "analyze",
    "audit",
    "summarize",
    "inspect",
]


def load_text() -> str:
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    return sys.stdin.read()


def main() -> int:
    text = load_text().strip()
    lowered = text.lower()

    reasons = []
    risk_flags = []
    mode = "NEEDS_CONFIRMATION"

    for term in POWER_TERMS:
        if term in lowered:
            mode = "POWER"
            reasons.append(f"matched power term: {term}")
            risk_flags.append(term)

    if mode != "POWER":
        build_matches = [term for term in BUILD_TERMS if term in lowered]
        safe_matches = [term for term in SAFE_TERMS if term in lowered]

        if build_matches:
            mode = "BUILD"
            reasons.extend(f"matched build term: {term}" for term in build_matches)
        elif safe_matches:
            mode = "SAFE"
            reasons.extend(f"matched safe term: {term}" for term in safe_matches)
        else:
            reasons.append("no known keywords matched")

    print(
        json.dumps(
            {
                "mode": mode,
                "reasons": reasons,
                "risk_flags": risk_flags,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
