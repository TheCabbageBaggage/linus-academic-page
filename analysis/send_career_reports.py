#!/usr/bin/env python3
"""
Versendet die 5 ACTA-Karriere-Berichte (PDF) an Linus.

Absender:  Clowie Claw <claw.clowie@gmail.com>   (HARTE REGEL)
An:        kohl.linus@gmail.com
Kein CC (Mail geht an Linus selbst).
HTML-Mail mit ACTA-Design + 5 PDF-Anhänge.
"""

import base64
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TOKEN = "/data/.config/gogcli/tokens_clowie.json"
TO_EMAIL = "kohl.linus@gmail.com"
FROM_EMAIL = "claw.clowie@gmail.com"
FROM_NAME = "Clowie Claw"
CLIENT_ID = "346557089211-umshm9dqdub0bgq9p8nd4hlj5vghng76.apps.googleusercontent.com"

REPORTS_DIR = ("/data/.openclaw/workspace/projects/linus-academic-page/"
               "analysis/acta_reports")

SUBJECT = ("ACTA-Berichte: Strategische Karriere- & Paper-Analysen "
           "(ACTA-2026-033 bis -037)")

ATTACHMENTS = [
    "ACTA-2026-033_roadmap.pdf",
    "ACTA-2026-034_review-pass2.pdf",
    "ACTA-2026-035_review-pass1.pdf",
    "ACTA-2026-036_paper-1.pdf",
    "ACTA-2026-037_paper-4.pdf",
]

HTML = """<!DOCTYPE html>
<html lang="de"><head><meta charset="UTF-8"></head>
<body style="margin:0;padding:0;background:#F5F6F7;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#1A1A1A;">
<div style="max-width:680px;margin:0 auto;background:#ffffff;">

  <div style="padding:28px 32px 20px 32px;border-bottom:3px solid #2C5F7C;">
    <div style="font-size:38px;font-weight:700;color:#2C5F7C;letter-spacing:-0.5px;">ACTA</div>
    <div style="font-size:13px;color:#8A9BA8;font-style:italic;margin-top:2px;">Analysen &middot; Strategie &middot; Dokumentation</div>
  </div>

  <div style="padding:28px 32px;">
    <h1 style="font-size:20px;color:#2C5F7C;margin:0 0 6px 0;line-height:1.25;">
      Strategische Karriere- &amp; Paper-Analysen
    </h1>
    <p style="font-size:12px;color:#8A9BA8;margin:0 0 22px 0;">
      Fünf ACTA-Berichte &middot; ACTA-2026-033 bis ACTA-2026-037 &middot; 18.09.2026
    </p>

    <p style="font-size:14px;line-height:1.6;margin:0 0 18px 0;text-align:justify;">
      Alle Ausarbeitungen der Codex-Analysen liegen jetzt als ACTA-Berichte vor &mdash;
      je als PDF im Anhang, konsistent im Petroleum-Design, mit Berichtsnummer,
      Executive Summary, Literaturverzeichnis (APA7) und EU-AI-Act-Transparenzhinweis.
      Zusätzlich sind sie auf ClawHub abgelegt und dauerhaft abrufbar.
    </p>

    <table style="width:100%;border-collapse:collapse;font-size:13px;margin:0 0 22px 0;">
      <thead>
        <tr style="background:#2C5F7C;color:#fff;">
          <th style="text-align:left;padding:8px 10px;border:0.5px solid #8A9BA8;">Nr.</th>
          <th style="text-align:left;padding:8px 10px;border:0.5px solid #8A9BA8;">Bericht</th>
          <th style="text-align:left;padding:8px 10px;border:0.5px solid #8A9BA8;">Umfang</th>
        </tr>
      </thead>
      <tbody>
        <tr><td style="padding:8px 10px;border:0.5px solid #8A9BA8;font-weight:700;color:#1A3440;">ACTA-2026-033</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">Strategische Roadmap 2026&ndash;2029</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">2.948 W&ouml;rter</td></tr>
        <tr style="background:#F5F6F7;"><td style="padding:8px 10px;border:0.5px solid #8A9BA8;font-weight:700;color:#1A3440;">ACTA-2026-034</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">Paper-Strategie vs. GM-Pfad (Pass 2)</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">2.414 W&ouml;rter</td></tr>
        <tr><td style="padding:8px 10px;border:0.5px solid #8A9BA8;font-weight:700;color:#1A3440;">ACTA-2026-035</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">Kritische Analyse Paper-Strategie / Medium / GM (Pass 1)</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">3.454 W&ouml;rter</td></tr>
        <tr style="background:#F5F6F7;"><td style="padding:8px 10px;border:0.5px solid #8A9BA8;font-weight:700;color:#1A3440;">ACTA-2026-036</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">Paper 1 &mdash; Vibe Coding in Regulated Industry (Outline)</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">2.565 W&ouml;rter</td></tr>
        <tr><td style="padding:8px 10px;border:0.5px solid #8A9BA8;font-weight:700;color:#1A3440;">ACTA-2026-037</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">Paper 4 &mdash; Vibe Coding and the SME (Outline, zur&uuml;ckgestellt)</td>
            <td style="padding:8px 10px;border:0.5px solid #8A9BA8;">2.188 W&ouml;rter</td></tr>
      </tbody>
    </table>

    <div style="background:#F5F6F7;border-left:4px solid #3D8B8B;padding:14px 18px;margin:0 0 22px 0;">
      <div style="font-weight:700;color:#1A3440;font-size:13px;margin-bottom:6px;">Kernbefund in einem Satz</div>
      <div style="font-size:13px;line-height:1.55;color:#2D3436;">
        Nicht die Kompetenz ist die Engstelle, sondern die Zuschreibung &mdash; und vier
        Governance-Papers verst&auml;rken genau das Spezialistenlabel, aus dem du heraus willst.
        Der st&auml;rkste Hebel ist Salesforce/Forecast als S&amp;OP- und
        Working-Capital-Mandat mit gemeinsamem KPI, nicht ein weiterer Digitaltitel.
      </div>
    </div>

    <div style="font-size:13px;line-height:1.6;margin:0 0 8px 0;">
      <strong style="color:#1A3440;">Ablage auf ClawHub:</strong><br>
      &middot; Research-Katalog &mdash; Kategorien <em>Strategie &amp; Karriere</em> und <em>Paper Outlines</em><br>
      &middot; Medium &mdash; Kategorien <em>Strategy &amp; Career</em>, <em>Paper Strategy</em>,
        <em>Vibe Coding &amp; Governance</em> (Volltext im Modal abrufbar)<br>
      &middot; Direkt: <a href="https://clawhub.cabbagebaggage.net/medium" style="color:#2C5F7C;">clawhub.cabbagebaggage.net/medium</a>
    </div>
  </div>

  <div style="padding:18px 32px 26px 32px;border-top:1px solid #8A9BA8;">
    <div style="font-size:10.5px;color:#8A9BA8;font-style:italic;line-height:1.5;text-align:justify;">
      Alle Berichte wurden automatisiert durch Clowie Claw (OpenClaw) erstellt; die
      inhaltliche Analyse stammt von OpenAI Codex (gpt-5.5). Transparenzhinweis gem.
      Verordnung (EU) 2024/1689 (EU-AI-Act), Art. 50: KI-generierter Inhalt.
      Gehaltsb&auml;nder, Wahrscheinlichkeiten und Markteinsch&auml;tzungen sind indikative
      Sch&auml;tzungen &mdash; keine Rechts-, Steuer- oder Arbeitsberatung. Keine Haftung
      f&uuml;r Entscheidungen auf Basis dieser Berichte.
    </div>
    <div style="font-size:10.5px;color:#8A9BA8;text-align:center;margin-top:12px;">
      ACTA &middot; ACTA-2026-033 &ndash; ACTA-2026-037 &middot; 18.09.2026
    </div>
  </div>
</div>
</body></html>
"""


