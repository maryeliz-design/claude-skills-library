---
name: session-kickoff
description: >
  Automatically orchestrates a full UX requirements session. Load this skill
  whenever a user provides any combination of feature context, meeting
  transcripts, work items, Figma screenshots, or brief descriptions of what
  they need to build. No session starter prompt needed — this skill reads the
  inputs, loads the right sub-skills in the correct order, and drives the
  session from intake to a completed spec, v0 prompt, and QA report.
version: 2.0.0
updated: 2026-04-13
---

# SKILL: Session Kickoff — Automatic Requirements Orchestrator

## Purpose
Eliminate the need for a session starter prompt. When this skill is active,
any input the user provides — a brief description, a transcript, work items,
a screenshot, or any combination — automatically triggers the full requirements
workflow in the correct order.

The user's only job is to share their inputs. This skill handles the rest.

---

## Step 1 — Always load first (every session, no exceptions)

Read and apply these skills immediately, before doing anything else:

1. **ux-requirements-synthesizer** — core output schema, ambiguity rules, and QA checklist.
2. **ux-design-principles** — Staff Designer critique layer: hierarchy,
   progressive disclosure, form design, states coverage, WCAG 2.2 AA
   accessibility, and copy standards.
3. **user-context** — extract persona, role, domain, sophistication level,
   stakes, and task environment from all available inputs before speccing.
   Build the User Context Profile before touching the spec.

---

## Step 2 — Detect input types and load conditional skills

Scan everything the user has provided. For each input type detected,
load the corresponding skill:

| Input detected | Load skill |
|---|---|
| Meeting transcript, call notes, Slack thread | **transcript-parser** |
| Figma screenshots, UI images, design exports | **figma-ingestion** |
| Any mention of AI agent, AI recommendation, AI-generated content, or automated actions | **agentic-ai-ux** |

If multiple input types are present, load all applicable skills.
Process them in this order: transcript → work items → Figma → brief context.

---

## Step 3 — Parse inputs before speccing (confirm before proceeding)

For each input type, run the relevant parser first and present a structured
summary to the user. Wait for confirmation before moving to the spec.

**If transcript present:**
Run transcript-parser → present Transcript Parse Report →
ask: *"Does this capture the right decisions and requirements?
Anything missing or misread?"*

**If Figma screenshot present:**
Run figma-ingestion → present Component Ingestion Report →
ask: *"Does this match the design intent?
Anything I'm misreading or missing?"*

**If brief context only (no structured input):**
Extract what is known, flag what is [UNRESOLVED], and proceed
directly to the spec — noting assumptions clearly.

Present each parser's output separately and wait for confirmation.
Do not combine all parsers into one wall of output.

---

## Step 4 — Build the spec

After all inputs are confirmed, run ux-requirements-synthesizer to
produce the full spec across all 10 sections:

1. Intent & Context
2. User Stories (normalized)
3. Screen Inventory
4. Component Spec (per screen)
5. Interaction & State Map
6. Data Contract
7. Copy & Tone Notes
8. Constraints & Out-of-Scope
9. Ambiguity Log
10. v0 Prompt

Apply ux-design-principles as a critique layer while building —
weave design judgment into the spec as it is written, not as a
separate pass after the fact.

Apply agentic-ai-ux if the feature involves AI — annotate the spec
with [AI-TRANSPARENCY], [AI-CONTROL], and [AI-BOUNDARY] flags inline.

Apply user-context decisions throughout — copy register, density
defaults, confirmation patterns, and domain vocabulary all flow from
the User Context Profile built in Step 1.

---

## Step 5 — Write the v0 prompt

Load **v0-prompt-patterns** and compose the v0 prompt using the
appropriate screen archetypes. The v0 prompt lives in Section 10
of the spec and must be self-contained — readable without the rest
of the spec.

Always include in the v0 prompt:
- Stack and design system declaration
- One named section per screen
- All states (default, loading, empty, error, success)
- All copy (real labels, not placeholders)
- Constraints / out-of-scope
- AI UX annotations translated into v0 instructions (if applicable)

---

## Step 6 — Run spec QA

Load **spec-qa** and run the full quality gate across all gates:
1. Completeness
2. Design system vocabulary accuracy
3. States coverage
4. Copy completeness
5. Accessibility
6. v0 prompt readiness

Present the QA Report with:
- READY / NOT READY verdict
- Any ❌ blockers (must fix before handoff)
- Any ⚠️ items (fix if time allows)
- Confidence score 1–10

If blockers exist, fix them before presenting the final output.

---

## Step 7 — Present final output

```
## Session Output: [Feature Name]

### User Context Profile
[Role, domain, sophistication, stakes, task environment]

### Spec
[All 10 sections]

### Design Critique
[From ux-design-principles]

### AI UX Critique (if applicable)
[From agentic-ai-ux]

### v0 Prompt
[Paste-ready, self-contained]

### Spec QA Report
[Verdict, blockers, confidence score]
```

---

## Behaviour Rules

1. **Never ask the user to load a skill** — this skill orchestrates everything.
2. **Never skip Step 1** — ux-requirements-synthesizer, ux-design-principles, and user-context are unconditional.
3. **Always confirm parsed inputs before speccing.**
4. **Never present a spec with ❌ blockers** — fix them first.
5. **Always produce both outputs** — a shareable spec AND a paste-ready v0 prompt.
6. **Ambiguity log is not failure** — [UNRESOLVED] items are expected. Surface them clearly.
7. **One screen per v0 prompt section** — never blend multiple screens.

---

## If v0 Output Needs Refinement

Load **v0-refinement** automatically when the user shares v0 output that
missed the mark. Produce a Gap Report and targeted refinement prompts.

Trigger phrases:
- "v0 didn't get..."
- "this isn't right..."
- "it's missing..."
- "the [component] is wrong..."
- Sharing a screenshot of v0 output alongside a complaint
