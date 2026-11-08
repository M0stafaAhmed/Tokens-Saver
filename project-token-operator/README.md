# Project Token Operator

A project-specific Claude Skill for operating one designated project workspace with low context overhead, strict task boundaries, recoverable state, and reliable verification.

It is designed for long-running repositories, technical projects, Obsidian vaults, documentation systems, research projects, and multi-stage deliverables.

## How it differs from Token Saver

| Skill | Responsibility |
|---|---|
| [Token Saver](../token-saver/) | General efficiency across chat, writing, research, analysis, coding, and tool use |
| **Project Token Operator** | Project-specific source-of-truth, phase control, workspace safety, continuity, and deliverable verification |
| [OSCP Project Operator](../oscp-project-operator/) | Existing OSCP-Exam-PoC-specific rules and documentation workflow |

The Project Token Operator is reusable across projects. It does not contain project facts. Each project supplies its own profile and state.

## Package contents

- `SKILL.md` — core project operating contract.
- `references/project-bootstrap.md` — first-time project reconnaissance and setup.
- `references/phase-execution.md` — scope control, selective inspection, and safe execution.
- `references/context-architecture.md` — durable project context, state, and chat handoffs.
- `references/verification-and-handoff.md` — quality gates and completion reports.
- `templates/PROJECT_PROFILE.template.md` — reusable project-specific configuration.
- `templates/PROJECT_STATE.template.md` — compact task and phase state.

## Install once in Claude

1. Download or clone the repository.
2. Create a ZIP containing the `project-token-operator` folder at its root.
3. In Claude, open **Customize → Skills → + Create skill → Upload a skill**.
4. Upload the ZIP and enable the Skill.
5. Confirm Code execution and file creation are enabled under Claude Settings → Capabilities.

The Skill is account-level. Install it once; do not upload a separate copy for every project.

## Configure each project

For each project that needs strict continuity:

1. Copy `templates/PROJECT_PROFILE.template.md` into the project's own workspace or Claude Project knowledge.
2. Name the copy `PROJECT_PROFILE.md`.
3. Fill only confirmed project details: source of truth, workspace, immutable inputs, working copy, output paths, conventions, prohibited changes, and verification requirements.
4. Copy `templates/PROJECT_STATE.template.md` as `PROJECT_STATE.md` only when the project needs multi-stage continuity.
5. Keep the profile stable. Update the state only at meaningful task or phase boundaries.

Do not create empty profile/state files just to satisfy the Skill. For a small or one-off project task, use the Skill with the actual source files and skip the configuration ceremony.

## Use it

Start a task in the relevant project chat with:

```text
Use Project Token Operator for this project.

Read PROJECT_PROFILE.md and PROJECT_STATE.md if they exist.
Identify the current authorized task and its stopping condition.
Inspect only the files required for that task.
Do not advance to another phase or perform unrelated cleanup.
Preserve source files and exact evidence.
Execute the task, verify the actual output, update project state if needed,
then report changed files, checks, blockers, and the exact next authorized task.
```

For a new project:

```text
Use Project Token Operator to bootstrap this project.
First inspect the existing README, directory structure, and relevant manifests.
Do not modify source files.
Identify the likely source of truth and missing project facts.
Propose a concise PROJECT_PROFILE.md and PROJECT_STATE.md only if they are needed.
Do not invent project details or begin implementation.
```

For a fresh chat, attach or make available the project's current profile, state, and only the source files needed for the next task. Do not paste the full previous conversation.

## Claude Free considerations

The Skill requires no scripts, hooks, subagents, paid models, or Claude Code. In a recurring Claude Project, keep stable instructions and a curated profile in Project knowledge; supply task-specific files in the relevant chat. Do not upload a full repository or archive when a focused subset is sufficient.

The Skill cannot increase usage quotas or guarantee persistent access to local files or prior chats. It only improves the operating discipline.

## Official Claude references

- [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [What are Projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
