#!/usr/bin/env python3
"""
Definitionen der 5 ACTA-Berichte für Linus' Karriere-/Paper-Analysen.
Importiert den Builder aus generate_career_reports.py und erzeugt HTML+PDF.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from generate_career_reports import (  # noqa: E402
    OUT, build_report, html_to_pdf, register_report,
)

AUTHOR = "Clowie Claw"
CLIENT = "Linus Kohl"

# ---------------------------------------------------------------------------
# R1 — Strategische Roadmap 2026–2029
# ---------------------------------------------------------------------------
R1_EXEC = """
Die zentrale strategische Aussage dieses Berichts lautet: **die Engstelle ist nicht
Kompetenz, sondern Zuschreibung.** Das Profil (PhD TU Wien, ~19 Publikationen,
Bereichsleitung Digitalisierung & IT in der Schwerindustrie, ~6 Mio. € Budget,
echte Tiefe in lokalen LLMs und Agenten-Infrastruktur) ist überdurchschnittlich.
Die aktuelle Position ist jedoch strukturell eine Stabsfunktion ohne direkte
P&L-, EBIT-, Sales- oder Supply-Chain-Nähe. Die Rotec-Absage wird nicht als
Fachurteil, sondern als Marktsignal gelesen: digitale Komplexität wird zugetraut,
operative Ergebnisverantwortung noch nicht sichtbar.

**Der strategische Fehler wäre, diese Lücke mit noch mehr intellektueller
Exzellenz im falschen Label zu beantworten.** Vier Papers zu AI Governance,
Vibe Coding und Compliance zementieren das Spezialistenprofil. Für CIO/CDO/Group
Digital nützlich, für General Management gefährlich.

**Kernbefund:** Der stärkste Karrierepfad ist nicht ein größerer Digitaltitel,
sondern Mitverantwortung für eine operative Ergebnisgröße — Forecast Accuracy,
Lieferperformance, Working Capital, Anlagenverfügbarkeit, Engineering-Durchlaufzeit.

**Harte Zielkonflikte:** Vollzeit-Bereichsleitung, sichtbarer Corporate-Kandidat,
aktiver Publizist, Ecosystem-Builder, Startup-Gründer und präsenter Vater sind
nicht gleichzeitig leistbar. Empfehlung: **2026 ist kein Startup-Jahr, sondern
ein Karriere-Repositionierungsjahr.**

**Zeitbudget-Kern:** Das „Karriere-Push"-Szenario (50 h Corporate, 4 h Thought
Leadership, max. 1 h Startup-Exploration, 3 h Sport) ist das vernünftigste
2026-Szenario. Das „Alles gleichzeitig"-Szenario (68 h) ist nicht nachhaltig.

**Drei konkrete Bewegungen 2026–2027:**
Salesforce/Forecast zur GM-Brücke machen (S&OP-/Working-Capital-Initiative statt
IT-Integration) · einen operativen Sponsor außerhalb IT gewinnen · formale
Co-Ownership-Rolle mit echten KPIs verhandeln.
"""

R1_CLOSE = """
**Klare Empfehlung.** Nicht „Corporate plus Papers plus Startup", sondern:
**2026–2027 Corporate-GM-Repositionierung als Hauptspiel, Thought Leadership
als Beweisführung, Startup nur als konfliktarmes Optionsportfolio.**

1. **Salesforce/Forecast wird der stärkste Karrierehebel** — nicht als IT-Projekt,
   sondern als S&OP-/Working-Capital-Mandat mit gemeinsamem KPI-Set
   (Forecast Accuracy, Bias, Lieferperformance, Bestandsreichweite, Working Capital).
2. **Keine weitere Digitalrolle um der Größe willen.** Suche Ergebnisnähe, nicht Titel.
3. **Governance als öffentliche Hauptidentität streichen.** Nur als Vertrauensanker nutzen.
4. **Weniger, aber schärfer publizieren:** industrielle Performance, lokale KI,
   Planung, Working Capital, operative Lernfähigkeit — nicht Audit und Compliance.
