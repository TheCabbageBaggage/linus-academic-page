#!/usr/bin/env python3
"""
ACTA-Berichte: Strategische Karriere- & Paper-Analysen (Codex, 2026-09)
=======================================================================
Erzeugt fünf ACTA-konforme Reports (HTML + PDF) aus den Codex-Analysen:

  R1  Strategische Roadmap 2026–2029
  R2  Paper-Strategie vs. General-Management-Pfad (Pass 2)
  R3  Kritische Analyse: Paper-Strategie, Medium-Artikel, GM-Positionierung (Pass 1)
  R4  Vibe Coding in Regulated Industry (Paper 1, Outline)
  R5  Vibe Coding & SME (Paper 4, Outline)

Jeder Bericht: Cover mit ACTA-YYYY-NNN, Executive Summary, Inhalt,
Fazit/Empfehlungen, Literaturverzeichnis (APA7), EU-AI-Act-Disclaimer.
"""

import html as _html
import os
import re
import subprocess
import sys
import unicodedata
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ACTA_DIR = "/data/.openclaw/workspace/acta/reporting"
sys.path.insert(0, ACTA_DIR)

from acta_registry import register_report  # noqa: E402

ANALYSIS = HERE
OUT = os.path.join(HERE, "acta_reports")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------------------
# Design-Tokens (ACTA Bericht-PALETTE — verbindlich)
# ---------------------------------------------------------------------------
PETROLEUM = "#2C5F7C"
DEEP_NAVY = "#1A3440"
TEAL = "#3D8B8B"
SLATE = "#8A9BA8"
CHARCOAL = "#2D3436"
OFF_WHITE = "#F5F6F7"
DARK_TEXT = "#1A1A1A"

FONT_STACK = ("-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, "
              "'Segoe UI', Roboto, Arial, sans-serif")

CSS = f"""
@page {{ size: A4; margin: 18mm 16mm 16mm 16mm; }}
* {{ box-sizing: border-box; }}
body {{
  font-family: {FONT_STACK};
  color: {DARK_TEXT}; font-size: 10.5pt; line-height: 1.55;
  margin: 0; padding: 0; background: #fff;
}}
.page {{ max-width: 190mm; margin: 0 auto; padding: 0; }}
@media screen {{ body {{ padding: 8mm 6mm; }} }}
.cover {{ padding-top: 6mm; }}
.brand {{ font-size: 44pt; font-weight: 700; color: {PETROLEUM}; letter-spacing: -0.5pt; }}
.brand-sub {{ font-size: 13pt; color: {SLATE}; font-style: italic; margin-top: 1mm; }}
hr.rule {{ border: 0; border-top: 3px solid {PETROLEUM}; margin: 7mm 0 8mm 0; }}
h1.doc-title {{ font-size: 22pt; color: {PETROLEUM}; margin: 0 0 3mm 0; line-height: 1.2; }}
p.doc-subtitle {{ font-size: 11pt; color: {SLATE}; margin: 0 0 8mm 0; }}
.cards {{ display: flex; gap: 4mm; flex-wrap: wrap; margin: 0 0 8mm 0; }}
.card {{
  background: {OFF_WHITE}; border-left: 3px solid {PETROLEUM};
  padding: 4mm 5mm; min-width: 38mm; flex: 1;
}}
.card .v {{ font-size: 17pt; font-weight: 700; color: {PETROLEUM}; line-height: 1.1; }}
.card .l {{ font-size: 8.5pt; color: {SLATE}; margin-top: 1mm; }}
.meta {{ font-size: 9pt; color: {CHARCOAL}; border-top: 1px solid {SLATE}; padding-top: 3mm; }}
.meta b {{ color: {DEEP_NAVY}; }}
h1 {{ font-size: 17pt; color: {PETROLEUM}; margin: 9mm 0 3mm 0; border-bottom: 2px solid {PETROLEUM};
      padding-bottom: 1.5mm; }}
h1.sec {{ page-break-before: always; }}
h2 {{ font-size: 12.5pt; color: {DEEP_NAVY}; margin: 6mm 0 2.5mm 0; }}
h3 {{ font-size: 11pt; color: {TEAL}; margin: 4.5mm 0 2mm 0; }}
p {{ margin: 0 0 2.8mm 0; text-align: justify; }}
ul, ol {{ margin: 0 0 3mm 0; padding-left: 6mm; }}
li {{ margin-bottom: 1.4mm; }}
strong {{ color: {DEEP_NAVY}; }}
blockquote {{
  margin: 3mm 0; padding: 3mm 4mm; background: {OFF_WHITE};
  border-left: 3px solid {TEAL}; font-style: italic; color: {CHARCOAL};
}}
blockquote p {{ margin: 0; }}
table {{ width: 100%; border-collapse: collapse; margin: 3mm 0 4mm 0; font-size: 8.5pt;
         table-layout: fixed; }}
th {{ background: {PETROLEUM}; color: #fff; text-align: left; padding: 1.6mm 2mm;
      font-weight: 600; border: 0.5px solid {SLATE}; word-wrap: break-word; }}
td {{ padding: 1.6mm 2mm; border: 0.5px solid {SLATE}; vertical-align: top;
      word-wrap: break-word; overflow-wrap: anywhere; }}
tr:nth-child(even) td {{ background: {OFF_WHITE}; }}
code {{ font-family: 'IBM Plex Mono', 'SF Mono', Menlo, monospace; font-size: 9pt;
        background: {OFF_WHITE}; padding: 0.4mm 1mm; border-radius: 2px; }}
pre {{ background: {OFF_WHITE}; border-left: 3px solid {SLATE}; padding: 3mm 4mm;
       overflow-wrap: anywhere; white-space: pre-wrap;
       font-family: 'IBM Plex Mono', 'SF Mono', Menlo, monospace; font-size: 8.5pt;
       margin: 3mm 0; }}
.callout {{ padding: 3.5mm 4.5mm; margin: 4mm 0; border-left: 4px solid {PETROLEUM};
            background: {OFF_WHITE}; font-size: 10pt; }}
.callout.warn {{ border-left-color: #CC9A33; }}
.callout.alert {{ border-left-color: #BF3939; }}
.callout.success {{ border-left-color: #387359; }}
.callout .t {{ font-weight: 700; color: {DEEP_NAVY}; display: block; margin-bottom: 1mm; }}
.lit {{ font-size: 9pt; }}
.lit p {{ padding-left: 6mm; text-indent: -6mm; margin-bottom: 2mm; }}
.disclaimer {{ font-size: 8pt; color: {SLATE}; font-style: italic; margin-top: 8mm;
               border-top: 1px solid {SLATE}; padding-top: 3mm; text-align: justify; }}
.footer-note {{ font-size: 8pt; color: {SLATE}; text-align: center; margin-top: 6mm; }}
</style>
"""


