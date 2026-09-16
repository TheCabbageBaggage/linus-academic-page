# Paper 2 — The Compliance-Innovation Paradox: Augmentation vs. Automation under Regulated AI Use

> **Status:** Outline v1 | **Target:** 7,000–9,000 words
> **Venue:** *Academy of Management Discoveries* (AMD) · *Technovation* · *Journal of Product Innovation Management*
> **Method:** Mixed methods — quantitative survey + qualitative case interviews
> **Sequencing:** Write **after** Paper 1. Paper 1 supplies the mechanism; Paper 2 tests its effect.
> **Co-author target:** TU Wien + ideally a management/innovation scholar for the survey instrument

---

## 1. Abstract (draft)

The dominant account of organisational AI adoption holds that firms default to automation — cutting headcount in proportion to observed productivity gains — rather than reimagining work around augmentation. This view, most prominently articulated in practitioner discourse, is supported by observation but has not been tested empirically, and has never been tested in settings where automation is legally constrained. We propose and test a **compliance-contingency model**: the proposition that regulatory load acts as a *forcing function toward augmentation*, because automating a regulated process inherits the full certification and oversight burden, whereas augmenting a human who remains accountable does not. Surveying [N] digitalisation, IT, and operations leaders in DACH industrial firms, complemented by [n] in-depth case interviews, we find [pending] . The results reframe compliance from an obstacle to AI adoption into a structural driver of higher-quality adoption, and identify the conditions under which the effect reverses. The practical implication is that firms in regulated sectors may be structurally advantaged in adopting AI well — a claim directly counter to the compliance-as-brake consensus.

**Keywords:** AI adoption, augmentation, automation, regulatory compliance, EU AI Act, industrial firms, contingency theory

---

## 2. Introduction

### 2.1 Opening hook
Two firms deploy the same model to the same process. One cuts 30% of the team and reassigns the work to a pipeline. The other keeps the team and gives each member an AI collaborator, retaining human accountability at every decision point. The second firm is slower to book its productivity gain — and, we argue, structurally more resilient, more compliant, and ultimately more innovative. The literature currently explains this difference by culture or leadership. We propose it is substantially explained by **regulatory exposure**.

### 2.2 The automation default
Trace the argument as it currently stands: observed productivity gains (the 30% figure recurs in the discourse) → arithmetic extrapolation → headcount reduction → "AI is just automation." Note that this chain contains an unexamined assumption: that the productivity gain is *substitutable*. It is not, when a human signature is legally required on the output.

### 2.3 The gap
Three linked gaps:
1. **Empirical.** The augmentation-vs-automation claim is asserted from case observation, not tested with systematic data.
2. **Contingency.** No model specifies *when* which strategy is chosen. The literature treats the choice as a function of leadership disposition.
3. **Regulated settings.** The compliance regime is almost universally modelled as a *friction* on adoption. We are not aware of a study that models it as a *determinant of adoption mode*.

**Precise gap statement:** There is no empirically tested contingency model explaining how regulatory exposure shifts firms between automation and augmentation strategies in AI adoption.

### 2.4 Research questions
- **RQ1** — Do firms in regulated sectors differ systematically from firms in unregulated sectors in their AI adoption *mode* (automation-dominant vs. augmentation-dominant)?
- **RQ2** — Does perceived compliance load predict augmentation-dominant adoption, controlling for firm size, AI maturity, and leadership disposition?
- **RQ3** — Under what conditions does the compliance→augmentation effect reverse (i.e. when does regulation push firms *away* from adoption entirely)?
- **RQ4** — How do practitioners in regulated industry reason about the automation/augmentation choice — is compliance salient in their decision framing?

### 2.5 Contribution
First empirical contingency model of AI adoption mode. Reframes compliance as a structural driver. Provides a validated measurement instrument for adoption mode (a secondary but genuinely useful contribution — reviewers like instruments).

### 2.6 Roadmap

---

## 3. Theoretical background & hypotheses

