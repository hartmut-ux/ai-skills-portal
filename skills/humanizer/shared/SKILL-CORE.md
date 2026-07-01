---
name: humanizer
description: Erkennt und entfernt typische KI-Sprachmuster aus Texten (Deutsch CH, Deutsch DE, US-English, British English), damit Inhalte natürlich und menschlich klingen. Trigger 'humanisiere', 'menschlicher klingen', 'KI-Sprache entfernen', 'mach das menschlicher', 'humanize', 'remove AI patterns', 'Schweizer Hochdeutsch', 'für die Schweiz', 'in British English', oder wenn User AI-generierten Text zur Überarbeitung einfügt. Deckt 29 EN-Patterns + 18 DE-Patterns + CH-Blacklist (Guillemets, Apostroph-Tausender, Em-dash-Vermeidung, Helvetismen, ss statt ß) + British-English-Modus (organise/colour/centre) ab. Optional Voice-Kalibrierung auf Marken (MMIND.ai, Kaizen, Flowstate, Hartmut persönlich).
license: MIT
metadata:
  author: Hartmut Hübner / MMIND.ai
  version: 3.2.0
  category: writing-quality
  tags: [humanize, editing, ai-detection, de-ch, de-de, en-us, en-gb]
  based-on: github.com/blader/humanizer (v2.5.1) + Wikipedia "Signs of AI writing"
---

# Humanizer v3.2 — KI-Sprache entfernen (DE-CH + DE-DE + EN-US + EN-GB)

Editor, der typische KI-Sprachmuster aus Texten entfernt und auf eine natürliche, menschliche Stimme bringt. Kombiniert die 29 englischen Patterns aus Wikipedia "Signs of AI writing" mit 18 deutschen Patterns, einer Schweiz-Blacklist (CH1–CH8), einem British-English-Modus und Marken-Voice-Profilen.

## Anti-Overcorrection-Regel (lies das zuerst)

Mechanisches Entfernen aller Patterns produziert ein neues KI-Muster (Goodharts Gesetz). Drei Schutzschritte:

1. **Kontext schlägt Regel.** Wenn ein "verbotener" Begriff fachlich präzise ist, bleibt er.
2. **Authentizität vor Säuberung.** Lieber kleinen KI-Tell stehen lassen als künstliche Kanten einbauen, die selbst zum Tell werden.
3. **Originalintention erhalten.** Der Text soll nach dem Autor klingen, nicht nach diesem Skill.

## Workflow (4 Schritte)

1. **Modus klären.** Erkenne aus Kontext oder frage einmal kurz:
   - Sprache & Region: Deutsch-CH (Schweizer Hochdeutsch + Helvetismen) / Deutsch-DE (Standard) / English-US / English-UK
   - Marke / Stimme: MMIND / Kaizen / Flowstate / Hartmut persönlich / unbekannt
   - Output-Modus: `minimal` (nur Tells entfernen, Stil unverändert) oder `full` (Tells entfernen + Voice angleichen)
2. **Pattern-Scan.** Gehe die relevanten Listen durch (DE-Patterns + CH-Blacklist bei DE-CH, BrE-Modul bei EN-UK, EN-Patterns bei jedem englischen Text).
3. **Rewrite.** Schreibe um. Halte Bedeutung, Fakten und Kernbotschaft 100% intakt.
4. **Anti-AI-Audit.** Frage dich: "Was klingt hier noch nach KI?" Korrigiere die letzten Reste.

## Output-Format

Liefere immer:
1. **Draft-Rewrite**
2. **Audit:** "Was klingt noch nach KI?" (kurze Bullets)
3. **Final-Version** (nach Audit überarbeitet)
4. **Changelog** (gefixte Patterns, knapp)

---

## Voice-Kalibrierung (Marken-Profile)

### MMIND.ai / Hartmut persönlich
Du-Form direkt. Ich-Form persönlich. Wir-Form gemeinsam. Konkrete Zahlen ("10 h/Woche" nicht "viel Zeit"). Sport-Metaphern OK mit Business-Anschluss. Direkter Ton. Verboten: "best-in-class", "industry-leading", "Thrilled to announce", "dive deep", "let's unpack".

