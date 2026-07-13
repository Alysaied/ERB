# Acceptance Criteria — F-19: Shrinkage & Obsolescence Analysis

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-19 |
| **Feature Name** | Shrinkage & Obsolescence Analysis |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-039, US-040 |
| **Primary roles** | Inventory Controller, Finance, Ops, Purchasing |
| **Format** | Given / When / Then |
| **Criteria count** | 10 (H2 / V2 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-19** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-19-H1
- **Given** reason-coded losses exist
- **When** I run shrinkage analysis for a period
- **Then** trends by reason/location/sku display

#### FAC-19-H2
- **Given** slow-moving stock exists (Phase 3)
- **When** I open obsolescence view
- **Then** candidates and disposition actions are listed

### 2. Validation Scenarios

#### FAC-19-V1
- **Given** end date before start date
- **When** I run report
- **Then** validation fails

#### FAC-19-V2
- **Given** period exceeds max window
- **When** I run
- **Then** validation fails or requires export job

### 3. Error Scenarios

#### FAC-19-E1
- **Given** no adjustment history
- **When** I run
- **Then** empty result with success, not error

#### FAC-19-E2
- **Given** intelligence API down
- **When** I open page
- **Then** error banner

### 4. Permission Scenarios

#### FAC-19-P1
- **Given** I lack SHRINKAGE_VIEW
- **When** I open analysis
- **Then** denied

#### FAC-19-P2
- **Given** scoped user
- **When** I run
- **Then** only scoped locations included

### 5. Edge Cases

#### FAC-19-X1
- **Given** retired reason codes in history
- **When** I analyze
- **Then** historical codes still appear in trends

#### FAC-19-X2
- **Given** action from obsolete list creates write-off
- **When** I launch disposition
- **Then** F-17 draft prefilled


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-039, US-040 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-19-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-19*
