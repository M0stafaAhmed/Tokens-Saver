# Project Context Architecture and Chat Continuity

Load this reference when the project spans multiple chats, large files, recurring tasks, or long-running phases.

## 1. Separate project memory from task memory

**Stable project memory** includes:
- Purpose and scope.
- Source-of-truth paths.
- Architecture and settled decisions.
- Naming and formatting conventions.
- Immutable inputs and prohibited operations.
- Validation requirements.

**Task memory** includes:
- Current requested deliverable.
- Files required for the active task.
- Temporary findings and decisions.
- Current acceptance checks.

Keep stable rules in `PROJECT_PROFILE.md` or concise Project instructions. Keep current work in `PROJECT_STATE.md`. Keep raw temporary output in its source file or report, not duplicated in chat or state.

## 2. Use one profile and one state file

Do not create competing project profiles, phase trackers, or handoff documents.

- The profile changes only when stable project facts or rules change.
- The state changes when meaningful work is completed, a phase changes, a blocker appears, or the next action changes.

If an existing project uses another established source of truth, retain it rather than forcing this naming convention.

## 3. Curate Claude Project knowledge

When Claude Projects are available:
- Use a dedicated Claude Project for a recurring workspace when the separation is useful.
- Put concise stable instructions and a curated project profile into Project knowledge.
- Avoid uploading multiple duplicate versions of the same file.
- Upload only reusable references and files likely to matter across chats.
- Supply task-specific files in the current chat when they are only needed once.
- Keep long archives and generated outputs out of default Project knowledge unless necessary.

Do not assume every file is relevant to every chat, or that Project knowledge provides unlimited capacity. On Free, choose the most valuable recurring workspaces and keep the knowledge set small.

## 4. Continue versus start a new chat

Continue the current chat when recent details and active files are still needed for the next task.

Start a new chat at a meaningful boundary when:
- The previous phase is complete and verified.
- The next phase has substantially different inputs.
- The current conversation has accumulated irrelevant research or raw outputs.
- A clean context with a compact state file is cheaper than carrying the old history.

Do not restart solely because a chat is long. Re-establishing context and re-uploading files can cost more than continuing.

## 5. Handoff contents

A useful handoff contains only:
1. Project name and objective.
2. Current phase and exact next task.
3. Active workspace and authoritative paths.
4. Constraints, prohibitions, and settled decisions.
5. Verified results and files changed.
6. Unresolved issues and missing inputs.
7. Acceptance checks and stopping condition.

Do not paste the conversation transcript or full documents. Point to exact files and sections.

## 6. Re-verify after a reset

A state file is a record, not proof of current filesystem state.

After opening a new chat:
- Confirm the files are actually attached or accessible.
- Check that referenced paths exist in the current workspace.
- Verify relevant branch/revision or file version when it matters.
- Confirm that the state does not conflict with newer project files.
- Do not claim to remember or access content that is unavailable.
