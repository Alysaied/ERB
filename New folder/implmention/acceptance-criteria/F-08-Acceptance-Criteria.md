# Acceptance Criteria — F-08: Inter-Location Stock Transfers

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-08 |
| **Feature Name** | Inter-Location Stock Transfers |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-058, US-059, US-060, US-061, US-063 |
| **Primary roles** | Regional/Store Manager, Operations Director, Warehouse Manager |
| **Format** | Given / When / Then |
| **Criteria count** | 18 (H5 / V4 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-08** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-08-H1
- **Given** source has transferable capacity above minimum
- **When** I submit a transfer request with justification
- **Then** request is PENDING approval

#### FAC-08-H2
- **Given** I am an independent approver
- **When** I approve the request
- **Then** transfer becomes approved for execution

#### FAC-08-H3
- **Given** transfer is approved
- **When** I dispatch then receive at destination
- **Then** source decreases, destination increases, in-transit clears

#### FAC-08-H4
- **Given** transfer is in transit (Phase 2)
- **When** I open in-transit monitor
- **Then** qty, source, destination, and status are visible

#### FAC-08-H5
- **Given** I reject a request with reason
- **When** request is rejected
- **Then** no stock moves; rationale is stored

### 2. Validation Scenarios

#### FAC-08-V1
- **Given** source equals destination
- **When** I submit
- **Then** validation fails

#### FAC-08-V2
- **Given** requested qty exceeds transfer capacity
- **When** I submit
- **Then** blocked by source minimum (BR-012)

#### FAC-08-V3
- **Given** justification missing
- **When** I submit
- **Then** validation fails

#### FAC-08-V4
- **Given** qty <= 0
- **When** I submit
- **Then** validation fails

### 3. Error Scenarios

#### FAC-08-E1
- **Given** source location frozen
- **When** I dispatch
- **Then** blocked

#### FAC-08-E2
- **Given** approve own request (SoD)
- **When** I approve
- **Then** blocked

#### FAC-08-E3
- **Given** receive qty mismatches dispatch
- **When** I receive
- **Then** discrepancy/exception path required

### 4. Permission Scenarios

#### FAC-08-P1
- **Given** I lack TRANSFER_REQUEST
- **When** I create request
- **Then** denied

#### FAC-08-P2
- **Given** I lack TRANSFER_APPROVE
- **When** I approve
- **Then** denied

#### FAC-08-P3
- **Given** I can request for my store but not approve network transfers
- **When** I open approval queue
- **Then** queue empty / unauthorized

### 5. Edge Cases

#### FAC-08-X1
- **Given** capacity changes after request before approve
- **When** approver reviews
- **Then** system re-validates capacity at approval

#### FAC-08-X2
- **Given** cancel after dispatch not allowed
- **When** I cancel
- **Then** only pre-dispatch cancel permitted

#### FAC-08-X3
- **Given** partial receive
- **When** remaining stays in-transit until complete
- **Then** balances stay consistent


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-058, US-059, US-060, US-061, US-063 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-08-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-08*
