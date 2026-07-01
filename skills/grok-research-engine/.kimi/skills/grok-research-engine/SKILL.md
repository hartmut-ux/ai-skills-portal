---
name: grok-research-engine
description: Deep research engine powered by the Grok API with web search, X/Twitter search, and multi-agent reasoning. Use this skill whenever the user wants to research a topic before creating content, needs current trends/news/statistics with source links, wants to find top-performing tweets or LinkedIn posts on a topic, needs scientific papers or expert opinions, or asks for market/competitor analysis with citations. Triggers on: 'recherchiere', 'research', 'finde aktuelle Quellen', 'was sagt die Forschung', 'aktuelle Trends zu', 'top posts zum Thema', 'Quellenrecherche', 'Deep Research', 'Grok research', 'find sources', 'what are people saying about', 'trending on X', or any research-before-content request. Also triggers when content-engine or content-strategist need a research foundation — this skill runs BEFORE content creation. Always use this skill when the user needs current, sourced information that goes beyond Claude's training data.
---

# Grok Research Engine — Kimi Code CLI wrapper

This is the **Kimi Code CLI wrapper** for `grok-research-engine`. The full skill definition lives in `shared/SKILL-CORE.md` in the same skill folder.

## When to use

Use when the user asks for:
- `/grok-research-engine`
- "run grok-research-engine"
- Any trigger described in the core skill

## How to invoke

In Kimi Code CLI:

```
/grok-research-engine
```

## Instructions

1. Read `shared/SKILL-CORE.md` for the platform-agnostic workflow, rules, and examples.
2. Execute the workflow using Kimi Code CLI tools.
3. Load any referenced files from `shared/` or subdirectories relative to this skill folder.

## References

- `shared/SKILL-CORE.md` — full skill definition