### 3.1 Contingency theory as the lens
Why contingency theory rather than TAM/UTAUT: those explain *whether* technology is adopted; we are explaining *in what mode*. Draw on organisational contingency traditions (Lawrence & Lorsch; Donaldson) and on the IS literature's contingency applications.

### 3.2 The augmentation/automation distinction
Formalise the two modes. Critically, they are **not** a spectrum of intensity but differ in *where accountability sits*:
- **Automation:** accountability is designed into the system; the human is removed from the loop.
- **Augmentation:** accountability remains with the human; the system advises.

This distinction is what makes compliance relevant, because regulatory instruments almost universally require a *human* accountable party — they cannot be satisfied by a system alone.

### 3.3 Compliance load as a forcing function
The core theoretical move. Develop the causal logic:
1. Regulatory instruments require human accountability for regulated decisions (AI Act Art. 14 human oversight; SOX signatures; IEC 62443 operator responsibility).
2. Automating such a decision requires demonstrating that the *system* satisfies every control the human previously satisfied — a substantially larger certification burden.
3. Augmenting leaves the human in place, so the existing controls continue to hold.
4. Therefore, holding other factors constant, higher compliance load shifts the cost calculus toward augmentation.

State this as an explicit mechanism with a figure, then formalise.

### 3.4 When the effect reverses
The theoretically interesting boundary condition. Propose that beyond some compliance threshold, firms exit adoption altogether rather than choosing a mode — prohibition becomes the third option. This yields a non-monotonic relationship, which is exactly the kind of finding AMD likes.

```
Adoption mode
   augmentation │              ╭──────╮
   dominant     │        ╭─────╯      ╰─────╮
                │   ╭────╯                  ╰───  prohibition
   automation   │╭──╯                             zone
   dominant     ╰╯
                └──────────────────────────────▶ compliance load
```

### 3.5 Hypotheses
- **H1** — Regulated-sector firms exhibit higher augmentation-dominance than matched unregulated firms.
- **H2** — Perceived compliance load is positively associated with augmentation-dominance, controlling for firm size, AI maturity, and leadership AI-usage.
- **H3** — The association in H2 is non-monotonic: at very high compliance load, the relationship with any adoption (of either mode) turns negative.
- **H4** — Leadership AI-usage moderates H2: the compliance→augmentation effect is stronger where senior leadership personally uses AI tools.
- **H5** — Where employees perceive that productivity gains will not be shared, reported adoption mode diverges from actual use (the information-gap hypothesis — see §3.6).

### 3.6 The information-gap hypothesis
Introduce the claim that hidden AI use distorts self-reported adoption data, which is a **methodological threat** to every survey in this literature, including ours. Propose a proxy measure (tool-provision telemetry vs. self-report delta) and be explicit that this is exploratory.

---

## 4. Method

### 4.1 Design
Explanatory sequential mixed methods: quantitative survey (H1–H4) → qualitative interviews (RQ4, mechanism validation). Justify the order.

### 4.2 Sampling frame
Digitalisation / IT / operations leaders in DACH industrial firms. Target **n≈80–150** completed responses. Feasible via the author's professional network plus DACH industry associations (Austrian Chamber of Commerce, IV, VDMA contacts). Document the realistic response-rate arithmetic honestly — this is a hard-to-reach population.

Stratify by regulatory exposure: **high** (steel/chemicals/energy/pharma/rail — Seveso, IEC 62443, GMP) vs. **low** (general manufacturing, services).

### 4.3 Instrument
Because no validated scale for "adoption mode" exists, present the development process:
- Item generation from the augmentation/automation literature
- Expert review (n≈5 practitioners/academics)
- Pre-test (n≈15)
- Resulting **Adoption Mode Index (AMI)** — publish the items in an appendix; this is a contribution in itself

Control variables: firm size, sector, AI maturity (self-assessed + tool provisioning), leadership AI-usage, GDPR/AI-Act familiarity, union/works-council presence (a DACH-specific confounder worth calling out).

