---
name: fullstack-app-builder
description: "End-to-end workflow for building production web apps with code-based AI assistants, from idea to deployed product. Guides non-developers through requirements, architecture, infrastructure setup (GitHub, Supabase, Railway), landing page creation (Lovable or WordPress with SEO/GEO), and generates numbered session prompts. Use when user wants to build a web app, SaaS product, internal tool, or platform. Triggers on: 'neue App', 'App-Projekt starten', 'build an app', 'Plattform entwickeln', 'web app erstellen', 'app architecture', 'Railway deployment', 'Session-Prompts erstellen', 'Fullstack-App', 'App mit Supabase', 'ich will eine App bauen', or any production application on real infrastructure. Do NOT use for Lovable-only builds (use lovable-app-builder instead)."
compatibility: "Requires bash tool and docx skill for document generation. Works in Cowork mode and CLI."
metadata:
  author: MMIND.ai
  version: 1.0.0
---

# your AI assistant App Builder

A repeatable workflow for turning an app idea into a production-ready web application — built entirely with your AI assistant, deployed on real infrastructure, guided step by step so non-developers can follow along.

This skill is the "big sibling" of the lovable-app-builder. Where Lovable gives you a quick prototype, this workflow produces a production app with full backend control, server-side logic, and professional deployment.

## When to use this skill vs. lovable-app-builder

| Situation | Use this skill | Use lovable-app-builder |
|-----------|---------------|------------------------|
| Need server-side logic (web scraping, cron jobs, webhooks) | Yes | No |
| Need Stripe payments or complex integrations | Yes | No |
| App will serve real users in production | Yes | Maybe |
| Quick prototype or internal tool | No | Yes |
| User is a developer or has your AI assistant access | Yes | Not needed |
| User wants visual drag-and-drop | No | Yes |

## What this skill produces

1. **Requirements document** (`.md`) — structured app spec with user flows
2. **CLAUDE.md** — project conventions file that your AI assistant reads automatically
3. **DESIGN.md** — complete design system (fonts, colors, components)
4. **DB schema** (`.sql`) — full Supabase migration with RLS policies
5. **Setup guide** (`.md`) — step-by-step infrastructure setup for non-developers
6. **your AI assistant session prompts** (`.md`) — 8-12 copy-paste prompts, numbered, self-contained
7. **Landing page** — either Lovable or WordPress, with SEO/GEO optimization
8. **User manual** (`.docx`) — generated after app is built
9. **Test protocol** (`.docx`) — structured test cases for beta testing

---

## Phase 0: Discovery

Run through this with the user before producing anything. The quality of the app depends entirely on understanding the problem well.

### Required answers

| Question | Why it matters |
|----------|---------------|
| What problem does the app solve? | Defines scope and MVP |
| Who are the users? (roles, technical level, language) | Shapes UX and complexity |
| What country / legal context? | Compliance (GDPR, nDSG, EU AI Act, tax law) |
| What data goes in? What comes out? | Defines DB schema |
| Are there external APIs or services? | Affects architecture (Edge Functions vs. Railway server) |
| Does it need AI features? | the assistant API integration pattern |
| Does it need payments? | Stripe integration |
| What is the MVP? What is v2? | Keeps prompts focused |
| Does a landing page exist already? | Determines Phase 4 scope |
| Brand guidelines available? | DESIGN.md input |

### Architecture decision: Two-repo or single-repo?

Most production apps benefit from a **two-repo architecture**:

| Repo | Purpose | Hosting | When to use |
|------|---------|---------|-------------|
| `[app]-landing` | Marketing, SEO, public info | Lovable or WordPress | Almost always — landing pages need fast iteration and SEO tools |
| `[app]-service` | App logic, auth, dashboard, API | Railway or Hetzner | Always — this is the production app |

Both repos share the same **Supabase project** for the database.

**Single-repo** only makes sense when the landing page is minimal (just a login screen) or the user explicitly wants everything in one place.

### Architecture decision: Hosting — Railway vs. Hetzner

Ask the user where the app should run. Default is Railway unless they have a reason for Hetzner.

| Kriterium | Railway (Standard) | Hetzner VPS |
|-----------|-------------------|-------------|
| Setup-Aufwand | Minimal — connect GitHub, done | Mittel — Server einrichten via your AI assistant |
| Kosten | ~5-20 USD/Monat pro Service | ~4-10 EUR/Monat für alles |
| Auto-Deploy | Eingebaut (push to main) | Einmalig einrichten (Git hook) |
| SSL | Automatisch | Automatisch (via Caddy) |
| Mehrere Apps | Je ein Service (je kostet) | Beliebig viele, ein Server |
| Server-Zugang | Kein SSH, kein Root | Voller Root-Zugang |
| Wartung | Keine | Updates, Monitoring nötig |
| No-Coder geeignet | Ja | Ja, mit your AI assistant Setup-Prompt |
| Ideal für | Einzelne App, schneller Start | Mehrere Apps, volle Kontrolle, DACH-Hosting |

