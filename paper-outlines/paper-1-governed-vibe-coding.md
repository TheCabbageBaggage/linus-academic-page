# Paper 1 — Vibe Coding in Regulated Industry: A Governed Experimentation Framework

> **Status:** Working paper — outline v1 | **Target:** 9,000–11,000 words (journal) / 12–14 pages (conference)
> **Lead paper.** This is the flagship. It is the only one of the three that should be written to completion before the others begin.
> **Venue:** ICIS · ECIS · *Business & Information Systems Engineering* (BISE)
> **Method:** Design Science Research (DSR) — the same paradigm as the ARCHIE dissertation
> **Co-author target:** TU Wien (Ansari / Sihn / Reisinger) for DSR rigour and reviewer dialogue

---

## 1. Abstract (draft)

Agentic code generation ("vibe coding") lets domain experts build functioning software in hours, and industrial organisations are adopting it faster than their governance functions can respond. Existing compliance instruments — EU AI Act Art. 6 (high-risk classification), IEC 62443, ISO/IEC 27001, SOX-style change management — were authored before a model could generate an internal tool whose logic no human can fully reconstruct. The result is a governance vacuum: teams either block vibe coding outright (and lose the innovation) or permit it unmanaged (and lose the audit trail). We present a Design Science Research artefact — a two-track governance model that separates a sandboxed **experimental lane** from a hardened **promotion lane** — built and evaluated in the digitalisation function of a European heavy-industry group. The artefact's core novelty is an explicit **promotion gate**: a documented, testable set of criteria (provenance logging, model/version pinning, accountable human owner, data-zone compliance, reproducibility statement) that a vibe-coded tool must satisfy before production use. We further propose a **rewrite-threshold model** that indicates when the cost of human review exceeds the cost of disciplined re-implementation — a decision point largely absent from the literature. Evaluation draws on three real promotion decisions from the case organisation and structured assessment against DSR evaluation criteria. The contribution is operational: it renders vibe coding auditable without rendering it inert.

**Keywords:** vibe coding, generative AI, AI governance, EU AI Act, design science research, industrial digitalisation, compliance, software provenance

---

## 2. Introduction

### 2.1 Opening hook
A maintenance planner at a steel plant writes a small Python script with an LLM to reconcile spare-part lists across two ERP exports. It works. It saves four hours a week. It is also, from the perspective of an ISO 27001 auditor, an undocumented production system processing business-critical data with no owner, no change log, and no reproducible build. Multiply this by a hundred motivated employees and the governance question stops being hypothetical.

### 2.2 Status quo
The dominant organisational responses cluster into two failure modes:
- **Prohibition by default.** IT security and audit functions block generative coding tools, citing provenance, licensing, and data-leakage risk. Innovation moves to shadow IT.
- **Unmanaged permissiveness.** Tools are enabled org-wide with a usage policy, but no mechanism connects the produced code to the compliance regime. Audit findings accumulate quietly.

