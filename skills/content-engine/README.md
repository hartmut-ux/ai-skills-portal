# content-engine

Universal content creation engine for newsletters, LinkedIn posts, blog articles, thought leadership, and multi-format content repurposing. Use this skill whenever the user wants to create a newsletter edition, write LinkedIn posts, draft blog articles, create whiteboard graphic prompts, develop editorial calendars, repurpose content across formats, or produce any structured marketing content — for MMIND.ai, Hartmut Hübner personal, or any new brand. Also triggers when the user mentions 'newsletter', 'LinkedIn post', 'content calendar', 'editorial', 'teaser', 'carousel', 'whiteboard graphic', 'Nano Banana prompt', 'content repurposing', 'ghost-writing', 'thought leadership', 'WEF blog', or any content production task. For Kaizen Institute content, use the dedicated Kaizen skill instead.

## Structure

```text
content-engine/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/content-engine/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/content-engine/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/content-engine/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py content-engine
```
