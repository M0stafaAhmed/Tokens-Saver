# Evidence Integrity

## Objective

Preserve the examination record so that every technical claim can be traced to actual evidence. Accuracy takes priority over brevity, polish, or apparent completeness.

## Evidence classes

Classify material as one of the following when its status matters:

- Confirmed: directly supported by recorded command output, application response, file contents, or another concrete observation.
- Successfully exploited: the technique was executed and the stated privileged outcome was observed.
- Failed attempt: the approach was actually attempted and did not achieve its intended result.
- Partially validated: some behavior was demonstrated, but the complete intended outcome was not.
- Hypothesis: a plausible explanation or attack path that has not been tested.
- Proposed technique: an approach suggested for possible future testing.
- General technical explanation: background knowledge, not a claim about what happened on the examination target.

Never silently promote one class into another.

## Preserve exact evidence

Preserve source values and technical artifacts accurately, including:

- Commands and arguments.
- Standard output and standard error.
- HTTP requests and responses.
- IP addresses, ports, hostnames, paths and usernames.
- Flags, hashes, tokens and challenge-specific values.
- Configuration excerpts and file permissions.
- Timestamps and ordering when recorded.
- Error messages and failed attempts.

Do not normalize, paraphrase, truncate, mask, or replace an exact value when it is part of the technical evidence. Do not invent a replacement value. If a value is unavailable in the source, say that it is unavailable.

The user has chosen to publish the examination report through a shareable Firebase Hosting URL without authentication. Do not independently redact examination details or flags against that explicit project decision. Do not, however, invent or expose unrelated personal credentials that are not part of the examination record.

## Claims about actions

- Use first person only for actions the record supports.
- Do not claim a command was executed merely because it appears in a proposed command block.
- Do not claim a flag was recovered or submitted unless the record confirms it.
- Do not claim an interactive root shell when the evidence only demonstrates a privileged command or process.
- Distinguish container-root from host-root. A root UID inside a container does not establish host compromise.
- Do not claim persistence, lateral movement, or container escape without evidence.

## Failed attempts and negative results

Preserve failed experiments when they explain the investigation or eliminate a path. Record what was tried, what happened, and what conclusion the evidence supports. Do not delete failed attempts merely to make the report look successful.

## Uncertainty and conflicts

When sources disagree:
1. Identify the conflicting statements.
2. Prefer direct contemporaneous output over later summaries.
3. Preserve both accounts if the conflict cannot be resolved.
4. Mark the result unresolved rather than choosing the more convenient version.

A technically plausible inference must remain labeled as an inference until supported by evidence.

## Validation before delivery

For each transformed document, verify that:
- Exact command blocks remain intact.
- Output and flag values are unchanged.
- Failed attempts remain present.
- The attack chain has not gained unsupported steps.
- User and root records remain associated with the correct machine.
- The document does not claim more than its evidence demonstrates.
