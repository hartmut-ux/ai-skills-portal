# digitalscheck-navigator

Begleitet KMU durch alle drei Module des Digitalscheck Liechtenstein (KONZEPT, INVEST, TRAINING). Erstellt Anträge, Offerten, Kostenrechnungen, Prozessanalysen (IST/SOLL), Massnahmenpläne, Implementierungspläne und Abschlussberichte – alles konform zur AVW-Richtlinie 2025. Nutze diesen Skill immer wenn ein Nutzer den Digitalscheck, eine Digitalisierungsförderung in Liechtenstein, ein KMU-Digitalisierungsprojekt mit Fördermitteln, oder Module wie Digital KONZEPT, Digital INVEST oder Digital TRAINING erwähnt. Auch bei Begriffen wie 'Amt für Volkswirtschaft Förderung', 'Digitalisierungsscheck FL', 'KMU-Förderung Liechtenstein' oder wenn ein Angebot, Antrag oder Abschlussbericht für ein Digitalischeck-Projekt erstellt werden soll.

## Structure

```text
digitalscheck-navigator/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/digitalscheck-navigator/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/digitalscheck-navigator/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/digitalscheck-navigator/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py digitalscheck-navigator
```
