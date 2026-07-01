---
name: token-saver
description: Reduziert Token-Verbrauch in the assistant-Sessions massiv (50-95%) durch sieben Hebel - Output-Komprimierung, Symbol-First Code-Reading, Tool-Output-Filtering, Docs-Compression, Ghost-Token-Hygiene, Session-State-Management und MCP-Tool-Awareness. Use this skill whenever the user mentions 'Token sparen', 'Context-Limit', 'spart Tokens', 'terser mode', 'caveman mode', 'context window voll', 'API-Kosten reduzieren', 'the assistant wird langsam', 'zu viel Output', 'kürzer antworten', 'less context', 'reduce tokens', 'optimize context', 'token budget', 'cost optimization', '/compact', 'neue Session', 'session zu lang', oder wenn der User in einer langen Session arbeitet und merkt, dass der Kontext überläuft. Auch triggern wenn der User vor einer grossen Operation steht (Monorepo-Analyse, viele Dateien lesen, lange Logs auswerten) und proaktiv Tokens sparen will. NICHT triggern für reine Inhalts-Komprimierung von Texten (das ist humanizer-Job) oder für RAG-Optimierung (das ist rag-text-optimizer-Job).
license: MIT
metadata:
  author: Hartmut Hübner / MMIND.ai
  version: 2.0.0
  category: efficiency
  tags: [token-optimization, context-management, cost-reduction, claude-code, productivity, mcp, serena, repomix, ccusage]
---

# Token Saver v2

Massive Token-Reduktion (50-95%) für the assistant-Sessions durch sieben direkt anwendbare Hebel.

**Neu in v2:** Session-State-Management (Hebel 6) + MCP-Tool-Awareness (Hebel 7), inspiriert von den Patterns aus serena, repomix, ccusage, context7 und dem praktischen /compact-Workflow.

## Wann diesen Skill anwenden

- User sagt explizit: "spar Tokens", "kürzer", "terse", "caveman mode", "context voll"
- Session ist lang (>40 Antworten / >50 Tool-Calls) und Kontext füllt sich
- Bevorstehende Operation ist token-intensiv: Monorepo lesen, lange Logs auswerten, viele PDFs
- User klagt über API-Kosten oder langsame Antworten
- User sagt "/compact", "neue Session", "session ist zu lang"
- User fragt nach Token-Verbrauch oder Kosten

---

## Die sieben Hebel (Sofort-Anwendung)

### Hebel 1: Output-Komprimierung (Caveman/Terse Mode)

**Effekt:** -60 bis -75% Output-Tokens.

**Regeln in dieser Reihenfolge anwenden:**
1. Keine Höflichkeitsfloskeln ("Gerne!", "Natürlich!", "Ich werde jetzt...")
2. Keine Wiederholung der User-Frage
3. Keine Erklärung, was the assistant gleich tut, bevor er es tut (nur ein Satz Status, wenn Tool-Call folgt)
4. Bullet Points statt Prosa, sobald >3 Punkte
5. Code-Blöcke ohne erklärende Vor- und Nach-Kommentare
6. Kein Pre- und Postamble um Deliverables
7. Tabellen statt Listen, wenn Spalten-Vergleich sinnvoll

**Beispiel:**

❌ Lang (180 Tokens):
> "Gerne erkläre ich dir die drei wichtigsten Schritte zur Implementierung. Bevor wir loslegen, möchte ich kurz den Kontext skizzieren. Der erste Schritt besteht darin, dass du..."

✅ Terse (45 Tokens):
> "Drei Schritte:
> 1. Schema in Supabase anlegen
> 2. API-Route in Next.js
> 3. UI-Component verkabeln"

**Auto-Trigger:** Wenn der User in einer Session bereits >5 Antworten erhalten hat, automatisch in Terse Mode wechseln, ausser er fordert Prosa explizit.

Details: siehe `references/output-compression.md`

---

### Hebel 2: Symbol-First Code-Reading

**Effekt:** -90 bis -97% Tokens bei Code-Analyse (laut Code Review Graph & Token Savior).

**NIEMALS** als ersten Zug eine ganze Datei `Read`-en, wenn der User nach Code fragt. **IMMER** in dieser Reihenfolge:

1. **Glob** für Datei-Discovery: `pattern: "src/**/*.ts"` — kostet ~50 Tokens, gibt Pfade
2. **Grep** für Symbol/Keyword: `pattern: "function processPayment", output_mode: "files_with_matches"` — kostet ~100 Tokens, gibt Treffer
3. **Grep mit Context**: `pattern: "processPayment", output_mode: "content", -C: 5` — gibt nur relevante Zeilen
4. **Read mit Offset/Limit**: Erst dann gezielt `offset: 120, limit: 40` — statt 2000 Zeilen

