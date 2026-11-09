# Phase Gates — Do Only the Authorized Task

Use this reference for work that changes a project document, involves several documents, or has a review/approval boundary.

## Freeze a narrow task contract

Determine the active phase and six fields:
1. **Deliverable:** exact file or result.
2. **Inputs:** authoritative files and sections.
3. **Allowed writes:** filenames or directory scope.
4. **Forbidden changes:** source files, operating-system state, other phases.
5. **Acceptance criteria:** structural, factual, and operational checks.
6. **Stop:** point after which no further work is authorized.

Do not turn this internal structure into a long questionnaire. Read the ledger first; ask a single essential question only when the task cannot proceed safely.

## Recommended separation

- **Decision reconciliation:** one existing `decisions.md`; preserve original provenance and distinguish approval from observation. Do not redesign architecture.
- **Research correction:** one research report and its cited sources/experiments. Do not edit the ledger unless explicitly asked.
- **Architecture revision:** use the reviewed decision ledger and qualified research evidence; no deployment or configuration changes.
- **Implementation planning:** map verified requirements to components, risk boundaries, and tests; no code or sudo changes without authority.
- **Kali validation:** execute only specifically authorized tests on a confirmed Kali environment with a rollback/safety plan. No hidden or global config changes.

Do not combine these phases merely because the next seems obvious.

## Modification practice

1. Confirm the real file and active workspace; inspect the specific target headings first.
2. Preserve a recoverable original before substantial or destructive edits.
3. Make smallest sufficient change in existing file.
4. Verify changed sections and any references needed to check consistency.
5. If a contradiction requires a new user policy decision, record it and stop the affected portion; continue independent safe work if possible.
6. Report status and stop.

No automatic rewrite of historical records, no spurious `updated` fields, no unrelated cleanup, no repeated full-tree scans.

## Short response shape

```text
Status: ...
Changed: ...
Verified: ...
Unresolved: ...
Not attempted: ...
Next authorized task (if any): ...
```

Avoid dumping the entire report, shell transcript, or unchanged source content into chat. User chooses model/effort separately; prompts should not mention a thinking setting.
