# critical-thinking-guardian

Background quality-control skill that applies critical thinking best practices to EVERY conversation. Runs as a silent guardian layer — catching logical fallacies, challenging unexamined assumptions, ensuring evidence-based reasoning, and promoting intellectual humility. Use this skill on EVERY response Claude generates, regardless of topic. It is especially important when the user or Claude makes claims, proposes strategies, evaluates options, drafts arguments, analyzes data, or makes decisions. Also triggers on: 'prüfe meine Logik', 'stimmt das wirklich', 'ist das ein gutes Argument', 'check my reasoning', 'devil's advocate', 'Gegenargumente', 'Denkfehler', 'bias check', 'assumption check', or any situation where reasoning quality matters — which is every situation.

## Structure

```text
critical-thinking-guardian/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/critical-thinking-guardian/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/critical-thinking-guardian/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/critical-thinking-guardian/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py critical-thinking-guardian
```
