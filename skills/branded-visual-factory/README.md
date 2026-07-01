# branded-visual-factory

Generates on-brand HTML/CSS infographics, cheat sheets, data cards, and carousel slides as code — fully editable, pixel-perfect, PNG-exportable. Supports multiple brands (MMIND.ai, FlowMomentum.ai). Use whenever the user wants to create a branded infographic, cheat sheet, visual content card, social media graphic, data visualization, carousel, or any visual content piece that should follow brand guidelines. Also triggers on: 'erstelle eine Infografik', 'Cheat Sheet', 'Visual erstellen', 'branded graphic', 'LinkedIn Visual', 'Daten-Karte', 'Social Media Grafik', 'Infographic', 'visuellen Content erstellen', or when content-engine requests a visual deliverable. Do NOT use for generative art or p5.js sketches (use programmatic-infographics instead) or for AI image generation prompts (use brand-guardian instead).

## Structure

```text
branded-visual-factory/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/branded-visual-factory/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/branded-visual-factory/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/branded-visual-factory/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py branded-visual-factory
```
