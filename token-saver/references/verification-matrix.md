# Verification Matrix and Quality Gates

Load this reference when work changes files, code, data, configurations, research conclusions, or any consequential decision.

## 1. Match verification to risk

| Task | Minimum useful check | Escalate when |
|---|---|---|
| Direct factual answer | Validate the premise if uncertain or time-sensitive | High consequence or disputed facts |
| Rewrite / translation | Check meaning, omissions, tone, required structure | Legal, technical, or contractual semantics |
| Summary | Compare against source coverage and preserve key exceptions | Source is long, conflicting, or evidence-sensitive |
| Code edit | Review changed lines and run the most relevant test | Broad effects, security-sensitive code, or regressions |
| Multi-file edit | Inspect file list and diff; validate cross-file links/references | Schema or interface changes |
| Data transformation | Compare row counts, columns/schema, nulls, and representative records | Irreversible data changes or financial/operational use |
| Research / recommendation | Verify decisive claims and cite sources | Current regulation, security, health, finance, or safety |
| Repository operation | Verify target branch, exact paths, object hashes, and final state | Destructive or forceful changes |
| Generated document | Inspect layout, tables, links, and required content | Delivery depends on rendering or print fidelity |

## 2. Use the strongest discriminating check first

Do not run every conceivable validation. Select the check most likely to detect a consequential error.

Examples:
- A parsing failure should be tested with a parser, not only a visual glance.
- A repository transfer should compare blob hashes or exact content, not merely confirm that a folder is visible.
- A data conversion should compare schema and record counts, then inspect representative values.
- A code fix should exercise the failing path, not just compile unrelated files.

## 3. Preserve evidence and uncertainty

- Keep original commands, outputs, identifiers, timestamps, and error messages exact when they support a technical claim.
- Distinguish observed facts, source-backed facts, inferences, hypotheses, failed attempts, and proposals.
- Do not turn an untested recommendation into a verified result.
- Preserve negative results when they affect the conclusion.
- If sources conflict, identify the conflict and state what remains unresolved.
- Do not omit limitations simply because they make the result less tidy.

## 4. Avoid false verification

A check is not evidence unless it was actually performed. A passing check supports only the behavior it covers. A successful file-write response does not prove downstream behavior. A build does not prove correctness of every runtime path.

Use precise status terms:
- **Verified:** checked directly by an appropriate test or inspection.
- **Partially verified:** some requirements checked; others remain.
- **Not verified:** no direct check performed.
- **Blocked:** required input or capability unavailable.

## 5. Final quality gate

Before delivering, check:
- Is the requested output present?
- Does it meet the stated acceptance criteria?
- Were unrelated files or requirements changed?
- Are exact values and evidence intact?
- Are citations and source provenance preserved where required?
- Are assumptions and limitations visible?
- Is the next step actionable?

Do not repeat the entire workflow in the final response. Report the result and the checks that matter.
