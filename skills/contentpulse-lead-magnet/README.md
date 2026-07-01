# contentpulse-lead-magnet

Erstellt professionelle Lead Magnets aus ContentPulse-Exports: Cheat Sheets (HTML/CSS via branded-visual-factory), Whitepapers (.docx), Präsentationen (.pptx). Nimmt strukturierte Prompts aus ContentPulse entgegen mit Thema, Research-Summary, Quellen-Links, Brand-Profil und Format-Wahl. Use when user pastes a ContentPulse lead magnet prompt, mentions 'ContentPulse Lead Magnet', 'Lead Magnet erstellen', 'Cheat Sheet aus ContentPulse', 'Whitepaper erstellen', 'Präsentation aus Research', or when a structured JSON block with contentpulse_export marker is present. Also triggers on: 'Lead Magnet aus meiner Recherche', 'mach ein Cheat Sheet zu', 'erstelle ein Whitepaper', 'Präsentation aus Wiki-Wissen'.

## Structure

```text
contentpulse-lead-magnet/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/contentpulse-lead-magnet/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/contentpulse-lead-magnet/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/contentpulse-lead-magnet/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py contentpulse-lead-magnet
```
