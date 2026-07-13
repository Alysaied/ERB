# Acceptance Criteria — F-21: Returns Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-21 |
| **Feature Name** | Returns Management |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-064, US-065, US-066, US-067 |
| **Primary roles** | CSR, Receiving Clerk, Warehouse Manager, Inventory Controller |
| **Format** | Given / When / Then |
| **Criteria count** | 16 (H5 / V3 / E3 / P3 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-21** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-21-H1
- **Given** original order exists and is eligible
- **When** I create RA
- **Then** RA issued and visible to warehouse

#### FAC-21-H2
- **Given** goods arrive
- **When** I receive against RA and inspect
- **Then** inspection result recorded

#### FAC-21-H3
- **Given** disposition RESTOCK
- **When** I complete disposition
- **Then** ATP increases for sellable qty

#### FAC-21-H4
- **Given** disposition WRITE_OFF or QUARANTINE
- **When** I complete
- **Then** stock does not re-enter sellable incorrectly

#### FAC-21-H5
- **Given** CSR views status
- **When** end-to-end RA→receive→disposition status visible
- **Then** customer communication supported

### 2. Validation Scenarios

#### FAC-21-V1
- **Given** RA qty > shipped qty
- **When** I create
- **Then** blocked

#### FAC-21-V2
- **Given** disposition before inspection
- **When** I disposition
- **Then** blocked

#### FAC-21-V3
- **Given** invalid disposition decision
- **When** I submit
- **Then** validation fails

### 3. Error Scenarios

#### FAC-21-E1
- **Given** receive without RA when RA required
- **When** I receive
- **Then** blocked

#### FAC-21-E2
- **Given** cancel RA after receipt started
- **When** I cancel
- **Then** blocked

#### FAC-21-E3
- **Given** wrong item vs RA
- **When** I inspect
- **Then** discrepancy/exception required

### 4. Permission Scenarios

#### FAC-21-P1
- **Given** I lack RETURN_AUTHORIZE
- **When** I create RA
- **Then** denied

#### FAC-21-P2
- **Given** I lack RETURN_DISPOSITION
- **When** I disposition
- **Then** denied

#### FAC-21-P3
- **Given** CSR cannot write-off high value without Finance
- **When** I write-off
- **Then** routed/denied per threshold

### 5. Edge Cases

#### FAC-21-X1
- **Given** partial return lines
- **When** I RA subset
- **Then** remaining order lines unaffected

#### FAC-21-X2
- **Given** restock damaged accidentally selected
- **When** policy prevents
- **Then** only RESTOCK if inspection OK


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-064, US-065, US-066, US-067 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-21-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-21*
