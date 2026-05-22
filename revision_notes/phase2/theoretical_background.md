# Theory / background — source map

Index of literature relevant to `contents/theoretical.tex`. **Not** drafting instructions — look up papers here, fetch via Zotero MCP, read, then decide usage.

**Manuscript file:** `contents/theoretical.tex` (two subsections: etiology, neuroimaging modalities).  
**Related prose elsewhere:** `contents/introduction.tex` (terminology deferral to `\ref{sec:theoretical}`), `contents/challenges.tex` (symptom-profile cites).  
**Reviewer text:** `reviewer_feedback.txt` (R1/R2 theory-related comments).  
**BibTeX:** `references.bib` (verify citekeys after Zotero export; some duplicates).

---

## Fetching papers (Zotero MCP)

| Step | Tool | Argument |
|------|------|----------|
| Resolve citekey → item | `zotero_search_by_citation_key` | `citekey`: e.g. `omanMotionSicknessSynthesis1990` |
| Metadata / abstract | `zotero_get_item_metadata` | `item_key`: from table below (column **ZK**) |
| Full PDF text | `zotero_get_item_fulltext` | same `item_key` — large; use when needed |
| Search by author/year | `zotero_search_items` | `query`: e.g. `Kennedy 2010` (short queries work best) |

If citekey lookup fails, use **ZK** from this file or search by title fragment.

**PDF in library:** most rows marked `pdf`; `reasonMotionSickness1975` has metadata only (no attachment).

---

## Topic tags (legend)

| Tag | Meaning |
|-----|---------|
| `terminology` | MS, VIMS, cybersickness, simulator sickness, diagnostic labels |
| `symptoms` | SSQ N/O/D, symptom profiles, vection vs symptoms |
| `sensory-conflict` | Sensory conflict / rearrangement / mismatch |
| `vection` | Vection, unexpected vection, vection–sickness relation |
| `postural` | Postural instability theory or measurement |
| `poison` | Evolutionary / toxin-expulsion (Treisman) |
| `hmd` | HMD-specific mechanisms (VAC, pose, display) |
| `oculomotor` | Eye movement / oculomotor theories or symptoms |
| `rest-frame` | Rest frame / presence-related conflict |
| `predictive` | Predictive coding, mismatch, information theory |
| `nausea-neural` | Nausea networks, vestibular–emetic, fMRI of sickness |
| `vection-neural` | Neural correlates of vection (not nausea per se) |
| `fnirs-methods` | fNIRS instrumentation, depth, haemodynamics |
| `fnirs-cs` | fNIRS applied to cybersickness / VR |
| `eeg-methods` | EEG in VR / portability (not corpus stats) |
| `fMRI-extra` | fMRI sickness literature outside review corpus |
| `scales` | FMS, SSQ, measurement |
| `corpus` | One of the 92 corpus studies |
| `legacy-tex` | Cited in current `theoretical.tex` (pre-revision) |
| `R1` / `R2` | Mentioned in reviewer feedback for theory/background |

---

## Paper index

