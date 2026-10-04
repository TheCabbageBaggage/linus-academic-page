## Essay 5 — Why Industrial AI Needs Memory, Not Another Copilot

Das Handbuch weiß, wofür eine Maschine gebaut wurde. Der Wartungsbericht weiß, was im vergangenen Winter ausgetauscht wurde. Die erfahrene Mitarbeiterin weiß, warum der naheliegende Lösungsversuch damals nicht funktioniert hat. Ein Copilot, der nur das Handbuch kennt, kann ausgezeichnet formulieren. Ob er der Instandhaltung hilft, ist eine andere Frage.

Stellen wir uns eine wiederkehrende Störung an einer Fertigungslinie vor. Das ist ein Gedankenexperiment, kein Bericht aus einem unserer Werke. Ein Antrieb meldet eine Temperaturüberschreitung. Der Assistent empfiehlt, Kühlung und Lager zu prüfen. Beides klingt vernünftig. Doch seit einem Umbau gilt eine andere Sensorkonfiguration; die aktuelle Materialvariante verlangt ein verändertes Fahrprofil; der letzte Lagertausch hat das gleiche Symptom nicht beseitigt. Die eigentliche Herausforderung beginnt dort, wo die allgemeine Antwort endet.

Meine These lautet: Industrielle AI braucht vor allem ein überprüfbares Gedächtnis für Anlagen, Ereignisse und Entscheidungen — nicht noch eine Oberfläche, die vorhandene Dokumente flüssiger wiedergibt. Als Digitalisierungsverantwortlicher interessiert mich daran weniger die Eleganz der Architektur als die Frage, ob die nächste Diagnose besser wird. Ein Gedächtnis verdient seinen Namen erst, wenn Menschen seinen Inhalt einordnen, korrigieren und begründet verwenden können.

### Das Problem ist nicht fehlendes Wissen, sondern fehlender Zusammenhang

Organisationen beschäftigen sich lange vor generativer AI mit ihrem Gedächtnis. Walsh und Ungson beschrieben bereits 1991, wie Informationen aus der Vergangenheit gespeichert und für gegenwärtige Entscheidungen abgerufen werden. Ihr Ansatz hilft, eine aktuelle Verwechslung aufzulösen: Eine große Dokumentensammlung ist noch keine lernende Organisation. Entscheidend ist, welcher Teil der Vergangenheit für die jetzige Situation relevant ist.

Im gedachten Störungsfall genügt es deshalb nicht, Berichte mit ähnlichen Wörtern zu finden. Ich möchte wissen, ob sie dieselbe Anlagenkonfiguration betreffen, unter vergleichbaren Bedingungen entstanden und eine tatsächlich bestätigte Ursache enthalten. „Lager gewechselt“ beschreibt eine Maßnahme. Es beweist weder einen Lagerschaden noch die Wirksamkeit des Austauschs. Wer diese Unterschiede verwischt, macht aus einem Arbeitsprotokoll eine scheinbar gesicherte Diagnose.

Hinzu kommt Wissen, das sich nicht vollständig in Berichte übersetzen lässt. Nonaka beschreibt das Zusammenspiel von implizitem und explizitem Wissen als Grundlage organisationaler Wissensbildung (1994). Daraus leite ich keine Aufforderung ab, jede Erfahrung in ein Formular zu pressen. Ich leite eine bescheidenere Aufgabe ab: An entscheidenden Übergaben müssen Beobachtung, Interpretation und überprüftes Ergebnis unterscheidbar werden.

Für die Instandhaltung bedeutet das beispielsweise, einen vermuteten Fehler nicht automatisch als bestätigte Ursache abzulegen. Eine offene Hypothese bleibt offen, bis eine zuständige Person sie bewertet. Auch ein erfolgloser Eingriff ist wertvoll, wenn dokumentiert ist, unter welchen Bedingungen er erfolglos blieb. Ohne diese Grenze könnte der nächste Copilot gerade die häufig wiederholte Fehlannahme besonders überzeugend reproduzieren.

### Gedächtnis ist eine Verantwortungsstruktur

Unter industriellem Gedächtnis verstehe ich keine neue Datenbankkategorie. Ich meine eine verlässliche Verbindung aus Ereignis, Kontext, Entscheidung, Begründung und Ergebnis. Dazu gehören die damalige Version einer Anlage, die Herkunft einer Aussage und die Person oder Rolle, die sie fachlich verantwortet. Diese Anforderungen sind ein Gestaltungsprinzip, kein Versprechen eines bestimmten Softwareprodukts.

