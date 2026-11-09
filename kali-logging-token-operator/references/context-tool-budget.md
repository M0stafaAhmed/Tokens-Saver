# Context and Tool Budget for Claude Desktop

This reference exists to reduce repeated work without compromising evidence and validation.

## Work from a bounded document map

1. If the current workspace is accessible, list filenames and sizes once.
2. Read the active task's exact target headings from the ledger or report.
3. Consult only nearby supporting sections and documents needed for a conflict.
4. Reuse a fresh outline or hash instead of rereading an unchanged 40 KB file.
5. After modification, review a focused diff or altered section and one proportionate verification pass.

Never use a content search against `reference/` or `backups/` by default. Expand into original material only when provenance is ambiguous or disputed.

## Bounded command examples

Adapt to available shell tools. Do not blindly run a command against unknown paths.

```bash
find . -maxdepth 2 -type f -name '*.md' -printf '%p %s bytes\n' | sort | head -60
grep -nE '^#{1,4} ' decisions.md | head -90
rg -n 'EXP-1[3-8]|K-0[1-9]|K-1[0-4]' phase3-terminal-mediation-research.md | head -70
sed -n '135,190p' decisions.md
sha256sum decisions.md architecture-proposal.md
```

Prefer a targeted `rg`/`grep` + bounded `sed` over printing a full report. If `rg` is unavailable, use `grep`; do not install dependencies just for convenience.

## Avoid recursive analysis loops

- Each call must answer a specific unresolved question.
- Do not repeatedly search the same terms or print the same directory list without a changed hypothesis.
- Do not launch new research branches to achieve a perfect understanding of unrelated topics.
- Run tests that actually check the requested claim; stop when they answer it or show a concrete gap.
- Focus verification on changed files and consequential interactions.
- Save detailed reproducible findings in the existing report; keep chat summaries short.
- If the user requested a review gate, stop and wait for their next authorization.

## When to split phases

Split when the work crosses a **different source of truth or permission boundary**: research → policy reconciliation → architecture → implementation → real Kali validation. Do not split a single straightforward file edit into gratuitous micro-prompts.

Do not consume repeated tool calls checking a past cloud workspace after access is clearly unavailable. Explain that blocker and request only the indispensable file(s).

## Durable handoff

Reuse the current `Project-Handoff.md` or authorized project-state file; do not create a competing history log. At an approved phase boundary, record:
- Exact deliverable and verification.
- Current phase, stop point, and next authorized task.
- Paths and checksums only when verified.
- Remaining specific policy conflicts and unrun tests.
- Source references and environment/version limitations.

Do not paste giant command outputs, raw secret-bearing evidence, or previous chat transcripts. A new Claude chat must verify accessible files rather than assuming persistence.

## Reality check

Skills cannot increase the Free allowance, change the time window, or force a model/effort setting. Better scoping can reduce avoidable work; there is no defensible fixed percentage of token savings without measurement.
