# Check claims

Audit the passage for epistemic overreach — instances where the certainty or causal scope of a claim exceeds what the evidence supports. Read the passage, then flag each problematic sentence with: the original text, the type of overreach, and a concrete alternative anchored in the available evidence.

## What to flag

**1. Unhedged field-level causal claims**
Sentences asserting that a practice or phenomenon *limits*, *prevents*, *drives*, or *determines* a field-level outcome, without a citation or corpus count to support the causal link.
- Bad: "X limits cumulative progress."
- Fix: "X recurs across N corpus studies and constrains cross-study comparability" — or cite the evidence for the causal claim.

**2. Ungrounded universal statements**
Claims using "always," "never," "all," "none," or their implicit equivalents ("the field does X," "studies consistently Y") without a corpus count or a citation backing the scope.

**3. Unsupported causal chains**
A → B claims where the mechanism is asserted rather than cited or directly inferred from corpus data.

**4. Overclaiming from limited evidence**
Conclusions stated as field-level patterns when the underlying count is small (e.g., inferring a general trend from 2–3 studies without flagging the count).

**5. Certainty mismatches**
Evidence is correlational but the claim is stated as causal; the corpus is too small or heterogeneous for the strength of the conclusion; hedges present in the underlying sources have been dropped.

## What NOT to flag

- Claims directly derived from corpus counts stated inline (e.g., "16 of 30 studies report X").
- Claims supported by a citation in the same sentence.
- Claims already using hedging qualifiers ("appears to," "may," "suggest," "have been identified as," "is consistent with").
- Standard methodological descriptions that are definitionally true (e.g., "k-fold without subject stratification permits subject-identity leakage").
- Statements about corpus-internal observations where the corpus itself is the evidence (e.g., "43 of 77 EEG studies do not report the reference electrode").

## Scope

This is a claims audit, not a flow or style pass. Do not rephrase for readability; do not alter citations; do not flag value judgments (those are covered by the style rules in AGENTS.md). Only flag and propose minimal fixes for epistemic overreach.

Report each issue as:
- **Sentence**: [exact original text]
- **Type**: [which category above]
- **Proposed fix**: [minimal rephrasing anchored in available evidence]
