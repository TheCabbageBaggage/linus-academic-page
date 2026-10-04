#!/usr/bin/env python3
"""Render the six executive-essay figures in the Acta palette.

Charts  -> PNG (matplotlib)
Diagrams-> SVG hand-built (layer/flow), Helvetica stack, Acta colours only.
Output: assets/fig-*.png / .svg  (referenced from the essays)
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

PETROLEUM = "#2C5F7C"
NAVY = "#1A3440"
TEAL = "#3D8B8B"
SLATE = "#8A9BA8"
CHARCOAL = "#2D3436"
OFFWHITE = "#F5F6F7"
SUCCESS = "#387359"
WARNING = "#CC9A33"
ALERT = "#BF3939"

FONT = "Liberation Sans"  # metric-compatible Helvetica substitute
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": [FONT, "Helvetica", "Arial", "DejaVu Sans"],
    "text.color": CHARCOAL,
    "axes.labelcolor": CHARCOAL,
    "xtick.color": CHARCOAL,
    "ytick.color": CHARCOAL,
    "axes.edgecolor": SLATE,
})

def _finish(ax, path, title):
    ax.set_facecolor(OFFWHITE)
    ax.figure.patch.set_facecolor(OFFWHITE)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(SLATE)
    ax.spines["bottom"].set_color(SLATE)
    ax.set_title(title, fontsize=11, fontweight="bold", color=NAVY, pad=12)
    ax.figure.tight_layout()
    ax.figure.savefig(path, dpi=200, facecolor=OFFWHITE)
    plt.close(ax.figure)
    print("wrote", path.name)

def barh(path, title, labels, values, colors, xlabel):
    fig, ax = plt.subplots(figsize=(9, 4.2))
    y = range(len(values))
    bars = ax.barh(list(y), values, color=colors, height=0.55, zorder=3)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel(xlabel, fontsize=9)
    ax.grid(axis="x", color=SLATE, alpha=0.25, zorder=0)
    for b, v in zip(bars, values):
        ax.text(b.get_width() + max(values) * 0.015, b.get_y() + b.get_height() / 2,
                f"{v:g}", va="center", fontsize=9, color=NAVY, fontweight="bold")
    _finish(ax, path, title)

def bar(path, title, labels, values, colors, ylabel):
    fig, ax = plt.subplots(figsize=(8.4, 4.2))
    x = range(len(values))
    bars = ax.bar(list(x), values, color=colors, width=0.5, zorder=3)
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_ylim(0, max(values) * 1.18)
    ax.grid(axis="y", color=SLATE, alpha=0.25, zorder=0)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + max(values) * 0.02,
                f"{v:g}", ha="center", fontsize=9, color=NAVY, fontweight="bold")
    _finish(ax, path, title)

# Essay 2 — Corporate IT (bar)
barh(OUT / "fig-essay-corporate-it-1.png",
     "Zeit bis zum belastbaren Betriebsentscheid",
     ["Individuelle Klärung\nohne vorbereiteten Pfad", "Vorbereiteter\nPlattformpfad"],
     [20, 8], [PETROLEUM, TEAL], "Arbeitstage (illustrativ)")

# Essay 4 — Measure Decisions (bar)
bar(OUT / "fig-essay-measure-decisions-1.png",
    "Vom Pilotportfolio zum prüfbaren Wertbeitrag",
    ["Gestartet", "mit Entscheidungs-\nOwner", "mit Baseline\nund Vergleich", "mit Nettoeffekt"],
    [20, 12, 7, 3], [PETROLEUM, TEAL, SUCCESS, NAVY], "Anzahl Projekte (illustrativ)")

# Essay 6 — Industrial Transformation (bar)
bar(OUT / "fig-essay-industrial-transformation-1.png",
    "Weniger Prozessbestand, kürzere Durchlaufzeit\nbei konstantem Durchsatz",
    ["1.000 Einheiten\nProzessbestand", "600 Einheiten\nProzessbestand"],
    [10, 6], [PETROLEUM, TEAL], "Mittlere Durchlaufzeit (Tage, illustrativ)")
# note: 2-bar version kept consistent with spec
print("charts done")
