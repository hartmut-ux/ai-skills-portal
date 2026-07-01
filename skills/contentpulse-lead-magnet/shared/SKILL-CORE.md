---
name: contentpulse-lead-magnet
description: "Erstellt professionelle Lead Magnets aus ContentPulse-Exports: Cheat Sheets (HTML/CSS via branded-visual-factory), Whitepapers (.docx), Präsentationen (.pptx). Nimmt strukturierte Prompts aus ContentPulse entgegen mit Thema, Research-Summary, Quellen-Links, Brand-Profil und Format-Wahl. Use when user pastes a ContentPulse lead magnet prompt, mentions 'ContentPulse Lead Magnet', 'Lead Magnet erstellen', 'Cheat Sheet aus ContentPulse', 'Whitepaper erstellen', 'Präsentation aus Research', or when a structured JSON block with contentpulse_export marker is present. Also triggers on: 'Lead Magnet aus meiner Recherche', 'mach ein Cheat Sheet zu', 'erstelle ein Whitepaper', 'Präsentation aus Wiki-Wissen'."
---

# ContentPulse Lead Magnet Factory

Erstellt professionelle, brand-konforme Lead Magnets aus ContentPulse-Daten. Dieses Skill ist das Gegenstück zum Prompt-Generator in ContentPulse — es empfängt strukturierte Inputs und routet sie an den passenden Produktions-Skill.

## Wie es funktioniert

1. User kopiert einen strukturierten Prompt aus ContentPulse
2. Dieses Skill erkennt das Format und extrahiert die Daten
3. Je nach gewähltem Format wird an den richtigen Sub-Skill delegiert
4. Ergebnis: Ein fertiges, brand-konformes Deliverable

## Input-Format erkennen

ContentPulse generiert Prompts mit einem eindeutigen Marker. Erkenne diesen Block:

```
## CONTENTPULSE LEAD MAGNET EXPORT
format: cheat_sheet | whitepaper | presentation | checklist | framework | mini_guide
brand: MMIND.ai | FlowMomentum.ai | [custom]
```

Wenn dieser Block vorhanden ist, aktiviere diesen Skill automatisch.

Falls der User KEINEN strukturierten Prompt hat, aber ein Lead Magnet erstellen will, führe ihn durch die Eingabe (siehe Abschnitt "Manueller Modus").

## Routing-Logik

| Format | Ziel-Skill | Datei-Typ | Beschreibung |
|--------|-----------|-----------|-------------|
| `cheat_sheet` | branded-visual-factory | .html → .png | 1-seitige visuelle Zusammenfassung, Grid-Layout |
| `checklist` | branded-visual-factory | .html → .png | Checkbox-Liste, visuell ansprechend |
| `whitepaper` | docx | .docx | 4-8 Seiten, professionelles Layout mit TOC |
| `presentation` | pptx | .pptx | 8-15 Slides, Brand-konform |
| `framework` | branded-visual-factory | .html → .png | Visuelles Framework-Diagramm, 3-5 Schritte |
| `mini_guide` | docx | .docx | 2-4 Seiten, kompakte Anleitung |

## Schritt-für-Schritt-Workflow

### Schritt 1: Input parsen

Extrahiere aus dem ContentPulse-Prompt:

| Feld | Pflicht | Verwendung |
|------|---------|-----------|
| `topic` | Ja | Hauptthema des Lead Magnets |
| `format` | Ja | Bestimmt den Routing-Pfad |
| `brand` | Ja | Bestimmt Farben, Fonts, Logo |
| `research_summary` | Ja | Inhaltliche Basis mit Key Stats |
| `sources` | Ja | Original-Quellen mit URLs für Zitate |
| `key_stats` | Nein | Hervorgehobene Zahlen/Daten |
| `frameworks` | Nein | Eigene Frameworks des Users |
| `target_audience` | Nein | ICP-Beschreibung für Tonalität |
| `product_description` | Nein | Was der User verkauft (für CTA) |
| `lead_magnet_cta` | Nein | Gewünschter Call-to-Action |
| `post_hooks` | Nein | Vorgeschlagene LinkedIn-Post-Hooks |

### Schritt 2: Brand laden

