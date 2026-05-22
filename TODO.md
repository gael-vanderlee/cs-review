# Revision TODOs

## Critical

1. `[AE, R1]` Comment: The manuscript framing around `BCI` is not convincing, and the title, abstract, and keywords are affected by that framing.
   - Decision: remove the `BCI` framing.
   - Done: Title changed to "The Neurophysiology of Cybersickness in VR…"; abstract and introduction rewritten around "neuromarkers" as the scope-defining concept; "BCI" removed throughout.
2. `[AE, R1]` Comment: The paper does not clearly establish its novelty relative to `Chang et al. (2023)` or explain why a new review is needed now.
   - Decision: Compare more in depth (scope, number of papers), move comparison to the Intro
   - Done: Chang comparison paragraph added to Introduction with four verified differentiators: corpus size (33 vs 92), search window (2021-09 vs 2025-03), modality coverage (EEG-only vs multi-modal incl. neurostim), and theoretical engagement scope.
3. `[AE, R2, R3]` Comment: The search strategy appears to miss relevant neurostimulation literature, and the manuscript should clarify the scope regarding other modalities such as `PET` and `MEG`.
   - Decision: expand search terms to `Neurostimulation` and `PET`, and no further.
   - Done (search): Search query updated to include neurostimulation terms (tDCS, tACS, TMS, GVS); 0 eligible PET and 0 MEG studies returned. Methods now states this explicitly with the verbatim query and database search dates.
4. `[R3]` Comment: The current eligibility criteria may exclude dataset-based prediction papers, which could make the prediction literature coverage incomplete.
   - Decision: Yes
   - Done: 6 dataset-reuse papers retained in corpus; Methods acknowledges these as borderline inclusions and notes that pure-dataset ML prediction is a related but distinct literature focused on classification benchmarking rather than neuromarker discovery. Discussion pass still pending.
5. `[AE, R1, R2, R3]` Comment: The theoretical grounding is not strong enough, and the theories introduced early are not sufficiently used to structure the synthesis in the Results and Discussion.
   - Decision: add papers to the theory discussion.
   - Decision: the results and discussion will explicitly address that an overwhelming majority of papers rely on sensory conflict theory.
   - Done (Background): Background rewritten with distinct theoretical accounts (sensory conflict, postural instability, unexpected vection, poison/toxin, display-specific, oculomotor, predictive coding) and corpus theory-engagement counts (73/92 explicit, 75/87 cite sensory conflict). Results/Discussion grounding pending.
6. `[R1]` Comment: The terminology around `cybersickness`, `VIMS`, `simulator sickness`, and `motion sickness` is not sufficiently precise, and Reviewer 1 challenges the current hierarchy.
   - Decision: use the term used by each cited paper rather than enforcing a single hierarchy across the manuscript.
   - Done: Hybrid policy adopted — VIMS introduced as umbrella term in Background/Theory; each cited paper's own term preserved in Results.
7. `[R1, R3]` Comment: The synthesis of the included studies is difficult to follow, and a table of all reviewed studies would make the patterns, modalities, and sickness measures much clearer.
   - Decision: add a table of all studies.
   - Done (decision): Table will appear in-text. Generation pending.
8. `[R3]` Comment: The Discussion and Future Directions sections are too narrative and are not grounded enough in the reviewed corpus.

## High priority

1. `[R3]` Comment: There is a PRISMA inconsistency: the text reports `119` duplicates removed, while Figure 1 reports `114`.
   - Done (prose): V3 counts replaced with the V4/Stim PRISMA flow (443 identified, 224 duplicates removed, 219 screened, 119 excluded at title/abstract, 100 sought for retrieval, 8 not retrieved, 92 included). Figure regeneration pending (flagged with \TODO[prisma:figure]).
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
   - Done (Abstract + Background): Explicit counts added (77 EEG, 4 fNIRS, 11 neurostim-only, 0 fMRI/MEG/PET). Remaining vague phrases in Results/Discussion pending.
8. `[R1]` Comment: The `nausea network` discussion may be overstated given the limited number of `fMRI` studies and should be connected to broader nausea and vection literature.
   - Done: Nausea-network discussion reframed as extra-corpus background given absence of fMRI studies in the corpus; connected to broader MS-nausea and vection literature.
9. `[R2]` Comment: The `fNIRS` background needs correction, especially regarding temporal resolution and the inability to measure deep structures such as the amygdala or insula.
   - Done: Temporal resolution corrected (comparable to fMRI, not superior); deep-structure inaccessibility stated explicitly.
10. `[R3]` Comment: The critique of the `eyes-closed` baseline needs stronger justification and should explain what alternative baselines are more appropriate in VR studies.
11. `[R1, R3]` Comment: The machine learning discussion relies too heavily on `accuracy` and should better reflect issues such as sensitivity/specificity and arbitrary sick versus non-sick thresholds.
12. `[R1, R2]` Comment: Some claims are too strong, especially around sex or gender differences and the interpretation of susceptibility markers.
13. `[R1]` Comment: The claim that susceptibility is `not random` and rooted in measurable baseline brain differences is too strong for the current evidence base.
14. `[R1]` Comment: Objective measures of cybersickness should be discussed more carefully because cybersickness and motion sickness are subjective phenomena.

## Medium priority

1. `[R1]` Comment: The organization of the modality subsections could be improved, including moving `ERP` before `fMRI`.
2. `[R1]` Comment: The `other physiological correlates` section appears incomplete and may not contribute enough to the overall argument.
   - Done: Section removed; postural sway and pupillometry will be mentioned briefly in Discussion.
3. `[R1]` Comment: Section `F` may not be necessary.
   - Done: Section F split — Confounding Factors promoted to a top-level Results subsection; Recovery/Datasets/Cognition demoted to 1–2 Discussion paragraphs.
4. `[R1, AE]` Comment: The manuscript's fit for `TVCG` was questioned because of the current framing and breadth.
   - Done (partial): TVCG-fit paragraph added to Introduction linking the VR-hardware confounder finding to practitioner implications. Full argument to be expanded in Discussion.
5. `[Editor letter]` Comment: The revised manuscript must stay within TVCG page limits and include all required submission elements.
   - Done (decision): 20-page hard cap confirmed; per-section budget allocated. Compliance check pending.
6. `[Editor letter]` Comment: The revision should be accompanied by a separate, specific response to every Associate Editor and reviewer comment.