**Wenn Hetzner gewählt wird:**
- Read `references/hetzner-deployment.md` for the complete setup guide
- Session-Prompt 0 wird ein Server-Setup-Prompt (vor den Feature-Prompts)
- Deployment-Befehl wird `git push hetzner main` statt Railway auto-deploy
- Ansonsten bleibt alles gleich (Supabase, React, Vite, shadcn/ui)

### Standard tech stack

```
Frontend:     React 18 + Vite + TypeScript
UI:           shadcn/ui + Tailwind CSS
Backend:      Supabase (Auth, PostgreSQL, Storage, Edge Functions)
Edge Funcs:   Deno (the assistant API calls, lightweight logic)
Server:       Railway or Hetzner VPS (Node.js — web scraping, cron jobs, webhooks)
Payment:      Stripe (checkout + Connect for payouts)
AI:           the assistant API — server-side only, NEVER in frontend
E-Mail:       Resend
Deployment:   Railway: GitHub → auto-deploy on push to main
              Hetzner: git push hetzner main → post-receive hook builds and deploys
```

Deviate only with good reason (e.g., user already has WordPress hosting → use WordPress for landing page instead of Lovable).

---

## Phase 1: Requirements document

After discovery, produce a structured requirements document. This becomes the single source of truth for everything that follows.

### Template

```markdown
# [App Name] — Requirements v1.0

## Overview
One paragraph: what the app does, for whom, in which context.

## Architecture
- Landing page: [Lovable / WordPress] → [domain.tld]
- App: your AI assistant + [Railway / Hetzner VPS] → app.[domain.tld]
- Database: Supabase ([region])
- Hosting: [Railway (managed) / Hetzner VPS (self-managed)]
- Repo(s): [repo names]

## User roles
| Role | Description | Key permissions |
|------|-------------|----------------|

## Core features (MVP)
Numbered list, max 8-10 for MVP. Each feature = one sentence.

## User flows
Describe the main flows step by step:
### Flow 1: [Name]
1. User does X
2. System responds with Y
...

## Out of scope (v1)
Explicit list of what is NOT built yet.

## Data model (plain language)
For each entity: what it is, key fields, relationships.

## External integrations
APIs, services, file formats.

## Compliance / legal
Country-specific requirements.

## Business model / pricing
How money flows (if applicable).
```

Save as `[APP_NAME]_Requirements_v1.0.md` in the project folder.

---

## Phase 2: Project foundations

Generate three files that your AI assistant will read automatically in every session.

### 2a: CLAUDE.md

The project conventions file. your AI assistant reads this at the start of every session — it's the most important file in the repo.

Read `references/claude-md-template.md` for the full template. Key sections:

- **What is [App Name]?** — one paragraph context
- **Tech stack** — exact versions and tools
- **Folder structure** — where everything lives
- **Conventions** — language rules (UI text vs. code vs. DB), code style, security rules
- **Database** — migration conventions, UUID keys, CHECK constraints
- **Edge Functions** — Deno runtime rules, CORS, error handling
- **Railway Server** — Express routes, health check, webhook handling
- **Git workflow** — branch strategy, commit messages, auto-deploy
- **Environment variables** — complete list with placeholders
- **Business logic** — pricing, rules, state machines

### 2b: DESIGN.md

The visual design system. Provides your AI assistant with exact colors, fonts, and component rules so every page looks consistent.

Read `references/design-md-template.md` for the full template. Key sections:

- **Font** — Google Font name, weights, typography scale (desktop + mobile)
- **Colors** — brand colors with hex codes, neutrals, alpha variants
- **Gradients** — dark and light gradient definitions
- **Tailwind config** — ready-to-paste configuration
- **shadcn/ui theme** — CSS custom properties mapping
- **Component rules** — buttons, cards, inputs, navigation, chat, badges, tables

If the user has brand guidelines: extract colors, font, and rules from them.
If no brand guidelines exist: propose a professional palette (always include: primary, accent, neutral-600 for text, neutral-100 for backgrounds, white for cards).

### 2c: Database schema

Full SQL migration file with all tables, RLS policies, indices, and triggers.

