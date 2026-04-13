---
name: transcript-parser
description: >
  Parse and structure messy meeting transcripts into clean, synthesizer-ready
  intent signals. Use whenever the user provides a meeting transcript, call
  notes, or Slack thread as input to a requirements task. Extracts decisions,
  open questions, user pain points, implied features, and out-of-scope markers.
  Output feeds directly into the ux-requirements-synthesizer skill.
version: 1.0.0
updated: 2026-03-27
---

# SKILL: Transcript Parser — Meeting Notes to Intent Signals

## Purpose
Strip noise from meeting transcripts and extract structured signals for
requirements synthesis. A raw transcript is low-density input — this skill
distills it to only what matters for spec writing.

---

## Phase 1 — Orientation

### Step 1: Classify the transcript

Before extracting anything, identify:
- **Meeting type:** Discovery · Requirements review · Design critique · Stakeholder review · Sprint planning · Other
- **Participants:** Roles present (PM, designer, engineer, stakeholder, user) — names optional
- **Product area:** What feature/product is being discussed?
- **Approximate date/recency:** Recent = higher weight; old = flag for validation

State these classifications before proceeding.

---

## Phase 2 — Signal Extraction

### Step 2: Extract by signal type

Read the full transcript and categorise every meaningful statement into one
of these signal buckets:

**DECISION** — something that was agreed upon, confirmed, or signed off
> Format: `[DECISION] "{paraphrased}" — attributed to: [role/name]`
> Weight: High. Treat as confirmed requirement.

**REQUIREMENT** — a stated functional need or user need
> Format: `[REQUIREMENT] "{paraphrased}" — source: [role/name]`
> Weight: High. Feed directly into user stories.

**PAIN POINT** — a problem, frustration, or gap described by any participant
> Format: `[PAIN POINT] "{paraphrased}" — expressed by: [role/name]`
> Weight: Medium. Informs "why" behind requirements.

**OPEN QUESTION** — something explicitly unresolved or deferred
> Format: `[OPEN QUESTION] "{paraphrased}" — raised by: [role/name]`
> Weight: High. Becomes [UNRESOLVED] in spec Ambiguity Log.

**REJECTED IDEA** — something that was explicitly ruled out or dismissed
> Format: `[REJECTED] "{paraphrased}" — reason: [if stated]`
> Weight: High. Feeds directly into Constraints & Out-of-Scope.

**ASSUMPTION** — something treated as true but not explicitly confirmed
> Format: `[ASSUMPTION] "{paraphrased}"`
> Weight: Medium. Flag for validation.

**OPINION / PREFERENCE** — subjective views not backed by data or decisions
> Format: `[OPINION] "{paraphrased}" — from: [role/name]`
> Weight: Low. Do not treat as requirement. Note for context only.

**NOISE** — small talk, repetition, tangents, scheduling, pleasantries
> Do not extract. Discard silently.

---

## Phase 3 — User Story Synthesis

### Step 3: Convert REQUIREMENT and PAIN POINT signals to user stories

For each REQUIREMENT and PAIN POINT signal, write a normalised user story:

```
As a [actor — infer from context or use "user" if unclear],
I want to [goal derived from signal]
so that [outcome — infer if not stated, mark as [INFERRED] if so].

Acceptance criteria (derive from signal + context):
  - [ ] criterion 1
  - [ ] criterion 2 [INFERRED if not stated]
```

If a PAIN POINT doesn't map clearly to a specific feature, write it as a
problem statement instead:
```
Problem: [description]
Opportunity: [what a solution might address — INFERRED]
```

---

## Phase 4 — Scope Signals

### Step 4: Build scope boundaries from transcript

```
In scope (from DECISION + REQUIREMENT signals):
  - [item]

Out of scope (from REJECTED signals):
  - [item] — reason: [if stated]

Assumed in scope (from ASSUMPTION signals — needs validation):
  - [item]
```

---

## Phase 5 — Structured Output

### Step 5: Produce the Transcript Parse Report

```
## Transcript Parse Report
Meeting type: [classification]
Product area: [area]
Participants: [roles]

### Decisions (confirmed requirements)
[All DECISION signals]

### Requirements
[All REQUIREMENT signals + derived user stories]

### Pain Points
[All PAIN POINT signals + derived problem statements]

### Open Questions → Ambiguity Log
[All OPEN QUESTION signals — these become [UNRESOLVED] items in the spec]

### Rejected / Out of Scope
[All REJECTED signals]

### Assumptions (needs validation)
[All ASSUMPTION signals]

### Opinions (context only — not requirements)
[All OPINION signals, brief]

### Synthesizer Handoff Summary
Confirmed requirements: [count]
Open questions to resolve: [count]
Out-of-scope items: [count]
Recommended next input: [what would most help complete the spec —
  e.g. "Figma screenshot of the proposed layout" / "Jira ticket with AC" /
  "Clarification on [specific open question]"]
```

---

## Phase 6 — Handoff to Synthesizer

After presenting the report, the parsed signals feed into
ux-requirements-synthesizer as follows:

- DECISION + REQUIREMENT → Section 2 (User Stories)
- PAIN POINT → Section 1 (Intent & Context)
- OPEN QUESTION → Section 9 (Ambiguity Log)
- REJECTED → Section 8 (Constraints & Out-of-Scope)
- ASSUMPTION → Section 9 (Ambiguity Log, flagged for validation)

---

## Rules

1. **Never invent requirements** not present in the transcript
2. **Paraphrase, don't quote** — summarise intent, not exact wording
3. **Attribute signals to roles**, not names (unless name is the only identifier)
4. **OPINION ≠ REQUIREMENT** — a stakeholder preferring a colour is not a requirement
5. **One signal per line** — do not bundle multiple signals together
6. **Conflicting signals must be flagged** — if two participants contradict each other, create an OPEN QUESTION
7. **Recency matters** — if the transcript contains a revision of an earlier statement, keep only the most recent as DECISION/REQUIREMENT; note the revision

---

## Conflict Detection

When two signals contradict each other, generate an explicit conflict flag:

```
[CONFLICT] Topic: [what]
  Position A: "[paraphrased]" — [role/name]
  Position B: "[paraphrased]" — [role/name]
  → Add to Ambiguity Log as [UNRESOLVED]
```
