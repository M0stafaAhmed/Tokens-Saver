# OSCP-Exam-PoC Website Architecture

## Project objective

Transform the maintained OSCP-Exam-PoC Obsidian vault into an interactive, instructor-facing examination report, while retaining the vault as the source documentation.

The instructor will receive a shareable Firebase Hosting URL. After review, the same static website must remain runnable locally.

## Settled architecture

- Frontend: Astro with TypeScript.
- Rendering: static generation.
- Styling and interactions: CSS, Astro components, and lightweight JavaScript.
- Search: Pagefind, generated as part of the static build.
- Hosting: Firebase Hosting.
- Authentication: none.
- Backend: none.
- Database: none.
- Cloud Functions: none.
- Public deployment: intentional; anyone with the URL can access the report.
- Local use: retain a reproducible local website package and build instructions.

Do not add authentication, Firestore, Storage, a database, backend APIs, analytics, or external services unless the user explicitly changes the architecture.

## Content pipeline

1. Preserve the original uploaded archive.
2. Preserve the extracted original source vault.
3. Normalize and validate documentation in a separate working copy.
4. Build the website from the approved working vault.
5. Keep website source code separate from source documentation.
6. Generate static output for Firebase Hosting and local use.

Never modify the original archive or source-vault/ during transformations.

## Website information architecture

The planned website includes:

- Command Center / Dashboard.
- Examination Timeline.
- Machine Dossiers for VE-01, EA-01, ME-01, HA-01, and IN-01.
- Reusable PoC Library, including unsuccessful attempts.
- Methodology.
- Difficulties and Lessons Learned.
- Scripts and Evidence.
- Exam Context and References.

Machine dossiers should preserve separate Overview, User, and Root records where present.

## Design direction

Hybrid presentation:
- Security operations interface for the command center, navigation, status, filters, and timeline.
- Technical editorial presentation for detailed machine reports, methodology, exploit explanations, code, commands, and evidence.
- Dark graphite/charcoal foundation, restrained amber accent, muted cyan secondary accent, readable typography, and clear code blocks.
- Avoid a stereotypical green Matrix aesthetic.
- Use purposeful animation and respect reduced-motion preferences.

## Timeline integrity

- Derive timeline events from recorded source dates and supported chronology.
- Do not fabricate timestamps or examination events.
- Distinguish exact timestamps, date-only records, and inferred ordering.
- Link every event to its supporting machine or project record where possible.

## Content and link handling

The ingestion layer must account for Obsidian frontmatter, wikilinks, aliases, heading links, embeds, callouts, relative Markdown links, attachments, and tags.

Do not silently discard unsupported constructs. Report them and preserve the source material.

Numbers and dashboard statistics must be derived from actual imported records, not invented.

Failed and partially validated attempts must remain distinguishable from validated techniques.

## Privacy and deployment

The user intentionally chose a public, unauthenticated Firebase Hosting report for instructor review. Do not implement a login screen or pretend static files are access-controlled.

The same static build should be usable locally. Provide clear deployment and local-run instructions. Firebase authentication for CLI deployment is performed by the user on their own machine.

Avoid adding external analytics, remote fonts, tracking scripts, or runtime APIs without explicit approval.