**Faustregel:** Eine Datei >300 Zeilen NIE komplett lesen. Erst Grep, dann gezielt.

**Repo-Mapping:** Bei Monorepos zuerst `find . -type f -name "*.md" -path "*/docs/*"` o.ä. via Bash für eine 50-Zeilen-Karte, dann gezielt.

Details: siehe `references/symbol-first-reading.md`

---

### Hebel 3: Tool-Output-Filtering

**Effekt:** -60 bis -98% Tokens bei Logs, API-Responses, Build-Output.

**Regeln:**

1. **Vor jedem Bash-Call überlegen:** Brauche ich die volle Ausgabe oder reicht Filterung?
   - Build-Logs: `npm run build 2>&1 | tail -30`
   - Test-Output: `pytest 2>&1 | grep -E "(PASSED|FAILED|ERROR)" | head -50`
   - Lange Dateien: `wc -l file.log` zuerst, dann gezielt
2. **JSON-Responses:** `| jq '.data[] | {id, status}'` statt voller Dump
3. **Lange Outputs in Datei umlenken:** `command > /tmp/full.log` und dann `head/tail/grep` auf der Datei
4. **MCP/Tool-Calls mit head_limit:** Bei Grep/Glob immer `head_limit` setzen, default 250 ist meist zu viel
5. **Bei sehr grossen Outputs (>5k Tokens):** Output in SQLite/CSV/JSON-Datei dumpen, dann nur Summary in Context laden (Context-Mode-Pattern)

Details: siehe `references/tool-output-filtering.md`

---

### Hebel 4: Docs-Compression

**Effekt:** Docs von 11k → 1.3k Tokens (-88%, laut the assistant Token Optimizer).

**Wenn der User Docs/Specs/PDFs/Skill-Definitionen anhängt, die >2000 Tokens haben:**

1. **Erst Skim-Read:** `Read` mit `limit: 50` für Überblick
2. **Dann strukturieren:** Frage the assistant (sich selbst) — was sind die 5-10 Kernaussagen?
3. **Schreibe komprimierte Version** als `.compressed.md` in den outputs-Ordner
4. **Arbeite mit der komprimierten Version weiter**, nicht mit dem Original

**Anwendbar bei:**
- README/CLAUDE.md vor Refactor
- API-Docs vor Integration
- PDF-Spezifikationen
- Eigenen Skill-Files vor Edits

**CLAUDE.md-Template für Repos:** siehe `assets/CLAUDE.md.terse.template` — drop-in für Projekte, erzwingt Terseness ohne Code-Änderung.

Details: siehe `references/docs-compression.md`

---

### Hebel 5: Ghost-Token-Hygiene

**Effekt:** -10 bis -30% versteckte Tokens.

**Vor und während der Arbeit:**

1. **Keine Mega-Pastes:** Wenn User 50k Tokens Code pastet, frage zuerst: "Welche Funktion/Datei genau?"
2. **System-Reminders ignorieren-aber-nicht-wiederholen:** Nie System-Reminders zurück-quoten
3. **Tool-Listen nicht expandieren:** Wenn ToolSearch nötig ist, gezielt query bauen — nicht alle Tools laden
4. **Frühe Konsolidierung:** Bei Multi-File-Edits zuerst Plan in einem Tool-Call, dann Batch-Edits
5. **Keine Re-Reads:** Datei, die gerade editiert wurde, nicht nochmal Read-en (Harness trackt State)
6. **TodoList klein halten:** Max 7 Items, alte completed regelmässig wegräumen

Details: siehe `references/ghost-tokens.md`

---

### Hebel 6: Session-State-Management (NEU in v2)

**Effekt:** -40 bis -60% über mehrere Sessions hinweg. Verhindert, dass Kontext-Reload Tokens frisst.

**Das Problem:** Jede neue Session fängt bei 0 an — User müssen Kontext neu erklären, was 5-20k Tokens kostet.

**Die Lösung: Strukturierte Session-Übergabe**

#### 6a. Session-Abschluss (vor dem Schliessen)

```
1. /compact in your AI assistant (komprimiert Context auf ~20%)
2. Prompt: "Append this summary to docs/progress.md and save standalone to session_summary.md"
3. NICHT /clear — stattdessen einfach neue Session starten
```

#### 6b. Session-Start (in neuer Session)

```
@CLAUDE.md
@docs/progress.md
@session_summary.md  ← Optional, nur wenn kürzlich
```

Damit laden nur ~3-5k Tokens statt 50k+ Kontext-Rebuild.

#### 6c. Mid-Session-Compact (alle ~40 Antworten)

```
/compact Focus on [aktuelle Aufgabe]
→ Context schrumpft von 80% auf ~20%
→ Danach: "Save summary to session_summary.md"
```