Rules:
- Every table: `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
- Every table: `created_at TIMESTAMPTZ DEFAULT now()`, `updated_at TIMESTAMPTZ DEFAULT now()`
- Every table: `ALTER TABLE ... ENABLE ROW LEVEL SECURITY;` with at least one policy
- Enums: use `CHECK` constraints, not PostgreSQL enum types
- Foreign keys: always with `ON DELETE CASCADE` or explicit handling
- Order matters: create referenced tables BEFORE tables that reference them (especially for RLS policies that query other tables)
- Include `updated_at` trigger function
- Include Storage bucket creation if file uploads are needed
- Test the migration order by reading it top-to-bottom — every table and function must exist before it's referenced

---

## Phase 3: Infrastructure setup guide

Generate a step-by-step setup guide specifically for non-developers. This is critical — the user will follow these steps literally.

Read `references/setup-guide-template.md` for the full template.

### Key principles for setup guides

1. **Assume nothing.** Explain what to install, where to download it, and how to verify.
2. **Give exact commands.** No "configure your environment" — give the actual `cp .env.example .env.local` command.
3. **One step per numbered item.** Never combine two actions.
4. **Show expected output.** "You should see: `v20.x.x`" after `node --version`.
5. **Anticipate errors.** Add a troubleshooting section for common problems.
6. **Hardcode project-specific values.** Don't use `<your-project-ref>` — fill in the actual Supabase project ref, the actual Railway domain, the actual repo URL.

### Setup sections

1. Prerequisites (Node.js, Git, Supabase CLI)
2. Clone repo
3. Copy starter kit files
4. Connect Supabase (API keys, CLI login, link project)
5. Run database migration (`supabase db push`)
6. Connect Railway (deploy from GitHub, environment variables, custom domain)
7. Configure landing page links (point login/register to app subdomain)
8. First commit and deploy
9. Daily workflow summary (how to work with your AI assistant day-to-day)
10. Troubleshooting

---

## Phase 4: Landing page with SEO/GEO

Every production app needs a landing page. This phase covers both creation and optimization.

### Option A: Lovable landing page (recommended for speed)

If using Lovable, the landing page is a separate repo. Key tasks:
- Create landing page with hero, features, pricing, CTA sections
- All login/register buttons link to `https://app.[domain]/login` and `/register`
- Share the same Supabase project (if needed for contact forms, waitlist, etc.)

### Option B: WordPress landing page

When the user already has WordPress hosting or prefers it for CMS flexibility.
Read `references/wordpress-landing.md` for setup patterns.

### SEO optimization (apply to both options)

Every landing page must include:

**Technical SEO:**
- `<title>` tag with primary keyword (max 60 chars)
- `<meta name="description">` with value proposition (max 155 chars)
- Open Graph tags (og:title, og:description, og:image, og:url)
- Twitter Card tags
- Canonical URL
- `robots.txt` allowing crawling
- `sitemap.xml` with all public pages
- Schema.org structured data (Organization, SoftwareApplication, or appropriate type)
- Fast loading (< 3s LCP) — optimize images, lazy load below-the-fold
- Mobile responsive (Google mobile-first indexing)

**Content SEO:**
- H1 with primary keyword on every page
- Clear heading hierarchy (H1 → H2 → H3)
- Alt text on all images
- Internal linking between pages
- At least 300 words of unique content per page

### GEO optimization (for regional apps)

When the app targets a specific region (like Liechtenstein/Eastern Switzerland):

- `hreflang` tags if multiple language versions exist
- Local business Schema.org markup (address, region, phone)
- Region-specific keywords in titles and descriptions
- Google Business Profile entry (if applicable)
- Regional directory listings
- Content in the local language variant (e.g., Swiss German conventions: no ß, CHF instead of EUR)

Save SEO/GEO checklist as part of the setup guide or as a separate `SEO_CHECKLIST.md`.

---

## Phase 5: your AI assistant session prompts

The core output — numbered, self-contained prompts that the user copies into fresh your AI assistant sessions.

### Prompt design rules

1. **Each prompt starts with context.** your AI assistant has no memory between sessions. Every prompt must begin with "Lies zuerst CLAUDE.md und DESIGN.md" (or English equivalent) so the assistant loads the project context.

2. **Each prompt is one feature.** Never combine features. One prompt = one coherent feature that can be tested independently.

3. **Each prompt lists what exists.** Briefly state what was built in previous sessions so your AI assistant doesn't rebuild or break it.

4. **Each prompt is specific.** Not "build the dashboard" but a numbered list of exactly what to build, which components, which DB tables to use, which routes to create.

5. **Each prompt includes constraints.** Security rules, design rules, and "do not build" boundaries.

6. **Model recommendation per prompt.** Opus for architecture-heavy prompts (auth, chatbot, payment), Sonnet for feature-building prompts (CRUD, UI, search).

### Standard session sequence

Adapt to the specific app, but this order works for most projects:

