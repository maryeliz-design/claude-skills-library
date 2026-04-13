---
name: ux-design-principles
description: >
  Apply Staff Product Designer thinking to any UX requirements spec or v0
  prompt. Use on every feature spec to ensure outputs reflect senior design
  judgment — not just functional requirements. Covers interaction patterns,
  visual hierarchy, cognitive load, form design, empty/error/loading states,
  progressive disclosure, accessibility (WCAG 2.2 AA), and design-system-specific
  design decisions. Runs as a design critique layer on top of the
  ux-requirements-synthesizer output before the v0 prompt is written.
version: 1.0.0
updated: 2026-03-27
---

# SKILL: UX Design Principles — Staff Designer Lens

## Purpose
Ensure every spec and v0 prompt reflects senior design judgment, not just
functional requirements. This skill runs as a critique and enrichment layer
on top of ux-requirements-synthesizer output — catching design gaps, applying
proven patterns, and ensuring the prototype v0 produces is close to
production-quality in its thinking.

---

## When to Apply

Run this skill after the ux-requirements-synthesizer has produced a draft
spec, before writing the v0 prompt. Work through each section below and
annotate the spec with design decisions, pattern recommendations, and
flagged gaps.

---

## 1. Information Architecture & Hierarchy

### Questions to answer for every screen:
- What is the **single most important action** on this screen? Is it the
  most visually prominent element? If not, fix it.
- What is the **reading order**? Does the layout guide the eye from context
  → action → feedback in a logical sequence?
- Are **related items visually grouped**? (Gestalt proximity — things that
  belong together should be near each other)
- Is there a **clear page title** that tells users exactly where they are?
- Is the **hierarchy of headings** correct? (Display → Heading → Body —
  never skip levels)

### Staff Designer standard:
Every screen has one primary action (hero or primary button). Secondary
actions are visually subordinate. Destructive actions are never the most
prominent element on the page.

---

## 2. Progressive Disclosure

### Principle:
Show only what the user needs for the current step. Reveal complexity
gradually, only when it becomes relevant to the task.

### Apply when:
- A form has more than 6–8 fields → consider sectioning or multi-step
- A page has both summary and detail content → show summary first,
  detail on demand (SafDrawer, expand/collapse, SafDialog)
- A feature has advanced options most users won't need → hide behind
  "Advanced settings" or a secondary disclosure
- An AI capability is new to the user → introduce it contextually,
  not all at once

### Design pattern guidance:
- **Wizard / multi-step:** Use when a task has 3+ distinct phases with
  different data needs. Each step should be completable independently.
  Always show progress (step indicator). Always allow back navigation.
- **Expand/collapse sections:** Use for optional or contextual detail
  within a single screen. Default to collapsed for non-critical sections.
- **SafDrawer:** Use for record detail that supplements (not replaces)
  the current view. User stays in context.
- **SafDialog:** Use for focused tasks that require full attention.
  Keep content minimal — if it needs to scroll, it's probably a page.

---

## 3. Form Design

### Field ordering:
- Logical flow matches the user's mental model (not the database schema)
- Required fields before optional fields within a section
- Related fields grouped together (e.g. address fields, date range fields)
- Destructive or irreversible fields last, with extra confirmation

### Field labelling:
- Every field has a visible label (never placeholder-only)
- Labels are concise and specific ("Company name" not "Name")
- Required fields marked consistently (asterisk + legend, or "(required)")
- Optional fields marked with "(optional)" — don't mark everything required
- Help text used sparingly — only when the label alone is insufficient

### Validation:
- **Inline validation** on blur (not on every keystroke — too aggressive)
- **Specific error messages** — "Enter a valid email address" not "Invalid input"
- **Success validation** shown only when genuinely useful (e.g. username availability)
- On submission failure: scroll to first error, focus it, show summary
  alert at top of form
- Never clear the form on error — preserve user input

### Field type selection:
| Use case | design system component |
|---|---|
| Short free text | SafTextField |
| Long free text | SafTextArea |
| Numeric input | SafNumberField (not SafTextField type=number) |
| Single option from short list (≤6) | SafRadioGroup |
| Single option from long list | SafSelect |
| Multiple options from short list | SafCheckboxGroup |
| Multiple options from long list | SafCombobox (multi-select) |
| Searchable single select | SafCombobox (single) |
| On/off setting | SafToggleSwitch |
| Filter tag that can be removed | SafChip type=closable |

