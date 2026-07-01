# first-principles-engine

Strips any topic down to its fundamental truths using Elon Musk's first principles methodology — deletion, presence at the problem, and relentless speed. Use this skill whenever the user wants to deeply analyze a topic, challenge assumptions, rethink a business model, question conventional wisdom, do a first principles analysis, strip something down to basics, or says things like "break this down", "what's really true here", "challenge my assumptions", "rethink this from scratch", "what am I missing", or "strip this down". Also triggers for strategic analysis, competitive rethinking, innovation brainstorming, or when the user wants to rebuild a concept from the ground up. Do NOT use for simple factual questions, quick summaries, or routine document creation.

## Structure

```text
first-principles-engine/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/first-principles-engine/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/first-principles-engine/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/first-principles-engine/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py first-principles-engine
```