| # | Feature | Model | Why this order |
|---|---------|-------|----------------|
| 1 | Auth (magic link / OAuth) + role selection | Opus | Foundation — everything depends on auth |
| 2 | Dashboard layout + sidebar + routing | Opus | Navigation structure before content |
| 3 | Primary user flow (onboarding, wizard, or main input) | Opus | Core value proposition |
| 4 | Secondary user flow (other role's perspective) | Opus | Completes the two-sided marketplace/flow |
| 5 | Search / browse / discovery | Sonnet | Users need to find things |
| 6 | Interaction workflow (contact, request, apply) | Sonnet | Connects the two sides |
| 7 | Content management (CRUD for domain objects) | Sonnet | Create, edit, list, delete |
| 8 | Auxiliary features (referrals, tracking, logging) | Sonnet | Nice-to-have but important |
| 9 | Verification / validation workflows | Sonnet | Data integrity |
| 10 | Payment integration (Stripe) | Sonnet | Last because it needs all other data |

### Prompt template

````markdown
## Prompt [N] — [Feature Name]

**Modell:** [Opus / Sonnet]

```
Du baust [feature description] für [App Name].

Lies zuerst CLAUDE.md und DESIGN.md im Repo-Root — dort stehen alle Konventionen, der Tech-Stack und das Design-System.

[What already exists from previous sessions — 2-3 sentences]

[DB tables relevant for this feature]

Baue folgendes:

1. **[Component/Feature]** ([route or file path])
   - [Specific requirement]
   - [Specific requirement]
   - [Design details from DESIGN.md]

2. **[Component/Feature]** ([route or file path])
   - [Specific requirement]
   - [Specific requirement]

[Security constraints, compliance rules, etc.]

UI-Texte auf [language]. Code auf Englisch.
Alle UI-Elemente mit shadcn/ui. Farben gemäss DESIGN.md.
```
````

### Tips section (append to prompts file)

Always include practical tips for the user at the end:

```markdown
## Tipps für die Arbeit mit your AI assistant

- **Ein Prompt pro Session.** Nicht mischen.
- **Testen nach jeder Session:** `npm run dev`, dann im Browser prüfen.
- **Bei Fehlern:** Fehlermeldung kopieren und your AI assistant geben.
- **Deployen:** `git add . && git commit -m "feat: ..." && git push origin main`
- **Railway deployed automatisch** nach jedem Push auf main.
```

---

## Phase 6: User manual and test protocol

After the app is built (all prompts completed), generate documentation.

### User manual (.docx)

Use the `docx` skill to create a professional manual. Chapters:

1. Einleitung — what the app does
2. Erste Schritte — login, onboarding
3. Navigation — sidebar overview
4. [Core feature chapters — one per major feature]
5. Einstellungen
6. Datenschutz + Export
7. FAQ (5-8 questions)
8. Support-Kontakt

### Test protocol (.docx)

Use the `docx` skill. Sections:

1. Einführung — time estimate, preparation
2. Test-Dateien — sample data needed
3. Testfälle (TC-01 bis TC-N) — one per feature
4. Nicht-funktionale Tests — mobile, error cases, performance
5. Feedback-Formular — rating 1-5 per feature
6. Offene Fragen
7. Bug-Report-Vorlage

---

## Delivery checklist

Before handing over to the user:

```
[ ] Requirements document — reviewed and confirmed by user?
[ ] CLAUDE.md — all conventions, stack, and business logic documented?
[ ] DESIGN.md — colors, fonts, components specified?
[ ] DB schema — all tables have RLS? Migration order correct?
[ ] Setup guide — tested step by step? No assumptions? Hosting option (Railway/Hetzner) correct?
[ ] Landing page — SEO meta tags? Schema.org? sitemap.xml?
[ ] GEO optimization — regional keywords? Local schema markup?
[ ] Session prompts — each self-contained? Model recommendations?
[ ] .env.example — all needed variables listed (no real keys)?
[ ] .gitignore — .env.local, node_modules, dist excluded?
```

---

## Reference files

- `references/claude-md-template.md` — Full CLAUDE.md template with all sections
- `references/design-md-template.md` — Full DESIGN.md template
- `references/setup-guide-template.md` — Infrastructure setup guide template
- `references/wordpress-landing.md` — WordPress landing page patterns
- `references/seo-geo-checklist.md` — Complete SEO/GEO optimization checklist
- `references/railway-deployment.md` — Railway-specific deployment patterns (default)
- `references/hetzner-deployment.md` — Hetzner VPS deployment (alternative to Railway)
- `references/supabase-patterns.md` — Supabase Edge Functions, RLS, Storage patterns
- `references/stripe-integration.md` — Stripe Checkout + Connect patterns
