---
name: admin-post-meeting-recap
description: >
  Generates a ready-to-send Teams post-meeting recap with a summary, prioritised
  next steps with tagged owners, and a confirmation prompt. Use whenever the user
  wants to write a meeting recap, send a follow-up summary, or document meeting
  outcomes. Triggers on: "write a recap for", "summarise the meeting", "post-meeting
  summary", "send a follow-up for", "document the outcomes", "write up what we decided".
version: 1.0.0
updated: 2026-04-13
relevant_roles: [design, product, engineering, strategy]
owner: "@MaryCampoTR"
---

# SKILL: Admin > Post-Meeting Recap

## Purpose
Turns raw meeting notes into a ready-to-send Teams recap message with a factual
summary, prioritised next steps with owners and deadlines, and a thumbs-up
confirmation prompt for alignment.

## When to Use
- Immediately after any meeting that produced decisions or actions
- User has notes, decisions, and next steps and wants them formatted for Teams
- Design reviews, stakeholder syncs, planning sessions, working sessions,
  team standups, any meeting requiring documented outcomes and accountability
- Phrases like "write a recap", "summarise the meeting", "send a follow-up",
  "document the outcomes", "write up what we decided"

## When NOT to Use
- Pre-meeting preparation (use admin-pre-meeting-prep)
- Meeting invites (use admin-generate-meeting-invite)
- If no next steps or decisions exist — a recap without accountability is just
  a summary; ask the user for owners before generating

## Instructions

**Collect from the user:**
- Meeting topic / purpose (required)
- Key points discussed (required)
- Decisions made (recommended)
- Next steps with owners (required — ask before generating if missing)
- Timelines / deadlines (recommended; use TBC if unknown)

**Draft the message with this structure:**

**[Meeting topic] — Recap**
*[Date if provided, otherwise omit]*

Summary: 2–4 sentences. Factual and neutral — captures the purpose, key discussion
points, and significant decisions. No evaluative language ("great session!").

**Next Steps**
Numbered list. Each item includes:
- A concrete action (not vague — "Send revised wireframes to @Name" not "Follow up")
- Owner @mentioned as `@Firstname Lastname`
- Deadline: "by [Day Date]" or TBC if unknown

Order by priority or logical sequence.

Close every recap with:
**Please react with 👍 to confirm you've seen this and are aligned on next steps.**

**Tone rules:**
- Direct and factual — this is a record, not a narrative
- No filler: avoid "great discussion", "exciting progress", "as per our conversation"
- Deadlines written consistently: "by Fri 18 Apr" not "end of week" or "soon"
- Contested or unresolved items noted neutrally: "To be confirmed: [item]"

## Output Format
A single Teams message ready to copy-paste. No preamble. After the message,
add one italicised note:
*Verify @mention display names match Teams before sending. Adjust any TBC deadlines before posting.*

## Dependencies
Pairs with admin-pre-meeting-prep (before) and admin-presentation-intro-framework (during).
