---
name: humanizer
description: Erkennt und entfernt typische KI-Sprachmuster aus Texten (Deutsch CH, Deutsch DE, US-English, British English), damit Inhalte natürlich und menschlich klingen. Trigger 'humanisiere', 'menschlicher klingen', 'KI-Sprache entfernen', 'mach das menschlicher', 'humanize', 'remove AI patterns', 'Schweizer Hochdeutsch', 'für die Schweiz', 'in British English', oder wenn User AI-generierten Text zur Überarbeitung einfügt. Deckt 29 EN-Patterns + 18 DE-Patterns + CH-Blacklist (Guillemets, Apostroph-Tausender, Em-dash-Vermeidung, Helvetismen, ss statt ß) + British-English-Modus (organise/colour/centre) ab. Optional Voice-Kalibrierung auf Marken (MMIND.ai, Kaizen, Flowstate, Hartmut persönlich).
---

# Humanizer — Kimi Code CLI wrapper

This is the **Kimi Code CLI wrapper** for `humanizer`. The full skill definition lives in `shared/SKILL-CORE.md` in the same skill folder.

## When to use

Use when the user asks for:
- `/humanizer`
- "run humanizer"
- Any trigger described in the core skill

## How to invoke

In Kimi Code CLI:

```
/humanizer
```

## Instructions

1. Read `shared/SKILL-CORE.md` for the platform-agnostic workflow, rules, and examples.
2. Execute the workflow using Kimi Code CLI tools.
3. Load any referenced files from `shared/` or subdirectories relative to this skill folder.

## References

- `shared/SKILL-CORE.md` — full skill definition