Common-method bias mitigation: temporal separation of predictor and outcome where feasible, marker variable, Harman's single-factor check.

### 4.4 Qualitative component
**n≈12–15** semi-structured interviews, sampled purposively for contrast (high-compliance adopters, high-compliance non-adopters, low-compliance adopters). Thematic analysis following Braun & Clarke. Focus: how the automation/augmentation choice was actually framed, whether compliance appeared in the reasoning, and what alternatives were silently discarded.

### 4.5 Analysis
- OLS / ordered logit for H1–H2
- Non-linear specification (quadratic term + spline) for H3
- Interaction term for H4
- Qualitative: thematic + a small cross-case matrix linking stated reasoning to AMI score

### 4.6 Ethics & data protection
Anonymity for firms and individuals (this population is small and identifiable within DACH). GDPR-compliant processing. Note that respondents may under-report non-compliant practice — a known limitation.

---

## 5. Expected findings & how to handle them

Plan for three outcome scenarios, because the paper must be writable either way:
- **H1/H2 confirmed.** The clean result. Lead with the reframing: compliance as driver.
- **H1/H2 null.** Still publishable as a *disconfirmation of a widely held assumption* — arguably more interesting, and AMD explicitly values this. The contribution becomes "leadership disposition, not compliance, drives mode."
- **H3 dominant.** The non-monotonic result is the headline. Reframe the paper around the prohibition zone.

State in the paper that scenario pre-planning occurred; it strengthens credibility.

---

## 6. Discussion

### 6.1 Reframing compliance
Take the finding to its conclusion: if compliance load drives augmentation, then regulated firms are — counterintuitively — better positioned for *good* AI adoption than unregulated ones, provided they stay below the prohibition threshold. This is the paper's headline claim if H1–H2 hold.

### 6.2 Policy implications
Two concrete implications: (a) AI-Act implementation guidance should account for the fact that heavy obligations can push firms out of adoption entirely; (b) sector regulators could reduce the prohibition-zone risk by providing *promotion paths* rather than only restrictions. Cross-reference Paper 1's promotion gate as one such path.

### 6.3 Relationship to Mollick's model
Direct engagement: the Leadership/Crowd/Lab model explains how firms *can* avoid the automation default. This paper adds *why some firms are structurally pushed toward augmentation regardless of leadership intent* — a complement, not a contradiction.

### 6.4 Limitations
Cross-sectional (no causal claim beyond mechanism plausibility); self-report and the information gap; single region (DACH) — generalisability caveats; small-n in the high-compliance stratum.

---

## 7. Conclusion
Answer RQ1–RQ4 in one sentence each. State the AMI as a reusable contribution. Point forward to Paper 3 (institutional learning) and Paper 4 (SME extension).

---

## References (seed list)
Lawrence & Lorsch 1967 · Donaldson 2001 · Rai 2020 · Mikalef et al. 2022 · Brynjolfsson & McAfee · Dell'Acqua et al. 2023 (jagged frontier) · Noy & Zhang 2023 · Mollick 2025 · EU AI Act Reg. 2024/1689 · Braun & Clarke 2006 · Podsakoff et al. 2003 (CMB) · plus the augmentation/automation debate in HCI and IS

---

## Writing plan
| Phase | Deliverable | Effort |
|---|---|---|
| 1 | Instrument development + pre-test | 30 h |
| 2 | Survey deployment + follow-up | 25 h |
| 3 | Interviews (12–15) + transcription | 35 h |
| 4 | Quantitative analysis | 30 h |
| 5 | Qualitative analysis + integration | 30 h |
| 6 | Write-up + submission | 40 h |
| | **Total** | **~190 h** |

## Pre-writing blockers
1. **Survey access** — this population is hard to reach; secure the distribution channel (associations, network) *before* building the instrument.
2. **Co-author in management/innovation** — the AM and OM literatures have different reviewer expectations than IS. This paper needs the right co-author.
3. **Paper 1 accepted or at least submitted** — the mechanism should be established first.
