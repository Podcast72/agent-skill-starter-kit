# Optional Hooks

Hooks are optional.
They should be few, small, deterministic and non-destructive.

Common examples:

- pre-prompt mode guard;
- pre-tool scope guard;
- post-response report check.

Hooks can be helpful when the same guardrail is needed often, but too many hooks can make a setup fragile or hard to understand.
