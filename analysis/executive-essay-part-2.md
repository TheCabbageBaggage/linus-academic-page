## Essay 2 — Everyone Can Build Software. What Is Corporate IT For?

Freitagnachmittag baut eine Produktionsplanerin mit einem AI-Werkzeug eine kleine Anwendung. Sie liest Auftragslisten ein, markiert Terminrisiken und erzeugt einen Vorschlag für die nächste Planungsrunde. Am Montag wollen drei Kollegen sie ebenfalls nutzen. Jetzt fehlen nicht zusätzliche Funktionen, sondern Antworten: Welche Aufträge darf wer sehen? Was bedeutet eine rote Markierung? Wer hilft, wenn der Import vor der Frühbesprechung ausfällt?

Diese Szene ist illustrativ, kein Bericht aus meinem Unternehmen. Sie beschreibt aber die Managementfrage, die ich für entscheidend halte: Was soll Corporate IT leisten, wenn eine Fachfunktion bereits mit funktionierender Software statt mit einer Anforderung vor der Tür steht?

Meine These: IT muss nicht länger jede Lösung selbst bauen, sondern einen schnellen, wirtschaftlich tragfähigen Weg von lokaler Problemlösung zu verantwortbarem Betrieb organisieren. Das ist keine kleinere Aufgabe. Es ist eine andere Vereinbarung zwischen Geschäftsverantwortlichen und IT.

### Code ist nicht dasselbe wie Lieferfähigkeit

Die Überschrift ist bewusst zugespitzt. Nicht jeder kann belastbare Software entwickeln. Doch AI kann bestimmte Entwicklungsaufgaben erheblich beschleunigen: In einem kontrollierten Experiment erledigten Entwickler mit GitHub Copilot eine abgegrenzte Programmieraufgabe um 55,8 Prozent schneller als die Vergleichsgruppe (Peng et al., 2023). Daraus folgt weder, dass Fachanwender ohne Unterstützung Produktionssysteme beherrschen, noch dass die gesamten Lebenszykluskosten entsprechend sinken.

Ein anderes Experiment zeigt, warum diese Einschränkung wichtig ist. Erfahrene Open-Source-Entwickler benötigten mit den untersuchten AI-Werkzeugen von Anfang 2025 für Aufgaben in vertrauten Projekten 19 Prozent länger, obwohl sie sich beschleunigt fühlten (Becker et al., 2025). Die Ergebnisse widersprechen sich nicht zwangsläufig: Eine isolierte Aufgabe und die Änderung eines gewachsenen Systems stellen unterschiedliche Anforderungen. Beide Studien untersuchen Entwickler, nicht industrielle Citizen Developer.

Ich würde deshalb weder eine universelle Produktivitätsrevolution budgetieren noch die Entwicklung als Spielerei abtun. Die relevante Verschiebung beginnt früher: Ein Fachbereich kann eine Idee als ausführbares Artefakt diskutieren. Die Produktionsplanerin muss nicht mehr ausschließlich beschreiben, was sie meint. Sie kann zeigen, welche Information ihre Entscheidung verändern würde.

Ein linearer Ablauf aus Anforderung, Backlog, Implementierung und Übergabe sollte dafür nicht der einzige Eingang bleiben. Ebenso wenig darf eine überzeugende Oberfläche als Betriebsfreigabe gelten. Ich möchte zwei getrennte Entscheidungen sehen: Ist das Problem wertvoll genug? Und welche technische sowie organisatorische Form verdient seine Lösung?

In der illustrativen Planungsszene könnte der größte Nutzen darin liegen, einen missverständlichen Terminbegriff sichtbar zu machen. Vielleicht genügt danach eine Änderung im bestehenden Planungssystem. Die selbstgebaute Anwendung hätte dann ihren Zweck erfüllt, ohne je produktiv zu werden. IT sollte diese Entdeckung als Erfolg anerkennen, statt nur ausgelieferte Anwendungen zu zählen.

### Drei Wege statt einer Freigabemaschine

Ich schlage drei Lösungsklassen vor. Nicht als neue Bürokratie, sondern als gemeinsame Sprache für unterschiedliche Konsequenzen. Maßgeblich ist, was bei Fehlern passiert, nicht ob die Anwendung in Python, einer Low-Code-Umgebung oder per Prompt entstanden ist.

