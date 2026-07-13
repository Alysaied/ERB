# Acceptance Criteria — F-23: Inventory Performance KPIs

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-23 |
| **Feature Name** | Inventory Performance KPIs |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-073 |
| **Primary roles** | CEO, COO, CFO, Ops Director |
| **Format** | Given / When / Then |
| **Criteria count** | 9 (H2 / V1 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-23** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-23-H1
- **Given** fulfillment and inventory history exist
- **When** I open executive KPI dashboard
- **Then** fill rate, turnover, DOS, accuracy vs targets display

#### FAC-23-H2
- **Given** I select a period
- **When** trends update
- **Then** comparison to targets visible

### 2. Validation Scenarios

#### FAC-23-V1
- **Given** period missing
- **When** I query KPIs
- **Then** validation fails

### 3. Error Scenarios

#### FAC-23-E1
- **Given** insufficient history for turnover
- **When** I view
- **Then** KPI shows unavailable/N/A with explanation

#### FAC-23-E2
- **Given** service error
- **When** I open
- **Then** error banner

### 4. Permission Scenarios

#### FAC-23-P1
- **Given** I lack KPI_VIEW_EXEC
- **When** I open UI-003
- **Then** denied

#### FAC-23-P2
- **Given** non-executive role
- **When** I navigate via URL
- **Then** blocked by permission guard

### 5. Edge Cases

#### FAC-23-X1
- **Given** target not configured
- **When** I view
- **Then** KPI shows value without target comparison

#### FAC-23-X2
- **Given** drill to operational report
- **When** I click fill rate
- **Then** opens supporting F-22 report


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-073 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-23-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-23*
