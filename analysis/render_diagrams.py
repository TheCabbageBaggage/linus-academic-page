#!/usr/bin/env python3
"""Hand-built SVG diagrams (Acta palette) for essays 1, 3, 5."""
from pathlib import Path
OUT = Path(__file__).resolve().parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

PETROLEUM="#2C5F7C"; NAVY="#1A3440"; TEAL="#3D8B8B"; SLATE="#8A9BA8"
CHARCOAL="#2D3436"; OFFWHITE="#F5F6F7"; SUCCESS="#387359"; WARNING="#CC9A33"; ALERT="#BF3939"
FONT = "Helvetica Neue, Helvetica, Arial, Liberation Sans, sans-serif"

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def svg_open(w,h,title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="{FONT}"><title>{esc(title)}</title>'
            f'<rect width="{w}" height="{h}" fill="{OFFWHITE}"/>')

def txt(x,y,s,size=13,fill=CHARCOAL,weight="normal",anchor="start"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" '
            f'text-anchor="{anchor}">{esc(s)}</text>')

def box(x,y,w,h,fill,label,sub=None,stroke=None,tcol="#ffffff"):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" '
    s+=f'stroke="{stroke or fill}" stroke-width="1.2"/>'
    if sub:
        s+=txt(x+w/2,y+h/2-2,label,13,tcol,"bold","middle")
        s+=txt(x+w/2,y+h/2+15,sub,10,tcol,"normal","middle")
    else:
        s+=txt(x+w/2,y+h/2+5,label,13,tcol,"bold","middle")
    return s

def arrow(x1,y1,x2,y2,color=SLATE,dashed=False,w=1.8,marker="arr"):
    d=' stroke-dasharray="5 4"' if dashed else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d} '
            f'marker-end="url(#{marker})"/>')

def defs():
    return (f'<defs>'
            f'<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{SLATE}"/></marker>'
            f'</defs>')

# ---------- Essay 1: five layers ----------
W,H=880,560
s=svg_open(W,H,"Fünf Schichten einer verantworteten Entscheidungsschleife")+defs()
s+=txt(30,38,"Fünf Schichten einer verantworteten Entscheidungsschleife",16,NAVY,"bold")
layers=[
 (NAVY,  "1 · Menschliche Ergebnisverantwortung", "Business Owner, Eingriffsrecht, Eskalation"),
 (WARNING,"2 · Agent mit begrenzter Kompetenz",     "Informieren · empfehlen · vorbereiten"),
 (PETROLEUM,"3 · Überprüfbarer Kontext",            "Historie, Provenienz, Anlagenidentität"),
 (TEAL,   "4 · Betriebliche Systeme",               "ERP · MES · CMMS · PLM · OT"),
 (SUCCESS,"5 · Ergebnis und Feedback",              "beobachtetes Ergebnis → Lernschleife"),
]
y=70
for i,(c,main,sub) in enumerate(layers):
    s+=box(60,y,760,66,c,main,sub)
    if i<len(layers)-1:
        s+=arrow(440,y+66,440,y+92)
    y+=92
# feedback arrow right side
fx=846
s+=f'<path d="M820 {70+4*92+33} C {fx+22} {70+4*92+33}, {fx+22} {70+33}, 820 {70+33}" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arr)"/>'
s+=txt(700,300,"Feedback: Ergebnis → Verantwortung",10,TEAL,"bold")
s+='</svg>'
(OUT/"fig-essay-agentic-enterprise-1.svg").write_text(s,encoding="utf-8")
print("wrote fig-essay-agentic-enterprise-1.svg")

# ---------- Essay 3: nine-node flow ----------
W,H=960,520
s=svg_open(W,H,"Delegation endet nicht beim Freigabeknopf")+defs()
s+=txt(30,38,"Delegation endet nicht beim Freigabeknopf",16,NAVY,"bold")
bw,bh=176,62
row1=[("Störungsmeldung",PETROLEUM),("Kontext und Quellen",PETROLEUM),("Agentenvorschlag",PETROLEUM)]
row2=[("Fachperson entscheidet",NAVY),("Begrenzte Ausführung",PETROLEUM),("Ergebnisprüfung",TEAL)]
row3=[("Stop und Eskalation",ALERT),("Manueller Rückfallprozess",WARNING),("Gemeinsamer Lernreview",TEAL)]
xs=[40, 380, 720]
for i,(lab,c) in enumerate(row1):
    s+=box(xs[i],70,bw,bh,c,lab)
for i in range(2):
    s+=arrow(xs[i]+bw,70+bh/2,xs[i+1],70+bh/2)
for i,(lab,c) in enumerate(row2):
    s+=box(xs[i],200,bw,bh,c,lab)
s+=arrow(440,132,440,200)
s+=arrow(xs[0]+bw,231,xs[1],231)
s+=arrow(xs[1]+bw,231,xs[2],231)
for i,(lab,c) in enumerate(row3):
    s+=box(xs[i],330,bw,bh,c,lab)
s+=arrow(xs[0]+bw/2,262,xs[0]+bw/2,330)
s+=arrow(xs[0]+bw,361,xs[1],361)
s+=arrow(xs[1]+bw,361,xs[2],361)
s+=arrow(xs[2]+bw/2,262,xs[2]+bw/2,330)
# learning loop back
s+=arrow(808,392,808,440,TEAL,w=2)
s+=f'<path d="M808 440 L 40 440 L 40 101" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arr)"/>'
s+=txt(370,462,"Lernschleife: bestätigtes Ergebnis aktualisiert den Kontext",10,TEAL,"bold")
s+='</svg>'
(OUT/"fig-essay-factory-manager-2030-1.svg").write_text(s,encoding="utf-8")
print("wrote fig-essay-factory-manager-2030-1.svg")

# ---------- Essay 5: four layers ----------
W,H=880,500
s=svg_open(W,H,"Industrielles Gedächtnis als überprüfbarer Lernkreis")+defs()
s+=txt(30,38,"Industrielles Gedächtnis als überprüfbarer Lernkreis",16,NAVY,"bold")
layers=[
 (SLATE,    "1 · Betriebliche Quellen", "Handbücher · Ereignisse · Erfahrungsberichte"),
 (PETROLEUM,"2 · Kontext und Identität", "Anlage · Version · Zeitpunkt · Provenienz"),
 (TEAL,     "3 · Evidenz", "relevante Fundstellen, fachlich geprüft"),
 (NAVY,     "4 · Entscheidung", "begründet, nachvollziehbar, verantwortet"),
]
y=70
for i,(c,main,sub) in enumerate(layers):
    s+=box(60,y,760,64,c,main,sub)
    if i<len(layers)-1:
        s+=arrow(440,y+64,440,y+90)
    y+=90
s+=f'<path d="M820 {70+3*90+32} C {866} {70+3*90+32}, {866} {70+2*90+32}, 820 {70+2*90+32}" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arr)"/>'
s+=txt(690,290,"Feedback aktualisiert Evidenz, nicht Häufigkeit",10,TEAL,"bold")
s+='</svg>'
(OUT/"fig-essay-industrial-memory-1.svg").write_text(s,encoding="utf-8")
print("wrote fig-essay-industrial-memory-1.svg")
print("diagrams done")
