---
name: project-token-operator
description: "Use for long-running projects: enforce task scope, inspect selectively, protect source files, maintain compact state, and verify phase deliverables."
---

# Project Token Operator

## Purpose

Operate one designated project workspace with minimal repeated inspection, context growth, and avoidable tool use while preserving project correctness and continuity.

This Skill complements **Token Saver**:
- Token Saver provides general efficiency habits across tasks.
- Project Token Operator governs execution inside a specific ongoing project.

Apply this Skill only when the user is working on an identifiable project, repository, vault, codebase, documentation set, or multi-stage deliverable. Do not impose project procedures on unrelated questions.

## 1. Establish the active project

Before project work:
1. Identify the project from the current Claude Project, user request, attached files, or explicit workspace.
2. Check for `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, README, manifest, and existing instructions.
3. Treat the current files as authoritative over remembered summaries.
4. Confirm the active source of truth, working copy, outputs, and constraints.
5. Reuse existing project state. Do not create duplicate trackers or ask for information already recorded.

If the project cannot be identified or its files are unavailable, state exactly what is missing. Do not invent paths, workspace persistence, project facts, or previous progress.

For a new project or missing profile, consult [Project Bootstrap](references/project-bootstrap.md). Use the supplied templates only when creating or updating project configuration is authorized.

## 2. Lock the requested task and phase

For every non-trivial project task, identify:
- The exact requested task or phase.
- The authorized input files and workspace.
- Permitted operations and prohibited changes.
- Required deliverables.
- Acceptance and verification checks.
- The stopping condition.

Execute only the authorized task. Do not advance to another phase, perform unrelated cleanup, redesign settled architecture, or create optional deliverables without permission.

If the user specifies sequential review or a checkpoint, stop at that boundary and wait.

If the next phase is unclear, consult current project state. Do not treat an old chat summary as authorization.

## 3. Minimize project inspection

Use the smallest sufficient working set:
1. Reuse current conversation evidence and already inspected files.
2. Inspect the project index, state, directory tree, or relevant manifest.
3. Search for specific filenames, headings, symbols, records, or dependencies.
4. Read only the necessary sections or line ranges.
5. Expand inspection only when required to understand dependencies, resolve conflicts, or verify the result.

For multi-file work, classify files as required, related, generated, unrelated, or unknown before opening them broadly.

Do not reread unchanged files or repeat successful searches while the results remain valid. After edits, inspect the relevant diff or changed regions first.

For detailed patterns, consult [Phase Execution](references/phase-execution.md).

## 4. Protect the project workspace

- Follow the project's documented source-of-truth hierarchy.
- Preserve original archives, source exports, baselines, and backups unless the user explicitly authorizes modification.
- Work in the designated working copy. Do not overwrite the only recoverable source.
- Preserve existing structure, filenames, identifiers, configuration, and conventions unless change is requested.
- Make the smallest sufficient edit.
- Do not install packages, add dependencies, create helper scripts, or introduce services merely for convenience or marginal token savings.
- Review an existing script before running it, especially if it writes, deletes, migrates, or transforms files.
- Never claim access to a local/cloud workspace unless it is actually available in this session.

Project-specific rules in `PROJECT_PROFILE.md` take precedence over generic examples in this Skill, unless they conflict with safety or an explicit newer user instruction.

## 5. Preserve project knowledge and evidence

Keep durable context separate from transient task material:
- **Project profile:** stable purpose, workspace paths, source hierarchy, constraints, conventions, and validation rules.
- **Project state:** current task, verified progress, changed files, blockers, and exact next action.
- **Task context:** only the inputs and decisions needed for the current task.
- **Transient material:** raw outputs, exploratory results, failed searches, and superseded alternatives; do not copy these forward unless they matter.

Do not compress away exact technical evidence, commands, code, logs, data, identifiers, hashes, credentials, measurements, or provenance.

Distinguish confirmed results, partial results, failed attempts, hypotheses, proposals, and unverified work. Never turn a suggestion into a claimed action.

For continuity across chats, consult [Context Architecture](references/context-architecture.md).

## 6. Execute and verify proportionately

- Batch independent read-only checks where supported.
- Keep dependent actions and writes sequential.
- Bound tool and command output at its source.
- Use one focused search before broadening.
- Validate according to the risk and scope of the change.
- Inspect changed files and relevant outputs; run focused tests or deterministic checks when available.
- Report skipped checks, unavailable capabilities, and unresolved conflicts.
- Never claim a test, file write, deployment, or validation that did not happen.

For detailed quality gates, consult [Verification and Handoff](references/verification-and-handoff.md).

## 7. Maintain one compact project state

Use an existing state file if available. Do not create another one.

If a project is multi-stage and no state record exists, create one only when the user authorizes it or the task clearly requires a durable handoff and file-writing is available.

Update state at meaningful phase boundaries, not after every minor action. Record verified facts, exact paths, decisions, changes, unresolved issues, and the next authorized task. Keep it smaller than the material it replaces.

Do not paste entire transcripts, source documents, or raw logs into the state file. Never include passwords, API keys, or secrets.

## 8. Completion report and stop

Return a concise project report containing:
1. Status and completed deliverable.
2. Files or resources created, modified, or removed.
3. Verification actually performed.
4. Warnings, blockers, or unresolved issues.
5. State/checkpoint location when relevant.
6. Exact next authorized task, if one exists.

Do not narrate routine tool calls or repeat large file contents. Stop when the requested scope is complete.

## Reference selection

Load only the relevant reference:
- New project, missing configuration, initial reconnaissance → [Project Bootstrap](references/project-bootstrap.md)
- Task boundaries, execution, selective inspection, source protection → [Phase Execution](references/phase-execution.md)
- Project files, context reuse, Projects, new-chat handoffs → [Context Architecture](references/context-architecture.md)
- Validation, completion reports, checkpoints → [Verification and Handoff](references/verification-and-handoff.md)

## Platform boundary

Use only tools and file access actually available in the current Claude session. This Skill does not create persistent storage, grant local filesystem access, increase Free-plan limits, or enable unavailable integrations. If the required workspace is not accessible, ask for the smallest missing input or explain the exact limitation.
