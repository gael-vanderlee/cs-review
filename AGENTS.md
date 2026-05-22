This is a review paper on Brain Computer Interfaces (BCIs) studies using Virtual Reality (VR).
The manuscript is under revision for TVCG; reviewer feedback is in [reviewer_feedback.txt](reviewer_feedback.txt) and condensed actions are in [TODO.md](TODO.md).

## Manuscript vs internal workflow

**Internal names stay internal.** Pipeline folder names under `review_scripts/data/` (e.g. `V4/Stim/` in paths below) are not manuscript vocabulary. Do **not** use search-iteration labels (`V4`, `Stim`, `NoStim`, or shorthand like `V4/Stim`) in manuscript prose (`contents/*.tex`, abstract, captions). In the paper, write *the studies included in this review*, *the literature retrieved by the search*, or *prior work*.

**Background vs review findings.** Sections that introduce the field must not report results of *this* systematic review (counts, modality breakdowns, theory-engagement tallies, meta-analytic statistics, PRISMA numbers). Those belong in Methods and Results.

When drafting Background/Theory, ask: *Could this sentence appear in a textbook chapter before the reader knows our search existed?* If it requires our CSV or screening, move it to Methods or Results.

User in the loop: When you are working on high level planning or important decisions and encounter a non obvious choice where there are compromises, or the path hasn't been explicitely defined: **ask the user**. Do not make assumptions or decide for him, let the user steer the direction of this project. Likewise, if you need more information to produce a quality output: external papers, figures, information, ask the user.

## Writing Style Instructions for Latex

*   **Tone:** Formal, objective, and strictly factual.
*   **Language:** Use precise, specific, and unambiguous terminology. All language must be **literal**, avoiding metaphors or figurative expressions.
*   **Clarity:** Prioritize a clear and logical flow. The language must be precise without being convoluted, ensuring the core point is always understandable.
*   **Objectivity Rules:** Strictly avoid all superlatives, exaggeration, emotional language, and **value judgments**. Do not characterize a subject with subjective descriptors (e.g., do not call a method "simple," "elegant," or "complex"). Present the facts and allow the reader to draw their own conclusions.
*   **Flow:** Open each (sub)section with one orienting sentence stating its aim before any definition or detail. Move from larger to smaller (broader construct → narrower instance, dominant framework → refinements, general claim → consequence). Connect adjacent sentences with explicit logical links (cause, contrast, consequence) rather than juxtaposing standalone facts.
*   **Vocabulary and structure:** Vary nouns when one would otherwise repeat more than 3–4 times in a paragraph. Use parallel structure when comparing siblings (e.g. modalities on the same axes). Cross-reference (`\autoref`) terms already introduced earlier rather than redefining them. Place each fact in the section where its topic belongs.

**IMPORTANT**: Do not make assumptions or guess claims, numbers or citations. Each claim must be made not from something that is likely true, but from something that has been verified to be true. Run scripts, read sources, ask the user, be careful not to hallucinate.

The analysis pipeline lives in a sibling repo: `/mnt/Space/Projects/PhD/Latex/review_scripts` (see its own `AGENTS.md` for structure). It hosts search exports, the merge/screen/extract pipeline, and the figure/stats scripts. That repo was also used for a separate Vection review — **the Vection track is out of scope for this manuscript**; only the cybersickness track matters here.

## Corpus data

92 manually selected studies. The active search query includes neurostimulation (tDCS/tACS/TMS/GVS) and neuroimaging terms (TODO Critical #3; R2/R3).

Canonical paths:

- [PDF_HighLevel_Analysis_GPT54.csv](../review_scripts/data/V4/Stim/PDF_HighLevel_Analysis_GPT54.csv) — 92 rows. GPT-5.4 high-level read of each PDF: summary, main contribution, cybersickness measurement, BCI method, theory engagement, objective category, study details, shortcomings. Use this CSV for narrative tasks (identifying papers, extracting trends, qualitative synthesis). **Both CSVs already reflect the final manually-selected corpus — ignore the `Included` column; do not re-filter on it.**
- [Plots_Analysis_GPT54.csv](../review_scripts/data/V4/Stim/Plots_Analysis_GPT54.csv) — 92 rows. GPT-5.4 structured extraction of numerical/categorical fields (EEG channels, sampling rate, preprocessing, bands, classification metrics, VR device, CS questionnaires, demographics, theory mention, band-power changes per region, etc.). Consumed by `review_scripts/analysis/` scripts to produce stats and figures.
- [V4_manual_selection.csv](../review_scripts/data/V4/Stim/V4_manual_selection.csv), [selected.csv](../review_scripts/data/V4/Stim/selected.csv) — manual screening artefacts feeding into the 92-paper corpus.
- [notes.md](../review_scripts/data/V4/notes.md) — exact PubMed/WoS/Scopus search queries.

## Manuscript layout

- [review_bci_cs.tex](review_bci_cs.tex) — main file
- [contents/](contents/) — section files
- [figures/](figures/) — figures (many generated by `review_scripts/analysis/`)
- [references.bib](references.bib)
- [template_tvcg/](template_tvcg/) — active TVCG template; [template_ieee/](template_ieee/) is unused
- Build: run `latexmk review_bci_cs.tex` from the repo root. Output lands in [out/review_bci_cs.pdf](out/review_bci_cs.pdf) (the `latexmkrc` sets `$out_dir = 'out'`). Do **not** use `make` — the included `makefile` is a generic template pointing at `template.tex` and will not build this manuscript.

## Tooling

- **Python**: the sibling `review_scripts` repo uses `uv`. The system `python3` has no scientific packages installed and `pip install` is blocked. To run a one-off snippet that needs pandas / pypdf / etc., use `uv run --with <pkg1>[,<pkg2>] python -c "..."` from any directory. Example: `uv run --with pandas python -c "import pandas as pd; print(pd.read_csv('data/V4/Stim/Plots_Analysis_GPT54.csv').shape)"`. The `.venv` at the repo root works too (`.venv/bin/python`) but only has what's already locked in `uv.lock`.
- **PDF text extraction**: `pdftotext` / `mutool` / `poppler` are not available on this machine. Use `uv run --with pypdf python -c "import pypdf; ..."` to extract text from PDFs (e.g. reading references from Zotero exports placed under `revision_notes/assets/`).
- **Zotero MCP**: You can use the zotero mcp tool to access my zotero library, search for papers, get citations, read full texts, run semantic searches and more.

## Workflow notes

- Reviewers asked for a corpus-grounded synthesis (TODO Critical #5, #7, #8). When making claims in the manuscript, prefer counts/statements derivable from the two CSVs over narrative assertions.
- TODO Critical #1 removes the `BCI` framing — when editing prose, prefer "neuroimaging" / "brain-directed methods" / explicit modality names over "BCI" unless the cited paper itself uses BCI.
- TODO Critical #6: do not enforce a single hierarchy across cybersickness / VIMS / simulator sickness / motion sickness — match the term used by each cited paper.
