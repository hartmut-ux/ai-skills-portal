# grok-research-engine

Deep research engine powered by the Grok API with web search, X/Twitter search, and multi-agent reasoning. Use this skill whenever the user wants to research a topic before creating content, needs current trends/news/statistics with source links, wants to find top-performing tweets or LinkedIn posts on a topic, needs scientific papers or expert opinions, or asks for market/competitor analysis with citations. Triggers on: 'recherchiere', 'research', 'finde aktuelle Quellen', 'was sagt die Forschung', 'aktuelle Trends zu', 'top posts zum Thema', 'Quellenrecherche', 'Deep Research', 'Grok research', 'find sources', 'what are people saying about', 'trending on X', or any research-before-content request. Also triggers when content-engine or content-strategist need a research foundation — this skill runs BEFORE content creation. Always use this skill when the user needs current, sourced information that goes beyond Claude's training data.

## Structure

```text
grok-research-engine/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/grok-research-engine/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/grok-research-engine/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/grok-research-engine/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py grok-research-engine
```
