# Contributing to the Claude Skills Library

Thanks for contributing! This guide covers everything you need to add a new skill or improve an existing one.

---

## Adding a New Skill

### 1. Create your skill file

Create a new `.md` file in the appropriate folder under `skills/`:

| Folder | Use for |
|--------|---------|
| `skills/design/` | UI/UX design, Figma, visual tools, frontend |
| `skills/requirements/` | Specs, transcripts, work items, v0 prompts |
| `skills/content/` | Case studies, documents, writing workflows |

Not sure where it fits? Put it in the closest category and note it in your PR.

### 2. Use the standard front-matter

Every skill file must start with this YAML block:

```yaml
---
name: your-skill-name
description: >
  One to three sentences. What does this skill do? When should Claude use it?
  Be specific about triggers — this text is used in the catalog.
version: 1.0.0
updated: YYYY-MM-DD
relevant_roles: [design, product, engineering, strategy]
owner: @your-github-handle
---
```

### 3. Structure your skill content

```markdown
# SKILL: Your Skill Name — Short Subtitle

## Purpose
What problem does this skill solve? Who is it for?

## When to Use
- Bullet list of trigger conditions

## When NOT to Use
- Conditions where this skill doesn't apply

## Instructions
[The actual skill instructions for Claude]

## Output Format
What should Claude produce when this skill is active?

## Dependencies
List any other skills this one relies on
```

### 4. Submit a pull request

- Branch name: `skill/your-skill-name` or `fix/skill-name-issue`
- PR title: `Add: your-skill-name` or `Update: skill-name — what changed`
- Describe what the skill does, who it's for, and how you've tested it

The catalog (`README.md`) will auto-update when your PR is merged. You don't need to edit it manually.

---

## Editing an Existing Skill

1. Edit the skill file directly
2. Bump the `version` in the front-matter
3. Update the `updated` date
4. Submit a PR with a clear description of what changed and why

---

## Skill Quality Standards

- [ ] Front-matter is complete and valid YAML
- [ ] Description is specific enough to be useful in the catalog
- [ ] "When to Use" and "When NOT to Use" sections are both present
- [ ] Skill has been tested in at least one real Claude session
- [ ] No confidential or proprietary content included
