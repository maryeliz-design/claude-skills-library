---
name: admin-refine-response
description: >
  Refines and polishes Teams messages for professional communication. Use whenever
  the user wants to write, draft, improve, or respond to a Microsoft Teams message.
  Triggers on: "refine this message", "help me respond to this", "write a Teams
  message", "polish this", "make this more professional", or any time the user
  shares a rough draft or a received message and wants help crafting a response.
version: 1.0.0
updated: 2026-04-13
relevant_roles: [design, product, engineering, strategy]
owner: "@maryeliz-design"
---

# SKILL: Admin > Refine Response

## Purpose
Produces polished, ready-to-send Microsoft Teams messages. Preserves the user's
authentic voice while improving clarity, tone, and structure. Works for both new
messages and responses to existing ones.

## When to Use
- User wants to write a new Teams message from context or bullet points
- User pastes a received message and wants help responding
- User has a rough draft and wants it polished before sending
- Project updates, stakeholder communications, cross-team coordination,
  responding to feedback, clarifying decisions
- Any Teams message where tone and clarity matter

## When NOT to Use
- Long-form documents, reports, or emails
- Meeting invites (use admin-generate-meeting-invite)
- Post-meeting summaries (use admin-post-meeting-recap)

## Instructions

**Identify the mode:**
- Mode A (New message): user provides what to communicate, key points, audience
- Mode B (Response): user provides the received message, their draft/sentiments,
  and any relevant preceding context
- Infer the mode from context; only ask if genuinely unclear

**Draft the message applying these rules:**
- Length: 50–150 words. Exceed only if complexity requires it — flag when you do
- Formatting: bold for emphasis, bullets for lists; no headers on short messages
- Tone: professional yet personable — direct and warm, never stiff or corporate
- Voice: mirror the user's register from their draft or notes
- Structure: lead with the main point; close with a clear next step if needed
- No filler: avoid "I hope this finds you well", "please don't hesitate to reach out"

**Offer a variant only when warranted:**
On high-stakes or tone-sensitive messages (pushing back, delivering bad news,
chasing a delayed stakeholder), offer two labelled options:
> **Option A – Collaborative**: [message]
> **Option B – Direct**: [message]
Do not default to always offering two versions.

## Output Format
The final message text only — no preamble, no explanation. Ready to copy-paste
into Teams.

## Dependencies
None. Can be used standalone.