### Button placement:
- Primary action always rightmost in a footer (SafButtonFooter type=form)
- Cancel/back always leftmost or as SafButtonInline
- Never two primary buttons side by side
- Destructive confirm button: SafButton appearance=hero (demands attention)
  inside a SafDialog — never inline on the main page

---

## 4. Empty, Loading & Error States

These are not edge cases — they are **core UI states** that must be
designed for every data-driven screen. v0 will not produce them unless
explicitly specified.

### Empty state checklist:
- [ ] Is there an icon that communicates the context (not a generic placeholder)?
- [ ] Is the heading specific? ("No documents found" not "Nothing here")
- [ ] Is there a clear explanation of why it's empty?
- [ ] Is there a primary action to resolve the emptiness (if applicable)?
- [ ] Are there two types of empty state? (1) Zero data ever created vs
      (2) Search/filter returned no results — these need different messages
      and different CTAs

### Loading state checklist:
- [ ] Are SafSkeleton components shaped like the content they replace?
- [ ] Does the skeleton match the approximate number of items expected?
- [ ] Is there a reasonable timeout after which an error state shows?
- [ ] For actions (button clicks): does the button show a loading state
      to prevent double-submission?

### Error state checklist:
- [ ] Is the error message specific about what failed and why?
- [ ] Is there a recovery action (retry, go back, contact support)?
- [ ] For form errors: is each field error adjacent to the field?
- [ ] For page-level errors: is SafAlert type=error used at the top?
- [ ] For catastrophic errors (page won't load): is there an escape path?

---

## 5. Feedback & Confirmation

Users need to know when their actions have succeeded, failed, or are
in progress. Design explicit feedback for every state transition.

### Feedback patterns:
| Action | Feedback pattern |
|---|---|
| Form save (same page) | SafAlert type=success inline, auto-dismiss after 5s |
| Form save (navigate away) | Toast/alert on destination page |
| Destructive action (delete) | SafDialog confirm → success alert after |
| Async operation in progress | Button loading state + SafProgressRing if >2s |
| Background operation | SafAlert type=info, non-blocking |
| Validation error | Per-field state=invalid + top-of-form SafAlert type=error |

### Confirmation dialog rules:
- Required for: delete, deactivate, bulk actions, irreversible operations
- Not required for: save, create, edit (these are easily reversible)
- Dialog copy: be specific about what will be deleted/affected
- Primary confirm button: SafButton appearance=hero (high contrast = gravity)
- Never auto-confirm on a timer

---

## 6. Cognitive Load Management

### Principles:
- **Chunk information** — no more than 5–7 items in an ungrouped list
  before introducing sections or pagination
- **One primary task per screen** — if a screen is trying to do two things,
  consider splitting it
- **Reduce choices** — when a select has >10 options, consider grouping,
  search, or a different pattern entirely
- **Use familiar patterns** — don't invent new interactions when a standard
  pattern exists. Familiar = fast.
- **Surface key information first** — don't bury the most important data
  at the bottom of a long form or table

### Table design:
- Maximum ~7 columns before horizontal scroll or column hiding
- Primary identifier column always first and leftmost
- Sortable columns indicated with icon
- Row actions in final column, right-aligned
- Sticky header for tables > ~10 rows
- Pagination or infinite scroll — never both

### Navigation:
- Current location always indicated (active nav item, breadcrumb)
- Breadcrumbs required for pages > 2 levels deep
- Back navigation always available (browser back or explicit button)
- Never trap users in a dead end

---

## 7. Accessibility — WCAG 2.2 AA (Non-Negotiable)

Every spec must pass this checklist before the v0 prompt is written.
Flag any item that cannot be confirmed as [A11Y-RISK] in the spec.

### Colour & Contrast:
- [ ] Text on background: minimum 4.5:1 contrast ratio (AA)
- [ ] Large text (18px+ or 14px bold): minimum 3:1
- [ ] Interactive elements (buttons, inputs): minimum 3:1 against adjacent colours
- [ ] Never use colour as the only means of conveying information
      (e.g. error state must have icon + text, not just red colour)
- [ ] Status colours are AA-compliant when used as specified —
      do not use Tier 1 palette colours directly (they may not be)

### Keyboard & Focus:
- [ ] All interactive elements reachable by keyboard (Tab / Shift+Tab)
- [ ] Focus order is logical (matches visual reading order)
- [ ] Focus ring always visible — design system focus pattern:
      box-shadow: 0 0 0 2px #ffffff, 0 0 0 4px var(--saf-interactive-focus)
- [ ] No keyboard traps (except intentional modal traps with ESC escape)
- [ ] SafDialog: focus trapped inside modal, returns to trigger on close
- [ ] Skip-to-content link for long navigation headers

### Screen Readers & Semantics:
- [ ] All images have alt text (decorative images: alt="")
- [ ] Form fields associated with labels (SafTextField handles this)
- [ ] Error messages programmatically associated with their field
      (aria-describedby or SafTextField validationMessage prop)
- [ ] Icon-only buttons have aria-label (SafButtonIcon requires this)
- [ ] Status changes announced (SafAlert uses role=alert or aria-live)
- [ ] Data tables have column headers (th with scope)
- [ ] Modal dialogs have aria-labelledby pointing to the dialog title

### Touch & Motor:
- [ ] Minimum touch target: 44×44px (some design systems use 40px —
      flag if compact density used on mobile)
- [ ] Sufficient spacing between adjacent touch targets
- [ ] No interactions that require precise hovering or drag-only actions

### Content & Language:
- [ ] Plain language — reading level appropriate for the audience
- [ ] Error messages in plain language (not error codes)
- [ ] Instructions don't rely on position alone ("click the button on the left")
- [ ] Time limits: user can extend or disable if applicable

---

## 8. Motion & Animation

- Use animation purposefully — it should communicate state change,
  not decorate
- Respect prefers-reduced-motion — all animations must have a static
  fallback
- Loading skeletons: animate-pulse (subtle, not distracting)
- Transitions: 150–200ms for micro-interactions, 250–300ms for larger
  layout changes
- Never autoplay video or audio without user consent

---

## 9. Copy & Microcopy Standards

### Voice:
- Professional, clear, human — not robotic or overly casual
- Active voice ("Save document" not "Document will be saved")
- Second person ("Your documents" not "User documents")
- Sentence case for UI labels (not Title Case For Everything)

### Error messages — the 3-part formula:
1. **What happened** ("We couldn't save your changes")
2. **Why** ("Your session has expired")
3. **What to do** ("Sign in again to continue")

### Empty states — the 2-part formula:
1. **What's missing and why** ("No documents yet")
2. **What to do about it** ("Create your first document to get started")

### Buttons:
- Verb + noun format ("Save document", "Add user", "Delete record")
- Never generic labels ("OK", "Submit", "Yes") — be specific
- Destructive actions: match the consequence ("Delete", "Remove", "Deactivate")
  not softened ("Confirm", "Continue")

### Placeholders:
- Use for format hints only ("DD/MM/YYYY", "+1 555 000 0000")
- Never use placeholder as a substitute for a label
- Never use placeholder for instructions — use helpText instead

---

## 10. Design Critique Output Format

After applying this skill to a spec, append a **Design Critique** section:

```
## Design Critique

### Hierarchy & Layout
[observations and recommendations]

### Progressive Disclosure
[recommendations for what to hide/reveal]

### Form Design
[field type, ordering, validation recommendations]

### States Coverage
- Empty state: [defined / needs work / missing]
- Loading state: [defined / needs work / missing]
- Error state: [defined / needs work / missing]
- Success feedback: [defined / needs work / missing]

### Cognitive Load
[recommendations to simplify or chunk]

### Accessibility Flags
[A11Y-RISK items — what needs attention before handoff]

### Copy Recommendations
[specific label, error, or empty state copy suggestions]

### Patterns Applied
[list of design patterns recommended and why]
```



============================================================
FILE: agentic-ai-ux.md
SAVE AS: agentic-ai-ux.md
============================================================

---
name: agentic-ai-ux
description: >
  Apply Human-AI agent interaction UX principles to any feature spec or v0
  prompt that involves AI-generated content, AI recommendations, automated
  actions, or agentic AI experiences. Use when the feature being designed
  includes any AI agent behaviour — surfacing recommendations, taking actions
  on behalf of users, generating content, or operating autonomously. Covers
  transparency, user control, boundaries, cognitive modularity, error
  recovery, feedback loops, privacy, and accessibility for AI interactions.
  Based on the Human-AI Agent Interaction UX design principles.
version: 1.0.0
updated: 2026-03-27
---

# SKILL: Agentic AI UX — Human-AI Interaction Design Principles

## Purpose
Ensure features involving AI agents are designed to build user trust,
maintain human control, and operate transparently. This skill runs as a
specialist design layer on top of ux-requirements-synthesizer and
ux-design-principles — applied only when the feature includes AI agent
behaviour of any kind.

---

## When to Apply

Apply this skill when the feature spec includes any of:
- AI-generated recommendations, summaries, or content
- Automated actions taken on the user's behalf
- Agentic AI that operates across multiple steps or sessions
- AI that accesses external data, documents, or systems
- AI confidence scores, citations, or sourced outputs
- User feedback loops that improve AI behaviour
- Any "AI does X for you" capability

---

## The 9 Principles — Design Criteria & Patterns

---

### Principle 1: Transparency & Explainability

**Core question:** Can the user understand *why* the AI did what it did?

Users must be able to validate, correct, or override AI output with
confidence. Black-box AI erodes trust irreversibly.

#### Criterion 1.1 — Reasoning visibility
> Do users understand the reasoning behind the AI agent's critical decisions?

**Design patterns to specify in the v0 prompt:**
- **Explanation affordance:** Every AI recommendation includes a
  "Why this?" or "How was this generated?" trigger
  → Use SafButtonInline or SafTooltip for inline explanations
  → Use SafDrawer for detailed reasoning that needs more space
- **Confidence signal:** When AI confidence is variable, surface it
  → SafBadgeStatus: high confidence = success, medium = warning, low = neutral
  → Never show a confidence score as a raw percentage without context
- **Key factors summary:** List the 2–3 most influential inputs that
  shaped the AI output (e.g. "Based on: document type, jurisdiction, date")
- **Audit trail:** For high-stakes actions, log what the AI did and why
  → Accessible via SafDrawer or a dedicated history/audit screen

**Spec annotation format:**
```
[AI-TRANSPARENCY] Reasoning affordance required:
  Trigger: [SafButtonInline "Why this?" | SafTooltip | info icon]
  Content: [what the explanation should contain]
  Location: [inline with recommendation | SafDrawer | modal]
```

#### Criterion 1.2 — Source citations
> Do users have direct access to source citations for AI-generated recommendations?

**Design patterns:**
- Inline citation markers on AI-generated text (numbered refs or footnotes)
- Cited source accessible via SafAnchor (opens source) or SafDrawer
  (shows source preview)
- Distinguish clearly: **AI inference** vs **sourced fact**
  → Use visual differentiation (icon, label, or SafBadgeStatus)
- When no source exists: state explicitly ("AI-generated — no source")
  → Never omit this disclosure

**Spec annotation format:**
```
[AI-CITATION] Source citation required:
  Display: [inline marker | footnote | cited sources list]
  Access: [SafAnchor to source | SafDrawer preview]
  No-source state: [explicit disclosure text]
```

---

### Principle 2: User Control & Agency

**Core question:** Is the human always in control, with meaningful ability
to override or opt out?

Over-reliance on automation removes human judgment from outcomes. Every
AI action must have a human override path.

#### Criterion 2.1 — Override & opt-out
> Do users have the ability to override, refine, or opt out of any AI-driven action?

**Design patterns:**
- **Pause/cancel:** Every AI-initiated process has a visible stop control
  → SafButtonIcon appearance=tertiary (stop icon) always visible during
    AI operations
- **Edit before apply:** AI-generated content is editable before
  confirmation — never auto-applied
  → Recommendation → editable SafTextArea/SafTextField → confirm
- **Manual alternative:** Always provide a path to complete the task
  without AI assistance
  → SafButtonInline "Do this manually" or equivalent escape
- **Persistent opt-out:** If a user disables an AI feature, respect it
  across sessions — never re-enable without explicit consent
- **Parameter adjustment:** For AI outputs driven by configurable inputs,
  expose those inputs so users can refine
  → Inline edit controls or SafDrawer settings panel

**Spec annotation format:**
```
[AI-CONTROL] Override path required:
  Pause/cancel: [where and how]
  Edit before apply: [editable field or confirmation step]
  Manual alternative: [what and where]
  Opt-out: [persistent setting location]
```

#### Criterion 2.2 — High-stakes checkpoints
> Do users have checkpoints and approvals for high-stakes or compliance-sensitive actions?

**Design patterns:**
- Define "high-stakes" explicitly in the spec (e.g. filing a document,
  sending a communication, deleting records, executing a workflow)
- **Explicit approval gate:** AI suggests → user reviews → user confirms
  → AI executes. Never AI suggests → AI executes.
  → SafDialog with SafButtonFooter: "Approve & execute" + "Edit" + "Cancel"
- **Approval summary:** Before confirmation, show a plain-language summary
  of exactly what will happen
- **Timestamp + rationale logging:** Log who approved, when, and what
  they approved — accessible in audit trail
- **Safe exception path:** If user cannot approve (e.g. needs escalation),
  provide an escalation route

**Spec annotation format:**
```
[AI-CHECKPOINT] Approval gate required:
  Trigger condition: [what makes this high-stakes]
  Gate type: [SafDialog | dedicated review screen]
  Summary content: [what the approval summary must include]
  Logging: [what gets recorded]
  Escalation path: [if applicable]
```

---

### Principle 3: Clarity & Consistency

**Core question:** Does the AI behave predictably, and does it feel native
to the user's existing workflow?

#### Criterion 3.1 — Context continuity
> Do users experience consistent context, remembered preferences, and smooth task handoffs?

**Design patterns:**
- **Session memory:** AI retains context from previous interactions —
  users never re-state information the AI already knows
  → Spec must define: what context is retained, for how long, and where
    it is stored
- **Preference persistence:** User choices about AI behaviour (tone,
  detail level, opt-outs) persist across sessions
- **Handoff continuity:** If a task spans multiple sessions, the AI
  resumes from where the user left off
  → Progress indicator showing where in the task the user is
  → Summary of what has been done so far

#### Criterion 3.2 — Workflow integration
> Do users experience the AI as naturally integrated into their existing workflow?

**Design patterns:**
- AI appears contextually within the task — not as a separate mode or
  screen the user has to switch to
- AI suggestions appear adjacent to the relevant content (inline, not
  in a separate panel that requires context switching)
- AI follows the same interaction vocabulary as the rest of the product
  → Use design system components — never invent new AI-specific UI patterns
    unless there is no existing equivalent
- Reduce steps: AI should eliminate work, not add new steps
  → Audit the flow: if the AI feature adds >2 steps, question whether
    it's truly integrated

---

### Principle 4: Boundaries & Limits

**Core question:** Does the user always know when the AI has hit a limit,
and what to do next?

Silent AI failure is the most damaging trust pattern. When the AI cannot
proceed, it must say so explicitly.

#### Criterion 4.1 — Limit transparency
> Do users understand when the AI agent cannot proceed and what next steps to take?

**Design patterns:**
- **Blocked state:** When AI cannot proceed, show:
  1. What it tried to do ("Couldn't summarise this document")
  2. Why it failed ("The document is password-protected")
  3. What the user should do ("Remove password protection and try again")
  → SafAlert type=warning for recoverable limits
  → SafAlert type=error for hard failures
- **Graceful degradation:** When AI feature is unavailable, the manual
  path must still work — never remove core functionality because AI is down
- **Audit recording:** Stuck states are logged for support/audit

**Spec annotation format:**
```
[AI-BOUNDARY] Limit state required:
  Trigger: [what causes the AI to fail or block]
  Message: [what — why — what to do, specific]
  Severity: [warning (recoverable) | error (hard stop)]
  Fallback: [manual alternative still available]
```

#### Criterion 4.2 — Responsibility clarity
> Do users clearly understand the division of responsibility between themselves and the AI?

**Design patterns:**
- **AI label:** All AI-generated content is clearly labelled
  → Visual badge, icon, or label: "AI generated" / "AI suggested"
  → SafBadgeStatus appearance=info or a dedicated AI provenance badge
- **Advisory framing:** AI output is framed as a suggestion, not a
  decision ("AI suggests:" not "Your answer is:")
- **Approval = human ownership:** Once a user approves an AI action,
  that approval is attributed to the user in the audit trail
- **Escalation path:** When the AI reaches its limits, the escalation
  path to human support is visible and accessible

---

### Principle 5: Cognitive Load & Modularity

**Core question:** Is AI-generated complexity presented in digestible,
scannable units?

AI can generate more information than humans can process. The design
must filter and structure AI output, not dump it.

#### Criterion 5.1 — Scannable, digestible units
> Do users receive information in scannable, digestible units?

**Design patterns:**
- **Chunked AI output:** Structure AI responses into sections with
  clear headings — never a wall of AI-generated prose
  → Heading (heading font) → Key point → Supporting detail (collapsed)
- **Priority ordering:** Lead with the most important AI insight —
  don't make users read to the bottom to find the action
- **Progressive detail:** Summary first, full detail behind a disclosure
  → SafButtonInline "Show full analysis" or SafDrawer for detail
- **Progress signalling:** For multi-step AI tasks, show where in the
  process the AI is and what remains
  → Step indicator or SafProgressRing with status text

#### Criterion 5.2 — Progressive capability reveal
> Do users discover AI capabilities gradually, as they become relevant?

**Design patterns:**
- **Contextual introduction:** Introduce AI features at the moment
  they are relevant — not in a feature tour or onboarding dump
  → First-use: SafAlert type=info explaining what the AI will do
  → Subsequent uses: feature is available without explanation
- **No capability overload:** Don't show all AI features at once —
  surface the one most relevant to the current task
- **Trust-building sequence:** Simple AI actions first, high-stakes
  AI actions only after the user has built familiarity
- **Dismissible introductions:** Users can dismiss AI feature callouts
  and the preference persists

---

### Principle 6: Error Handling & Recovery

**Core question:** When AI fails, can the user recover without losing
their work or starting over?

#### Criterion 6.1 — Escalation paths
> Do users have a clear path to escalate when the AI cannot continue?

**Design patterns:**
- **Visible escalation:** "Get human help" or "Contact support" always
  accessible from any AI failure state
  → SafButtonInline or SafAnchor — never buried
- **Context preservation:** When escalating to a human, the AI's
  attempt and the user's context are passed along
  → Auto-populate support form with: what was attempted, what failed,
    relevant document/context identifiers
- **Seamless resume:** After resolving an issue, user returns to exactly
  where they were — no restart required
- **No dead ends:** Every AI error state has at least one forward path

---

### Principle 7: Feedback & Learning

**Core question:** Can users teach the AI, and do they see evidence that
their feedback matters?

#### Criterion 7.1 — Meaningful feedback mechanism
> Do users have a way to provide meaningful feedback that improves AI interactions?

**Design patterns:**
- **Contextual feedback:** Feedback control is adjacent to the AI output,
  not in a separate settings screen
  → Thumbs up/down, star rating, or "Was this helpful?" inline
  → Optional: free-text detail field (collapsed by default)
- **Feedback on specific outputs:** User can flag a specific AI-generated
  item, not just rate the overall experience
- **Low-friction submission:** Feedback submits in one tap/click — never
  require a form

#### Criterion 7.2 — Visible learning loop
> Do users understand how their feedback improves the system?

**Design patterns:**
- **Acknowledgement:** When feedback is submitted, confirm it was received
  and explain how it will be used
  → SafAlert type=success: "Thanks — your feedback helps improve
    AI suggestions for your team"
- **Improvement visibility:** When AI behaviour changes based on feedback,
  surface this
  → "Based on your feedback, AI suggestions now prioritise X"
- **Consent & opt-out:** Users can opt out of contributing to AI
  training — this preference is honoured and visible in settings

---

### Principle 8: Privacy, Data Use & Ethics

**Core question:** Do users know what data the AI uses and how it is handled?

#### Criterion 8.1 — Data transparency
> Do users clearly understand which privacy and data handling policies apply?

**Design patterns:**
- **Just-in-time disclosure:** When AI accesses data (documents, user
  history, external sources), disclose it at the point of access
  → Not buried in a privacy policy — surfaced contextually
  → "This AI uses your recent document history to generate suggestions"
- **Data use summary:** Accessible from any AI feature — one tap to
  see what data is being used and why
- **Retention clarity:** How long is AI interaction data retained?
  Surfaced in settings, not just the privacy policy
- **Clear path to settings:** From any AI feature, user can navigate
  directly to their privacy/data settings
  → SafButtonInline or SafAnchor "Manage data settings"

---

### Principle 9: Accessibility & Inclusion for AI Interactions

**Core question:** Can users of all abilities effectively oversee and
control the AI?

#### Criterion 9.1 — Equitable access
> Do users of varying abilities have equitable access to AI interactions?

**Design patterns:**
- All AI controls meet keyboard and focus standards (see
  ux-design-principles skill)
- AI-generated content is readable by screen readers:
  → Dynamic AI output injected into the DOM must use aria-live regions
  → AI status changes announced: "AI is generating your summary..."
    "Summary complete"
- AI confidence/status indicators never use colour alone
  → Always pair with icon + text label
- Voice/assistive input paths considered if users cannot type

#### Criterion 9.2 — Cognitive accessibility
> Do users understand AI outputs regardless of cognitive processing preferences?

**Design patterns:**
- Plain language in all AI output — no jargon, no legal/technical
  boilerplate without a plain-language summary
- Adjustable detail level: user can request simpler or more detailed
  AI output
- Consistent structure: AI output always follows the same format
  so users know what to expect
- Reading mode / focus mode: if AI generates long content, provide
  a distraction-free reading option

---

## AI UX Critique Output Format

After applying this skill, append an **AI UX Critique** section to the spec:

```
## AI UX Critique

### Transparency & Explainability
- Reasoning affordance: [specified | missing | needs work]
- Source citations: [specified | n/a | missing]
- [AI-TRANSPARENCY] annotations added: [list]

### User Control & Agency
- Override paths: [specified | missing]
- High-stakes checkpoints: [specified | n/a | missing]
- [AI-CONTROL] annotations added: [list]

### Clarity & Consistency
- Context continuity: [addressed | needs work]
- Workflow integration: [addressed | needs work]

### Boundaries & Limits
- Limit states: [specified | missing]
- Responsibility clarity: [addressed | missing]
- [AI-BOUNDARY] annotations added: [list]

### Cognitive Load
- Output chunking: [addressed | needs work]
- Progressive reveal: [addressed | needs work]

### Error Recovery
- Escalation paths: [specified | missing]

### Feedback & Learning
- Feedback mechanism: [specified | n/a | missing]
- Learning loop visibility: [addressed | n/a | missing]

### Privacy & Data Use
- Data disclosure: [specified | missing]

### Accessibility
- AI-specific a11y: [addressed | needs work]
- [A11Y-RISK] items: [list]

### AI UX Patterns Applied
[List of specific patterns added to the spec and why]
```

---

## AI Component Vocabulary (the design system)

No new components needed — use design system components with intentional props:

| AI UX need | recommended pattern |
|---|---|
| AI confidence level | SafBadgeStatus appearance=success/warning/neutral |
| AI provenance label | SafBadgeStatus appearance=info "AI generated" |
| Reasoning trigger | SafButtonInline "Why this?" or SafTooltip |
| Reasoning detail | SafDrawer (right side, dismissible) |
| Approval gate | SafDialog modal=true + SafButtonFooter |
| AI error/limit | SafAlert type=warning or type=error |
| AI in-progress | SafProgressRing + status text (aria-live) |
| Inline feedback | Thumbs up/down as SafButtonIcon appearance=tertiary |
| Feedback confirmation | SafAlert type=success (auto-dismiss) |
| Data settings link | SafButtonInline or SafAnchor |
| Contextual AI intro | SafAlert type=info (dismissible) |
| AI suggested content | SafCard or SafTextArea (editable, pre-populated) |
