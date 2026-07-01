# Visual Elements Catalog — Branded Visual Factory

Komplettes Inventar aller visuellen Elemente, die per HTML/CSS + inline SVG in Infographics einsetzbar sind. Kein JavaScript nötig (ausser optional für Recharts/D3-Varianten).

---

## 1. DIAGRAMME & CHARTS

### Donut / Pie Chart (CSS conic-gradient)
Perfekt für Verteilungen, Anteile, Budget-Splits.
```css
.donut {
  width: 200px; height: 200px;
  border-radius: 50%;
  background: conic-gradient(
    var(--color-primary) 0% 65%,
    var(--color-secondary) 65% 85%,
    var(--color-fill-neutral) 85% 100%
  );
  /* Loch in der Mitte: */
  mask: radial-gradient(circle at center, transparent 60%, black 61%);
  -webkit-mask: radial-gradient(circle at center, transparent 60%, black 61%);
}
```
**Varianten:** Vollkreis (Pie), Halbkreis (Gauge), Dreiviertelkreis

### Horizontale Balken (CSS flexbox)
Perfekt für Vergleiche, Rankings, Vorher/Nachher.
```css
.bar {
  height: 32px;
  background: var(--color-primary);
  border-radius: 6px;
  width: 75%; /* = Datenwert */
  transition: width 0.5s;
}
```
**Varianten:** Gestapelt, gruppiert, mit Labels, mit Prozent-Anzeige

### Vertikale Balken (CSS grid)
Perfekt für Zeitreihen, Monatswerte, Quartalsvergleiche.
```css
.bar-chart {
  display: flex;
  align-items: flex-end;
  gap: 12px;
  height: 200px;
}
.bar-column {
  width: 48px;
  background: var(--color-primary);
  border-radius: 6px 6px 0 0;
  height: 75%; /* = Datenwert */
}
```

### Progress Ring / Gauge (SVG circle)
Perfekt für Zielerreichung, Scores, KPIs.
```html
<svg width="120" height="120" viewBox="0 0 120 120">
  <circle cx="60" cy="60" r="50" fill="none" stroke="#F2F2F2" stroke-width="10"/>
  <circle cx="60" cy="60" r="50" fill="none" stroke="#CC798E" stroke-width="10"
    stroke-dasharray="314" stroke-dashoffset="78" /* 75% gefüllt */
    transform="rotate(-90 60 60)" stroke-linecap="round"/>
</svg>
```

### Radar / Spider Chart (SVG polygon)
Perfekt für Kompetenzprofile, Reifegrad-Assessments, Multi-Dimensionen.
```html
<svg viewBox="0 0 200 200">
  <!-- Hintergrund-Raster (5 Stufen) -->
  <polygon points="..." fill="none" stroke="#F2F2F2"/>
  <!-- Datenfläche -->
  <polygon points="100,20 170,70 150,160 50,160 30,70"
    fill="rgba(204,121,142,0.3)" stroke="#CC798E" stroke-width="2"/>
  <!-- Datenpunkte -->
  <circle cx="100" cy="20" r="4" fill="#CC798E"/>
</svg>
```

### Sparkline (SVG path)
Perfekt für Trend-Indikatoren in kleinem Raum.
```html
<svg width="120" height="40" viewBox="0 0 120 40">
  <path d="M0,35 L20,28 L40,30 L60,15 L80,18 L100,8 L120,5"
    fill="none" stroke="#CC798E" stroke-width="2"/>
</svg>
```

### Funnel Chart (CSS trapezoids)
Perfekt für Sales Funnels, Conversion Flows.
```css
.funnel-step {
  height: 48px;
  background: var(--color-primary);
  margin: 0 auto;
  border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  color: white;
}
/* Jede Stufe schmaler */
.funnel-step:nth-child(1) { width: 100%; }
.funnel-step:nth-child(2) { width: 80%; }
.funnel-step:nth-child(3) { width: 60%; }
.funnel-step:nth-child(4) { width: 40%; }
```

