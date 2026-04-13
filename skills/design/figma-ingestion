---
name: figma-ingestion
description: >
  Extract accurate component specifications from Figma screenshots (no MCP,
  no Dev Mode required). Use whenever the user shares a Figma screenshot,
  export, or any UI image and needs it interpreted into design system component
  specs before writing requirements or a v0 prompt. Produces a structured
  Component Ingestion Report that feeds directly into the
  ux-requirements-synthesizer skill.
version: 1.0.0
updated: 2026-03-27
---

# SKILL: Figma Ingestion — Screenshot-Only Visual Analysis

## Purpose
Extract structured component specifications from Figma screenshots with no
MCP or Dev Mode access. Output feeds directly into the
`ux-requirements-synthesizer` spec schema.

**Core discipline:** Never assume. Never invent. Extract what is visible,
flag what is not.

---

## Phase 1 — Visual Inventory

### Step 1: Describe what you see (before any interpretation)

Write a plain-language description of the screenshot:
- How many distinct UI regions/sections are visible?
- What is the approximate layout structure (sidebar + main? top nav + content? form? table?)
- What interactive elements are visible (buttons, inputs, selects, toggles, etc.)?
- Are multiple states or variants shown side-by-side?
- Are there annotations, labels, or red-lines visible?
- What density does the UI appear to use (compact / standard)?

Present this description to the user before proceeding. Ask:
*"Is this the complete view, or are there additional screens/states I should
see before extracting the spec?"*

---

## Phase 2 — Component Identification

### Step 2: Map visible elements to design system components

For each distinct UI element visible, attempt to identify it against the
design system component vocabulary. Use this matching hierarchy:

1. **Exact match** — element clearly matches a known design system component
2. **Probable match** — element likely matches with minor uncertainty
3. **Unrecognised** — element does not match any known design system component
   (flag as [CUSTOM] or [UNRESOLVED])

**Known design system components to match against:**
SafButton · SafButtonIcon · SafButtonEmbeddedIcon · SafButtonInline ·
SafButtonAvatar · SafButtonFooter · SafTextField · SafTextArea ·
SafNumberField · SafSearchField · SafSelect · SafSelectTextField ·
SafListbox · SafOption · SafCombobox · SafCheckbox · SafCheckboxGroup ·
SafRadio · SafRadioGroup · SafToggleSwitch · SafAlert · SafBadgeStatus ·
SafBadgeCounter · SafStatusDot · SafProgressRing · SafTooltip ·
SafBreadcrumb · SafAnchor · SafAnchorCta · SafDialog · SafDrawer ·
SafChip · SafAvatar · SafCard · SafDivider · SafSkeleton ·
SafProductHeader · SafSidenav · SafNav

### Step 3: Extract per-component details

For each identified component, extract as much as is visually determinable:

```
Component: [SafComponentName] | Confidence: high / probable / low
Location: [describe position on screen]
Visible props:
  - appearance: [value if determinable, else UNRESOLVED]
  - density: [standard | compact — infer from sizing]
  - state: [default | hover | focus | invalid | disabled — infer from visual]
  - [other props visible]
Visible content:
  - label: "[text if readable]"
  - placeholder: "[text if readable]"
  - icon: [icon name or description]
Notes: [anything unusual or ambiguous]
```

---

## Phase 3 — Layout & Hierarchy Extraction

### Step 4: Document the layout structure

```
Layout:
  Root: [ProductHeader + Sidenav + MainContent | Full-width | Centered | etc.]
  MainContent:
    - PageHeader: [title text] + [action buttons]
    - [Section name]: [components]
  Overlays: [any modals or drawers visible]
```

Structural pattern vocabulary:
ProductHeader · Sidenav · MainContent · PageHeader · FormSection ·
ActionBar · DataRegion · DetailPanel · EmptyState · Modal · Drawer

### Step 5: Extract visual hierarchy signals