def esc(t: str) -> str:
    return _html.escape(t, quote=False)


def slug(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()[:60]


# ---------------------------------------------------------------------------
# Markdown -> HTML (Tabellen, Überschriften, Listen, Code, Blockquotes)
# ---------------------------------------------------------------------------
def md_to_html(md: str, offset_h1: bool = True) -> str:
    lines = md.split("\n")
    out, i = [], 0
    first_h1_seen = False

    def inline(s: str) -> str:
        s = esc(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\[([^\]]+)\]\((https?://[^\)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        # Code fence
        if s.startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append("<pre>" + esc("\n".join(buf)) + "</pre>")
            continue

        # Table
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in header)
            trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue

        # Headings
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl, txt = len(m.group(1)), m.group(2)
            if lvl == 1 and offset_h1:
                if not first_h1_seen:
                    first_h1_seen = True
                    out.append(f"<h1>{inline(txt)}</h1>")
                else:
                    out.append(f'<h1 class="sec">{inline(txt)}</h1>')
            elif lvl == 1:
                out.append(f"<h1>{inline(txt)}</h1>")
            else:
                out.append(f"<h{lvl}>{inline(txt)}</h{lvl}>")
            i += 1
            continue

        # HR
        if re.match(r"^-{3,}$", s):
            out.append(f'<hr class="rule" style="border-top:1px solid {SLATE}">')
            i += 1
            continue

        # Blockquote
        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(buf)) + "</blockquote>")
            continue

        # Lists
        if re.match(r"^[-*]\s+", s):
            buf = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                buf.append(re.sub(r"^[-*]\s+", "", lines[i].strip()))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(b)}</li>" for b in buf) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", s):
            buf = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                buf.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(b)}</li>" for b in buf) + "</ol>")
            continue

        if not s:
            i += 1
            continue

        # Paragraph
        buf = [s]
        i += 1
        while i < len(lines):
            nx = lines[i].strip()
            if (not nx or nx.startswith("#") or nx.startswith("|") or nx.startswith(">")
                    or nx.startswith("```") or re.match(r"^[-*]\s+", nx)
                    or re.match(r"^\d+\.\s+", nx) or re.match(r"^-{3,}$", nx)):
                break
            buf.append(nx)
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")

    return "\n".join(out)


