# Revision TODOs

## Critical

1. `[AE, R1]` Comment: The manuscript framing around `BCI` is not convincing, and the title, abstract, and keywords are affected by that framing.
   - Decision: remove the `BCI` framing.
   - Done: Title changed to "The Neurophysiology of Cybersickness: A Systematic Review of Neuromarkers, Neurostimulation, and Reporting Practice in Virtual Reality"; abstract and introduction rewritten around "neuromarkers" as the scope-defining concept; "BCI" removed throughout.
2. `[AE, R1]` Comment: The paper does not clearly establish its novelty relative to `Chang et al. (2023)` or explain why a new review is needed now.
   - Decision: Compare more in depth (scope, number of papers), move comparison to the Intro
   - Done (Intro): Chang comparison paragraph with four verified differentiators: corpus size (33 vs 92), search window (2021-09 vs 2025-03), modality coverage (EEG-only vs multi-modal incl. neurostim), and theoretical engagement scope.
   - Done (Discussion): Phase 6 repurposed the Chang paragraph to a findings-level comparison (delta/theta reproduce at 16/30 and 20/35; alpha inconsistency partly resolves once HMD vs screen is accounted for, cross-ref §3.6).
3. `[AE, R2, R3]` Comment: The search strategy appears to miss relevant neurostimulation literature, and the manuscript should clarify the scope regarding other modalities such as `PET` and `MEG`.
   - Decision: expand search terms to `Neurostimulation` and `PET`, and no further.
   - Done (search): Search query updated to include neurostimulation terms (tDCS, tACS, TMS, GVS); 0 eligible PET and 0 MEG studies returned. Methods now states this explicitly with the verbatim query and database search dates.
4. `[R3]` Comment: The current eligibility criteria may exclude dataset-based prediction papers, which could make the prediction literature coverage incomplete.
   - Decision: Yes
   - Done: 6 dataset-reuse papers retained in corpus; Methods acknowledges these as borderline inclusions and notes that pure-dataset ML prediction is a related but distinct literature focused on classification benchmarking rather than neuromarker discovery. Phase 6 confirmed the Methods coverage is sufficient; no separate Discussion paragraph added (would duplicate Methods).
5. `[AE, R1, R2, R3]` Comment: The theoretical grounding is not strong enough, and the theories introduced early are not sufficiently used to structure the synthesis in the Results and Discussion.
   - Decision: add papers to the theory discussion.
   - Decision: the results and discussion will explicitly address that an overwhelming majority of papers rely on sensory conflict theory.
   - Done (Background): Background rewritten with distinct theoretical accounts (sensory conflict, postural instability, unexpected vection, poison/toxin, display-specific, oculomotor, predictive coding) and corpus theory-engagement counts (73/92 explicit, 75/87 cite sensory conflict).
   - Done (Results): Phase 5 threaded sensory-conflict, postural-instability, and unexpected-vection lenses across modality subsections.
   - Done (Discussion): Phase 6 anchors the Objective Markers paragraph on the postural-instability account (Riccio & Stoffregen 1991; Stoffregen & Smart 1998); the Conceptual Variability paragraph in Challenges explicitly states that few studies return to their etiological theory when interpreting their findings.
6. `[R1]` Comment: The terminology around `cybersickness`, `VIMS`, `simulator sickness`, and `motion sickness` is not sufficiently precise, and Reviewer 1 challenges the current hierarchy.
   - Decision: use the term used by each cited paper rather than enforcing a single hierarchy across the manuscript.
   - Done: Hybrid policy adopted — VIMS introduced as umbrella term in Background/Theory; each cited paper's own term preserved in Results.
7. `[R1, R3]` Comment: The synthesis of the included studies is difficult to follow, and a table of all reviewed studies would make the patterns, modalities, and sickness measures much clearer.
   - Decision: add a table of all studies.
   - Done: Generated landscape longtable of all 92 studies (8 columns: Ref, Modality, N, VR device, Stimulus, CS measure, Objective, Topic) at `contents/tables/all_studies.tex`, `\input` from Results intro. Spans 2 landscape pages (tightened in Phase 4 from 4→2 pages via Topic column + raggedright). Per-row cells hand-written from `Main Contribution` per `revision_notes/phase4/table_key_finding_rules.md`; all ≤8 words, banned-word audit clean.