5. **Sponsorship intern aufbauen, nicht nur Reputation extern.** Der Sichtbarkeitskanal
   ist nicht das Paper, sondern der interne Executive One-Pager in der Sprache der
   Entscheider (Ist-Zustand, Ziel-KPI, Euro-Logik, Entscheidungsbedarf).
6. **Startup 2026 bewusst klein halten** — rechtlich sauber, generisch, ohne
   Industriekunden-Akquise; Ziel ist Optionswert, nicht Umsatz.
7. **Kein 68-Stunden-Selbstausbeutungsmodell mit Kleinkind.** Das wäre schlechte
   Risikosteuerung, keine Ambition.

**Die unangenehme Wahrheit:** Der nächste Karrieresprung entsteht nicht durch noch
mehr Beweise der Intelligenz. Er entsteht, wenn Entscheider Linus in Konflikten
zwischen Sales, Operations, Finance, IT und Risiko als jemanden erleben, der
Geschäftsleistung verbessert und Entscheidungen tragfähig macht.

**Offene Fragen (vom Analysten adressiert, zu klären):**
Nebenbeschäftigungs-/IP-Klauseln im Arbeitsvertrag · reale Co-Ownership-Chance für
S&OP/Sales Excellence/Supply Chain Analytics · Rotec-Feedback und die tatsächlichen
Entscheider · heute messbare Forecast-KPIs · glaubwürdige Fürsprecher außerhalb IT ·
realistische freie Abende pro Woche · Zielbild GM vs. CDO/Chief Transformation Officer.
"""

R1_REFS = [
    "Mollick, E. (2026). The IT department: Where AI goes to die. Financial Times. "
    "https://www.ft.com (By Invitation, 2026)",
    "Kohl, L. (2025). Knowledge-based maintenance assistance systems: A design science "
    "approach to cognitive maintenance support (Dissertation). Technische Universität Wien.",
    "Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in "
    "information systems research. MIS Quarterly, 28(1), 75–105.",
    "Davenport, T. H., & Westerman, G. (2018). Why so many high-profile digital "
    "transformations fail. Harvard Business Review Digital Articles.",
    "Iansiti, M., & Lakhani, K. R. (2020). Competing in the age of AI: Strategy and "
    "leadership when algorithms and networks run the world. Harvard Business Review Press.",
]

# ---------------------------------------------------------------------------
# R2 — Pass 2
# ---------------------------------------------------------------------------
R2_EXEC = """
**Harte These:** Die aktuelle Paper-Strategie ist in ihrer jetzigen Form strategisch
falsch, wenn das Primärziel General Management ist. Sie ist intellektuell plausibel
und akademisch verwertbar, löst aber nicht das Karriereproblem, das nach der
Rotec-Ablehnung sichtbar wurde — und kann es verschärfen, weil sie Linus noch
klarer als Digital-/AI-Governance-Spezialisten markiert.

**Die Lücke in einem Satz:** Die Papers beantworten die Frage *„Wer kann AI-Nutzung
in regulierten Organisationen sauber einhegen?"* Die Karrierefrage lautet aber
*„Wem traut man zu, Geschäftsleistung, Kapitalbindung, Lieferfähigkeit,
Forecast-Qualität und Führung über Funktionsgrenzen hinweg zu verbessern?"*

**Rangfolge-Empfehlung:**
- **Paper 1 behalten, umbauen** auf „Governed AI Experimentation for Industrial
  Performance Improvement" — Vibe Coding nur als Mechanismus, nicht als Headline-Identität.
- **Paper 2 streichen oder stark reduzieren** — als Hauptautor zu teuer und zu akademisch;
  nur als Co-Autor mit fremdem Methodenlead.
- **Paper 3 umbauen** — aus dem Audit-Frame heraus zu „Operational Learning
  Infrastructure"; Evaluation auf Wiederverwendbarkeit und Skalierung.
- **Paper 4 streichen** — SME ist eine Ablenkung; allenfalls kurzer Praxisartikel.

**Die Compliance-Kompetenz-Falle:** Ein starkes Label zieht Folgeangebote an.
Label „AI Governance" → mehr Gremien, mehr Policy, mehr Risikomanagement, selten P&L.
Kernkritik: *„Linus darf Governance nicht verkaufen. Er muss gesteuerte
Geschäftsbeschleunigung verkaufen."*

