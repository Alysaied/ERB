# Acceptance Criteria — F-12: Partial Fulfillment & Backorder Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-12 |
| **Feature Name** | Partial Fulfillment & Backorder Management |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-045, US-046 |
| **Primary roles** | CSR, Warehouse Manager, Purchasing |
| **Format** | Given / When / Then |
| **Criteria count** | 12 (H3 / V3 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-12** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-12-H1
- **Given** full qty unavailable
- **When** I ship available qty with customer acknowledgment
- **Then** partial shipment posts; backorder created for remainder

#### FAC-12-H2
- **Given** stock arrives for backorder (Phase 2)
- **When** priority queue auto-reserves
- **Then** backorder can be fulfilled in sequence

#### FAC-12-H3
- **Given** I view backorder board
- **When** open backorders show
- **Then** customer, SKU, qty, priority, status

### 2. Validation Scenarios

#### FAC-12-V1
- **Given** partial ship without customer ack
- **When** I submit
- **Then** blocked

#### FAC-12-V2
- **Given** ship qty > available
- **When** I submit
- **Then** blocked

#### FAC-12-V3
- **Given** backorder qty <= 0
- **When** I create
- **Then** validation fails

### 3. Error Scenarios

#### FAC-12-E1
- **Given** order already fully shipped
- **When** I create backorder
- **Then** rejected

#### FAC-12-E2
- **Given** backorder fulfill when ATP still insufficient
- **When** I fulfill
- **Then** fails with clear ATP error

### 4. Permission Scenarios

#### FAC-12-P1
- **Given** I lack BACKORDER_MANAGE
- **When** I create/prioritize backorders
- **Then** denied

#### FAC-12-P2
- **Given** CSR can ack partial but not change purchasing priority
- **When** I edit priority
- **Then** denied if not authorized

### 5. Edge Cases

#### FAC-12-X1
- **Given** multiple backorders same SKU
- **When** stock arrives for 1 unit
- **Then** highest priority consumes first

#### FAC-12-X2
- **Given** customer cancels backorder
- **When** I cancel
- **Then** reservation/backorder cleared


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-045, US-046 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-12-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-12*
