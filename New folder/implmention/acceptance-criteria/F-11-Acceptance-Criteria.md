# Acceptance Criteria — F-11: Pick, Pack & Ship Fulfillment

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-11 |
| **Feature Name** | Pick, Pack & Ship Fulfillment |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-044, US-049 |
| **Primary roles** | Warehouse Picker/Packer, Warehouse Manager, CSR |
| **Format** | Given / When / Then |
| **Criteria count** | 15 (H3 / V3 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-11** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-11-H1
- **Given** confirmed reserved orders await pick
- **When** I generate/open pick list
- **Then** queue shows my location work

#### FAC-11-H2
- **Given** I pick and verify lines
- **When** I pack and ship
- **Then** shipment is confirmed and on-hand decreases; reservation clears

#### FAC-11-H3
- **Given** order progresses
- **When** CSR opens status
- **Then** reservation/pick/pack/ship states are visible

### 2. Validation Scenarios

#### FAC-11-V1
- **Given** verify qty does not match pick
- **When** I submit verify
- **Then** fails

#### FAC-11-V2
- **Given** lot required but missing
- **When** I verify pick
- **Then** fails

#### FAC-11-V3
- **Given** ship before pack
- **When** I ship
- **Then** blocked

### 3. Error Scenarios

#### FAC-11-E1
- **Given** location frozen
- **When** I pick
- **Then** blocked

#### FAC-11-E2
- **Given** stock physically missing at pick
- **When** I record pick failure
- **Then** exception path (F-13) engaged; no silent short ship

#### FAC-11-E3
- **Given** shipment API fails after pack
- **When** I retry ship
- **Then** no double deduction

### 4. Permission Scenarios

#### FAC-11-P1
- **Given** I lack FULFILL_PICK
- **When** I verify pick
- **Then** denied

#### FAC-11-P2
- **Given** I lack FULFILL_SHIP
- **When** I confirm shipment
- **Then** denied

#### FAC-11-P3
- **Given** pick queue for other site
- **When** I list awaiting picks
- **Then** not visible outside scope

### 5. Edge Cases

#### FAC-11-X1
- **Given** FEFO lot selection
- **When** I pick perishable
- **Then** system guides/enforces rotation policy

#### FAC-11-X2
- **Given** status inquiry during pick
- **When** CSR views
- **Then** shows in-progress state

#### FAC-11-X3
- **Given** gap C-01 location queue missing
- **When** workaround list-by-order works until endpoint added
- **Then** documented limitation not treated as pass


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-044, US-049 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-11-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-11*