**Das Sichtbarkeits-Problem:** ICIS, ECIS, BISE, JMIS werden in der
voestalpine-Entscheidungslogik kaum gelesen. Sponsorship entsteht nicht durch
Publikation, sondern durch **wiederholte Exposition gegenüber Entscheidungsträgern
in deren Sprache**.
"""

R2_CLOSE = """
**Konkrete Empfehlung, in Reihenfolge:**

1. **Portfolio sofort von vier auf maximal zwei Papers kürzen** (4 h Entscheidung,
   8 h Re-Scoping).
2. **Paper 1 innerhalb von zwei Wochen auf Business-KPIs umschreiben** (20–30 h) —
   neuer Abstract, neue Forschungsfrage, neue Case-Auswahl. Jedes Gate muss zeigen,
   wie es schnelle Experimente in Forecast, Materialplanung, Instandhaltung oder
   Werkzeugmanagement ermöglicht.
3. **Vor jeder weiteren öffentlichen Veröffentlichung eine interne Kommunikations-
   und Risikoprüfung** (6–10 h): vertrauliche Details entfernen, Arbeitgeberbezug
   neutralisieren, Media-Relations-Risiko prüfen. Die 9.000 Wörter Medium-Artikel
   sind ein kontrollbedürftiges Reputationsasset, kein Karriereturbo.
4. **Internes Sponsorship-Paket bauen** (25–40 h): drei One-Pager für
   GF/Sales/Controlling — Forecast Accuracy, Predictive Maintenance ROI,
   Working Capital durch Materialplanung. Näher am Rotec-Problem als jeder Journalartikel.
5. **Operative Rotation oder Co-Ownership aktiv vorbereiten** (40–60 h über drei Monate
   plus politische Arbeit). Ziel: Mitverantwortung für einen Wertstrom.

**Die unbequeme Kernfrage, die der Bericht stellt:**
*Schreibst du diese Papers, weil sie die härteste Brücke Richtung General Management
bauen, oder weil sie in deiner Komfortzone liegen und dir ein kontrollierbares
Exzellenzfeld geben, nachdem Rotec gezeigt hat, dass interne Macht- und
Sponsorship-Logik unbequemer ist als inhaltliche Leistung?*

Anerkennung im falschen Feld fühlt sich wie Fortschritt an, während sie die spätere
Auswahlentscheidung verengt.
"""

R2_REFS = [
    "Mollick, E. (2026). The IT department: Where AI goes to die. Financial Times.",
    "Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in "
    "information systems research. MIS Quarterly, 28(1), 75–105.",
    "Pfeffer, J. (2010). Power: Why some people have it and others don't. HarperBusiness.",
    "Kotter, J. P. (2012). Leading change. Harvard Business Review Press.",
    "Kohl, L. (2025). Knowledge-based maintenance assistance systems (Dissertation). "
    "Technische Universität Wien.",
]

# ---------------------------------------------------------------------------
# R3 — Pass 1
# ---------------------------------------------------------------------------
R3_EXEC = """
**Executive Verdict:** Die vier Paper sind als akademisches Programm plausibel,
aber als Karriereinstrument für den GM-Pfad schief ausgerichtet: Sie beweisen
Governance-Kompetenz, nicht Ergebnisverantwortung. Paper 1 und 3 können als
Glaubwürdigkeitsanker bleiben, wenn sie strikt als Nebenprodukt realer operativer
Transformation gerahmt werden. **Paper 2 und 4 sind derzeit Karriere-Kosten.**

**Der methodische Befund pro Paper:**

| Paper | Echtheit des Gaps | Haupt-Bruchpunkt | Erfolgswahrscheinlichkeit |
|---|---|---|---|
| 1 — Governed Vibe Coding | Am realsten | Evaluation dünn (3 Fälle), Rewrite-Threshold unbelegt | 35–45 % mit TU-Co-Autor; 10–20 % ohne |
| 2 — Compliance-Innovation Paradox | Gefährlich groß formuliert | Survey-Rekrutierung n≈80–150 bricht ohne Verband/Institut | 10–15 % (AMD); <10 % ohne Co-Autor |
| 3 — Crowd to Lab to Audit | Plausibel, nah an eigener Spur | Selbstreferenzialität (Designer = Evaluator) | 40–55 % (CIRP CMS); 15–25 % (JMIS/ISJ) |
| 4 — Vibe Coding & SME | Real, aber nicht der beste Gap | Case-Zugang zu SMEs massiv überschätzt | 10–20 % starke Journals |

