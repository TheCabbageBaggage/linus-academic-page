## Essay 1 — The Agentic Industrial Enterprise

Eine Fabrik wird nicht agentisch, weil sie einen Chatbot installiert. Sie wird es, sobald ein Softwaresystem verändert, wer ein Problem bemerkt, wer Handlungsoptionen vorbereitet und wer handeln darf. Die entscheidende Frage folgt erst danach: Wer verantwortet das Ergebnis, wenn die Empfehlung falsch war?

Man stelle sich eine Wartungswarnung am Freitagmittag vor. Ein Agent findet vergleichbare Störungen, prüft Ersatzteile und schlägt einen Eingriff am Wochenende vor. Technisch beeindruckend. Organisatorisch ungeklärt: Die Produktion braucht die Anlage, die Instandhaltung braucht Personal, und der Kundenauftrag hat einen zugesagten Liefertermin. Eine gute Antwort löst diesen Konflikt nicht. Eine verantwortbare Entscheidung schon.

Dieses Beispiel ist illustrativ, kein Bericht über ein produktives System. Es zeigt jedoch, wo ich die eigentliche Managementaufgabe sehe: **Agents werden Teil des Operating Models, sobald sie Entscheidungsarbeit verändern; ihr Wert entsteht nicht durch ihre Anzahl, sondern durch klar verantwortete Entscheidungsschleifen.** Wer ihre Einführung allein als Softwareprogramm führt, bearbeitet deshalb nur einen Teil der Aufgabe.

### Die Entscheidung ist die richtige Einheit

In meiner Perspektive als Digitalisierungs- und IT-Verantwortlicher ist die Frage „Wo können wir Agents einsetzen?“ zu offen. Ich würde stattdessen fragen: Welche wiederkehrende Entscheidung ist heute langsam, schlecht vorbereitet oder zwischen Funktionen zerschnitten? Das führt vom Technologiekatalog zur Materialdisposition, zum Forecast-Abgleich oder zur Freigabe eines Wartungsfensters.

Der Gedanke ist nicht neu. Davenport und Short beschrieben bereits 1990, dass Informationstechnologie und Prozessgestaltung gemeinsam gedacht werden müssen. Die Forschung zu komplementären Investitionen zeigt ebenfalls, warum zusätzliche Technik ohne organisatorische Veränderungen ein unvollständiges Produktivitätsversprechen bleibt (Brynjolfsson et al., 2021). Daraus leite ich keine garantierte Agentenrendite ab. Ich leite eine Reihenfolge ab: zuerst die Arbeitslogik verstehen, dann die technische Intervention bestimmen.

Eine operative Entscheidung lässt sich in sechs Elemente zerlegen: Auslöser, Kontext, Optionen, Entscheidungsrecht, Ausführung und Rückmeldung. Bei der Wartungswarnung ist der Auslöser eine auffällige Zustandsprognose. Zum Kontext gehören Anlagenhistorie, Auftragslage, Ersatzteilverfügbarkeit und die Unsicherheit der Prognose. Optionen reichen von zusätzlicher Inspektion bis zur geplanten Unterbrechung. Erst danach folgt die Entscheidung, nicht schon mit dem ersten Warnsignal.

Die Literatur zu zustandsbasierter Instandhaltung beschreibt das Zusammenspiel von Diagnose, Prognose und Instandhaltungsentscheidungen ausführlich (Jardine et al., 2006). Für das Management ist entscheidend, die Grenzen dieser Schritte sichtbar zu halten. Eine bessere Ausfallprognose ist weder automatisch eine bessere Terminentscheidung noch bereits vermiedener Stillstand. Dazwischen liegen Kapazitätskonflikte, Kostenabwägungen und Menschen mit unterschiedlichen Zielen.

Ich würde deshalb für jeden Agenten einen Entscheidungseigentümer benennen. Nicht jemanden, der das Tool administriert, sondern eine Person mit Mandat für das betroffene Ergebnis. Sie muss erklären können, welche Entscheidung sich verändert, welche Fehler akzeptabel sind und unter welchen Bedingungen der bisherige Prozess wieder übernimmt. Fehlt diese Person, fehlt nicht bloß Governance. Es fehlt das Geschäftsmodell des Vorhabens.

### Fünf Schichten, die Verantwortung zusammenhalten

