#!/usr/bin/env python3
"""
ClawHub-Integration der 6 Executive Essays + DOI-Verifikation.

Quelle: analysis/2026-10-01-executive-essays.md (konsolidiert, je Essay body+figure+references)
Ziel:   clawhub-dashboard/dashboard/briefing/data/medium_articles.json

Idempotent: bestehende Einträge gleicher id werden ersetzt.
Figure-Pfade werden auf assets/figures/... belassen (liegen bereits unter
dashboard/redesign/assets/figures/).
"""
import json
import os
import re

ANALYSIS = "/data/.openclaw/workspace/projects/linus-academic-page/analysis"
SRC = os.path.join(ANALYSIS, "2026-10-01-executive-essays.md")
DOI_MD = os.path.join(ANALYSIS, "2026-10-01-doi-verification.md")
MEDIUM = "/data/.openclaw/workspace/clawhub-dashboard/dashboard/briefing/data/medium_articles.json"

# Essay-Reihenfolge -> ClawHub id, Titel, target
ESSAYS = [
    ("essay-agentic-enterprise", "The Agentic Industrial Enterprise",
     "Thought Leadership · Operating Model", "LinkedIn / Medium / HBR-Stil"),
    ("essay-corporate-it", "Everyone Can Build Software. What Is Corporate IT For?",
     "CIO / Management", "LinkedIn / Medium / HBR-Stil"),
    ("essay-factory-manager-2030", "The Factory Manager of 2030 Will Manage Humans and Agents",
     "Führung / General Management", "LinkedIn / Medium / HBR-Stil"),
    ("essay-measure-decisions", "Stop Counting AI Pilots. Measure Decisions.",
     "Business-KPI / Controlling", "LinkedIn / Medium / HBR-Stil"),
    ("essay-industrial-memory", "Why Industrial AI Needs Memory, Not Another Copilot",
     "Forschung / Knowledge Graphs", "LinkedIn / Medium / HBR-Stil"),
    ("essay-industrial-transformation", "From Digital Transformation to Industrial Transformation",
     "Industrielle Transformation", "LinkedIn / Medium / HBR-Stil"),
]


def split_essays(text):
    parts = re.split(r"^## (Essay \d+ — .+)$", text, flags=re.M)
    out = []
    for i in range(1, len(parts), 2):
        head = parts[i].strip()
        body = parts[i + 1].strip()
        out.append((head, body))
    return out


def clean_figure(body):
    """FIGURE-Metadatenblock in eine saubere Abbildung mit Bildunterschrift umwandeln."""
    m = re.search(r"### Figure\s*\n(.*?)(?=\n### References)", body, re.S)
    if not m:
        return body
    fig = m.group(1)
    img = re.search(r"!\[.*?\]\((.*?)\)", fig)
    title = re.search(r"^title:\s*(.+)$", fig, re.M)
    caption = re.search(r"^caption:\s*(.+)$", fig, re.M)
    out = ["### Abbildung\n"]
    t = title.group(1).strip() if title else "Abbildung"
    if img:
        out.append(f"![{t}]({img.group(1)})\n")
    if title:
        out.append(f"**{t}**\n")
    if caption:
        out.append(f"> {caption.group(1).strip()}\n")
    return body[:m.start()] + "".join(out) + body[m.end():]


def count_words(md):
    # strip figure/refs blocks for a fair body word count
    body = re.split(r"### Figure", md)[0]
    body = re.sub(r"[`*#>|\-]", " ", body)
    return len([w for w in body.split() if w.strip()])


def main():
    text = open(SRC, encoding="utf-8").read()
    essays = split_essays(text)
    assert len(essays) == 6, f"erwartet 6 Essays, gefunden {len(essays)}"

    medium = json.load(open(MEDIUM, encoding="utf-8"))
    index = {e.get("id"): i for i, e in enumerate(medium)}

    replaced = 0
    for (head, body), (eid, title, cat, target) in zip(essays, ESSAYS):
        body = re.sub(r"\n---\s*$", "", body.strip()).strip()
        body = clean_figure(body)
        words = count_words(body)
        entry = {
            "id": eid,
            "title": title,
            "subtitle": head.split("—", 1)[1].strip() if "—" in head else head,
            "category": "Executive Essays",
            "status": "Fertig — Review",
            "target": target,
            "hasDraft": True,
            "outline": body,
            "outlineLines": len(body.split("\n")),
            "date": "2026-10-01",
            "words": words,
            "figure": True,
            "acta_report_id": "ACTA-2026-039",
            "tags": ["executive-essay", "hbr-stil", "acta", "v2"],
        }
        if eid in index:
            medium[index[eid]] = entry
            replaced += 1
            print(f"  ersetzt: {eid} ({words} Wörter)")
        else:
            medium.append(entry)
            print(f"  neu:     {eid} ({words} Wörter)")

    # DOI-Verifikationsbericht als eigener Eintrag (Nachvollziehbarkeit)
    doi_body = open(DOI_MD, encoding="utf-8").read()
    doi_id = "essays-doi-verification-2026-10-01"
    doi_entry = {
        "id": doi_id,
        "title": "DOI- und Referenz-Verifikation — Executive Essays",
        "subtitle": "45/45 Referenzen aufgelöst (DOI-Handle-API, 2026-10-01)",
        "category": "Research Papers",
        "status": "Fertig — Review",
        "target": "Interne Qualitätssicherung",
        "hasDraft": True,
        "outline": doi_body,
        "outlineLines": len(doi_body.split("\n")),
        "date": "2026-10-01",
        "tags": ["quellenprüfung", "doi", "apa7", "executive-essays"],
    }
    if doi_id in index:
        medium[index[doi_id]] = doi_entry
        print(f"  ersetzt: {doi_id}")
    else:
        medium.append(doi_entry)
        print(f"  neu:     {doi_id}")

    json.dump(medium, open(MEDIUM, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\nmedium_articles.json: {len(medium)} Einträge geschrieben")


if __name__ == "__main__":
    main()
