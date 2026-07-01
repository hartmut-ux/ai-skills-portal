# Docs-Compression (Hebel 4)

Quelle: Claude Token Optimizer (nadimtuhin).
Ziel: Lange Docs/Specs von 11k → 1.3k Tokens (-88%).

## Anwendungsfälle

- README/CLAUDE.md vor Refactor
- API-Dokumentation vor Integration
- PDF-Spezifikationen (50+ Seiten)
- Eigene Skill-Files vor Edits
- Vertragsdokumente, Förderrichtlinien
- Lange RFCs / Whitepaper

## Drei-Schritt-Pipeline

### Schritt 1: Skim-Read (200 Tokens)

```
Read file_path: "/path/to/long-doc.md"
     limit: 80
```

Reicht für Überblick: Headings, erste Abschnitte, Struktur. Bei PDFs `pages: "1-5"`.

### Schritt 2: Strukturierung (Mental)

Beantworte für dich:
- Was sind die 5-10 Kernaussagen?
- Welche Sections sind für die aktuelle Aufgabe relevant?
- Welche Sections kann ich ignorieren?
- Gibt es Tabellen/Listen, die als-ist übernommen werden müssen?

### Schritt 3: Komprimierte Version schreiben

Erstelle eine `.compressed.md` im outputs-Ordner:

```markdown
# [Doc-Title] (compressed)

**Source:** /original/path
**Compression-Ratio:** 11k → 1.3k Tokens
**Date:** 2026-05-19

## TL;DR
[3-5 Sätze]

## Kern-Fakten
- Fakt 1
- Fakt 2
- ...

## Relevante Sections für aktuelle Aufgabe
### [Section-Name]
[3-5 Zeilen Essence]

## Tabellen (verbatim übernommen)
[Tabellen, die du nicht paraphrasieren darfst]

## Constraints / Pflichten
- Constraint 1
- Constraint 2

## Ignoriert (weil irrelevant)
- [Section X — Marketing-Boilerplate]
- [Section Y — Geschichte des Projekts]
```

Ab jetzt arbeitest du mit `.compressed.md`, nicht mit dem Original.

## Wann NICHT komprimieren

- Doc ist < 2k Tokens (lohnt sich nicht)
- Doc ist rechtlich verbindlich und muss verbatim referenziert werden
- User braucht 1:1-Übersetzung oder Zitate

## Komprimierungs-Patterns

### Pattern A: API-Docs
Behalte: Endpoints, Methods, Required/Optional Params, Response Schemas, Error Codes.
Streiche: Marketing-Blurb, Versions-Historie, FAQ, Beispiel-Curl-Calls.

### Pattern B: Förderrichtlinien
Behalte: Förderhöhe, Eligible Costs, Deadlines, Pflicht-Dokumente, Auszahlungs-Bedingungen.
Streiche: Politischer Kontext, Vision, Erfolgsgeschichten, FAQ.

### Pattern C: README / CLAUDE.md
Behalte: Install-Commands, Architektur-Entscheidungen, Conventions, Don'ts.
Streiche: Geschichte, Credits, lange Markdown-Badges, ASCII-Art.

### Pattern D: PDF-Verträge
Behalte: Parteien, Leistung, Vergütung, Laufzeit, Kündigung, Haftung, Gerichtsstand.
Streiche: Präambel, Glossar (referenzieren statt inline), Anhänge ohne Pflicht.

## Faustregeln

| Original-Grösse | Ziel-Grösse | Methode |
|---|---|---|
| 2-5k Tokens | 800-1.5k | Skim + Bullet-Summary |
| 5-15k Tokens | 1-2k | Section-Selection + Komprimierung |
| 15-50k Tokens | 2-3k | TL;DR + Index + On-Demand-Lookup |
| > 50k Tokens | Auslagern in RAG/Wiki (Karpathy-Pattern) |
