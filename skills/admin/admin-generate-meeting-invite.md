---
name: admin-generate-meeting-invite
description: >
  Generates structured meeting invite content (description, agenda, and goals)
  ready to paste directly into a calendar invite or meeting request. Use whenever
  the user wants to write a meeting invite, draft a calendar event description,
  or turn rough meeting context into polished invite copy. Triggers on: "generate
  a meeting invite", "write an invite for", "help me set up a meeting", "draft a
  calendar invite", "create a meeting request".
version: 1.0.0
updated: 2026-04-13
relevant_roles: [design, product, engineering, strategy]
owner: "@MaryCampoTR"
---

# SKILL: Admin > Generate Meeting Invite

## Purpose
Turns rough meeting context into three structured sections — Description, Agenda,
and Goal — ready to copy-paste into a calendar invite. Clear, scannable, and
useful to all attendees before the meeting starts.

## When to Use
- User needs to create a calendar invite and wants structured copy
- User has a rough idea of meeting purpose and wants it formalised
- Phrases like "generate a meeting invite", "write an invite for", "help me
  set up a meeting", "draft a calendar invite", "create a meeting request"
- Any time the user describes a meeting they need to schedule

## When NOT to Use
- Opening script or run-of-show for the meeting (use admin-presentation-intro-framework)
- Post-meeting recap (use admin-post-meeting-recap)
- Pre-meeting question and research prep (use admin-pre-meeting-prep)

## Instructions

**Extract from the user's message:**
- What the meeting is about (required)
- Who's involved (optional — shapes tone)
- Key topics or decisions to address (optional — drives agenda)
- General purpose or desired outcome (optional — drives goal bullets)

Infer missing details where reasonable. Only ask if the core purpose is genuinely unclear.

**Produce exactly three labelled sections:**

**Description**
1–2 sentences. What the meeting is about and why it's happening now.
Neutral calendar framing — "This meeting will..." not "I want to..."

**Agenda**
1–3 bullet points. Concrete activities using action-oriented phrasing:
e.g. "Review current wireframes", "Discuss stakeholder feedback", "Align on next steps"
No sub-bullets. No time allocations unless the user requested them.

**Goal**
1–3 bullet points. Specific desired outcomes — what attendees leave with.
Agenda = what you'll *do*. Goal = what you'll *achieve*. Keep them distinct.

No filler: avoid "touch base", "sync up", "circle back".
Bullets should be scannable in under 10 seconds.

## Output Format
Three labelled sections — Description, Agenda, Goal — in order.
No preamble, no commentary. Output only the invite content, ready to copy-paste.

## Dependencies
None. Can be used standalone.
