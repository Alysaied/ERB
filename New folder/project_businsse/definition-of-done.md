# Definition of Done (DoD): Inventory Management System

**Document Owner:** Product Owner  
**Purpose:** Define the minimum conditions a user story must meet before it is considered complete and potentially shippable  
**Audience:** Product Owner, Scrum Master, development team, QA, release management, business stakeholders  
**Based On:** BRD-IMS-001, Definition of Ready (DOR-IMS-001), Acceptance Criteria (AC-REV-IMS-001), Non-Functional Requirements (NFR-IMS-001), Project Scope & MVP boundaries  
**Applies To:** All user stories, bugs, and enablers delivered in a sprint or release increment

---

## How to Use This Checklist

1. **When:** Complete the DoD checklist before marking a story **Done** on the sprint board and before including it in a release candidate.
2. **Who:** The delivery team completes technical items; QA confirms testing; Product Owner grants final business acceptance.
3. **Rule:** A story is **Done** only when **all applicable** checklist items are checked. Items marked *(N/A)* require a brief justification in the story record.
4. **Partial completion:** Work that does not meet DoD returns to **In Progress** or is split; it is not counted toward sprint velocity as complete.

**Sign-off roles**

| Role | Confirms |
|------|----------|
| **Developer** | Implementation, unit tests, code review participation |
| **Tech Lead** | Code review approval, architecture/NFR compliance |
| **QA Engineer** | Test execution, AC verification, regression |
| **Product Owner** | Business acceptance, demo approval, scope confirmation |
| **Security / Compliance** *(when required)* | Security checks for access, audit, and SoD stories |

---

## Definition of Done — Master Checklist

### 1. Acceptance Criteria Satisfied

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 1.1 | All **Given / When / Then** acceptance criteria for the story are implemented | | AC-xxx IDs: |
| 1.2 | **Happy path** criteria verified and passing | | |
| 1.3 | **Validation rules** criteria verified and passing | | |
| 1.4 | **Error scenarios** criteria verified and passing | | |
| 1.5 | **Edge cases** criteria verified and passing | | |
| 1.6 | QA has executed test cases mapped to each AC criterion with **pass results** recorded | | Test run ID: |
| 1.7 | No open **defects** at severity High or Critical against the story | | |
| 1.8 | Medium/Low defects deferred only with Product Owner approval and documented workaround | | |

---

### 2. Code Reviewed

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 2.1 | Code changes submitted via pull request (or equivalent) linked to the story | | PR #: |
| 2.2 | **Peer code review** completed by at least one qualified reviewer (not sole author) | | Reviewer: |
| 2.3 | All review comments **resolved** or explicitly deferred with Tech Lead approval | | |
| 2.4 | Code follows project **coding standards** and naming conventions | | |
| 2.5 | No unresolved **static analysis** or linter warnings introduced by the change | | |
| 2.6 | Business logic aligns with **FR-xxx** functional requirement and approved story text | | |

---

### 3. Unit Tests Passed

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 3.1 | **Unit tests** written for new or changed business logic | | |
| 3.2 | Unit tests cover happy path and key validation/error branches | | |
| 3.3 | All unit tests **pass** in the CI pipeline for the branch | | Build #: |
| 3.4 | Code coverage meets team threshold for changed modules *(project default: ≥80% on new code)* | | Coverage: |
| 3.5 | No unit tests disabled or skipped without Tech Lead approval and story comment | | |

---

### 4. Integration Tests Passed

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 4.1 | **Integration tests** executed for workflows crossing modules, services, or data stores | | |
| 4.2 | Integration tests cover story **dependencies** (e.g., reservation → ATP update, receipt → movement history) | | |
| 4.3 | All integration tests **pass** in the CI/CD pipeline | | Build #: |
| 4.4 | **API / service contracts** validated where the story exposes or consumes integrations | | |
| 4.5 | **Database migrations** (if any) applied and verified in integration environment | | Migration ID: |
| 4.6 | End-to-end scenario tested where story is part of a **golden path** (receive → put-away → ATP → reserve → pick) | | E2E ID: |

---

### 5. Documentation Updated

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 5.1 | **User-facing documentation** updated (help text, field labels, workflow guides) if behavior is visible to business users | | Doc link: |
| 5.2 | **Release notes** or sprint increment notes drafted for the story | | |
| 5.3 | **API / technical documentation** updated for new or changed endpoints, events, or integrations | | |
| 5.4 | **Business process** or SOP updates identified and handed to change management *(when operational workflow changes)* | | |
| 5.5 | Story record updated with **implementation notes**, known limitations, and configuration requirements | | |
| 5.6 | Traceability maintained: story ↔ FR ↔ AC ↔ test cases ↔ PR | | |

---

### 6. Security Checks Completed

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 6.1 | **Role-based access control** verified — unauthorized roles cannot perform restricted actions (FR-081) | | |
| 6.2 | **Location-scoped access** verified where applicable (FR-082) | | |
| 6.3 | **Segregation of duties** rules enforced and tested for approval workflows (FR-084) | | |
| 6.4 | **User activity logging** and **audit trail** entries verified for material inventory changes (FR-083, FR-086) | | |
| 6.5 | No **secrets, credentials, or sensitive data** committed to source control | | |
| 6.6 | Dependency **vulnerability scan** passes for new or updated packages *(or exceptions approved)* | | Scan ID: |
| 6.7 | Security review completed for stories affecting **authentication, authorization, audit, or financial data** | | Reviewer: |

---

