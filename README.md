# Tokens-Saver

A collection of Claude Skills focused on reducing unnecessary token and context consumption while preserving accuracy and output quality.

## Skills

| Skill | Purpose |
|---|---|
| [Token Saver](token-saver/) | General-purpose context and token efficiency for long-context, research, coding, and multi-file tasks. |
| [OSCP Project Operator](oscp-project-operator/) | Project-specific operation of the OSCP-Exam-PoC vault and its instructor-facing website. |

## Install a Skill in Claude

Each Skill is packaged in its own folder with a `SKILL.md` file.

1. Download or clone this repository.
2. ZIP only the selected Skill folder, keeping that folder at the ZIP root.
3. In Claude, open **Customize → Skills → Add → Upload a skill**.
4. Upload the ZIP and enable the Skill.

Do not ZIP the repository root when installing one Skill; Claude expects the selected Skill folder to be the ZIP's top-level directory.

## Design principle

Token reduction is subordinate to correctness. These Skills favor selective retrieval, bounded tool output, minimal repeated work, scoped changes, and compact checkpoints. They do not compress exact source evidence, code, or data.
