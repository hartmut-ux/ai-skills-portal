# token-saver

Reduziert Token-Verbrauch in Claude-Sessions massiv (50-95%) durch sieben Hebel - Output-Komprimierung, Symbol-First Code-Reading, Tool-Output-Filtering, Docs-Compression, Ghost-Token-Hygiene, Session-State-Management und MCP-Tool-Awareness. Use this skill whenever the user mentions 'Token sparen', 'Context-Limit', 'spart Tokens', 'terser mode', 'caveman mode', 'context window voll', 'API-Kosten reduzieren', 'Claude wird langsam', 'zu viel Output', 'kürzer antworten', 'less context', 'reduce tokens', 'optimize context', 'token budget', 'cost optimization', '/compact', 'neue Session', 'session zu lang', oder wenn der User in einer langen Session arbeitet und merkt, dass der Kontext überläuft. Auch triggern wenn der User vor einer grossen Operation steht (Monorepo-Analyse, viele Dateien lesen, lange Logs auswerten) und proaktiv Tokens sparen will. NICHT triggern für reine Inhalts-Komprimierung von Texten (das ist humanizer-Job) oder für RAG-Optimierung (das ist rag-text-optimizer-Job).

## Structure

```text
token-saver/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/token-saver/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/token-saver/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/token-saver/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py token-saver
```
