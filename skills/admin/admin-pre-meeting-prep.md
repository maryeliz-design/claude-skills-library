---
name: admin-pre-meeting-prep
description: >
  Generates a structured pre-meeting prep pack including research context,
  delegation opportunities with ready-to-send Teams messages, strategic questions,
  and facilitation notes. Use whenever the user wants to prepare for an upcoming
  meeting, build context before a stakeholder session, or plan how to navigate a
  difficult meeting. Triggers on: "help me prep for", "I have a meeting about",
  "prepare me for", "what should I know before", "pre-meeting prep", "how should
  I approach this meeting".
version: 1.0.0
updated: 2026-04-13
relevant_roles: [design, product, strategy]
owner: "@MaryCampoTR"
---

# SKILL: Admin > Pre-Meeting Prep

## Purpose
Takes meeting context and produces a four-section prep pack: background research
and knowledge gaps, delegation opportunities with copy-paste Teams messages,
strategic questions categorised by purpose, and facilitation notes with talking
points, friction navigation, and success criteria.

## When to Use
- User is preparing for an upcoming meeting and wants to walk in ready
- Stakeholder meetings, design reviews, strategy sessions, cross-functional
  alignment, any meeting where preparation quality impacts outcomes
- Phrases like "help me prep for", "I have a meeting about", "prepare me for",
  "what should I know before", "pre-meeting prep", "how should I approach this"

## When NOT to Use
- Writing the meeting opening script (use admin-presentation-intro-framework)
- Documenting outcomes after the meeting (use admin-post-meeting-recap)
- Creating the calendar invite (use admin-generate-meeting-invite)

## Instructions

**Collect from the user:**
- Meeting purpose and topic (required)
- Who's attending and the user's role (recommended)
- Known agenda items / discussion points (recommended)
- Specific objectives or concerns (recommended)

If only the topic is provided, proceed with reasonable inferences — flag assumptions.

**Produce four sections in order:**

---

**Section 1 — Pre-Meeting Research & Context**

2–4 bullet points of relevant background on the topic, attendees, or context.
Where knowledge gaps exist that the user should fill, flag them explicitly:
> ⚠️ **Knowledge gap:** [What's unknown and where/how to find it]

Factual and scannable. No padding.

---

**Section 2 — Delegation Opportunities**

1–3 tasks that could be handled by someone else before or after the meeting.
For each, provide a ready-to-send Teams message:

**Delegate to:** [Role or name, or "[Relevant teammate]"]
**Task:** [What needs doing and why it's relevant]

> 💬 **Teams message (copy-paste ready):**
> Hey [name] — I have a [topic] meeting [timeframe]. Could you [specific ask] before then? [One sentence of context.] Thanks

If no delegation opportunities exist: *"No delegation opportunities identified."* — omit messages.

---

**Section 3 — Questions to Ask**

6–10 strategic questions categorised by purpose. Star the top 3–4 with ⭐.

Categories (use whichever apply):
- **🎯 Clarifying** — resolve ambiguity or confirm understanding
- **📊 Strategic** — direction, priority, or decisions
- **🔍 Diagnostic** — surface blockers, risks, or gaps
- **🤝 Alignment** — test or build shared understanding
- **➡️ Forward-looking** — next steps, ownership, timelines

Format:
- ⭐ [Question] *(category)*
- [Question] *(category)*

Starred questions = the ones that matter most if time runs short.

---

**Section 4 — Facilitation Notes**

**Key talking points**
2–4 bullet points — the things most important to say or land in this meeting.
Written as points to make, not questions to ask.

**Friction navigation** (only if tension is anticipated)
> Potential friction: [what it is]
> Suggested approach: [one sentence on how to navigate it]

**Success criteria**
2–3 checkable outcomes:
*"By the end of this meeting, we should have [X]."*
Concrete enough to actually verify — not vague ("aligned") but specific
("agreed on which flows go into the demo").

---

## Output Format
All four sections in order, output directly with no preamble. Close with:
*Tip: Review this 15–20 minutes before the meeting, not the night before — it'll be fresher.*

## Dependencies
Pairs with admin-presentation-intro-framework (during the meeting) and
admin-post-meeting-recap (after). Delegation messages can be polished further
with admin-refine-response.
