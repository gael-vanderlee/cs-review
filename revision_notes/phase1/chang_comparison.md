# Side job — Chang et al. (2023) comparison

**Status**: COMPLETE (2026-05-21). Source PDF: [revision_notes/assets/Brain activity during cybersickness a scoping.pdf](../assets/Brain%20activity%20during%20cybersickness%20a%20scoping.pdf). All claims below sourced from page numbers given.

## Comparison matrix

| Dimension | Chang et al. 2023 | This review |
|---|---|---|
| Review type | Scoping review (PRISMA-ScR) [p.2 §3.1] | Systematic review (PRISMA 2020) |
| Databases searched | Web of Science + Google Scholar (2) [p.4 §3.1] | PubMed + Web of Science + Scopus (3) |
| Search date | 20 September 2021 [p.4 §3.1] | 27 March 2025 |
| Search terms | `{EEG OR electroencephalogram} AND {cybersickness} AND {VR sickness} NOT {therapy}` [p.4 §3.1] | Broader: includes ERP, MEG, fMRI, fNIRS, PET, neurostimulation/tACS/tDCS/TMS/GVS terms alongside EEG; broader sickness terms (incl. VIMS, simulator sickness, motion sickness); broader VR terms (HMD, immersive environment) |
| Inclusion-keyword scope | EEG only | EEG, fNIRS, fMRI, MEG, PET, neurostimulation modalities |
| Date window | Publications up to 2021-09-20 [p.4 §3.2] | Publications up to 2025-03-27 |
| Corpus size | 33 articles (38 analyses) [p.4 §4] | 92 studies |
| Modalities covered | EEG only [scope by design] | EEG (77), fNIRS (4), neurostimulation (11: GVS 5, tDCS 3, tACS 2, Other 1). fMRI/MEG/PET searched, 0 eligible |
| Includes neurostimulation? | No [out of scope; explicitly excludes therapy] | Yes |
| Meta-analytic statistics? | No — qualitative synthesis + Sankey diagram counts [p.4–5] | Yes — VR-device × alpha band power ($p=0.0036$, large effect), × beta ($p=0.0146$); Egger's test for publication bias ($p=0.011$) |
| Methodological audit | EEG pipeline characterization (preprocessing, feature extraction, selection, classification) [p.4 §3.3] | Pipeline characterization + reporting audit (accuracy-only ML reporting, baseline choice, sick/non-sick threshold practice, publication bias) |
| Reporting recommendations | Future-work directions on EEG approaches [Conclusion] | Concrete reporting recommendations grounded in corpus findings |
| Theoretical framing | Not engaged; RQs are narrowly about EEG markers, classification accuracy, and experimental setups [p.3 §1 RQ1–RQ3] | Dedicated theoretical-background section; corpus audit of which theories studies invoke (sensory conflict 75/87 of theory-engaged studies; postural instability; unexpected vection; etc.) |
| Terminology treatment | Conflates "cybersickness" / "VR sickness" with motion-bed-induced discomfort, no distinction surfaced [p.4 §3.1 note] | Explicit treatment of the cybersickness / VIMS / simulator sickness / motion sickness construct space with hybrid policy (umbrella in Background, paper's own term in Results) |
| Field-level critical appraisal | Catalogue of pipeline choices, no critique [p.4 §3.3] | Critical appraisal of recurring shortcomings (accuracy-only ML reporting, weak baselines, ad hoc sick/non-sick thresholds, publication bias) |
| Year | 2023 | 2026 (target) |

## Key deltas (load-bearing for the novelty paragraph)

1. **Scope**: Chang is EEG-only by design. This review covers neurostimulation alongside neuroimaging — the entire "neuromarker" frame is broader.
2. **Corpus size**: 92 vs 33 (≈ 2.8×), with 3.5 additional years of literature (2021-09 → 2025-03).
3. **Meta-analytic depth**: Chang's synthesis is qualitative (Sankey diagrams, counts). This review adds corpus-level inferential statistics on hardware confounds and publication bias.
4. **Databases**: Chang uses Google Scholar (non-curated index, no controlled-vocabulary search) and only WoS. This review uses three curated databases (PubMed, WoS, Scopus), more reproducible search.
5. **Field-level perspective**: Chang's RQs are narrowly about EEG findings, classification accuracy, and experimental setups. This review additionally engages with the theoretical frameworks invoked across the corpus, the cybersickness/VIMS/SS/MS terminology debate, and a critical appraisal of recurring methodological shortcomings — i.e. the conceptual and methodological scaffolding in which findings are produced, not only the findings themselves.

## Pinned for cross-references

- `abs:chang-corpus-delta` → "92 vs 33"
- `intro:chang-search-date` → "September 2021"
- `intro:chang-modality-scope` → "EEG only"
- `intro:chang-corpus-size` → "33 articles (38 analyses)"
- `intro:chang-review-type` → "scoping review"