Die persönliche Arbeitshilfe unterstützt einen einzelnen Menschen, beispielsweise beim Formatieren freigegebener Testdaten. Sie verändert keine führenden Datensätze und schafft keine Abhängigkeit für andere. Dafür sollte ein leichter Pfad genügen: erlaubte Werkzeuge, klare Datengrenzen, nachvollziehbare Ablage und ein einfacher Löschweg. Personenbezogene oder vertrauliche Inhalte können allerdings schon diesen vermeintlich kleinen Fall anspruchsvoll machen.

Die teamweite Entscheidungshilfe benötigt mehr. Sobald mehrere Planer derselben Prioritätenliste vertrauen, müssen Definitionen, Aktualität und fachliche Prüfung geklärt sein. Ich würde einen namentlichen Owner, eine Vertretung und Tests gegen bekannte Fehlersituationen verlangen. Eine lesende Anwendung ist nicht automatisch harmlos: In unserem Beispiel könnte ein veralteter Vorschlag eine falsche Reihenfolge nahelegen, obwohl die Software selbst nichts im ERP schreibt.

Ein betriebsrelevantes System erfordert einen belastbaren Betriebsentscheid. Schreibt die Lösung Aufträge zurück, beeinflusst sie Kundenversprechen oder wird sie für die Produktionssteuerung unverzichtbar, sind Wiederherstellung, Zugriffsrechte, Änderungen und Support ausdrücklich zu regeln. Für sicherheitskritische Eingriffe wäre diese vereinfachte Klassifikation kein Ersatz für die zusätzlich erforderliche fachliche Sicherheitsbewertung.

Diese Klassen sind mein Gestaltungsvorschlag, kein extern zertifiziertes Modell. Ihr Nutzen liegt in der Bewegung zwischen ihnen. Wenn aus einer persönlichen Hilfe eine Teamroutine wird, muss ein neuer Entscheid ausgelöst werden. Nicht erst nach einem Vorfall, sondern sobald Nutzung, Datenzugriff oder Abhängigkeit wachsen.

Auch die Finanzierung sollte mitwandern. Einen kleinen Versuch kann die Fachfunktion aus ihrem Verbesserungsbudget tragen. Für den dauerhaften Betrieb braucht sie eine transparente Gesamtrechnung einschließlich Betreuung, Plattformverbrauch und Ablösung. Andernfalls wird der Prototyp als billig gefeiert, während seine Folgekosten still im IT-Budget landen. Ich würde die Nutzung deshalb nicht nur freigeben, sondern für einen benannten Zeitraum finanzieren und anschließend anhand der Wirkung erneut entscheiden.

### Die Plattform muss Arbeit abnehmen

Was bleibt für Corporate IT? Zunächst die gemeinsame technische Grundlage, die eine Fachfunktion nicht bei jeder Idee neu erfinden sollte: Identität, Datenzugriff, freigegebene Entwicklungsumgebungen, Integrationsschnittstellen und ein verlässlicher Weg zur Bereitstellung. Plattformfähigkeit heißt für mich nicht, einen Werkzeugkatalog zu veröffentlichen. Sie heißt, wiederkehrende schwierige Entscheidungen in brauchbare Voreinstellungen zu übersetzen.

Beim Zugriff ist die Zugehörigkeit zum Unternehmensnetz kein ausreichendes Vertrauensargument. Die Zero-Trust-Architektur des NIST stellt Ressourcen, Identitäten und explizite Authentifizierung sowie Autorisierung in den Mittelpunkt (Rose et al., 2020). Für die Planungsanwendung bedeutet das beispielsweise: Die Plattform vermittelt genau den benötigten lesenden Zugriff, statt ein persönliches Konto mit weitreichenden Rechten dauerhaft in ein Skript einzubauen.

Auch sichere Entwicklung darf nicht als nachträgliche Prüfung missverstanden werden. Das Secure Software Development Framework des NIST beschreibt Praktiken, die in den Entwicklungslebenszyklus integriert werden sollen (Souppaya et al., 2022). Ich würde daraus für den internen Standardweg konkrete Hilfen ableiten: Versionierung, automatisierte Tests, Prüfung von Abhängigkeiten und einen dokumentierten Umgang mit gefundenen Schwachstellen.

Die Notwendigkeit verschwindet nicht, weil Code aus einem Modell kommt. Pearce et al. (2021) zeigten in gezielt sicherheitsrelevanten Szenarien, dass ein früher Copilot verwundbaren Code erzeugen konnte. Diese Untersuchung erlaubt keine pauschale Fehlerquote für heutige Werkzeuge. Sie reicht jedoch aus, um die Annahme zurückzuweisen, generierter Code müsse allein wegen seiner Herkunft weniger geprüft werden.