Für unseren Temperaturfall würde ich einen kleinen, nachvollziehbaren Verlauf verlangen: Welches Aggregat war betroffen? Welche Konfiguration war aktiv? Welche Messung löste den Eingriff aus? Welche Optionen wurden verworfen? Was geschah nach der Maßnahme? Die Antwort sollte außerdem zeigen, wo Informationen fehlen. Ein leeres Feld ist ehrlicher als eine vom Sprachmodell ergänzte Begründung.

Provenienz ist dabei keine akademische Zugabe. Das W3C-Modell PROV-O stellt Begriffe bereit, um Entitäten, Aktivitäten und beteiligte Akteure miteinander zu verbinden (Lebo et al., 2013). Für Führungskräfte ist die praktische Übersetzung einfach: Jede handlungsrelevante Aussage braucht einen Weg zurück zu ihrem Ursprung. Eine zusammengefasste Empfehlung ohne prüfbare Herkunft wäre für mich keine ausreichende Grundlage einer Wartungsfreigabe.

Auch Zeit muss ausdrücklich modelliert werden. Ein heute gültiger Wartungsstandard kann für die Bewertung einer früheren Entscheidung ungeeignet sein. Umgekehrt darf eine überholte Arbeitsanweisung nicht als aktuelle Empfehlung erscheinen. Ich würde deshalb zwischen dem Zeitpunkt des Ereignisses und dem Zeitpunkt seiner Dokumentation unterscheiden sowie Änderungen sichtbar halten. Wer nur den neuesten Text speichert, verliert die Erklärung dafür, warum eine frühere Entscheidung damals vernünftig erschien.

Das verlangt einen fachlichen Eigentümer. IT kann Zugänge, Versionierung und Verfügbarkeit bereitstellen. Ob eine Ursache bestätigt oder eine Maßnahme noch zulässig ist, muss die zuständige Betriebsfunktion entscheiden. Für personenbezogene Inhalte kommen Zweckbindung, Datenminimierung und Speicherbegrenzung hinzu, wie sie die Datenschutz-Grundverordnung verlangt (Europäisches Parlament & Rat, 2016). Ein industrielles Gedächtnis ist kein Freibrief für ein unbegrenztes Gedächtnis über Beschäftigte.

### Die Frage bestimmt die Architektur

Der naheliegende Einwand lautet: Reicht nicht Retrieval-Augmented Generation über unsere Dokumente? Für viele Fragen lautet meine Antwort ausdrücklich ja. Das von Lewis und Kollegen beschriebene RAG-Prinzip verbindet ein generatives Modell mit abgerufenen Informationen (2020). Wer eine gültige Bedienungsanleitung oder eine dokumentierte Verfahrensbeschreibung sucht, braucht nicht automatisch ein aufwendigeres System.

Anders liegt der Fall, wenn die Antwort aus mehreren Arten von Evidenz entstehen muss. „Was empfiehlt das Handbuch?“ ist eine Textfrage. „Welche Konfiguration lief während der letzten drei vergleichbaren Ereignisse?“ ist eine strukturierte Verlaufsfrage. „Welche Anlagen verwenden dasselbe Bauteil?“ ist eine Beziehungsfrage. Ich würde diese Fragen nicht allein deshalb durch dieselbe technische Methode beantworten, weil das Benutzerfenster überall gleich aussieht.

Dokumentensuche erschließt Texte. Ereignis- und Zeitreihendaten beschreiben Abläufe und Zustände. Knowledge Graphs können Beziehungen zwischen Anlagen, Komponenten, Fehlerbildern und Maßnahmen explizit darstellen; Hogan und Kollegen ordnen die hierfür verfügbaren Konzepte und Verfahren umfassend ein (2021). Harte betriebliche Grenzen gehören dagegen in überprüfbare Regeln und Freigaben. Ein Sprachmodell sollte keine verbindliche Sicherheitsbedingung aus verstreuten Textfragmenten improvisieren müssen.

Das ist kein Plädoyer für einen Graphen in jedem Werk. Eine relationale Tabelle kann für einen eng begrenzten Fall die bessere Lösung sein. Ebenso wenig beweist eine im Graphen gespeicherte Verbindung eine Ursache. Dass eine Störung nach einem Materialwechsel auftrat, rechtfertigt zunächst eine Untersuchung, nicht die Behauptung, das Material habe sie verursacht.

