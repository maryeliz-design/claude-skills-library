---
name: v0-prompt-patterns
description: >
  A pattern library of proven v0 prompt structures for common screen
  archetypes. Use when writing the v0 prompt section of a requirements spec,
  or when asked to produce a v0 prompt directly. Covers: form page, data table,
  dashboard, detail panel, empty/error states, modal flows, and navigation
  shells. Compose from patterns rather than writing from scratch every time.
version: 2.0.0
updated: 2026-04-13
---

# SKILL: v0 Prompt Patterns — Screen Archetypes

## Purpose
Reusable, proven v0 prompt structures for the most common screen types.
Compose from these patterns to produce consistently high-quality prompts
with minimal variation between runs.

---

## Universal Preamble (include in EVERY v0 prompt)

```
Build using [your design system name, e.g. shadcn/ui, MUI, Chakra, or custom].

Stack: [React 18 + TypeScript + Tailwind CSS | Vue 3 | etc.]
Component library: [package name and version if relevant]

Fonts: [heading font] for headings · [body font] for body text · [icon set] for icons

Token / style reminders:
- [List any critical token or class naming conventions]
- [Focus ring pattern if non-standard]
- [Any "gotcha" prop names your design system uses]
- Primary CTA color: [hex]
- Page background: [hex or token]
```

---

## Pattern 1: Navigation Shell

Use for: Any screen that needs a top header + sidebar layout.
Compose this first, then layer content patterns on top.

```
## Navigation Shell

### Top Header
- Background: [dark/brand color]
- Left: product logo/wordmark
- Right: user avatar, settings, notifications

### Sidebar Navigation
- Background: [surface color]
- Width: [e.g. 240px standard, 48px collapsed]
- Nav items: [list items with icons]
- Active state: [description]
- Collapsed state: icons only

### Main Content Area
- Background: [page background]
- Padding: [e.g. 24px]
- Max-width: [e.g. 1200px centered]
```

---

## Pattern 2: Form Page

Use for: Create/edit flows, settings pages, onboarding steps.

```
## [FormName] Form

Layout: Single column, max-width [e.g. 640px], centered.

### Fields
- [FieldName]: [text input | select | textarea | toggle]
  - Label: "[label text]"
  - Placeholder: "[placeholder]"
  - Help text: "[instructional text]"
  - Required: [yes/no]
  - Validation: "[error message on invalid]"

[Repeat per field]

### Actions (footer)
- Primary: "[Submit label]" — [primary button style]
- Secondary: "[Cancel label]" — [ghost/secondary button style]

### States
- Default: form fields in resting state
- Validation error: inline error message below each invalid field, form does not submit
- Loading: primary button shows spinner, fields disabled
- Success: [redirect to X | show success message]

### Empty / pre-fill behaviour
- [If editing: pre-fill all fields from existing record]
- [If creating: all fields empty]
```

---

## Pattern 3: Data Table

Use for: List views, admin tables, search results.

```
## [TableName] Table

Layout: Full-width within content area.

### Toolbar (above table)
- Left: page title "[Title]" + record count badge
- Right: [Search field] + [Filter button] + [Primary action button: "[label]"]

### Columns
| Column | Type | Sortable | Notes |
|--------|------|----------|-------|
| [Name] | text | yes | Primary identifier, links to detail |
| [Status] | badge | no | [list possible values and colors] |
| [Date] | date | yes | Format: [MMM D, YYYY] |
| [Actions] | icon buttons | no | Edit, Delete |

### Row states
- Default: standard row
- Hover: subtle background highlight
- Selected: [checkbox + highlight if multi-select]

### Empty state
- Illustration or icon
- Heading: "[No items yet]"
- Body: "[Descriptive message]"
- CTA: "[Primary action button]"

### Loading state
- Show [3–5] skeleton rows

### Pagination
- [X] rows per page
- Previous / Next controls
- "[X–Y of Z results]" label
```

---

## Pattern 4: Dashboard

Use for: Overview/home screens with metrics and summary content.

```
## [Dashboard Name]

Layout: [2 or 3] column grid, responsive (stack to 1 column on mobile).

### Stat Cards (top row)
Card 1:
  - Label: "[Metric name]"
  - Value: "[e.g. 1,284]"
  - Trend: [+12% vs last period | no trend]
  - Color accent: [e.g. primary brand color on top border]

[Repeat per card — typically 3–4]

### Charts (middle row)
Chart 1:
  - Type: [line | bar | donut]
  - Title: "[Chart title]"
  - Data: [describe what it shows]
  - Color sequence: [list colors in order]
  - X-axis: [label]
  - Y-axis: [label]

### Secondary content (bottom row)
- [Recent activity list | Quick actions | Data table summary]

### Loading state
- Skeleton cards for stat row
- Skeleton placeholder for charts
```

---

## Pattern 5: Detail Panel / Drawer

Use for: Side panels, record detail views, inspection drawers.

```
## [PanelName] Detail Panel

Trigger: [clicking a row | clicking an item | button]
Type: [side drawer — right | modal — centered | inline expansion]
Width: [e.g. 480px]

### Header
- Title: [record name or "[Entity] Details"]
- Close button: top-right ×
- Optional: status badge, action buttons

### Sections
Section 1: "[Section name]"
  - [Field]: [value display format]
  - [Field]: [value display format]

Section 2: "[Section name]"
  - [Describe content]

### Footer actions
- Primary: "[Action label]"
- Secondary: "[Action label]" or close

### States
- Loading: skeleton content
- Error: error message with retry
- Empty: "[No data message]"
```

---

## Pattern 6: Modal / Confirmation Dialog

Use for: Confirmations, quick-add forms, alerts requiring action.

```
## [ModalName] Dialog

Trigger: [describe what opens it]
Type: [confirmation | form | informational]
Width: [e.g. 480px | 640px]
Backdrop: dimmed, click-outside [closes | does not close]

### Content
- Title: "[Dialog title]"
- Body: "[Supporting message or form fields]"

### Actions
- Primary: "[Confirm/Submit label]" — [primary/destructive style]
- Secondary: "[Cancel label]" — ghost style

### States
- Default: content visible, actions enabled
- Loading: primary button spinner, actions disabled
- Error: inline error message above actions
```

---

## Pattern 7: Empty & Error States

Include these in every pattern that displays data. Never omit.

```
## Empty State
- Icon: [relevant icon]
- Heading: "[Nothing here yet / No results found]"
- Body: "[Short explanation — why it's empty, what to do]"
- CTA: "[Primary action if applicable]"

## Error State
- Icon: warning or error icon
- Heading: "[Something went wrong]"
- Body: "[Brief explanation]"
- Actions: "[Retry]" + "[Contact support / Go back]"

## Loading State
- Use skeleton components that match the shape of loaded content
- Never use a full-page spinner unless the entire page is blocking
```

---

## Composition Guide

Most screens are composed from 2–3 patterns:

| Screen type | Patterns to combine |
|---|---|
| List page | Navigation Shell + Data Table |
| Create/edit page | Navigation Shell + Form Page |
| Dashboard | Navigation Shell + Dashboard |
| Detail view | Navigation Shell + Data Table + Detail Panel |
| Onboarding step | Form Page (no shell) |
| Confirmation flow | Modal + (any triggering pattern) |

Always include the Universal Preamble at the top of the combined prompt.
