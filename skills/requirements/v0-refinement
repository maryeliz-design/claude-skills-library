---
name: v0-refinement
description: >
  Diagnose v0 prototype output that missed the mark and produce targeted
  refinement prompts. Use when v0 has generated a prototype that is
  incomplete, inaccurate, or mishandled complex interactions — and you
  need to fix it without starting over. Covers: gap diagnosis, root cause
  identification, surgical follow-up prompt writing, multi-screen flow
  composition, and complex interaction patterns v0 commonly mishandles.
version: 1.0.0
updated: 2026-03-27
---

# SKILL: v0 Refinement — Diagnosis & Targeted Iteration

## Purpose
When v0 produces output at 60–80% and you need to close the gap efficiently.
Instead of rewriting the entire prompt, this skill diagnoses *why* v0 missed
and writes a surgical follow-up prompt that targets only the gaps — preserving
what worked.

---

## Phase 1 — Gap Diagnosis

### Step 1: Categorise what went wrong

Review the v0 output against the spec. Identify every gap and assign it
to one of these root cause categories:

---

**Category A: Missing content**
v0 didn't generate something that was in the spec.
→ Cause: The spec mentioned it but the v0 prompt didn't repeat it explicitly.
  v0 only produces what the prompt asks for — it doesn't read the spec.
→ Fix: Add the missing element to a follow-up prompt explicitly.

**Category B: Wrong component**
v0 used a generic HTML element or ShadCN component instead of the
specified design system component.
→ Cause: v0 doesn't have native knowledge of the design system. If the prompt
  said "use SafSelect" but didn't describe its structure, v0 substituted.
→ Fix: Describe the component's structure and behaviour, not just its name.

**Category C: Missing state**
v0 generated the default state but not empty/loading/error/disabled states.
→ Cause: States are almost never generated unless explicitly prompted
  with their trigger condition AND visual result.
→ Fix: Prompt each state separately with: trigger → what changes → result.

**Category D: Layout drift**
v0 produced the right components but in the wrong layout or hierarchy.
→ Cause: Layout instructions were ambiguous or implied rather than explicit.
→ Fix: Describe layout with explicit structure (flex/grid), named regions,
  and the relationship between elements.

**Category E: Copy mismatch**
v0 used generic placeholder text instead of specified copy.
→ Cause: Copy wasn't included in the v0 prompt, or was listed separately
  and v0 didn't connect it to the right component.
→ Fix: Inline copy directly with each component in the follow-up prompt.

**Category F: Interaction not implemented**
v0 rendered the visual but the interaction doesn't work (click does nothing,
state doesn't change, form doesn't validate).
→ Cause: v0 needs interactions described as explicit handler logic,
  not just visual descriptions.
→ Fix: Describe interactions as: "When [trigger], [state variable changes
  to X], which causes [visual result Y]."

**Category G: Multi-screen flow broken**
v0 generated screens that don't connect properly — navigation breaks,
state doesn't persist between screens, back button doesn't work.
→ Cause: Multi-screen flows need explicit state management and routing
  instructions — v0 won't infer them.
→ Fix: See Multi-Screen Flow patterns below.

**Category H: Responsive/density wrong**
v0 generated desktop when mobile was needed, or standard density when
compact was specified.
→ Cause: v0 defaults to desktop/standard unless explicitly instructed.
→ Fix: Restate density and responsive requirements at the top of the
  follow-up prompt, not just in component specs.

**Category I: Accessibility missing**
Focus rings absent, aria attributes missing, colour-only status indicators.
→ Cause: v0 doesn't apply accessibility patterns unless explicitly asked.
→ Fix: Add a dedicated accessibility section to the follow-up prompt.

---

### Step 2: Produce a Gap Report

```
## v0 Gap Report
Screen: [screen name]
Overall accuracy: [estimated %]

Gaps identified:
| # | Category | What's missing/wrong | Root cause | Fix approach |
|---|---|---|---|---|
| 1 | [A–I] | [description] | [cause] | [fix] |
| 2 | ... | | | |

Priority order for fixes:
1. [highest impact gap — usually layout or missing states]
2. ...

Recommended approach: [single follow-up prompt | multiple targeted prompts]
```

---

## Phase 2 — Refinement Prompt Patterns

