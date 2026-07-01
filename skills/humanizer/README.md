# humanizer

Erkennt und entfernt typische KI-Sprachmuster aus Texten (Deutsch CH, Deutsch DE, US-English, British English), damit Inhalte natürlich und menschlich klingen. Trigger 'humanisiere', 'menschlicher klingen', 'KI-Sprache entfernen', 'mach das menschlicher', 'humanize', 'remove AI patterns', 'Schweizer Hochdeutsch', 'für die Schweiz', 'in British English', oder wenn User AI-generierten Text zur Überarbeitung einfügt. Deckt 29 EN-Patterns + 18 DE-Patterns + CH-Blacklist (Guillemets, Apostroph-Tausender, Em-dash-Vermeidung, Helvetismen, ss statt ß) + British-English-Modus (organise/colour/centre) ab. Optional Voice-Kalibrierung auf Marken (MMIND.ai, Kaizen, Flowstate, Hartmut persönlich).

## Structure

```text
humanizer/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/humanizer/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/humanizer/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/humanizer/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py humanizer
```
