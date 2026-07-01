# Argument Analysis Toolkit

Schritt-für-Schritt-Anleitung zur Dekonstruktion und Bewertung von Argumenten. Nutze dieses Toolkit, wenn eine Konversation komplexe Argumente, Geschäftsentscheidungen oder strategische Empfehlungen enthält.

---

## Phase 1: Argument identifizieren und übersetzen

### Schritt 1: Ist es überhaupt ein Argument?

Nicht jede Aussage ist ein Argument. Unterscheide:

- **Argument**: Behauptung + Begründung → "Wir sollten X tun, weil Y und Z"
- **Erklärung**: Beschreibung eines Sachverhalts → "So funktioniert das"
- **Meinung**: Unbegründete Präferenz → "Ich finde X gut"
- **Befehl**: Handlungsanweisung → "Mach X"

Nur Argumente können logisch analysiert werden. Bei Meinungen: nach Begründung fragen.

### Schritt 2: Argument in Prämissen und Schlussfolgerung zerlegen

**Übersetzungsregeln:**
1. **Genau übersetzen** — Keine Wörter hinzufügen oder weglassen, die den Sinn verändern
2. **Ökonomisch übersetzen** — So wenige Prämissen wie nötig (jede zusätzliche Prämisse = zusätzliche Angriffsfläche)
3. **Grosszügig übersetzen** (Principle of Charity) — Immer die stärkste Version des Arguments testen

**Beispiel:**
> "KI wird unsere Branche komplett umkrempeln. Jedes Unternehmen, das jetzt nicht investiert, wird in 5 Jahren nicht mehr existieren."

Übersetzt:
- **Prämisse 1**: KI verändert die Branche fundamental
- **Prämisse 2**: Unternehmen, die nicht in KI investieren, können in der veränderten Branche nicht bestehen
- **Prämisse 3 (versteckt)**: Es gibt keine andere Möglichkeit, sich anzupassen als KI-Investition
- **Schlussfolgerung**: Jedes Unternehmen muss jetzt in KI investieren

### Schritt 3: Versteckte Prämissen (Enthymeme) aufdecken

Die wichtigste Prämisse ist oft die, die NICHT ausgesprochen wird. Frage:
- "Was muss zusätzlich wahr sein, damit diese Schlussfolgerung folgt?"
- "Welche Annahme verbindet Prämisse X mit der Schlussfolgerung?"

Im Beispiel oben: Prämisse 3 ist das schwächste Glied — und sie war versteckt.

---

## Phase 2: Argument bewerten

### Deduktive Argumente (Schlussfolgerung MUSS folgen)

**Test 1 — Validität:**
"Kann ich die Prämissen als wahr akzeptieren UND trotzdem die Schlussfolgerung ablehnen?"
- Ja → Argument ist **ungültig** (invalide)
- Nein → Argument ist **gültig** (valide)

**Test 2 — Stichhaltigkeit (Soundness):**
"Sind alle Prämissen tatsächlich wahr?"
- Ja (und valide) → Argument ist **stichhaltig**
- Nein → Argument ist **nicht stichhaltig** (trotz Validität)

### Induktive Argumente (Schlussfolgerung ist WAHRSCHEINLICH)

**Stärke-Test:**
"Wie wahrscheinlich ist die Schlussfolgerung, wenn die Prämissen wahr sind?"
- Sehr wahrscheinlich → **starkes** induktives Argument
- Weniger wahrscheinlich → **schwaches** induktives Argument

**Relevanz der Prämissen:**
- Sind die Prämissen relevant für die Schlussfolgerung?
- Reichen die Prämissen aus (Stichprobengrösse, Datenqualität)?
- Sind die Prämissen akzeptabel (plausibel, belegt)?

---

## Phase 3: Häufige Argumentfehler erkennen

### Formale Fehler (Strukturfehler)

| Fehler | Muster | Beispiel |
|---|---|---|
| Denying the Antecedent | Wenn P dann Q. Nicht P. Also nicht Q. | "Wenn es regnet, wird das Spiel abgesagt. Es regnet nicht. Also findet das Spiel statt." (Falsch — es könnte andere Gründe für Absage geben) |
| Affirming the Consequent | Wenn P dann Q. Q. Also P. | "Wenn er betrogen hat, ist er pleite. Er ist pleite. Also hat er betrogen." (Falsch — viele Gründe für Pleite möglich) |
| Undistributed Middle | Alle A sind B. Alle C sind B. Also alle A sind C. | "Alle Hunde sind Tiere. Alle Katzen sind Tiere. Also sind alle Hunde Katzen." |

### Informale Fehler (Inhaltsfehler)

