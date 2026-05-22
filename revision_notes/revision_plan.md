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

14. **Contributions (3, locked)**:
    1. Most current and broadest systematic synthesis of cybersickness neuromarkers in VR (92 studies, includes neurostimulation alongside neuroimaging, post-dates Chang 2023).
    2. Meta-analytic evidence that VR display hardware modulates band-power responses — VR-device type significantly affects alpha (p=0.0036, large effect) and beta (p=0.0146); reframes prior contradictions in the EEG-cybersickness literature as partly hardware-attributable.
    3. Methodological audit of the field — detection of publication bias (Egger's test, p=0.011), prevalence of accuracy-only ML reporting, weak baselines — leading to concrete reporting recommendations.

## Working conventions

- **Folder layout**: phase-specific side-job notes live in `revision_notes/phaseN/` (N = 0–9). Cross-phase artefacts stay in `revision_notes/`: `revision_plan.md`, `change_log.md`, and `assets/` (PDFs, Zotero exports).
- **Placeholders**: every unresolved value in source uses `\TODO[tag]{current-or-best-guess}`, rendered bright red in the PDF and grep-able from `contents/`. Tags use `topic:specifier` form (e.g. `\TODO[stat:alpha-p]{0.0036}`, `\TODO[chang:corpus-size]{n=??}`). Phase 8 sweeps `\TODO` to zero.
- **Side jobs**: each phase has a "Side jobs" subsection listing verification / info-gathering tasks that must complete *before* drafting prose for that phase. Outputs land in `revision_notes/phaseN/<topic>.md` as bullet notes, not prose. Rule: no prose claim enters a `.tex` file without a corresponding side-job note backing it.
- **Change log**: every phase appends to `revision_notes/change_log.md` (one line per change, tagged with the reviewer comment it addresses). Feeds Phase 9 response letter directly. Make sure to also keep the `TODO.md` file up to date

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
- **Second-pass deferred to Phase 8**: abstract numbers re-pinned after Phases 5–6 stabilize.

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
- **Side jobs**:
  - `phase5/stats_provenance.md` — for every statistic that will appear in Results (or be referenced in Abstract/Discussion), record the exact source line in `unified_statistical_report.txt` or the relevant plot's underlying script, the numbers, and the test that produced it. No statistic enters prose without an entry here.
  - `phase5/eyes_closed_alternatives.md` — short literature check on what baselines are recommended for immersive VR EEG (R3 High #10). Identify 2–3 concrete alternatives before writing the critique.
  - `phase5/accuracy_audit.md` — for the classification papers (n=38 per `Primary_objective`), record which report sens/spec, which report AUC/F1, which only report accuracy, and which expose the sick/non-sick threshold. Drives the High #11 rewrite with actual counts.
  - `phase5/gender_findings_audit.md` — list which corpus papers report sex/gender differences vs no differences; check against R1/R2 cited reviews before softening claims.

### Phase 6 — Discussion + Future Directions rewrite (M)
Re-anchor `contents/discussion.tex` and `contents/future.tex` in the cited corpus (no claims without a corpus-derived count or a cited paper). Add objective-measures caveat that CS/MS are intrinsically subjective; list postural sway and pupillometry as candidate objective signals (High #14). Use the Egger result and the publication-bias question to motivate concrete methodological recommendations.
- Addresses: **Critical #8**; High #11, #14.
- **Side jobs**:
  - `phase6/discussion_citation_map.md` — for every paragraph slated for Discussion/Future, list which corpus papers it draws on; flag any paragraph that lacks specific citations before drafting.
  - `phase6/objective_measures_evidence.md` — short note on postural sway and pupillometry as candidate objective CS measures (R1 High #14): a few primary refs + what they actually claim.

### Phase 7 — Page-fit + style sweep (S–M)
Compile, measure against budget, cut. Sweep for value-judgment language and metaphor per AGENTS.md. Verify every figure/table is referenced and every claim has a citation or a corpus count.
- Addresses: Medium #5; AGENTS.md style rules.

### Phase 8 — Polish & second-pass (M)
Items deferred from earlier phases:
- **Abstract second pass**: re-pin numbers (`\TODO[abs:*]{...}` placeholders), tighten now that Results/Discussion are final.
- **Title sanity check**: only revisit if scope shifted during drafting.
- **Placeholder sweep**: `grep -r "\\\\TODO" contents/` must return zero. Each placeholder resolved against its side-job note.
- **Cross-reference audit**: every `\ref`/`\cite` resolves; every figure/table is referenced from prose at least once.
- **Corpus citation audit** (two-way check):
  - Every paper in the 92-study corpus has a BibTeX entry in `references.bib` and is `\cite`d at least once in the manuscript (most should be reachable via the all-studies table). Any uncited corpus paper is either added to the prose or flagged for deliberate omission with a one-line justification.
  - Any paper that was cited in the prior draft but is no longer in the corpus (see `V3_2025_selected_not_in_V4.csv`) is removed from prose unless it is being cited for a *non-corpus* reason (e.g. a foundational theory citation, an out-of-scope comparison). Each surviving dropped-corpus citation gets a one-line justification.
- **Final style pass**: AGENTS.md formality/objectivity rules, no metaphor, no value judgments.
- **Compile clean** under TVCG template; verify 20-page cap is met with all required elements (biographies, affiliations, index terms).
- **Side jobs**:
  - `phase8/citation_audit.md` — produced by a script that takes (a) the 92-row corpus, (b) `references.bib`, (c) the list of `\cite` keys actually used in `contents/*.tex`, and outputs three lists: corpus-papers-without-bib-entry, corpus-papers-not-cited-in-prose, and v3-not-v4-papers-still-cited. Each list is reviewed manually and resolved before submission.

### Phase 9 — Response letter (S, draws on `revision_notes/change_log.md`)
Structured **by theme**, not per reviewer (per meeting notes), with a per-comment cross-reference and a diff. Themes likely: framing & terminology, search & scope, theory grounding, all-studies table & corpus counts, methodological audit, missing references, minor corrections. Separate document.
- Addresses: Editor letter Medium #6.

## Open risks carried into drafting

- **TVCG-fit thread** (R1 Major #5): removing BCI strengthens scientific framing but weakens the "belongs in TVCG" argument. Compensated by the explicit VR-hardware/practitioner thread seeded in Phase 1 (`phase1/tvcg_fit_thread.md`) and closed in Phase 6 Discussion. If reviewers re-raise this, the meta-analytic VR-device finding (Contribution #2) is the load-bearing rebuttal.
- **Terminology hybrid** (Decision 2): declines R1's full request. Pre-draft the response-letter justification during Phase 2 so Background prose stays consistent — likely: "imposing a single hierarchy across the corpus would misrepresent cited authors who use different umbrella terms."