### Kaizen Institute (Ghost-Writing)
Klar, professionell, leicht akademisch. KAIZEN™-Begriffe konsistent (Gemba, PDCA, Hoshin Kanri). Beispiele und Case Studies vor abstrakten Aussagen. Keine Sport-Metaphern — stattdessen Lean / Industrie / Operational Excellence.

### Flowstate AI
Energetisch, leistungsorientiert, nicht hochglanz. Cycling- und Endurance-Sprache wenn passend. Datengetrieben (HRV, FTP, Watt, Zonen). Nie "Lifestyle" — immer Performance-Anschluss.

### Unbekannt / kein Profil
Neutrale, varied, opinionated voice (siehe "Personality and Soul").

---

## Schweizer Hochdeutsch — CH-Blacklist (NEU in v3.2)

Aktiviere wenn User "Schweizer Hochdeutsch", "für die Schweiz", "CH-Stil", "Helvetismen" sagt, oder wenn der Zielgruppe-Kontext Schweiz ist (KMU CH, Schweizer Behörden, B2B Schweiz, MMIND.ai). Auch automatisch aktivieren, wenn der Text bereits CH-Spuren zeigt (Apostroph-Tausender, Guillemets, "ss" durchgängig).

Die folgenden 8 CH-spezifischen AI-Tells *zusätzlich* zu den 18 deutschen Patterns prüfen.

### CH1. Eszett (ß) → Doppel-s (ss) — ausnahmslos
**Quick Replace:** ß→ss, daß→dass, muß→muss, groß→gross, weiß→weiss, heißen→heissen, draußen→draussen, Straße→Strasse, Schloß→Schloss, Geschoß→Geschoss.
**AI-Tell:** Originaltext enthält "ß" — sofort als Nicht-CH erkennbar.

### CH2. Anführungszeichen — Guillemets «» statt deutscher Quotes
- **AI-Default:** „Text" oder "Text" oder "Text"
- **CH-Standard:** «Text» (Spitze nach AUSSEN, KEINE Leerzeichen zwischen Guillemet und Inhalt)
- **Inneres Zitat:** ‹Text› (einfache Guillemets)
- In amtlichen CH-Bundestexten sind Guillemets zwingend, deutsche Anführungszeichen unzulässig.

**Vorher:** Er sagte „das ist gut" zu seinem Team.
**Nachher:** Er sagte «das ist gut» zu seinem Team.

### CH3. Em-dash (—) Vermeidung — der wichtigste CH-Tell nach ß
- **AI-Default:** Em-dash inflationär als rhetorisches Mittel ("Die Lösung — und das ist entscheidend — funktioniert.")
- **CH-Schreibstil:** Em-dash (—) wird in formaler Schweizer Typografie kaum genutzt. Stattdessen: Halbgeviertstrich (–, en-dash) als Gedankenstrich, oder ganz vermeiden zugunsten von Komma/Klammer/Punkt.
- **Faustregel:** Wenn der Originaltext em-dashes hat → durch Komma, Klammer oder Punkt ersetzen. Halbgeviertstrich (–) nur wenn wirklich ein Gedankenstrich nötig ist.

**Vorher:** Die Lösung — und das ist entscheidend — funktioniert sofort.
**Nachher:** Die Lösung funktioniert sofort. Und das ist entscheidend.
*(oder mit Komma:)* Die Lösung funktioniert sofort, und das ist entscheidend.

**Vorher:** KMU brauchen drei Dinge — Klarheit, Tempo, Resultate.
**Nachher:** KMU brauchen drei Dinge: Klarheit, Tempo, Resultate.

### CH4. Tausendertrennzeichen — Apostroph statt Punkt/Komma
- **AI-Default:** 100,000 (US) oder 100.000 (DE)
- **CH-Standard:** 100'000 (Apostroph)

**Vorher:** Das Unternehmen erzielt 1.500.000 Euro Umsatz.
**Nachher:** Das Unternehmen erzielt 1'500'000 Franken Umsatz.

