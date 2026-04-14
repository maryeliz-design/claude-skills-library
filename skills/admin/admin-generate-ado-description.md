---
name: admin-generate-ado-description
description: >
  Generates a structured, Markdown-formatted Azure DevOps (ADO) work item
  description for design tasks — ready to paste directly into a work item.
  Use whenever the user wants to write an ADO description, document a design
  task for a sprint, or turn a brief summary into a formatted work item.
  Triggers on: "generate an ADO description", "write a work item for", "create
  an ADO task for", "document this design task", "write up this sprint item".
version: 1.0.0
updated: 2026-04-13
relevant_roles: [design, product]
owner: "@MaryCampoTR"
---

# SKILL: Admin > Generate ADO Description

## Purpose
Turns design task context into a structured, Markdown-formatted ADO work item
description — clear and actionable for UX, engineering, and product teams.
Output is ready to paste directly into the ADO Description field.

## When to Use
- User needs to create or update an ADO work item for a design task
- User has a Figma link and a list of sprint deliverables and wants them formalised
- Phrases like "generate an ADO description", "write a work item for", "create
  an ADO task", "document this design task", "write up this sprint item"

## When NOT to Use
- Parsing or reading an existing ADO work item (use ux-generate-design-requirements)
- Non-design work items (engineering tasks, bug reports without UX component)

## Instructions

**Collect from the user:**
- Task summary — what the design task is and why it exists (required)
- Figma link — URL to the relevant design files (required)
- Planned updates / deliverables — specific items for this sprint (required)
- Background / references — context, prior decisions, related work items (optional)

If task summary or planned deliverables are missing, ask before generating.

**Produce Markdown with this structure:**

```
## Summary
[2–4 sentences. What is this task, why does it exist, what problem does it address.
Written for a mixed audience: UX, engineering, and product.
Lead with what, then why. Be direct.
Bad: "This task involves updating wireframes for the new flow."
Good: "Updates the HITL validation wireframes to reflect feedback from the March
stakeholder review, ahead of the April engineering handoff."]

## Design Files
[Figma link as labelled Markdown hyperlink: [View in Figma](URL)]
[Multiple files: one per line with a short label]

## Planned Updates
- [ ] [Specific deliverable 1]
- [ ] [Specific deliverable 2]
- [ ] [Specific deliverable 3]
[One checkbox per discrete, verifiable deliverable.
Concrete outcomes not vague activities:
"Deliver final wireframes for the HITL validation flow" not "Work on wireframes"]

## Background & References
[Only include if background was provided — omit section entirely if not]
[Bulleted list: brief label + link or description]
[e.g. "- Related work item: #12345 — HITL Validation Phase 1"]
```

**ADO vocabulary — always use correct terms:**
- Work item (not ticket), User Story (not issue), Acceptance Criteria (not Definition of Done)
- Iteration Path / Sprint, Tags (not labels)

## Output Format
Markdown only — no preamble, no commentary. After the output, add one italicised note:
*Paste into the ADO work item Description field. Verify the Figma link is accessible
to all team members before saving.*

## Dependencies
Feeds into ADO work items that may later be parsed by ux-generate-design-requirements.
