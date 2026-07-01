---
name: digitalscheck-navigator
description: "Begleitet KMU durch alle drei Module des Digitalscheck Liechtenstein (KONZEPT, INVEST, TRAINING). Erstellt Anträge, Offerten, Kostenrechnungen, Prozessanalysen (IST/SOLL), Massnahmenpläne, Implementierungspläne und Abschlussberichte – alles konform zur AVW-Richtlinie 2025. Nutze diesen Skill immer wenn ein Nutzer den Digitalscheck, eine Digitalisierungsförderung in Liechtenstein, ein KMU-Digitalisierungsprojekt mit Fördermitteln, oder Module wie Digital KONZEPT, Digital INVEST oder Digital TRAINING erwähnt. Auch bei Begriffen wie 'Amt für Volkswirtschaft Förderung', 'Digitalisierungsscheck FL', 'KMU-Förderung Liechtenstein' oder wenn ein Angebot, Antrag oder Abschlussbericht für ein Digitalischeck-Projekt erstellt werden soll."
---

# Digitalscheck Navigator

Dieser Skill unterstützt MMIND.ai dabei, liechtensteinische KMU durch den kompletten Digitalscheck-Förderprozess zu begleiten – von der Antragstellung über die Durchführung bis zum Abschlussbericht.

## Kontext

Der Digitalscheck ist ein Förderinstrument des Amts für Volkswirtschaft (AVW) des Fürstentums Liechtenstein. Er unterstützt KMU bei der digitalen Transformation ihrer Wertschöpfungskette. Die Grundlage bildet die Richtlinie vom 25. Februar 2025 (LNR 2025-332 BNR 2025/320).

Für die Detailbestimmungen lies `references/richtlinie-zusammenfassung.md`.

## Die drei Module im Überblick

| Modul | Ziel | Förderquote | Max. Förderung | Laufzeit |
|-------|------|-------------|----------------|----------|
| **Digital KONZEPT** | IST/SOLL-Analyse, Massnahmenkatalog, Implementierungsplan | 50% | CHF 15'000 | 6 Monate |
| **Digital INVEST** | Umsetzung der Massnahmen aus KONZEPT | 20% | CHF 30'000 | 12 Monate |
| **Digital TRAINING** | Schulung der Mitarbeitenden | 30% | CHF 15'000 | 6 Monate |

Jedes Modul wird separat beantragt. Die Module bauen aufeinander auf: KONZEPT ist Voraussetzung für INVEST und TRAINING.

## Förderbare Kosten