| Fehler | Was passiert | Gegenmittel |
|---|---|---|
| **Ad Hominem** | Person wird angegriffen statt Argument | "Was ist das Argument, unabhängig von der Person?" |
| **Strohmann** | Schwächere Version des Arguments wird angegriffen | "Ist das wirklich das, was gesagt wurde?" (Principle of Charity) |
| **Falsche Dichotomie** | Nur zwei Optionen präsentiert, obwohl mehr existieren | "Welche weiteren Optionen gibt es?" |
| **Hastige Verallgemeinerung** | Schluss von zu wenigen Fällen auf alle | "Wie gross ist die Stichprobe?" |
| **Zirkelschluss** | Schlussfolgerung ist in den Prämissen versteckt | "Setzt das nicht voraus, was es beweisen soll?" |
| **Red Herring** | Ablenkung vom eigentlichen Thema | "Was war die ursprüngliche Frage?" |
| **Slippery Slope** | Übertriebene Kausalkette ohne Belege | "Ist jeder Schritt in dieser Kette tatsächlich belegt?" |
| **Appeal to Emotion** | Gefühle statt Argumente | "Was ist die Evidenz jenseits der emotionalen Wirkung?" |
| **Kompositionsfehler** | Eigenschaft eines Teils wird auf das Ganze übertragen | "Gilt das für den Teil oder das Ganze?" |
| **Tu Quoque** | "Du machst das doch auch" als Gegenargument | "Das ändert nichts an der Gültigkeit des Arguments" |

---

## Phase 4: Problem-Reframing

Bevor du ein Problem löst, prüfe ob es das richtige Problem ist.

### Drei Reframing-Techniken:

**1. Subjekt wechseln:**
- Original: "Unsere Mitarbeiter nutzen die KI-Tools nicht"
- Reframe 1: "Unsere Manager schaffen kein Umfeld für KI-Nutzung"
- Reframe 2: "Unsere Organisation hat KI nicht in die Workflows integriert"
→ Jedes Subjekt führt zu anderen Lösungen

**2. Messung wechseln:**
- Original: "Wir haben zu wenig Innovation"
- Reframe 1: "Nur 5% unseres Umsatzes kommt von Produkten der letzten 3 Jahre"
- Reframe 2: "Wir bringen nur 1 neues Produkt pro Jahr auf den Markt"
→ Jede Messung zeigt eine andere Facette

**3. Ziel hinterfragen:**
- Statt "Wie machen wir den Fahrstuhl schneller?" → "Wie machen wir das Warten weniger störend?"
- Statt "Wie senken wir die Kosten?" → "Wie schaffen wir mehr Wert pro eingesetztem Euro?"

---

## Phase 5: Socratic Questioning Framework

Sechs Fragekategorien für tiefgehende Analyse:

| Kategorie | Beispielfragen | Ziel |
|---|---|---|
| **Klärung** | "Was genau meinst du mit X?" / "Kannst du ein Beispiel geben?" | Präzise Definitionen sicherstellen |
| **Annahmen prüfen** | "Warum muss das so sein?" / "Was wäre, wenn das Gegenteil stimmt?" | Ungeprüfte Prämissen aufdecken |
| **Evidenz suchen** | "Welche Daten stützen das?" / "Wie wissen wir das?" | Entscheidungen auf Fakten gründen |
| **Perspektiven wechseln** | "Wie würde ein Kunde/Konkurrent das sehen?" | Einseitigkeit durchbrechen |
| **Ursprung prüfen** | "Woher kommt diese Überzeugung?" / "Wer hat das zuerst gesagt?" | Quellen und Motive identifizieren |
| **Konsequenzen durchdenken** | "Was passiert, wenn wir das tun?" / "Was wenn wir es NICHT tun?" | Handlungsfolgen antizipieren |

---

## Schnell-Bewertung: Argument in 60 Sekunden prüfen

1. **Was ist die Schlussfolgerung?** (1 Satz)
2. **Was sind die Hauptgründe?** (Prämissen)
3. **Folgt die Schlussfolgerung logisch?** (Validität)
4. **Sind die Gründe wahr?** (Stichhaltigkeit)
5. **Was fehlt?** (Versteckte Prämissen, fehlende Perspektiven)
6. **Wie stark ist die Evidenz?** (Daten vs. Meinungen vs. Anekdoten)

---

## Quellen

- Haber, J. (2020). *Critical Thinking* — MIT Press Essential Knowledge Series
- Toulmin, S. (2003). *The Uses of Argument*
- HBR (2024). *HBR Guide to Critical Thinking*
- Wedell-Wedellsborg, T. (2020). *What's Your Problem?*
- Architecture of Foundational Reason — First Principles Analysis
