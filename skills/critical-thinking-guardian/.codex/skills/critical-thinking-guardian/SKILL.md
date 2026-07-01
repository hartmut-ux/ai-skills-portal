---
name: critical-thinking-guardian
description: Background quality-control skill that applies critical thinking best practices to EVERY conversation. Runs as a silent guardian layer — catching logical fallacies, challenging unexamined assumptions, ensuring evidence-based reasoning, and promoting intellectual humility. Use this skill on EVERY response Claude generates, regardless of topic. It is especially important when the user or Claude makes claims, proposes strategies, evaluates options, drafts arguments, analyzes data, or makes decisions. Also triggers on: 'prüfe meine Logik', 'stimmt das wirklich', 'ist das ein gutes Argument', 'check my reasoning', 'devil's advocate', 'Gegenargumente', 'Denkfehler', 'bias check', 'assumption check', or any situation where reasoning quality matters — which is every situation.
---

# Critical Thinking Guardian — Codex CLI wrapper

This is the **Codex CLI wrapper** for `critical-thinking-guardian`. The full skill definition lives in `shared/SKILL-CORE.md` in the same skill folder.

## When to use

Use when the user asks for:
- `critical-thinking-guardian`
- "run critical-thinking-guardian"
- Any trigger described in the core skill

## How to invoke

In Codex CLI:

```
critical-thinking-guardian
```

## Instructions

1. Read `shared/SKILL-CORE.md` for the platform-agnostic workflow, rules, and examples.
2. Execute the workflow using Codex CLI tools.
3. Load any referenced files from `shared/` or subdirectories relative to this skill folder.

## References

- `shared/SKILL-CORE.md` — full skill definition
