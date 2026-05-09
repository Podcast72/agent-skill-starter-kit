# Evolution Notes

Minimal metadata means small fields such as event type, task type, mode, status and timestamp.

Full prompt text should not be logged because it may contain sensitive or unnecessary detail.

This pattern is passive because it only records minimal metadata when explicitly allowed.

Review logs manually by opening `usage_log.jsonl`, checking the event fields and deciding whether any workflow changes are worth documenting by hand.

No automatic upgrade is performed.
