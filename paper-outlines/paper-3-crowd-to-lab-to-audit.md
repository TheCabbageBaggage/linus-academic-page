# Paper 3 — From Crowd to Lab to Audit: An Institutional Model of AI Learning in Industrial Firms

> **Status:** Outline v1 | **Target:** 6,000–8,000 words (journal) / 8–10 pages (conference)
> **Venue:** *Journal of Management Information Systems* (JMIS) · *Information Systems Journal* · **CIRP CMS** (conference, faster path)
> **Method:** Conceptual development + DSR instantiation
> **Sequencing:** Third. Builds on Paper 1's artefact; can run in parallel with Paper 2 if capacity allows.
> **Co-author target:** TU Wien — this one is closest to the author's existing publication track (knowledge graphs, competence-based planning, CIRP)

---

## 1. Abstract (draft)

Organisations adopting generative AI commonly distribute experimentation across the workforce, following what has become known as a "Crowd-to-Lab" pattern: employees discover use cases, a dedicated team develops them further. The pattern has one structural weakness that its proponents do not address. It has no memory. When the crowd experiments, the organisation learns nothing durable; when people leave, the learning leaves with them; and nothing in the pattern produces evidence that would satisfy an external auditor. We argue that institutional AI learning in industrial firms requires a **knowledge-retention loop** that converts distributed experimentation into an organisational asset and an audit-defensible record simultaneously. Drawing on the design of knowledge-graph-based learning assistance systems for industrial maintenance and on a Design Science Research instantiation in a European heavy-industry group, we propose a six-stage learning loop — capture, link, grade, retain, expose, audit — and specify the graph schema that implements it. The artefact is evaluated against the requirements of institutional knowledge retention and against ISO/IEC 42001 documentation expectations. We find that the requirements of audit and the requirements of institutional memory are not merely compatible but largely identical, and that treating them as one system removes a substantial duplication of effort. The contribution extends the practitioner Crowd/Lab model into a form that survives staff turnover and external inspection.

**Keywords:** organisational learning, generative AI, knowledge graphs, design science research, institutional memory, AI management systems, ISO/IEC 42001

---

## 2. Introduction

### 2.1 Opening hook
A firm runs a successful AI experimentation programme for eighteen months. Two hundred use cases are identified. Twelve reach production. Then the person who designed the programme leaves — and nobody can reconstruct which use cases were tried, why nine-tenths of them were abandoned, or what conditions made the twelve successful ones work. The organisation spent eighteen months learning and retained almost none of it. It will make the same mistakes again next year.

### 2.2 The Crowd-to-Lab pattern and its silence
Recount the model as it is currently proposed: leadership sets direction, the crowd surfaces use cases, a lab develops them. It is a genuinely good model and it addresses the central strategic failure of treating AI as enterprise software. But it is a *throughput* description, not a *memory* description. It says how ideas flow. It says nothing about what is retained.

### 2.3 Three consequences of having no memory
1. **Learning loss.** Abandoned experiments are the most information-dense artefacts in the programme and are almost universally discarded.
2. **Turnover fragility.** Institutional AI knowledge concentrates in individuals, the exact failure mode KM research warned about for two decades.
3. **Audit exposure.** An auditor asking "how do you know this AI use case is safe?" receives an answer that depends on the continued employment of the person who built it.

### 2.4 The gap
The AI-adoption literature is rich on *how to start* and thin on *how to remember*. Knowledge-management literature has the memory machinery (ontologies, knowledge graphs, organisational memory systems) but was developed largely before generative AI changed the nature of what is being remembered — experiments, prompt patterns, failure modes, and governance decisions rather than documents and expertise directories. Nobody has connected the two for the industrial AI case.

**Precise gap statement:** No artefact exists that simultaneously satisfies the institutional-memory requirements of a firm running distributed AI experimentation and the documentation requirements of an external AI audit.

### 2.5 Research questions
- **RQ1** — What must be captured from distributed AI experimentation for the resulting learning to be institutionally retained?
- **RQ2** — What artefact design makes that capture automatic rather than an administrative afterthought?
- **RQ3** — To what extent do the requirements of institutional memory and of audit convergence on a common representation?
- **RQ4** — How does the artefact perform against ISO/IEC 42001 documentation expectations?

### 2.6 Contribution
A six-stage learning loop, a graph schema implementing it, a validated convergence claim (memory ≈ audit evidence), and a DSR instantiation in industry. The paper is deliberately positioned as the *institutional* counterpart to practical adoption frameworks.

### 2.7 Roadmap

---

## 3. Theoretical background

### 3.1 Organisational memory and learning
Walsh & Ungson's organisational memory; Nonaka & Takeuchi's SECI; Argote's organisational learning. Key carryover concepts: retention bins, the distinction between individual and organisational knowledge, and the observation that *forgetting* requires no effort while *remembering* does.