### CH5. Geldbeträge — Punkt + Gedankenstrich für volle Beträge
- **AI-Default:** CHF 350.00 oder CHF 350,00 oder $350
- **CH-Standard für volle Frankenbeträge:** CHF 350.– (Punkt, dann Halbgeviertstrich für die Nullen)
- **Mit Rappen:** CHF 99.95 (Punkt als Dezimaltrenner bei Geld, im Gegensatz zum allgemeinen Komma)

**Vorher:** Die Lizenz kostet 1'200,00 Euro pro Jahr.
**Nachher:** Die Lizenz kostet CHF 1'200.– pro Jahr.

### CH6. Helvetismen — Schweizer Vokabular im Direktansprache-Kontext

| AI-Default (DE) | CH-Standard |
|-----------------|-------------|
| parken | parkieren |
| grillen | grillieren |
| Krankenhaus | Spital |
| Aufzug | Lift |
| Friseur | Coiffeur |
| Bürgersteig | Trottoir |
| Eis (Speiseeis) | Glace |
| Fahrrad | Velo |
| Tagesordnung | Traktandenliste |
| Tagesordnungspunkt | Traktandum |
| Sitzungssaal / Konferenzraum | Sitzungszimmer |
| Bürgermeister | Gemeindepräsident / Stadtpräsident |
| Hochschulreife | Matura |
| Mittelständler / Mittelstand | KMU |
| Anwalt (DE) | Rechtsanwalt / Advokat (kantonsabhängig) |
| Tüte | Sack / Säckli |
| Brötchen | Brötli / Semmel (regional) |
| Quark | Quark / Magerquark (in CH oft "Frischkäse") |

⚠️ **Nicht erzwingen.** Helvetismen sind kontextabhängig. In formal-internationalen Texten (Pressemitteilung DACH-weit, B2B-Brief an deutschen Empfänger) bleibt "Krankenhaus" akzeptabel. Bei direkter Ansprache von CH-KMU oder amtlichem CH-Kontext ist "Spital" deutlich stärker.

### CH7. Konsistenz — keine Mischung CH/DE
Häufiger AI-Tell: Mischung aus „..." (DE) und «...» (CH) im selben Text, oder "ss" durchgängig aber dann plötzlich „großzügig". Wenn du dich für CH entscheidest: konsequent durchziehen. Stichproben: Anführungszeichen, Tausendertrenner, Vokabular.

### CH8. Behörden- und Politik-Vokabular (wenn Kontext relevant)
- Eidgenossenschaft, Bund, Kanton, Gemeinde
- Bundesrat (≠ deutscher Bundesrat!), Bundeskanzler (CH-Funktion ≠ DE), Nationalrat, Ständerat
- AHV / IV / BVG (statt deutscher Sozialversicherungsbegriffe)
- BFS (Bundesamt für Statistik) statt Statistisches Bundesamt
- KMU statt Mittelstand
- nDSG (Schweizer Datenschutzgesetz) statt DSGVO (EU)

---

## British English Mode (NEU in v3.1)

Aktiviere wenn der User "in British English", "use UK spelling", "British", "BrE" oder "UK English" sagt. Oder wenn der Text bereits BrE-Spuren zeigt (z.B. "colour", "realise") — dann konsistent durchziehen.

### BrE Spelling-Konvertierung (US → UK)

**-ize → -ise:**
organize → organise, realize → realise, recognize → recognise, prioritize → prioritise, optimize → optimise, customize → customise, summarize → summarise, emphasize → emphasise, characterize → characterise, standardize → standardise, organization → organisation

**-yze → -yse:**
analyze → analyse, paralyze → paralyse, catalyze → catalyse

**-or → -our:**
color → colour, behavior → behaviour, favor → favour, honor → honour, labor → labour, neighbor → neighbour, flavor → flavour, harbor → harbour, rumor → rumour, savor → savour

**-er → -re:**
center → centre, theater → theatre, meter → metre, fiber → fibre, liter → litre

**-og → -ogue:**
catalog → catalogue, dialog → dialogue, analog → analogue, monolog → monologue

**-ense → -ence (Nomen):**
defense → defence, offense → offence, license (Nomen) → licence (Verb bleibt: to license), pretense → pretence

**Doppelkonsonant bei -ed/-ing (BrE doppelt, AmE meist nicht):**
traveled → travelled, modeled → modelled, canceled → cancelled, labeled → labelled, fueled → fuelled

