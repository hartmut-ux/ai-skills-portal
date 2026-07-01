# Setup Guide Template

This template produces a step-by-step guide for non-developers. Fill in all `[PLACEHOLDER]` values. The guide should be so specific that someone with no terminal experience can follow it.

---

```markdown
# [App Name] — Setup-Anleitung

Diese Anleitung bringt dich von Null zum laufenden Projekt. Danach arbeitest du nur noch mit Claude Code — du beschreibst was du willst, Claude baut es.

---

## Architektur-Übersicht

[App Name] besteht aus [Anzahl] Teilen:

| Teil | Repo | Hosting | Domain | Zweck |
|------|------|---------|--------|-------|
| **Landingpage** | `[repo-landing]` | [Lovable / WordPress] | [domain.tld] | Marketing, SEO |
| **App** | `[repo-service]` | Railway | app.[domain.tld] | Login, Dashboard, Kernfunktionen |

[Beide nutzen dasselbe Supabase-Projekt für die Datenbank.]

**Supabase-Projekt:** https://[project-ref].supabase.co (Region: [region])

---

## Voraussetzungen (einmalig installieren)

### 1. Node.js
- Herunterladen: https://nodejs.org/ (LTS Version)
- Installieren, Standard-Einstellungen
- Prüfen: Terminal öffnen, `node --version` eingeben → sollte v20+ zeigen

### 2. Git
- Herunterladen: https://git-scm.com/
- Installieren, Standard-Einstellungen
- Prüfen: `git --version`

### 3. Supabase CLI
\```bash
npm install -g supabase
\```
Prüfen: `supabase --version`

### 4. Claude Code
- Desktop App oder VS Code Extension — muss bereits installiert sein

---

## Schritt 1: GitHub Repo klonen

\```bash
cd ~/Documents
git clone https://github.com/[github-user]/[repo-name].git
cd [repo-name]
\```

---

## Schritt 2: Starter-Kit kopieren

Kopiere den Inhalt des `starter-kit/` Ordners in dein geklontes Repo:

- `CLAUDE.md` → Wurzel des Repos
- `DESIGN.md` → Wurzel des Repos
- `.claude/skills/` → Wurzel des Repos
- `supabase/migrations/` → Wurzel des Repos
- `package.json` → Wurzel des Repos
- `.gitignore` → Wurzel des Repos
- `.env.example` → Wurzel des Repos

[Tipp für Nicht-Entwickler: Wenn versteckte Dateien (.claude, .gitignore, .env.example) im Finder nicht sichtbar sind, Cmd+Shift+. drücken. Oder alle Dateien über Terminal kopieren.]

---

## Schritt 3: Supabase verbinden

1. Öffne dein Supabase Dashboard: https://supabase.com/dashboard
2. Wähle das Projekt "[Projektname]"
3. Gehe zu **Settings → API**
4. Kopiere:
   - **Project URL** → `https://[project-ref].supabase.co`
   - **anon public Key** → das ist `VITE_SUPABASE_ANON_KEY`
   - **service_role Key** → das ist `SUPABASE_SERVICE_ROLE_KEY` (GEHEIM!)

5. Erstelle `.env.local`:
\```bash
cp .env.example .env.local
\```

6. Öffne `.env.local` und fülle die Werte ein:
\```
VITE_SUPABASE_URL=https://[project-ref].supabase.co
VITE_SUPABASE_ANON_KEY=eyJ...dein-anon-key...
ANTHROPIC_API_KEY=sk-ant-...dein-key...
SUPABASE_SERVICE_ROLE_KEY=eyJ...dein-service-key...
\```

7. Supabase CLI verbinden:
\```bash
supabase login
supabase link --project-ref [project-ref]
\```

---

## Schritt 4: Datenbank-Schema erstellen

\```bash
supabase db push
\```

Prüfen: Supabase Dashboard → Table Editor → Tabellen sollten sichtbar sein.

---

## Schritt 5: Railway verbinden

1. Öffne https://railway.app/dashboard
2. Neues Projekt → "Deploy from GitHub repo"
3. Wähle `[repo-name]`

4. Umgebungsvariablen setzen:
   - Railway Dashboard → dein Service → Variables
   - `VITE_SUPABASE_URL` = `https://[project-ref].supabase.co`
   - `VITE_SUPABASE_ANON_KEY` = (gleicher Wert wie .env.local)

5. Custom Domain:
   - Railway Dashboard → Settings → Custom Domain
   - `app.[domain.tld]` hinzufügen
   - CNAME Record beim Domain-Registrar eintragen

---

## Schritt 6: Landingpage-Links anpassen

[Alle Login/Registrierungs-Buttons auf der Landingpage verlinken auf die App:]

- "Registrieren" → `https://app.[domain.tld]/register`
- "Anmelden" → `https://app.[domain.tld]/login`
- [Weitere rollenspezifische Links]

---

## Schritt 7: Erster Commit und Deploy

\```bash
npm install
npm run build
git add .
git commit -m "chore: initial project setup"
git push origin main
\```

Railway deployed automatisch. Nach 2-3 Minuten ist die App erreichbar.

---

## Täglicher Workflow

### So arbeitest du mit Claude Code:

1. **Öffne Claude Code** im `[repo-name]` Ordner
2. **Sage was du willst** (in normalem Deutsch/English)
3. **Claude Code baut es.** Es liest CLAUDE.md + DESIGN.md automatisch.
4. **Testen:** `npm run dev` → http://localhost:5173 im Browser
5. **Deployen:** `git add . && git commit -m "feat: ..." && git push origin main`
6. **Fertig.** Railway deployed automatisch.

### Für Edge Functions:
\```bash
supabase functions serve    # Lokal testen
supabase functions deploy   # Live deployen
\```

### Für Datenbank-Änderungen:
\```bash
supabase db push            # Migration auf Produktion
\```

---

## Hilfe bei Problemen

| Problem | Lösung |
|---------|--------|
| `npm run build` zeigt Fehler | Fehlermeldung an Claude Code geben |
| Seite lädt nicht | Railway Dashboard → Deployment Logs prüfen |
| Edge Function Fehler | `supabase functions serve` lokal testen |
| `supabase db push` schlägt fehl | Im SQL Editor manuell ausführen |
| SSL-Warnung bei Custom Domain | Warten (10-60 Min für Zertifikat) |

---

## Was du NICHT tun musst

- Code lesen oder verstehen
- Dateien manuell bearbeiten
- Terminal-Befehle auswendig lernen
- Deployment konfigurieren (einmalig eingerichtet)
- Datenbank manuell verwalten

## Was du tun musst

- Claude Code sagen was du willst
- Im Browser testen
- `git push origin main` wenn es passt
- Bei Fehlern die Fehlermeldung weitergeben
```
