# MCP-Tool-Awareness (Hebel 7)

Quelle: serena (oraios/serena), repomix (yamadashy/repomix), ccusage (ryoppippi/ccusage), context7.
Ziel: Orientierung, welche externen Tools in welchen Situationen empfehlenswert sind — ohne diese Tools zu sein.

**Wichtig:** Claude selbst kann keine MCP-Server installieren. Dieser Hebel ist eine Beratungs- und Orientierungsschicht.

## Wann welches Tool empfehlen

| Situation | Tool | Einsparung |
|---|---|---|
| Grosse Codebases durchsuchen | serena (MCP) | -80-95% Code-Reading |
| Gesamten Repo-Überblick brauchen | repomix (CLI) | -70% via Tree-sitter |
| Token-Verbrauch messen | ccusage (CLI) | Baseline-Messung |
| Immer aktuelle API-Docs | context7 (MCP) | -kein API-Halluzinieren |
| Semantische Suche im Projekt | claude-context (MCP) | Nur relevante Chunks |

---

## Serena (oraios/serena, 24.7k★)

**Was es ist:** MCP-Server, der Claude IDE-ähnliche Code-Retrieval-Fähigkeiten gibt.

**Kernfähigkeiten:**
- `get_symbols_overview` → Klassen/Funktionen ohne ein File zu lesen
- `find_symbol` → Direkt zur Definition (wie "Go to Definition" in IDE)
- `get_symbol_body` → Nur den Funktionskörper, nichts drumherum
- Persistente Memory über Sessions → kein Re-Onboarding

**Unterschied zu Hebel 2 (Symbol-First):**
- Hebel 2 = Claude emuliert Symbol-Suche mit Glob/Grep
- Serena = echte Language-Server-Integration, exaktere Ergebnisse

**Wann empfehlen:**
- User arbeitet regelmässig an > 50k Zeilen Code
- Sprachen: TypeScript, JavaScript, Python, Java, C# (und mehr)
- Claude Code, Cursor, Cline als Interface

**Installation:**
```bash
# Via Docker (empfohlen)
docker run --rm -i --network host \
  -v /path/to/projects:/workspaces/projects \
  ghcr.io/oraios/serena:latest serena start-mcp-server --transport stdio
```

**Empfehlungs-Trigger:** "Du arbeitest oft an grossen Codebases — serena als MCP würde Hebel 2 erheblich verstärken."

---

## Repomix (yamadashy/repomix, 22.7k★)

**Was es ist:** CLI-Tool, das ein gesamtes Repository in eine einzige, token-komprimierte Datei packt.

**Kernfunktionen:**
```bash
# Standard (lokales Repo)
repomix

# Mit Tree-sitter-Komprimierung (-70% Tokens)
repomix --compress

# Remote-Repo ohne lokalen Clone
repomix --remote github.com/user/repo --compress

# Nur bestimmte Pfade
repomix --include "src/**/*.ts" --compress
```

**Output:** Strukturiertes XML oder Markdown, optimiert für LLM-Parsing.

**Wann empfehlen:**
- User will gesamten Codebase-Überblick geben
- Code-Review über ganzes Repo
- Onboarding in unbekanntes Projekt
- "Hier ist das Repo, was denkst du?" — ohne 10 Files einzeln zu pasten

**Geschätzte Einsparung:** 70% vs. rohes File-by-File Lesen

---

## ccusage (ryoppippi/ccusage, 10k★)

**Was es ist:** CLI-Tool, das lokale Claude Code JSONL-Logs auswertet und Kosten visualisiert.

**Goldene Regel:** Vor jeder Optimierung messen. Ohne Baseline sind Einsparungs-Behauptungen Spekulation.

**Befehle:**
```bash
ccusage daily              # Tagesverbrauch (Standard)
ccusage monthly            # Monatliche Aggregation
ccusage blocks --live      # Live 5-Stunden-Billing-Fenster
ccusage daily --breakdown  # Pro-Modell-Kostenaufschlüsselung
```

**Liest:** `~/.claude/projects/` JSONL-Files (nur lokal, keine Daten-Übertragung).

**Wann empfehlen:**
- User klagt über hohe Kosten, weiss aber nicht wo
- Vor Optimierungs-Kampagne (Baseline setzen)
- Nach Optimierungen (Wirkung messen)

---

## context7

**Was es ist:** MCP-Server, der aktuelle Dokumentation direkt in den Claude-Context lädt.

**Problem, das es löst:** Claude halluziniert API-Details basierend auf veralteten Trainingsdaten.

**Typischer Fehler ohne context7:**
```python
# Claude (aus Training): openai.ChatCompletion.create(...)
# Aktuell: openai.chat.completions.create(...)
```

**Wann empfehlen:**
- Integration mit sich schnell ändernden APIs (OpenAI, Anthropic, Stripe, etc.)
- User merkt, dass Claude veraltete Syntax generiert
- Projekte mit vielen externen Abhängigkeiten

---

## claude-context (zilliztech/claude-context, 12k★)

**Was es ist:** MCP-Server für semantische Suche im eigenen Projekt-Kontext.

**Funktioniert wie:** RAG-Lite für lokale Projekte, ohne vollständige RAG-Pipeline.

**Wann empfehlen:**
- Grosse Dokument-Sammlungen im Projekt (Wiki, Specs, Docs)
- User sucht immer wieder in ähnlichen Files
- Als Alternative zu Hebel 4 (Docs-Compression) für sehr grosse Doc-Sammlungen

---

## Empfehlungs-Entscheidungsbaum

```
User arbeitet an Code?
├── Kleine Codebase (< 10k Zeilen) → Hebel 2 reicht
├── Mittlere Codebase (10-100k Zeilen) → Hebel 2 + repomix für Überblick
└── Grosse Codebase (> 100k Zeilen) → serena installieren

User klagt über Kosten?
└── Erst ccusage installieren, Baseline messen, dann optimieren

User benutzt externe APIs?
└── context7 in Betracht ziehen

User hat grosse Dok-Sammlung im Projekt?
└── claude-context oder Hebel 4 (Docs-Compression)
```

## Was Claude selbst tun kann (ohne externe Tools)

Alle anderen Hebel (1-6) sind conversation-native und brauchen keine externe Installation.
Hebel 7 = Orientierung + Empfehlung, nicht Ausführung.