| Citekey | ZK | pdf | Tags | Notes |
|---------|-----|-----|------|-------|
| `kennedyResearchVisuallyInduced2010` | `H6E2YNF3` | yes | terminology, VIMS | R1 |
| `keshavarzMotionSicknessCurrent2022` | `GUCR2BSY` | yes | terminology, sensory-conflict | R1; duplicate Zotero entry `PR73YFUI` |
| `lacknerMotionSicknessMore2014` | `EI6HCX35` | yes | terminology, symptoms | R1 |
| `chaMotionSicknessDiagnostic` | `S9JDJLL8` | yes | terminology | R1; Bárány criteria |
| `PDFMotionSickness` | `M4RIL8TW` | yes | terminology, symptoms | R1; Lawson, HVE 2nd ed. **ch. 23** (symptomatology, ~p. 531) |
| `cakirHandbookVirtualEnvironments2015` | `MCT6FSCU` | yes | terminology, sensory-conflict, vection, hmd | R1; Keshavarz, Hecht & Lawson, HVE **ch. 26** (~p. 647). Zotero title OK; bib key name legacy |
| `kennedySimulatorSicknessQuestionnaire1993` | — | yes | symptoms, scales | SSQ structure; R1 symptom thread |
| `stanneyCybersicknessNotSimulator1997` | — | yes | symptoms, terminology | SSQ profiles CS vs SS; in `challenges.tex`; R1 |
| `rebenitschReviewCybersicknessApplications2016` | — | yes | symptoms, terminology | MS vs CS profiles; in `challenges.tex` |
| `keshavarzEffectVisualMotion2019` | `J5QT4JQM` | yes | symptoms, vection, corpus | Vection/VIMS factors in VR |
| `weechPresenceCybersicknessVirtual2019` | — | yes | terminology | VIMS / presence; in `introduction.tex` |
| `reasonMotionSickness1975` | `NE2ND3GK` | no | sensory-conflict | R1/R2; book |
| `reasonMotionSicknessAdaptation1978` | — | yes | sensory-conflict | R1/R2 |
| `omanMotionSicknessSynthesis1990` | — | yes | sensory-conflict | R1/R2; duplicate bib entries |
| `davisSystematicReviewCybersickness2014` | — | yes | sensory-conflict, legacy-tex | Legacy primary conflict cite; R1 criticized |
| `zhangMotionSicknessCurrent2016` | — | yes | sensory-conflict, legacy-tex | Legacy; different paper than Keshavarz & Golding 2022 |
| `blesMotionSicknessOnly1998` | — | yes | sensory-conflict | Subjective vertical mismatch; legacy-tex |
| `protheroUnifiedApproachPresence2003` | — | yes | rest-frame, sensory-conflict, legacy-tex | `@incollection` |
| `hettingerVectionSimulatorSickness1990` | — | yes | vection, sensory-conflict, legacy-tex | R1 discussed; legacy-tex |
| `keshavarzVectionVisuallyInduced2015` | `7WYMLH47` | yes | vection | Vection–VIMS relationship review |
| `teixeiraUnexpectedVectionExacerbates2022` | `HDEM8CEY` | yes | vection | R1 |
| `teixeiraInvestigatingRelativeContributions2024` | `VYT3ZTQV` | yes | vection, postural | R1 |
| `riccioEcologicalTheoryMotion1991` | — | yes | postural, sensory-conflict | R2 |
| `stoffregenPosturalInstabilityPrecedes1998` | — | yes | postural | R2 |
| `cortesEEGbasedExperimentVR2023a` | — | yes | postural, eeg-methods, corpus, legacy-tex | VR walking + postural instability |
| `treismanMotionSicknessEvolutionary1977` | — | yes | poison, legacy-tex | R1 |
| `kramidaResolvingVergenceAccommodationConflict2016` | — | yes | hmd, legacy-tex | VAC |
| `ebenholtzMotionSicknessOculomotor1992` | — | yes | oculomotor, legacy-tex | |
| `nurnbergerMismatchVisualVestibularInformation2021` | — | yes | predictive, sensory-conflict, corpus, legacy-tex | Transfer entropy / mismatch |
| `palmisanoCybersicknessHeadMountedDisplays2020` | — | yes | hmd, vection | Head pose vs virtual pose |
| `yatesIntegrationVestibularEmetic2014` | — | yes | nausea-neural | R1; duplicate bib |
| `cohenNeuralBasisMotion2019` | — | yes | nausea-neural, fMRI-extra | R1; current Zotero export key |
| `schmalNeuronalMechanismsTreatment2013` | — | yes | nausea-neural | R1 |
| `bertiNeuropsychologicalApproachesVisuallyInduced2020` | `K4VBXMG8` | yes | vection-neural | R1; MT+, vection imaging |
| `napadowBrainCircuitryUnderlying2013` | — | yes | nausea-neural, fMRI-extra, legacy-tex | R1 |
| `toschiMotionSicknessIncreases2017` | `QPA6CCHI` | yes | nausea-neural, fMRI-extra, legacy-tex | MT+ connectivity |
| `scholkmannReviewContinuousWave2014` | `QUKSTNXN` | yes | fnirs-methods | R2; duplicate bib |
| `PresentFutureUse` | `KN6Q3Y3S` | yes | fnirs-methods | Pinti et al. 2020; bib `@misc` / webpage parent `UHVX65P4` |
| `krokosQuantifyingVRCybersickness2022` | — | yes | eeg-methods, corpus, legacy-tex | |
| `yamamuraHemodynamicVRAdaptingUsers2021` | — | yes | fnirs-cs, corpus | Active corpus fNIRS row; legacy prose may still use `...2021a`, but current BibTeX key lacks the `a` suffix |
| `yamamuraPleasantLocomotionReducing2020` | — | yes | fnirs-cs, corpus | Active corpus fNIRS row |
| `yeoInvestigatingCorticalActivity2024` | `5QF2J5SB` | yes | fnirs-cs, corpus | |
| `tanimuraEffectsLowResolution3D2019` | — | yes | fnirs-cs, corpus | Active corpus fNIRS row; low-resolution 3D video / cerebral blood-flow dynamics |
| `zhangAnalysisMotionSickness2020` | — | yes | fnirs-cs, legacy-tex | Relevant fNIRS/VIMS reference, but source-checking found it is not an active corpus row |
| `gavganiCybersicknessrelatedChangesBrain2018` | — | yes | fnirs-cs | fNIRS + TCD; relevant background, but not an active corpus row |
| `keshavarzValidatingEfficientMethod2011` | — | yes | scales | FMS original |
| `goldingChapter27Motion2016` | — | yes | terminology | Elsevier handbook MS |
| `goldingMotionSicknessSusceptibility1998` | — | yes | scales | MSSQ |
| `hettingerVisuallyInducedMotion1992` | `7PFREYE6` | yes | vection | Hettinger & Riccio — not `riccioEcologicalTheoryMotion1991` |
| `miyazakiRestingstateFunctionalConnectivity2021` | — | yes | nausea-neural, fMRI-extra | Recovery connectivity; used in Results |
| `limTestretestReliabilityVirtual2021` | — | yes | hmd | Display type; `challenges.tex` |
| `stanneyIdentifyingCausesSolutions2020` | `SA2QCV4L` | yes | terminology | Broad cybersickness agenda |

