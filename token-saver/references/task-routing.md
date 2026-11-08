# Task Routing and Intake

Load this reference when a task has several requirements, ambiguous scope, tool choices, or meaningful execution cost.

## 1. Classify the work

Use the class in `SKILL.md` and choose one primary path.

| Work type | First move | Avoid |
|---|---|---|
| Direct question | Answer from known, reliable context | Browsing or outlining a plan without need |
| Text transformation | Process the supplied source | Re-researching or adding commentary |
| Research / comparison | Define the decision criteria and decisive unknowns | Searching every possible angle |
| Diagnosis / troubleshooting | Reproduce the failure path and isolate the first uncertain point | Changing many variables at once |
| Code / repository | Inspect tree, entry points, and relevant symbols | Reading every file or rewriting unrelated code |
| File / data analysis | Inspect format, schema, and representative content | Dumping all rows or pages |
| Document / artifact | Identify audience, required sections, source material, and output format | Creating multiple drafts or formats unasked |
| Multi-stage project | Establish milestones, inputs, constraints, and checkpoint | Turning every action into a separate phase |

## 2. Intake contract

For non-trivial work, internally extract:

- **Outcome:** what must exist or be decided at completion?
- **Inputs:** which supplied files, messages, systems, or sources are authoritative?
- **Constraints:** what must be preserved, excluded, or not changed?
- **Acceptance checks:** how will success be verified?
- **Stop condition:** where must execution end?

Do not ask the user to fill out a form. Infer what is clear. Ask one concise question only when a missing detail blocks the work or materially changes the result.

If the user has already given a task sequence, permission boundary, or approval gate, preserve it exactly.

## 3. Decide whether a tool is worth its cost

Use a tool only when it changes the quality or feasibility of the result.

| Need | Tool decision |
|---|---|
| Supplied text contains everything needed | No external retrieval |
| A fact may have changed or requires external confirmation | Focused web search |
| A file is attached or available in a connected library | Inspect that file, not a guessed external copy |
| A file must be changed in a connected repository | Use the repository integration and verify the result |
| A calculation is deterministic and non-trivial | Calculate once; show method only as needed |
| A result depends on unavailable local access | State the limitation; do not pretend to execute it |

Before searching, identify the exact uncertainty. A search that cannot alter the decision is probably unnecessary.

## 4. Prompt structure for one-pass execution

When drafting a prompt or consolidating a request, include only the fields that matter:

```text
Goal:
Inputs / source of truth:
Constraints:
Required output:
Validation / definition of done:
Stop condition:
```

Do not force this template on simple prompts. Its purpose is to eliminate avoidable clarification rounds on complex work.

A useful request gives Claude the outcome, necessary context, constraints, and expected output together. It does not need to describe every intermediate action unless the sequence itself matters.

## 5. Research routing

For research:
1. Convert the request into a small set of answerable subquestions.
2. Identify which claims require current verification.
3. Search authoritative sources first; use community sources only when community experience is itself relevant.
4. Use focused follow-up searches to resolve conflicts or gaps.
5. Stop when the decision is supported. Do not keep searching for marginally different sources.
6. Distinguish source-backed facts, interpretation, and recommendation.
7. Cite material external claims and retain publication dates for time-sensitive information.

Do not manufacture certainty when sources conflict or are incomplete.

## 6. Troubleshooting routing

For a failure:
1. Capture the exact error and relevant environment details.
2. Identify the earliest failing operation.
3. Form the smallest set of plausible causes.
4. Test the most discriminating, least destructive check first.
5. Change one causal variable at a time where practical.
6. Preserve the original state before destructive fixes.
7. Stop when the cause and verified fix are established.

Do not repeat failed commands unchanged unless new evidence justifies the retry.

## 7. Output routing

- A yes/no request gets a direct yes/no unless explanation was requested.
- A decision request gets one recommendation, its decisive reasons, and material trade-offs.
- A writing request gets the complete requested draft, not an explanation of how to write it.
- A code request gets usable code and necessary execution/validation details.
- A project task gets the actual deliverable plus a concise completion report.
- A request for multiple options gets multiple options; otherwise do not create variants by default.

Keep the response proportional to its use, not to the amount of material inspected.