Für den Alltag würde ich außerdem eine einfache Beobachtbarkeit vorsehen: Wann lief der letzte Import erfolgreich? Welche Datenversion lag einer Empfehlung zugrunde? Wer hat eine Änderung veröffentlicht? Dazu gehören ein Rücksetzweg und ein benannter Kontakt. Das sind keine dekorativen Technikmerkmale, sondern Antworten auf die Montagsfragen aus der Eingangsszene.

Datenverträge verdienen dabei besondere Aufmerksamkeit. Ein Feld namens Lieferdatum ist erst brauchbar, wenn Bedeutung, Zeitzone, Änderungslogik und verantwortliche Quelle geklärt sind. Für unsere illustrative Anwendung würde ich diese Definition zusammen mit Beispieldaten und erwarteten Ergebnissen bereitstellen. So prüft ein Test nicht bloß, ob der Import läuft, sondern ob die fachliche Bedeutung erhalten bleibt. Die Fachfunktion muss diese Bedeutung bestätigen; IT kann sie nicht aus dem Spaltennamen erraten.

Eine solche Plattform würde ich an der Zeit bis zur validierten Fachwirkung messen. Hinzu kämen Wiederherstellbarkeit, Betreuungsaufwand und die Frage, ob wertvolle Lösungen nach einem vereinbarten Zeitraum noch verantwortbar genutzt werden. Die Zahl angelegter Entwicklerkonten wäre dafür kein ausreichender Erfolgsmaßstab.

### Den Prototyp respektieren, nicht konservieren

Der schwierige Moment kommt, wenn ein nützlicher Prototyp technisch nicht tragfähig ist. Für mich ist weder „Alles neu bauen“ noch „Nichts anfassen, es funktioniert“ eine verantwortliche Standardantwort. Die Entscheidung muss Nutzen, Verzögerung, Betriebskosten und Risiko gemeinsam betrachten.

In der illustrativen Planungsszene könnte die Benutzeroberfläche gut sein, während der Datenimport auf kopierten Dateien und unklaren Felddefinitionen beruht. Dann wäre es plausibel, zunächst den Import durch eine stabile Schnittstelle zu ersetzen. Fowler beschreibt mit der Strangler-Fig-Modernisierung das Prinzip einer schrittweisen Ablösung statt eines vollständigen Austauschs auf einmal (Fowler, 2004). Ich würde dieses Prinzip prüfen, nicht mechanisch auf jeden Prototyp übertragen.

Ein Neubau wäre dagegen meine Präferenz, wenn das Artefakt nicht sinnvoll testbar ist, seine Abhängigkeiten unklar bleiben oder die notwendige Betriebsqualität nur durch fortgesetzte Sonderlösungen erreichbar wäre. Auch dann sollte die Vorarbeit erhalten bleiben: fachliche Regeln, Beispiele, akzeptierte Oberflächen und Erkenntnisse über die tatsächliche Nutzung. Die Implementierung wegzuwerfen muss nicht heißen, die Entdeckung wegzuwerfen.

Für den Entscheid würde ich einen kurzen gemeinsamen Termin verlangen, keinen monatelangen Architekturprozess. Der Business Owner erläutert die wirtschaftliche Wirkung und die Kosten des Wartens. IT legt die tragfähigen Varianten samt laufendem Aufwand dar. Security bewertet das konkrete Risiko. Ein benanntes Produktteam entscheidet über Industrialisierung, begrenzten Weiterbetrieb oder Einstellung.

Wichtig ist, wer danach verantwortlich bleibt. Die Fachfunktion besitzt Problem, Regeln und Nutzen. IT verantwortet die vereinbarten Plattform- und Betriebsstandards. Der erfolgreiche Prototyp darf kein Übergaberitual auslösen, bei dem der Fachbereich seine Verantwortung samt Notebook an IT abgibt.

### Der bessere Weg muss wirklich besser sein

Der stärkste Einwand lautet: Das ist ein freundlicher Name für Shadow IT. Diesen Einwand nehme ich ernst. Mehr lokale Entwicklungsfreiheit kann mehr unübersichtliche Abhängigkeiten schaffen; mein Vorschlag beseitigt dieses Risiko nicht durch ein Etikett. Ein zentraler Standardweg muss deshalb im konkreten Fall beweisen, dass er schneller zu einer belastbaren Entscheidung führt als das Ausweichen.

