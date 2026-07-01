# Tool-Output-Filtering (Hebel 3)

Quelle: RTK (Rust Token Killer), Context Mode.
Ziel: 60-98% Reduktion bei Logs, Build-Output, API-Responses.

## Kern-Frage vor jedem Bash-Call

> Brauche ich die volle Ausgabe oder reicht ein gefilterter Auszug?

Default-Antwort: **Filterung reicht meistens.**

## Standard-Filter pro Output-Typ

### Build-Logs
```bash
npm run build 2>&1 | tail -50
yarn build 2>&1 | grep -E "(error|warning|✓|✗)" | head -30
cargo build 2>&1 | grep -E "(error|warning)" | head -30
```

### Test-Output
```bash
pytest 2>&1 | grep -E "(PASSED|FAILED|ERROR|SKIPPED)" | tail -50
jest 2>&1 | grep -E "(✓|✗|FAIL|PASS)" | head -50
go test ./... 2>&1 | grep -E "(FAIL|ok|---)" | tail -30
```

### Lange Log-Files
```bash
# Erst Grösse checken
wc -l /var/log/app.log

# Dann gezielt
tail -100 /var/log/app.log
grep -E "ERROR|FATAL" /var/log/app.log | tail -50
sed -n '1000,1100p' /var/log/app.log
```

### JSON-API-Responses
```bash
# Nicht: curl https://api/users → 200kb
# Sondern:
curl -s https://api/users | jq '.data[] | {id, name, status}' | head -30
curl -s https://api/users | jq '.data | length'
curl -s https://api/users | jq '.data[0]'   # Schema-Inspektion
```

### Git-Diffs
```bash
git diff --stat              # Übersicht
git diff --name-only         # Nur Pfade
git diff HEAD~1 -- src/      # Nur Subdir
git log --oneline -20        # Compact log
```

### Process / System
```bash
ps aux | grep node | head -10
df -h | head -5
du -sh /path/* | sort -h | tail -10
```

## Lange Outputs in Datei umlenken (Context-Mode-Pattern)

Wenn ein Tool gigabytes-Output produziert:

```bash
# Dump in Datei
heavy_command > /tmp/output.full 2>&1

# Arbeite auf der Datei
wc -l /tmp/output.full              # Wie viel?
head -50 /tmp/output.full           # Anfang
tail -50 /tmp/output.full           # Ende
grep -c "ERROR" /tmp/output.full    # Zählung
grep "ERROR" /tmp/output.full | head -20  # Sample
```

Claude sieht nie den vollen Output — nur Auszüge. 100MB Log → 5kb Context.

## Grep/Glob mit head_limit

Default-`head_limit` ist 250 — meist zu viel. Setze immer:

```
Grep pattern: "TODO"
      head_limit: 30
      output_mode: "content"
```

Bei `files_with_matches` reichen oft 20.

## MCP-Tool-Calls

- Vor MCP-Call überlegen: Welcher Subset reicht?
- `list_*`-Calls fast immer mit `limit`/`pageSize`
- Bei vagen Results: ersten Call mit kleinem `limit`, dann gezielter
- Niemals "give me everything" als Default

## SQLite/CSV-Auslagerung (für sehr grosse Datasets)

Wenn der User mit grossen Datasets arbeitet:

1. Daten in SQLite/CSV laden (via Python in Bash)
2. Nur Summary-Queries in Context
3. Beispiel:
```bash
python3 -c "
import sqlite3, csv
con = sqlite3.connect(':memory:')
# ... load ...
print(con.execute('SELECT count(*), status FROM data GROUP BY status').fetchall())
"
```

So bleibt der Raw-Data im Linux-Sandbox, nur Aggregate kommen in den Context.

## Faustregeln

| Output-Grösse erwartet | Strategie |
|---|---|
| < 1k Tokens | Direkt ok |
| 1-5k Tokens | head/tail/grep |
| 5-50k Tokens | Auslagern + Summary |
| > 50k Tokens | Refuse oder Splitting |