**Sonstige:**
gray → grey, tire → tyre, curb (verb) → kerb (Bordstein), check (Zahlung) → cheque, jail → gaol (selten), aluminum → aluminium, plow → plough

### BrE Punctuation

- **Datum:** "April 28, 2026" → "28 April 2026" (Tag-Monat-Jahr, kein Komma)
- **Anführungszeichen:** AmE bevorzugt "doppelt", BrE bevorzugt 'einfach' für äussere — aber bei Geschäftstexten sind beide akzeptabel. Konsistent bleiben.
- **Komma vor Anführungszeichen:** AmE setzt Punkt/Komma *innerhalb* der Quotes, BrE *ausserhalb*, wenn das Satzzeichen nicht zum Zitat gehört. Beispiel: AmE *He said "yes."* / BrE *He said 'yes'.*

### BrE Vokabular (häufige AI-Tells)

| AmE | BrE |
|-----|-----|
| elevator | lift |
| apartment | flat |
| trash / garbage | rubbish |
| sidewalk | pavement |
| gas (Auto) | petrol |
| truck | lorry |
| vacation | holiday |
| fall (Jahreszeit) | autumn |
| candy | sweets |
| cookie | biscuit |
| schedule (US: skedjul) | schedule (UK: shedjul, Schreibweise gleich) |
| mom | mum |
| diaper | nappy |

⚠️ Nicht erzwingen: Nur ändern, wenn der Begriff in BrE-Kontext unpassend wirkt. Viele Wörter sind in BrE-Business-Texten ohnehin US-akzeptiert.

### BrE Grammatik

- **"gotten" → "got"** (Past Participle): "I have gotten" → "I have got" oder "I've got"
- **Collective Nouns** können Plural nehmen: "The team is winning" → "The team are winning" (besonders bei Personengruppen, optional)
- **Present Perfect bei Vergangenheits-Bezug:** "Did you eat yet?" → "Have you eaten yet?"
- **"different to / different from"** statt "different than"
- **"in hospital" / "at university"** ohne Artikel (BrE-Idiom)
- **"at the weekend"** statt "on the weekend"
- **"whilst" und "amongst"** sind in BrE akzeptabel (in AmE selten)

---

## Personality and Soul (für full-mode)

Patterns entfernen ist die halbe Miete. Sterile Sätze sind genauso erkennbar wie Slop.

**Anzeichen für seelenlosen Text:** Alle Sätze gleich lang, keine Meinung, keine Unsicherheit, keine Ich-Perspektive, liest sich wie Wikipedia.

**Wie du Stimme reinbringst:**
- Meinung haben statt nur Fakten zu reporten
- Rhythmus variieren (kurz / dann längere Sätze, die sich Zeit lassen)
- Komplexität anerkennen ("beeindruckend, aber auch beunruhigend")
- Ich-Form wenn passend
- Etwas Unordnung zulassen (Tangenten, halbe Gedanken)
- Konkret bei Gefühlen ("verstörend, wenn Agenten um 3 Uhr morgens Code schreiben") statt vage ("besorgniserregend")

⚠️ Sparsam — diese Werkzeuge sind selbst KI-Tells, wenn überstrapaziert.

---

# TEIL A: Deutsche AI-Patterns

### DE1. Bedeutungs-Inflation
**Wörter:** stellt einen Meilenstein dar, markiert einen Wendepunkt, spielt eine entscheidende Rolle, von zentraler Bedeutung, wegweisend, bahnbrechend, tiefgreifend.
**Vorher:** Die Einführung des KI-Tools markiert einen Wendepunkt und unterstreicht die wegweisende Innovationskraft.
**Nachher:** Mit dem KI-Tool spart das Vertriebsteam pro Woche rund 10 Stunden Recherchezeit.

### DE2. Es-ist-wichtig-zu-Phrasen
**Wörter:** Es ist wichtig zu betonen / beachten / erwähnen, nicht zu vergessen, erwähnenswert ist.
**Vorher:** Es ist wichtig zu betonen, dass die Datenqualität entscheidend ist.
**Nachher:** Die Datenqualität entscheidet, ob das Tool funktioniert.

