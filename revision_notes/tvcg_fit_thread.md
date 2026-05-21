# Side job — TVCG fit thread

**Status**: COMPLETE (2026-05-21). Threads selected for use in Intro closer + Discussion practitioner-implications paragraph.

## Selected threads

### Thread 1 — Hardware choice modulates measured neural response
- **Corpus stat**: VR display type (HMD vs screen) significantly modulates alpha-band response during cybersickness ($p=0.0036$, large effect) and beta-band response ($p=0.0146$). Sources: [unified_statistical_report.txt](../../review_scripts/data/V4/Stim/unified_analysis/unified_statistical_report.txt), [anova_summary_report.txt](../../review_scripts/data/V4/Stim/plots/anova_summary_report.txt).
- **VR-practitioner takeaway**: comparing or aggregating neural-marker results across hardware is not straightforward; the choice of HMD vs flat screen alters the measured EEG signature itself, not only sickness intensity.

### Thread 2 — Stimulus paradigm influences which brain rhythms vary
- **Corpus observation** (already in [results.tex:335](../contents/results.tex#L335)): driving scenarios produce increased alpha 46.7% of the time vs 15.8% for navigation tasks.
- **VR-practitioner takeaway**: scenario design influences which neuromarkers are recoverable, which matters for any adaptive/closed-loop VR system that depends on a specific frequency band.

### Thread 3 — Mitigation work is starting to bridge into VR-deployable interventions
- **Corpus content**: 11 neurostimulation studies (5 GVS, 3 tDCS, 2 tACS, 1 Other). Several couple stimulation with EEG.
- **VR-practitioner takeaway**: closed-loop mitigation via brain stimulation is no longer purely future-work; the literature is at the threshold of in-VR application.

### Thread 4 — Reporting practice gaps that VR system researchers can act on
- **Corpus stats**: prevalence of accuracy-only ML reporting (see Phase 5 `accuracy_audit.md`); eyes-closed baseline is widespread despite its known confound with alpha suppression; sick/non-sick thresholds set ad hoc.
- **VR-practitioner takeaway**: a small checklist for new VR-EEG studies (reference baseline, threshold rationale, sens/spec alongside accuracy) substantially improves cross-study comparability.

### Thread 5 — Publication bias evidence motivates pre-registration in VR-EEG work
- **Corpus stat**: Egger's test detects funnel-plot asymmetry ($p=0.011$).
- **VR-practitioner takeaway**: the field would benefit from pre-registered, hardware-controlled designs in future VR cybersickness studies.

## Where each thread lands

- **Intro closer** (TVCG-fit defense, Phase 1): threads 1, 3 lead — they make the strongest case that the paper informs VR system design. Threads 2, 4, 5 referenced in passing.
- **Discussion practitioner-implications paragraph** (Phase 6): all five threads, each as a separate sentence.

## What NOT to do

- Do not over-claim that this review provides design guidelines (it does not; it provides corpus-grounded observations that *inform* design decisions).
- Do not present the meta-analytic findings as definitive proof of hardware causation — they are corpus-level associations.
