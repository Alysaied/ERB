# Acceptance Criteria — F-15: Full Physical Inventory Count

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-15 |
| **Feature Name** | Full Physical Inventory Count |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-032 |
| **Primary roles** | Inventory Controller, Warehouse Manager, Ops Director |
| **Format** | Given / When / Then |
| **Criteria count** | 12 (H3 / V2 / E2 / P3 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-15** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-15-H1
- **Given** I initiate physical count for a location
- **When** freeze activates
- **Then** receiving/shipping/transfers/adjustments blocked

#### FAC-15-H2
- **Given** teams enter results
- **When** I monitor progress
- **Then** completion % is visible

#### FAC-15-H3
- **Given** all zones complete
- **When** I certify the count
- **Then** variances are produced and freeze can be released per process

### 2. Validation Scenarios

#### FAC-15-V1
- **Given** certify while incomplete
- **When** I certify
- **Then** blocked

#### FAC-15-V2
- **Given** missing location
- **When** I create count
- **Then** validation fails

### 3. Error Scenarios

#### FAC-15-E1
- **Given** transaction attempted during freeze
- **When** I receive/ship
- **Then** blocked with freeze status

#### FAC-15-E2
- **Given** certify without authority
- **When** I certify
- **Then** denied

### 4. Permission Scenarios

#### FAC-15-P1
- **Given** I lack PHYSICAL_COUNT_MANAGE
- **When** I initiate
- **Then** denied

#### FAC-15-P2
- **Given** I lack PHYSICAL_COUNT_CERTIFY
- **When** I certify
- **Then** denied

#### FAC-15-P3
- **Given** staff can enter counts but not lift freeze
- **When** I attempt unfreeze
- **Then** denied

### 5. Edge Cases

#### FAC-15-X1
- **Given** in-transit transfer exists at freeze start
- **When** I initiate
- **Then** system warns and handles per policy

#### FAC-15-X2
- **Given** recount required for large variance
- **When** I flag recount
- **Then** certify waits on recount


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-032 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-15-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-15*
