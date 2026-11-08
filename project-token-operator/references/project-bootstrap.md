# Project Bootstrap and Initial Reconnaissance

Load this reference only when the project is new, its operating rules are missing, or the user explicitly requests project setup.

## 1. Do not start with a full read

Begin with a bounded inspection:
1. Confirm which project/workspace the user means.
2. List the top-level files and directories.
3. Read the main README or equivalent entry point.
4. Locate existing manifests, project instructions, state files, and tests.
5. Search for relevant architecture, constraints, and source-of-truth declarations.

Do not recursively read every file. Do not assume the directory tree itself proves which files are authoritative.

## 2. Establish the source-of-truth hierarchy

Identify, when present:
- Original uploads, exports, archives, or raw data.
- Authoritative source files.
- Working copies or transformation areas.
- Generated outputs and reports.
- Temporary files and experiments.

Prefer a hierarchy explicitly documented by the project owner. Never designate a copy as authoritative merely because it is easier to access.

If the hierarchy is unclear and a destructive action is proposed, stop and report the ambiguity.

## 3. Identify project constraints

Extract only confirmed facts:
- Project objective and deliverables.
- Active workspace and exact paths.
- Existing technical architecture and decisions.
- Naming, formatting, and documentation conventions.
- Immutable files or prohibited operations.
- Dependencies and tools already available.
- Required validation and acceptance criteria.
- Current phase, if the state is known.

Keep unknowns marked as unknown. Do not fill gaps with plausible guesses.

## 4. Configure only when useful

Use `templates/PROJECT_PROFILE.template.md` to create a project profile when stable rules and paths need to be reused across tasks or chats.

Use `templates/PROJECT_STATE.template.md` when:
- The project has more than one meaningful phase.
- Work will continue across chats or context resets.
- Several people or tools need to understand verified progress.
- The next action depends on a set of decisions or results that would otherwise need repeated explanation.

Do not create configuration files for a one-off request. Do not overwrite an existing profile or state file; inspect and update it only with authorization.

## 5. Initial deliverable

For a first-time bootstrap, produce:
- A concise inventory of relevant top-level structure.
- The proposed source-of-truth hierarchy.
- Confirmed constraints and decisions.
- Missing facts that block safe execution.
- A minimal profile/state proposal if justified.
- The exact next action.

Do not begin unrelated implementation during bootstrap unless the user explicitly includes it.