**Aufwands-Realität:** 675 h sind Schreibplan-Stunden. Realistisch für vier
publizierbare Papers: **1.000–1.300 h** über mehrere Jahre, inkl. Wartezeit,
Co-Autor-Koordination, Freigaben, Datenbereinigung, Reviewer-Runden und Rejections.

**Die Medium-Artikel:** Technisch stark, aber öffentlich eher „Engineer mit
Homelab/Agent-Stack" als „zukünftiger Geschäftsführer eines Industriebereichs".
Artikel 1 (188M-Token-Audit) adressiert Engineers; Artikel 2 („Personal AI
Infrastructure, built during paternity leave") ist reputativ ambivalent.

**Fehlende Arbeit:** Kein fünftes Governance-Paper, sondern ein belastbares,
zahlengestütztes Paper oder Executive Essay über **Forecast Accuracy, Working
Capital, S&OP und Ergebniswirkung**.
"""

R3_CLOSE = """
**Empfohlene nächste drei Handlungen:**

1. **Bis 2026-10-15: Paper-Portfolio halbieren und ein Karriere-KPI-Paper ergänzen.**
   Paper 1 nur weiterführen, wenn TU-Co-Autor und organisationale Freigabe real sind.
   Paper 2 und 4 einfrieren. Paper 3 als optionales CIRP-CMS-Follow-on scopen.
   Einseiter für Paper/Essay 5 (Forecast Accuracy → S&OP → Working Capital) entwerfen.
2. **Bis 2026-10-31: Eine belastbare Forecast-KPI-Baseline erzeugen.** Gemeinsam mit
   Sales und Controlling eine baselinefähige Kennzahl definieren: forecast error, bias,
   planning volatility, manual reconciliation effort, revenue-risk proxy oder
   inventory/working-capital proxy. **Ohne Zahl gibt es keine GM-Story, nur eine IT-Erzählung.**
3. **Bis 2026-11-30: Medium-Launch neu priorisieren.** Nicht mit zwei
   Infrastruktur-Artikeln starten, sondern mit einem Entscheider-Artikel
   („One Forecast Number" oder „Predictive Maintenance with a Euro Owner").
   Der 188M-Token-Audit darf danach als technischer Nebenkanal erscheinen.

**Schlussurteil:** Nicht versuchen, die nächste Karrierestufe durch mehr Forschung
über AI Governance zu gewinnen. Ein bis zwei Governance-Arbeiten nutzen, um die
intellektuelle Glaubwürdigkeit zu halten, aber die knappe Energie auf eine
öffentlich und intern belegbare Ergebnisgeschichte legen: **Forecast Accuracy,
S&OP, Working Capital, Predictive Maintenance mit Euro-KPI.**

Empfohlene Selbstbeschreibung statt „Industry-informed researcher":
**„Industrial transformation leader using digital systems to improve measurable
business performance in regulated manufacturing."**
"""

R3_REFS = [
    "Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in "
    "information systems research. MIS Quarterly, 28(1), 75–105.",
    "Mollick, E. (2026). The IT department: Where AI goes to die. Financial Times.",
    "Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). "
    "A design science research methodology for information systems research. "
    "Journal of Management Information Systems, 24(3), 45–77.",
    "Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science "
    "research for maximum impact. MIS Quarterly, 37(2), 337–355.",
    "Kohl, L. (2025). Knowledge-based maintenance assistance systems (Dissertation). "
    "Technische Universität Wien.",
]

# ---------------------------------------------------------------------------
# R4 / R5 — Paper-Outlines
# ---------------------------------------------------------------------------
R4_EXEC = """
**Was im Report steht:** Die vollständige Outline des Leitpapiers — Gap-Analyse,
Forschungsfragen, DSR-Artefakt (Two-Track-Model + Promotion Gate G1–G6 +
Rewrite-Threshold), Evaluationsdesign, Venue- und Co-Autor-Strategie.

**Bewertung dieses Berichts (siehe R2/R3):** Paper 1 ist das einzige Paper mit
klarem Keep-Status — aber **nur nach Umbau**. Der Artefaktkern (G1–G6, Provenance,
Data-Zone, Owner, Failure Mode, Exit Path) ist in Auditorensprache geschrieben.
Für den GM-Pfad muss das Paper mit Business-KPIs beginnen: cycle time to validated
experiment, time-to-benefit, avoided process cost, business-owner accountability,
economic threshold for rewrite vs. review. Governance wird dann zur
Ermöglichungsinfrastruktur, nicht zur Kernbotschaft.

**Der stärkste Beitrag** ist nicht der Zwei-Lane-Ansatz (Sandbox vs. Production ist
bekannt), sondern der **Rewrite-Threshold** — die ökonomische Entscheidung, ab wann
menschliches Review teurer ist als saubere Re-Implementierung. Dieser Teil ist laut
Outline selbst „a proposition, not a validated finding" und muss empirisch
kalibriert werden.

**Harte Voraussetzungen:** TU-Wien-Co-Autor (Ansari/Sihn/Reisinger) für DSR-Rigor,
organisationale Freigabe vor dem Schreiben, mindestens ein vertriebs-, operations-
oder finanznaher KPI im Case-Material. Ohne Co-Autor lesen Top-Reviewer es als
Fallbericht.
"""

R4_CLOSE = """
**Empfehlung:** Paper 1 innerhalb von zwei Wochen auf Business-KPIs umschreiben
(20–30 h). Neuer Abstract, neue Forschungsfrage, neue Case-Auswahl. Jedes Gate
muss zeigen, wie es schnelle Experimente in Forecast, Materialplanung,
Instandhaltung oder Werkzeugmanagement ermöglicht — nicht nur Risiken reduziert.
Ohne KPI-Bezug bleibt es ein CIO-Signal.

Weiterführung nur, wenn zwei Bedingungen bis zu einem festen Datum real sind:
(a) TU-Co-Autor zugesagt, (b) organisationale Freigabe erteilt. Sonst einfrieren.
"""

R4_REFS = [
    "Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in "
    "information systems research. MIS Quarterly, 28(1), 75–105.",
    "Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). "
    "A design science research methodology for information systems research. "
    "Journal of Management Information Systems, 24(3), 45–77.",
    "Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science "
    "research for maximum impact. MIS Quarterly, 37(2), 337–355.",
    "Verordnung (EU) 2024/1689 des Europäischen Parlaments und des Rates vom "
    "13. Juni 2024 zur Festlegung harmonisierter Vorschriften für künstliche "
    "Intelligenz (EU-AI-Act). Amtsblatt der Europäischen Union.",
    "ISO/IEC 27001:2022. Information security, cybersecurity and privacy protection — "
    "Information security management systems — Requirements. ISO.",
]

R5_EXEC = """
**Was im Report steht:** Die vollständige Outline des SME-Papiers — Gap
(large regulated firm vs. KMU), Drei-Kriterien-Gate (Owner Sign-off, Data
Declaration, Provenance Note), Accountability-Inversion als theoretischer Hebel,
Case-Design (6–10 SME-Owner), Venue-Strategie.

**Bewertung dieses Berichts (siehe R2/R3): Streichen oder delegieren.**
Das SME-Thema ist nicht Linus' beste Arena. Als Industry-Autor eines großen
Industriekonzerns hat er keinen natürlichen Zugangsvorteil zu SME-Ownern, die
undokumentierte AI-Nutzung offenlegen und Tool-Walkthroughs erlauben. Der Case-Zugang
ist massiv unterschätzt.

**Akademisch zu dünn:** Die Drei-Kriterien-Gate-Idee ist praktisch nützlich, aber
Reviewer könnten sagen: *Das ist eine Checkliste, kein wissenschaftlicher Beitrag.*
Der theoretische Hebel „accountability inversion" (im KMU *ist* die Owner-Signatur
das Control) müsste deutlich stärker ausgearbeitet werden.

