# CLAUDE.md Template

Use this template as a starting point. Fill in all `[PLACEHOLDER]` values with project-specific information. Remove sections that don't apply (e.g., Railway Server if no server-side logic is needed).

---

```markdown
# [App Name] — Projekt-Konventionen für Claude Code

## Was ist [App Name]?

[One paragraph: what the app does, for whom, in which context. Include the business model if relevant.]

## Tech-Stack

\```
Frontend:     React 18 + Vite + TypeScript
UI:           shadcn/ui + Tailwind CSS
Backend:      Supabase (Auth, PostgreSQL, Storage, Edge Functions)
Edge Funcs:   Deno (für Claude API Calls, leichte Logik)
Server:       Railway (Node.js — Web Scraping, Cron-Jobs, Payment Webhooks)
Payment:      Stripe (Empfangen + Auszahlen via Connect)
AI:           Claude API (Anthropic) — nur serverseitig, NIE im Frontend
E-Mail:       Resend
Domain:       [domain.tld]
Repo:         GitHub → Railway auto-deploy bei Push auf main
\```

## Ordnerstruktur

\```
[app-name]/
├── CLAUDE.md                    ← diese Datei
├── DESIGN.md                   ← Design-System
├── .claude/
│   └── skills/                  ← Skills für Claude Code
├── src/
│   ├── components/              ← Wiederverwendbare UI-Komponenten
│   │   └── ui/                  ← shadcn/ui Komponenten
│   ├── pages/                   ← Seitenkomponenten (eine pro Route)
│   ├── hooks/                   ← Custom React Hooks
│   ├── lib/                     ← Utilities, Supabase Client, Typen
│   │   ├── supabase.ts          ← Supabase Client-Instanz
│   │   └── types.ts             ← TypeScript-Typen (aus DB generiert)
│   ├── layouts/                 ← Layout-Komponenten (Sidebar, Header)
│   └── App.tsx                  ← Router + Haupt-App
├── supabase/
│   ├── migrations/              ← SQL-Migrationen (nummeriert)
│   └── functions/               ← Edge Functions (Deno)
│       └── [function-name]/     ← Eine Funktion pro Ordner
├── server/                      ← Railway Node.js Server (optional)
│   ├── src/
│   │   ├── scraper/             ← Web Scraping
│   │   ├── cron/                ← Geplante Jobs
│   │   ├── webhooks/            ← Stripe/Payment Webhooks
│   │   └── index.ts             ← Express Server Entry Point
│   ├── package.json
│   └── tsconfig.json
├── public/
│   ├── sitemap.xml
│   ├── robots.txt
│   └── og-image.png
├── package.json
├── vite.config.ts
├── tailwind.config.js
├── tsconfig.json
└── .env.local                   ← Lokale Umgebungsvariablen (NICHT committen)
\```

## Konventionen

### Sprache
- **UI-Texte:** [Deutsch / English], [Schweizer Rechtschreibung (kein ß, CHF) / andere Variante]
- **Code:** Englisch (Variablen, Funktionen, Kommentare)
- **DB-Spalten:** [Deutsch / English] — wie im Schema definiert
- **Commit-Messages:** Englisch

### Code-Stil
- TypeScript strict mode
- Funktionale React-Komponenten mit Hooks
- Keine `any` Types — immer explizit typisieren
- shadcn/ui für alle UI-Elemente (keine custom CSS wo vermeidbar)
- Tailwind für Layout und Spacing
- Supabase Client nur über `src/lib/supabase.ts` importieren

### Sicherheit — KRITISCH
- **Claude API Key:** NUR in Supabase Edge Functions oder Railway Server. NIEMALS im Frontend.
- **Supabase Service Key:** NUR serverseitig. Im Frontend nur den anon Key verwenden.
- **Stripe Secret Key:** NUR auf Railway Server.
- **RLS (Row Level Security):** MUSS auf allen Tabellen aktiv sein. Keine Tabelle ohne RLS.
- **.env.local:** NIEMALS committen. Steht in .gitignore.

### Datenbank
- Alle Migrationen unter `supabase/migrations/` als nummerierte SQL-Dateien
- Format: `001_initial_schema.sql`, `002_add_feature_x.sql`, ...
- Jede Migration muss idempotent sein (IF NOT EXISTS)
- UUID als Primary Key überall
- created_at + updated_at (timestamptz) auf jeder Tabelle
- CHECK constraints statt PostgreSQL enums

### Edge Functions (Supabase)
- Deno Runtime
- Jede Funktion in eigenem Ordner unter `supabase/functions/`
- `index.ts` als Entry Point
- CORS-Header setzen für Frontend-Zugriff
- Fehler immer als JSON zurückgeben
- [AI-Nutzung in ai_usage_log loggen (falls EU AI Act relevant)]

### Railway Server (optional)
- Express.js + TypeScript
- Für alles was Edge Functions nicht können: Puppeteer/Cheerio, Cron, Stripe Webhooks
- Health-Check Endpoint: GET /health
- Alle Routen unter /api/

### Git-Workflow
- `main` Branch = Produktion (Railway deployed automatisch)
- Feature-Branches: `feature/[feature-name]`
- Commit-Messages: Konventionell (`feat:`, `fix:`, `chore:`, `docs:`)
- Kein Force-Push auf main

[## Compliance / Regulierung
Add compliance requirements here if applicable:
- EU AI Act: Logging, Human-in-the-Loop, Transparency, Limits
- GDPR / nDSG: Data handling, consent, deletion
- Financial: Tax calculations, audit trail
]

## Umgebungsvariablen

\```env
# .env.local (Frontend)
VITE_SUPABASE_URL=https://[project-ref].supabase.co
VITE_SUPABASE_ANON_KEY=eyJ...

# Supabase Edge Functions (Secrets)
ANTHROPIC_API_KEY=sk-ant-...
SUPABASE_SERVICE_ROLE_KEY=eyJ...

# Railway Server (optional)
DATABASE_URL=postgresql://...
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
RESEND_API_KEY=re_...
\```

[## Business-Logik
Add pricing rules, state machines, validation rules here.
Example:
- Vermittlungsgebühr: 15% des bestätigten Jahreslohns
- Probezeit: 3 Monate, danach Bonus-Auszahlung
]

## Datenbank-Tabellen (Übersicht)

[List all table names, comma-separated]

→ Vollständiges Schema in `supabase/migrations/001_initial_schema.sql`
→ Details in `[APP_NAME]_Requirements_v1.0.md`
```