### 3.2 Knowledge graphs as memory substrate
Graph-based institutional memory: entities, relations, provenance. Justify the choice over alternatives (document repositories, wikis, embeddings-only). The argument: audits ask *relational* questions ("who approved this, under what evidence, and what depended on it"), and relational questions require a relational representation. Embeddings retrieve; graphs substantiate.

### 3.3 The author's prior track record (positioning, not vanity)
This paper sits directly on the author's published work — knowledge graph learning assistance (2024), competence-based planning (CIRP 2023), explainable event extraction (2025). State plainly that the novelty is transposing a proven industrial maintenance pattern onto the AI-experimentation domain, and that this is a *legitimate and strong* contribution type, not a thin one.

### 3.4 AI management systems and documentation obligations
ISO/IEC 42001's documentation expectations; EU AI Act Art. 11/12 (technical documentation and logging); how these are typically satisfied today (static documents, annual reviews) and why that is structurally mismatched to a domain where the relevant artefacts change weekly.

### 3.5 Related work
- AI adoption frameworks and practitioner models
- Organisational memory systems
- Knowledge graphs in industrial/manufacturing (own work + others)
- Shadow-AI and hidden-use detection
- Audit and accountability in algorithmic systems

---

## 4. Method

### 4.1 Design approach
Conceptual development first (the loop and schema), then DSR instantiation to demonstrate feasibility and evaluate. Be explicit that the conceptual contribution stands independently of the instantiation, which is a common and defensible structure in IS journals.

### 4.2 Design requirements
- **DR1** — Capture must not require the experimenter to do extra work (capture-at-source, or it will not happen).
- **DR2** — The representation must answer auditor-style relational queries directly.
- **DR3** — The schema must accommodate failure and abandonment as first-class outcomes, not just successes.
- **DR4** — Provenance must be preserved across later modification of an entry.
- **DR5** — The representation must survive the departure of the person who created the entry.
- **DR6** — The system must remain useful to the experimenter, not only to the auditor — otherwise adoption fails.

DR6 is the design's hardest constraint and deserves explicit discussion: memory systems that serve only compliance are abandoned within a year.

### 4.3 Case setting and data
Industrial group; AI experimentation programme; approximately [N] experiment records collected over [X] months. Data sources: experiment logs, promotion-gate decisions (from Paper 1), interview data from participants, and the retrospective query test described below.

### 4.4 Evaluation — the retrospective query test
The distinctive evaluation design: compile a set of **auditor-style questions** (n≈20) that a real internal auditor or regulator might pose about the firm's AI use ("Which AI tools process personal data?" "Who approved this and on what evidence?" "What happens to this tool if its author leaves?"). Then measure the time and completeness with which each can be answered (a) from the current document-based state, (b) from the graph instantiation. This is a concrete, quantitative, and unusually convincing evaluation for a conceptual paper.

### 4.5 Convergence analysis
Systematically map each schema element to the specific control or documentation obligation it satisfies, demonstrating the claimed memory/audit convergence rather than asserting it.

---

## 5. The artefact

### 5.1 The six-stage learning loop

```
  CAPTURE ──▶ LINK ──▶ GRADE ──▶ RETAIN ──▶ EXPOSE ──▶ AUDIT
     ▲                                                  │
     └──────────────── feedback into new experiments ────┘
```