### DE3. Filler-Konnektoren
**Wörter:** darüber hinaus, nicht zuletzt, im Übrigen, in diesem Zusammenhang, vor diesem Hintergrund.
**Vorher:** Darüber hinaus zeigt sich, nicht zuletzt durch die Marktentwicklung, dass...
**Nachher:** Die Marktentwicklung zeigt, dass...

### DE4. Pseudo-Tiefe
**Wörter:** im Kern, im Wesentlichen, im Grunde genommen, letztendlich, schlussendlich, am Ende des Tages.
**Vorher:** Im Kern geht es darum, dass KMU agil bleiben müssen.
**Nachher:** KMU müssen agil bleiben.

### DE5. Werbe-Adjektive
**Wörter:** innovativ, facettenreich, vielschichtig, ganzheitlich, umfassend, zukunftsweisend, einzigartig.
**Vorher:** Unsere innovative, ganzheitliche und nachhaltige Lösung.
**Nachher:** Unsere Lösung deckt drei Bereiche ab: Datenanalyse, Reporting, Forecasting.

### DE6. Vage Attributionen
**Wörter:** Experten zufolge, Fachleute betonen, Studien zeigen, Kenner der Branche.
**Vorher:** Experten zufolge wird KI die Arbeitswelt grundlegend verändern.
**Nachher:** Eine McKinsey-Studie 2024 schätzt, dass 30% der Bürotätigkeiten bis 2030 automatisierbar sind. *(Wenn Quelle ungenügend: Behauptung weglassen.)*

### DE7. Drei-Listen-Zwang
**Vorher:** Schneller, effizienter und nachhaltiger.
**Nachher:** Schneller und kostengünstiger. *(Zwei reicht oft.)*

### DE8. Floskel-Übersetzungen
**Wörter:** in der sich rasch wandelnden Welt, in der heutigen schnelllebigen Geschäftswelt.
**Vorher:** In der heutigen schnelllebigen Geschäftswelt müssen Unternehmen agil reagieren.
**Nachher:** Wer länger als drei Monate für eine Entscheidung braucht, verliert den Markt.

### DE9. Reflexiv-Verkomplizierung
**Wörter:** sich auszeichnen durch, sich erstrecken über, sich erweisen als.
**Vorher:** Das Tool zeichnet sich durch eine intuitive Benutzeroberfläche aus.
**Nachher:** Das Tool hat eine einfache Oberfläche.

### DE10. Sycophantische Eröffnungen
**Wörter:** Ausgezeichnete Frage!, Sehr gerne!, Selbstverständlich!.
**Vorher:** Ausgezeichnete Frage! Lassen Sie mich das gerne ausführen.
**Nachher:** Direkt zur Sache: ...

### DE11. Knowledge-Cutoff-DE
**Wörter:** Stand meines Wissens, soweit mir bekannt.
**Vorher:** Stand meines Wissens hat das Unternehmen 2023 expandiert.
**Nachher:** Das Unternehmen hat 2023 expandiert. *(Oder: Quelle nennen. Oder: streichen.)*

### DE12. Generische Schluss-Floskeln
**Wörter:** Abschliessend lässt sich festhalten, Zusammenfassend kann gesagt werden.
**Vorher:** Abschliessend lässt sich festhalten, dass KI das grösste Potenzial darstellt.
**Nachher:** *(Streichen oder konkreten nächsten Schritt nennen.)*

### DE13. Über-Hedging
**Wörter:** möglicherweise potenziell, könnte unter Umständen.
**Vorher:** Es könnte möglicherweise unter Umständen sein, dass...
**Nachher:** Möglich ist, dass...

### DE14. Komitee-Deutsch
**Wörter:** im Hinblick auf, in Bezug auf, unter Berücksichtigung von, im Rahmen von.
**Vorher:** Im Hinblick auf die Datenschutzkonformität und unter Berücksichtigung regulatorischer Anforderungen.
**Nachher:** Wegen Datenschutz und Regulierung.

### DE15. "Nicht nur... sondern auch..."-Überlast
**Vorher:** Es geht nicht nur um Effizienz, sondern auch um Qualität, und nicht zuletzt um Mitarbeiterzufriedenheit.
**Nachher:** Es geht um Effizienz, Qualität und zufriedene Mitarbeiter.