### Treemap (CSS grid)
Perfekt für Budget-Verteilungen, Marktanteile.
```css
.treemap {
  display: grid;
  grid-template-columns: 3fr 2fr 1fr;
  grid-template-rows: 2fr 1fr;
  gap: 4px;
  height: 300px;
}
.treemap__cell {
  border-radius: 8px;
  padding: 12px;
  display: flex; flex-direction: column; justify-content: flex-end;
}
```

---

## 2. LAYOUT-STRUKTUREN

### Org Chart / Hierarchie-Baum
Perfekt für Team-Strukturen, Skill-Übersichten (wie Charlie Hills' Beispiel).
- CSS Grid + Border-Verbindungen
- Karten mit Avataren, Titeln, Beschreibungen
- Farbkodierte Kategorien als Pill-Badges

### Flowchart mit Pfeilen
Perfekt für Entscheidungsbäume, Prozessabläufe.
- CSS Flexbox + SVG Arrow-Connectors
- Entscheidungsknoten (Rauten per CSS transform: rotate(45deg))
- Ja/Nein-Verzweigungen

### Matrix / Quadrant-Diagramm (2x2)
Perfekt für Priorisierung, Einordnung, Strategiefelder.
```css
.matrix {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 4px;
  position: relative;
}
/* Achsenbeschriftungen als absolute Elemente */
```

### Timeline (horizontal oder vertikal)
Perfekt für Roadmaps, historische Entwicklung, Phasenmodelle.
- Zentrale Linie + Marker-Punkte + Karten links/rechts abwechselnd

### Kanban-Board
Perfekt für Workflow-Darstellungen, Status-Übersichten.
- 3-4 Spalten: To Do / In Progress / Done
- Karten mit Mini-Tags

### Venn-Diagramm (CSS circles + mix-blend-mode)
Perfekt für Überschneidungen, Synthesen.
```css
.venn-circle {
  width: 250px; height: 250px;
  border-radius: 50%;
  background: rgba(204,121,142,0.4);
  position: absolute;
  mix-blend-mode: multiply;
}
```

### Mind Map / Radial Layout
Perfekt für Themen-Cluster, Ideenräume.
- Zentraler Knoten + radiale Äste mit SVG Lines

### Vergleichs-Tabelle (styled HTML table)
Perfekt für Feature-Vergleiche, Tool-Gegenüberstellungen.
- Zebra-Stripes, Checkmarks (✓/✗), farbkodierte Bewertungen

---

## 3. DATEN-DISPLAY-ELEMENTE

### Grosse Zahl + Kontext (Hero Stat)
```css
.hero-stat { font-size: 120px; font-weight: 700; color: var(--color-primary); }
.hero-context { font-size: 22px; opacity: 0.7; }
```

### KPI-Karte (Zahl + Trend-Pfeil + Label)
```
┌──────────────┐
│  ↑ 23%       │
│  Revenue     │
│  CHF 1.2M    │
└──────────────┘
```

### Fortschrittsbalken mit Label
```css
.progress { height: 12px; background: var(--color-fill-neutral); border-radius: 6px; }
.progress__fill { height: 100%; background: var(--color-primary); border-radius: 6px; width: 73%; }
```

### Score / Rating (gefüllte Kreise)
○○○○○ → ●●●●○ (4/5)

### Countdown / Metric Row
Drei bis fünf KPIs nebeneinander in einer Reihe, je mit Zahl + Label.

### Heatmap (CSS Grid + Farbabstufungen)
Perfekt für Kalender-Übersichten, Skill-Matrizen.
- Grid-Zellen mit Opacity-Abstufungen der Akzentfarbe

---

## 4. DEKORATIVE & STRUKTURELLE ELEMENTE

### Icons (Unicode + SVG)
- ✓ ✗ → ← ↑ ↓ ⚡ ⏱ 📊 🎯 ⚙️ (Unicode, sparsam)
- Besser: Inline SVG Icons (Lucide-Style, 24x24, 1.5px stroke)

### Badges / Pills
```css
.badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  background: var(--color-primary);
  color: white;
}
```

### Farbkodierte Kategorie-Marker
Wie in Charlie Hills' Beispiel: farbige Balken oben an Spalten.
```css
.category-bar {
  height: 6px;
  border-radius: 3px;
  background: var(--color-primary);
}
```

### Verbindungslinien (CSS borders + SVG)
- Gestrichelt: `border: 2px dashed #F2F2F2`
- Durchgezogen mit Pfeil: SVG path + marker-end
- L-förmig: CSS borders auf Pseudo-Elementen

### Avatar-Platzhalter
```css
.avatar {
  width: 48px; height: 48px;
  border-radius: 50%;
  background: var(--color-fill-light);
  border: 2px solid var(--color-primary);
  display: flex; align-items: center; justify-content: center;
}
```

### Trennlinien-Varianten
- Dünn: `1px solid #F2F2F2`
- Akzent: `2px solid #CC798E`
- Gepunktet: `2px dotted #F2F2F2`
- Gradient (nur FlowMomentum): `linear-gradient(...)`

### Nummerierte Schritte (verschiedene Stile)
- Kreis mit Zahl (wie bisher)
- Quadrat mit gerundeten Ecken
- Hexagon (CSS clip-path)
- Linie mit Punkt (Timeline-Stil)

### Callout-Boxen
- Info-Box (linker Farbbalken)
- Highlight-Box (vollfarbiger Hintergrund)
- Quote-Box (grosse Anführungszeichen)
- Warning-Box (Rahmen + Icon)

### Dekorative Shapes (FlowMomentum)
- Organische Wellenformen (SVG path, echo Logo)
- Kreise mit Opacity
- Gradient-Overlays auf Sektionen

---

## 5. KOMBINATIONEN FÜR MAXIMALE WIRKUNG

### "Dashboard-Stil" Infographic
Kombination aus:
- 2-3 KPI-Karten oben (Hero Stats)
- 1 Donut Chart (Verteilung)
- 1-2 Horizontal Bars (Vergleich)
- 1 Sparkline (Trend)
- Callout-Box unten (Key Takeaway)

### "Org Chart" Infographic (Charlie Hills Stil)
Kombination aus:
- Hierarchie-Knoten mit Avatar + Title + Description
- Farbkodierte Kategorie-Badges
- Gestrichelte Verbindungslinien
- Grid-Layout für die Team-Ebene

### "Assessment / Scorecard" Infographic
Kombination aus:
- Radar Chart (Gesamtbild)
- 4-6 Progress Rings (Detail-KPIs)
- Ampel-Badges (Rot/Gelb/Grün → in Brand-Farben)
- Score-Summe als Hero Stat

### "Funnel + Metrics" Infographic
Kombination aus:
- Funnel Chart (Phasen)
- KPI-Karten pro Phase (Conversion Rate)
- Pfeil-Connectors
- Highlight-Box (bester Hebel)

### "Comparison Matrix" Infographic
Kombination aus:
- Styled Tabelle (2-4 Spalten)
- Checkmarks und X-Marks
- Farbkodierte Bewertungs-Badges
- Winner-Badge oben
- Fussnote mit Quelle

### "Process + Data" Hybrid
Kombination aus:
- Timeline/Steps links (Prozess)
- Daten-Visualisierung rechts (Chart zu jedem Schritt)
- Verbindungslinien zwischen Steps und Charts
- Highlight-Box am Ende

---

## ENTSCHEIDUNGSHILFE: Welches Element für welche Daten?

| Datentyp | Bestes Element | Alternative |
|----------|---------------|------------|
| Ein Anteil (z.B. "65%") | Donut/Gauge | Hero Stat |
| Mehrere Anteile (Budget-Split) | Donut/Pie | Treemap |
| Vergleich 2-5 Werte | Horizontale Balken | Vergleichs-Tabelle |
| Zeitreihe (Quartale) | Vertikale Balken | Sparkline |
| Zielerreichung (Score) | Progress Ring | Fortschrittsbalken |
| Mehrere Dimensionen | Radar Chart | Matrix/Quadrant |
| Phasen/Stufen | Funnel | Timeline |
| Ja/Nein-Vergleich | Tabelle mit ✓/✗ | Side-by-Side Cards |
| Hierarchie/Struktur | Org Chart | Mind Map |
| Entscheidungsbaum | Flowchart | Matrix |
| Trend-Richtung | Sparkline + Pfeil | KPI-Karte mit ↑↓ |
| Reifegrad / Assessment | Radar + Progress Rings | Score Cards |
