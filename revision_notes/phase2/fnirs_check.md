# Phase 2 — fNIRS factual check

Reviewer 2 noted two issues in the fNIRS background: the draft implied that fNIRS has superior temporal resolution to fMRI, and it did not state that fNIRS cannot readily measure deep structures such as the insula or amygdala.

## Checked sources

- `scholkmannReviewContinuousWave2014`: Continuous-wave fNIRS measures haemodynamic changes through near-infrared light. Because it measures haemodynamic responses, its effective temporal interpretation differs from EEG and is closer in kind to other haemodynamic methods than to electrophysiology.
- `PresentFutureUse`: Pinti et al. describe fNIRS as portable and wearable compared with scanner-based imaging, but still limited by optical penetration and extracerebral contamination. The method is primarily suited to superficial cortical regions.
- Structured corpus (`Plots_Analysis_GPT54.csv`): four eligible studies used fNIRS (`Neuroimaging_device = fNIRS`): Yeo 2024, Yamamura 2021, Yamamura 2020, and Tanimura 2019. The extracted regions are cortical or surface-accessible regions; the corpus does not contain fNIRS measurements of insula or amygdala.
- Source-check correction: `zhangAnalysisMotionSickness2020` and `gavganiCybersicknessrelatedChangesBrain2018` are relevant fNIRS/NIRS cybersickness references in Zotero or older materials, but they are not active corpus fNIRS rows.

## Corrected wording constraints

- Do not say fNIRS has superior temporal resolution to fMRI in a way that implies EEG-like temporal precision.
- It is acceptable to say fNIRS is more portable and easier to combine with movement or HMD-based VR than fMRI.
- State that fNIRS is constrained to cortical tissue reachable by near-infrared light and cannot readily assess deep structures, including the insula and amygdala.
- Contrast EEG, fNIRS, and fMRI by measurement principle: EEG records electrical activity with high temporal resolution; fNIRS and fMRI measure haemodynamic correlates; fMRI can access deeper structures but imposes immobility constraints that limit ecological VR paradigms.