#### 6d. Session-State-Datei-Struktur

Empfohlene Dateien im Projekt (lightweight, <5k Tokens gesamt):

| Datei | Inhalt | Wann laden |
|---|---|---|
| `CLAUDE.md` | Permanent: Stack, Conventions, Don'ts | Immer |
| `docs/progress.md` | Running Log aller Sessions | Session-Start |
| `session_summary.md` | Letzte Session-Zusammenfassung | Optional |
| `.claude/commands/` | Custom Slash Commands | Bei Bedarf |

Details: siehe `references/session-state.md`

---

### Hebel 7: MCP-Tool-Awareness (NEU in v2)

**Effekt:** Orientierung, welche externen Tools wann Tokens sparen — ohne diese Tools zu sein.

the assistant selbst kann keine MCP-Server installieren, aber User können es. Dieser Hebel erklärt wann und warum:

#### Wann welches Tool empfehlen

| User-Kontext | Empfohlenes Tool | Warum |
|---|---|---|
| Code-Analyse in grosser Codebase | serena (MCP) | Symbol-level retrieval, kein volles File-Read |
| Ganzes Repo als Kontext brauchen | repomix (CLI) | Repo → 1 Datei, Tree-sitter-Komprimierung -70% |
| Token-Verbrauch messen | ccusage (CLI) | Baseline vor Optimierung, täglicher Breakdown |
| API-Docs immer aktuell | context7 (MCP) | Kein veraltetes Halluzinieren, nur relevante Docs |
| Semantische Suche im Projekt | claude-context (MCP) | Nur relevante Chunks statt ganze Files |

#### Serena: Das wichtigste Tool (Symbol-First via MCP)

Serena erweitert Hebel 2 um echte IDE-Fähigkeiten:
- `get_symbols_overview` → Struktur ohne File-Read
- `find_symbol` → Direkt zur Funktion, nicht grep
- `get_symbol_body` → Exakt die Funktion, nichts drumherum
- Persistente Memory über Sessions (verhindert Re-Onboarding)

**Empfehlung an User:** "Wenn du regelmässig mit grossen Codebases arbeitest: serena installieren spart 80-95% Code-Reading-Tokens."

#### Repomix: Repo-Komprimierung vor Analyse

```bash
# Ganzes Repo packen (mit Tree-sitter-Komprimierung)
repomix --compress

# Remote-Repo (kein lokaler Clone nötig)
repomix --remote github.com/user/repo --compress

# Output: ein einziges .xml/.md mit ~30% der rohen Tokens
```

Wann empfehlen: User will gesamten Codebase-Überblick, nicht nur einzelne Files.

#### ccusage: Erst messen, dann optimieren

```bash
ccusage daily          # Tagesverbrauch
ccusage monthly        # Monatsaggregation  
ccusage blocks --live  # Live 5-Stunden-Fenster
```

**Goldene Regel:** Ohne Baseline-Messung (ccusage) weiss niemand, ob Optimierungen wirklich helfen.

Details: siehe `references/mcp-tool-awareness.md`

---

## Aktivierungs-Modi

Der User kann den Skill in drei Intensitätsstufen anwenden:

| Modus | Trigger | Verhalten |
|---|---|---|
| **Stealth** (Default bei langer Session) | Auto nach >5 Antworten | Hebel 1, 2, 3 silently aktiv |
| **Active** | "spar Tokens", "terse mode" | Alle 7 Hebel aktiv, kurzer Status |
| **Caveman** | "caveman mode", "extrem terse" | Maximale Komprimierung, Stichworte erlaubt |

**Caveman-Mode-Beispiel:**

❌ Normal: "Ich habe die Datei gelesen. Sie enthält drei Funktionen, von denen zwei async sind. Die erste Funktion `getUser` macht einen Datenbank-Call..."

✅ Caveman: "3 Funktionen. 2 async. getUser → DB. processPayment → Stripe. logEvent → noop."

---

## Pre-Flight Checklist

Vor jeder grossen Operation diese Checkliste durchgehen (siehe `assets/preflight-checklist.md`):

- [ ] Welche Hebel sind heute aktiv? (Default: 1, 2, 3)
- [ ] Operation token-intensiv? Wenn ja → erst Plan, dann Execute
- [ ] Outputs > 5k Token erwartet? → in Datei auslagern
- [ ] Docs/PDFs >2k Token? → komprimieren vor Use
- [ ] Code-Lesen geplant? → Symbol-First-Reihenfolge
- [ ] Session >40 Antworten? → /compact + session_summary.md
- [ ] User-Modus klar? (Stealth/Active/Caveman)

---

## Messung & Reporting

Wenn der User wissen will, wie viel gespart wurde:

