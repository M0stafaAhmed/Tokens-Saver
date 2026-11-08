# Phase Execution and Workspace Safety

Load this reference for multi-file changes, project implementation, repository operations, and tasks with explicit phases or approval gates.

## 1. Freeze the task boundary

Convert the request into a compact execution contract:
- Current task/phase.
- Inputs and exact workspace.
- Authorized modifications.
- Prohibited changes.
- Required outputs.
- Acceptance checks.
- Stop condition.

Treat user-defined sequencing as a hard boundary. Finish only the current requested phase. A related improvement is not implicit permission.

## 2. Inspect selectively

Use the following order where it fits:
1. Current project state and profile.
2. Relevant directory listing or inventory.
3. README, manifest, and entry points.
4. Search for target filenames, symbols, headings, or references.
5. Read relevant sections or line ranges.
6. Expand only when dependencies or verification require it.

For a large collection, classify files first:
- Required: directly needed for the task.
- Related: likely to affect the result.
- Generated: output, cache, build, or report.
- Unrelated: outside scope.
- Unknown: insufficient evidence to classify.

Read required and related files first. Do not inspect generated or unrelated content without a reason.

## 3. Protect source and working copies

Before modifying:
- Confirm the target directory and branch.
- Confirm whether files are original, working copies, or generated outputs.
- Preserve a recoverable source before bulk or destructive transformations.
- Check whether an equivalent output already exists.
- Avoid writes outside the authorized workspace.

Never overwrite the only original. Never delete, rename, migrate, or bulk-reformat beyond the explicit scope.

## 4. Execute with minimum change surface

- Make targeted edits.
- Preserve filenames, public interfaces, formats, and established conventions.
- Avoid opportunistic refactors.
- Do not create a second report, tracker, or manifest when one already serves the purpose.
- Use existing dependencies and tools where possible.
- Review scripts before running them.
- Batch independent read-only checks; sequence dependent operations and writes.

If the real project structure contradicts the plan, stop and reassess rather than forcing the original assumptions.

## 5. Avoid context rework

- Do not paste large source files into chat when a file reference, line range, or concise finding is enough.
- Do not reread unmodified inputs already inspected.
- After an edit, inspect the diff or changed section.
- Preserve command/error excerpts only when they explain a decision or reproducibility.
- Maintain a concise file map only when it prevents repeated discovery.

## 6. Phase boundary

At the stopping condition:
1. Verify the current deliverable.
2. Update the project state only if needed.
3. Report what is complete and what is not.
4. State the exact next authorized task.
5. Stop. Do not continue automatically.
