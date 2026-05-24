# TVCG Revision Plan

Planning document for the TVCG revision of TVCG-2025-09-0929. Effort tags: **S** ≤ half-day, **M** 1–2 days, **L** 3–5 days. Total ballpark: ~3 weeks of focused work within the AE's 3-month window.

## Decisions log (Phase 0)

1. **Title (final)** — *"The Neurophysiology of Cybersickness in Virtual Reality: A Systematic Review of Neural Correlates and Neurostimulation"*. Scope-defining concept in prose: **neuromarkers** (signals derived from non-invasive recording or modulation of brain activity that index or modulate cybersickness state).
2. **Terminology policy** — Hybrid: adopt VIMS-as-umbrella in Background/Theory (introducing the construct space per R1), but in Results refer to each study by the term that paper used. Updates TODO Critical #6. Aligned with meeting notes ("trouver une catégorisation si possible" + "on utilise le terme du papier").
3. **All-studies table placement** — In-text (R1's preference). Confirmed in meeting notes ("très important, point central du papier"). Costs ~2 pages of the 20-page survey budget.
4. **Dataset-based prediction papers — OUT of scope** (reverses TODO Critical #4). Rationale from meeting: focus is neuromarkers; reusing existing data = classification, not neuromarker discovery. Action: acknowledge in Methods/Discussion with a short paragraph citing the relevant sub-literature; count how many otherwise-eligible papers were excluded on this basis and report the number.
5. **PET / MEG / fMRI scope** — PET and MEG were in the search query. 0 eligible PET, 0 MEG, 0 fMRI in corpus. Methods states this plainly; no further searching.
6. **Motion sickness scope** — Stays focused on cybersickness/VIMS; do not broaden to classic motion sickness.
7. **Response letter format** — Structured by **theme**, not per reviewer, with a diff. Separate document (per Editor letter requirement).
8. **Page budget posture** — Survey hard cap is **20 pages** (the "pay for additional pages" path applies to regular papers, 12 → 18; survey papers are capped at 20 regardless). Treat 20 as binding; allocate per-section budget in a follow-up decision.
9. **Dataset-based prediction papers (6 already in corpus)** — Keep in corpus; acknowledge as tangential. Methods/Discussion adds a short paragraph stating dataset-only ML prediction is a related but distinct literature, with these 6 borderline cases retained because they were eligible under the search criteria. No re-screening, no stats regeneration. Closes the operational gap in Decision 4.
10. **Section F ("Additional Findings") — split**:
    - **Promote** the *Confounding Factors* subsubsection to a top-level Results subsection (or fold into Section B "Neural Correlates"). This is where the new corpus-level stats (VR-device × alpha p=0.0036, × beta p=0.0146, Egger p=0.011) land. These are arguably the strongest empirical contribution and should not be buried.
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
    | Methods + PRISMA (search queries, scope justifications, dataset-paper acknowledgment) | 1.5 |
    | Results — all-studies table ~2 | 7 |
    | &nbsp;&nbsp;&nbsp;&nbsp;Neural correlates ~2 | |
    | &nbsp;&nbsp;&nbsp;&nbsp;Classification ~1 | |
    | &nbsp;&nbsp;&nbsp;&nbsp;Individual diff + Mitigation ~1 | |
    | &nbsp;&nbsp;&nbsp;&nbsp;Meta-analytic confounders (promoted from Section F) ~1 | |
    | Discussion + Future Directions | 4 |
    | References | 2 |
    | **Total** | **20** |

14. **Contributions (3, locked; #3 reframed in Phase 6)**:
    1. Most current and broadest systematic synthesis of cybersickness neuromarkers in VR (92 studies, includes neurostimulation alongside neuroimaging, post-dates Chang 2023).
    2. Meta-analytic evidence that VR display hardware modulates band-power responses — HMD vs screen alpha Cliff's δ = 0.875 (p = 0.004, large effect) and beta δ = 0.664 (p = 0.015); reframes prior contradictions in the EEG-cybersickness literature as partly hardware-attributable.
    3. Methodological audit of the classification literature — across 38 classification or prediction studies, only 1 reports leave-one-subject-out validation, 19 expose no sick/non-sick threshold, and 13 report accuracy alone (no sens/spec, AUC, or F1) — leading to concrete reporting recommendations. (Earlier Egger publication-bias headline retired in Phase 6: the prior p=0.011 was produced by a methodology that double-counted within+cross accuracies and imputed n=30; corrected re-run yields p=0.036 / k=27 and is reported in Discussion as exploratory only, not as a contribution anchor.)

## Working conventions

- **Folder layout**: phase-specific side-job notes live in `revision_notes/phaseN/` (N = 0–9). Cross-phase artefacts stay in `revision_notes/`: `revision_plan.md`, `change_log.md`, and `assets/` (PDFs, Zotero exports).
- **Placeholders**: every unresolved value in source uses `\TODO[tag]{current-or-best-guess}`, rendered bright red in the PDF and grep-able from `contents/`. Tags use `topic:specifier` form (e.g. `\TODO[stat:alpha-p]{0.0036}`, `\TODO[chang:corpus-size]{n=??}`). Phase 8 sweeps `\TODO` to zero.
- **Side jobs**: each phase has a "Side jobs" subsection listing verification / info-gathering tasks that must complete *before* drafting prose for that phase. Outputs land in `revision_notes/phaseN/<topic>.md` as bullet notes, not prose. Rule: no prose claim enters a `.tex` file without a corresponding side-job note backing it.
- **Change log**: every phase appends to `revision_notes/change_log.md` (one line per change, tagged with the reviewer comment it addresses). Feeds Phase 9 response letter directly. Make sure to also keep the `TODO.md` file up to date
- **Drafting workflow (per phase)**: gather → reverse-outline → target outline → delta → draft → light flow pass. Concretely:
  1. **Gather** via the side-jobs listed for the phase. No prose yet.
  2. **Reverse-outline** the existing prose into `phaseN/current_outline.md`: one bullet per existing paragraph capturing its role, opening, claims, and citations. Mechanical transcription, not judgement. Skip this step only for sections receiving surface tweaks (a few citations swapped, a sentence softened); for substantially reworked sections (at minimum Theory, Results, Discussion) it is required.
  3. **Target outline** in `phaseN/outline.md`. Encodes flow, not just topics: per subsection, the argument it advances and its orienting sentence; per paragraph, its role (claim / evidence / refinement / consequence), what it opens with, what it hands to the next paragraph, and which side-job notes / corpus counts / citations anchor it. Ordering decisions (broader→narrower vs. punchline-last) made here. A paragraph with no anchor in side-job notes is flagged before drafting.
  4. **Delta** in `phaseN/delta.md`: per current-outline paragraph, tag `keep / revise / restructure / replace / delete`, plus a list of `new` paragraphs from the target outline that have no current counterpart. Structural sibling of `claims_audit.md` (which does the same at the claim level). Delta is ratified with the user before drafting.
  5. **Draft** into `contents/*.tex`, executing the delta. Structural reordering at this stage means the target outline was wrong — go back to step 3, do not improvise in prose.
  6. **Light flow pass** with [prompts/improve-flow.md](../prompts/improve-flow.md) as a sentence-level polish only (its scope: smoothing, no structural change, word count stable). If the flow pass wants to reorder paragraphs or move content, that is a signal the outline needs revisiting, not a license to restructure in-place. This pass should also make sure the tone and vocabulary is academic: no subjective assessments, no unsubstanciated adjectives, objective tone, factual reporting.

## Corpus-derived facts locked in Phase 0

- **PET & MEG**: Search query included both; 0 eligible studies returned. Methods will state this; no MEG-omission risk.
- **Dataset-based prediction papers**: 6/92 in corpus (4 reused public datasets, 2 used both reused + new). Critical #4 already partially operationalized.
- **Theory engagement**: 73/92 explicit, 14/92 implicit, 5/92 none. Among engaged: 75/87 cite sensory conflict. TODO Critical #5 framing empirically supported.
- **Modality counts**: EEG 77, fNIRS 4, fMRI 0; neurostim 11 (GVS 5, tDCS 3, tACS 2, Other 1). 11 "NaN" in Neuroimaging_device are the neurostim-only papers.

## Sequenced phases

### Phase 0 — Lock scope decisions and page budget (S, blocks everything)
No prose work until the open decisions below are closed and a per-section page budget is committed. The 20-page survey cap is the binding constraint that decides whether the all-studies table goes in-text or supplemental, and whether Section F / "other physiological correlates" survive.
- Addresses: Editor letter (page limit), Medium #4, #5.

### Phase 1 — Reframing pass: title, abstract, intro spine (M)
Reframe away from BCI before touching anything downstream — every section currently leans on the term, so doing this first prevents re-editing the same paragraphs twice. Includes: new title/abstract, rewritten intro that (a) states the neurophysiology + neurostimulation scope, (b) defends TVCG fit, (c) explicitly positions against Chang et al. 2023 (scope, corpus size, modality coverage, neurostimulation inclusion).
- Addresses: **Critical #1, #2**; R1 Major #1, Major #4, Major #5; Medium #4.
- Blocks: everything else.
- **Side jobs (do first, write notes, then draft)**:
  - `phase1/chang_comparison.md` — read Chang et al. 2023 in full; build a matrix (scope, corpus size, time window, modalities covered, meta-analytic depth, recommendations). Use a model to extract, but verify every claim against the PDF. Only then draft the Intro paragraph.
  - `phase1/tvcg_fit_thread.md` — list concrete VR-practitioner takeaways the paper supports (e.g. hardware-confounder advice), to seed the Intro's TVCG-fit defense.
- **Draft order**: frame sentence → title (locked) → abstract spine with `\TODO[abs:*]{...}` placeholders for numbers → intro spine. Full intro prose only after spine ratified.
- **Second-pass deferred to Phase 8**: abstract and conclusion rewritten holistically after Phases 5–7 stabilize (numbers re-pinned; claims aligned with final Results/Discussion; both sections kept appropriately high level).

### Phase 2 — Theory/Background rewrite (L, parallelizable with Phase 3)
Rewrite `contents/theoretical.tex` and the relevant background subsections in `contents/introduction.tex`:
- Replace weak sensory-conflict refs with Reason / Reason & Brand / Oman; remove "vection theory" phrasing; reposition poison theory as a *why* not a competitor; fix FMS attribution (Keshavarz & Hecht 2011).
- Add Keshavarz & Golding 2022, Lackner 2014, Cha et al., Lawson 2014, Keshavarz/Hecht/Lawson 2014, Teixeira 2022/2025 (unexpected vection), Berti & Keshavarz 2020, Yates 2014, Cohen 2019, Schmäl 2013.
- Rewrite the "CS vs SS vs MS via vection/disorientation/oculomotor/nausea" sentence (R1 says it's wrong).
- Fix fNIRS background: temporal resolution comparable to fMRI; deep structures (insula/amygdala) not accessible.
- Reframe nausea network around 0 fMRI in our corpus (this is the lever — corpus-grounded retraction, then bridge to MS-nausea + vection literature).
- Addresses: **Critical #5 (part 1), #6**; High #2, #3, #4, #5, #6, #8, #9.
- **Side jobs**:
  - `phase2/new_refs.md` — for each of the ~15 references R1/R2 want added (Reason, Reason & Brand, Oman, Lackner 2014, Keshavarz & Golding 2022, Cha et al., Lawson 2014, Keshavarz/Hecht/Lawson 2014, Teixeira 2022/2025, Berti & Keshavarz 2020, Yates 2014, Cohen 2019, Schmäl 2013, Kennedy/Drexler/Kennedy 2010, Hettinger 1990): collect full bibliographic data + DOI, populate `references.bib`, and add a one-line note on what each ref will support in prose. No improvising claims about what they say.
  - `phase2/r1_factual_check.md` — verify R1's specific assertion that "CS more strongly associated with vection/disorientation vs oculomotor/nausea-dominant SS/MS" is wrong, by checking the primary sources (Kennedy SSQ subscale literature). Document the corrected statement before rewriting.
  - `phase2/fnirs_check.md` — verify R2's claims (fNIRS temporal resolution comparable to fMRI; no deep structures) against 2–3 fNIRS methods reviews.
  - `phase2/theory_engagement_audit.md` — for the 87 papers that mention theory, tabulate which theory they cite and how (explicit framing vs passing mention). Confirms the "75/87 cite sensory conflict" framing is defensible at the per-paper level, not just at aggregate.
  - `phase2/nausea_network_evidence.md` — list the actual fMRI studies the original manuscript cited for the nausea-network claim; check whether they're in-corpus or extra-corpus references.
  - `phase2/theoretical_background.md` — source map for Section II prose (active corpus vs background citations).

### Phase 3 — Methods/PRISMA fixes (M, parallel with Phase 2)
Rewrite `contents/methodology.tex` to document the revised search and screening:
- New PubMed/WoS/Scopus query strings (from `review_scripts/data/V4/notes.md`), explicitly including neurostim terms.
- Reconcile 119 vs 114 duplicate count.
- Add explicit eligibility note about dataset-based prediction papers (Critical #4).
- Add one paragraph on excluded modalities: PET (searched, n=0), MEG (justify why omitted), fMRI (not excluded, just absent in corpus).
- Updated PRISMA figure with the new counts.
- Addresses: **Critical #3, #4**; High #1; R3 minor on PET/MEG.
- **Side jobs**:
  - `phase3/prisma_counts.md` — pull the actual identified / duplicates-removed / screened / excluded / included counts from `review_scripts/data/V4/Stim/` artefacts. Reconcile the 119 vs 114 discrepancy by tracing which value is correct.
  - `phase3/search_query_record.md` — copy the verbatim queries from `notes.md` and the date each database was searched; needed for Methods reproducibility.
  - `phase3/excluded_for_dataset_only.md` — count how many otherwise-eligible papers were excluded for being pure-dataset-reuse (informs the Decision-4 acknowledgment paragraph).

### Phase 4 — All-studies table + study-count integration (M, must precede Phase 5)
Generate a single table of all 92 studies (modality, sample size, VR device, stimulus, sickness measure, key finding) from `PDF_HighLevel_Analysis_GPT54.csv` + `Plots_Analysis_GPT54.csv` via a script in `review_scripts/`. This is the artefact that lets Results cite real counts ("77/92 EEG", "11 neurostimulation: 5 GVS / 3 tDCS / 2 tACS / 1 other") instead of "a substantial body of research". In-text per Decision 3.
- Addresses: **Critical #7**; High #7.
- **Side jobs**:
  - `phase4/paper_bibkey_map.csv` — for every row in the 92-paper corpus, map Citation Key → BibTeX key in `references.bib`. Flag missing or duplicate entries.
  - `phase4/table_column_spec.md` — finalize exact columns and abbreviations (e.g. CS measure as SSQ/FMS/VRSQ code) before generating LaTeX. Confirm landscape rotation needed.
  - `phase4/table_key_finding_rules.md` — define rules for the "key finding" column to keep cells ≤ ~12 words and avoid value-judgment language (per AGENTS.md). Use the `Main Contribution` field from `PDF_HighLevel_Analysis_GPT54.csv` as input; manual review pass before commit.

### Phase 5 — Results rewrite, corpus-grounded (L)
Regenerate every figure and statistic against the V4/Stim corpus *before* touching prose, then rewrite `contents/results.tex` against those outputs:
- Replace narrative with counts everywhere (R1 High #7).
- Move ERPs before fMRI (Medium #1).
- Cut or merge "other physiological correlates" (Medium #2) and Section F (Medium #3) per Phase 0 decisions.
- Integrate new findings: VR-device × alpha (p=0.0036, large effect), × beta (p=0.0146), Egger publication bias (p=0.011).
- Re-thread sensory-conflict / postural-instability / unexpected-vection lenses across modality subsections — this is the "use the theories to structure synthesis" half of Critical #5.
- Frame ML accuracy discussion around sensitivity/specificity and arbitrary sick/non-sick thresholds (High #11).
- Soften sex/gender claims with Kelly 2023, Kourtesis 2023, Lawson & Bolkhovsky 2023 (High #12); rephrase the "not random" baseline-brain claim (High #13).
- Justify eyes-closed critique and propose alternative baselines (High #10).
- Addresses: **Critical #5 (part 2), #7, #8**; High #7, #8, #10, #11, #12, #13; Medium #1, #2, #3.
- **Side jobs (do first, in order)**:
  - `phase5/figure_regeneration.md` — re-run every script under `review_scripts/analysis/` against `V4/Stim/Plots_Analysis_GPT54.csv` + `PDF_HighLevel_Analysis_GPT54.csv`. Produce a manifest mapping each figure in [figures/](figures/) to its generating script, input CSV columns, and the regenerated `unified_statistical_report.txt` section. Diff regenerated outputs against the prior draft's figures and flag any whose interpretation changes. Figures with no script or no clear V4-corpus provenance are flagged for removal or rebuild. **Blocks all other Phase 5 work.**
  - `phase5/claims_audit.md` — walk every quantitative and qualitative claim currently in `contents/results.tex` (and any claim in `abstract.tex`, `introduction.tex`, or `conclusion.tex` that depends on Results). Tag each as `keep` / `revise` / `discard` / `new` against the regenerated stats and the V4 corpus. Output is a checklist; the Results rewrite consumes it row by row. No claim survives into the new draft without an explicit tag.
  - `phase5/stats_provenance.md` — for every statistic that will appear in Results (or be referenced in Abstract/Discussion), record the exact source line in `unified_statistical_report.txt` or the relevant plot's underlying script, the numbers, and the test that produced it. No statistic enters prose without an entry here.
  - `phase5/eyes_closed_alternatives.md` — short literature check on what baselines are recommended for immersive VR EEG (R3 High #10). Identify 2–3 concrete alternatives before writing the critique.
  - `phase5/accuracy_audit.md` — for the classification papers (n=38 per `Primary_objective`), record which report sens/spec, which report AUC/F1, which only report accuracy, and which expose the sick/non-sick threshold. Drives the High #11 rewrite with actual counts.
  - `phase5/gender_findings_audit.md` — list which corpus papers report sex/gender differences vs no differences; check against R1/R2 cited reviews before softening claims.

### Phase 6 — Discussion + Future Directions rewrite (M)
Re-anchor `contents/discussion.tex` and `contents/future.tex` in the cited corpus (no claims without a corpus-derived count or a cited paper). Add objective-measures caveat that CS/MS are intrinsically subjective; list postural sway and pupillometry as candidate objective signals (High #14). Use the Egger result and the publication-bias question to motivate concrete methodological recommendations.

**Content carried forward from Phase 5** (these are interpretive / recommendation-shaped claims that Phase 5 explicitly kept observational so they could be developed here):

- **Eyes-closed baseline critique + alternatives** (R3 minor "Baseline Justification"). Phase 5 §3.1.5 P9 only states the prevalence (5/77 EEG studies). Phase 6 develops the full critique: why eyes-closed differs (alpha rebound — anchor Klimesch 2007 `65LDI5W8`, Barry 2007 `ZVG4XJXN`), and three recommended alternatives (eyes-open static-scene in HMD, pre-stimulus epochs, sham VR exposure) with in-corpus exemplars (Li 2023, Wu 2020, Takeuchi 2018) and a methodological anchor for "EEG works in HMD" (Gramann 2011 `PKWP4ZF7`). Full content already drafted in `phase5/eyes_closed_alternatives.md`.
- **Classification metric/threshold recommendations** (R1 / R3 High #11). Phase 5 §3.3 P22+P26 only state the corpus counts (13/38 accuracy-only, 7/38 sens/spec, 10/38 AUC/F1, 19/38 threshold-exposed). Phase 6 develops the interpretive critique (accuracy is uninformative under class imbalance with arbitrary thresholds) and recommends what classification studies should report.
- **Egger publication-bias interpretation + recommendations**. Phase 5 §3.6 P41 only states p=0.011. Phase 6 develops the caveats (Egger sensitive to heterogeneity in small-study samples) and the recommendations (pre-registration, null-finding venues, larger replication studies). One of the load-bearing pieces of Contribution #3.
- **Gender / sex Discussion paragraph**. Phase 5 §3.4 P33 states the calibrated facts (3/92 F>M, 11/92 male-only, with Kelly/Lawson/Kourtesis context). Phase 6 engages with Kelly 2023's mediation/moderation framework as a *future-directions* prescription: large-sample studies, separate-by-sex reporting even when underpowered, mediator analyses (VIMSSQ, postural instability, IPD, gaming experience). Anchor `phase5/gender_findings_audit.md` + Kelly fulltext.
- **Demoted Section-F content**. Recovery (Woo 2023, Miyazaki 2021 — 1 paragraph), Datasets (Kim 2019, Dasdemir 2023, Demirel 2025 + dataset-only acknowledgement per Decision 9 — 1 paragraph), Cognition (deduplicate against §3.2 ERP content; mention Mimnaugh / Wu / Berger findings in functional-impairment framing — 1 paragraph).

- Addresses: **Critical #8**; High #10, #11, #12, #13, #14; R3 baseline justification; Medium #3.
- **Side jobs**:
  - `phase6/discussion_citation_map.md` — for every paragraph slated for Discussion/Future, list which corpus papers it draws on; flag any paragraph that lacks specific citations before drafting.
  - `phase6/objective_measures_evidence.md` — short note on postural sway and pupillometry as candidate objective CS measures (R1 High #14): a few primary refs + what they actually claim.
  - `phase6/eyes_closed_critique.md` — full draft of the eyes-closed critique paragraph + alternatives. Inputs: `phase5/eyes_closed_alternatives.md`, Barry 2007, Klimesch 2007, Gramann 2011 fulltexts.
  - `phase6/classification_recommendations.md` — reporting-checklist recommendations for the 38-paper classification subset (sens/spec/AUC/F1 minimum set, threshold-disclosure, validation-scheme reporting). Inputs: `phase5/accuracy_audit.md` + audit CSV.
  - `phase6/egger_interpretation.md` — funnel-plot interpretation caveats + concrete pre-registration / replication recommendations. Inputs: `unified_statistical_report.txt` PUB-01 + statistical-bias literature.
  - `phase6/gender_recommendations.md` — Kelly's mediation/moderation framework operationalised as future-directions text. Inputs: Kelly 2023 fulltext, `phase5/gender_findings_audit.md`.
  - `phase6/demoted_content.md` — three short paragraph drafts (Recovery, Datasets, Cognition) with dedup against §3.2 ERPs and §3.5 Mitigation already-cited material.

### Phase 7 — Substantive audit (M, must precede page-fit)
Fact-check the full draft against corpus artefacts and Phase 5–6 side-job notes before any cutting or polish. Anchored on Phase-6 lessons: Egger methodology fix (p=0.036, k=27 — reconcile every Egger mention against `unified_statistical_report.txt` after regen), sway/eye-tracker count re-derived (25/92, not 16), Berger single-lab gender evidence (3/92 papers, one lab), CLF denominator drift (38 vs 41 — see `phase6/classification_recommendations.md`), and unverified `[NEW]` refs flagged in `phase6/ref_verification.md` and `phase6/discussion_citation_map.md`.

Checklist (work through in order; log resolutions in `phase7/substantive_audit.md`):
1. **Stat methodology** — every p-value, effect size, and n in prose matches `stats_provenance.md` / regenerated `unified_statistical_report.txt`; test choice and comparison groups match what the script actually ran (e.g. HMD-vs-non-HMD, Cliff's δ).
2. **Subagent number audit** — re-derive every corpus count quoted in Discussion/Challenges/Future (not only Results); flag any count that came from an LLM pass without a traced CSV query.
3. **Lab-count vs paper-count** — wherever a finding is attributed to "studies," confirm whether the evidence is one lab/protocol repeated (Berger gender block) vs independent replications; rephrase if needed.
4. **Stale-artefact sweep** — grep for retired stats (old alpha p=0.044, old Egger p=0.011, driving-vs-navigation 46.7%, n=41 classification denominator where prose says 38), wrong bibkeys, and figure snippets regenerated from stale scripts (`figures/*.tex`, `age_range_intervals_latex.tex`).
5. **Cross-note consistency** — `change_log.md`, `stats_provenance.md`, and phase side-job notes agree with what landed in `contents/*.tex`; patch prose or notes, not both silently diverging.
6. **Reference verification** — commit or replace every `[NEW]` / `[UNVERIFIED]` entry from Phase 6 (methodology refs in Challenges/Future, Egger/funnel-plot set, Kelly mediators if cited). No citation enters the submission build without DOI confirmed.

- Addresses: corpus-grounded accuracy across all sections; closes Phase-6 verification debt.

### Phase 7b — Page-fit + style sweep (S–M)
Compile, measure against budget, cut. Sweep for value-judgment language and metaphor per AGENTS.md. Verify every figure/table is referenced and every claim has a citation or a corpus count. Flag obvious cross-section repetition (same statistic or contribution bullet stated in multiple sections with divergent wording) for resolution in Phase 8.
- Addresses: Medium #5; AGENTS.md style rules.

### Phase 8 — Polish & second-pass (M)
Items deferred from earlier phases:
- **Abstract and conclusion (holistic rewrite)**: Rewrite `contents/abstract.tex` and `contents/conclusion.tex` in light of the finalized manuscript — not only re-pin `\TODO[abs:*]{...}` placeholders and corpus counts, but realign scope statements, the three contribution bullets, and closing takeaways with what Results and Discussion actually deliver. Keep both sections appropriately high level (no new methods detail, no subsection-by-subsection recap, no detailed results). After drafting, verify they do not re-introduce retired framing (BCI, outdated stats, demoted Section-F themes) or duplicate prose already stated in the Introduction or Discussion.
- **Cross-section consistency audit** (presentation layer; assumes Phase 7 substantive audit is clean): Read abstract, introduction, results, discussion, and conclusion as a set; flag and fix (a) contradictory *framing* or scope statements, (b) terminology drift (cybersickness vs VIMS vs SS) against Decision 2, (c) repeated paragraphs or near-duplicate claims (e.g. Chang comparison, hardware-confounder headline, Egger finding, contribution trio restated with divergent wording). Do not re-litigate corpus counts here — send discrepancies back to Phase 7. Log findings and resolutions in `phase8/consistency_audit.md`.
- **Title sanity check**: only revisit if scope shifted during drafting.
- **Placeholder sweep**: `grep -r "\\\\TODO" contents/` must return zero. Each placeholder resolved against its side-job note.
- **Cross-reference audit**: every `\ref`/`\cite` resolves; every figure/table is referenced from prose at least once.
- **Corpus citation audit** (two-way check):
  - Every paper in the 92-study corpus has a BibTeX entry in `references.bib` and is `\cite`d at least once in the manuscript (most should be reachable via the all-studies table). Any uncited corpus paper is either added to the prose or flagged for deliberate omission with a one-line justification.
  - Any paper that was cited in the prior draft but is no longer in the corpus (see `V3_2025_selected_not_in_V4.csv`) is removed from prose unless it is being cited for a *non-corpus* reason (e.g. a foundational theory citation, an out-of-scope comparison). Each surviving dropped-corpus citation gets a one-line justification.
- **Final style pass**: AGENTS.md formality/objectivity rules, no metaphor, no value judgments.
- **Compile clean** under TVCG template; verify 20-page cap is met with all required elements (biographies, affiliations, index terms).
- **Side jobs**:
  - `phase7/substantive_audit.md` — row-by-row log for the Phase 7 checklist (stat, count, ref, stale-artefact); each row tagged `verified / fixed / deferred-with-justification`.
  - `phase8/abstract_conclusion_outline.md` — target outline for abstract and conclusion (orienting sentence per paragraph, which contribution/result each paragraph reflects, explicit “do not repeat from Intro/Discussion” notes). Ratify before drafting.
  - `phase8/consistency_audit.md` — checklist of cross-section *framing* (contribution wording, terminology, intentional vs accidental repeats); each row tagged `aligned / fixed / intentional-repeat`.
  - `phase8/citation_audit.md` — produced by a script that takes (a) the 92-row corpus, (b) `references.bib`, (c) the list of `\cite` keys actually used in `contents/*.tex`, and outputs three lists: corpus-papers-without-bib-entry, corpus-papers-not-cited-in-prose, and v3-not-v4-papers-still-cited. Each list is reviewed manually and resolved before submission.

### Phase 9 — Response letter (S, draws on `revision_notes/change_log.md`)
Structured **by theme**, not per reviewer (per meeting notes), with a per-comment cross-reference and a diff. Themes likely: framing & terminology, search & scope, theory grounding, all-studies table & corpus counts, methodological audit, missing references, minor corrections. Separate document.

**Phase-5-specific themes to surface explicitly** (gathered during Phase 5 outline work):

- **Hardware confounder reframe** — current paper reports alpha HMD-vs-Screen p=0.044, δ=0.455. Revised draft reports p=0.0036, δ=0.875 (large effect), plus new beta finding (p=0.015, δ=0.664). The headline R3 specifically praised was *understated* in the current paper — flag the upward revision.
- **Gender claim reframe** — emphasize the §3.4 P33 change is **not a retraction** of the women-more-susceptible claim; it is a **calibration to a small effect detectable only in large samples** (Kelly 2023 r≈0.21; Lawson 37/76 = 48.7%; Kourtesis gaming-experience moderation). Useful framing for R1's High #12 / #13.
- **Stim-duration test change** — old L338 (HMD-vs-Screen, U=242, p<0.001, Cohen's d=0.76) replaced with HMD-vs-non-HMD (U=364, p=0.0014, Cliff's δ=−0.467). Explain (a) the comparison rule changed (Screen-only had n=4, too small), (b) Cliff's δ adopted for consistency with the other two hardware tests.
- **Reporting-gap counts placement** — explain why the metric/threshold counts (13/38 / 7/38 / 10/38 / 19/38) live inline in §3.3 instead of in §3.6, per R1's specific direction ("something to consider when talking about accuracies").
- **Eyes-closed prevalence reframe** — the critique stands but the prevalence is 5/77 EEG studies, not the dominant pattern; cite R3's request for justification + alternatives and point at the Phase-6 Challenges paragraph + Barry 2007 + Gramann 2011.
- **FLAG-G dropped finding** — the prior "driving 46.7% vs navigation 15.8% alpha-increase" claim does not reproduce against the V4 corpus (both 33.3%); silently removed from §3.6; mention in response letter for completeness.

**Phase-6-specific themes to surface explicitly** (gathered during Phase 6 outline + audit-of-audit work):

- **Contribution #3 reframe** — the original Egger publication-bias headline was retired. Two distinct issues: (a) the prior methodology entered within-subject and cross-subject accuracies as two non-independent rows per study and imputed n=30 for missing sample sizes, violating Egger's independence assumption; (b) even after the methodology fix (one effect per study, no imputation; corrected p=0.036, k=27), the pool is too small and the corpus too heterogeneous (we ourselves show large hardware effects on band power) to anchor a contribution. The methodological-audit contribution is now anchored on the corpus-direct reporting-gap counts (1/38 LOSO-CV; 19/38 no threshold; 13/38 accuracy-only). The corrected Egger result appears in Challenges as one exploratory sentence. The script fix is in `review_scripts/.../stats_tests.py` `assess_publication_bias`.
- **Discussion + Future wholesale rewrite** — `discussion.tex`, `challenges.tex`, `future.tex` rewritten across 17 paragraph slots. Every Discussion claim is anchored to a corpus count or cited primary source (no remaining "substantial body" / "many studies" phrases). Word count grew by ~755 words across the three files; expected, since reviewer-required content (objective-markers caveat, sex/gender future direction, reporting checklist) had no prior home.
- **Sex/gender as a future direction** (R1 High #12 / #13) — `future.tex` previously contained zero content on sex/gender. Phase 6 F4 adds a paragraph anchored on Kelly et al. 2023, Kourtesis et al. 2023 (cognition-motor), and Lawson & Bolkhovsky 2023, with three prescriptions: sex-stratified outcome reporting, IPD + gaming-experience covariates, multi-site pooled cohorts. Results §3.4 keeps the calibrated F>M count (3/92, single lab, not independently replicated); Discussion-side framing is "no independent replication" rather than "consistently reported."
- **Objective markers as a Discussion subsection** (R1 High #14) — new Discussion subsection "Objective Markers and the Limits of Self-Report." Postural sway anchored on Riccio & Stoffregen 1991 + Stoffregen & Smart 1998 with VR-specific coupling refs (Palmisano 2014, Dennison & D'Zmura 2018, Teixeira 2024); pupillometry on Kourtesis 2023 ×2 with arousal / cognitive-load confounds; 25/92 corpus studies already co-record force-plate, balance-board, eye-tracker, or pupillometry alongside EEG but treat them as covariates rather than candidate ground truth.
- **Section F demotion executed** (Decision 10) — Recovery (2 papers) folded into a final clause of the Objective Markers paragraph; Cognition (4 papers, `Primary_objective == "Cognitive effects"`) folded as context for the same paragraph; Datasets stays in Methods §"Modalities and Dataset-Reuse Studies" (already covered, no Discussion paragraph added).
- **Eyes-closed baseline critique** (R3 baseline-justification) — Phase 6 added a dedicated Challenges paragraph (5/77 EEG corpus prevalence) anchored on Berger 1929, Klimesch 2007, Barry 2007; F1 prescribes three matched alternatives with corpus exemplars (Li 2023 EO-HMD, Wu 2020 pre-stim, Takeuchi 2018 sham-VR).
- **Reporting checklist in Future Directions** (R1 / R3 High #11) — F1 enumerates the minimum reporting set: AUC or balanced accuracy with 95% CI, sens/spec at a stated operating point, class balance, numeric SSQ/FMS cutoff, subject-stratified validation, chance + non-neural feature baselines. Mirrors the C1 critique as a positive prescription.

- Addresses: Editor letter Medium #6.

## Open risks carried into drafting

- **Terminology hybrid** (Decision 2): declines R1's full request. Pre-draft the response-letter justification during Phase 2 so Background prose stays consistent — likely: "imposing a single hierarchy across the corpus would misrepresent cited authors who use different umbrella terms."

## Risks closed

- **TVCG-fit thread** (R1 Major #5) — closed. Practitioner thread is now triangulated across (a) the Intro TVCG-fit paragraph from Phase 1, (b) the explicit Cliff's δ hardware-confounder magnitudes in Challenges §C3 from Phase 6, (c) the Objective Markers Discussion subsection naming signals VR systems can already collect (sway, pupillometry), and (d) the F1 reporting standards aimed at the studies the TVCG audience produces. If reviewers re-raise this, the meta-analytic VR-device finding (Contribution #2) is the load-bearing rebuttal.
