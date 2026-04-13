---
name: user-context
description: >
  Capture and apply user context (persona, role, domain, sophistication
  level, task environment) before synthesizing requirements. Use at the
  start of any session where the product context, user type, or domain
  is not already established. Feeds persona signals directly into tone,
  density, progressive disclosure, copy register, and component decisions
  in the ux-requirements-synthesizer. Especially important when working
  across multiple products or user types.
version: 1.0.0
updated: 2026-03-27
---

# SKILL: User Context — Persona & Domain Layer

## Purpose
Ensure every spec is grounded in a specific user — their role, mental
model, sophistication level, and task environment. Without this layer,
component and copy decisions default to generic, which produces prototypes
that are technically correct but wrong for the audience.

Run this skill at the start of a session when the user context is not
already established, or when switching between product contexts.

---

## Phase 1 — Context Extraction

### Step 1: Extract user signals from available inputs

Scan all inputs (transcript, ADO work items, Figma, notes) for signals
about the user. Look for:

**Role signals:**
- Job title or function mentioned ("lawyer", "tax professional",
  "accountant", "paralegal", "compliance officer", "researcher")
- Task descriptions that imply a role ("reviewing contracts",
  "filing returns", "running searches")
- Product name or domain (legal = high-stakes, precise language;
  tax/accounting = compliance-driven, numerical)

**Sophistication signals:**
- Are technical terms used without explanation? (higher sophistication)
- Are workflow steps described in detail? (may indicate lower familiarity
  with the product)
- Is the feature for power users or general users?
- Is onboarding or guidance mentioned? (implies lower sophistication)

**Task environment signals:**
- Time pressure mentioned? (implies need for efficiency, compact density,
  minimal steps)
- High-stakes decisions? (implies need for confirmation patterns,
  audit trails, conservative defaults)
- Collaborative or solo? (implies sharing, commenting, or handoff patterns)
- Regulatory/compliance context? (implies audit trails, explicit approvals,
  conservative language)

**Device/context signals:**
- Desktop-first vs mobile consideration
- Internal tool vs client-facing
- Standalone product vs embedded in a workflow

---

## Phase 2 — User Context Profile

### Step 2: Produce a User Context Profile

If enough signals are present, produce the profile directly.
If signals are ambiguous or missing, ask the user to confirm before
proceeding — do not invent a persona.

```
## User Context Profile

### Primary User
Role: [job title / function]
Domain: [legal | tax | accounting | compliance | research | other]
Product context: [product name / area if known]

### Sophistication Level
Technical: [novice | intermediate | expert]
Product familiarity: [new user | regular user | power user]
Rationale: [what signals from inputs led to this assessment]

### Task Characteristics
Frequency: [daily | weekly | occasional | one-time]
Time pressure: [high — speed matters | low — accuracy matters | mixed]
Stakes: [high — errors have serious consequences | medium | low]
Regulatory context: [yes — compliance/audit requirements | no]
Collaboration: [solo | collaborative — shared with others]

### Device & Environment
Primary device: [desktop | mobile | both]
Interface type: [internal tool | client-facing product]
Workflow position: [standalone task | embedded in larger workflow]

### Design Implications
[Derived automatically from the profile — see Phase 3]
```

---

## Phase 3 — Design Implications

### Step 3: Translate profile into spec decisions

Apply these mappings based on the User Context Profile. Each implication
feeds directly into the ux-requirements-synthesizer spec.

---

#### Sophistication → Copy Register

| Sophistication | Copy register | Examples |
|---|---|---|
| Expert / power user | Precise, minimal explanation, domain vocabulary acceptable | "Set jurisdiction", "Apply filter", "Export to LEDES" |
| Intermediate | Clear labels, light guidance where needed | "Select jurisdiction", "Filter results", "Export file" |
| Novice / new user | Plain language, explain implications, avoid jargon | "Choose your country or region", "Show only matching results", "Save as a file" |

**Spec annotation:**
```
[USER-CONTEXT] Copy register: [expert | intermediate | novice]
→ [specific copy recommendation]
```

---

#### Stakes → Confirmation & Feedback Patterns

