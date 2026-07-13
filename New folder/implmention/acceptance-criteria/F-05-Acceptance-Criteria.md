# Acceptance Criteria — F-05: Goods Receiving & Verification

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-05 |
| **Feature Name** | Goods Receiving & Verification |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-015, US-016, US-017, US-019, US-020, US-029 |
| **Primary roles** | Receiving Clerk, Warehouse Manager, Buyer |
| **Format** | Given / When / Then |
| **Criteria count** | 19 (H5 / V5 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-05** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-05-H1
- **Given** a valid open PO exists for my location
- **When** I create and verify a goods receipt matching PO lines
- **Then** receipt is recorded and pending put-away is created

#### FAC-05-H2
- **Given** received qty/identity/condition differs
- **When** I document a discrepancy with reason and evidence
- **Then** discrepancy is open and PO/receipt status reflects it

#### FAC-05-H3
- **Given** discrepancy is investigated
- **When** I resolve it with outcome
- **Then** resolution is auditable and receipt can proceed per rules

#### FAC-05-H4
- **Given** authorized non-PO or return inbound arrives
- **When** I record ad-hoc/return receipt with authorization
- **Then** inbound is captured without inventing a PO

#### FAC-05-H5
- **Given** any receipt completes quantity change
- **When** I query movement history
- **Then** an immutable movement record exists with user, time, type, qty

### 2. Validation Scenarios

#### FAC-05-V1
- **Given** PO is not valid for receipt
- **When** I attempt to receive against it
- **Then** receipt is blocked (BR-007)

#### FAC-05-V2
- **Given** traceable product requires lot
- **When** I verify without lot
- **Then** verification fails

#### FAC-05-V3
- **Given** discrepancy lacks reason code
- **When** I submit
- **Then** validation fails

#### FAC-05-V4
- **Given** qty is zero or negative
- **When** I add a line
- **Then** validation fails

#### FAC-05-V5
- **Given** tolerance exceeded (Phase 2)
- **When** qty is outside tolerance
- **Then** system forces discrepancy path

### 3. Error Scenarios

#### FAC-05-E1
- **Given** PO closed/cancelled
- **When** I validate for receipt
- **Then** validation fails with clear status

#### FAC-05-E2
- **Given** location is under physical freeze
- **When** I attempt receipt
- **Then** receipt is blocked

#### FAC-05-E3
- **Given** concurrent update conflicts on receipt
- **When** I verify
- **Then** 409 conflict; no double-post

### 4. Permission Scenarios

#### FAC-05-P1
- **Given** I lack RECEIVE_GOODS
- **When** I open goods receipt workbench commands
- **Then** denied

#### FAC-05-P2
- **Given** I am scoped to WH-01
- **When** I try to receive into WH-02
- **Then** denied by location scope

#### FAC-05-P3
- **Given** I lack discrepancy resolve permission
- **When** I attempt resolve
- **Then** denied; Receiving Clerk may create but not always resolve

### 5. Edge Cases

#### FAC-05-X1
- **Given** partial PO receipt
- **When** I receive subset of lines
- **Then** PO remains PARTIAL; remaining qty still receivable

#### FAC-05-X2
- **Given** over-receipt within tolerance
- **When** auto-accept path applies
- **Then** no discrepancy required

#### FAC-05-X3
- **Given** shelf-life below MRSL
- **When** I verify
- **Then** receipt is blocked or quarantined per policy


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-015, US-016, US-017, US-019, US-020, US-029 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-05-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-05*
