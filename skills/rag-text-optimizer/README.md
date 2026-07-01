# rag-text-optimizer

>

## Structure

```text
rag-text-optimizer/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/rag-text-optimizer/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/rag-text-optimizer/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/rag-text-optimizer/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py rag-text-optimizer
```