def load_token():
    return json.load(open(TOKEN))


def save_token(d):
    with open(TOKEN, "w") as f:
        json.dump(d, f)


def refresh_if_needed(tok):
    if tok.get("expires_at", 0) - time.time() > 120:
        return tok
    data = urllib.parse.urlencode({
        "client_id": tok.get("client_id", CLIENT_ID),
        "client_secret": tok.get("client_secret", ""),
        "refresh_token": tok["refresh_token"],
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(req) as r:
        resp = json.load(r)
    tok["access_token"] = resp["access_token"]
    tok["expires_at"] = time.time() + resp.get("expires_in", 3600)
    save_token(tok)
    return tok


def send(tok, msg):
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    body = json.dumps({"raw": raw}).encode()
    req = urllib.request.Request(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages/send",
        data=body, method="POST")
    req.add_header("Authorization", f"Bearer {tok['access_token']}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.read().decode()[:800])
        raise


def main():
    missing = [a for a in ATTACHMENTS if not os.path.exists(os.path.join(REPORTS_DIR, a))]
    if missing:
        print("FEHLT:", missing)
        return 1

    tok = refresh_if_needed(load_token())

    msg = MIMEMultipart("mixed")
    msg["From"] = f"{FROM_NAME} <{FROM_EMAIL}>"
    msg["To"] = TO_EMAIL
    msg["Subject"] = SUBJECT

    alt = MIMEMultipart("alternative")
    alt.attach(MIMEText(HTML, "html", "utf-8"))
    msg.attach(alt)

    total = 0
    for name in ATTACHMENTS:
        path = os.path.join(REPORTS_DIR, name)
        with open(path, "rb") as f:
            part = MIMEBase("application", "pdf")
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment", filename=name)
        msg.attach(part)
        size = os.path.getsize(path)
        total += size
        print(f"  + {name} ({size/1024:.0f} KB)")

    res = send(tok, msg)
    print(f"Gesendet. id={res.get('id')} threadId={res.get('threadId')} "
          f"Anhänge={len(ATTACHMENTS)} gesamt={total/1024:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
