#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Append minimal usage metadata to a JSONL log.")
    parser.add_argument("--event-type", required=True)
    parser.add_argument("--task-type", required=True)
    parser.add_argument("--mode", required=True)
    parser.add_argument("--status", required=True)
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parents[1]
    evolution_dir = base_dir / "evolution"
    evolution_dir.mkdir(parents=True, exist_ok=True)
    log_path = evolution_dir / "usage_log.jsonl"

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": args.event_type,
        "task_type": args.task_type,
        "mode": args.mode,
        "status": args.status,
    }

    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=True) + "\n")

    print(json.dumps({"ok": True, "log_path": "evolution/usage_log.jsonl"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
