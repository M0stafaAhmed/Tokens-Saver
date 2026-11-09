# Evidence Integrity and Linux Verification

Load this reference only when handling terminal/shell feasibility research, experiments, sudo/PTY details, security-sensitive capture, or ledger reconciliation.

## Classification

Every technical claim needs appropriate provenance:

| Status | Permitted claim |
| --- | --- |
| Approved requirement | User decision supported by `decisions.md` |
| Observed in sandbox | Behavior in named sandbox with exact versions and limitations |
| Observed on Kali | Reproducible test on identified Kali host/version, with captured result |
| Documentation claim | Statement supported by specified manual/document version |
| Proposed | Hypothesis, architecture, remedy, or recommended experiment |
| Unverified | Not tested, no applicable evidence, or environment mismatch |
| Conflict | Requirement/evidence mismatch or competing approved policies needing resolution |

Never describe experiment results as an OS-wide guarantee. A simulator with `loginuid` manually set does not prove a real PAM login. A prototype without reliable acknowledgements does not prove lossless durability.

## Relevant research boundaries

Historical Phase 3 findings (verify against current report):
- Shell hooks can lose pre-history-expanded input; exact typed bytes require another justified capture method.
- Bash DEBUG and Zsh preexec have different granularity; neither substitutes for an application keystroke recorder.
- Nested PTYs, raw input, piped secrets, and terminal mediation create conditional visibility.
- Holder, relay, and analyzer failures differ; a dying holder can terminate its shell, while a dead reader may block a writer.
- sudo's `log_passwords` default observed on sandbox sudo 1.9.15p5 must not be generalized to inventory version 1.9.17p2-8 without K-06.
- OpenSSH client and shell versions in sandbox and Kali inventory differ. SSH mode boundaries require exact command options and PTY state.
- Experimental IDs EXP-13 through EXP-18 and planned Kali tests K-01 through K-14 must remain distinguishable.

These are context pointers, **not independently verified primary evidence**. Quote the report/test log for precise assertions and follow up with actual Kali verification when authorized.

## Security-sensitive changes

Never modify `/etc/sudoers`, drop-ins, PAM, audit rules, login shells, PTY modes, service units, or recorder privileges merely to inspect behavior. If active testing requires a change, get explicit user authorization and specify the isolation and restoration path.

Preserve credential evidence protection; no passwords, tokens, complete secret-bearing commands, or raw sensitive stdin in a public error log or chat handoff. Do not weaken filesystem ownership or permissions to simplify inspection.

## Research workflow

1. State the exact hypothesis or incompatibility.
2. Check matching versions and environment; read bounded primary source excerpts when useful.
3. Prefer the smallest safe read-only test. If a privileged/behavior-changing test is required and not authorized, report it as pending.
4. Capture commands, version, outputs, timestamp/context, and limitations in the report file.
5. Compare with approved requirements; do not silently rewrite policy.
6. Stop when the requested research question is answered or clearly blocked.

## Reconciliation rubric

For each finding state: `claim → environment/source → exact evidence location → affected decision(s) → status → proposed next test or decision`. Use short references rather than pasting full transcripts. Preserve the complete underlying report so later reviewers can inspect it.

A useful output identifies which assertions are verified, which are conditional, what remains impossible under the current method, and which approved requirement is still unmet.