### 7. Performance Requirements Met

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 7.1 | Applicable **NFR performance targets** verified for the story *(e.g., inventory lookup ≤2 seconds per NFR-PERF-002)* | | NFR ID: |
| 7.2 | No measurable **regression** in response time for core paths (on-hand query, ATP, movement recording) | | Benchmark: |
| 7.3 | **Bulk operations** (import, report generation) meet agreed duration targets or documented interim limits | | |
| 7.4 | Performance test results recorded for high-volume stories (movement history, dashboard aggregation, alerts) | | Test ID: |
| 7.5 | **Availability** and transaction-processing expectations aligned with BRD constraints (same-business-day updates where applicable) | | |

---

### 8. Product Owner Acceptance

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 8.1 | Story demonstrated in **sprint review** against acceptance criteria | | Demo date: |
| 8.2 | **Product Owner** confirms the implemented behavior matches the approved user story and AC | | PO sign-off: |
| 8.3 | Business SME validation completed for stories requiring operational or policy confirmation *(when applicable)* | | SME: |
| 8.4 | Story scope unchanged or **change formally accepted** — no unapproved scope creep | | |
| 8.5 | Story moved to **Done** on the backlog/board with completion date and release tag *(if applicable)* | | Release: |

---

### 9. Deployment & Release Readiness

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 9.1 | Code **merged** to the agreed integration branch (e.g., `develop` / `main`) | | Commit/merge: |
| 9.2 | CI/CD pipeline **green** for the merge commit | | Pipeline #: |
| 9.3 | Feature **deployed** to the target environment (dev / test / staging) per release plan | | Environment: |
| 9.4 | **Smoke test** passed in the deployed environment | | |
| 9.5 | **Rollback plan** understood for high-risk changes (data migration, inventory balance logic, access control) | | |
| 9.6 | Feature flags or configuration toggles documented *(if used)* | | |

---

### 10. Quality & Regression

| # | Criterion | ☐ | Notes / Evidence |
|---|-----------|:-:|------------------|
| 10.1 | **Regression suite** executed for affected modules with pass results | | Suite run ID: |
| 10.2 | Cross-story impacts assessed for shared capabilities (ATP, reservations, movement history, notifications) | | |
| 10.3 | **Test data** cleaned up or documented in non-production environments | | |
| 10.4 | Known issues logged in the defect tracker with severity and owner | | |

---

## Quick-Reference DoD Checklist (Sprint Completion Card)

Copy and complete per story:

```
Story ID: __________   Epic: __________   Sprint: __________   PO: __________

☐ Acceptance criteria satisfied (Happy / Validation / Error / Edge)
☐ QA test cases passed and linked to AC
☐ Code reviewed and PR merged
☐ Unit tests passed (CI green)
☐ Integration tests passed (CI green)
☐ Documentation updated
☐ Security checks completed (RBAC / SoD / audit as applicable)
☐ Performance requirements met (NFR verified)
☐ Regression tests passed
☐ Deployed to target environment and smoke tested
☐ Product Owner acceptance / demo complete

STORY DONE:  ☐ Yes   ☐ No — Blocker: _______________________
```

---

## Definition of Done — Release Increment Gate

Before a **release increment** (MVP go-live, Phase 2 drop) is declared Done, confirm these additional items:

| # | Release Gate Criterion | ☐ |
|---|------------------------|:-:|
| R.1 | All committed Must Have stories for the release meet story-level DoD | |
| R.2 | **UAT** completed for MVP scope with business sign-off | |
| R.3 | **Regression** and E2E golden paths pass in staging | |
| R.4 | **Security** review completed for go-live (access matrix, SoD, audit trail) | |
| R.5 | **Performance** and availability NFRs verified in staging under load representative of primary locations | |
| R.6 | **Release notes**, training materials, and support runbook published | |
| R.7 | **Rollback** and data recovery procedures tested | |
| R.8 | Product Owner and Project Sponsor **accept the release** for deployment | |

---

## Story-Type Variations

| Story type | Additional DoD emphasis |
|------------|-------------------------|
| **Master data / configuration** (EPIC-01) | Data validation rules tested; duplicate detection; import error handling |
| **Operational transaction** (receive, pick, transfer) | Movement history + balance atomicity; audit trail verified |
| **Approval workflow** | SoD tested; notification delivery; threshold routing |
| **Reporting / dashboard** | Correct aggregation; location scope; export performance |
| **Security / access** (EPIC-11) | Penetration of unauthorized paths; location isolation; account lifecycle |
| **Bug fix** | Regression test added; root cause documented; linked to original defect |

---

## Relationship to Definition of Ready (DoR)

| DoR (DOR-IMS-001) | DoD (this document) |
|-------------------|---------------------|
| Conditions to **start** work | Conditions to **complete** work |
| Validated at backlog refinement | Validated before story closure |
| Confirms clarity and testability | Confirms delivery quality and shippability |

A story must pass **DoR before entering the sprint** and **DoD before leaving the sprint** as complete.

---

## Common Reasons a Story Fails DoD

| Gap | Resolution |
|-----|------------|
| AC not fully tested | Complete missing test scenarios; do not mark Done |
| No integration test for cross-module story | Add integration test or document approved manual E2E evidence |
| RBAC not verified | Execute role-matrix tests before closing EPIC-11 dependent stories |
| Performance not measured | Run benchmark against NFR-PERF targets; optimize or get PO deferral |
| PO not available for demo | Schedule review; story stays In Review, not Done |
| Docs not updated for user-visible change | Update help/SOP before release increment |

---

## Document Control

| Attribute | Detail |
|-----------|--------|
| **Document ID** | DOD-IMS-001 |
| **Version** | 1.0 |
| **Created** | July 5, 2026 |
| **Author** | Product Owner |
| **Related Artifacts** | DOR-IMS-001, BRD-IMS-001, AC-REV-IMS-001, NFR-IMS-001, EPIC-IMS-001 |
| **Review Cadence** | Revisit at phase boundaries and after major NFR or compliance changes |

---

*End of Definition of Done Document*
