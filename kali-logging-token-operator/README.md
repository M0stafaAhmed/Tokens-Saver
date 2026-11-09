# Kali Logging Token Operator

A project-focused Claude Skill for the Kali automatic logging and terminal-mediation project. It follows the staged, evidence-preserving approach of OSCP Project Operator while applying the context-saving patterns of Token Saver and Project Token Operator.

## Why this Skill exists

Large architecture reviews, repeated inspection of long Markdown files, and unconstrained experimental loops can exhaust Claude Free usage without delivering the requested phase. This Skill controls **work boundaries and context use**, not the account's token allowance.

It is specific to this logging project. For unrelated work, use the existing general [Token Saver](../token-saver/) or reusable [Project Token Operator](../project-token-operator/).

## Contents

- `SKILL.md` — short activation, authority, execution, and stopping rules.
- `references/project-map.md` — historical project file roles and provenance.
- `references/phase-gates.md` — bounded work contracts and review gates.
- `references/evidence-verification.md` — Linux experiments, version limitations, and decision integrity.
- `references/context-tool-budget.md` — targeted inspection and economical continuation.
- `scripts/doc_probe.py` — optional read-only document inventory, heading/section extraction, and SHA-256 fingerprints.
- `tests/test_doc_probe.py` — synthetic automated tests for the inspector.

Reference documents are **selectively loaded**. No part of this package stores the live decision ledger or substitutes for project source files.

## Compatibility

Designed for Claude Desktop and web chat, including Free when Skills and code execution are available. It does not depend on Claude Code, hooks, subagents, paid models, MCP servers, extra Python packages, or persistent filesystem access.

The Skill cannot increase quotas, skip usage limits, make the cloud workspace durable, or control reasoning settings.

## Install

1. Download this folder from the repository.
2. ZIP it with `kali-logging-token-operator/` at the ZIP root (not individual files at ZIP root).
3. In Claude, open **Customize → Skills** (or the corresponding Plugins/Skills view if the interface has changed).
4. Choose **Create skill / Upload a skill**, upload the ZIP, and enable it.
5. Ensure **Code execution and file creation** is enabled in Claude Settings → Capabilities.

The folder name and YAML `name` match, and `SKILL.md` is the package entry point.

## Use

Example narrow request:

```text
Use Kali Logging Token Operator. Update the existing decisions.md
using only the corrected Phase 3 research report.
Preserve original decisions; do not edit architecture-proposal.md.
Verify the updated ledger, then stop. No architecture work.
```

Example research-only request:

```text
Use Kali Logging Token Operator. Investigate only whether
sudo 1.9.17p2-8 on the available Kali system has the documented
log_passwords behavior. Record exact versions, commands and
observations. Do not modify sudoers. Stop with findings and gaps.
```

Claude must **not** assume it is running on Kali simply because a historical inventory mentions Kali.

## Optional read-only inspector

Requires Python 3.10+. Review the helper before execution:

```bash
python scripts/doc_probe.py inventory /path/to/kali-logging-setup --limit 30
python scripts/doc_probe.py outline /path/to/decisions.md --limit 70
python scripts/doc_probe.py section /path/to/decisions.md "## 4. Proposed / Pending" --limit 90
python scripts/doc_probe.py fingerprint /path/to/decisions.md /path/to/architecture-proposal.md
```

The `section` command prints a section heading and its body, stopping at the next heading of equal or higher level. Output is capped and explicitly marked truncated when applicable. The script refuses symlink inputs and writes no files.

## Validate before uploading

```bash
python -m py_compile scripts/doc_probe.py tests/test_doc_probe.py
python -m unittest discover -s tests -v
```

The tests use temporary synthetic files. They never touch the real Kali project, scripts, sudoers, runtime logs, or the system configuration.

## Boundaries

The Skill does not authorize changing sudo, service definitions, shell startup, credential evidence, PTY behavior, or the live capture system. It also does not turn experimental evidence into approved design decisions. The current user request and live project ledger control scope.

## Sources and acknowledgements

Design references:
- [OSCP Project Operator](https://github.com/M0stafaAhmed/chat-export-transfer/tree/main/oscp-project-operator)
- [Token Saver](../token-saver/) and [Project Token Operator](../project-token-operator/)
- [Anthropic: Create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent Skills standard](https://agentskills.io/)

Package created for the ongoing Kali logging project. Existing repository authorship and project files are retained; no changes to the referenced Skills are required.
