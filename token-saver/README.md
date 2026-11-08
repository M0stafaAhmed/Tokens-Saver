# Token Saver

A general-purpose Claude Skill for reducing unnecessary context consumption, tool overhead, and repeated work across chat, writing, research, analysis, and coding.

## What it does

- Uses relevant conversation context instead of retrieving the same information repeatedly.
- Searches and reads selectively rather than loading large projects by default.
- Bounds tool output and batches independent checks safely.
- Keeps edits scoped and validates proportionately.
- Uses compact checkpoints for multi-stage work when a context reset is likely.
- Protects exact technical evidence, source data, and code from lossy compression.
- Keeps response length proportional to the requested depth and the actual task.

The Skill has no runtime dependencies and does not require bundled scripts, hooks, or subagents. Advanced integrations are never assumed.

## Install in Claude

1. Download the `token-saver` folder or clone this repository.
2. Create a ZIP containing the `token-saver` folder at the ZIP root. Do not ZIP the files without their containing folder.
3. In Claude, open **Customize → Skills**.
4. Select **+ Create skill → Upload a skill**.
5. Upload the ZIP and enable the Skill.

Claude decides when the Skill is relevant based on its description. To request it explicitly, start a task with: `Use Token Saver for this task.`

## Example prompts

- "Use Token Saver while reviewing this repository. Inspect only relevant files and verify the final diff."
- "Apply Token Saver to this research task. Search in focused batches and retain citations for factual claims."
- "Use Token Saver to shorten this document without removing technical meaning or exact evidence."
- "Continue from the existing project state. Avoid rereading unchanged inputs."

The Skill should not add process overhead to simple requests or shorten an answer when depth is required.

## Package contents

- `SKILL.md` — core operating rules.
- `references/large-task-playbook.md` — detailed patterns for repositories, research, validation, and checkpoints; load only when needed.