Manchmal wird dieser Entscheid „nicht bauen“ lauten. Wenn eine vorhandene Unternehmenslösung dieselbe Aufgabe ausreichend erfüllt, sollte Wiederverwendung Vorrang haben. Manchmal wird er eine zeitlich begrenzte Ausnahme enthalten. Entscheidend ist, dass Nutzen, verbleibendes Risiko, Owner und Ablaufdatum sichtbar sind. Geschwindigkeit bedeutet nicht Anspruchslosigkeit, sondern weniger ungeklärte Übergaben.

Am Montag würde ich deshalb keinen unternehmensweiten Citizen-Development-Rollout starten. Ich würde mit einer Fachbereichsleitung die letzte selbstgebaute Lösung ansehen: Welches Problem löst sie, wer nutzt sie, welche Entscheidung hängt daran, und wer trägt den Fehler? Dann ordnen wir sie einer Klasse zu und bestimmen den nächsten belastbaren Betriebsentscheid.

Anschließend messen wir die Zeit vom vorliegenden Prototyp bis zu diesem Entscheid, einschließlich Wartezeiten auf Daten, Zuständigkeiten und Prüfungen. In einem zweiten Durchlauf soll die Plattform einen dieser Engpässe beseitigen. So wird aus einer Grundsatzdebatte ein überprüfbarer Verbesserungsauftrag.

Corporate IT wird nicht dadurch unverzichtbar, dass ohne sie niemand Software bauen darf. Sie wird es, wenn aus guten lokalen Ideen verlässliche Geschäftswirkung entsteht. Dafür baut IT die Straße; für das Ziel bleibt das Geschäft verantwortlich.

### Figure

FIGURE
id: fig-essay-corporate-it-1
type: chart
kind: bar
title: Nicht nur Bauzeit messen, sondern Zeit bis zum Betriebsentscheid
caption: Rein illustrativer Vergleich für dieselbe hypothetische teamweite Entscheidungshilfe. Die Werte sind weder Studienergebnisse noch Unternehmensdaten oder Zielzusagen; sie verdeutlichen den vorgeschlagenen Messpunkt.
alt: Zwei Balken zeigen ausschließlich illustrative Durchlaufzeiten vom fertigen Prototyp bis zum belastbaren Betriebsentscheid: 20 Arbeitstage bei individueller Klärung und 8 Arbeitstage auf einem vorbereiteten Plattformpfad.
palette: acta-petroleum
data:
 - label: Individuelle Klärung ohne vorbereiteten Pfad — Arbeitstage
   value: 20
 - label: Vorbereiteter Plattformpfad — Arbeitstage
   value: 8
source_note: Illustrativ; frei gewählte didaktische Daten, keine empirische Messung. Darstellung ausschließlich in Petroleum #2C5F7C und Teal #3D8B8B, Text Charcoal #2D3436, Hintergrund Off-White #F5F6F7; Schrift Helvetica. Balkenachse beginnt bei null.
excalidraw_hint: Nicht anwendbar; Balkendiagramm mit zwei Balken und identischer Einheit.

### References

Becker, J., Rush, N., Barnes, B., & Rein, D. (2025). *Measuring the impact of early-2025 AI on experienced open-source developer productivity*. arXiv [Preprint]. https://doi.org/10.48550/arXiv.2507.09089

Fowler, M. (2004). *Strangler fig application*. MartinFowler.com [Fachessay; fortgeschriebene Onlinefassung]. https://martinfowler.com/bliki/StranglerFigApplication.html

Pearce, H., Ahmad, B., Tan, B., Dolan-Gavitt, B., & Karri, R. (2021). *Asleep at the keyboard? Assessing the security of GitHub Copilot's code contributions*. arXiv [Preprint; später veröffentlicht beim IEEE Symposium on Security and Privacy 2022]. https://doi.org/10.48550/arXiv.2108.09293

Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). *The impact of AI on developer productivity: Evidence from GitHub Copilot*. arXiv [Preprint]. https://doi.org/10.48550/arXiv.2302.06590

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207 — Verifizierte Verlagsseite: https://csrc.nist.gov/pubs/sp/800/207/final

Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure Software Development Framework (SSDF) version 1.1: Recommendations for mitigating the risk of software vulnerabilities* (NIST Special Publication 800-218). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-218 — Verifizierte Verlagsseite: https://csrc.nist.gov/pubs/sp/800/218/final
