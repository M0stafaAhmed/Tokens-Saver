# Documentation Voice

## Objective

Make the Markdown files read as a coherent personal engineering knowledge base maintained by the user, not as transcripts of conversations with an AI assistant.

## Voice rules

- Write actions the user actually performed in first person when that makes the record clearer: "I enumerated...", "I tested...", "I confirmed...".
- Use neutral technical prose for general explanations, vulnerability mechanics, commands, and reusable procedures. Do not force every paragraph into first person.
- State decisions as the user's decisions only when the project record confirms that the user made them.
- Remove conversational framing, pleasantries, apologies, and references to ChatGPT, an AI assistant, or AI-generated suggestions.
- Remove phrases such as "the assistant explained", "ChatGPT recommended", "we discussed", or "as mentioned in our conversation".
- Do not replace those phrases with false claims of personal testing or discovery.
- Convert an explanation into a standalone technical note only when its technical meaning is clear and supportable.
- If a point was proposed but never tested, label it as a hypothesis, possible approach, or unverified idea.
- If provenance matters, preserve it in a neutral form such as "Proposed approach — not tested" rather than referring to an AI conversation.
- Keep the user's natural technical style: direct, precise, and sufficiently detailed. Do not make the prose artificially academic or overly polished.

## Examples

Conversational:
> The assistant suggested checking Linux capabilities with getcap.

Standalone:
> Linux capability enumeration is part of the privilege-escalation workflow; SUID and sudo checks alone are insufficient.

Do not falsely rewrite it as:
> I checked all Linux capabilities and discovered a privilege-escalation path.

The final example claims an action and result that may never have happened.