Für das agentische Unternehmen schlage ich fünf Schichten vor. Das ist ein Gestaltungsrahmen, kein empirisch validiertes Reifegradmodell. Sein Zweck ist, Lücken zwischen intelligenter Empfehlung und belastbarer Betriebswirkung aufzudecken. Jede Schicht beantwortet eine organisatorische Frage; keine rechtfertigt sich allein durch eine attraktive Systemarchitektur.

Oben stehen menschliche Rollen. Wer besitzt das Ergebnis? Wer darf widersprechen? Wer entscheidet bei widersprüchlichen Zielen? Im Wartungsbeispiel muss die Abstimmung zwischen Produktion und Instandhaltung geklärt sein, bevor ein Agent die erste Intervention vorbereitet. Ein digitaler Vorschlag darf einen bestehenden Zielkonflikt sichtbar machen, aber keine ungeklärte Zuständigkeit verdecken.

Die zweite Schicht bilden Agents mit ausdrücklich begrenzten Kompetenzen. Einer darf Befunde zusammenstellen, ein anderer einen Auftragsentwurf vorbereiten. Daraus folgt nicht, dass beide Produktionsaufträge ändern dürfen. Ich behandle diese Grenzen wie delegierte Arbeitsaufträge: mit einem Zweck, zulässigen Informationsquellen, erlaubten Aktionen und einer Eskalationsregel. Ein gemeinsames Sprachmodell begründet noch kein gemeinsames Mandat.

Die dritte Schicht ist der überprüfbare Kontext. Eine Empfehlung braucht die richtige Anlage, den aktuellen Umbauzustand und die passende Dokumentversion. Knowledge Graphs können Beziehungen zwischen solchen Objekten explizit machen; sie sind aber kein obligatorischer Bestandteil jeder Lösung (Hogan et al., 2021). Für eine eng begrenzte Entscheidung kann eine sauber gepflegte Tabelle nützlicher sein als eine ambitionierte Wissensplattform ohne Verantwortliche.

Die vierte Schicht umfasst die betrieblichen Systeme: ERP, MES, Instandhaltungsmanagement und gegebenenfalls die Schnittstellen zur Betriebstechnik. Hier wird aus Sprache eine Transaktion. Berechtigungen, technische Prüfungen und Protokollierung müssen unabhängig davon funktionieren, wie überzeugend ein Agent argumentiert. NIST betont für Operational Technology die besonderen Anforderungen an Sicherheit, Zuverlässigkeit und Verfügbarkeit (Stouffer et al., 2023). Ein Sprachmodell darf diese Anforderungen nicht neu auslegen.

Die fünfte Schicht schließt den Kreis: Ergebnis und Feedback. Wurde die Empfehlung übernommen? Was wurde tatsächlich ausgeführt? Welche Wirkung trat ein, und welche Annahme war falsch? Ohne diese Rückmeldung bleibt unklar, ob das System hilft oder lediglich plausibel klingt. Dabei bedeutet Lernen zunächst eine kontrollierte Prozessverbesserung, nicht die automatische Veränderung produktiver Regeln nach jedem einzelnen Ereignis.

### Autonomie ist eine Variable, kein Fortschrittsmaß

Ich halte „möglichst autonom“ für ein schlechtes Unternehmensziel. Informationsbeschaffung, Empfehlung, vorbereitete Transaktion, beaufsichtigte Ausführung und eng begrenzte autonome Routine sind unterschiedliche Arbeitsverteilungen. Sie bilden keine Leiter, auf der jede Organisation möglichst schnell nach oben steigen müsste. Die klassische Forschung zu Automationsstufen trennt entsprechend verschiedene Funktionen und Grade der Automatisierung (Parasuraman et al., 2000).

Meine praktische Entscheidungshilfe besteht aus drei Fragen: Ist der Eingriff reversibel? Ist sein Zustand zuverlässig beobachtbar? Wie hoch sind die Fehlerkosten? Ein automatisch angelegter Entwurf kann vertretbar sein, während die verbindliche Bestellung derselben Position eine Freigabe benötigt. Die richtige Grenze hängt am konkreten Vorgang, nicht an der Leistungsfähigkeit des Modells im allgemeinen Benchmark.

