# TVCG Revision Plan

Planning document for the V4/Stim revision of TVCG-2025-09-0929. Effort tags: **S** ≤ half-day, **M** 1–2 days, **L** 3–5 days. Total ballpark: ~3 weeks of focused work within the AE's 3-month window.

## Decisions log (Phase 0)

1. **Title direction** — Neural correlates (broader), measurement + mitigation. Scope-defining word from meeting notes: **"neuromarkers"**. Working title to be finalized once abstract is drafted; e.g. *"Neuromarkers of Cybersickness in Virtual Reality: A Systematic Review of Measurement and Mitigation"*.
2. **Terminology policy** — Hybrid: adopt VIMS-as-umbrella in Background/Theory (introducing the construct space per R1), but in Results refer to each study by the term that paper used. Updates TODO Critical #6. Aligned with meeting notes ("trouver une catégorisation si possible" + "on utilise le terme du papier").
3. **All-studies table placement** — In-text (R1's preference). Confirmed in meeting notes ("très important, point central du papier"). Costs ~2 pages of the 20-page survey budget.
4. **Dataset-based prediction papers — OUT of scope** (reverses TODO Critical #4). Rationale from meeting: focus is neuromarkers; reusing existing data = classification, not neuromarker discovery. Action: acknowledge in Methods/Discussion with a short paragraph citing the relevant sub-literature; count how many otherwise-eligible papers were excluded on this basis and report the number.
5. **PET / MEG / fMRI scope** — Searched (PET, MEG were already in the V4/Stim query). 0 eligible PET, 0 MEG, 0 fMRI in corpus. Methods states this plainly; no further searching.
6. **Motion sickness scope** — Stays focused on cybersickness/VIMS; do not broaden to classic motion sickness.
7. **Response letter format** — Structured by **theme**, not per reviewer, with a diff. Separate document (per Editor letter requirement).
8. **Page budget posture** — Survey hard cap is **20 pages** (the "pay for additional pages" path applies to regular papers, 12 → 18; survey papers are capped at 20 regardless). Treat 20 as binding; allocate per-section budget in a follow-up decision.
9. **Dataset-based prediction papers (6 already in corpus)** — Keep in corpus; acknowledge as tangential. Methods/Discussion adds a short paragraph stating dataset-only ML prediction is a related but distinct literature, with these 6 borderline cases retained because they were eligible under the search criteria. No re-screening, no stats regeneration. Closes the operational gap in Decision 4.
10. **Section F ("Additional Findings") — split**:
    - **Promote** the *Confounding Factors* subsubsection to a top-level Results subsection (or fold into Section B "Neural Correlates"). This is where the new V4 corpus-level stats (VR-device × alpha p=0.0036, × beta p=0.0146, Egger p=0.011) land. These are arguably the strongest empirical contribution and should not be buried.
    - **Demote** *Recovery*, *Public Datasets*, *Cognition* into 1–2 paragraphs in Discussion (Recovery: 1 paper; Datasets: ties to the now-out-of-scope dataset literature per Decision 9; Cognition: 4 papers — too small for standalone subsubsections).
    - Section F heading disappears (concession to R1); corpus-completeness preserved by the all-studies table (Decision 3).
11. **"Other physiological correlates" section** — Remove as a standalone subsection. Briefly mention candidate non-neural objective measures (postural sway, pupillometry) in Discussion alongside the High #14 objective-measures caveat.
12. **Chang et al. (2023) comparison** — Paragraph in Intro (no table). 2–3 sentences contrasting scope, corpus size, modality breadth (this review includes neurostim), and meta-analytic depth.
13. **Page budget (sums to 20)**:

    | Section | Pages |
    |---|---|
    | Abstract | 0.5 |
    | Introduction (incl. Chang paragraph, neuromarker framing, TVCG-fit) | 2 |
    | Background / Theory (VIMS hierarchy, theory refs, fNIRS, vection, nausea reframing) | 3 |
    | Methods + PRISMA (V4/Stim queries, scope justifications, dataset-paper acknowledgment) | 1.5 |
    | Results — all-studies table ~2 | 7 |
    | &nbsp;&nbsp;&nbsp;&nbsp;Neural correlates ~2 | |
    | &nbsp;&nbsp;&nbsp;&nbsp;Classification ~1 | |
    | &nbsp;&nbsp;&nbsp;&nbsp;Individual diff + Mitigation ~1 | |
    | &nbsp;&nbsp;&nbsp;&nbsp;Meta-analytic confounders (promoted from Section F) ~1 | |
    | Discussion + Future Directions | 4 |
    | References | 2 |
    | **Total** | **20** |

## Corpus-derived facts locked in Phase 0

- **PET & MEG**: V4/Stim query included both; 0 eligible studies returned.
- **Dataset-based prediction**: 6/92 in corpus already (4 reused public datasets, 2 used both). Per Decision 4, these are out of scope and will need to be either re-screened out or acknowledged as out-of-focus inclusions — to confirm.
- **Theory engagement**: 73/92 explicit, 14/92 implicit, 5/92 none. Among engaged: 75/87 cite sensory conflict. TODO Critical #5 framing empirically supported.
- **Modality counts**: EEG 77, fNIRS 4, fMRI 0; neurostim 11 (GVS 5, tDCS 3, tACS 2, Other 1). The 11 missing `Neuroimaging_device` values correspond to neurostim-only papers.

## Corpus-derived facts locked in Phase 0

- **PET & MEG**: V4/Stim query included both; 0 eligible studies returned. Methods will state this; no MEG-omission risk.
- **Dataset-based prediction papers**: 6/92 in corpus (4 reused public datasets, 2 used both reused + new). Critical #4 already partially operationalized.
- **Theory engagement**: 73/92 explicit, 14/92 implicit, 5/92 none. Among engaged: 75/87 cite sensory conflict. TODO Critical #5 framing empirically supported.
- **Modality counts**: EEG 77, fNIRS 4, fMRI 0; neurostim 11 (GVS 5, tDCS 3, tACS 2, Other 1). 11 "NaN" in Neuroimaging_device are the neurostim-only papers.

## Sequenced phases

### Phase 0 — Lock scope decisions and page budget (S, blocks everything)
No prose work until the open decisions below are closed and a per-section page budget is committed. The 20-page survey cap is the binding constraint that decides whether the all-studies table goes in-text or supplemental, and whether Section F / "other physiological correlates" survive.
- Addresses: Editor letter (page limit), Medium #4, #5.

### Phase 1 — Reframing pass: title, abstract, keywords, intro spine (M)
Reframe away from BCI before touching anything downstream — every section currently leans on the term, so doing this first prevents re-editing the same paragraphs twice. Includes: new title/abstract/keywords, rewritten intro that (a) states the neurophysiology + neurostimulation scope, (b) defends TVCG fit, (c) explicitly positions against Chang et al. 2023 (scope, corpus size, modality coverage, neurostimulation inclusion).
- Addresses: **Critical #1, #2**; R1 Major #1, Major #4, Major #5; Medium #4.
- Blocks: everything else.

### Phase 2 — Theory/Background rewrite (L, parallelizable with Phase 3)
Rewrite `contents/theoretical.tex` and the relevant background subsections in `contents/introduction.tex`:
- Replace weak sensory-conflict refs with Reason / Reason & Brand / Oman; remove "vection theory" phrasing; reposition poison theory as a *why* not a competitor; fix FMS attribution (Keshavarz & Hecht 2011).
- Add Keshavarz & Golding 2022, Lackner 2014, Cha et al., Lawson 2014, Keshavarz/Hecht/Lawson 2014, Teixeira 2022/2025 (unexpected vection), Berti & Keshavarz 2020, Yates 2014, Cohen 2019, Schmäl 2013.
- Rewrite the "CS vs SS vs MS via vection/disorientation/oculomotor/nausea" sentence (R1 says it's wrong).
- Fix fNIRS background: temporal resolution comparable to fMRI; deep structures (insula/amygdala) not accessible.
- Reframe nausea network around 0 fMRI in our corpus (this is the lever — corpus-grounded retraction, then bridge to MS-nausea + vection literature).
- Addresses: **Critical #5 (part 1), #6**; High #2, #3, #4, #5, #6, #8, #9.

### Phase 3 — Methods/PRISMA fixes (M, parallel with Phase 2)
Rewrite `contents/methodology.tex` to document V4/Stim:
- New PubMed/WoS/Scopus query strings (from `review_scripts/data/V4/notes.md`), explicitly including neurostim terms.
- Reconcile 119 vs 114 duplicate count.
- Add explicit eligibility note about dataset-based prediction papers (Critical #4).
- Add one paragraph on excluded modalities: PET (searched, n=0), MEG (justify why omitted), fMRI (not excluded, just absent in corpus).
- Updated PRISMA figure with the new counts.
- Addresses: **Critical #3, #4**; High #1; R3 minor on PET/MEG.

### Phase 4 — All-studies table + study-count integration (M, must precede Phase 5)
Generate a single table of all 92 studies (modality, sample size, VR device, stimulus, sickness measure, key finding) from `PDF_HighLevel_Analysis_GPT54.csv` + `Plots_Analysis_GPT54.csv` via a script in `review_scripts/`. This is the artefact that lets Results cite real counts ("77/92 EEG", "11 neurostimulation: 5 GVS / 3 tDCS / 2 tACS / 1 other") instead of "a substantial body of research". Whether it lands in-text or supplemental is a Phase 0 decision.
- Addresses: **Critical #7**; High #7.

### Phase 5 — Results rewrite, corpus-grounded (L)
Rewrite `contents/results.tex` against the regenerated stats:
- Replace narrative with counts everywhere (R1 High #7).
- Move ERPs before fMRI (Medium #1).
- Cut or merge "other physiological correlates" (Medium #2) and Section F (Medium #3) per Phase 0 decisions.
- Integrate new findings: VR-device × alpha (p=0.0036, large effect), × beta (p=0.0146), Egger publication bias (p=0.011).
- Re-thread sensory-conflict / postural-instability / unexpected-vection lenses across modality subsections — this is the "use the theories to structure synthesis" half of Critical #5.
- Frame ML accuracy discussion around sensitivity/specificity and arbitrary sick/non-sick thresholds (High #11).
- Soften sex/gender claims with Kelly 2023, Kourtesis 2023, Lawson & Bolkhovsky 2023 (High #12); rephrase the "not random" baseline-brain claim (High #13).
- Justify eyes-closed critique and propose alternative baselines (High #10).
- Addresses: **Critical #5 (part 2), #7, #8**; High #7, #8, #10, #11, #12, #13; Medium #1, #2, #3.

### Phase 6 — Discussion + Future Directions rewrite (M)
Re-anchor `contents/discussion.tex` and `contents/future.tex` in the cited corpus (no claims without a corpus-derived count or a cited paper). Add objective-measures caveat that CS/MS are intrinsically subjective; list postural sway and pupillometry as candidate objective signals (High #14). Use the Egger result and the publication-bias question to motivate concrete methodological recommendations.
- Addresses: **Critical #8**; High #11, #14.

### Phase 7 — Page-fit + style sweep (S–M)
Compile, measure against budget, cut. Sweep for value-judgment language and metaphor per AGENTS.md. Verify every figure/table is referenced and every claim has a citation or a corpus count.
- Addresses: Medium #5; AGENTS.md style rules.

### Phase 8 — Response letter (S, if a change-log is kept through Phases 1–7)
Per-comment matrix (AE, R1.×, R2.×, R3.×), each with "Change made:" + section/line refs.
- Addresses: Editor letter Medium #6.

## Decisions required before drafting

1. **New title** — concrete wording, since it gates the abstract.
2. **Terminology policy** — confirm we are declining R1's specific request to adopt VIMS as the umbrella term and keep the "use each paper's own term" approach. R1 may push back; we need a defensible response-letter sentence.
3. **All-studies table placement** — in-text (R1's preference, ~1.5–2 pages) or supplemental (page-budget-friendly).
4. **PET/MEG handling** — did the V4/Stim re-search actually include PET terms and return 0, or was PET not searched? Same for MEG. The Methods rewrite needs the truth.
5. **Dataset-based prediction papers** — are these already in the 92, or do we still need a targeted top-up search? If the latter, this is a Phase 3 blocker.
6. **Section F fate** (R1 says cut) — remove, merge into Discussion, or defend? TODO Medium #3 has no decision recorded.
7. **"Other physiological correlates"** (R1 says cut) — same question. TODO Medium #2 has no decision.
8. **TVCG-fit defense** — explicit VR-practitioner-takeaways subsection in the Intro/Discussion, or rely on framing alone? Removing BCI may worsen, not improve, the perceived fit.
9. **Page budget per section** — commit to numbers (e.g., Intro 2, Background/Theory 3, Methods 2, Results 7, Discussion+Future 4, Refs 2) so cuts are decided, not negotiated section-by-section.
10. **Chang et al. 2023 comparison format** — short paragraph or compact comparison table?
11. **New stats placement** — VR-device × band-power and Egger: Results (with stats), Discussion (interpreted), or both?
12. **Response letter format** — embedded in the manuscript file or separate `response_letter.tex`? Editor expects separate.

## Risks in existing TODO decisions

- **Critical #3 ("Neurostimulation and PET, no further")** — corpus returned 0 PET, and R3 explicitly named **MEG** alongside PET. Adding PET terms without addressing MEG leaves a comment unanswered. Recommend explicitly justifying MEG omission in Methods.
- **Critical #6 (use each paper's term, no enforced hierarchy)** — defensible but directly declines R1's specific recommendation. The response letter must explain *why* (likely: imposing a hierarchy risks misrepresenting cited authors). Worth pre-drafting that justification now so the rest of the prose stays consistent with it.
- **Critical #5 ("overwhelming majority rely on sensory conflict")** — verify against the `Theory_Mentioned` / theory-engagement field in `PDF_HighLevel_Analysis_GPT54.csv` before committing. If most papers cite *no* theory at all (which R3 implies), the framing should be "most papers do not engage explicit theory; among those that do, sensory conflict dominates" — different message, same evidence.
- **Critical #1 (remove BCI framing entirely)** — interacts with R1 Major #5 (journal fit). Removing BCI strengthens the scientific framing but weakens the "this belongs in TVCG" argument. Need a compensating VR-hardware/practitioner thread (decision #8 above).
- **Critical #4 ("Yes" include dataset-based prediction)** — if those papers aren't already in the 92, accepting this means a new screening round, which is a Phase 3 blocker, not a Phase 5 prose tweak.
