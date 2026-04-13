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
  Based on Human-AI Agent Interaction UX design principles.
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
