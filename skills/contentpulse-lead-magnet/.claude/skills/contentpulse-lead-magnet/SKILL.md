---
name: contentpulse-lead-magnet
description: Erstellt professionelle Lead Magnets aus ContentPulse-Exports: Cheat Sheets (HTML/CSS via branded-visual-factory), Whitepapers (.docx), Präsentationen (.pptx). Nimmt strukturierte Prompts aus ContentPulse entgegen mit Thema, Research-Summary, Quellen-Links, Brand-Profil und Format-Wahl. Use when user pastes a ContentPulse lead magnet prompt, mentions 'ContentPulse Lead Magnet', 'Lead Magnet erstellen', 'Cheat Sheet aus ContentPulse', 'Whitepaper erstellen', 'Präsentation aus Research', or when a structured JSON block with contentpulse_export marker is present. Also triggers on: 'Lead Magnet aus meiner Recherche', 'mach ein Cheat Sheet zu', 'erstelle ein Whitepaper', 'Präsentation aus Wiki-Wissen'.
---

# Contentpulse Lead Magnet — Claude Code wrapper

This is the **Claude Code wrapper** for `contentpulse-lead-magnet`. The full skill definition lives in `shared/SKILL-CORE.md` in the same skill folder.

## When to use

Use when the user asks for:
- `contentpulse-lead-magnet`
- "run contentpulse-lead-magnet"
- Any trigger described in the core skill

## How to invoke

In Claude Code:

```
contentpulse-lead-magnet
```

## Instructions

1. Read `shared/SKILL-CORE.md` for the platform-agnostic workflow, rules, and examples.
2. Execute the workflow using Claude Code tools.
3. Load any referenced files from `shared/` or subdirectories relative to this skill folder.

## References

- `shared/SKILL-CORE.md` — full skill definition
