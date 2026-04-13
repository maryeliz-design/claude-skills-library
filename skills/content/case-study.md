---
name: case-study
description: >
  Use this skill whenever a user wants to create a UX or design case study
  document. Triggers include: mentions of 'case study', 'design case study',
  'UX case study', 'portfolio case study', requests to document a design
  initiative, project outcome, or design process for stakeholders or
  leadership review. Also trigger when a user mentions sections like 'the
  challenge', 'the solution', 'the outcome', 'design impact', or wants to
  write up a project for a portfolio or management review.
version: 2.0.0
updated: 2026-04-13
---

# Case Study Document Skill

Produces a polished, stakeholder-ready Word (.docx) case study document by
interviewing the user section by section, then generating a clean,
professionally formatted document using the docx skill.

---

## Workflow

### Step 1: Introduce and Begin the Interview

Greet the user and explain you'll ask questions across 6 sections to build
their case study. Tell them they can skip any section — you'll insert a
placeholder so they can fill it in later. Also let them know they're welcome
to **upload any existing documentation** (e.g. project briefs, research
reports, design specs, retrospectives, or slide decks) — you'll pull relevant
information from those files and use them to pre-fill answers, reducing how
much they need to type.

Then proceed section by section. **Ask one section at a time.**

If the user uploads documents, read them before starting the interview. For
each section, use what you find to propose a draft answer, then ask the user
to confirm, correct, or add to it rather than asking from scratch.

---

### Step 2: Section-by-Section Interview

Work through each section below in order. After the user responds, summarize
what you've captured and confirm before moving on. If a user skips a section,
note it and move on — you'll insert a placeholder in the doc.

---

#### Section 3.1 — The Challenge

Goal: A concise problem statement written for executive readers.

Ask the user:
- Who is the affected group? (e.g. customers, internal users, a specific segment)
- What problem did they face, and in what context or situation?
- What was the negative impact? (quantitative metrics preferred)
- What was the desired outcome of solving this?
- Any supporting evidence? (user feedback, analytics, stakeholder observations)

**Formula to apply when writing this section:**
> [Affected group] faces [problem] when [context/situation], which results in [negative impact]. We need to [desired outcome] that addresses the issue faced by the user.

If metrics aren't available, use qualitative evidence and note it clearly.

---

#### Section 3.2 — The Solution

Goal: A short description of the work done, followed by 3–5 bullet points.

Ask the user:
- How long was the design process, and what was its goal?
- What were the key steps or design methods used?
- Has this initiative launched yet, or is it still in progress?

**If launched:** Focus on concrete design actions and changes made.
**If in progress:** Focus on research, validation, stakeholder alignment, and artifacts delivered.

Write as: One sentence summary + 3–5 bullet points of key actions.

---

#### Section 3.3 — The Outcome

Goal: Measurable impact framed as increases in value or decreases in pain.

Ask the user:
- Has the initiative launched?
- What metrics improved? (activation rate, task completion, support tickets, etc.)
- Over what timeframe were these measured?
- If not launched: any leading indicators? (usability test results, prototype validation)

**If launched:** Present as: "In the [timeframe] post-launch, the [initiative]:" + 3–5 bullet points.
**If in progress:** Document validation metrics, usability test results, and milestones achieved.
**If no metrics:** Note this clearly with placeholder, suggest proxy metrics or qualitative indicators.

---

#### Section 3.4 — Visual Assets

Goal: List the visual artifacts that should accompany this case study.

Ask the user:
- What visual assets exist? (hi-fi designs, wireframes, UX flows, journey maps)
- Are there research artifacts that were key to the solution?
- Can they describe or name the visuals so placeholders can be inserted?

**Note:** This skill inserts clearly labeled image placeholders in the document.
The user will need to manually insert actual images after downloading the .docx file.

---

#### Section 3.5 — Customer or User Quotes

Goal: 2–3 verbatim (or lightly edited) quotes from customers or end users.

Ask the user:
- Do they have any customer, user, or stakeholder quotes?
- If yes, collect the quotes and who said them (role/segment is fine).
- Remind them: quotes should be short, punchy, and authentic.

If no quotes are available, insert a placeholder.

---

#### Section 3.6 — The Team

Goal: Credit everyone who contributed.

Ask the user:
- Who led the design work?
- Who were the design teammates?
- Were there cross-functional partners? (Product, Engineering, Research, etc.)

---

### Step 3: Review & Confirm

Once all sections are collected, present a brief structured summary.
Ask: "Does this look right? Anything you'd like to change before I create the document?"

Wait for confirmation before generating.

---

### Step 4: Generate the Word Document

Use the `docx` skill to produce the document. Follow all docx skill rules strictly.

#### Document Structure

```
Cover / Title Area
  - Case Study title (from project name)
  - Subtitle: "Design Case Study"
  - Date (use today's date)

The Challenge
The Solution
The Outcome
Visual Assets
Customer & User Quotes
The Team
```

#### Formatting Rules

**Page setup:**
- Size: A4
- Margins: standard (approx 1 inch all sides)

**Color palette:**
- Title: `000000` black (bold)
- Section headings: `000000` black, NOT bold
- Body text: `000000` black
- Bullet markers: accent color (use a brand color if the user has one, otherwise `444444`)
- Placeholder text: `AAAAAA` italic
- Footer text: `888888` grey

**Title block:**
- Eyebrow: "DESIGN CASE STUDY" — 9pt, all-caps, spaced
- Title: 36pt, black, bold
- Subtitle: "Design Case Study" — 14pt, `444444`
- Date: 11pt, black

**Section headings:**
- 20pt, black, NOT bold
- Spacing: before=240, after=0

**Body text:**
- 10pt, black
- Spacing: before=40, after=120

**Bullet points:**
- 10pt, black
- Indent: standard list indent

**Quotes:**
- 10pt, italic, left indent
- Attribution: 9pt, `555555`

**Image placeholders:**
- Single-cell table with light border and background
- Centered placeholder text: 9pt, `AAAAAA`, italic
- Caption below: 8pt, `888888`, italic

**Page footer:**
- Left: "© [Year] [Author/Organisation]"
- Right: optional logo (ask user if they have one to include)

**Team table:**
- 2-column: Name | Role
- Header row: dark background, white bold text
- Body rows: white, no alternating color
- One row per person

#### docx-js Implementation Notes

- Always install: `npm install -g docx`
- Never use `\n` — use separate Paragraph elements
- Never use `WidthType.PERCENTAGE` in tables — always DXA
- Tables need dual widths: `columnWidths` array AND per-cell `width`
- Use `ShadingType.CLEAR` for all shading, never `SOLID`
- PageBreak must live inside a Paragraph element

---

### Step 5: Deliver

Save the file to `/mnt/user-data/outputs/case-study.docx` and present it to the user.

Tell the user:
- Where to manually insert images (Section 3.4 placeholders)
- Which sections have placeholders they should fill in
- That they can ask you to update any section and regenerate
