# Acceptance Criteria — F-17: Stock Adjustments & Write-Offs

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-17 |
| **Feature Name** | Stock Adjustments & Write-Offs |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-011, US-035, US-036, US-077 |
| **Primary roles** | Warehouse Manager, Inventory Controller, Ops Director, Finance |
| **Format** | Given / When / Then |
| **Criteria count** | 16 (H4 / V4 / E3 / P3 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-17** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-17-H1
- **Given** I maintain reason codes
- **When** codes are active
- **Then** selectable on adjustments/discrepancies

#### FAC-17-H2
- **Given** I submit adjustment with reason and qty
- **When** routing applies
- **Then** pending approval then posts to stock + movement

#### FAC-17-H3
- **Given** I submit write-off with evidence
- **When** authorized approvers approve
- **Then** qty permanently removed with audit

#### FAC-17-H4
- **Given** adjustment pending
- **When** approver notified
- **Then** F-26 approval notification delivered

### 2. Validation Scenarios

#### FAC-17-V1
- **Given** adjustment without reason code
- **When** I submit
- **Then** blocked

#### FAC-17-V2
- **Given** retired reason code
- **When** I select
- **Then** blocked

#### FAC-17-V3
- **Given** write-off without evidence when required
- **When** I submit
- **Then** blocked

#### FAC-17-V4
- **Given** qty zero
- **When** I submit
- **Then** blocked

### 3. Error Scenarios

#### FAC-17-E1
- **Given** approve own adjustment (SoD)
- **When** I approve
- **Then** blocked

#### FAC-17-E2
- **Given** insufficient on-hand for negative adjustment
- **When** I approve
- **Then** blocked

#### FAC-17-E3
- **Given** location frozen
- **When** I submit ad-hoc adjust
- **Then** blocked except count-driven path

### 4. Permission Scenarios

#### FAC-17-P1
- **Given** I lack ADJUST_SUBMIT
- **When** I submit
- **Then** denied

#### FAC-17-P2
- **Given** I lack ADJUST_APPROVE / WRITE_OFF_AUTHORIZE
- **When** I approve
- **Then** denied

#### FAC-17-P3
- **Given** Finance-only write-off tier
- **When** Ops tries to final-approve
- **Then** denied

### 5. Edge Cases

#### FAC-17-X1
- **Given** threshold exactly at boundary
- **When** I submit
- **Then** routes to correct approver tier

#### FAC-17-X2
- **Given** reject adjustment
- **When** stock unchanged
- **Then** reason stored; submitter notified


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-011, US-035, US-036, US-077 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-17-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-17*