### Pattern 1: Surgical fix (single gap)

Use when one specific thing is wrong and the rest is acceptable.

```
The [component/screen] needs the following fix. Keep everything else
exactly as generated.

[Specific fix instruction]

Details:
- [Component]: [exact correction with props]
- [State/interaction]: [exact trigger → result]
- [Copy]: "[exact text]"
```

---

### Pattern 2: State injection

Use when default state is correct but other states are missing.
Address each state separately — never bundle all states into one prompt.

```
Add the following states to [component/screen name].
Do not change the default state.

## [State name] state
Trigger: [what causes this state]
Visual changes:
  - [Component]: [prop change or style change]
  - [Component]: [change]
Copy changes:
  - [Element]: "[state-specific text]"
Behaviour: [any interaction changes in this state]

## [Next state name] state
[repeat]
```

---

### Pattern 3: Interaction wiring

Use when the visual is correct but interactions don't work.
v0 needs interactions described as explicit state logic.

```
Wire the following interactions. The visual output is correct —
only the interaction logic needs to be added.

## [Interaction name]
Trigger: [user action — "When user clicks [element]"]
State change: [what React state variable changes and to what value]
Visual result: [what the user sees as a result]
Side effects: [any other components that change]
Error condition: [if applicable — when does this fail and what shows]

## [Next interaction]
[repeat]
```

---

### Pattern 4: Layout restructure

Use when components are correct but layout is wrong.

```
Restructure the layout of [screen name]. Keep all components and their
props — only the layout structure changes.

## New layout structure
Root: [flex | grid | other] [direction] [alignment]
  Region 1 — [name]:
    Position: [describe]
    Width: [value or constraint]
    Contains: [component list]
  Region 2 — [name]:
    [repeat]

Spacing:
  - Between [A] and [B]: [saf-* spacing value]
  - [Padding/margin rules]

Responsive behaviour:
  - [breakpoint]: [layout change]
```

---

### Pattern 5: Component substitution

Use when v0 used the wrong component (generic HTML or ShadCN instead
of the design system).

Describe the component's structure and behaviour — don't just name it,
because v0 has no native the design system knowledge.

```
Replace [wrong component] with the correct the design system [SafComponentName].

## [SafComponentName] specification
Visual structure:
  - [Describe the component's anatomy — what it looks like]
  - Container: [dimensions, background, border]
  - [Sub-element 1]: [description]
  - [Sub-element 2]: [description]

Props to apply:
  - appearance: [value] → [visual effect]
  - density: [value] → [sizing effect]
  - [other props]

States:
  - default: [appearance]
  - hover: [appearance — use --saf-interactive-*-hover token]
  - focus: box-shadow: 0 0 0 2px #ffffff, 0 0 0 4px var(--saf-interactive-focus)
  - disabled: [appearance — use --saf-disabled-* tokens]

Tokens:
  - background: var(--saf-interactive-[appearance]-default)
  - foreground: var(--saf-interactive-on-[appearance]-default)
  - border: outline: 1px solid var(--saf-interactive-border-[appearance]-default)
```

---

## Phase 3 — Multi-Screen Flow Patterns

These are the most common sources of "frequently mishandled complex
interactions." Use these patterns when building multi-screen prompts
from scratch OR when fixing broken flows.

### Flow composition rules

1. **One prompt section per screen** — never describe two screens in the
   same section
2. **Explicit routing** — every navigation action must state its
   destination: "On click → navigate to [ScreenName]"
3. **State that persists** must be explicitly named and passed:
   "Pass [data] to [ScreenName] as [prop/param]"
4. **Back navigation** must be specified: "Back button → navigate to
   [ScreenName], preserve [state]"
5. **Entry conditions** for each screen: "This screen renders when [condition]"

### Multi-step form / wizard

```
## Multi-Step Form: [Feature name]
Total steps: [n]
State management: track currentStep (1–n) and formData object

## Step [n]: [Step name]
Entry condition: currentStep === [n]
Progress indicator: Step [n] of [total] — [step label] active

Fields:
  [field specs]

Navigation:
  "Back" (if step > 1): SafButton appearance=secondary
    → currentStep -= 1, preserve all formData entered so far
  "Continue" / "Next": SafButton appearance=primary
    → validate current step fields
    → if invalid: show per-field errors, do not advance
    → if valid: currentStep += 1, merge step data into formData

Final step navigation:
  "Submit": SafButton appearance=primary
    → loading state: button disabled + SafProgressRing
    → on success: navigate to [SuccessScreen], pass [confirmation data]
    → on error: SafAlert type=error at top of form, stay on final step

## Success Screen
Entry condition: form submitted successfully
Shows: [confirmation content]
Primary action: [what user does next]
```

