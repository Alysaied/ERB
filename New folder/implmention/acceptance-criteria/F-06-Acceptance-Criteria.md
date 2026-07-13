# Acceptance Criteria — F-06: Put-Away Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-06 |
| **Feature Name** | Put-Away Management |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-018 |
| **Primary roles** | Warehouse Staff, Warehouse Manager |
| **Format** | Given / When / Then |
| **Criteria count** | 13 (H3 / V3 / E3 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-06** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-06-H1
- **Given** verified receipts await put-away
- **When** I open the put-away queue
- **Then** pending tasks for my location are listed

#### FAC-06-H2
- **Given** I select a valid storage position
- **When** I confirm put-away
- **Then** put-away is recorded and sellable ATP increases accordingly

#### FAC-06-H3
- **Given** put-away completes
- **When** pickers search stock
- **Then** quantity is locatable at the confirmed position

### 2. Validation Scenarios

#### FAC-06-V1
- **Given** storage position is missing
- **When** I confirm put-away
- **Then** validation fails

#### FAC-06-V2
- **Given** position is not at receipt location
- **When** I confirm
- **Then** rejected

#### FAC-06-V3
- **Given** qty exceeds pending put-away
- **When** I confirm
- **Then** rejected

### 3. Error Scenarios

#### FAC-06-E1
- **Given** receipt not yet verified
- **When** I attempt put-away
- **Then** blocked

#### FAC-06-E2
- **Given** already put away
- **When** I confirm again
- **Then** idempotent rejection / already complete

#### FAC-06-E3
- **Given** location frozen
- **When** I attempt put-away
- **Then** blocked

### 4. Permission Scenarios

#### FAC-06-P1
- **Given** I lack PUT_AWAY_EXECUTE
- **When** I confirm put-away
- **Then** denied

#### FAC-06-P2
- **Given** task is for another location outside my scope
- **When** I view queue
- **Then** task not visible

### 5. Edge Cases

#### FAC-06-X1
- **Given** stock received but not put away
- **When** Sales checks ATP
- **Then** quantity is not fully sellable/available per policy

#### FAC-06-X2
- **Given** split put-away across bins
- **When** I complete multiple confirmations
- **Then** pending reaches zero and positions sum to received qty


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-018 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-06-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-06*