- Primary heading (font size/weight → the project font heading scale)
- Visual groupings (→ form sections or card containers)
- Most prominent CTA (→ appearance=hero or appearance=primary)
- Visual dividers (→ SafDivider)
- Status indicators (→ SafBadgeStatus, SafStatusDot, SafAlert)

---

## Phase 4 — State & Interaction Inference

### Step 6: Identify visible states

- Form fields: error (red border=invalid), success (green), disabled (greyed)
- Buttons: disabled (muted colour)
- Toggles/checkboxes: on/off, checked/unchecked
- Multiple states shown side-by-side (states guide)

### Step 7: Infer implied interactions [INFERRED]

- Search field → results list or filtered view
- Save button → success state + error state
- Table with row actions → detail view or confirmation dialog
- Stepper/wizard layout → previous/next navigation
- Filter bar → data view responds to filter changes

---

## Phase 5 — Copy Extraction

### Step 8: Capture all visible text

```
Copy inventory:
  Page title: "[text]"
  Section headings: ["text1", "text2"]
  Field labels: ["label1", "label2"]
  Button labels: ["label1", "label2"]
  Placeholder text: ["text"]
  Body copy: ["text"]
  Error / validation messages: ["text"]
  Empty state messages: ["text"]
  Badge / status labels: ["text"]
```

Flag unreadable text as [TRUNCATED] or [UNREADABLE].

---

## Phase 6 — Ingestion Report Output

### Step 9: Produce the Component Ingestion Report

Present before any spec or prompt work. Wait for user confirmation.

```
## Component Ingestion Report
Source: [screenshot description / filename]
Confidence: [overall high / mixed / low]

### Layout
[Step 4 output]

### Components Identified
[Steps 2–3 output, one block per component]

### Visual Hierarchy
[Step 5 output]

### States Visible
[Step 6 output]

### Implied Interactions [INFERRED]
[Step 7 output]

### Copy Inventory
[Step 8 output]

### Unresolved Items
[Everything that could not be determined visually]
```

---

## Phase 7 — Handoff to Synthesizer

After user confirms, the ingestion report feeds into ux-requirements-synthesizer:
- Component names/props → Section 4 (Component Spec)
- Layout structure → Section 3 (Screen Inventory)
- Copy inventory → Section 7 (Copy & Tone Notes)
- Implied interactions → Section 5 (Interaction & State Map)
- Unresolved items → Section 9 (Ambiguity Log)

---

## Rules

1. Never invent a component not visible in the screenshot
2. Never assume a prop value that cannot be inferred visually
3. Confidence levels are mandatory on every component match
4. Flag truncated text rather than guessing
5. Multiple screenshots = multiple ingestion passes
6. Annotations override visual inference
7. Ask before assuming screen purpose

---

## Visual Matching Cues

| Visual appearance | Likely design system component |
|---|---|
| Pill/capsule with colored dot + text | SafBadgeStatus |
| Small circular number badge | SafBadgeCounter |
| Small colored dot only | SafStatusDot |
| Solid dark green button | SafButton appearance=primary |
| White outlined green button | SafButton appearance=secondary |
| Ghost/transparent button | SafButton appearance=tertiary |
| Orange/burnt-orange button | SafButton appearance=hero |
| Text with underline only | SafButtonInline or SafAnchor |
| Input with chevron-down | SafSelect or SafCombobox |
| Input with search icon | SafSearchField |
| Input with up/down steppers | SafNumberField |
| Toggle pill (on/off) | SafToggleSwitch |
| Square with checkmark | SafCheckbox |
| Circle radio dot | SafRadio |
| Colored banner with icon | SafAlert |
| Rounded tag with × close | SafChip type=closable |
| Circular user initial/photo | SafAvatar |
| Horizontal rule / divider line | SafDivider |
| Grey shimmer/pulse placeholder | SafSkeleton |
| Circular progress arc | SafProgressRing |