### Table → Detail → Edit flow

```
## Screen 1: [Entity] List
[Table spec]
Row click → navigate to [Entity] Detail, pass entityId

## Screen 2: [Entity] Detail
Entry condition: entityId present in route params
Fetch: load [entity] by entityId
  Loading: SafSkeleton matching detail layout
  Error: SafAlert type=error + retry button
  Success: render detail content

"Edit" button → navigate to [Entity] Edit, pass entityId + current data

## Screen 3: [Entity] Edit
Entry condition: entityId + current data present
Pre-populate: all fields with current data values

"Save" button:
  → loading state
  → on success: navigate back to [Entity] Detail (same entityId),
    show SafAlert type=success "Changes saved"
  → on error: SafAlert type=error at top of form

"Cancel" button → navigate back to [Entity] Detail, no changes
```

### Confirmation → Execute → Result flow

```
## Trigger
[Action button] on [screen]: SafButton appearance=[appearance] "[Label]"
→ opens Confirmation Dialog

## Confirmation Dialog (SafDialog modal=true)
Title: "[Action] [Entity]?"
Body: "This will [specific consequence]. [Irreversibility statement if applicable]."
[SafAlert type=warning if severe]

Footer (SafButtonFooter type=form):
  Left: SafButton appearance=hero "[Confirm action label]"
    → close dialog
    → loading: show SafProgressRing on triggering screen
    → on success: [result — navigate | show alert | update list]
    → on error: reopen dialog with SafAlert type=error
  Right: SafButtonInline "Cancel" → close dialog, no action

## Result state
Success: [where user ends up + what confirmation they see]
Error: [where user ends up + what error they see + recovery path]
```

---

## Phase 4 — v0 Common Mishandlings Reference

Quick lookup of interactions v0 frequently gets wrong, with fix patterns.

| v0 failure | Why it happens | Fix |
|---|---|---|
| Dropdown doesn't open | No open/close state wired | Add isOpen state + toggle on trigger click |
| Form submits without validation | No validation logic | Add per-field validation function called on submit |
| Empty state doesn't show | No conditional render | Add: `{data.length === 0 && <EmptyState />}` |
| Loading state never clears | No async simulation | Add setTimeout or useEffect with loading flag |
| Modal doesn't close on backdrop click | No backdrop handler | Add onClick on overlay div: `() => setIsOpen(false)` |
| Focus ring missing | CSS not applied | Explicitly add focus-visible styles with saf-focus token |
| Tabs don't switch content | No activeTab state | Add activeTab state + conditional content render per tab |
| Table sort doesn't work | No sort logic | Add sortField + sortDirection state + sort function |
| Chips not removable | No remove handler | Add onRemove prop + filter from chips array |
| Toast/alert doesn't auto-dismiss | No timeout | Add useEffect: `setTimeout(() => setVisible(false), 5000)` |
| SafCombobox search doesn't filter | No filter logic | Add filteredOptions = options.filter(o => o.includes(query)) |
| Multi-step back loses data | State not preserved | Lift formData to parent, pass as prop to each step |
| Drawer doesn't close on ESC | No keydown handler | Add useEffect with keydown listener for Escape key |
| Sticky header not sticky | Missing CSS | Add position: sticky, top: 0, z-index to header |

---

## Refinement Session Output Format

```
## v0 Refinement Plan
Original prompt: [brief description]
Output accuracy: [estimated %]

### Gap Report
[Step 2 output]

### Refinement Prompts
[One prompt per gap category, in priority order]
Prompt 1 — [Category + description]:
[prompt text]

Prompt 2 — [Category + description]:
[prompt text]

### Recommended sequence
[Order to apply prompts — some must precede others]

### Expected outcome
After applying all refinement prompts: [estimated % accuracy]
Remaining manual work: [anything that v0 cannot handle and needs
manual code edit]
```
