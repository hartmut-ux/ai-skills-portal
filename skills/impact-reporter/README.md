# impact-reporter

Erstellt Impact Reports, Impact Sections für Förderanträge und Fortschrittsberichte für jede Art von Projekt – ob EU-gefördert (Erasmus+, Horizon Europe, Creative Europe, Interreg), Schweizer Programme (Innosuisse, SNF, Movetia) oder B Corp Zertifizierung. Deckt den gesamten Lifecycle ab: von Impact-Abschnitten in Proposals über Zwischenberichte bis zum Abschlussbericht. Nutze diesen Skill immer wenn der User Impact Reporting, Wirkungsmessung, Projektevaluation, Logical Frameworks, Theory of Change, KPIs für Förderprojekte, Nachhaltigkeitsberichte, oder B Impact Assessments erwähnt – auch wenn nicht explizit von 'Impact Report' die Rede ist.

## Structure

```text
impact-reporter/
├── README.md
├── shared/
│   └── SKILL-CORE.md          # Platform-agnostic skill definition
├── .kimi/skills/impact-reporter/
│   └── SKILL.md               # Kimi wrapper
├── .claude/skills/impact-reporter/
│   └── SKILL.md               # Claude wrapper
└── .codex/skills/impact-reporter/
    └── SKILL.md               # Codex wrapper
```

## Packaging

From the repository root:

```bash
python scripts/package-skill.py impact-reporter
```
