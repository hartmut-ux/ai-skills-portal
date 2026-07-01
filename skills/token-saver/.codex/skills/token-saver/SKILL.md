---
name: token-saver
description: Reduziert Token-Verbrauch in Claude-Sessions massiv (50-95%) durch sieben Hebel - Output-Komprimierung, Symbol-First Code-Reading, Tool-Output-Filtering, Docs-Compression, Ghost-Token-Hygiene, Session-State-Management und MCP-Tool-Awareness. Use this skill whenever the user mentions 'Token sparen', 'Context-Limit', 'spart Tokens', 'terser mode', 'caveman mode', 'context window voll', 'API-Kosten reduzieren', 'Claude wird langsam', 'zu viel Output', 'kürzer antworten', 'less context', 'reduce tokens', 'optimize context', 'token budget', 'cost optimization', '/compact', 'neue Session', 'session zu lang', oder wenn der User in einer langen Session arbeitet und merkt, dass der Kontext überläuft. Auch triggern wenn der User vor einer grossen Operation steht (Monorepo-Analyse, viele Dateien lesen, lange Logs auswerten) und proaktiv Tokens sparen will. NICHT triggern für reine Inhalts-Komprimierung von Texten (das ist humanizer-Job) oder für RAG-Optimierung (das ist rag-text-optimizer-Job).
---

# Token Saver — Codex CLI wrapper

This is the **Codex CLI wrapper** for `token-saver`. The full skill definition lives in `shared/SKILL-CORE.md` in the same skill folder.

## When to use

Use when the user asks for:
- `token-saver`
- "run token-saver"
- Any trigger described in the core skill

## How to invoke

In Codex CLI:

```
token-saver
```

## Instructions

1. Read `shared/SKILL-CORE.md` for the platform-agnostic workflow, rules, and examples.
2. Execute the workflow using Codex CLI tools.
3. Load any referenced files from `shared/` or subdirectories relative to this skill folder.

## References

- `shared/SKILL-CORE.md` — full skill definition
