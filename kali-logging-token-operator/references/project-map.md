# Project Map and Source Authority

This document identifies **historically reported** files and decisions. It is not a replacement for the current project workspace or approval ledger.

## Historical Claude Desktop workspace

`/mnt/user-data/outputs/kali-logging-setup/`

Only trust that path after confirming it exists in the current session. Do not assume a Claude cloud directory survives a reset.

| File | Role |
| --- | --- |
| `decisions.md` | Primary approved/pending requirements, provenance, corrections, and technical investigations |
| `architecture-proposal.md` | Proposed technical design; not authorization to implement |
| `Project-Handoff.md` | Environment and project continuity information, subject to live verification |
| `phase3-terminal-mediation-research.md` | Version-qualified terminal-mediation findings, experiments, and proposed Kali tests |
| `backups/` | Historical retained versions; do not overwrite or clean without authorization |
| `reference/` | Original/supplied reference material; inspect only when relevant; keep immutable unless explicitly authorized |

Other files may exist. Discover before assuming either presence or absence.

## Approved design anchors — verify against ledger

Historically recorded requirements include:
- Evidence hierarchy `~/Tools-Log/<tool-name>/<date-stamp>/<session-timestamp>/`, tool-first rather than engagement-first.
- Resolve the original logged-in operator for ownership; `/root/Tools-Log` is a fallback when the original operator cannot reliably be established.
- Preserve exact command/evidence requirements, native output semantics, and special protection of credential-bearing material.
- Detect and report recording failures without destroying in-progress commands; keep a recovery path independent of failed logger.
- Investigate Bash/Zsh hooks, interactive PTYs, sudo native I/O logging, GUI lifecycle, process attribution, and retention feasibility.
- Keep generic system audit separate from the pentesting-tool capture project.

**Do not treat this list as exhaustive** or use it to replace exact decisions. Consult the live `decisions.md` for nuance, later supersession, and status.

## Last reported research checkpoint (not permanent policy)

As reported on 2026-11-07:
- Phase 3 terminal-mediation report corrected; EXP-13–18 ran in a sandbox, **not Kali**.
- Kali tests K-01–K-14 were specified but not run.
- Report's architecture recommendation remained **REDESIGN**.
- `decisions.md` and `architecture-proposal.md` reportedly remained unchanged during that correction.

Before citing any of these as current status, verify files and dates. The report's description in chat is not independently verified by this Skill.

## What the Skill must not do

Do not create a duplicate canonical ledger, reopen approved decisions without evidence, infer that a proposed test ran, or replace concrete Linux evidence with a summary. Never modify operational Kali settings on the strength of a simulation or old report.