**Optionale Verwertung:** Als TU-Wien-Masterarbeitsvehikel (studentische Feldarbeit,
minimaler Zeitanteil), oder als kurzer Praxisartikel. Nicht als 150-Stunden-Paper
im eigenen 2026–2027-Workload.
"""

R5_CLOSE = """
**Empfehlung:** Aus dem eigenen Arbeitsprogramm streichen. Zwei mögliche
Weiterverwertungen:

1. **Als Masterarbeit delegieren** — Betreuung ja, Feldarbeit und Schreiben nein.
   Linus tritt als Transferperson und Betreuer auf, nicht als Hauptautor.
2. **Als kurzen Praxisartikel** für ein KMU-/Transfermedium, falls das Thema
   öffentlich sichtbar bleiben soll. Aufwand dann 10–15 h statt 150 h.

**Begründung:** Paper 4 ist akademische Ausweitung eines Programms, bevor Paper 1
überhaupt bewiesen ist. Es verlängert die Vibe-Coding-Governance-Schublade, ohne
interne Karrierekraft zu erzeugen.
"""

R5_REFS = [
    "Verordnung (EU) 2024/1689 (EU-AI-Act). Amtsblatt der Europäischen Union.",
    "Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in "
    "information systems research. MIS Quarterly, 28(1), 75–105.",
    "Wirtz, B. W., Weyerer, J. C., & Geyer, C. (2019). Artificial intelligence and "
    "the public sector—Applications and challenges. International Journal of "
    "Public Administration, 42(7), 596–615.",
]


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
REPORTS = [
    dict(
        key="roadmap",
        file="analysis/2026-09-18-codex-strategic-roadmap.md",
        title="Strategische Roadmap 2026–2029",
        subtitle="Karrierepfade, Thought Leadership, Side-Startup und Zeitbudget — kritische Mehrperspektiven-Analyse",
        report_type="karriereanalyse",
        metrics=[("7", "Karrierepfade bewertet"), ("5", "Zeitbudget-Szenarien"),
                 ("2026–2029", "Planungshorizont"), ("68 h", "Warnschwelle Wochenlast")],
        meta={"Analyst": "OpenAI Codex (gpt-5.5)", "Auftrag": "Linus Kohl",
              "Quelle": "Karriere- und Projektkontext, Stand 2026-09-18",
              "Klassifikation": "Vertraulich"},
        exec_summary=R1_EXEC, closing=R1_CLOSE, references=R1_REFS,
    ),
    dict(
        key="review-pass2",
        file="analysis/2026-09-17-codex-paper-strategie-review-pass2.md",
        title="Paper-Strategie vs. General-Management-Pfad",
        subtitle="Kritische Strategieprüfung (Pass 2) — Label-Ökonomie, Sichtbarkeit und Opportunitätskosten",
        report_type="strategieanalyse",
        metrics=[("4", "Papers geprüft"), ("2", "empfohlene Streichungen"),
                 ("1.000–1.300 h", "realistischer Gesamtaufwand"), ("2", "Keep-Status")],
        meta={"Analyst": "OpenAI Codex (gpt-5.5)", "Auftrag": "Linus Kohl",
              "Quelle": "Codex-Review Pass 2, 2026-09-17", "Klassifikation": "Vertraulich"},
        exec_summary=R2_EXEC, closing=R2_CLOSE, references=R2_REFS,
    ),
    dict(
        key="review-pass1",
        file="analysis/2026-09-17-codex-paper-strategie-review.md",
        title="Kritische Analyse: Paper-Strategie, Medium-Artikel und GM-Positionierung",
        subtitle="Senior-Review (Pass 1) — methodische Machbarkeit, Venue-Realismus, Publikationsrisiko",
        report_type="strategieanalyse",
        metrics=[("4", "Papers methodisch geprüft"), ("2", "Medium-Artikel bewertet"),
                 ("675 h", "geplanter Aufwand (Plan)"), ("7", "unbequeme Wahrheiten")],
        meta={"Analyst": "OpenAI Codex (gpt-5.5)", "Auftrag": "Linus Kohl",
              "Quelle": "Codex-Review Pass 1, 2026-09-17", "Klassifikation": "Vertraulich"},
        exec_summary=R3_EXEC, closing=R3_CLOSE, references=R3_REFS,
    ),
    dict(
        key="paper-1",
        file="paper-1-governed-vibe-coding.md",
        title="Paper 1 — Vibe Coding in Regulated Industry",
        subtitle="A Governed Experimentation Framework — vollständige Outline (Leitpapier)",
        report_type="paper-outline",
        metrics=[("DSR", "Methode"), ("ICIS/ECIS/BISE", "Ziel-Venue"),
                 ("G1–G6", "Promotion Gate"), ("9.000–11.000", "Wörter (Ziel)")],
        meta={"Analyst": "OpenAI Codex (gpt-5.5)", "Auftrag": "Linus Kohl",
              "Quelle": "Paper-Outline v1", "Klassifikation": "Intern"},
        exec_summary=R4_EXEC, closing=R4_CLOSE, references=R4_REFS,
        source_override="paper-outlines/paper-1-governed-vibe-coding.md",
    ),
    dict(
        key="paper-4",
        file="paper-4-vibe-coding-sme.md",
        title="Paper 4 — Vibe Coding and the SME",
        subtitle="Democratised Innovation with Guardrails — vollständige Outline (zurückgestellt)",
        report_type="paper-outline",
        metrics=[("3", "Gate-Kriterien"), ("6–10", "SME-Cases geplant"),
                 ("JSBM", "Ziel-Venue"), ("zurückgestellt", "Status")],
        meta={"Analyst": "OpenAI Codex (gpt-5.5)", "Auftrag": "Linus Kohl",
              "Quelle": "Paper-Outline v1", "Klassifikation": "Intern"},
        exec_summary=R5_EXEC, closing=R5_CLOSE, references=R5_REFS,
        source_override="paper-outlines/paper-4-vibe-coding-sme.md",
    ),
]


FIXED_IDS = {
    "roadmap": "ACTA-2026-033",
    "review-pass2": "ACTA-2026-034",
    "review-pass1": "ACTA-2026-035",
    "paper-1": "ACTA-2026-036",
    "paper-4": "ACTA-2026-037",
}


def resolve_id(spec):
    """Feste Berichtsnummer, damit Re-Runs das Archiv nicht aufblaehen."""
    rid = FIXED_IDS[spec["key"]]
    try:
        from acta_registry import get_report
        if not get_report(rid):
            raise LookupError
    except Exception:
        reg = register_report(
            title=spec["title"], report_type=spec["report_type"],
            author=AUTHOR, client=CLIENT,
            classification=spec["meta"]["Klassifikation"], version="1.0",
            metadata={"key": spec["key"], "quelle": spec["file"]},
        )
        return reg["report_id"]
    return rid


def main():
    results = []
    for spec in REPORTS:
        src = spec.get("source_override") or spec["file"]
        path = src if os.path.isabs(src) else os.path.join(PROJECT, src)
        if not os.path.exists(path):
            print(f"!! fehlt: {path}")
            continue
        md = open(path, encoding="utf-8").read()

        rid = resolve_id(spec)

        html = build_report(rid, spec["title"], spec["subtitle"], md,
                            spec["metrics"], spec["meta"], spec["exec_summary"],
                            spec["closing"], spec["references"])
        hp = os.path.join(OUT, f"{rid}_{spec['key']}.html")
        pp = os.path.join(OUT, f"{rid}_{spec['key']}.pdf")
        open(hp, "w", encoding="utf-8").write(html)
        ok = html_to_pdf(hp, pp)
        words = len(md.split())
        results.append((rid, spec["title"], hp, pp, ok, words))
        print(f"{rid}  {spec['key']:14s}  pdf={'OK' if ok else 'FEHLT'}  {words:5d} Wörter")

    print("\n=== ZUSAMMENFASSUNG ===")
    for rid, t, hp, pp, ok, w in results:
        print(f"{rid} | {t} | {'PDF' if ok else 'HTML only'} | {w} Wörter")
    return results


if __name__ == "__main__":
    main()