8. `[R3]` Comment: The Discussion and Future Directions sections are too narrative and are not grounded enough in the reviewed corpus.
   - Done: Phase 6 wholesale rewrite of `discussion.tex`, `challenges.tex`, `future.tex` (17 paragraph slots). Every Discussion claim anchored to a corpus count (16/30 delta, 20/35 theta, 16/92 sway/eye-tracker co-recording, 5/77 eyes-closed baseline, 13/38 accuracy-only, 19/38 no threshold, 8/38 numeric cutoff, 1/38 LOSO-CV, 58/72 ≤32 channels, 14/72 ≤10 channels, 43/77 no reference electrode, 59/77 no notch filter, 11/92 male-only, 12.8/22.1 min stimulus-duration confound) or a cited primary source. Chang comparison repurposed from scope-recap (already in Intro) to findings-comparison.
   - Done (infra): Egger publication-bias headline formally dropped in Phase 7 (small k, high corpus heterogeneity); the paper's methodological-audit contribution is anchored on the reporting-gap counts above. Egger sentence absent from contents/; corresponding refs (Egger, Sterne, Peters, Macaskill, Duval-Tweedie, Poldrack) confirmed absent from `references.bib`.

## High priority

1. `[R3]` Comment: There is a PRISMA inconsistency: the text reports `119` duplicates removed, while Figure 1 reports `114`.
   - Done (prose): V3 counts replaced with the V4/Stim PRISMA flow (443 identified, 224 duplicates removed, 219 screened, 119 excluded at title/abstract, 100 sought for retrieval, 8 not retrieved, 92 included). Figure regeneration completed and \TODO placeholders resolved in Phase 8.
2. `[R1, R2]` Comment: Important references are missing across the theory and background sections, including foundational motion sickness references and more appropriate review sources.
   - Done: ~15 new references added and verified (Reason 1988/2002, Reason & Brand 1975, Oman 1990, Lackner 2014, Keshavarz & Golding 2022, Teixeira 2022/2025, Berti & Keshavarz 2020, Yates 2014, Cohen 2019, Schmäl 2013, Kennedy/Drexler/Kennedy 2010, Hettinger 1990, Lawson 2014, Keshavarz/Hecht/Lawson 2014).
3. `[R1]` Comment: The manuscript refers to a `vection theory` of motion sickness, but Reviewer 1 argues this is not a correct characterization and suggests engaging instead with work on unexpected vection.
   - Done: "Vection theory" framing removed; Background now presents an unexpected-vection account citing Teixeira and Berti & Keshavarz.
4. `[R1]` Comment: The statement contrasting cybersickness with simulator sickness or motion sickness using `vection`, `disorientation`, `oculomotor`, and `nausea` is not accurate as written.
   - Done: Inaccurate sentence removed and replaced with an accurate characterization verified against primary sources.
5. `[R1]` Comment: The sensory conflict theory references are weak, and the poison theory is described as though it competes with mechanistic theories of motion sickness.
   - Done: Weak sensory-conflict citations replaced with Reason 1988/2002, Reason & Brand 1975, Oman 1990; poison/toxin theory repositioned as a "why" hypothesis rather than a mechanistic competitor.
6. `[R1]` Comment: The `FMS` should cite the original source rather than only later papers that used the scale.
   - Done: Keshavarz & Hecht 2011 added as the original FMS source.
7. `[R1]` Comment: The manuscript should report clearer study counts in the text, for example how many included studies used `EEG` or `fMRI`, and should replace vague phrases such as `a substantial body of research`.
   - Done (Abstract + Background): Explicit counts added (77 EEG, 4 fNIRS, 11 neurostim-only, 0 fMRI/MEG/PET).
   - Done (Results): Phase 5 replaced vague phrases throughout with corpus counts (sample sizes, modality breakdowns, rhythm-change percentages, classification counts).
   - Done (Discussion + Future): Phase 6 grounds every claim in a corpus count or a cited primary source; no remaining "substantial body" / "many studies" / "a number of papers" phrases.
