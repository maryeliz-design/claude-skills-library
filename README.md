# Claude Skills Library

A personal library of Claude skill files. Browse the catalog below to find skills, or contribute your own via pull request.

> **What is a skill?** A skill is a `.md` file you load into a Claude project to give it specialised behaviour — like a plugin. Each skill has a clear purpose, trigger conditions, and instructions for Claude to follow.

---

## 📖 Skills Catalog

<!-- CATALOG_START -->
### 🎨 Design

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [agentic-ai-ux](./skills/design/agentic-ai-ux.md) | Apply Human-AI agent interaction UX principles to any feature spec or v0 prompt that involves AI-generated content, AI recommendations, automated actions, or agentic AI experiences. Use when the feature being designed includes any AI agent behaviour — surfacing recommendations, taking actions on behalf of users, generating content, or operating autonomously. Covers transparency, user control, boundaries, cognitive modularity, error recovery, feedback loops, privacy, and accessibility for AI interactions. Based on Human-AI Agent Interaction UX design principles. |  | — |
| [figma-ingestion](./skills/design/figma-ingestion.md) | Extract accurate component specifications from Figma screenshots (no MCP, no Dev Mode required). Use whenever the user shares a Figma screenshot, export, or any UI image and needs it interpreted into design system component specs before writing requirements or a v0 prompt. Produces a structured Component Ingestion Report that feeds directly into the ux-requirements-synthesizer skill. |  | — |
| [frontend-design](./skills/design/frontend-design.md) | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics. |  | — |
| [ui-designer](./skills/design/ui-designer.md) | Expert visual design craft, UI systems, and pixel-perfect implementation. Activates when building, styling, reviewing, or polishing any interface -- websites, apps, dashboards, component libraries, design systems, landing pages, or any screen needing visual polish. Triggers on: CSS styling, component design, layout, spacing, typography, color, dark mode, responsive design, design tokens, Figma, UI audits, visual hierarchy, icons, shadows, border-radius, animations. Also activates on: 'make it look good', 'improve the design', 'it looks off', 'spacing', 'colors', 'typography', 'design system', 'component library', 'pixel perfect', 'modern design', 'layout', 'responsive', 'dark mode', 'style this'. Applies whenever a visual interface is created or refined, even without saying 'UI'. Hands off to ux-designer for flow strategy and to ux-copywriter for interface text. Do NOT activate for user research methodology, psychology theory, backend logic, database schemas, API design without UI, or DevOps. |  | — |
| [ux-designer](./skills/design/ux-designer.md) | Expert UX design thinking, user psychology, and experience strategy. Activates when building, reviewing, or discussing any user-facing interface -- websites, apps, dashboards, forms, onboarding, checkout, sign-up, settings, landing pages, modals, navigation. Triggers on: user flows, wireframes, prototypes, usability, information architecture, content strategy, error handling, accessibility, interaction design, user testing, conversion. Also activates on: 'how should this flow', 'user experience', 'make it easier', 'onboarding', 'conversion', 'drop-off', 'friction', 'confusing', 'intuitive', 'usability', 'user journey'. Applies whenever a human uses an interface, even without saying 'UX'. Hands off to ux-copywriter for detailed microcopy work and to ui-designer for visual styling. Do NOT activate for purely visual styling, backend logic, database schemas, API design without UI, or DevOps. |  | — |

### 📋 Requirements

| Skill | Description | Relevant Roles | Owner |
|-------|-------------|---------------|-------|
| [session-kickoff](./skills/requirements/session-kickoff.md) | Automatically orchestrates a full UX requirements session. Load this skill whenever a user provides any combination of feature context, meeting transcripts, work items, Figma screenshots, or brief descriptions of what they need to build. No session starter prompt needed — this skill reads the inputs, loads the right sub-skills in the correct order, and drives the session from intake to a completed spec, v0 prompt, and QA report. |  | — |
| [spec-qa](./skills/requirements/spec-qa.md) | Final quality gate for any UX requirements spec before it is handed off to v0, a stakeholder, or a development team. Run after ux-requirements-synthesizer, ux-design-principles, and agentic-ai-ux have been applied. Produces a binary READY / NOT READY verdict with a clear list of blockers and a confidence score. Use before any spec leaves your hands. |  | — |
| [transcript-parser](./skills/requirements/transcript-parser.md) | Parse and structure messy meeting transcripts into clean, synthesizer-ready intent signals. Use whenever the user provides a meeting transcript, call notes, or Slack thread as input to a requirements task. Extracts decisions, open questions, user pain points, implied features, and out-of-scope markers. Output feeds directly into the ux-requirements-synthesizer skill. |  | — |
| [user-context](./skills/requirements/user-context.md) | Capture and apply user context (persona, role, domain, sophistication level, task environment) before synthesizing requirements. Use at the start of any session where the product context, user type, or domain is not already established. Feeds persona signals directly into tone, density, progressive disclosure, copy register, and component decisions in the ux-requirements-synthesizer. Especially important when working across multiple products or user types. |  | — |
| [ux-design-principles](./skills/requirements/ux-design-principles.md) | Apply Staff Product Designer thinking to any UX requirements spec or v0 prompt. Use on every feature spec to ensure outputs reflect senior design judgment — not just functional requirements. Covers interaction patterns, visual hierarchy, cognitive load, form design, empty/error/loading states, progressive disclosure, accessibility (WCAG 2.2 AA), and design-system-specific design decisions. Runs as a design critique layer on top of the ux-requirements-synthesizer output before the v0 prompt is written. |  | — |
| [ux-requirements-synthesizer](./skills/requirements/ux-requirements-synthesizer.md) | Transform piecemeal UX inputs (meeting transcripts, half-baked user stories, design artifacts) into complete, v0-ready requirement specs. Use when given any raw product/UX input and asked to produce a structured spec, prototype brief, or v0 prompt. Includes a full output schema, v0 prompt template, ambiguity resolution rules, and a pre-delivery checklist. |  | — |
| [v0-prompt-patterns](./skills/requirements/v0-prompt-patterns.md) | A pattern library of proven v0 prompt structures for common screen archetypes. Use when writing the v0 prompt section of a requirements spec, or when asked to produce a v0 prompt directly. Covers: form page, data table, dashboard, detail panel, empty/error states, modal flows, and navigation shells. Compose from patterns rather than writing from scratch every time. |  | — |
| [v0-refinement](./skills/requirements/v0-refinement.md) | Diagnose v0 prototype output that missed the mark and produce targeted refinement prompts. Use when v0 has generated a prototype that is incomplete, inaccurate, or mishandled complex interactions — and you need to fix it without starting over. Covers: gap diagnosis, root cause identification, surgical follow-up prompt writing, multi-screen flow composition, and complex interaction patterns v0 commonly mishandles. |  | — |

<!-- CATALOG_END -->

---

## 🚀 How to Use a Skill

1. Navigate to the skill file you want
2. Click **Raw** and copy the full content
3. In your Claude project, go to **Project Instructions** and paste the skill content
4. That's it — Claude will now follow the skill's instructions in that project

---

## 🤝 Contributing

Want to add a skill or improve an existing one? See [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## 📁 Folder Structure

```
claude-skills-library/
├── README.md              ← You are here (catalog)
├── CONTRIBUTING.md        ← How to add/edit skills
├── skills/
│   ├── design/            ← UI/UX, Figma, frontend
│   ├── requirements/      ← Specs, transcripts, v0 prompts
│   └── content/           ← Case studies, documents, writing
└── scripts/
    └── generate_catalog.py ← Auto-updates this catalog from skill front-matter
```