Gefördert werden **interne und externe Personalkosten**:
- Externe Leistungen: max. CHF 150/Std. (CHF 1'200/Tag)
- Interne Kosten Mitarbeitende: max. CHF 100/Std.
- Interne Kosten leitende Funktion: max. CHF 150/Std.

**Nicht gefördert** werden: Hardware, Standardsoftware/Lizenzen, Reisekosten, F&E, allgemeine Digitalisierungsstrategien.

## Vorgehensmodell: KONZEPT-Phase

Der MMIND.ai-Ansatz für Digital KONZEPT orientiert sich am **Leitfaden Digitalisierung für KMU** (MMIND.ai / KMU-HSG Universität St. Gallen) und umfasst folgende Module:

### Modul 1: Ziele und Anwendungsbeispiele für KI-Digitalisierung
- Kick-Off-Workshop mit Geschäftsleitung und Schlüsselpersonen
- Definition des konkreten Digitalisierungsziels
- Vorstellung von KI-Anwendungsbeispielen aus der Branche
- Identifikation der relevanten Geschäftsprozesse

### Modul 2: Prozessanalyse (IST vs. SOLL)
- Aufnahme der Kern-, Management- und Unterstützungsprozesse
- Dokumentation des IST-Zustands aller relevanten Prozesse
- Erarbeitung des SOLL-Zustands (digitalisiert/optimiert)
- Priorisierung mittels Aufwand-Nutzen-Matrix

### Modul 3: Prototypen-Entwicklung
- Ausarbeitung von zwei KI-Prototypen (z.B. auf Basis the assistant, Google AI Studio, Cursor)
- Proof of Concept im Workshop-Format
- Validierung der Machbarkeit und des Nutzens

### Modul 4: Massnahmenplan für INVEST und TRAINING
- Ableitung konkreter Digitalisierungsmassnahmen
- Kostenschätzung und Priorisierung
- Erstellung eines Implementierungsplans (Gantt-Chart)
- Definition der Schulungsmassnahmen für TRAINING

### Modul 5: Kostenrechnung und Antrag
- Berechnung der internen und externen Kosten
- Erstellung des Förderantrags für das AVW
- Abgleich mit Fördervoraussetzungen

## Kostenrechnung: Strategische Gestaltung

Die Kostenrechnung ist entscheidend für die Förderhöhe. Die Strategie:

**Ziel: Möglichst hoher Anteil interner Stunden**, damit die externen Kosten durch die 50%-Förderung möglichst vollständig gedeckt sind.

Bewährte Struktur (Beispiel HSW):

### Interne Kosten
| Aktivität | GL (Std.) | PL (Std.) | MA (Std.) | Stundensatz |
|-----------|-----------|-----------|-----------|-------------|
| Startaufwand / Vorbereitung | 4 | 4 | 0 | 150/120/100 |
| Kick-Off-Workshop (WS1) | 2 | 2×7 | 0 | 150/120/100 |
| Einsatzbesuche & Datensammlung | 3 | 3×7 | 3×7 | 150/120/100 |
| Präsentation Konzept (WS2) | 2 | 2×7 | 0 | 150/120/100 |
| Prototypen-Entwicklung | 2 | 3×7 | 0 | 150/120/100 |
| Implementierungsplan (WS3) | 2 | 3×3 | 0 | 150/120/100 |
| Fortlaufende Projektbetreuung | 0 | 0 | 0×2 | 100 |

### Externe Kosten
| Aktivität | Stunden | Stundensatz |
|-----------|---------|-------------|
| Vorbereitung Kick-Off-Workshop | 8 | CHF 150 |
| Einsatzbesuche & Datensammlung | 36 | CHF 150 |
| Präsentation Konzept & Massnahmenkatalog | 12 | CHF 150 |
| Prototypen-Entwicklung | 28 | CHF 150 |
| Implementierungsplan Workshop | 8 | CHF 150 |

**Wichtig**: Die "Personen"-Spalte bei Projektleitung multipliziert die Stunden, wenn mehrere Personen teilnehmen. Workshop-Format sichert hohe interne Stunden.

## Workflow: Angebotserstellung KONZEPT

Wenn ein Nutzer ein KONZEPT-Angebot für einen neuen Kunden erstellen möchte:

1. **Kundendaten erfassen**: Firma, Ansprechpartner, Branche, Mitarbeiterzahl, Sitz in FL, Bestehensdauer ≥3 Jahre
2. **Vorgespräch auswerten**: Transkript analysieren, Schmerzpunkte identifizieren, Use Cases ableiten
3. **Module konfigurieren**: Basierend auf Kundenbedarf die 5 Module anpassen
4. **Kostenrechnung erstellen**: Interne/externe Stunden kalkulieren, 50%-Förderung berechnen
5. **Angebot generieren**: Modulares docx mit Kundenspezifik

Für die Angebotsvorlage lies `references/angebot-template.md`.

## Workflow: Abschlussbericht KONZEPT

Der Abschlussbericht dokumentiert:
- Digitalisierungsziel und ausgesuchte Geschäftsprozesse
- IST-/SOLL-Prozessbeschreibungen
- Massnahmenkatalog mit Kostenschätzung und Priorisierung
- Implementierungsplan (Gantt-Chart)
- Arbeitsdokument mit Nachweisen

Format: Formular "Abschlussbericht" des AVW + Arbeitsdokument.

## Workflow: INVEST-Phase

1. Massnahmenplan aus KONZEPT als Basis
2. Separater Antrag beim AVW
3. Umsetzung der technischen Entwicklung (Apps, Integrationen, Automationen)
4. Abschlussbericht inkl. IT-Architekturskizzen
5. Förderquote: 20% der förderbaren Kosten, max. CHF 30'000

## Workflow: TRAINING-Phase

1. Ausbildungsplan erstellen (Ziel, Zeitrahmen, Inhalt, Methodik)
2. Separater Antrag beim AVW
3. Durchführung der Schulungen (nicht ausschliesslich am Arbeitsplatz)
4. Abschlussbericht mit Teilnehmerliste und Schulungsunterlagen
5. Förderquote: 30% der förderbaren Kosten, max. CHF 15'000

## Fördervoraussetzungen prüfen

Bevor ein Antrag erstellt wird, folgende Punkte prüfen:
- [ ] Privates Unternehmen mit ≤249 Beschäftigten
- [ ] Sitz in Liechtenstein
- [ ] Mind. 3 Jahre wirtschaftlich tätig
- [ ] Unbeschränkt steuerpflichtig in FL
- [ ] Kein Insolvenzverfahren
- [ ] Keine offenen AHV-/Steuerschulden
- [ ] Nachhaltige Wertschöpfung in FL erwartet
- [ ] Digitalscheck noch nie beantragt (einmalig pro KMU)

## Beihilfenregelung

De-minimis-Beihilfe: max. EUR 200'000 pro Unternehmensgruppe (verbundene Unternehmen). Alle De-minimis-Förderungen der letzten 2 Jahre + laufendes Jahr sind anzugeben.

## Referenzdokumente

- `references/richtlinie-zusammenfassung.md` – Detaillierte Zusammenfassung der AVW-Richtlinie 2025
- `references/angebot-template.md` – Modulare Angebotsvorlage für KONZEPT-Phase
- `references/kostenrechnung-vorlage.md` – Kalkulationsvorlage mit Formeln
- `references/leitfaden-prozessmodell.md` – Prozessmodell aus dem Leitfaden Digitalisierung
