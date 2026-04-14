---
name: admin-presentation-intro-framework
description: >
  Generates a meeting opening script and time-blocked agenda framework for
  professional presentations. Use whenever the user wants to prepare a talk
  track, draft an opening script, or structure how they'll run a session.
  Triggers on: "help me open this meeting", "write my intro for", "structure
  my presentation", "create a talk track", "draft my opening", or any time
  the user provides meeting context and wants to deliver it confidently.
version: 1.0.0
updated: 2026-04-13
relevant_roles: [design, product, strategy]
owner: "@MaryCampoTR"
---

# SKILL: Admin > Presentation Intro & Framework

## Purpose
Generates two things from meeting context: a 60–90 second verbatim opening
script with delivery cues, and a time-blocked skeletal agenda showing topic
flow, contributors, and wrap-up. Helps the user walk into any meeting prepared
to open confidently and keep the session on track.

## When to Use
- User is preparing to present or facilitate a meeting
- User needs an opening script to deliver verbatim or adapt
- User wants a structured agenda to reference during the meeting
- Stakeholder presentations, design reviews, team alignment sessions,
  workshop kick-offs, strategy sessions
- Phrases like "help me open this meeting", "I have a meeting about",
  "create a talk track", "how should I frame this session", "draft my opening"

## When NOT to Use
- Pre-meeting research and question prep (use admin-pre-meeting-prep)
- Post-meeting documentation (use admin-post-meeting-recap)
- Calendar invite copy (use admin-generate-meeting-invite)

## Instructions

**Collect inputs** — required: meeting topic, key topics/decisions to cover.
Recommended: attendees, desired outcomes, approximate duration (default to 45 min).
If critical inputs are missing, ask once — one message, all questions together.

**Section 1 — Opening Script (~150–225 words / 60–90 seconds spoken)**

Write a verbatim spoken intro with inline delivery cues:
- `[pause]` — a beat to let something land
- `[EMPHASIS]` — word or phrase to stress
- `[gesture: ...]` — optional physical cue (e.g. "gesture to the screen")

Structure of the script:
1. Hook / context-setter — why we're here and why it matters now
2. Introduce the agenda — what will be covered, briefly
3. Set expectations — what decisions need to be made, what's needed from the room
4. Time / logistics — duration and any housekeeping
5. Transition — move into the first topic

Tone: confident, warm, direct. No filler. Open strong — purpose and stakes in
the first two sentences.

**Section 2 — Skeletal Structure**

Time-blocked outline as a simple table. Each block includes:
- Time allocation (e.g. 0:00–0:05)
- Topic / section name
- Who leads or contributes ([Owner] if attendees not provided)
- Purpose: present / discuss / decide / inform

End with a Wrap-Up block: decisions made, next steps and owners, parked items.

## Output Format
Two clearly labelled sections — Opening Script then Skeletal Structure — output
directly with no preamble. Close with one line after both sections:
*Tip: Read the script aloud 2–3 times before the meeting to internalise the rhythm.*

## Dependencies
Pairs with admin-pre-meeting-prep (before the meeting) and
admin-post-meeting-recap (after).
