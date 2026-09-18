#!/usr/bin/env python3
"""
ClawHub-Integration der Karriere-/Paper-Analysen.

1. research_catalog.json  → 5 neue Einträge (Kategorie 'Strategie & Karriere')
2. medium_articles.json   → 5 neue Artikel-Einträge mit vollständigem Inhalt
                            (Kategorie 'Strategie & Karriere' / 'Paper Strategy')

Idempotent: bestehende Einträge mit gleicher id werden ersetzt, nicht dupliziert.
Die JSON-Struktur der Zieldateien bleibt unverändert (keine neuen Top-Level-Keys).
"""

import json
import os
import re

WORKSPACE = "/data/.openclaw/workspace"
ANALYSIS = os.path.join(WORKSPACE, "projects/linus-academic-page/analysis")
REPORTS = os.path.join(ANALYSIS, "acta_reports")

CATALOG = "/tmp/prodmirror/data/research_catalog.json"
MEDIUM = "/tmp/clawhub-src/medium_articles.json"
if not os.path.exists(MEDIUM):
    MEDIUM = "/tmp/prodmirror/data/medium_articles.json"

# ---------------------------------------------------------------------------
# Berichts-Metadaten (aus report_defs.py)
# ---------------------------------------------------------------------------
REPORTS_META = [
    dict(
        key="roadmap", rid="ACTA-2026-033",
        title="Strategische Roadmap 2026–2029",
        subtitle="Karrierepfade, Thought Leadership, Side-Startup und Zeitbudget",
        source="analysis/2026-09-18-codex-strategic-roadmap.md",
        category="Strategie & Karriere",
        medium_category="Strategy & Career",
        target="Intern / ClawHub",
        summary=("Kritische Mehrperspektiven-Analyse: 7 Karrierepfade bewertet (operative Leitung, "
                 "SVP Digital, Corporate Strategy, Venture Clienting, Consulting, Startup), "
                 "Gehaltsbänder AT/DE, 5 Zeitbudget-Szenarien und 24-Monats-Roadmap. Kernbefund: "
                 "die Engstelle ist Zuschreibung, nicht Kompetenz. Empfehlung: 2026 = "
                 "Karriere-Repositionierungsjahr, nicht Startup-Jahr. Salesforce/Forecast als "
                 "GM-Brücke (S&OP-/Working-Capital-Mandat statt IT-Integration)."),
        tags=["karriere", "general-management", "roadmap", "zeitbudget", "voestalpine"],
    ),
    dict(
        key="review-pass2", rid="ACTA-2026-034",
        title="Paper-Strategie vs. General-Management-Pfad (Pass 2)",
        subtitle="Label-Ökonomie, Sichtbarkeit und Opportunitätskosten",
        source="analysis/2026-09-17-codex-paper-strategie-review-pass2.md",
        category="Strategie & Karriere",
        medium_category="Paper Strategy",
        target="Intern / ClawHub",
        summary=("Strategieprüfung der Paper-Agenda gegen das GM-Ziel: Vier Governance-Papers "
                 "zementieren das Spezialistenlabel. Empfehlung: Portfolio auf max. 2 kürzen — "
                 "Paper 1 umbauen (Business-KPI-Rahmung), Paper 3 aus dem Audit-Frame holen, "
                 "Paper 2 und 4 streichen. Sichtbarkeit entsteht nicht durch Journals (ICIS/BISE "
                 "werden in Konzernentscheidungen kaum gelesen), sondern durch interne "
                 "Executive One-Pager in der Sprache der Entscheider."),
        tags=["paper-strategie", "governance-falle", "sponsorship", "opportunitätskosten"],
    ),
    dict(
        key="review-pass1", rid="ACTA-2026-035",
        title="Kritische Analyse: Paper-Strategie, Medium-Artikel und GM-Positionierung (Pass 1)",
        subtitle="Methodische Machbarkeit, Venue-Realismus, Publikationsrisiko",
        source="analysis/2026-09-17-codex-paper-strategie-review.md",
        category="Strategie & Karriere",
        medium_category="Paper Strategy",
        target="Intern / ClawHub",
        summary=("Senior-Review der vier Paper auf methodische Tragfähigkeit: Erfolgswahrschein"
                 "lichkeiten pro Venue, Bruchpunkte (Survey-Rekrutierung n≈80–150, SME-Case-Zugang, "
                 "Selbstreferenzialität), realistische 1.000–1.300 h statt geplanter 675 h. "
                 "Fehlende Arbeit: kein fünftes Governance-Paper, sondern ein zahlengestütztes "
                 "Forecast-Accuracy/S&OP/Working-Capital-Paper als Karriere-KPI."),
        tags=["paper-review", "dsr", "venue-analyse", "forecast-accuracy", "working-capital"],
    ),
    dict(
        key="paper-1", rid="ACTA-2026-036",
        title="Paper 1 — Vibe Coding in Regulated Industry: A Governed Experimentation Framework",
        subtitle="Vollständige Outline des Leitpapiers (DSR, ICIS/ECIS/BISE)",
        source="paper-outlines/paper-1-governed-vibe-coding.md",
        category="Paper Outlines",
        medium_category="Vibe Coding & Governance",
        target="ICIS / ECIS / BISE",
        summary=("Vollständige Working-Paper-Outline: Gap (organisch generierte Code-Artefakte "
                 "durch Domain Experts vs. procured AI systems), Two-Track-Governance-Modell "
                 "(Sandbox- vs. Hardened-Lane), Promotion Gate G1–G6 und Rewrite-Threshold-Modell "
                 "(wann Review teurer ist als Neuschreiben). Bewertung: einziger Keep-Kandidat, "
                 "aber nur nach Umbau auf Business-KPIs und mit TU-Wien-Co-Autor + Freigabe."),
        tags=["vibe-coding", "governance", "design-science", "regulated-industry"],
    ),
    dict(
        key="paper-4", rid="ACTA-2026-037",
        title="Paper 4 — Vibe Coding and the SME: Democratised Innovation with Guardrails",
        subtitle="Vollständige Outline, Status zurückgestellt",
        source="paper-outlines/paper-4-vibe-coding-sme.md",
        category="Paper Outlines",
        medium_category="Vibe Coding & Governance",
        target="Journal of Small Business Management",
        summary=("Outline des SME-Papiers: Drei-Kriterien-Gate (Owner Sign-off, Data Declaration, "
                 "Provenance Note), Accountability-Inversion als theoretischer Hebel, Case-Design "
                 "mit 6–10 SME-Ownern. Bewertung: streichen oder als Masterarbeit delegieren — "
                 "falsche Arena, überschätzter Case-Zugang, akademisch zu dünn für starke Journals."),
        tags=["vibe-coding", "sme", "governance", "zurückgestellt"],
    ),
]


