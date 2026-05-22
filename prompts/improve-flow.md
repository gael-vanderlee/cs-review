# Check flow

Check the flow of the changes with a focus on clarity and ease of reading while staying factually accurate and using precise vocabulary. Read the diff first to understand what changed and why, then read the surrounding sections and the manuscript outline (CLAUDE.md) so the revision sits coherently in the larger argument. Match the voice of the neighbouring paragraphs and of AGENTS.md (formal, literal, objective, no value judgements, no figurative language, clarity). Preserve every claim, citation, and the section's argumentative scope.

## What you are aiming for

The reader should be able to follow the argument without re-reading sentences or backtracking. A section is working when each paragraph has a clear role in the larger argument, adjacent sentences are connected by something more than topical adjacency, and the reader is told what a passage is about before being told the details.

Concretely, that usually means:

- A section or paragraph that introduces a new line of argument benefits from an orienting sentence; one that continues an established thread usually does not. Use judgement.
- Information is easier to absorb when it moves from broader to narrower (construct → instance, framework → refinements, claim → consequence), but the inverse can work when the broader point is the punchline. Pick the order that makes the argument visible.
- Adjacent sentences should be doing connected work. If a paragraph reads as a list of standalone facts, the connections are either missing or the facts belong in different paragraphs.
- Repeated nouns and parallel structures are signals about the prose, not rules. If the same noun anchors a paragraph three or four times in a row, ask whether that is deliberate emphasis or accidental monotony. If sibling concepts are being compared, parallel structure usually helps the comparison land.
- Justifications and relevance claims read better when they are part of a sentence's argument than when they are appended as a tag.
- A term defined once does not need to be redefined; an `\autoref` is usually enough.
- Meta-commentary about the review's own conventions tends to sit awkwardly in conceptual prose; consider whether it belongs in Methods or in a parenthetical.

These are tendencies, not rules. Override any of them when the local prose has a better reason to do something else, and say so when reporting the changes.

## Scope

A flow pass should leave word count roughly stable or shorter; if length is growing, the work has drifted into rewriting and is out of scope. Sentence-level smoothing and reordering within a paragraph: proceed. Structural changes — reordering paragraphs, splitting or merging subsections, moving content across files — should be proposed first, not applied.

## Before finishing

Re-read the original diff and list anything removed in the pre-existing revision that may have been load-bearing (named theories, modalities, specific empirical claims, citations). Flag these for the user; do not silently restore.

Check that the prose is publication-ready and contains no residue of the editing process or the internal workflow. The kinds of things that should not appear in the final manuscript include revision-tracking language ("in the previous version", "as suggested by the reviewer", "in response to R2"), references to internal artefacts (file names, paths, scripts, CSV columns, pipeline labels such as `V4/Stim`, model names like `GPT-5.4`, the `review_scripts` repo, the diff itself), meta-commentary on the manuscript's own state ("this section has been rewritten", "see the new paragraph below"), and first-person process language inappropriate for the venue ("we will add", "we plan to"). The general test: would each sentence survive type-setting in TVCG, read by someone who has never seen the prior version or the reviewer report?

Build with `latexmk review_bci_cs.tex` and confirm no new undefined references or citations. Report changes by principle and intent, not line by line.
