#!/usr/bin/env python3
"""
ClawHub-Integration v2 — Publikationsstrategie (2026-09-29)

Schreibt die überarbeitete Publikationsstrategie nach ClawHub:

  medium_articles.json   → 6 Executive Essays + 2 Research Papers + 1 Strategie-Report
  research_catalog.json  → ACTA-2026-039 (Strategie v2) + Essay-/Paper-Verweise

Quelle: analysis/2026-09-29-codex-publikationsstrategie-v2.md
Ziel:   clawhub-dashboard (lokale Repo-Kopie) — wird danach nach PROD deployed.
Idempotent: gleiche id ersetzt, nicht dupliziert.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = "/data/.openclaw/workspace"
CLUSTER = os.path.join(WORKSPACE, "clawhub-dashboard")
MEDIUM = os.path.join(CLUSTER, "dashboard/briefing/data/medium_articles.json")
CATALOG = os.path.join(CLUSTER, "dashboard/data/research_catalog.json")

SRC = os.path.join(HERE, "2026-09-29-codex-publikationsstrategie-v2.md")
md = open(SRC, encoding="utf-8").read().replace("ACTA-2026-038", "ACTA-2026-039")

DATE = "2026-09-29"


def section(start_re, end_re):
    m = re.search(start_re + r"\s*\n(.*?)(?=\n" + end_re + r")", md, re.S)
    return m.group(1).strip() if m else ""


def grab(anchor, end_re=r"###? "):
    """Holt den Abschnitt beginnend beim Anker bis zum naechsten Ueberschrift-Anker."""
    m = re.search(re.escape(anchor) + r"\s*\n(.*?)(?=\n" + end_re + r")", md, re.S)
    return m.group(1).strip() if m else ""


# --- Essay-/Paper-Metadaten (aus der v2-Struktur) -------------------------
ESSAYS = [
    ("essay-agentic-enterprise",
     "The Agentic Industrial Enterprise",
     "Agents werden Teil des Operating Models — nicht nur neue Softwaretools.",
     "1.650"),
    ("essay-corporate-it",
     "Everyone Can Build Software. What Is Corporate IT For?",
     "Wenn Fachbereiche mit AI selbst Software bauen, verschiebt sich IT von Umsetzung zu Plattform, Architektur und Governance.",
     "1.600"),
    ("essay-factory-manager-2030",
     "The Factory Manager of 2030 Will Manage Humans and Agents",
     "Führung verändert sich, wenn digitale Agents operative Aufgaben und Entscheidungen übernehmen.",
     "1.550"),
    ("essay-measure-decisions",
     "Stop Counting AI Pilots. Measure Decisions.",
     "AI-Wert entsteht nicht durch die Anzahl der Use Cases, sondern durch bessere und schnellere Entscheidungen und messbare Business-KPIs.",
     "1.500"),
    ("essay-industrial-memory",
     "Why Industrial AI Needs Memory, Not Another Copilot",
     "Industrie braucht Kontext, Historie, Knowledge Graphs und Prozesswissen statt isolierter Chatbots.",
     "1.700"),
    ("essay-industrial-transformation",
     "From Digital Transformation to Industrial Transformation",
     "Digitalisierung darf nicht als IT-Programm geführt werden, sondern über OEE, Kosten, Cash, Qualität und Durchlaufzeit.",
     "1.600"),
]

PAPERS = [
    ("research-paper-1-agentic-reference-architecture",
     "Paper 1 — Agentic Industrial Systems: A Reference Architecture for Human–AI Collaboration in Brownfield Manufacturing",
     "Referenzarchitektur — der logische Nachfolger der ARCHIE-Dissertation.",
     "DSR", "ICIS / ECIS / BISE", "sehr hoch"),
    ("research-paper-2-maturity-model",
     "Paper 2 — From Assistance to Agency: A Maturity Model for Agentic Manufacturing",
     "Reifegradmodell von Manual bis Autonomous multi-agent operation.",
     "Maturity Model / empirisch", "BISE / CIRP CMS / JMS", "sehr hoch"),
]


def build_medium():
    out = []

    # 1) Strategie-Report selbst
    out.append({
        "id": "acta-2026-039-publikationsstrategie-v2",
        "title": "Publikationsstrategie v2 — industrielle Steuerungsfähigkeit statt AI-Spezialistenlabel",
        "subtitle": "6 Executive Essays, 2 Papers, GM-Fit-Prüfung und 1.180h Zeitplan",
        "category": "Strategy",
        "status": "ACTA Report",
        "target": "Intern / ClawHub",
        "hasDraft": True,
        "acta_report_id": "ACTA-2026-039",
        "reportPdf": "acta/ACTA-2026-039_publikationsstrategie.pdf",
        "outline": md,
        "outlineLines": len(md.split("\n")),
    })

    # 2) Die 6 Essays
    for eid, title, kernthese, words in ESSAYS:
        body = grab(f"### Essay ", end_re=r"###? ") if False else ""
        # konkreter Abschnitt
        m = re.search(r"### Essay \d+ — \*\*" + re.escape(title) + r"\*\*\s*\n(.*?)(?=\n### )", md, re.S)
        content = m.group(1).strip() if m else ""
        text = (f"# {title}\n\n**Kernthese:** {kernthese}\n\n"
                f"**Zielwortzahl:** {words}\n\n---\n\n{content}")
        out.append({
            "id": eid,
            "title": title,
            "subtitle": kernthese,
            "category": "Executive Essays",
            "status": "Outline",
            "target": f"Medium · {words} Wörter",
            "hasDraft": True,
            "outline": text,
            "outlineLines": len(text.split("\n")),
        })

    # 3) Die 2 Papers
    for pid, title, sub, method, venue, prio in PAPERS:
        m = re.search(r"### Paper \d+ — \*\*(.*?)\*\*\s*\n(.*?)(?=\n### |\n## )", md, re.S)
        # exakt per Titel suchen
        key = title.split(" — ", 1)[1]
        m = re.search(re.escape(key) + r"\*\*\s*\n(.*?)(?=\n### |\n## )", md, re.S)
        content = m.group(1).strip() if m else ""
        text = (f"# {title}\n\n**Methodik:** {method} · **Ziel-Venue:** {venue} · "
                f"**Priorität:** {prio}\n\n---\n\n{content}")
        out.append({
            "id": pid,
            "title": title,
            "subtitle": sub,
            "category": "Research Papers",
            "status": "Working Paper" if "Paper 1" in title else "Outline",
            "target": venue,
            "hasDraft": True,
            "outline": text,
            "outlineLines": len(text.split("\n")),
        })

    return out


def build_catalog():
    summary = section(r"## Executive Summary für ACTA-2026-039\s*\n", r"\n## 1\.")
    summary = re.sub(r"\s+", " ", summary)[:900]
    return [
        {
            "id": "acta-2026-039-publikationsstrategie-v2",
            "title": "Publikationsstrategie v2 — industrielle Steuerungsfähigkeit statt AI-Spezialistenlabel",
            "category": "Strategie & Karriere",
            "date": DATE,
            "summary": summary,
            "source_url": "https://clawhub.cabbagebaggage.net/medium?open=acta-2026-039-publikationsstrategie-v2",
            "tags": ["publikationsstrategie", "executive-essays", "agentic-ai",
                     "general-management", "acta", "ACTA-2026-039"],
            "path": "acta/ACTA-2026-039_publikationsstrategie.pdf",
            "type": "PDF",
            "report_id": "ACTA-2026-039",
            "subtitle": "Sechs Executive Essays, zwei Papers und die Evidenz- und Aufwandslogik für ein GM-Zielbild",
        },
        {
            "id": "acta-2026-039-essays",
            "title": "Executive Essay-Serie (6 Teile) — Agentic Industrial Enterprise",
            "category": "Strategie & Karriere",
            "date": DATE,
            "summary": ("Sechs Essay-Outlines als sichtbare Serie: The Agentic Industrial Enterprise · "
                        "What Is Corporate IT For? · The Factory Manager of 2030 · Stop Counting AI Pilots. "
                        "Measure Decisions. · Why Industrial AI Needs Memory · From Digital Transformation to "
                        "Industrial Transformation. Jeweils mit Kernthese, Audience, Hook, Argumentationslinie und CTA."),
            "source_url": "https://clawhub.cabbagebaggage.net/medium",
            "tags": ["executive-essays", "thought-leadership", "agentic-ai", "acta"],
            "path": "acta/ACTA-2026-039_publikationsstrategie.pdf",
            "type": "PDF",
            "report_id": "ACTA-2026-039",
            "subtitle": "Essay-Portfolio für industrielle Positionierung",
        },
        {
            "id": "acta-2026-039-papers",
            "title": "Wissenschaftliche Agenda v2 — 2 Papers (Reference Architecture + Maturity Model)",
            "category": "Paper Outlines",
            "date": DATE,
            "summary": ("Fokussierte Agenda statt vier Governance-Papers: Paper 1 entwirft und evaluiert eine "
                        "Referenzarchitektur für Human–AI Collaboration in Brownfield Manufacturing (DSR, "
                        "ICIS/ECIS/BISE). Paper 2 operationalisiert den Übergang von Assistenz zu Agency als "
                        "Reife- und Fähigkeitsmodell (BISE/CIRP CMS). Gemeinsamer Kern: Entscheidung, Autonomie, "
                        "Übergabe, Kontext, Eingriffsrecht, wirtschaftliches Outcome."),
            "source_url": "https://clawhub.cabbagebaggage.net/medium",
            "tags": ["paper-agenda", "agentic-ai", "reference-architecture", "maturity-model", "acta"],
            "path": "acta/ACTA-2026-039_publikationsstrategie.pdf",
            "type": "PDF",
            "report_id": "ACTA-2026-039",
            "subtitle": "Zwei methodisch verbundene Papers",
        },
    ]


def load(p):
    return json.load(open(p, encoding="utf-8"))


def save(p, d):
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"  geschrieben: {p} ({len(d)} Einträge)")


def merge(target, new, key="id"):
    index = {e.get(key): i for i, e in enumerate(target)}
    added = replaced = 0
    for e in new:
        if e[key] in index:
            target[index[e[key]]] = e
            replaced += 1
        else:
            target.append(e)
            added += 1
    return added, replaced


def main():
    print("=== medium_articles.json ===")
    med = load(MEDIUM)
    # Alte, jetzt überholte Paper-Governance-Einträge als zurückgestellt markieren
    superseded = {"paper-2", "paper-3", "paper-4"}
    for a in med:
        if a.get("id") in superseded:
            a["status"] = "Zurückgestellt (Strategie v2)"
            a["category"] = "Auslaufend"
    a, r = merge(med, build_medium())
    save(MEDIUM, med)
    print(f"  neu: {a}, ersetzt: {r}")

    print("=== research_catalog.json ===")
    cat = load(CATALOG)
    a, r = merge(cat, build_catalog())
    save(CATALOG, cat)
    print(f"  neu: {a}, ersetzt: {r}")


if __name__ == "__main__":
    main()