8. `[R1]` Comment: The `nausea network` discussion may be overstated given the limited number of `fMRI` studies and should be connected to broader nausea and vection literature.
   - Done: Nausea-network discussion reframed as extra-corpus background given absence of fMRI studies in the corpus; connected to broader MS-nausea and vection literature.
9. `[R2]` Comment: The `fNIRS` background needs correction, especially regarding temporal resolution and the inability to measure deep structures such as the amygdala or insula.
   - Done: Temporal resolution corrected (comparable to fMRI, not superior); deep-structure inaccessibility stated explicitly.
10. `[R3]` Comment: The critique of the `eyes-closed` baseline needs stronger justification and should explain what alternative baselines are more appropriate in VR studies.
    - Done (Results): Phase 5 reports the corpus prevalence (5/77 EEG studies use eyes-closed resting; 6 if eyes-open + eyes-closed composites are counted) in §3.1.5.
    - Done (Challenges): Phase 6 added a dedicated eyes-closed paragraph in Challenges anchored on Berger 1929, Klimesch 2007, and Barry 2007 — establishes that closing the eyes elicits a large posterior alpha increase relative to eyes-open and that the VR exposure condition (eyes-open inside an HMD) is not matched on visual input, oculomotor state, or vigilance.
    - Done (Future): Three matched alternatives recommended in Future Directions with corpus exemplars — eyes-open resting with HMD on a static scene (Li 2023), pre-stimulus segment (Wu 2020), sham non-nauseogenic VR exposure (Takeuchi 2018).
