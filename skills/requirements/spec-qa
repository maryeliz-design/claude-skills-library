---
name: spec-qa
description: >
  Final quality gate for any UX requirements spec before it is handed off
  to v0, a stakeholder, or a development team. Run after
  ux-requirements-synthesizer, ux-design-principles, and agentic-ai-ux have
  been applied. Produces a binary READY / NOT READY verdict with a clear
  list of blockers and a confidence score. Use before any spec leaves your
  hands.
version: 1.0.0
updated: 2026-03-27
---

# SKILL: Spec QA — Pre-Handoff Quality Gate

## Purpose
A fast, structured final check that gives a binary verdict on whether a
spec is ready to hand off. Catches blockers before they become expensive
rework in v0, stakeholder review, or development.

Run this skill last — after all other skills have been applied.

---

## How to Use

Work through each section below against the spec. Score each item:
- ✅ Pass — criterion is met
- ⚠️ Needs work — criterion is partially met, fixable before handoff
- ❌ Blocker — criterion is not met, spec cannot proceed without resolution

A spec is **READY** only when zero ❌ blockers remain.
⚠️ items should be resolved but do not block handoff if the risk is
acknowledged and documented.

---

## Gate 1: Completeness

### 1.1 — All 10 spec sections present
- [ ] Section 1: Intent & Context
- [ ] Section 2: User Stories with acceptance criteria
- [ ] Section 3: Screen Inventory
- [ ] Section 4: Component Spec (per screen)
- [ ] Section 5: Interaction & State Map
- [ ] Section 6: Data Contract
- [ ] Section 7: Copy & Tone Notes
- [ ] Section 8: Constraints & Out-of-Scope
- [ ] Section 9: Ambiguity Log
- [ ] Section 10: v0 Prompt

### 1.2 — Unresolved items accounted for
- [ ] All [UNRESOLVED] items are in Section 9 only
  (none remaining in Sections 1–8 — those must be resolved or explicitly
  deferred with a named owner and deadline)
- [ ] Every [UNRESOLVED] item has a specific question, not just a flag
- [ ] [INFERRED] items are present only where genuinely inferred from
  inputs — none invented without basis

### 1.3 — Screen coverage
- [ ] Every screen mentioned in Section 3 has a corresponding component
  spec in Section 4
- [ ] No component appears in Section 4 that isn't in Section 3

---

## Gate 2: Design System Vocabulary Accuracy

### 2.1 — Component names
- [ ] Every component name matches the exact design system vocabulary
  (SafButton not Button, SafTextField not Input, etc.)
- [ ] No ShadCN component names used directly
  (Button → SafButton, Input → SafTextField, etc.)
- [ ] No generic HTML element descriptions used where a the design system
  component exists ("dropdown" → SafSelect or SafCombobox)

### 2.2 — Prop accuracy
- [ ] `appearance=` used, not `variant=`
- [ ] `density=` used, not `size=`
- [ ] SafBadgeStatus uses `appearance=info` not `appearance=informational`
- [ ] SafNumberField uses `instructionalText=` not `helpText=`
- [ ] SafButton `appearance=hero` is used for primary CTA (orange),
  not for destructive actions
- [ ] No prop values invented outside the component map

### 2.3 — Token accuracy
- [ ] CSS variables use `--saf-*` prefix throughout
- [ ] No Tier 1 palette tokens referenced directly in component specs
  (e.g. `--saf-color-orange-500` should be a Tier 2 semantic token)
- [ ] Focus ring specified as box-shadow pattern, not outline
- [ ] Form field borders specified as CSS `border` (inside stroke)
- [ ] All other component borders specified as CSS `outline` (outside stroke)

---

## Gate 3: States Coverage

For every screen and every data-driven component, verify:

### 3.1 — Required states present
- [ ] **Default state** — the baseline, populated view
- [ ] **Empty state** — zero data (first-time use)
- [ ] **Empty state (filtered)** — search/filter returned no results
  (different message and CTA from first-time empty)
- [ ] **Loading state** — async data fetch in progress
- [ ] **Error state** — data fetch failed or action failed
- [ ] **Success feedback** — confirmation that an action completed

### 3.2 — Form-specific states
- [ ] **Validation error state** — per-field invalid + top-of-form alert
- [ ] **Submission loading state** — button disabled + loading indicator
- [ ] **Success state** — confirmation after successful submission

### 3.3 — Interactive component states
- [ ] Disabled states specified where applicable
- [ ] Focus states rely on the design system focus ring pattern
- [ ] Hover states consistent with design system interactive tokens

---

