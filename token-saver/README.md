# Token Saver

A general-purpose Claude Skill for reducing unnecessary context consumption and repeated work without sacrificing correctness.

## What it does

- Uses targeted search and selective file reads instead of loading entire projects by default.
- Bounds tool output and avoids repeating valid reads, searches, and checks.
- Keeps edits scoped and validates only what changed unless broader verification is justified.
- Uses compact checkpoints for multi-stage work when a context reset is likely.
- Protects exact technical evidence, source data, and code from lossy compression.

The Skill has no runtime dependencies and does not require bundled scripts.

## Install in Claude

1. Download the `token-saver` folder or clone this repository.
2. Create a ZIP containing the `token-saver` folder at the ZIP root. Do not ZIP the files without their containing folder.
3. In Claude, open **Customize → Skills**.
4. Choose **Add → Upload a skill** and upload the ZIP.
5. Enable **Token Saver** if Claude presents an enable control.

A ready-to-upload ZIP can also be generated from this folder without changing its contents.

## Use it

Claude can select the Skill when a task matches its description. You can also invoke it explicitly with instructions such as:

- "Use Token Saver while reviewing this repository. Inspect only relevant files and verify the final diff."
- "Apply Token Saver to this multi-file documentation task. Keep exact evidence unchanged."
- "Continue this project from its existing state file. Avoid rereading unchanged inputs."

The Skill is intended for complex or context-heavy tasks. It should not add process overhead to simple requests.

## Package contents

- `SKILL.md` — core operating rules.
- `references/large-task-playbook.md` — detailed patterns for repositories, research, validation, and checkpoints; load only when needed.
