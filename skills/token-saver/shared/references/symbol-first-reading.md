# Symbol-First Code-Reading (Hebel 2)

Quelle: Code Review Graph, Token Savior, Claude Context.
Ziel: 49-97% Reduktion bei Code-Navigation.

## Kern-Regel

**Niemals als ersten Zug eine ganze Datei Read-en, wenn der User nach Code fragt.**

Die meisten Coding-Fragen brauchen 5-50 Zeilen Kontext, nicht 800.

## Vier-Stufen-Treppe

### Stufe 1: Discovery via Glob (50-200 Tokens)

```
Glob pattern: "src/**/*.ts"
```

Gibt eine Liste von Pfaden, sortiert nach modification time. Aus 100 Files siehst du, welche relevant aussehen.

### Stufe 2: Symbol-Suche via Grep (100-500 Tokens)

```
Grep pattern: "function processPayment"
      output_mode: "files_with_matches"
```

Zeigt nur Pfade mit Treffern. Du weisst jetzt: "Symbol lebt in `src/payment/stripe.ts` und `tests/payment.test.ts`".

### Stufe 3: Content mit Context (500-2000 Tokens)

```
Grep pattern: "processPayment"
      output_mode: "content"
      -C: 5
      head_limit: 50
```

Zeigt jede Match-Stelle mit 5 Zeilen Vor- und Nachkontext. Reicht für 80% aller Coding-Fragen.

### Stufe 4: Gezieltes Read (1000-3000 Tokens)

Erst wenn Stufe 3 nicht reicht:

```
Read file_path: "/path/to/file.ts"
     offset: 120
     limit: 60
```

Niemals `Read` ohne Offset/Limit auf Dateien > 300 Zeilen.

## Faustregeln

| Dateigrösse | Strategie |
|---|---|
| < 100 Zeilen | Read full ok |
| 100-300 Zeilen | Read full grenzwertig |
| 300-1000 Zeilen | Grep + targeted Read |
| > 1000 Zeilen | Strikt Grep-only |
| > 5000 Zeilen | Ablehnen oder splitten |

## Repo-Mapping bei grossen Codebases

Bevor du in ein unbekanntes Repo eintauchst, mache eine 50-Zeilen-Karte:

```bash
# Top-Level-Struktur
ls -la /repo/

# Source-Tree (2 Ebenen)
find /repo/src -maxdepth 2 -type d

# Wichtigste Files
find /repo -maxdepth 3 -name "package.json" -o -name "tsconfig.json" -o -name "README.md"

# Lines-per-File-Ranking
find /repo/src -name "*.ts" -exec wc -l {} + | sort -rn | head -20
```

Daraus baust du eine mentale Karte, ohne ein einziges File komplett zu lesen.

## Persistente Memory (Token-Savior-Pattern)

Wenn du in derselben Session mehrmals dieselben Files anfasst:

1. Bei der ersten Begegnung: Symbol-Map als kurze Notiz im Output halten
2. Nicht das ganze File re-readen — auf die Notiz referenzieren
3. Bei Edits: `Edit` mit präzisem `old_string`, nicht erst `Read` aller 800 Zeilen

## Beispiel: Bug-Fix in unbekanntem Monorepo

**User:** "Fix the off-by-one bug in our pagination logic."

**Falsch:**
1. Read jedes File im `src/`-Ordner → 100k Tokens

**Richtig:**
1. `Grep "pagination" --output_mode files_with_matches` → 3 Files
2. `Grep "page\\s*-\\s*1|offset\\s*=" --output_mode content -C 3` → exakte Stellen
3. `Edit` direkt mit präzisem `old_string`

Geschätzte Reduktion: ~95%.

## Wann ganze Files lesen ok ist

- Konfig-Files (< 100 Zeilen)
- README/CLAUDE.md (Orientierung)
- Wenn User explizit "read the whole file" sagt
- Bei Code-Reviews, wo Vollständigkeit Pflicht ist