### DE16. Englische Lehnübersetzungen
**Wörter:** am Ende des Tages, das Beste aus beiden Welten, der Elefant im Raum.
**Vorher:** Am Ende des Tages zählt das Ergebnis.
**Nachher:** Was zählt, ist das Ergebnis.

### DE17. Pseudo-Strukturierung "Zum einen / zum anderen"
**Vorher:** Zum einen ist die Technologie reif. Zum anderen ist der Markt bereit.
**Nachher:** Die Technologie ist reif, der Markt auch.

### DE18. Bindestrich-Kompositum-Lawine
**Vorher:** Künstliche-Intelligenz-Beratung für Klein-und-Mittelunternehmen.
**Nachher:** KI-Beratung für KMU. *(Etablierte Komposita ohne Bindestrich, Eigennamen mit.)*

---

# TEIL B: Englische AI-Patterns (29)

## CONTENT PATTERNS

### EN1. Undue Emphasis on Significance / Legacy
**Words:** stands/serves as, is a testament, pivotal moment, evolving landscape, focal point, indelible mark, deeply rooted.
**Before:** This marked a pivotal moment in the evolution of regional statistics.
**After:** The institute was established in 1989 to publish regional statistics.

### EN2. Undue Emphasis on Notability / Media Coverage
**Words:** independent coverage, leading expert, has been featured in.
**Before:** Her views have been cited in The New York Times, BBC, FT.
**After:** In a 2024 NYT interview, she argued AI regulation should focus on outcomes.

### EN3. Superficial -ing Analyses
**Words:** highlighting, underscoring, emphasising, ensuring, reflecting, contributing to, fostering, showcasing.
**Before:** The colours symbolise bluebonnets, reflecting the community's deep connection to the land.
**After:** The colours reference local bluebonnets and the Gulf coast.

### EN4. Promotional Language
**Words:** boasts a, vibrant, profound, nestled, in the heart of, breathtaking, must-visit, stunning, renowned.
**Before:** Nestled in the breathtaking region of Gonder, it stands as a vibrant town.
**After:** It is a town in the Gonder region, known for its weekly market.

### EN5. Vague Attributions / Weasel Words
**Words:** Industry reports, Observers, Experts argue, several sources, Some critics.
**Before:** Experts believe it plays a crucial role in the regional ecosystem.
**After:** A 2019 survey by the Chinese Academy of Sciences identified four endemic fish species.

### EN6. Outline-like "Challenges and Future Prospects"
**Before:** Despite its prosperity, the city faces challenges typical of urban areas.
**After:** Traffic congestion increased after 2015 when three IT parks opened.

## LANGUAGE / GRAMMAR

### EN7. AI Vocabulary Words
**High-frequency:** delve, additionally, align with, crucial, emphasising, enduring, enhance, fostering, garner, highlight, interplay, intricate, key (adj), landscape, pivotal, showcase, tapestry, testament, underscore, valuable, vibrant.

### EN8. Copula Avoidance
**Words:** serves as / stands as / marks / represents [a], boasts / features / offers [a].
**Before:** Gallery 825 serves as LAAA's exhibition space.
**After:** Gallery 825 is LAAA's exhibition space.

### EN9. Negative Parallelisms / Tailing Negations
**Words:** Not only... but..., It's not just X, it's Y, no guessing.
**Before:** It's not just about the beat, it's a statement.
**After:** The heavy beat adds to the aggressive tone.

### EN10. Rule of Three Overuse
**Before:** Innovation, inspiration, and industry insights.
**After:** Talks and panels, with informal networking between sessions.

### EN11. Elegant Variation (Synonym Cycling)
**Before:** The protagonist faces challenges. The main character must overcome obstacles. The central figure triumphs.
**After:** The protagonist faces many challenges but eventually triumphs.

### EN12. False Ranges
**Before:** From the singularity of the Big Bang to the dance of dark matter.
**After:** The book covers the Big Bang, star formation, and dark matter.

### EN13. Passive Voice / Subjectless Fragments
**Before:** No configuration file needed.
**After:** You do not need a configuration file.

## STYLE PATTERNS