Auch immer größere Kontextfenster ersetzen diese Auswahl nicht. Liu und Kollegen zeigen für untersuchte Sprachmodelle und Aufgaben, dass die Position relevanter Informationen in langen Eingaben die Leistung beeinflussen kann (2024). Daraus folgt nicht, dass jedes neue Modell gleich reagiert. Für meine Architekturentscheidung folgt daraus aber: Mehr mitgelieferter Text ist kein ausreichender Nachweis besserer Entscheidungen. Ich will Relevanz, Gültigkeit und Herkunft prüfen, nicht bloß Kontextvolumen kaufen.

### Ein kleiner Lernkreis schlägt das große Wissensprogramm

Am Montagmorgen würde ich nicht mit einer unternehmensweiten Ontologie beginnen. Ich würde eine wiederkehrende, nicht sicherheitskritische Diagnoseentscheidung auswählen und die erfahrenen Beteiligten fragen: Welche fünf Informationen nutzt ihr, die heute nirgends gemeinsam auffindbar sind? Dann würde ich an abgeschlossenen Fällen prüfen, ob diese Informationen überhaupt zuverlässig rekonstruiert werden können.

Dabei erwarte ich keinen sauberen Ausgangszustand. Für den Versuch würde ich zunächst die Anlagenbezeichnungen aus Wartungsauftrag, Ersatzteilliste und Schichtbericht abgleichen. Wenn dasselbe Aggregat drei Namen trägt, ist eine eindeutige Zuordnung wichtiger als eine anspruchsvollere Suchfunktion. Unklare Identitäten werden markiert, nicht stillschweigend zusammengeführt. Dieser unspektakuläre Arbeitsschritt gehört ins Budget und in den Zeitplan.

Der erste Test braucht auch schwierige Beispiele: einen veralteten Bericht, zwei widersprüchliche Ursachenangaben und einen ähnlich klingenden Fehler an einer anderen Konfiguration. Das System sollte passende Evidenz liefern, Unterschiede erklären und bei fehlender Grundlage auf eine Empfehlung verzichten können. Der NIST AI Risk Management Framework betont die Bedeutung kontextbezogener Bewertung und fortlaufenden Risikomanagements (Tabassi, 2023). Für mich heißt das: Ein gelungener Vorführfall ist noch keine Betriebserlaubnis.

Danach beginnt die eigentliche Gedächtnisarbeit. Die Fachperson hält fest, ob sie einen Vorschlag genutzt, verändert oder verworfen hat. Nach dem Eingriff wird ergänzt, was tatsächlich beobachtet wurde. Nicht jede Ablehnung macht die Empfehlung falsch; nicht jede Annahme macht sie richtig. Deshalb braucht es regelmäßige fachliche Reviews statt eines automatischen Lernens aus bloßen Zustimmungssignalen.

Wirtschaftlich würde ich Diagnosezeit, erfolgreiche Erstbehebung und Wiederholfehler betrachten, ergänzt um falsche Empfehlungen und den Aufwand für Pflege und Prüfung. Bei seltenen Störungen wäre ich mit schnellen Erfolgsbehauptungen vorsichtig. Ein einfacher Vorher-nachher-Vergleich kann Veränderungen des Produktmixes oder der Anlagenbelastung nicht ausschließen. Die Übersicht von Jardine und Kollegen zur zustandsorientierten Instandhaltung verdeutlicht, dass Datenerfassung, Diagnose und Wartungsentscheidung zusammengehören (2006); der Nutzen liegt nicht allein im Erkennen eines Signals.

Dabei würde ich auch eine Vergleichsfrage offenhalten: Wäre derselbe Effekt mit einer besseren Übergaberoutine oder einer bereinigten Fehlerliste günstiger erreichbar? Wenn ja, ist das kein Scheitern der Digitalisierung, sondern ein vernünftiger Investitionsentscheid. Die laufenden Kosten für Datenpflege, fachliche Freigabe und Integration müssen gegen vermiedene Suchzeit und bessere Eingriffe stehen. Ich würde kein Gedächtnis finanzieren, das mehr Aufmerksamkeit verbraucht, als es dem Betrieb zurückgibt.