## Gate 4: Copy Completeness

### 4.1 — All copy present
- [ ] Every button has a specific verb+noun label (not "Submit", "OK", "Yes")
- [ ] Every form field has a label (not placeholder-only)
- [ ] Every empty state has a heading + body + CTA (if applicable)
- [ ] Every error message follows the 3-part formula:
  what happened + why + what to do
- [ ] Every loading state has status text (not just a spinner)
- [ ] Page titles present for every screen
- [ ] Dialog titles present for every dialog

### 4.2 — Copy tone consistency
- [ ] Tone is consistent across all screens in the spec
- [ ] Sentence case used for labels (not Title Case)
- [ ] Active voice used throughout
- [ ] No placeholder copy remaining ("Lorem ipsum", "TBD", "TODO")

---

## Gate 5: Accessibility

### 5.1 — Non-negotiable a11y criteria
- [ ] All icon-only buttons have aria-label specified
  (SafButtonIcon always requires this)
- [ ] All images/illustrations have alt text specified
- [ ] Form fields use label prop (not aria-label as a label substitute)
- [ ] Error messages associated with their field
  (validationMessage prop on SafTextField/SafSelect/etc.)
- [ ] SafDialog: focus trap and return-to-trigger behaviour specified
- [ ] Colour is never the only means of conveying information
  (status indicators always have icon + text, not colour alone)
- [ ] No touch targets below 44×44px on mobile screens
  (flag if compact density used on mobile)

### 5.2 — Dynamic content
- [ ] AI-generated or dynamically injected content uses aria-live regions
  (if applicable)
- [ ] Status changes announced to screen readers

---

## Gate 6: v0 Prompt Readiness

### 6.1 — Prompt structure
- [ ] Universal preamble present (stack, fonts, design system token reminders)
- [ ] Every screen has a named section in the prompt
- [ ] All states called out explicitly in the prompt
  (v0 will not generate what isn't asked for)
- [ ] All copy included in the prompt (real labels, not placeholders)
- [ ] Constraints / out-of-scope section present

### 6.2 — Prompt clarity
- [ ] No ambiguous instructions ("make it look nice", "standard layout")
- [ ] Layout described with recommended pattern names or explicit structure
- [ ] Component props specified, not just component names
- [ ] Interactions described as trigger → state change → visual result
- [ ] One screen per prompt section (not multiple screens blended)

### 6.3 — Agentic AI prompt (if applicable)
- [ ] [AI-TRANSPARENCY] annotations translated into v0 prompt instructions
- [ ] [AI-CONTROL] override paths specified in prompt
- [ ] [AI-BOUNDARY] limit states specified in prompt
- [ ] AI provenance labels included in component specs

---

## Gate 7: Destination Fitness

Apply the checks relevant to where this spec is going next.

### If going to stakeholder review:
- [ ] Intent & Context (Section 1) is written in plain language —
  no design system jargon
- [ ] User stories are human-readable without design knowledge
- [ ] Ambiguity log is clearly framed as questions, not failures
- [ ] Out-of-scope is explicit to prevent scope creep in the review

### If going to v0 directly:
- [ ] v0 prompt is self-contained — readable without the rest of the spec
- [ ] No spec shorthand in the prompt (e.g. "see Section 4" — copy it in)
- [ ] Prompt length is appropriate — complex screens split into
  separate prompt sections

### If going to dev handoff:
- [ ] Data contract (Section 6) has enough detail for API planning
- [ ] Component props are exact (dev will use these as implementation reference)
- [ ] Interaction & State Map (Section 5) covers all edge cases
- [ ] Accessibility requirements are explicit, not implied

---

## QA Report Output Format

```
## Spec QA Report
Spec: [feature name]
QA date: [date]
Destination: [v0 | stakeholder review | dev handoff | varies]

### Verdict: READY / NOT READY

### Blockers (❌ — must fix before proceeding)
- [Gate X.X] [description of blocker]

### Needs Work (⚠️ — fix if time allows)
- [Gate X.X] [description + recommended fix]

### Passed (✅)
- Gates passed: [list]

### Confidence Score
[1–10 — how confident that v0 will produce a ~90%+ accurate prototype
from this spec, where 10 = paste and go, 1 = significant rework expected]

Confidence rationale: [one sentence explaining the score]
```

---

## Fast-Pass Mode

For time-pressured situations, run only the ❌-critical gates:
Gates 2.1, 2.2, 3.1, 4.1, 5.1, 6.1

These are the gates most likely to cause significant v0 rework if missed.
Flag that full QA was not run and note the risk.
