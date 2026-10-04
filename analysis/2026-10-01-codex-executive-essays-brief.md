# Codex Brief — Six Executive Essays (HBR style), 2026-10-01

## Role
Act as a senior editor for Harvard Business Review with the analytical rigor of an
industrial innovation strategist and the sourcing discipline of an academic reviewer.
You write for C-level readers who scan, not study.

## Task
Write **six finished executive essays**, ready to publish, based on the six
outlines already prepared (below and in
`clawhub-dashboard/dashboard/briefing/data/medium_articles.json`, ids `essay-*`).

Author voice: **Dr. Linus Kohl**, Head of Digitalization & IT at an Austrian
heavy-industry group (voestalpine Krems) with a PhD in industrial engineering.
First-person practitioner-scholar. Never pompous, never "guru". Concrete, contrarian,
grounded in operations.

## Hard requirements (non-negotiable)

### 1. Style — HBR
- Length: **1,400–1,800 words** per essay (target counts given per outline).
- Structure: arresting hook (a scene, a number, a wrong belief) → the thesis in one
  sentence → 3–5 tight sections with subheads → an honest counterargument →
  "what to do Monday morning" implications → one memorable closing line.
- Short paragraphs. Concrete factory/enterprise detail. No bullet-point dumps as the
  main body — bullets only where genuinely a list.
- No fluff, no "in today's fast-paced world", no buzzword stacking.
- German-language essays: keep the working titles as given (English titles are fine —
  they are the brand), but write the **article body in German** unless the outline
  says otherwise. Subheads in German. Keep established technical terms in English
  (Agent, Copilot, Forecast, Working Capital) where that is how practitioners say it.

### 2. Citations — MUST BE VERIFIABLE (critical)
- Every factual claim, statistic, or attributed idea needs a source in the
  **References** section at the end of each essay.
- Format: APA-style, plus **DOI or URL**, plus venue, plus year. Example:
  Mollick, E. (2025). *Co-Intelligence: Living and Working with AI*. Portfolio. ISBN …
- **Never invent a source.** If you are not sure a source exists, either omit the
  claim or flag it inline as `[Quelle prüfen]` and list it under a
  "Zu verifizieren" block. A fabricated citation is a total failure.
- Prefer primary sources: peer-reviewed papers, official EU/institutional documents
  (EU AI Act regulation number, ISO/IEC standards), credible industry reports with a
  named publisher and year, and named books/articles.
- Where the source is standard knowledge with a stable identifier, give the identifier
  (e.g. Regulation (EU) 2024/1689; ISO/IEC 27001:2022; IEC 62443).
- Aim for **6–12 references per essay**. Quality over quantity.

### 3. Figures — one per essay (spec only; assets are generated downstream)
For each essay, output a **figure specification** in this exact block format:

```
FIGURE
id: fig-<essay-id>-1
type: chart|diagram
kind: <bar|line|stacked-bar|scatter|flow|layers|matrix|timeline|quadrant>
title: <figure title>
caption: <1–2 sentence caption, German>
alt: <accessibility alt text>
palette: acta-petroleum
data:            # for charts — real or clearly illustrative numbers with source note
 - label: ...
   value: ...
source_note: <"Illustrative" or a real source>
excalidraw_hint: <for diagrams: node/edge sketch in words, 6–12 nodes, 1–2 sentences>
```

- Mix the six: at least **two charts** (with data) and at least **two diagrams**.
- Charts must carry a `source_note`; if illustrative, say "Illustrativ" explicitly.
- Diagrams must be expressible as Excalidraw nodes/edges (they will be rendered as
  Excalidraw scenes + SVG).

### 4. Acta design compliance
- Figures use the Acta palette only: Petroleum #2C5F7C (primary), Deep Navy #1A3440,
  Teal #3D8B8B, Slate #8A9BA8, Charcoal #2D3436, Off-White #F5F6F7,
  Success #387359, Warning #CC9A33, Alert #BF3939. Font Helvetica.
- Do **not** write HTML/CSS. Write markdown; the renderer downstream handles layout.

## Output format
Produce ONE markdown file with six top-level sections, exactly in this shape:

```
# Executive Essays — Series

## Essay 1 — The Agentic Industrial Enterprise
<full essay body in markdown, with subheads>
### Figure
<FIGURE block>
### References
<APA list>

## Essay 2 — Everyone Can Build Software. What Is Corporate IT For?
...
```

Write the finished file to:
`/data/.openclaw/workspace/projects/linus-academic-page/analysis/2026-10-01-executive-essays.md`

## The six essays (authoritative outlines are in
`/data/.openclaw/workspace/projects/linus-academic-page/analysis/2026-10-01-essay-outlines-source.md` — READ THAT FILE FIRST and expand its argumentation lines)

1. **The Agentic Industrial Enterprise** — Agents become part of the operating model,
   not just new software tools. (central thought-leadership theme; ~1,650 words)
2. **Everyone Can Build Software. What Is Corporate IT For?** — When business units
   build software with AI, IT shifts from delivery to platform, architecture, governance.
   (~1,600 words)
3. **The Factory Manager of 2030 Will Manage Humans and Agents** — Leadership changes
   when digital agents take on operational tasks and decisions. (~1,550 words)
4. **Stop Counting AI Pilots. Measure Decisions.** — AI value comes from better/faster
   decisions and measurable business KPIs, not from the number of use cases.
   (~1,500 words)
5. **Why Industrial AI Needs Memory, Not Another Copilot** — Industry needs context,
   history, knowledge graphs and process knowledge, not isolated chatbots. (~1,700 words)
6. **From Digital Transformation to Industrial Transformation** — Digitalization must
   not be run as an IT program, but through OEE, cost, cash, quality and lead time.
   (~1,600 words)

## Autonomy
- Read `/data/.openclaw/workspace/projects/linus-academic-page/analysis/2026-10-01-essay-outlines-source.md` and, if reachable, the JSON entry for each id.
- Work autonomously. Do not ask questions. If a detail is uncertain, mark it
  `[Quelle prüfen]` rather than inventing it.
- Self-check before finishing: word counts in range; every essay has ≥6 references
  with DOI/URL; every essay has exactly one FIGURE block; no fabricated sources.
- If web access is available, verify the citations (DOIs resolve); if not, be
  conservative and flag uncertain ones.
- Exit criteria: the six essays are written to the output path, complete and
  self-consistent. Report the output path, per-essay word counts, and a list of any
  `[Quelle prüfen]` flags.
