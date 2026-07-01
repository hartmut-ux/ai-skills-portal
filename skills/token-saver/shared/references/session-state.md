# Session-State-Management (Hebel 6)

Quelle: Claude Code Token-Saving Guide (dholdaway), Best Practices for Productive Claude Usage (Educative), Claude Code Best Practices (Anthropic).
Ziel: 40-60% Token-Reduktion über mehrere Sessions, verhindert teuren Kontext-Rebuild.

## Das Problem

Ohne Session-Management passiert folgendes:
- User schliesst Session A mit 50k Kontext
- Öffnet Session B
- Erklärt alles neu → 10-20k Tokens für "Orientierungs-Wiederholung"
- Claude hat keinen Kontext → Mehr Fehler → Mehr Korrekturen → Mehr Tokens

## Die Lösung: Drei-Datei-System

### Datei 1: CLAUDE.md (Permanent-Kontext)

**Zweck:** Einmal schreiben, jede Session lädt es automatisch.

**Inhalt (max. 5k Tokens):**
```markdown
## Projekt
[Name, Typ, Status]

## Tech Stack
[Frameworks, Sprachen, Services]

## Conventions
[Naming, Formatierung, Import-Stil]

## Don'ts
[Was nie tun — wichtigste Guardrails]

## Bekannte Issues
[Aktive Bugs, offene Entscheidungen]
```

Wenn >5k Tokens: weniger kritische Sections in `docs/` auslagern.

### Datei 2: docs/progress.md (Running Log)

**Zweck:** Chronologisches Gedächtnisprotokoll aller Sessions.

```markdown
## Session 2026-06-07
- Problem: Auth-Refactor
- Gelöst: Login, Logout, Refresh
- Offen: Token-Refresh Edge-Case
- Nächste Session: Tests schreiben
```

### Datei 3: session_summary.md (Letzte Session)

**Zweck:** Schnell-Reload der letzten Session ohne progress.md komplett zu lesen.

```markdown
## Letzte Session: 2026-06-07
### Was gemacht
[3-5 Bullets]
### Wo aufgehört
[Ein Satz]
### Nächster Schritt
[Direkt actionable]
### Offene Fragen
[Max 3]
```

## Workflow: Session-Abschluss

```
1. In Claude Code: /compact Focus on [aktuelle Aufgabe]
   → Context von 80% auf ~20% geschrumpft
   
2. Prompt nach /compact:
   "Append this summary to docs/progress.md. 
    Save standalone to session_summary.md."
   
3. NICHT /clear verwenden — einfach neues Fenster öffnen.
   /clear löscht alles, ohne Sicherung.
```

## Workflow: Session-Start

```
@CLAUDE.md
@docs/progress.md
@session_summary.md  ← Nur wenn kürzlich (< 24h)
```

**Token-Kosten:** ~3-5k statt 50k+ Rebuild → -85% für Kontext-Laden.

## Workflow: Mid-Session-Compact

**Wann:** Alle ~40 Antworten oder wenn Context-Bar bei ~70%.

```
/compact Focus on [aktuelle Spezifik]

Dann: "Save this compact summary to session_summary.md"
```

Danach wieder bei ~20% Auslastung, keine Session-Neuerung nötig.

## Custom Slash Commands (.claude/commands/)

Wiederholte Workflows als Slash Commands speichern:
```
.claude/commands/analyze-bug.md:
  "1. Use gh issue view $ARGUMENTS 
   2. grep for related code
   3. Propose minimal fix"
```

Check these into git für Team-Sharing.

## Wann KEINE Session-Übergabe

- Exploration-Sessions (kein bleibendes Ergebnis)
- Einmalige Queries
- Sessions < 15 Antworten (Overhead lohnt nicht)

## Faustregeln

| Session-Länge | Empfehlung |
|---|---|
| < 15 Antworten | Kein Compact nötig |
| 15-40 Antworten | Session-Summary am Ende |
| > 40 Antworten | Mid-Session-Compact + Summary |
| > 80 Antworten | Zwei Compacts + neue Session empfehlen |