11. `[R1, R3]` Comment: The machine learning discussion relies too heavily on `accuracy` and should better reflect issues such as sensitivity/specificity and arbitrary sick versus non-sick thresholds.
    - Done (Results): Phase 5 added inline reporting-gap counts in Results §3.3 (38-paper classification subset: 13/38 accuracy-only, 7/38 sens/spec, 10/38 AUC/F1, 19/38 expose threshold, 8/38 numeric cutoff, 1/38 LOSO-CV).
    - Done (Challenges): Phase 6 C1 paragraph develops the critique anchored on Saito & Rehmsmeier 2015 (PR vs ROC under imbalance), Combrisson & Jerbi 2015 (empirical chance level), and Varoquaux 2018 (subject-leakage in k-fold).
    - Done (Future): Phase 6 F1 minimum reporting set: primary AUC or balanced accuracy with 95% CI; sensitivity/specificity at a stated operating point; class balance; numeric SSQ/FMS cutoff; subject-stratified validation (LOSO or held-out subjects); chance and non-neural feature baselines.
    - Done (Contribution #3): Reframed away from the prior Egger publication-bias headline. Two distinct issues with the original analysis: (a) the prior methodology double-counted within-subject and cross-subject accuracies as two non-independent rows per study and imputed n=30 for missing sample sizes, violating Egger's independence assumption; (b) even after the methodology fix (one effect per study, no imputation; corrected p=0.036, k=27), the pool is too small and the corpus too heterogeneous (we ourselves show large hardware effects on band power) to anchor a contribution. Phase 7 formally dropped the Egger sentence from contents/ and confirmed the corresponding refs (Egger 1997, Sterne, Peters, Macaskill, Duval-Tweedie, Poldrack) are absent from `references.bib`. The methodological-audit contribution is now anchored on the corpus-direct reporting-gap counts above.
12. `[R1, R2]` Comment: Some claims are too strong, especially around sex or gender differences and the interpretation of susceptibility markers.
    - Done (Results): Phase 5 calibrated the gender claim in Results §3.4 — three F>M reports (all from a single laboratory, not independently replicated), 11/92 male-only samples, 15/92 sex not reported. Anchored on Kelly 2023, Kourtesis 2023 (cognition-motor), Lawson & Bolkhovsky 2023.
    - Done (Future): Phase 6 F4 develops the future-directions paragraph around Kelly et al.'s mediation/moderation framework with three concrete prescriptions: sex-stratified outcome reporting, interpupillary-distance and gaming-experience covariates, multi-site pooled cohorts.
13. `[R1]` Comment: The claim that susceptibility is `not random` and rooted in measurable baseline brain differences is too strong for the current evidence base.
    - Done (Results): Phase 5 replaced the "not random" closing of §3.4 with a calibrated statement that neural correlates of susceptibility are measurable but demographic moderators remain weak and the corpus is underpowered for either as a deployable biomarker.
14. `[R1]` Comment: Objective measures of cybersickness should be discussed more carefully because cybersickness and motion sickness are subjective phenomena.
    - Done (Discussion): Phase 6 dedicates a Discussion subsection ("Objective Markers and the Limits of Self-Report") stating that cybersickness has no diagnostic biomarker and that ground truth is self-report. Postural sway is presented as the theoretically anchored candidate (postural-instability account; Riccio & Stoffregen 1991, Stoffregen & Smart 1998; VR-specific coupling in Palmisano 2014, Dennison & D'Zmura 2018, Teixeira 2024). Pupillometry is presented as a second candidate (Kourtesis 2023 × 2) with arousal and cognitive-load confounds named. Corpus context (re-derived in Phase 7): 16 of 92 corpus studies already co-record force-plate, balance-board, eye-tracker, or pupillometry alongside EEG but typically as covariates rather than as candidate ground truth.
    - Done (Future): F5 reframes these candidates as outcome variables (rather than covariates) and adds heart-rate variability, electrodermal activity, and head-motion dynamics as further candidates whose corpus-level predictive value is not yet quantified.

## Medium priority

1. `[R1]` Comment: The organization of the modality subsections could be improved, including moving `ERP` before `fMRI`.
   - Done (Results): Phase 5 reordered Results §3.2 to put ERPs before fNIRS (no fMRI subsection in the V4/Stim corpus, so the reviewer's "ERP before fMRI" intent maps to ERP before fNIRS).
2. `[R1]` Comment: The `other physiological correlates` section appears incomplete and may not contribute enough to the overall argument.
   - Done (Results): Phase 5 removed the standalone subsection.
   - Done (Discussion + Future): Phase 6 "Objective Markers and the Limits of Self-Report" subsection covers sway (postural-instability account) and pupillometry (with confounds); Future F5 prescribes treating them as outcome variables.
3. `[R1]` Comment: Section `F` may not be necessary.
   - Done (Results): Confounding Factors promoted to standalone §3.6 (Phase 5).
   - Done (Discussion + Future): re-homed demoted themes — recovery (Woo, Miyazaki) in Discussion objective-markers closing + Future longitudinal paragraph; cognition (Mimnaugh, Wu, Xu, Berger 2025) folded into objective-markers opening; public datasets (Kim, Dasdemir, Demirel) in Future F1 open-science paragraph; dataset-reuse scope stays in Methods only.
4. `[R1, AE]` Comment: The manuscript's fit for `TVCG` was questioned because of the current framing and breadth.
   - Done (Intro): TVCG-fit paragraph added to Introduction linking the VR-hardware confounder finding to practitioner implications.
   - Done (Discussion + Future): Phase 6 reinforces the practitioner thread via (a) the hardware-confounder uplift in Challenges with explicit Cliff's δ magnitudes for HMD vs screen (alpha and beta), (b) the objective-markers paragraph that names sway and pupillometry as candidate signals VR systems can already collect, and (c) the F1 reporting standards aimed at studies the TVCG audience produces.
5. `[Editor letter]` Comment: The revised manuscript must stay within TVCG page limits and include all required submission elements.
   - Done (decision): 20-page hard cap confirmed; per-section budget allocated. Compliance check completed in Phase 8 (manuscript compiles to exactly 20 pages).
6. `[Editor letter]` Comment: The revision should be accompanied by a separate, specific response to every Associate Editor and reviewer comment.
