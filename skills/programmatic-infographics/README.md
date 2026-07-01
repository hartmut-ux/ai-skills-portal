# programmatic-infographics

Creating programmatic infographics and generative visual art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating infographics using code, generative art, algorithmic art, data visualizations, flow fields, or particle systems.

## Structure

```text
programmatic-infographics/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/programmatic-infographics/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/programmatic-infographics/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/programmatic-infographics/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py programmatic-infographics
```