Vor einer Ausweitung würde ich außerdem einen einfachen Übergabetest verlangen: Kann eine Fachperson, die am ursprünglichen Fall nicht beteiligt war, die Empfehlung anhand der verfügbaren Belege prüfen? Dafür muss sie nicht jede technische Einzelheit des Systems verstehen. Sie muss erkennen können, welche Anlage gemeint ist, welche Annahmen gelten und welcher Befund noch fehlt. Gelingt das nur im Gespräch mit dem Projektteam, ist noch kein betriebliches Gedächtnis entstanden. Dann haben wir Wissen lediglich an eine neue Gruppe von Spezialisten gebunden, statt es für die nächste Schicht nutzbar zu machen.

Meine Zielvorstellung ist deshalb weder der allwissende Copilot noch ein lückenloser digitaler Zwilling der gesamten Organisation. Sie ist eine begrenzte, belastbare Fähigkeit: Für eine wichtige Entscheidung lässt sich nachvollziehen, was wir wussten, warum wir handelten und was daraus wurde. Wenn dadurch der nächste Eingriff besser begründet ist, hat AI industriellen Wert geschaffen. Nicht die eloquenteste Antwort gewinnt, sondern diejenige, die weiß, welche Vergangenheit für diesen Moment zählt.

### Figure

FIGURE
id: fig-essay-industrial-memory-1
type: diagram
kind: layers
title: Industrielles Gedächtnis als überprüfbarer Lernkreis
caption: Vier Schichten verbinden betriebliche Quellen mit einer begründeten Entscheidung. Rückmeldungen aktualisieren bestätigtes Wissen, nicht bloß die Häufigkeit einer Empfehlung.
alt: Schichtdiagramm mit Quellen, Kontext, Evidenz und Entscheidung; ein Rückkopplungspfeil führt vom beobachteten Ergebnis zur fachlichen Prüfung zurück.
palette: acta-petroleum
source_note: Illustrativ; eigene konzeptionelle Darstellung, angelehnt an Walsh und Ungson (1991), PROV-O (2013) und Hogan et al. (2021).
excalidraw_hint: Zehn Knoten in vier horizontalen Schichten: Handbücher, Ereignisse, Erfahrungsberichte; Anlagenidentität, Version und Zeitpunkt, Provenienz; relevante Evidenz, fachliche Prüfung; Entscheidung, beobachtetes Ergebnis. Aufwärtspfeile verbinden die Schichten, ein Rückkopplungspfeil führt vom Ergebnis zur fachlichen Prüfung; ausschließlich Petroleum #2C5F7C, Deep Navy #1A3440, Teal #3D8B8B, Slate #8A9BA8, Charcoal #2D3436 und Off-White #F5F6F7 verwenden, Schrift Helvetica.

### References

Europäisches Parlament & Rat der Europäischen Union. (2016). Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung). *Amtsblatt der Europäischen Union, L 119*, 1–88. https://eur-lex.europa.eu/eli/reg/2016/679/oj

Hogan, A., Blomqvist, E., Cochez, M., d’Amato, C., de Melo, G., Gutierrez, C., Kirrane, S., Gayo, J. E. L., Navigli, R., Neumaier, S., Ngonga Ngomo, A.-C., Polleres, A., Rashid, S. M., Rula, A., Schmelzeisen, L., Sequeda, J., Staab, S., & Zimmermann, A. (2021). Knowledge graphs. *ACM Computing Surveys, 54*(4), Article 71. https://doi.org/10.1145/3447772

Jardine, A. K. S., Lin, D., & Banjevic, D. (2006). A review on machinery diagnostics and prognostics implementing condition-based maintenance. *Mechanical Systems and Signal Processing, 20*(7), 1483–1510. https://doi.org/10.1016/j.ymssp.2005.09.012

Lebo, T., Sahoo, S., & McGuinness, D. (Eds.). (2013). *PROV-O: The PROV ontology*. W3C Recommendation. https://www.w3.org/TR/prov-o/

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-t., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems, 33*, 9459–9474. https://arxiv.org/abs/2005.11401

Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the middle: How language models use long contexts. *Transactions of the Association for Computational Linguistics, 12*, 157–173. https://doi.org/10.1162/tacl_a_00638

Nonaka, I. (1994). A dynamic theory of organizational knowledge creation. *Organization Science, 5*(1), 14–37. https://doi.org/10.1287/orsc.5.1.14

Tabassi, E. (2023). *Artificial intelligence risk management framework (AI RMF 1.0)* (NIST AI 100-1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.AI.100-1

Walsh, J. P., & Ungson, G. R. (1991). Organizational memory. *Academy of Management Review, 16*(1), 57–91. https://doi.org/10.5465/amr.1991.4278992
