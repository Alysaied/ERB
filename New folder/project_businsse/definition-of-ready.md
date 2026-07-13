# Definition of Ready (DoR): Inventory Management System

**Document Owner:** Product Owner  
**Purpose:** Define the minimum conditions a user story must meet before it enters a sprint or development queue  
**Audience:** Product Owner, Scrum Master, business analysts, development team, QA  
**Based On:** BRD-IMS-001, Product Epics (EPIC-IMS-001), User Stories (US-001 – US-090), Acceptance Criteria (AC-REV-IMS-001), MoSCoW Prioritization  
**Applies To:** All user stories, spikes, and enablers scheduled for delivery

---

## How to Use This Checklist

1. **When:** Complete the DoR checklist during backlog refinement, before sprint planning.
2. **Who:** Product Owner confirms business readiness; team confirms delivery readiness; QA confirms test readiness.
3. **Rule:** A story is **Ready** only when **all applicable** checklist items are checked. Items marked *(N/A)* must include a brief justification.
4. **Blocked stories:** If any item fails, the story stays in the backlog with documented blockers and an owner.

**Sign-off roles**

| Role | Confirms |
|------|----------|
| **Product Owner** | Business value, scope, priority, dependencies, open questions |
| **Delivery Lead / Tech Lead** | Size, technical feasibility, non-functional impacts |
| **QA Lead** | Test scenarios, acceptance criteria testability |
| **Business SME** *(when required)* | Policy values, workflow rules, integration assumptions |

---

## Definition of Ready — Master Checklist

### 1. Story Identity & Traceability

| # | Criterion | ☐ | Notes / Reference |
|---|-----------|:-:|-------------------|
| 1.1 | Story has a unique ID (e.g., US-xxx) and descriptive title | | |
| 1.2 | Story is mapped to a parent **Epic** (EPIC-01 – EPIC-12) | | |
| 1.3 | Story traces to an approved **Functional Requirement** (FR-xxx) | | |
| 1.4 | Story traces to at least one **Business Objective** (BO-xx) or documented pain point (PP-xx) | | |
| 1.5 | Delivery **phase** is confirmed (MVP / Phase 2 / Phase 3) and aligned with MoSCoW priority | | |

---

### 2. Business Value Defined