ZK `—` = resolve via `zotero_search_by_citation_key` (not looked up this pass).

---

## Current `theoretical.tex` citekeys (legacy)

From last committed version; all tagged `legacy-tex` above.

`davisSystematicReviewCybersickness2014`, `zhangMotionSicknessCurrent2016`, `hettingerVectionSimulatorSickness1990`, `blesMotionSicknessOnly1998`, `protheroUnifiedApproachPresence2003`, `treismanMotionSicknessEvolutionary1977`, `cortesEEGbasedExperimentVR2023a`, `kramidaResolvingVergenceAccommodationConflict2016`, `ebenholtzMotionSicknessOculomotor1992`, `nurnbergerMismatchVisualVestibularInformation2021`, `krokosQuantifyingVRCybersickness2022`, `yamamuraHemodynamicVRAdaptingUsers2021a`, `zhangAnalysisMotionSickness2020`, `napadowBrainCircuitryUnderlying2013`, `toschiMotionSicknessIncreases2017`

Note: the legacy list above records the citekeys in the pre-revision `theoretical.tex`; it is not a statement that all listed papers remain active corpus papers.

---

## Review corpus (modalities)

From `Plots_Analysis_GPT54.csv`; not a reading list — counts for context.

| Modality | n (92) |
|----------|--------|
| EEG | 77 |
| fNIRS | 4 |
| fMRI | 0 |
| Neurostim | 11 |

Theory mention (aggregate, Phase 0): ~73/92 papers note theory; ~75/87 engaged cite sensory conflict — see `PDF_HighLevel_Analysis_GPT54.csv` for per-paper fields.

---

## Reviewer feedback index (theory-related)

Pointer only — full wording in `reviewer_feedback.txt`.

| Ref | Topics |
|-----|--------|
| R1 Major #2 | terminology — Kennedy, Keshavarz & Golding, Lackner, Cha; VIMS hierarchy |
| R1 | sensory-conflict — Reason, Oman; weak Davis/Zhang refs |
| R1 | vection — not “vection theory”; Hettinger; Teixeira; unexpected vection |
| R1 | poison — Treisman as evolutionary, not competing mechanistic theory |
| R1 | nausea — Yates, Cohen, Schmäl; Berti & Keshavarz; limited fMRI basis |
| R1 | symptoms — vection not SSQ item; oculomotor/nausea in CS |
| R1 | FMS — original scale source |
| R2 Minor §IIB | fnirs-methods — temporal resolution vs fMRI |
| R2 Minor IVB2 | fnirs-methods — depth, insula/amygdala |
| R2 | sensory-conflict, postural — Reason, Riccio, Stoffregen |
| R3 Critical #5 | theory lenses vs Results synthesis (cross-phase) |

---

## `references.bib` quirks (factual)

- Duplicate keys: `omanMotionSicknessSynthesis1990`, `yatesIntegrationVestibularEmetic2014`, `scholkmannReviewContinuousWave2014`, `cohenNeuralBasisMotion2019` / `…2019a`
- `PresentFutureUse` — Pinti 2020; attached PDF under storage key `KN6Q3Y3S`
- HVE ch. 26 — Zotero item `MCT6FSCU`; bib may still export as `cakirHandbookVirtualEnvironments2015`

---

*Source map for Phase 2. Updated after Zotero import of theory + fNIRS refs.*
