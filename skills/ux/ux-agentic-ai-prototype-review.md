---
name: ux-agentic-ai-prototype-review
description: >
  Reviews and fixes HTML prototype code for agentic AI interfaces, producing
  improved copy-paste ready code and a prioritised change report. Use whenever
  the user shares HTML and wants a review, audit, or improvement pass — especially
  for AI-powered interfaces or pre-demo polish. Triggers on: "review this HTML",
  "fix my prototype", "audit this code", "clean this up before the demo", "check
  this for accessibility", "polish this component".
version: 1.0.0
updated: 2026-04-13
relevant_roles: [design, engineering]
owner: "@MaryCampoTR"
---

# SKILL: UX > Agentic AI — Prototype Review & Fix

## Purpose
Takes HTML prototype code and produces two outputs: improved ready-to-use HTML
with inline comments explaining key fixes, and a prioritised Change Report
(Critical → High → Medium) with a quick-scan format showing issue, fix, and impact.

## When to Use
- User pastes HTML code (full page or components) and wants it reviewed or improved
- AI-powered interface prototypes being prepared for stakeholder demos
- Accessibility audits on prototype code
- Pre-demo polish passes
- Phrases like "review this HTML", "fix my prototype", "audit this code",
  "clean this up before the demo", "check for accessibility", "polish this component"

## When NOT to Use
- Design spec or requirements work (use ux-generate-design-requirements)
- Non-HTML code reviews
- Live production code (this skill is scoped to prototypes)

## Instructions

Apply all four lenses in order. Map findings to severity tiers.

**Lens 1 — Agentic AI UX (Critical / High)**
Primary lens. Check against Human-AI interaction principles:
- Transparency: AI-generated content has a reasoning/source affordance ("Why this?")?
- User control: can the user override, edit, or cancel any AI action before it executes?
- High-stakes gates: approval checkpoints before irreversible AI actions?
- Limit/failure states: does the UI communicate when AI cannot proceed, with a forward path?
- AI provenance labelling: is AI-generated content clearly marked?
- Feedback mechanism: inline feedback control present (thumbs up/down or equivalent)?
- Cognitive load: AI output chunked and progressive — not wall-of-text?
- Data disclosure: user informed what data the AI is using, when relevant?

Critical: AI executes irreversible action without approval; no failure state; AI output unlabelled in high-stakes context
High: no override path; no reasoning affordance on key recommendations; feedback mechanism absent

**Lens 2 — Accessibility WCAG 2.2 AA (Critical / High)**
- Missing alt text on images
- Interactive elements without accessible labels (aria-label, aria-labelledby)
- Dynamic AI output not in an aria-live region
- Colour contrast failures
- Broken keyboard focus order or missing tabindex
- Form inputs without associated label elements
- Error states without role="alert"

Critical: blocks screen reader users; form inputs without labels
High: contrast failures; missing aria-live on AI output; broken focus order

**Lens 3 — UX & Visual Quality (High / Medium)**
- Primary action not visually prominent; hierarchy unclear
- Loading / empty / error states missing
- Inconsistent spacing or broken typography hierarchy
- Missing interaction feedback (hover, active, disabled states)
- AI in-progress state absent during AI operations
- Broken or absent responsive breakpoints

High: missing loading/error/empty states that would break the demo
Medium: visual inconsistencies, spacing issues, missing hover states

**Lens 4 — Code Quality (Medium)**
- Inline styles that should be classes
- Duplicate or redundant CSS
- Non-semantic HTML (div where button or nav is correct)
- Hardcoded values that should be tokens/variables
- Dead commented-out code

Medium unless causing a functional bug — then High.

## Output Format

**Section 1 — Improved HTML**
Full corrected HTML with:
- All issues fixed
- Inline comments on every significant change: `<!-- FIX: [brief reason] -->`
- `<!-- PRESERVED: [what was left as-is and why] -->` block at top if relevant
- Surgical fixes only — do not rewrite working sections

**Section 2 — Change Report**
```
## Change Report

### ✅ Working Well
[What was intentionally preserved]

### 🔴 Critical
| Issue | Fix applied | Impact |

### 🟠 High
| Issue | Fix applied | Impact |

### 🟡 Medium
| Issue | Fix applied | Impact |

### ⚡ Quick Wins
[2–3 highest-leverage changes for partial-fix situations]

### ⚠️ Breaking Changes
[Anything that changes behaviour — flag before deploying]
```

If the HTML is a fragment, note: *"Reviewed as a component fragment — page-level
accessibility and structure not assessed."*
Omit severity tiers with no findings.

## Dependencies
Complements ux-generate-design-requirements. References agentic-ai-ux principles
(if installed) for the AI UX lens.
