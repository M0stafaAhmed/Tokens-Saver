---
name: kali-logging-token-operator
description: "Use for the Kali automatic-logging project: minimize Claude context and tool waste while preserving decisions, research evidence, phase boundaries, and verified deliverables."
---

# Kali Logging Token Operator

A focused Claude Desktop Skill for the Kali automatic logging / terminal-mediation project. Apply it when inspecting or editing that project's decisions, architecture, research, tests, or implementation plans. Do not activate for unrelated Kali or logging questions.

## Mission and precedence

Deliver the currently authorized project task with the least avoidable reading, tool output, rework, and conversation overhead. **Correctness, safety, source fidelity, and user instructions outrank token efficiency.**

This Skill complements general-purpose Token Saver and Project Token Operator; it does not require either to be installed. The user selects model and reasoning effort in Claude's interface: **do not insert model or thinking-level directions into task prompts or reports.** A Skill cannot change account allowances.

## 1. Establish the live project boundary

1. Identify the exact phase and requested deliverable from the user's current message. Do not infer permission to proceed from a previous chat or from a report's suggested next step.
2. Confirm the workspace actually exists. The historically used Claude Desktop workspace is `/mnt/user-data/outputs/kali-logging-setup/`, but cloud paths and files must be checked in the current session.
3. Locate the current `decisions.md`, `architecture-proposal.md`, `Project-Handoff.md`, and phase-specific research reports by inspecting filenames and relevant headings. Do not assume historical copies or hashes are current.
4. Treat the current decision ledger as the source for approved requirements, not a summary in this Skill. Consult historical records when provenance or conflict matters.
5. Freeze a small task contract: **inputs; permitted changes; prohibited changes; deliverable; verification; stop condition.** Keep it internal unless the user needs to see it.

When ambiguity does not block safe work, choose the narrowest grounded interpretation. Never restart the former 60-question interview or ask for decisions that the ledger already records.

## 2. Source and claim discipline

Maintain these distinct statuses:
- **User-approved:** a requirement or policy traceable to the decision ledger.
- **Observed:** an experiment or system observation with environment, version, method, and limits.
- **Proposed:** an engineering design or recommendation not yet approved.
- **Unverified:** an assumption or unexecuted test.
- **Conflict:** explicit incompatibility or ambiguous authority; do not silently resolve by invention.

Do not promote a sandbox observation to Kali verification. Version-specific sudo, Bash, Zsh, OpenSSH, PTY, and kernel behavior must remain qualified. Keep original commands, test IDs, log excerpts, timestamps, failures, and results exact when they matter. Never discard a security requirement merely because a prototype fails it.

Read [Evidence and Technical Verification](references/evidence-verification.md) when researching Linux capture feasibility, reconciling decisions, interpreting experiments, or reporting tests.

## 3. One phase, one deliverable, one stop

- Operate only the phase explicitly authorized. Decision reconciliation, research, architecture, implementation, and Kali validation are separate tasks.
- Research tasks are read-only unless an experiment is specifically authorized for the available environment.
- A report is not authority to edit a separate ledger. A ledger update is not authority to redesign architecture.
- No sudoers modifications, `use_pty` changes, package installation, shell startup edits, service changes, deployment, or live Kali experimentation without the user's explicit authorization.
- Make targeted edits in the authorized working copy; preserve originals and relevant backups. Do not create parallel `decisions-final` or `architecture-new` documents.
- Stop immediately after the deliverable and its proportionate validation. Do not begin the next phase even if time or tokens remain.

Read [Phase Gates](references/phase-gates.md) only when coordinating a multi-step phase, editing linked documents, or preparing a handoff.

## 4. Minimize context and tool cost

- Reuse findings and inspected documents still valid in this session.
- Start with a directory inventory or heading outline, then search for exact headings, IDs, and terms. Read bounded sections before opening large files.
- Inspect relevant version-specific manuals and primary documentation when an actual technical claim depends on them, not for background decoration.
- Bound shell output at its source; use counts, targeted ranges, hashes, or diffs. Avoid repeating whole file contents in conversation.
- Batch independent read-only inspections where supported; serialize writes and dependent verification.
- Do not introduce a script, full-system scan, dependency, or expansive research branch merely to save a few tokens.
- Never omit required acceptance checks to reduce output.

Read [Context and Tool Budget](references/context-tool-budget.md) when a task uses extensive files, commands, web research, or a fresh Claude chat.

## 5. Optional read-only helper

`scripts/doc_probe.py` can show bounded Markdown headings, a selected section, file fingerprints, or a small project document inventory. It uses the Python standard library and never edits project files. Review the script before using it, confirm the relevant filesystem is available, and run it only when it is useful. See the README for examples. Its output is inspection assistance, not proof of project correctness.

## 6. Completion and continuity

After working, verify the actual changed file(s), relevant references, and any tests that ran. Confirm untouched documents were not modified when the task requires isolation. If a tool or test is unavailable, state that plainly.

Report concisely:
1. **Status** — completed, partial, blocked, or unresolved.
2. **Deliverable** — exact path(s) and changes.
3. **Verification** — checks actually performed, not planned.
4. **Open issues** — genuine conflicts, unexecuted Kali tests, and evidence gaps.
5. **Stop point** — what was not attempted; next task only if already identified.

Use an existing project handoff or state document when a durable checkpoint is authorized. Do not duplicate whole research reports, paste entire transcripts, or manufacture a second project tracker.

## Reference selection

Load **only** the reference needed for the active task:
- Current project file roles and history-sensitive decisions → [Project Map](references/project-map.md)
- One-phase execution, source safety, approval boundaries → [Phase Gates](references/phase-gates.md)
- Evidence, experiment classification, Kali validation → [Evidence and Technical Verification](references/evidence-verification.md)
- Selective retrieval, compact tools, session reset and checkpoints → [Context and Tool Budget](references/context-tool-budget.md)

This is a project operating procedure, not an implementation specification. Current project documents and the user's explicit instructions take precedence over historical examples.