- **Capture** — automatic from the experimentation environment (Paper 1's provenance log is the input). Zero extra effort.
- **Link** — connect each experiment to the problem it addressed, the process it touched, the people involved, and the regulatory regime that applies. This is where the graph earns its keep.
- **Grade** — record the outcome, including *abandoned* and *why*. Abandonment rationale is the single most valuable and most commonly discarded datum.
- **Retain** — persist with provenance, versioned, independent of the individual who authored it.
- **Expose** — surface the memory back to practitioners as *reuse suggestions* ("someone tried this in 2024 — here is what happened"). This is the stage that makes the system adopted rather than resented.
- **Audit** — answer relational compliance queries directly from the retained structure.

Note the loop closure: the memory feeds new experiments, which is what distinguishes organisational learning from an archive.

### 5.2 Graph schema
Present the entity types and relations explicitly:

**Entities:** `Experiment` · `Problem` · `Process` · `Person` · `RegulatoryRegime` · `Artefact` · `Outcome` · `Evidence` · `Control`

**Key relations:** `addresses`, `applied_to`, `authored_by`, `owned_by`, `subject_to`, `produced`, `resulted_in`, `evidenced_by`, `satisfies`, `supersedes`, `reused_by`

Note that `supersedes` and `reused_by` are what give the graph a temporal dimension that flat document stores lack — and that audits are frequently about *history*, not state.

### 5.3 Mapping memory requirements to audit obligations
The convergence table — the paper's central evidentiary claim:

| Schema element | Institutional-memory purpose | Audit/documentation obligation satisfied |
|---|---|---|
| `Experiment` + provenance | Retain what was tried and how | AI Act Art. 11 technical documentation analogue |
| `Outcome` (incl. abandoned) | Avoid repeating failures | AI Act Art. 12 logging; 42001 continual improvement |
| `owned_by` | Survive turnover | 42001 roles & responsibilities; 27001 A.5.2 |
| `subject_to` | Know which regime applies | AI Act risk classification; 62443 zone model |
| `evidenced_by` | Justify decisions post-hoc | 42001 evidence retention; SOX-style audit trail |
| `supersedes` | Preserve decision history | Change-management records |

The claim: **every memory requirement has a corresponding audit obligation, and vice versa.** That is why maintaining two systems is waste.

### 5.4 Design principles
DP1 — Capture at source or not at all.
DP2 — Abandonment is data.
DP3 — Memory must serve the practitioner before it serves the auditor.
DP4 — Represent relations, not documents; audits ask relational questions.
DP5 — Preserve history, not just current state.

---

## 6. Demonstration & evaluation

### 6.1 Instantiation
Describe the implementation: schema, population process, tooling. Note where it was simpler or harder than expected.

### 6.2 Retrospective query test results
Present the auditor-question benchmark. Report per-question completeness and time-to-answer for both conditions. This table is the paper's strongest empirical content — make it prominent.

### 6.3 Practitioner reception
What experimenters actually thought. Address DR6 directly: did anyone use the exposure stage voluntarily? If not, report that honestly and treat it as a design failure requiring iteration.

### 6.4 Against ISO/IEC 42001
Structured assessment of how the artefact supports each relevant clause. Note where it does *not* help — claiming full coverage would be implausible.

### 6.5 Threats to validity
Single instantiation; the researcher designed both the artefact and the evaluation (mitigate with external auditor participation in constructing the question set — this is important and should be arranged in advance).

---

## 7. Discussion

### 7.1 The convergence thesis generalised
If memory and audit converge for AI experimentation, does the same hold for other domains (quality management, safety cases)? Speculative but generative — a good source of future-work and citation potential.

### 7.2 Completing the practitioner model
The Crowd-to-Lab pattern describes idea throughput. The learning loop describes retention. Together they form a complete institutional model. State this as the paper's relationship to the practitioner discourse, with explicit reference to Mollick's Lab concept.

### 7.3 Why firms do not do this
Honest engagement with the adoption problem: retention requires sustained effort with deferred payoff, in direct tension with how AI programmes are funded and measured. Name this as the real barrier — it is organisational, not technical.

### 7.4 Limitations
Conceptual-plus-single-case; no longitudinal evidence that retained memory actually improved later decisions (identify as the obvious next study); schema complexity may not survive contact with a less structured domain.

---

## 8. Conclusion
Answer RQ1–RQ4. State the loop, the schema, and the convergence claim. Name the next study: a longitudinal test of whether the retention loop changes subsequent decisions (that would be Paper 5, and it is a genuinely strong one).

---

## References (seed list)
Walsh & Ungson 1991 · Nonaka & Takeuchi 1995 · Argote & Miron-Spektor 2011 · Alavi & Leidner 2001 · Hogan et al. (graph-based KM) · Hevner et al. 2004 · Peffers et al. 2007 · Mollick 2025 · ISO/IEC 42001:2023 · ISO/IEC 27001:2022 · EU AI Act Art. 11/12 · plus the author's own: knowledge graph learning assistance 2024, explainable event extraction 2025, competence-based planning CIRP 2023, text mining CIRP 2021

---

## Writing plan
| Phase | Deliverable | Effort |
|---|---|---|
| 1 | Conceptual loop + schema formalisation | 30 h |
| 2 | Convergence mapping (schema ↔ controls) | 20 h |
| 3 | Instantiation + population | 25 h |
| 4 | Retrospective query test design & execution | 35 h |
| 5 | Evaluation + 42001 assessment | 25 h |
| 6 | Write-up + submission | 35 h |
| | **Total** | **~170 h** |

## Pre-writing blockers
1. **External auditor involvement in the question-set design** — without it, the evaluation looks self-serving and reviewers will say so. Arrange early.
2. **Paper 1's provenance log in place** — the capture stage depends on it.
3. **Decide journal vs. CIRP CMS first** — CMS accepts a shorter version and gets a citation on the board within months. Given the author's existing CIRP track, publishing the conference version first and the journal version after is the pragmatic sequence.