| # | Criterion | ☐ | Notes / Reference |
|---|-----------|:-:|-------------------|
| 2.1 | User story is written in standard format: **As a** \<role\>, **I want** \<goal\>, **so that** \<business value\> | | |
| 2.2 | **Business value** is explicit and tied to a measurable outcome (e.g., reduce stockouts, improve accuracy, shorten approval time) | | |
| 2.3 | **Primary user role** is identified and exists in the role catalog (UR-xx) or documented interim role (e.g., IMS Administrator) | | |
| 2.4 | Story priority is agreed (Must / Should / Could / Won't for current release) | | |
| 2.5 | Product Owner has confirmed the story is **in scope** per BRD-IMS-001 and not deferred | | |

---

### 3. Acceptance Criteria Complete

| # | Criterion | ☐ | Notes / Reference |
|---|-----------|:-:|-------------------|
| 3.1 | Acceptance criteria exist and use **Given / When / Then** format | | |
| 3.2 | **Happy path** scenarios are defined (minimum 2 per story) | | |
| 3.3 | **Validation rules** are defined — required fields, business rules, authorization checks (minimum 2) | | |
| 3.4 | **Error scenarios** are defined — unauthorized access, invalid input, blocked actions (minimum 2) | | |
| 3.5 | **Edge cases** are defined — boundary conditions, exceptions, unusual valid situations (minimum 2) | | |
| 3.6 | Criteria describe **observable business outcomes**, not implementation or UI design | | |
| 3.7 | Criteria IDs are assigned (AC-xxx-H/V/E/Xn) and linked to the user story | | |

---

### 4. Dependencies Identified

| # | Criterion | ☐ | Notes / Reference |
|---|-----------|:-:|-------------------|
| 4.1 | **Functional dependencies** on other user stories are listed (e.g., US-024 depends on US-023) | | |
| 4.2 | **Epic-level dependencies** are understood (e.g., EPIC-11 access control required before operational stories) | | |
| 4.3 | **Master data prerequisites** are identified (product, location, reason codes, thresholds, policies) | | |
| 4.4 | **Integration dependencies** are documented (order source system, finance export, notification channels) | | |
| 4.5 | **Policy/configuration dependencies** are identified (approval thresholds, ATP rules, tolerance limits, routing rules) | | |
| 4.6 | Dependent stories are **done or scheduled earlier** in the same or prior sprint, OR a documented stub/mock approach is agreed for incremental delivery | | |
| 4.7 | External team dependencies (IT, Finance, Purchasing, Marketing) have named contacts and expected response dates | | |

---

### 5. Story Size Understood

| # | Criterion | ☐ | Notes / Reference |
|---|-----------|:-:|-------------------|
| 5.1 | Story has been **estimated** by the delivery team (story points or t-shirt size) | | |
| 5.2 | Story is small enough to complete within **one sprint**; if not, it has been split into smaller stories | | |
| 5.3 | Team agrees the story is **INVEST**-aligned (Independent, Negotiable, Valuable, Estimable, Small, Testable) | | |
| 5.4 | Non-functional requirements (performance, availability, security) impacting the story are noted and sized | | |
| 5.5 | For large or ambiguous stories, a **spike** or discovery task is completed before committing to delivery | | |

**Sizing guidance for this project**

| Size | Guidance |
|------|----------|
| **S (1–3 pts)** | Single role, single workflow step, no integration, ≤8 acceptance criteria |
| **M (5 pts)** | Multiple validation rules, approval routing, or 1–2 story dependencies |
| **L (8 pts)** | Cross-role workflow, multiple dependencies, or policy engine behavior |
| **Too large** | Split if >8 points, >3 dependencies, or spans multiple business processes (BP-xx) |

---

### 6. Questions Resolved

| # | Criterion | ☐ | Notes / Reference |
|---|-----------|:-:|-------------------|
| 6.1 | All **open clarification questions** for the story are resolved or explicitly deferred with Product Owner approval | | |
| 6.2 | **Business policy gaps** are closed (e.g., approval thresholds, ATP definition, ad-hoc receipt rules, backorder priority) | | |
| 6.3 | **Assumptions** are documented where the BRD or FR leaves ambiguity (integration boundaries, interim manual processes) | | |
| 6.4 | Conflicts between BRD, MoSCoW, and phase tags are **reconciled** for this story | | |
| 6.5 | Stakeholder sign-off obtained for stories affecting **finance, audit, or segregation of duties** controls | | |
| 6.6 | No unresolved **blockers** remain on the story record or sprint board | | |

**Reference:** BRD Requirements Errata (ISS-001 – ISS-048) and domain clarification questions (Q-01 – Q-25) must be checked for story impact.

---

### 7. Test Scenarios Identified

| # | Criterion | ☐ | Notes / Reference |
|---|-----------|:-:|-------------------|
| 7.1 | QA has mapped acceptance criteria to **test scenarios** (minimum one test scenario per AC criterion) | | |
| 7.2 | **Happy path test data** requirements are identified (products, locations, users, roles, stock balances) | | |
| 7.3 | **Negative test scenarios** are identified for validation and error AC categories | | |
| 7.4 | **Role-based access tests** are defined for stories with authorization or location-scope rules | | |
| 7.5 | **End-to-end test path** is identified where the story participates in a golden path (e.g., receive → put-away → ATP → reserve → pick) | | |
| 7.6 | UAT participants and **business sign-off criteria** are identified for MVP Must Have stories | | |
| 7.7 | Regression scope is noted for stories that change shared capabilities (ATP, movement history, audit trail) | | |

---

### 8. Delivery & Operational Readiness

| # | Criterion | ☐ | Notes / Reference |
|---|-----------|:-:|-------------------|
| 8.1 | **UI/UX** expectations are agreed at business level (fields, statuses, messages) without prescribing technical design | | |
| 8.2 | **Notification routing** is defined for alert/approval stories (recipients, channels, escalation) | | |
| 8.3 | **Change management** impact is understood (training, SOP updates, adoption enforcement) for operational stories | | |
| 8.4 | **Go-live / rollout** location scope is confirmed for location-specific stories | | |
| 8.5 | Story includes or links to **demo script** steps for sprint review | | |

---

## Quick-Reference DoR Checklist (Sprint Planning Card)

Copy and complete per story:

```
Story ID: __________   Epic: __________   Sprint: __________   PO: __________

☐ Business value defined and linked to BO/PP
☐ User story format complete (As / I want / So that)
☐ Role identified and valid (UR-xx)
☐ Acceptance criteria complete (Happy / Validation / Error / Edge)
☐ All AC use Given / When / Then
☐ Dependencies identified and scheduled
☐ Story sized and ≤ 1 sprint
☐ Open questions resolved or deferred with approval
☐ Test scenarios identified and mapped to AC
☐ NFR impacts noted (if any)
☐ Stakeholder sign-off (if control/finance story)

READY FOR DEVELOPMENT:  ☐ Yes   ☐ No — Blocker: _______________________
```

---

## Definition of Ready — Epic-Level Gate (First Story in Epic)

Before the **first story** of an epic enters development, confirm these additional items:

| # | Epic Gate Criterion | ☐ |
|---|---------------------|:-:|
| E.1 | Epic business goal and success measures are agreed | |
| E.2 | Foundational enabler stories are Ready (typically EPIC-01 Master Data and EPIC-11 Security for MVP) | |
| E.3 | Cross-epic dependency map reviewed with delivery team | |
| E.4 | MVP cut line for the epic confirmed against MoSCoW | |
| E.5 | Business SMEs assigned for epic duration | |

---

## Common Reasons a Story Fails DoR (This Project)

Use this list during refinement to accelerate resolution:

| Blocker | Typical resolution |
|---------|-------------------|
| ATP calculation undefined | Publish ATP definition appendix; link to US-024 |
| Approval thresholds not set | COO/CFO policy sign-off; interim defaults documented |
| Order integration boundary unclear | Document minimum order data contract before US-041+ |
| Notification recipients undefined | Define routing table before US-076+ |
| Story depends on Phase 2 FR in MVP sprint | Descope, split story, or document manual workaround |
| IMS Administrator role not formalized | Confirm UR-20 or interim governance owner |
| Story > 8 points | Split by workflow step, role, or happy path vs. exceptions |

---

## Relationship to Definition of Done (DoD)

| DoR (this document) | DoD (separate artifact) |
|---------------------|-------------------------|
| Conditions to **start** work | Conditions to **complete** work |
| Confirms clarity, value, testability | Confirms code, tests, documentation, deployment |
| Validated at backlog refinement | Validated at sprint review / release |

A story that passes DoR but fails DoD is **not done**. A story that fails DoR should **not** enter the sprint.

---

## Document Control

| Attribute | Detail |
|-----------|--------|
| **Document ID** | DOR-IMS-001 |
| **Version** | 1.0 |
| **Created** | July 5, 2026 |
| **Author** | Product Owner |
| **Related Artifacts** | BRD-IMS-001, EPIC-IMS-001, US-REV-IMS-001, AC-REV-IMS-001, MoSCoW Prioritization, RTM-IMS-001 |
| **Review Cadence** | Revisit at phase boundaries (MVP → Phase 2 → Phase 3) |

---

*End of Definition of Ready Document*
