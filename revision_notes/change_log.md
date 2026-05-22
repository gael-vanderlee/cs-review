# Revision change log

Append-only. One line per change. Feeds the Phase 9 response letter.

Format: `YYYY-MM-DD | phase | file:loc | reviewer-tag | change`

## Phase 0 — decisions

- 2026-05-21 | 0 | revision_plan.md | Crit#1 | Title changed to "The Neurophysiology of Cybersickness in Virtual Reality: A Systematic Review of Neural Correlates and Neurostimulation" (BCI framing removed).
- 2026-05-21 | 0 | revision_plan.md | Crit#6, R1-Maj#2 | Terminology policy: VIMS as umbrella in Background, each paper's own term in Results.
- 2026-05-21 | 0 | revision_plan.md | Crit#7, R1-Maj#3 | All-studies table will be in-text.
- 2026-05-21 | 0 | revision_plan.md | Crit#4, R3-Maj | Dataset-only prediction papers: out of scope; acknowledge tangentially.
- 2026-05-21 | 0 | revision_plan.md | Crit#3, R3-min | PET/MEG: searched in V4/Stim query, 0 eligible; will state plainly in Methods.
- 2026-05-21 | 0 | revision_plan.md | R1-other | Section F: split — Confounding Factors promoted, Recovery/Datasets/Cognition demoted to Discussion.
- 2026-05-21 | 0 | revision_plan.md | R1-other | "Other physiological correlates" section: removed; covered briefly in Discussion.

## Phase 1 — reframing pass

- 2026-05-21 | 1 | review_bci_cs.tex | infra | Added `\TODO[tag]{value}` placeholder macro and `revision_notes/` scaffolding.
- 2026-05-21 | 1 | contents/abstract.tex | Crit#1, Crit#3, Crit#7, Crit#8, R1-Maj#1, R1-Maj#4, R1-Hi#7, R3-Maj | Rewrote abstract: removed BCI framing, reframed around neuromarkers; updated corpus to 92 with modality breakdown; surfaced VR-device × band-power meta-analytic findings and Egger publication bias; added Chang novelty clause; flagged methodological audit. Both Phase 1 placeholders resolved inline (search cut-off 27 March 2025; Chang corpus N=33).
- 2026-05-21 | 1 | revision_notes/chang_comparison.md | R1-Maj#4, AE-novelty | Completed Chang 2023 side job; comparison matrix verified against PDF with page refs.
- 2026-05-21 | 1 | revision_notes/tvcg_fit_thread.md | R1-Maj#5 | Completed TVCG-fit side job; selected 5 threads, with Threads 1 & 3 leading Intro closer and all 5 to land in Discussion (Phase 6).
- 2026-05-21 | 1 | review_bci_cs.tex:84 | Crit#1 | Updated journal title to final Decision 1 wording.
- 2026-05-21 | 1 | title_page.tex:12 | Crit#1 | Updated cover-page title to match.
- 2026-05-21 | 1 | contents/introduction.tex | Crit#1, Crit#2, R1-Maj#1, R1-Maj#4, R1-Maj#5, AE-novelty | Rewrote Introduction: removed BCI framing and the R1-flagged inaccurate CS-vs-SS-vs-MS sentence (now deferred to Section II per Phase 2); introduced "neuromarkers" frame sentence; added Chang comparison paragraph with verified corpus deltas (33 vs 92, 2021-09 vs 2025-03, EEG-only vs multi-modal incl. neurostim); added three contributions; added TVCG-fit takeaway sentence (Thread 1 from `tvcg_fit_thread.md`); added section roadmap. Compiles clean, 17 pp, no undefined refs.
- 2026-05-21 | 1 | contents/introduction.tex, revision_notes/chang_comparison.md | R1-Maj#4, AE-novelty | Added a fourth Chang differentiator: this review engages with theoretical frameworks, terminology, and field-level methodological critique — Chang's RQs are narrowly findings/pipeline-focused. Updated comparison matrix with corresponding rows.

## Phase 2 — theory/background rewrite

- 2026-05-22 | 2 | revision_notes/new_refs.md, revision_notes/r1_factual_check.md, revision_notes/fnirs_check.md, revision_notes/theory_engagement_audit.md, revision_notes/nausea_network_evidence.md | Crit#5, Crit#6, R1-Maj#2, R1-theory, R2-fNIRS, R3-theory | Added Phase 2 verification notes for new references, terminology/symptom correction, fNIRS limits, corpus theory engagement, and nausea-network evidence.
- 2026-05-22 | 2 | contents/theoretical.tex | Crit#5, Crit#6, R1-Maj#2, R1-theory, R2-theory | Rewrote Section II background: added VIMS/cybersickness terminology hierarchy; replaced weak sensory-conflict citations with Reason/Reason & Brand/Oman; separated sensory conflict, postural instability, unexpected vection, poison/toxin, display-specific, oculomotor, and predictive-coding accounts; added corpus counts for theory engagement.
- 2026-05-22 | 2 | contents/theoretical.tex | R1-nausea, R2-fNIRS, R3-modalities | Rewrote modality background: corrected fNIRS temporal/depth language; stated 77 EEG, 4 fNIRS, 11 neurostimulation-only, and 0 fMRI/MEG/PET in the V4/Stim corpus; reframed fMRI/nausea-network references as extra-corpus background.
- 2026-05-22 | 2 | contents/introduction.tex, contents/challenges.tex | Crit#1, Crit#6, R1-symptoms, R3-theory | Aligned linked prose with the Phase 2 terminology policy and removed the R1-flagged implication that vection is a symptom or that cybersickness lacks nausea/oculomotor involvement.
- 2026-05-22 | 2 | contents/theoretical.tex, revision_notes/new_refs.md, revision_notes/fnirs_check.md, revision_notes/nausea_network_evidence.md | R2-fNIRS, R1-nausea | Reconciled Phase 2 prose with subagent source checks: corrected active V4/Stim fNIRS corpus citations to Yeo 2024, Yamamura 2021, Yamamura 2020, and Tanimura 2019; moved Zhang 2020 and Gavgani 2018 to non-active background status; re-verified Schmäl 2013 citation metadata.
- 2026-05-22 | 2 | contents/introduction.tex, revision_notes/theoretical_background.md | R1-Maj#2, R2-fNIRS, R3-modalities | Reconciled diff-review findings: removed fMRI from the Introduction's eligible recording-corpus list and updated the Phase 2 source map to distinguish active V4/Stim fNIRS rows from legacy/background fNIRS references.
- 2026-05-22 | 2 | contents/theoretical.tex, contents/results.tex, revision_notes/new_refs.md, revision_notes/nausea_network_evidence.md, revision_notes/theoretical_background.md | infra | Synced manuscript and Phase 2 notes with current Zotero-exported citekeys for Cohen 2019 and Yamamura 2021 after bibliography regeneration.
- 2026-05-22 | 2 | contents/theoretical.tex, contents/introduction.tex, contents/challenges.tex, AGENTS.md | style, R3-theory | Removed internal V4/Stim labels and all corpus-derived counts from Background; AGENTS.md now documents manuscript vs internal naming and background-vs-results boundaries.
- 2026-05-22 | 2 | contents/theoretical.tex | R3-modalities | Removed fMRI and nausea-network background prose; fNIRS paragraph no longer contrasts with fMRI.
