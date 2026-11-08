# Project Verification and Handoff

Load this reference when delivering a project phase, modifying files, handling evidence, or preparing work for a new chat.

## 1. Match verification to the change

| Work | Minimum verification |
|---|---|
| Small documentation edit | Inspect the changed section and surrounding context |
| Multi-file documentation change | Review changed-file list, key references, links, and metadata |
| Code change | Review diff and run the most relevant tests |
| Data transformation | Compare input/output counts and schema; inspect representative records |
| Configuration change | Validate syntax and inspect the effective configuration |
| Repository operation | Verify branch, exact paths, commit, and changed object IDs |
| Build or deployment | Inspect actual build/deploy result and expected output location |
| Research-backed project document | Verify decisive claims and retain source citations |

Use broader checks only when the risk or scope warrants them.

## 2. Preserve technical and factual integrity

Keep exact:
- Commands, arguments, paths, flags, identifiers, IPs, ports, hashes, timestamps, and outputs.
- Source excerpts and provenance.
- Error messages and meaningful failed attempts.
- Configuration values and file permissions.
- Dataset values and record relationships.

Do not claim an operation ran merely because a command appears in a note or plan. Do not claim success from partial evidence.

## 3. Record status precisely

Use:
- **Verified:** directly checked by an appropriate inspection or test.
- **Partially verified:** some acceptance criteria checked; others remain.
- **Not verified:** no direct validation performed.
- **Blocked:** required access, input, or capability is unavailable.
- **Unresolved:** evidence conflicts or does not support a definite conclusion.

Do not describe an artifact as complete if required acceptance checks remain untested.

## 4. Update project state

At a meaningful boundary, update only the relevant state fields:
- Current phase/task and status.
- Completed deliverables.
- Exact changed file paths.
- Verification performed and result.
- Decisions and blockers.
- Next authorized task.

Do not rewrite the entire state file for a small change if a targeted update is possible. Do not bump dates or status fields when no actual project change occurred.

## 5. Completion report

Keep the report actionable:
1. Status.
2. Deliverables and paths.
3. Validation actually performed.
4. Warnings and unresolved items.
5. Checkpoint location.
6. Next authorized task.

Do not echo entire files, logs, or tool outputs.

## 6. Handoff rule

Before handing work to a new chat:
- Ensure the profile and state are current.
- Include only the files necessary for the next task.
- Verify the next task is authorized.
- Preserve exact paths and version identifiers.
- Do not include credentials or secrets.
- Stop at the stated phase boundary.
