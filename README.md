# Tokens-Saver

A collection of Claude Skills focused on reducing unnecessary token and context consumption while preserving accuracy, project continuity, and output quality.

## Skills

| Skill | Purpose |
|---|---|
| [Token Saver](token-saver/) | Advanced general-purpose efficiency across chat, writing, research, analysis, coding, and tool use. Designed for Claude Free and does not depend on paid features. |
| [Project Token Operator](project-token-operator/) | Project-specific execution: source-of-truth control, phase discipline, selective inspection, compact state, and verified handoffs. |
| [Kali Logging Token Operator](kali-logging-token-operator/) | Dedicated Claude Desktop workflow for the Kali logging/terminal-mediation project: research boundaries, exact decision provenance, bounded inspection, and phase-gated verification. |

## Install a Skill in Claude

Each Skill has its own folder containing `SKILL.md` and optional supporting references/templates.

1. Download or clone this repository.
2. ZIP only the selected Skill folder, keeping that folder at the ZIP root.
3. In Claude, open **Customize → Skills → + Create skill → Upload a skill** (or the equivalent Skills view in the current interface).
4. Upload the ZIP and enable the Skill.
5. Ensure **Code execution and file creation** is enabled under Claude Settings → Capabilities.

Install each Skill once. Project-specific configuration files are supplied separately to the relevant project; do not create another Skill copy for every project.

## Which Skill should I use?

- **Token Saver:** General task efficiency across different kinds of work.
- **Project Token Operator:** A designated, recurring project that needs controlled phases, source protection, and continuity across chats.
- **Kali Logging Token Operator:** The specific Kali automatic-logging project with detailed Linux research and decision-ledger rules.

## Design principle

Token reduction is subordinate to correctness. These Skills favor selective retrieval, bounded tool output, minimal repeated work, scoped changes, and compact checkpoints. They do not compress exact source evidence, code, or data.
