---
name: fullstack-app-builder
description: End-to-end workflow for building production web apps with code-based AI assistants, from idea to deployed product. Guides non-developers through requirements, architecture, infrastructure setup (GitHub, Supabase, Railway), landing page creation (Lovable or WordPress with SEO/GEO), and generates numbered session prompts. Use when user wants to build a web app, SaaS product, internal tool, or platform. Triggers on: 'neue App', 'App-Projekt starten', 'build an app', 'Plattform entwickeln', 'web app erstellen', 'app architecture', 'Railway deployment', 'Session-Prompts erstellen', 'Fullstack-App', 'App mit Supabase', 'ich will eine App bauen', or any production application on real infrastructure. Do NOT use for Lovable-only builds (use lovable-app-builder instead)."
---

# Fullstack App Builder — Kimi Code CLI wrapper

This is the **Kimi Code CLI wrapper** for `fullstack-app-builder`. The full skill definition lives in `shared/SKILL-CORE.md` in the same skill folder.

## When to use

Use when the user asks for:
- `/fullstack-app-builder`
- "run fullstack-app-builder"
- Any trigger described in the core skill

## How to invoke

In Kimi Code CLI:

```
/fullstack-app-builder
```

## Instructions

1. Read `shared/SKILL-CORE.md` for the platform-agnostic workflow, rules, and examples.
2. Execute the workflow using Kimi Code CLI tools.
3. Load any referenced files from `shared/` or subdirectories relative to this skill folder.

## References

- `shared/SKILL-CORE.md` — full skill definition