Auch ein Mensch in der Schleife ist keine hinreichende Absicherung. Bainbridge beschrieb schon 1983 die Ironie, dass Automatisierung dem Menschen ausgerechnet schwierige Überwachungs- und Ausnahmeaufgaben hinterlassen kann. Wer Empfehlungen prüfen soll, braucht deshalb Zeit, verständliche Belege und tatsächliche Eingriffsmacht. Eine Freigabeschaltfläche unter permanentem Zeitdruck organisiert möglicherweise nur die Weitergabe von Verantwortung.

Daraus folgen unbequeme Führungsentscheidungen. Wer kann einen Agenten sofort stoppen? Wer trägt die Kosten zusätzlicher Datenpflege? Welcher Ausnahmefall bleibt ausdrücklich menschlich? Und wer entscheidet, dass eine schnellere Bearbeitung den zusätzlichen Kontrollaufwand nicht rechtfertigt? Das NIST AI Risk Management Framework stellt Verantwortlichkeit, laufende Bewertung und Risikobehandlung in einen gemeinsamen Rahmen (Tabassi, 2023). Für mich gehört diese Arbeit in die operative Führung, unterstützt durch IT und Risikofunktionen.

### Ein begrenzter Test statt einer großen Ankündigung

Der naheliegende Einwand lautet: Ist das nicht einfach Workflow-Automatisierung mit neuer Sprache? Teilweise ja. Wo Regeln stabil und Eingaben strukturiert sind, würde ich klassische Automatisierung bevorzugen. Der zusätzliche Nutzen eines Agents muss sich dort zeigen, wo Kontext zusammengetragen und situationsabhängig zwischen Handlungsoptionen gearbeitet wird. ReAct demonstriert technisch die Verbindung von sprachmodellgestütztem Schlussfolgern und Aktionen; das ist jedoch noch kein Nachweis industrieller Wirtschaftlichkeit (Yao et al., 2023).

Statt ein unternehmensweites Agentenprogramm anzukündigen, würde ich einen 90-Tage-Test beauftragen. Sein Gegenstand wäre eine häufige, nicht sicherheitskritische Entscheidung: etwa die Vorbereitung interner Klärungsfälle bei fehlenden Ersatzteilinformationen. Der Agent dürfte recherchieren und einen Vorschlag dokumentieren. Bestellungen, Anlagensteuerung und verbindliche Terminänderungen blieben außerhalb seines Mandats.

In den ersten drei Wochen würde das Team den Ausgangsprozess beobachten. Wie lange dauert die Klärung? Welche Rückfragen entstehen? Wie häufig fehlen eindeutige Materialnummern? Operations und Controlling müssten gemeinsam festlegen, was eine Verbesserung wäre. Die Messung sollte den vollständigen Aufwand einschließen: Recherche, Prüfung, Korrektur und spätere Nacharbeit. Sonst erscheint eingesparte Vorbereitungszeit als Gewinn, während die Kontrolle teurer wird.

In der nächsten Phase arbeitet der Agent zunächst parallel zum bisherigen Vorgehen. Fachpersonen vergleichen seine Vorschläge mit den realen Entscheidungen, ohne dass er selbst Transaktionen auslöst. Danach kann eine begrenzte Nutzung folgen. Jede Empfehlung erhält Quellenbezug, Zeitstempel und einen nachvollziehbaren Entscheidungsausgang. Overrides werden nicht als Widerstand verbucht, sondern nach Ursache und Qualität geprüft.

Vor dem Start würde ich Abbruchbedingungen vereinbaren: nicht nachvollziehbare Quellen, unzulässige Zugriffsversuche oder eine Fehlerlast, die den vereinbarten Nutzen aufzehrt. Ein technisch gesperrter Schreibzugriff ist dabei stärker als eine bloße Anweisung im Prompt. Stoppen muss möglich sein, ohne dass die betroffene Routine arbeitsunfähig wird. Der manuelle Rückfallweg gehört zum Versuch, nicht erst zum späteren Betrieb.

Am Ende zählen weder die Zahl erzeugter Vorschläge noch begeisterte Demonstrationen. Entscheidend sind Bearbeitungszeit, richtige Erstentscheidungen, Nacharbeit und die wirtschaftliche Konsequenz. Ein einfacher Vorher-nachher-Vergleich genügt nicht für eine sichere Kausalaussage, wenn sich gleichzeitig Auftragslage oder Personalbesetzung verändern. Ich würde deshalb, wo möglich, vergleichbare Fälle gegenüberstellen und Störeinflüsse offen dokumentieren. Ein negatives Ergebnis ist ebenfalls nützlich, wenn es eine schlechte Skalierungsentscheidung verhindert.