def load_json(p):
    return json.load(open(p, encoding="utf-8"))


def save_json(p, d):
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  geschrieben: {p} ({len(d)} Einträge)")


def md_path(spec):
    return os.path.join(os.path.dirname(ANALYSIS), spec["source"])


def build_catalog_entries():
    entries = []
    for s in REPORTS_META:
        entries.append({
            "id": s["rid"].lower(),
            "title": s["title"],
            "category": s["category"],
            "date": "2026-09-18",
            "summary": s["summary"],
            "source_url": f"https://clawhub.cabbagebaggage.net/medium?open={s['key']}",
            "tags": s["tags"] + ["acta", s["rid"]],
            "path": f"acta/{s['rid']}_{s['key']}.pdf",
            "type": "PDF",
            "report_id": s["rid"],
            "source_note": s.get("note", ""),
            "subtitle": s["subtitle"],
        })
    return entries


def build_medium_entries():
    out = []
    for s in REPORTS_META:
        p = md_path(s)
        content = open(p, encoding="utf-8").read()
        out.append({
            "id": s["rid"].lower(),
            "title": s["title"],
            "subtitle": s["subtitle"],
            "category": s["medium_category"],
            "status": "ACTA Report",
            "target": s["target"],
            "hasDraft": True,
            "outlineLines": len(content.split("\n")),
            "outline": content,
            "acta_report_id": s["rid"],
            "reportPdf": f"acta/{s['rid']}_{s['key']}.pdf",
            "reportHtml": f"acta/{s['rid']}_{s['key']}.html",
            "tags": s["tags"],
        })
    return out


def merge(target, new, key="id"):
    index = {e.get(key): i for i, e in enumerate(target)}
    added, replaced = 0, 0
    for e in new:
        if e[key] in index:
            target[index[e[key]]] = e
            replaced += 1
        else:
            target.append(e)
            added += 1
    return added, replaced


def main():
    print("=== research_catalog.json ===")
    if os.path.exists(CATALOG):
        cat = load_json(CATALOG)
        a, r = merge(cat, build_catalog_entries())
        save_json(CATALOG, cat)
        print(f"  neu: {a}, ersetzt: {r}")
    else:
        print("  ! catalog nicht gefunden:", CATALOG)

    print("=== medium_articles.json ===")
    if os.path.exists(MEDIUM):
        med = load_json(MEDIUM)
        a, r = merge(med, build_medium_entries())
        save_json(MEDIUM, med)
        print(f"  neu: {a}, ersetzt: {r}")
    else:
        print("  ! medium nicht gefunden:", MEDIUM)


if __name__ == "__main__":
    main()
