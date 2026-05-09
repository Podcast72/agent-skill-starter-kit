#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def build_entry(event_type: str, task_type: str, mode: str, status: str) -> dict:
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "task_type": task_type,
        "mode": mode,
        "status": status,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Write minimal usage metadata for manual review.")
    parser.add_argument("--event-type", required=True)
    parser.add_argument("--task-type", required=True)
    parser.add_argument("--mode", required=True)
    parser.add_argument("--status", required=True)
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parents[1]
    evolution_dir = base_dir / "evolution"
    evolution_dir.mkdir(parents=True, exist_ok=True)
    log_path = evolution_dir / "usage_log_example.jsonl"

    entry = build_entry(args.event_type, args.task_type, args.mode, args.status)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=True) + "\n")

    print(json.dumps({"ok": True, "log_path": "evolution/usage_log_example.jsonl"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
