# Acceptance Criteria — F-07: Purchase Order & Inbound Supply Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-07 |
| **Feature Name** | Purchase Order & Inbound Supply Management |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-013, US-014, US-021, US-022, US-055, US-079 |
| **Primary roles** | Buyer, Purchasing Manager, Warehouse Manager |
| **Format** | Given / When / Then |
| **Criteria count** | 18 (H5 / V4 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-07** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-07-H1
- **Given** supplier and products are active
- **When** I create a PO with lines
- **Then** PO is OPEN and visible in inbound pipeline

#### FAC-07-H2
- **Given** PO is open
- **When** I schedule expected delivery dates
- **Then** inbound calendar reflects the plan

#### FAC-07-H3
- **Given** PO needs change
- **When** I amend lines/dates or cancel per rules
- **Then** status and receipt authorization update correctly

#### FAC-07-H4
- **Given** open POs and delays exist
- **When** I open inbound tracking
- **Then** open qty, ETA, and delays are visible

#### FAC-07-H5
- **Given** inbound delay is detected
- **When** notification recipients are configured
- **Then** delay alert is raised (via F-26)

### 2. Validation Scenarios

#### FAC-07-V1
- **Given** supplier is inactive
- **When** I create PO
- **Then** blocked

#### FAC-07-V2
- **Given** line product is discontinued
- **When** I add line
- **Then** blocked (BR-027)

#### FAC-07-V3
- **Given** line qty <= 0
- **When** I save
- **Then** validation fails

#### FAC-07-V4
- **Given** cancel when fully received
- **When** I cancel
- **Then** blocked

### 3. Error Scenarios

#### FAC-07-E1
- **Given** amend after partial receipt beyond allowed
- **When** I amend received lines downward below received qty
- **Then** rejected

#### FAC-07-E2
- **Given** supplier code unknown
- **When** I reference supplier
- **Then** 404/validation error

#### FAC-07-E3
- **Given** concurrent amend
- **When** two buyers save
- **Then** optimistic lock conflict on one

### 4. Permission Scenarios

#### FAC-07-P1
- **Given** I lack PO_MANAGE
- **When** I create/amend PO
- **Then** denied

#### FAC-07-P2
- **Given** I have PO_VIEW only
- **When** I list open POs
- **Then** read OK, write denied

#### FAC-07-P3
- **Given** PO is for another location outside scope
- **When** I view
- **Then** hidden or denied

### 5. Edge Cases

#### FAC-07-X1
- **Given** requisition converts to PO
- **When** I convert approved requisition
- **Then** PO created with traceable link

#### FAC-07-X2
- **Given** supplier performance metrics (Phase 3)
- **When** deliveries complete late
- **Then** performance record updates

#### FAC-07-X3
- **Given** expected delivery in the past without receipt
- **When** tracking view
- **Then** shows delayed status


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-013, US-014, US-021, US-022, US-055, US-079 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-07-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-07*
