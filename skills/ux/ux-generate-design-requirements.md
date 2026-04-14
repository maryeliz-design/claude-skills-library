---
name: ux-generate-design-requirements
description: >
  Accepts any mix of UX reference materials — transcripts, emails, screenshots,
  Figma exports, ADO work items, notes — and synthesizes them into a structured,
  actionable set of UX/design requirements. Use whenever the user wants to generate
  design requirements or turn raw inputs into a spec. Triggers on: "generate
  requirements from", "synthesize these references", "turn this into requirements",
  "create a spec from", "here are my inputs", or any time the user provides
  mixed materials and wants design requirements as output.
version: 1.0.0
updated: 2026-04-13
relevant_roles: [design, product]
owner: "@MaryCampoTR"
---

# SKILL: UX > Generate Design Requirements

## Purpose
Accepts any mix of reference materials and synthesizes them into a structured,
v0-ready UX requirements spec. Acts as an orchestrator — classifies inputs,
applies the right parsing approach to each, then synthesizes everything into
a single coherent spec with a Saffron-ready v0 prompt.

## When to Use
- User provides any combination of transcripts, Figma screenshots, ADO work
  items, emails, notes, or verbal descriptions and wants requirements out
- Starting a new design sprint and need to formalise scattered inputs
- Phrases like "generate requirements from", "synthesize these references",
  "turn this into requirements", "create a spec from", "here are my inputs"

## When NOT to Use
- HTML prototype review (use ux-agentic-ai-prototype-review)
- Single clean ADO work item that just needs a description written
  (use admin-generate-ado-description)

## Instructions

**Step 1 — Classify all inputs**

| Input type | Approach | Signal weight |
|---|---|---|
| Meeting transcript / call notes / Slack thread | Parse for decisions, pain points, implied features, open questions | Medium |
| Figma screenshot / UI image | Extract component specs, layout intent, visual hierarchy | High |
| ADO work item / user story | Normalise to user story format with AC | High |
| Email, notes, bullet points | Extract intent and constraints directly | Low–Medium |
| Existing code / PR | Extract data shape and constraints | High |

State the classification briefly — one line per input — before proceeding.

**Step 2 — Parse each input**

Transcripts/notes: extract decisions, pain points, implied features, open questions,
out-of-scope markers. Weight by source reliability.

Figma screenshots: describe what is visible before interpreting. Extract component
names, layout structure, visual hierarchy, interaction hints. Flag anything that
cannot be determined from the image alone.

ADO work items: normalise to actor / goal / outcome / acceptance criteria.
Flag incomplete or contradictory AC.

Emails/notes/chat: extract intent signals and constraints directly.

Resolve conflicts between multiple inputs of the same type before Step 3.

**Step 3 — Synthesize into a requirements spec**

Produce all sections. Mark [UNRESOLVED] for anything that cannot be inferred — never guess.

```
## Feature: [Name]

### 1. Intent & Context
- Problem being solved
- Primary user
- What triggers this flow
- Success condition

### 2. User Stories (normalised)
As a [actor], I want to [goal] so that [outcome].
Acceptance criteria:
  - [ ] criterion 1

### 3. Screen Inventory
[ScreenName]: [one-line purpose]
Route: [path if known, else UNRESOLVED]

### 4. Component Spec (per screen)
- Saffron component name
- Props and values
- Content / copy
- Conditional visibility rules

### 5. Interaction & State Map
[Trigger] → [State change] → [Visual result]
Include: empty, loading, error, success, disabled, edge cases

### 6. Data Contract
- Key data entities
- Required vs optional fields
- Async operations (loading/error states required)

### 7. Copy & Tone Notes
- Button labels, field labels, error messages, empty states
- Tone: professional / conversational / instructional

### 8. Constraints & Out-of-Scope

### 9. Ambiguity Log
- [UNRESOLVED] item — question to ask

### 10. v0 Prompt (ready to paste)
[Saffron-ready v0 prompt using stack: React 18 + TypeScript + Tailwind CSS 3.4
with saf-* utilities + ShadCN/ui + @saffron/core-components]
```

**Ambiguity rules:**
- Infer: default density = standard; error/loading/empty states always required
  for async data; confirmations for destructive actions
- Always flag [UNRESOLVED]: specific copy not in inputs, async vs sync, navigation
  destinations, role-based visibility, destructive action patterns
- Never invent: business logic, API contracts, Saffron props not in the component map

**Step 4 — Offer iteration path**

After the spec, append:
*To refine: add more inputs and re-run, or resolve [UNRESOLVED] items in the chat
and ask for an updated spec.*

## Output Format
Full spec with all 10 sections. [UNRESOLVED] items only in Section 9.
No preamble — output the spec directly.

## Dependencies
Works with: transcript-parser, figma-ingestion, ado-story-parser (if installed)
for pre-processing inputs before synthesis. Feeds into: ux-agentic-ai-prototype-review
for reviewing the resulting prototype HTML.