1. Schätze Baseline: "Ohne Skill hätte ich vermutlich X Tokens verbraucht"
2. Schätze Actual: "Mit den Hebeln waren es ~Y Tokens"
3. Faktor angeben: "≈ 65% gespart"

Für echte Messung → ccusage (CLI-Tool, aussen) empfehlen.

Sei ehrlich — Schätzungen sind Schätzungen, keine exakte Messung.

---

## Beispiele

### Beispiel 1: User startet Monorepo-Refactor

**User:** "Refactor das Auth-System in meinem Next.js-Repo."

**Falsch (alte Methode):**
1. `Read` alle Auth-Dateien (10 × 800 Zeilen = 8k Lines = ~50k Tokens)
2. Lange Erklärung schreiben
3. Edits

**Richtig (mit Skill):**
1. `Glob "src/**/{auth,login,session}*"` → Pfade (200 Tokens)
2. `Grep "export.*function" --glob "src/auth/**"` → Symbole (500 Tokens)
3. `Read` nur betroffene Funktionen mit `offset/limit` (3k Tokens)
4. Plan in 5 Bullets (200 Tokens)
5. Batch-Edits

**Geschätzt:** ~5k statt ~50k Tokens → -90%

---

### Beispiel 2: User hat 50-Seiten-PDF-Spec

**User:** "Hier die Spec, baue mir das Backend."

**Mit Skill:**
1. `Read` PDF, `limit: 80` für Skim
2. Komprimiere auf 1-Pager: Endpoints + Datenmodell + Auth + Constraints
3. Speichere als `spec.compressed.md` in outputs
4. Arbeite ab jetzt mit komprimierter Version

**Geschätzt:** 35k → 4k Tokens für jeden weiteren Reference-Read → -88%

---

### Beispiel 3: Session zu lang (>40 Antworten)

**User:** "Die Session ist voll / the assistant antwortet langsam"

**Mit Skill:**
1. "Führe `/compact` aus mit Focus auf [aktuelle Aufgabe]"
2. "Speichere Summary in `session_summary.md`"
3. Neue Session: `@CLAUDE.md @session_summary.md` laden

**Geschätzt:** 50k Context → 10k nach Compact → -80%

---

### Beispiel 4: Kostencheck vor Optimierung

**User:** "Ich zahle zu viel für your AI assistant"

**Mit Skill:**
1. Empfehle ccusage: `ccusage daily --breakdown`
2. Zeige Baseline
3. Dann gezielte Massnahmen pro teuerstem Muster

---

## Was dieser Skill NICHT tut

- **Keine** Text-Humanisierung (das ist `humanizer`)
- **Keine** RAG-Pipeline-Optimierung (das ist `rag-text-optimizer`)
- **Kein** Setup von Proxy-Servern oder externen Tools (Skill ist conversation-native)
- **Keine** Garantie auf exakte Zahlen — Token-Schätzungen bleiben Schätzungen
- **Keine** Anwendung, wenn User explizit "ausführlich" oder "Prosa" verlangt

---

## Quellen (Inspiration)

Dieser Skill destilliert Patterns aus 12+ Open-Source-Tools:

1. Caveman the assistant (juliusbrussee/caveman) — Hebel 1
2. RTK Rust Token Killer (rtk-ai/rtk) — Hebel 3
3. Code Review Graph (tirth8205/code-review-graph) — Hebel 2
4. Context Mode (mksglu/context-mode) — Hebel 3
5. the assistant Token Optimizer (nadimtuhin/claude-token-optimizer) — Hebel 4
6. Token Optimizer (alexgreensh/token-optimizer) — Hebel 5
7. Token Optimizer MCP (ooples/token-optimizer-mcp) — Hebel 5
8. the assistant Context (zilliztech/claude-context) — Hebel 2 + 7
9. the assistant Token Efficient (drona23/claude-token-efficient) — Hebel 1 + Asset
10. Token Savior (mibayy/token-savior) — Hebel 2 + 7
11. serena (oraios/serena, 24.7k★) — Hebel 7 (Symbol-First via MCP)
12. repomix (yamadashy/repomix, 22.7k★) — Hebel 7 (Repo-Komprimierung)
13. ccusage (ryoppippi/ccusage, 10k★) — Hebel 7 (Token-Messung)
14. context7 — Hebel 7 (Aktuelle API-Docs ohne Halluzinierung)
15. your AI assistant Token-Saving Guide (dholdaway/gist) — Hebel 6

Diese Tools liefern teilweise mehr (Vector Search, Proxy-Filtering, IDE-Integration). Der Skill deckt nur das ab, was the assistant conversation-native erreichen kann, plus Orientierung zu den Tools, die User selbst installieren können.
