# Check flow

Check the flow of the changes with a focus on clarity and ease of reading while staying factually accurate and using precise vocabulary. Read the diff first to understand what changed and why, then read the surrounding sections and the manuscript outline (review_bci_cs.tex) so the revision sits coherently in the larger argument. Match the voice of the neighbouring paragraphs and of AGENTS.md (formal, literal, objective, no value judgements, no figurative language, clarity). Preserve every claim, citation, and the section's argumentative scope.

Apply these principles:

1. Open each (sub)section with one orienting sentence that states the aim before any definition or detail.
2. Move from larger to smaller: broader construct → narrower instance, dominant framework → refinements, general claim → consequence.
3. Connect adjacent sentences with explicit logical links (cause, contrast, consequence). If a paragraph reads as a list of standalone facts, it needs connectives.
4. Vary vocabulary: if one noun (e.g. "account", "framework") repeats more than 3–4 times in a paragraph, substitute synonyms or restructure.
5. Restore parallel structure when comparing siblings (e.g. modalities on the same axes: temporal/spatial resolution, portability, cost).
6. Integrate justifications into the prose rather than appending them as checklist tags ("This is relevant because…").
7. Place each fact in the section where it belongs. If a sentence addresses a different concern than its paragraph's topic, move it.
8. Cross-reference (\autoref) rather than redefine a term already introduced earlier in the manuscript.
9. Keep meta-statements about review conventions out of conceptual prose — push them to Methods or a parenthetical.

Scope rules:

- A flow pass should leave word count roughly stable or shorter. If you find yourself adding length, you are drifting into rewriting.
- Sentence-level smoothing and reordering within a paragraph: proceed.
- Structural changes (reordering paragraphs, splitting or merging subsections, moving content across files): propose first, do not apply.

Before finishing:

- Re-read the original diff and list anything removed in the pre-existing revision that may have been load-bearing (named theories, modalities, specific empirical claims, citations). Flag these; do not silently restore.
- Confirm the prose is publication-ready. Flag and remove any residue of the editing process or internal workflow:
  - revision-tracking language ("in the previous version", "we have now added", "as suggested by the reviewer", "in response to R2");
  - references to internal artefacts (file names, paths, scripts, CSV columns, pipeline labels such as `V4/Stim`, model names like `GPT-5.4`, the `review_scripts` repo, the diff itself);
  - meta-commentary on the manuscript's own state ("this section has been rewritten", "see the new paragraph below");
  - first-person process language inappropriate for the venue ("we will add", "we plan to").

  Test for each sentence: *would it survive type-setting in TVCG as-is, read by someone who has never seen the prior version or the reviewer report?* If not, rewrite or remove.
- Build with `latexmk review_bci_cs.tex` and confirm no new undefined references or citations.
- Report changes by principle, not line by line.
