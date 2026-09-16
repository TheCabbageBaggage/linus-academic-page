# Paper 4 — Vibe Coding and the SME: Democratised Innovation with Guardrails

> **Status:** Outline v1 (scoped, deliberately deferred) | **Target:** 6,000–8,000 words
> **Venue:** *Journal of Small Business Management* · *Technovation* · applied/transfer venue
> **Method:** Multiple case study (SMEs) + adaptation of Paper 1's artefact
> **Sequencing:** **Fourth — do not start before Paper 1 is accepted.** The SME context requires a framework that has already been validated in the large-firm case; writing it in parallel risks producing four half-arguments instead of one real contribution.
> **Co-author target:** TU Wien (this is largely a Master's-thesis-shaped project — a strong vehicle for a supervised thesis student)

---

## 1. Abstract (draft)

Small and medium enterprises face a version of the generative-AI governance problem that is structurally different from the large-firm case. They have no IT department to block or enable tools, no internal auditor to demand evidence, no AI management system, and no compliance function — but they are subject to the same EU AI Act obligations as any other deployer, and they carry the same data-protection exposure. At the same time they possess what large firms struggle to recreate: an owner-operator who is personally accountable, close to the work, and able to make decisions in days rather than quarters. We ask whether the governance artefact developed for regulated large firms can be reduced to an SME-viable form, and what must change when the accountable party is the firm's owner rather than a named employee. Based on [n] case studies of DACH SMEs using generative coding tools, we propose an SME-specific variant of the two-track governance model in which the accountability mechanism is the owner's signature and the audit trail is a single structured record rather than a control framework. The contribution is a genuinely lightweight guardrail model for firms that will never build a governance function.

**Keywords:** SME, generative AI, vibe coding, governance, EU AI Act, owner-operator accountability, technology adoption

---

## 2. Introduction

### 2.1 Opening hook
A twelve-person engineering office generates an internal tool with an LLM that quotes jobs from historical drawings. It works, and it materially improves margins. The owner has never heard of the EU AI Act, has no data-processing record for the tool, and does not know that the tool has become part of how the business makes decisions about customers. Nothing is wrong yet. Everything is undocumented.

### 2.2 Why the SME case is not just "smaller"
The distinction is structural, not one of scale:
| Dimension | Large regulated firm | SME |
|---|---|---|
| Who blocks/gates | IT security, audit, legal | Nobody — the owner decides |
| Accountability | Named employee in a role | The owner, personally |
| Compliance apparatus | Frameworks, control matrices | None |
| Decision latency | Weeks to quarters | Hours to days |
| Failure cost | Audit finding, fine | Existential — the business is the owner's livelihood |
| Risk tolerance | Low, institutionalised | Personally high, economically fragile |

Both dimensions cut against the assumption that SMEs simply need a scaled-down version of the large-firm model. Some parts shrink to nothing; others become more, not less, important.

### 2.3 The gap
SME AI adoption research is still largely at the adoption-barrier stage (`what stops SMEs adopting AI`). The governance question — *given that they are adopting, what should they do* — is barely addressed, and the emerging large-firm governance frameworks are unusable for a firm with no compliance function. Regulatory guidance (national AI Act implementation guidance, chamber-of-commerce material) is generic and not operational.

**Precise gap statement:** No governance artefact exists that is simultaneously (a) compatible with EU AI Act deployer obligations, (b) implementable by a firm with no compliance function, and (c) light enough that an owner-operator would actually use it.

### 2.4 Research questions
- **RQ1** — How do SMEs use generative coding tools in practice, and what governance is currently in place (usually none)?
- **RQ2** — Which elements of the large-firm two-track model survive reduction to SME scale, and which become counter-productive?
- **RQ3** — What replaces the named-employee accountability mechanism when the accountable party is the owner?
- **RQ4** — What is the minimum viable audit trail for an SME that nevertheless satisfies EU AI Act deployer obligations?

### 2.5 Contribution
An SME-specific guardrail model; an empirically grounded account of actual SME generative-coding practice; a minimal evidence standard that is defensible without being bureaucratic.

### 2.6 Roadmap

---

## 3. Theoretical background

### 3.1 SME technology adoption
TOE framework (Tornatzky & Fleischer), resource-based constraints, owner-manager centrality in SME decision-making — the owner's disposition is the single largest determinant, which is both an obstacle and, we argue, an asset for accountability.

### 3.2 The regulatory position of the SME as deployer
Critical clarification the literature frequently gets wrong: the AI Act's obligations attach to **deployers**, not only providers, and an SME that uses an AI tool in a regulated decision is a deployer regardless of size. Establish the actual obligation surface for a small firm — it is smaller than firms fear, but not zero.

### 3.3 Owner-operator accountability as governance mechanism
Develop the central theoretical idea: in a firm where the owner is personally liable and personally present in the work, **the owner's signature is a functioning control** — it is the same accountability a large firm tries to reconstruct through segregation of duties and role definitions. This is a genuinely interesting reframing: the SME's constraint (no governance apparatus) is partially offset by the fact that accountability cannot diffuse the way it does in a large firm.

### 3.4 Related work
SME AI adoption studies · citizen development and low-code governance · regulatory guidance for small deployers · light-weight compliance models (e.g. GDPR tools for SMEs)

---

## 4. Method

### 4.1 Design
Exploratory multiple case study, **n≈6–10 DACH SMEs** across sectors, selected for contrast in size (5–50 and 50–250) and in the type of generative coding use. Theoretical sampling, replication logic (Yin).

### 4.2 Selection criteria
- Must currently use (or have used) generative coding tools beyond simple text assistance
- Mix of sectors: engineering/services, small manufacturing, professional services, trade
- One or more cases in a *regulated* activity (making clear the obligations are real)

### 4.3 Data collection
Owner/senior decision-maker interviews (primary), employee interviews where possible (n≈2 per case for the larger firms), documentary evidence (whatever exists — often nothing, which is itself a datum), and a walkthrough of the actual generated tool.

### 4.4 Analysis
Cross-case analysis, pattern matching against the large-firm model's elements to derive what survives. Build a reduction table: element → keep / adapt / drop / replace-with-what.

### 4.5 Ethics
Small firms and owners are identifiable. Anonymise the firms; describe sectors at a granularity that does not permit easy identification. Note that asking about undocumented AI use is sensitive — owners have no incentive to disclose, which is a real limitation and should be stated.

---

## 5. The artefact — SME variant

### 5.1 Reduction from the large-firm model

| Paper 1 element | SME treatment | Rationale |
|---|---|---|
| Experimental lane | **Kept, simplified** | Synthetic/public data only is still the cheapest control available |
| Promotion gate (6 criteria) | **Reduced to 3** | See §5.2 |
| Named accountable employee | **Replaced by owner declaration** | The owner *is* the accountable party |
| Model/version pinning | **Kept** | Trivial to do, disproportionately valuable |
| Data-zone compliance | **Kept — the most important one** | Data protection exposure is the SME's real risk |
| Change-management integration | **Dropped** | No change-management process exists |
| Rewrite-threshold model | **Simplified to a rule of thumb** | Owners decide faster and with less formal analysis |

### 5.2 The three-criterion SME gate
Deliberately minimal, because a gate with six criteria will not be used by a firm with no compliance function:
- **S1 — Owner sign-off.** The owner knows the tool exists, knows what it does, and has recorded that. One line, one date.
- **S2 — Data declaration.** The tool's inputs and outputs are described, and the tool touches no personal data beyond what the firm is already lawfully processing.
- **S3 — Provenance note.** Model and version, date generated, and who asked for it. One structured record.

Three criteria, each satisfiable in under an hour by a non-specialist. The claim to test: does a gate this permissive still produce a defensible position if the firm is later asked to explain its AI use?

### 5.3 The single structured record
Replace a control framework with **one structured record per tool** — a machine-readable one-pager. Present a concrete template. Argue that a firm that maintains exactly one artefact per AI tool is in a materially better position than one that maintains none but has read the guidance.

### 5.4 Design principles
DP1 — Reduce criteria until an owner-operator will actually comply.
DP2 — The owner's signature *is* the control; do not try to reconstruct segregation of duties.
DP3 — Protect data first; everything else is secondary.
DP4 — One record per tool, structured, kept.
DP5 — Provide the template, not the framework.

---

## 6. Evaluation

### 6.1 Case analysis
What the cases actually do. Expect: substantial ungoverned use, high owner confidence, low documentation. Report the gap between perception and practice — this is likely the paper's most quotable finding.

### 6.2 Assessment of the SME variant
Apply the variant to each case retrospectively and assess: would S1–S3 have been satisfiable? Would the resulting record have been defensible? Where does the model break (expect: tools that quietly became customer-facing, and tools whose outputs feed regulated decisions).

### 6.3 Owner evaluation
Structured feedback from participants on whether they would adopt the three criteria. The adoption question is the real test of the artefact — report it honestly including any refusal.

### 6.4 Threats to validity
Small sample; self-report on sensitive undocumented use; the researcher has no SME-owner identity, which may affect disclosure; single national context (DACH regulatory implementation).

---

## 7. Discussion

### 7.1 Compliance proportionality
Engage with the proportionality principle: the AI Act's obligations scale with role and risk, and the SME case is where proportionality is most likely to be honoured — but only if guidance is operational. This paper provides one operational instance.

### 7.2 The accountability inversion
The theoretical payoff: in large firms, accountability is diffused and must be reconstructed by design; in SMEs, accountability is concentrated and must simply be *recorded*. This inverts the standard assumption that small firms are structurally worse at governance.

### 7.3 Relationship to Papers 1–3
Explicitly state the research programme: the large-firm mechanism (P1), its behavioural drivers (P2), its institutional memory (P3), and its proportional reduction (P4). Frame the four papers as a coherent agenda — this materially strengthens reviewer perception of each one.

### 7.4 Limitations
Small n; single region; the artefact is a reduction whose sufficiency under real regulatory scrutiny is untested.

---

## 8. Conclusion
Answer RQ1–RQ4. State the three-criterion gate and the single-record standard. Name the next step: a longitudinal deployment with a chamber of commerce or industry association, producing evidence on whether owners sustain compliance.

---

## References (seed list)
Tornatzky & Fleischer 1990 · Yin 2018 (case study) · EU AI Act Reg. 2024/1689 (deployer obligations) · national AI Act implementation guidance (AT/DE) · GDPR Art. 30/32 · SME AI adoption literature · citizen development / low-code governance literature · light-weight compliance tooling studies

---

## Writing plan
| Phase | Deliverable | Effort |
|---|---|---|
| 1 | Case recruitment (6–10 SMEs) | 25 h |
| 2 | Interviews + tool walkthroughs | 40 h |
| 3 | Cross-case analysis + reduction table | 25 h |
| 4 | Artefact formulation + template | 20 h |
| 5 | Evaluation + write-up | 40 h |
| | **Total** | **~150 h** |

## Pre-writing blockers
1. **Paper 1 accepted (or at minimum under review)** — the reduction claim is only credible if the parent model is established.
2. **Case access** — 6–10 SME owners willing to disclose undocumented AI use is real work. A chamber-of-commerce or industry-association partnership is the practical route.
3. **Decide the thesis vehicle** — this is an excellent Master's thesis project and could be supervised through TU Wien, with the student doing the fieldwork. That changes the effort budget materially and should be decided before recruitment.

---

## Note on sequencing (important)

The original proposal listed this as a "separate, later paper" and that judgement stands. The strong recommendation across the research programme is:

1. **Write Paper 1 to completion.** Nothing else matters until one paper exists.
2. **Papers 2 and 3 can then run in parallel** with different co-authors, because they use different methods and different literatures.
3. **Paper 4 only after Paper 1 is accepted** — ideally as a supervised thesis.

Four papers written simultaneously is how a research agenda produces zero publications. One completed paper, on the page, with a real DOI, produces scientific presence. Everything else is plan.