| Stakes level | Pattern implications |
|---|---|
| High | Explicit confirmation dialogs for all irreversible actions. Audit trail required. Success confirmation must be persistent (not auto-dismiss). Error messages highly specific. |
| Medium | Confirmation for destructive actions only. Standard success/error feedback. |
| Low | No confirmation for reversible actions. Toast/auto-dismiss feedback acceptable. |

**Spec annotation:**
```
[USER-CONTEXT] Stakes level: [high | medium | low]
→ Confirmation pattern: [required for all irreversible | destructive only | not required]
→ Success feedback: [persistent | auto-dismiss after 5s]
→ Error specificity: [highly specific with recovery steps | standard]
```

---

#### Time Pressure → Density & Efficiency

| Time pressure | Design implications |
|---|---|
| High | Compact density preferred. Minimal clicks to primary action. Keyboard shortcuts considered. No unnecessary confirmation steps for low-stakes actions. Progressive disclosure over upfront information. |
| Low | Standard density. Can afford more guidance, help text, contextual explanation. |
| Mixed | Standard density with compact option available. Power user shortcuts alongside guided flows. |

**Spec annotation:**
```
[USER-CONTEXT] Time pressure: [high | low | mixed]
→ Default density: [compact | standard]
→ Primary action reachable in: [n] steps
```

---

#### Regulatory Context → Audit & Compliance Patterns

If regulatory context is YES, add to every relevant screen:

- Explicit approval gates before consequential actions
- Timestamp + user attribution on all state changes
- Audit trail accessible from relevant records
- No auto-execute on AI suggestions — always requires human approval
- Confirmation dialogs include what will be logged

**Spec annotation:**
```
[USER-CONTEXT] Regulatory context: yes
→ Audit trail required on: [list of actions]
→ Approval gate required before: [list of consequential actions]
```

---

#### Domain → Vocabulary & Mental Model

| Domain | Key vocabulary signals | Mental model |
|---|---|---|
| Legal | Matter, document, jurisdiction, filing, precedent, counsel | Document-centric, risk-aware, precedent-driven |
| Tax | Return, filing, jurisdiction, period, assessment, entity | Form-centric, deadline-driven, accuracy-critical |
| Accounting | Account, period, entity, ledger, reconciliation, audit | Numbers-centric, period-driven, audit-aware |
| Compliance | Policy, obligation, control, risk, evidence, framework | Risk-centric, evidence-driven, process-oriented |
| Research | Source, citation, query, result, relevance, analysis | Search-centric, citation-aware, exploratory |

Apply domain vocabulary consistently in:
- Field labels (use domain terms, not generic terms)
- Empty state copy ("No matters found" not "No items found")
- Button labels ("File document" not "Submit")
- Error messages ("Filing failed" not "Action failed")

**Spec annotation:**
```
[USER-CONTEXT] Domain: [legal | tax | accounting | compliance | research]
→ Domain vocabulary applied: [list key terms used in spec]
```

---

#### Collaboration → Sharing & Handoff Patterns

| Collaboration type | Design implications |
|---|---|
| Solo | No sharing controls needed. Personal preferences and history matter. |
| Collaborative | Sharing controls, permission levels, activity/audit visibility. Handoff states (assigned to, reviewed by). Comments or annotations if applicable. |

---

## Phase 4 — Context Persistence

### Step 4: Carry context through the session

Once a User Context Profile is established, it applies to every screen
and decision in the session. Annotate the synthesizer spec with:

```
[USER-CONTEXT ACTIVE]
Role: [role] | Domain: [domain] | Sophistication: [level]
Stakes: [level] | Time pressure: [level] | Regulatory: [yes/no]
→ All design decisions in this spec reflect this context.
```

If a spec covers multiple user types (e.g. an admin screen and a
professional screen in the same feature), create a separate profile
for each user type and annotate which screens each profile applies to.

---

## Rules

1. **Never invent a persona** without signals from inputs — ask if unclear
2. **One profile per user type** — don't blend two different users into one
3. **Domain vocabulary takes precedence** over generic UI copy — always
4. **Sophistication affects copy, not functionality** — don't remove
   features for novice users; add guidance instead
5. **High stakes always means explicit confirmation** — never optimise
   away a confirmation gate for efficiency in a high-stakes context
6. **Regulatory context is binary** — if any regulatory context exists,
   all compliance patterns apply; don't apply them selectively
