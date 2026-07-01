# fullstack-app-builder

End-to-end workflow for building production web apps with code-based AI assistants, from idea to deployed product. Guides non-developers through requirements, architecture, infrastructure setup (GitHub, Supabase, Railway), landing page creation (Lovable or WordPress with SEO/GEO), and generates numbered session prompts. Use when user wants to build a web app, SaaS product, internal tool, or platform. Triggers on: 'neue App', 'App-Projekt starten', 'build an app', 'Plattform entwickeln', 'web app erstellen', 'app architecture', 'Railway deployment', 'Session-Prompts erstellen', 'Fullstack-App', 'App mit Supabase', 'ich will eine App bauen', or any production application on real infrastructure. Do NOT use for Lovable-only builds (use lovable-app-builder instead)."

## Structure

```text
fullstack-app-builder/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/fullstack-app-builder/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/fullstack-app-builder/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/fullstack-app-builder/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py fullstack-app-builder
```