Montagmorgen braucht es dafür kein neues Organigramm. Es braucht einen Tisch mit Prozessverantwortung, Fachwissen, IT und Controlling sowie eine schriftliche Antwort auf vier Fragen: Welche Entscheidung verändern wir? Wer verantwortet sie? Welche Handlung bleibt ausgeschlossen? Woran erkennen wir nach 90 Tagen, dass es sich lohnt? Erst dann würde ich über zusätzliche Agents und größere Reichweite sprechen.

Das agentische Industrieunternehmen entsteht nicht, wenn Software überall mitredet. Es entsteht, wenn bessere Vorbereitung, begrenzte Handlungsvollmacht und überprüfbare Ergebnisse zusammenfinden. **Die Einheit der Transformation ist nicht der Agent. Es ist die verantwortete Entscheidungsschleife.**

### Figure

FIGURE
id: fig-essay-agentic-enterprise-1
type: diagram
kind: layers
title: Fünf Schichten einer verantworteten Entscheidungsschleife
caption: Agents wirken innerhalb eines organisatorischen Systems aus Rollen, begrenzten Kompetenzen, überprüfbarem Kontext, betrieblichen Systemen und Ergebnisrückmeldung. Autonomie wird für die konkrete Entscheidung festgelegt, nicht pauschal für das Modell.
alt: Fünf übereinanderliegende Schichten verbinden menschliche Ergebnisverantwortung mit Agenten, Kontext, betrieblichen Systemen und Feedback; ein Rückpfeil führt Ergebnisse zur verantwortlichen Person zurück.
palette: acta-petroleum
source_note: Illustrativ; eigener Gestaltungsrahmen, kein empirisch validiertes Reifegradmodell.
excalidraw_hint: Acht Knoten in fünf Ebenen zeichnen: Business Owner und Eingriffsrecht; Agent und Kompetenzgrenze; überprüfbarer Kontext; ERP/MES/CMMS; Ergebnis und Feedback. Ebenen mit gerichteten Pfeilen verbinden, Feedback zum Business Owner zurückführen; Helvetica, Petroleum #2C5F7C und Deep Navy #1A3440 für Rahmen, Teal #3D8B8B für Feedback, Off-White #F5F6F7 als Hintergrund, Warning #CC9A33 für Kompetenzgrenzen.

### References

Bainbridge, L. (1983). Ironies of automation. *Automatica, 19*(6), 775–779. https://doi.org/10.1016/0005-1098(83)90046-8

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics, 13*(1), 333–372. https://doi.org/10.1257/mac.20180386

Davenport, T. H., & Short, J. E. (1990). The new industrial engineering: Information technology and business process redesign. *Sloan Management Review, 31*(4), 11–27. https://sloanreview.mit.edu/article/the-new-industrial-engineering-information-technology-and-business-process-redesign/

Hogan, A., Blomqvist, E., Cochez, M., d’Amato, C., de Melo, G., Gutierrez, C., Kirrane, S., Gayo, J. E. L., Navigli, R., Neumaier, S., Ngomo, A.-C. N., Polleres, A., Rashid, S. M., Rula, A., Schmelzeisen, L., Sequeda, J., Staab, S., & Zimmermann, A. (2021). Knowledge graphs. *ACM Computing Surveys, 54*(4), Article 71. https://doi.org/10.1145/3447772

Jardine, A. K. S., Lin, D., & Banjevic, D. (2006). A review on machinery diagnostics and prognostics implementing condition-based maintenance. *Mechanical Systems and Signal Processing, 20*(7), 1483–1510. https://doi.org/10.1016/j.ymssp.2005.09.012

Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics—Part A: Systems and Humans, 30*(3), 286–297. https://doi.org/10.1109/3468.844354

Stouffer, K., Pease, M., Tang, C., Zimmerman, T., Pillitteri, V., Lightman, S., Hahn, A., Saravia, S., Sherule, A., & Thompson, M. (2023). *Guide to operational technology (OT) security* (NIST SP 800-82 Rev. 3). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-82r3

Tabassi, E. (2023). *Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI 100-1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.AI.100-1

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. *International Conference on Learning Representations*. https://openreview.net/forum?id=WE_vluYUL-X
