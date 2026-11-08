# Obsidian and YAML Standards

## Objective

Maintain valid, consistent Obsidian Markdown without imposing one metadata schema on documents that serve different purposes.

## Frontmatter reference

Use this as the reusable-PoC example:

    ---
    type: reusable-poc
    project: OSCP-Exam-PoC
    status: validated
    updated: "2026-11-06"
    related_machines:
      - IN-01
    tags:
      - oscp
      - ssrf
      - url-validation
    ---

This is not a universal schema for every document type.

## YAML rules

- Frontmatter begins on the first line and is enclosed by valid YAML delimiters.
- Use lowercase kebab-case for the type property.
- Quote dates in YYYY-MM-DD format.
- Use two-space indentation for nested mappings and lists.
- Use one list item per line.
- Do not use tabs for YAML indentation.
- Do not create duplicate mapping keys.
- Preserve meaningful existing properties, including properties not listed in the reference example.
- Preserve document-specific properties where they are justified.
- Do not invent missing values, dates, statuses, machine IDs, or tags.
- Do not force one property set onto every document type.
- Keep property ordering consistent within each document type once that type's schema has been established.
- Use tags that describe the actual subject, not tags added merely to increase discoverability.

## Document-type schemas

Establish schemas from the real vault and its existing content. At minimum, distinguish:

- Dashboard.
- Exam Context.
- Machine Overview.
- User foothold.
- Root privilege escalation.
- Methodology.
- Difficulties and Lessons.
- Reusable PoC.
- Script index.

A missing property is not automatically an error. Determine whether it is required for that document type before proposing a change.

## Obsidian links

- Preserve valid wikilinks, aliases, heading links, and block references.
- Preserve the existing folder hierarchy and filenames.
- Do not rename notes to make a guessed link resolve.
- Prefer fully qualified vault-relative links when duplicate basenames make a short link ambiguous.
- A bare link such as [[user]] or [[root]] may be ambiguous when multiple machine folders contain those filenames. Resolve it using the source note's machine context and actual vault structure; otherwise report the ambiguity.
- Do not treat a link as broken solely because an automated resolver cannot interpret an Obsidian-specific feature.
- Distinguish a genuinely missing destination from an ambiguous destination, an external link, and a same-note heading link.
- Preserve links to attachments and embedded files.

## Repair discipline

Before repairing a link:
1. Identify the source file and exact original link.
2. Identify the intended existing destination.
3. Verify that the destination exists.
4. Propose the exact correction.
5. Apply it only in the authorized working copy.

Never invent a destination or create a replacement note just to clear an audit warning.

## Validation

After an authorized metadata or link change:
- Parse YAML with an available parser.
- Check for duplicate keys and malformed frontmatter.
- Confirm list indentation and date formatting.
- Re-run link checks.
- Review ambiguous and unsupported link syntax manually.
- Compare the changed files with the originals to ensure unrelated content was not modified.

Validation is read-only. Do not let a validator silently fix files.
