#!/usr/bin/env python3
"""
ACTA-2026-039 — Publikationsstrategie v2 (Codex gpt-6-sol, 2026-09-29)

Ein einzelner ACTA-Bericht aus:
  analysis/2026-09-29-codex-publikationsstrategie-v2.md

Reiht sich in die Serie ACTA-2026-033..037 ein (Karriere-/Paper-Analysen).
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from generate_career_reports import (  # noqa: E402
    OUT, build_report, html_to_pdf, register_report,
)

AUTHOR = "Clowie Claw"
CLIENT = "Linus Kohl"
RID = "ACTA-2026-039"

SRC = os.path.join(HERE, "2026-09-29-codex-publikationsstrategie-v2.md")
md = open(SRC, encoding="utf-8").read()

# Berichtsnummer im Quelltext auf 039 korrigieren (Doc wurde fuer 038 geschrieben)
md = md.replace("ACTA-2026-038", RID)


def extract(md, start_pat, end_pat):
    m = re.search(start_pat + r"(.*?)" + end_pat, md, re.S)
    return m.group(1).strip() if m else ""


exec_summary = extract(md, r"## Executive Summary für ACTA-2026-039\s*\n", r"\n## 1\.")

# Fazit/Schlussentscheidung
closing = extract(md, r"\*\*Schlussentscheidung:\*\*", r"\n## Anhang A")

# Literaturverzeichnis (APA7) -> Liste
lit_block = extract(md, r"## 7\. Literaturverzeichnis \(APA 7\)\s*\n", r"\n## Anhang A")
references = [ln.strip().lstrip("*").strip()
              for ln in lit_block.split("\n") if ln.strip()]
references = [re.sub(r"^\*\*|\*\*$", "", r) for r in references]

metrics = [
    ("6", "Executive Essays"),
    ("2", "wissenschaftliche Papers"),
    ("1.180 h", "realistischer Gesamtaufwand"),
    ("24–30", "Monate Planungshorizont"),
]

meta = {
    "Analyst": "OpenAI Codex (gpt-6-sol)",
    "Auftrag": "Linus Kohl",
    "Quelle": "Codex-Run 2026-09-29, gpt-6-sol",
    "Klassifikation": "Vertraulich",
}

html = build_report(
    RID,
    "Publikationsstrategie v2 — industrielle Steuerungsfähigkeit statt AI-Spezialistenlabel",
    "Sechs Executive Essays, zwei Papers und die Evidenz- und Aufwandslogik für ein GM-Zielbild",
    md, metrics, meta, exec_summary, closing, references,
)

hp = os.path.join(OUT, f"{RID}_publikationsstrategie.html")
pp = os.path.join(OUT, f"{RID}_publikationsstrategie.pdf")
open(hp, "w", encoding="utf-8").write(html)
ok = html_to_pdf(hp, pp)

# Registry
try:
    from acta_registry import get_report
    if not get_report(RID):
        raise LookupError
except Exception:
    register_report(
        title="Publikationsstrategie v2 — industrielle Steuerungsfähigkeit statt AI-Spezialistenlabel",
        report_type="strategieanalyse",
        author=AUTHOR, client=CLIENT,
        classification=meta["Klassifikation"], version="1.0",
        file_path=pp,
        metadata={"key": "publikationsstrategie-v2", "quelle": "2026-09-29-codex-publikationsstrategie-v2.md"},
    )

print(f"{RID}  pdf={'OK' if ok else 'FEHLT'}  {len(md.split())} Woerter  refs={len(references)}")
print("HTML:", hp)
print("PDF :", pp)