Lies die passende Brand-Datei:
- MMIND.ai → Lies `references/brand-mmind-summary.md` (enthält Farben, Fonts, Stil-Regeln)
- FlowMomentum.ai → Frage den User nach Brand-Details oder nutze branded-visual-factory brands/flowmomentum.md
- Custom → Extrahiere Brand-Infos aus dem Prompt (colors, fonts, logo_url)

### Schritt 3: An Sub-Skill delegieren

#### Route A: Cheat Sheet / Checklist / Framework → branded-visual-factory

Rufe den branded-visual-factory Skill auf. Übergib:

```
Erstelle ein [cheat_sheet/checklist/framework] zum Thema: [topic]

Brand: [brand] (lade die passende Brand-Config)

INHALT:
[research_summary — aufbereitet als Punkte/Sektionen]

KEY STATS:
[key_stats — als hervorgehobene Datenpunkte]

QUELLEN:
[sources — als Fussnoten-Referenzen]

CTA:
[lead_magnet_cta oder Default: "Mehr erfahren: [website]"]

EIGENE FRAMEWORKS:
[frameworks — falls vorhanden, als visuelles Element integrieren]
```

Beachte die Regeln der branded-visual-factory:
- Exakte Dimensionen (1080x1350 für Social, A4 für Print)
- NUR Brand-Palette-Farben
- Keine Gradients, Shadows bei MMIND.ai
- Logo-Position gemäss Brand-Config
- QA-Validierung vor Ausgabe

#### Route B: Whitepaper / Mini-Guide → docx

Rufe den docx Skill auf. Lies zuerst die SKILL.md des docx-Skills. Erstelle ein professionelles Word-Dokument:

**Whitepaper-Struktur (4-8 Seiten):**
1. Titelseite: Titel + Untertitel + Brand-Logo + Autor
2. Inhaltsverzeichnis
3. Executive Summary (1 Absatz)
4. Problemstellung (aus research_summary)
5. Analyse / Hauptteil (2-4 Abschnitte mit Daten aus key_stats)
6. Framework / Lösung (aus frameworks, falls vorhanden)
7. Handlungsempfehlungen (3-5 konkrete Schritte)
8. Über den Autor + CTA
9. Quellenverzeichnis (aus sources — mit funktionierenden URLs)

**Formatierung:**
- Brand-Farben für Überschriften
- Inter (MMIND.ai) oder Satoshi (FlowMomentum) als Schrift
- Quellenangaben als Fussnoten mit Nummern
- Jede Behauptung muss auf eine Quelle aus sources verweisen
- Schweizer Rechtschreibung (ss statt ß)

**Mini-Guide-Struktur (2-4 Seiten):**
1. Titel + Brand-Logo
2. Problem: Warum ist das wichtig? (1 Absatz)
3. Lösung: 3-5 Schritte (je 1 Absatz + Beispiel)
4. Quick-Wins: Was kann der Leser SOFORT tun?
5. CTA + Kontaktinfo

#### Route C: Präsentation → pptx

Rufe den pptx Skill auf. Lies zuerst die SKILL.md des pptx-Skills. Erstelle eine professionelle Präsentation:

**Präsentations-Struktur (8-15 Slides):**
1. Titel-Slide: Thema + Untertitel + Brand-Logo
2. Problem-Slide: "Warum das wichtig ist" — 1 Key Stat gross
3. Kontext-Slide: 3 Fakten aus der Recherche
4-8. Hauptteil: Je 1 Slide pro Kernaussage (1 Punkt + 1 Visualisierung)
9. Framework-Slide (falls vorhanden): Eigenes Framework visuell dargestellt
10. Handlungsempfehlungen: 3-5 konkrete Schritte
11. Zusammenfassung: 3 Takeaways
12. CTA-Slide: Kontakt + Lead-Magnet-Link + QR-Code (optional)

**Formatierung:**
- Brand-Farben für Akzente und Überschriften
- Maximal 6 Wörter pro Überschrift
- Maximal 3 Bullet Points pro Slide
- Jede Zahl/Statistik mit Quellenangabe (klein, unten rechts)
- Speaker Notes mit Kontext aus research_summary

### Schritt 4: Quellen-Integrität prüfen