def extract_h1(md: str) -> str:
    for ln in md.split("\n"):
        if ln.startswith("# "):
            return ln[2:].strip()
    return ""


def strip_first_h1(md: str) -> str:
    lines = md.split("\n")
    for idx, ln in enumerate(lines):
        if ln.startswith("# "):
            return "\n".join(lines[idx + 1:]).strip()
    return md.strip()


# ---------------------------------------------------------------------------
# Report-Bau
# ---------------------------------------------------------------------------
def build_report(report_id, doc_title, subtitle, source_md, metrics, meta,
                 exec_summary, closing, references, body_offset_h1=True):
    created = datetime.now(timezone.utc).strftime("%d.%m.%Y")
    body = md_to_html(strip_first_h1(source_md), offset_h1=body_offset_h1)

    cards = "".join(
        f'<div class="card"><div class="v">{esc(v)}</div><div class="l">{esc(l)}</div></div>'
        for v, l in metrics
    )

    esc_meta = "".join(f"<div><b>{esc(k)}:</b> {esc(v)}</div>" for k, v in meta.items())

    exec_html = md_to_html(exec_summary, offset_h1=False)
    closing_html = md_to_html(closing, offset_h1=False)
    lit_html = "".join(f"<p>{esc(r)}</p>" for r in references)

    return f"""<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8">
<title>{esc(doc_title)} — {report_id}</title>
<style>{CSS}</style></head><body>
<div class="page">

<div class="cover">
  <div class="brand">ACTA</div>
  <div class="brand-sub">Analysen · Strategie · Dokumentation</div>
  <hr class="rule">
  <h1 class="doc-title">{esc(doc_title)}</h1>
  <p class="doc-subtitle">{esc(subtitle)}</p>
  <div class="cards">{cards}</div>
  <div class="meta">
    {esc_meta}
    <div><b>Berichtsnummer:</b> {esc(report_id)}</div>
    <div><b>Erstellt:</b> {esc(created)}</div>
  </div>
</div>

<h1 class="sec">Executive Summary</h1>
{exec_html}

<h1 class="sec">Analyse</h1>
{body}

<h1 class="sec">Fazit &amp; Empfehlungen</h1>
{closing_html}

<h1 class="sec">Literaturverzeichnis</h1>
<div class="lit">{lit_html}</div>

<h1 class="sec">Disclaimer</h1>
<p class="disclaimer">
Dieser Bericht wurde durch ein KI-System (Clowie Claw, ein auf OpenClaw basierender
KI-Assistent) automatisiert erstellt und durch ein großes Sprachmodell (OpenAI Codex,
gpt-5.5) mitanalysiert. Inhalt im Sinne der Verordnung (EU) 2024/1689 (EU-AI-Act),
Artikel 50: <b>KI-generierter Inhalt — Transparenzhinweis.</b>
Erstellt am {esc(created)}, Berichtsnummer {esc(report_id)}.
Verantwortlich für Zweck und Verwendung: Linus Kohl (Auftraggeber), Clowie Claw (Erstellung).
Zweck: interne strategische Entscheidungsunterstützung. Der Bericht kann trotz sorgfältiger
Erstellung Fehler, Auslassungen oder veraltete Annahmen enthalten; insbesondere
Gehaltsbänder, Wahrscheinlichkeiten und Markteinschätzungen sind <b>indikative Schätzungen,
keine Rechts-, Steuer- oder Arbeitsberatung</b> und bedürfen der eigenständigen Verifikation.
Für Entscheidungen auf Basis dieses Berichts wird keine Haftung übernommen.
</p>

<div class="footer-note">ACTA · {esc(report_id)} · Seite {esc(str(1))}ff.</div>
</div></body></html>"""


def html_to_pdf(html_path, pdf_path):
    """HTML -> PDF via Playwright/Chromium (wie im ACTA-Standard)."""
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--no-sandbox"])
            pg = b.new_page()
            pg.goto("file://" + html_path, wait_until="load")
            pg.pdf(path=pdf_path, format="A4", print_background=True,
                   margin={"top": "14mm", "bottom": "14mm", "left": "14mm", "right": "14mm"})
            b.close()
        return True
    except Exception as e:
        print(f"  ! Playwright fehlgeschlagen: {e}")
        return False