### 2.3 The gap
The vibe-coding discourse (Karpathy's original coinage onward, and the practitioner literature that followed) is written almost entirely for venture-backed software teams. It assumes the deployer owns their risk appetite end-to-end. It is silent on the case where the deployer is an industrial firm subject to external audit, product-liability regimes, and the EU AI Act's high-risk obligations. Meanwhile the AI-governance literature (risk registers, model cards, AI management systems per ISO/IEC 42001) is built for *procured* AI systems, not for *organically generated* code artefacts. Nobody has published a governance mechanism that sits between the two.

**Precise gap statement:** There exists no validated artefact that allows an industrial organisation to permit high-velocity AI code generation by non-developers while preserving a defensible audit trail and a clear chain of accountability.

### 2.4 Research questions
- **RQ1** — What are the concrete compliance failure points that arise when AI-generated code enters a regulated industrial environment?
- **RQ2** — What artefact design permits high-velocity experimentation while maintaining an audit-defensible record of every generated artefact?
- **RQ3** — Under which conditions should a generated artefact be promoted, reviewed, or rewritten?
- **RQ4** — How does the artefact perform against the DSR evaluation criteria in a real industrial setting?

### 2.5 Contribution
A DSR artefact (two-track model + promotion gate + rewrite-threshold model), instantiated and evaluated in a European heavy-industry group, with transferable design principles for other regulated sectors (energy, pharma, rail, finance-adjacent operations).

### 2.6 Roadmap
Sections 3–8: theoretical background, method, artefact design, instantiation, evaluation, discussion and limitations.

---

## 3. Theoretical & regulatory background

### 3.1 Vibe coding as a socio-technical phenomenon
Definition and boundary-setting. Distinguish three tiers, because the governance burden differs sharply:
- **T1 — Scripting assistance:** autocomplete and block-level generation inside an existing, reviewed codebase.
- **T2 — Component generation:** a full function or module generated and integrated into a maintained system.
- **T3 — Standalone tool generation:** a complete application generated and deployed by a domain expert outside the SDLC.

The governance literature treats these as one category. They are not. **Paper 1's scope is T3**, the genuinely ungoverned case.

### 3.2 The regulatory stack that applies
| Instrument | What it demands | Why generated code strains it |
|---|---|---|
| EU AI Act Art. 6 / Annex III | Risk classification, technical documentation, human oversight | A tool whose logic is model-generated may not have documented architecture |
| ISO/IEC 27001 A.8.25–A.8.34 | Secure development, change control, separation of environments | Vibe-coded tools bypass the change-control process entirely |
| IEC 62443 (OT/ICS) | Zone/conduit model, least privilege, patch discipline | Generated tools often bridge zones informally |
| GDPR Art. 25/32 | Data protection by design, processing records | Prompts and generated code may carry personal data |
| ISO/IEC 42001 (AI MS) | AI management system, roles, impact assessment | Designed for procured AI models, not ad-hoc code artefacts |
| Internal SOX-style controls | Segregation of duties, evidence retention | The generator and the deployer are frequently the same person |

### 3.3 Governance of AI vs. governance of *AI-generated artefacts*
Position the distinction: model governance (what model, what data, what evaluation) is comparatively mature; **artefact governance** (what did this specific generated thing do, who owns it, how do we prove it) is not. This is the paper's conceptual contribution to sit on.

### 3.4 Related work clusters
- DSR methodology (Hevner et al. 2004; Peffers et al. 2007; vom Brocke et al. 2020)
- Responsible AI / AI governance in organisations (Rai 2020; Mikalef et al. 2022)
- Shadow IT and citizen development (Silic & Back 2014; Rinta-Kahila et al.)
- Human-AI collaboration in knowledge work (author's own prior work: LLM-chatbot maintenance assistance, PHM)
- Software provenance and supply-chain integrity (SLSA, SBOM-as-analogy)

---

## 4. Research method

### 4.1 Design Science Research
Justify DSR over a survey or multiple-case study: the research question is *what should be built to solve this class of problem*, which is squarely DSR. Use **Peffers et al. (2007) DSRM** as the six-step process spine and **Hevner's (2004)** seven guidelines as the evaluation frame.

### 4.2 DSRM instantiation map
| DSRM activity | This study |
|---|---|
| 1. Problem identification | Compliance failure points observed in case organisation (RQ1) |
| 2. Objectives of a solution | Design requirements DR1–DR6 derived from §3.2 |
| 3. Design & development | Two-track model, promotion gate, rewrite-threshold model |
| 4. Demonstration | Three real promotion decisions |
| 5. Evaluation | Hevner criteria + practitioner/auditor assessment |
| 6. Communication | Journal submission + organisational rollout |

### 4.3 Design requirements (derived, not assumed)
- **DR1** — Must not require a security review before the first line of code is written (otherwise experimentation dies).
- **DR2** — Must produce a machine-readable provenance record at generation time, not retrofitted.
- **DR3** — Must identify exactly one accountable human owner per artefact.
- **DR4** — Must enforce a hard data-zone boundary: production/personal data never enters the experimental lane.
- **DR5** — Must be satisfiable by a non-developer (the whole point of T3).
- **DR6** — Must map to existing control frameworks to avoid creating a parallel compliance universe.

### 4.4 Case setting
European heavy-industry group; digitalisation and IT function; ~X hundred knowledge workers with access to generative coding tools. Anonymised at the level the organisation requires. Describe the OT/IT separation, the audit regime, and the existing change-management process.

### 4.5 Data collection
- Artefact usage telemetry from the experimental lane (N = XX artefacts over X months)
- Promotion-gate decision records (three analysed in depth)
- Semi-structured interviews: artefact authors (n≈10), IT security (n≈3), internal audit (n≈2), business owners (n≈5)
- Document analysis: existing policies, audit findings, control matrix

### 4.6 Evaluation strategy
Two-layer: **(a)** technical evaluation against DR1–DR6, **(b)** stakeholder evaluation through practitioner and auditor assessment (usefulness, ease of use, fit with audit expectations). Report explicitly on the negative case — what the artefact did *not* solve.

---

## 5. The artefact

### 5.1 Overview
Two lanes with a controlled boundary. Present as a diagram (Mermaid → PNG, per house standard).

```
                 ┌───────────────────────────────┐
   idea ────────▶│  EXPERIMENTAL LANE            │
                 │  · synthetic / public data    │
                 │  · auto-provenance capture    │
                 │  · no prod network access     │
                 │  · ephemeral by default       │
                 └──────────────┬────────────────┘
                                │  PROMOTION GATE
                                ▼
                 ┌───────────────────────────────┐
                 │  HARDENED LANE                │
                 │  · reviewed + owned           │
                 │  · version-pinned model       │
                 │  · logged, reproducible       │
                 │  · in change-management       │
                 └───────────────────────────────┘
```

### 5.2 Component A — Experimental lane
Design decisions and their rationale. Ephemerality as the default safety property: an artefact that is never persisted carries no compliance burden. What is logged (prompt, model+version, timestamp, author, data class touched) and why that is the minimum viable provenance set.

### 5.3 Component B — Promotion gate
The heart of the contribution. Six criteria, each testable and each traceable to a control in §3.2:

| # | Criterion | Evidence required | Maps to |
|---|---|---|---|
| G1 | Accountable human owner named | Named individual, role recorded | 27001 A.5.2, SOX segregation |
| G2 | Provenance record complete | Generation log + model/version pin | 42001, AI Act Art. 11 analogue |
| G3 | Data-zone compliance | Declaration of data classes used | GDPR Art. 30, 62443 zone model |
| G4 | Behaviour is bounded | Input/output constraints stated | 62443, safety case |
| G5 | Failure mode is understood | What happens when it breaks, who is paged | 27001 A.5.29 |
| G6 | Exit path exists | How it is decommissioned or rewritten | Change management |

A tool failing any criterion is *not rejected* — it stays experimental. The gate decides **promotion**, not existence. This framing is what keeps innovation alive and is the paper's key design insight.

### 5.4 Component C — Rewrite-threshold model
Formalise the decision most teams make instinctively. Define:
- `C_review` = cost to review, understand, and formally validate a generated artefact
- `C_rewrite` = cost to re-implement the same behaviour under normal SDLC discipline

Proposition: as artefact complexity and provenance incompleteness grow, `C_review` grows super-linearly while `C_rewrite` grows linearly. Therefore a **crossover point** exists beyond which disciplined rewriting is both cheaper *and* more auditable than attempting to validate generated code. Present as a conceptual model with illustrative parameters; note that empirical calibration is future work. (Flag honestly: this is a proposition, not a validated finding.)

### 5.5 Design principles (for generalisation)
DP1 — Ephemeral by default, persistent by promotion.
DP2 — Provenance at generation time, never retrofitted.
DP3 — One artefact, one accountable human.
DP4 — Gate the promotion, not the creation.
DP5 — Reuse existing control vocabulary instead of inventing a parallel one.

---

## 6. Demonstration — three promotion decisions

Present three real cases, anonymised, chosen for contrast:
- **Case A — promoted.** A data-reconciliation helper. Shows the gate working smoothly and cheaply.
- **Case B — rewritten.** A more complex generated tool where `C_review > C_rewrite`; illustrates the threshold model in action.
- **Case C — blocked at the gate.** A tool that failed G3 (data-zone) and could not be salvaged. Shows the gate has teeth.

For each: what was built, why it mattered to the business, which criteria applied, what evidence was produced, the decision, the outcome. Include the *time cost* of the gate — if complying takes two weeks, nobody will comply, and that number is itself a finding.

---

## 7. Evaluation

### 7.1 Against design requirements (DR1–DR6)
Table with verdict per requirement. Be honest about partial satisfaction — e.g. DR5 (non-developer satisfiability) is the most likely to be only partially met.

### 7.2 Against Hevner's seven guidelines
Explicit mapping, one short paragraph each.

### 7.3 Stakeholder evaluation
Theme the interview data: what authors found burdensome, what auditors found reassuring, where the two groups disagreed (there will be disagreement — that is a finding).

### 7.4 Threats to validity
Single-organisation instantiation; researcher is an organisational insider (address reflexivity honestly — this is both the study's greatest strength and its principal validity threat); no longitudinal data on audit outcomes yet.

---

## 8. Discussion

### 8.1 The compliance-load reframing
Develop the counterintuitive claim that a heavier compliance regime can push organisations toward *better* AI adoption, because automation of a regulated process inherits the full certification burden while augmentation of a still-accountable human does not. Connect to Paper 2's contingency model — state explicitly that Paper 1 provides the mechanism and Paper 2 tests the effect.

### 8.2 Relationship to the Leadership/Crowd/Lab model
The Lab gives the mandate to experiment; the promotion gate gives the mechanism to do it inside a regulated firm. Paper 1 is the missing operational layer beneath the Lab. Cite Mollick's essay as the practitioner framing this research operationalises.

### 8.3 Implications for practice
Five concrete recommendations for digitalisation leads in regulated industry, phrased as actions not concepts.

### 8.4 Limitations
Single case; insider researcher; calibration of the rewrite-threshold model is illustrative; regulatory landscape (AI Act implementation) still in motion.

---

## 9. Conclusion
Restate RQ1–RQ4 and answer each in one sentence. Restate the artefact and the design principles. Name the next study (Paper 2).

---

## References (seed list — complete during writing)
Hevner et al. 2004 · Peffers et al. 2007 · vom Brocke et al. 2020 · Gregor & Hevner 2013 · Rai 2020 · Mikalef et al. 2022 · Silic & Back 2014 · Karpathy 2025 (coinage) · Mollick 2025 · EU AI Act (Reg. 2024/1689) · ISO/IEC 27001:2022 · ISO/IEC 42001:2023 · IEC 62443 · plus author's own prior work (CIRP Annals 2021, 2023; PHM 2023; BISE-adjacent output)

---

## Writing plan
| Phase | Deliverable | Effort |
|---|---|---|
| 1 | Finalise gap + RQ, lock co-author | 15 h |
| 2 | §3 regulatory stack table + related work | 30 h |
| 3 | Artefact formalisation (gate + threshold model) | 35 h |
| 4 | Case write-ups from data | 30 h |
| 5 | Evaluation + discussion | 30 h |
| 6 | Polish, internal review, submit | 25 h |
| | **Total** | **~165 h** |

## Pre-writing blockers
1. **Co-author confirmed** — TU Wien. Without this, top-tier reviewers read it as a case report.
2. **IRB / voestalpine clearance** for using organisational data — before writing, not after.
3. **Media-relations sign-off** on whether the organisation is named or anonymised.
