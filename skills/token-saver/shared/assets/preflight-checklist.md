# Pre-Flight Checklist v2 (vor token-intensiver Operation)

Anwenden vor: Monorepo-Analyse, viele Files lesen, lange Logs auswerten,
PDF-Specs verarbeiten, Multi-Step-Refactor, Datenmigration, neue lange Session.

## Vor dem Start

- [ ] **Modus klar?** Stealth / Active / Caveman?
- [ ] **Welche Hebel aktiv?** Default 1, 2, 3. Bei grosser Operation auch 4 + 5 + 6.
- [ ] **Output-Volumen geschätzt?** Wenn >5k Tokens erwartet → Auslagerung planen.
- [ ] **Docs/PDFs in Scope >2k Tokens?** → Kompression vor Use.
- [ ] **Code-Reading geplant?** → Symbol-First-Reihenfolge zwingend.
- [ ] **Pastes vom User analysiert?** → Bei Mega-Paste erst Zielfrage stellen.
- [ ] **Session bereits lang (>40 Antworten)?** → /compact empfehlen.
- [ ] **session_summary.md vorhanden?** → Laden für Kontext-Kontinuität.

## Während der Operation

- [ ] Jeder Bash-Call gefiltert (head/tail/grep/jq)?
- [ ] Grep/Glob mit `head_limit`?
- [ ] Read mit `offset`/`limit` bei Files >300 Zeilen?
- [ ] Keine Re-Reads derselben Datei?
- [ ] Batch-Edits statt einzeln?
- [ ] TodoList unter 7 Items?
- [ ] Nach 40 Antworten: /compact vorschlagen?

## Vor jeder Antwort

- [ ] Erste Floskel gestrichen?
- [ ] User-Frage nicht wiederholt?
- [ ] Bullets ab 3 Punkten?
- [ ] Kein "Ich werde jetzt..."?
- [ ] Kein Postamble nach Deliverable?

## Nach der Operation

- [ ] Session-State sauber? → Summary in session_summary.md speichern.
- [ ] Wenn Session >40 Antworten → /compact + Datei-Sicherung vorschlagen.
- [ ] Schätzung für User: "≈ X% Tokens gespart vs. naive Methode."
- [ ] Hat etwas nicht funktioniert? → Note für Skill-Refinement.
- [ ] Externes Tool sinnvoll? → Empfehlung aus Hebel 7.

## Rote Flags (Stopp und nachdenken)

- 🚩 Du willst gerade ein 5000-Zeilen-File komplett lesen.
- 🚩 Du willst gerade dieselbe Datei zum 3. Mal Read-en.
- 🚩 Du quotest System-Reminder zurück.
- 🚩 Du wiederholst die User-Frage in der Antwort.
- 🚩 Du schreibst Postamble nach einem File-Link.
- 🚩 Bash-Command ohne head/tail/grep auf etwas Unbekanntes.
- 🚩 Session >40 Antworten ohne /compact.
- 🚩 User erklärt dasselbe zum zweiten Mal — session_summary.md fehlt.

Jede rote Flag → Stopp, anders machen.