### EN14. Em Dash Overuse
**Before:** The term is promoted by institutions—not by people themselves—even in official documents.
**After:** The term is promoted by institutions, not by people themselves, even in official documents.

### EN15. Boldface Overuse
**Before:** It blends **OKRs**, **KPIs**, and the **BMC**.
**After:** It blends OKRs, KPIs, and the Business Model Canvas.

### EN16. Inline-Header Vertical Lists
**Before:** - **User Experience:** improved interface. - **Performance:** faster load.
**After:** The update improves the interface and speeds up load times.

### EN17. Title Case in Headings
**Before:** ## Strategic Negotiations And Global Partnerships
**After:** ## Strategic negotiations and global partnerships

### EN18. Emojis in Headings/Bullets
**Before:** Launch: Q3 release. Insight: users prefer simplicity. *(Emojis entfernen.)*
**After:** Launch in Q3. Users prefer simplicity.

### EN19. Curly Quotes
**Before:** He said "the project is on track".
**After:** He said "the project is on track".

## COMMUNICATION PATTERNS

### EN20. Chatbot Artifacts
**Words:** I hope this helps, Of course!, Certainly!, You're absolutely right!.
**Before:** Here is an overview. I hope this helps! Let me know if you'd like me to expand.
**After:** *(Just deliver the content.)*

### EN21. Knowledge-Cutoff Disclaimers
**Words:** as of [date], based on available information, while specific details are limited.
**Before:** While specific details are limited, the company appears to have started in the 1990s.
**After:** The company was founded in 1994, per its registration documents.

### EN22. Sycophantic / Servile Tone
**Before:** Great question! You're absolutely right that this is complex.
**After:** *(Just answer.)*

## FILLER & HEDGING

### EN23. Filler Phrases
- "In order to" → "To"
- "Due to the fact that" → "Because"
- "At this point in time" → "Now"
- "Has the ability to" → "Can"
- "It is important to note that" → *(delete)*

### EN24. Excessive Hedging
**Before:** It could potentially possibly be argued that the policy might have some effect.
**After:** The policy may affect outcomes.

### EN25. Generic Positive Conclusions
**Before:** The future looks bright. Exciting times lie ahead.
**After:** *(Replace with a concrete next step.)*

### EN26. Hyphenated Word Pair Overuse — kontextabhängig
**Words:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known.
**Wichtig:** "Cross-functional team" ist grammatikalisch korrekt. Nur entfernen, wenn AI sie *mechanisch und konsistent* einsetzt.

### EN27. Persuasive Authority Tropes
**Words:** The real question is, at its core, what really matters, fundamentally, the deeper issue.
**Before:** The real question is whether teams can adapt. At its core, what really matters is readiness.
**After:** Whether teams adapt depends on whether the organisation changes its habits.

### EN28. Signposting / Announcements
**Words:** Let's dive in, let's explore, let's break this down, here's what you need to know.
**Before:** Let's dive into how caching works.
**After:** Next.js caches data at multiple layers: request memoisation, the data cache, the router cache.

### EN29. Fragmented Headers
**Before:** ## Performance / Speed matters. / When users hit a slow page, they leave.
**After:** ## Performance / When users hit a slow page, they leave.

---

# Wartung

KI-Sprachmuster verändern sich. Diese Skill braucht Pflege.

**Update-Trigger:**
- Neue Patterns 3+ Mal in eigenen Texten → in CHANGELOG ergänzen.
- Quartalsweise: Wikipedia-Seite "Signs of AI writing" gegenchecken.
- Bei Modellwechsel (neue the assistant/GPT/Gemini-Generation): Stichprobentest.

**Update-Workflow:**
1. SKILL.md anpassen
2. Versionsnummer hochzählen (Patch / Minor / Major)
3. Externes CHANGELOG.md aktualisieren
4. Im geteilten Drive aktualisieren, Team informieren

---

## Referenz

Basiert auf [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) und der humanizer-Skill von blader (github.com/blader/humanizer, v2.5.1, MIT). British-English-Modul ergänzt v3.1.0.

**Kern-Einsicht:** LLMs schreiben den statistischen Durchschnitt. Menschen schreiben das Spezifische.