Vor der finalen Ausgabe:
- [ ] Jede Zahl/Statistik hat eine Quellenangabe
- [ ] Alle Quellen-URLs aus dem ContentPulse-Export sind verlinkt
- [ ] Keine halluzinierten Statistiken (nur Daten aus research_summary + sources)
- [ ] CTA enthält einen konkreten nächsten Schritt

### Schritt 5: Begleit-Content generieren

Nach dem Lead Magnet: Generiere automatisch 3 LinkedIn-Post-Hooks, die auf den Lead Magnet verweisen. Nutze die post_hooks aus dem Export als Basis, oder generiere neue:

```
Hook 1 (TOFU — Aufmerksamkeit):
"[Provokante Statistik aus dem Lead Magnet]. Ich habe [Format] dazu erstellt — Link im ersten Kommentar."

Hook 2 (MOFU — Vertrauen):
"[Framework-Name] — mein [Zahl]-Schritte-System für [Ergebnis]. Kostenloses [Format] zum Download."

Hook 3 (BOFU — Konversion):
"[Konkretes Ergebnis eines Kunden]. Den kompletten Leitfaden gibt es als [Format] — Link unten."
```

## Manueller Modus (ohne ContentPulse-Export)

Wenn der User kein strukturiertes Prompt aus ContentPulse hat, frage:

1. "Zu welchem Thema soll der Lead Magnet sein?"
2. "Welches Format? (Cheat Sheet, Whitepaper, Präsentation, Checklist, Framework, Kurzanleitung)"
3. "Welche Marke? (MMIND.ai, FlowMomentum.ai, oder andere)"
4. "Hast du Research-Material oder Quellen, die ich verwenden soll?"
5. "Was ist der CTA — was soll der Leser nach dem Lesen tun?"

Dann sammle die Antworten und verfahre wie oben.

## Qualitäts-Regeln (IMMER)

- **Keine leeren Superlative** ("best-in-class", "world-class", "industry-leading")
- **Keine AI-Phrasen** ("delve into", "dive deep", "let's unpack")
- **Schweizer Rechtschreibung** (ss statt ß)
- **Konkrete Zahlen** statt vage Aussagen
- **Jede Behauptung mit Quelle** aus dem Export
- **Brand-konform** — keine Farben/Fonts ausserhalb der Palette
- **Sofort nutzbar** — der User muss nichts nachbearbeiten

## Beispiel-Workflow

```
User pastet aus ContentPulse:

## CONTENTPULSE LEAD MAGNET EXPORT
format: cheat_sheet
brand: MMIND.ai
topic: 5 KPIs für KI-Readiness in KMU
research_summary: |
  Laut einer Studie von MIT Sloan (2025) messen nur 12% der KMU ihre KI-Readiness systematisch.
  Die wichtigsten Indikatoren: Datenqualität, Prozessdigitalisierung, Mitarbeiter-Skills,
  Budget-Allokation, Führungs-Commitment. McKinsey-freie Alternative: Fraunhofer KI-Readiness-Check.
sources:
  - title: "MIT Sloan: AI Readiness Index"
    url: "https://sloanreview.mit.edu/ai-readiness-2025"
    date: "2025-03"
  - title: "Fraunhofer KI-Readiness-Check"
    url: "https://www.fraunhofer.de/ki-readiness"
    date: "2025-06"
key_stats:
  - "12% der KMU messen KI-Readiness systematisch"
  - "3.2x höhere Erfolgsrate bei strukturiertem Assessment"
frameworks:
  - name: "MMIND KI-Readiness-Radar"
    steps: ["Daten-Audit", "Prozess-Scan", "Team-Assessment", "Budget-Check", "Leadership-Alignment"]
target_audience: "KMU-CEOs, 10-250 Mitarbeitende, DACH"
product_description: "AI-Beratung für KMU — von der Strategie bis zur Implementierung"
lead_magnet_cta: "Kostenlosen KI-Readiness-Check buchen: https://mmind.space/readiness"

→ the assistant erkennt den Marker
→ Lädt branded-visual-factory
→ Lädt brands/mmind.md
→ Erstellt ein Cheat Sheet mit 5 KPIs, Key Stats, Framework-Visualisierung, Quellen, CTA
→ Exportiert als HTML + PNG
→ Generiert 3 LinkedIn-Post-Hooks
```
