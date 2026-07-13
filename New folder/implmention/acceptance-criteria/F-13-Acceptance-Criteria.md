# Acceptance Criteria — F-13: Fulfillment Exception Handling

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-13 |
| **Feature Name** | Fulfillment Exception Handling |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-047, US-050, US-078 |
| **Primary roles** | Warehouse Manager, CSR, Inventory Controller |
| **Format** | Given / When / Then |
| **Criteria count** | 12 (H4 / V2 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-13** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-13-H1
- **Given** pick failure or damage occurs
- **When** I create an exception with reason
- **Then** order is routed out of happy path; alert raised

#### FAC-13-H2
- **Given** damage exception
- **When** I apply quarantine
- **Then** ATP excludes damaged qty

#### FAC-13-H3
- **Given** exception resolved
- **When** I return order to correct flow or cancel
- **Then** status and inventory corrected

#### FAC-13-H4
- **Given** authorized substitution (Phase 3)
- **When** approver accepts substitute SKU
- **Then** fulfillment continues with audit of substitution

### 2. Validation Scenarios

#### FAC-13-V1
- **Given** exception without reason
- **When** I submit
- **Then** validation fails

#### FAC-13-V2
- **Given** substitution without approval
- **When** I submit substitute
- **Then** blocked

### 3. Error Scenarios

#### FAC-13-E1
- **Given** resolve already-resolved exception
- **When** I resolve again
- **Then** rejected

#### FAC-13-E2
- **Given** exception on cancelled order
- **When** I create
- **Then** rejected

### 4. Permission Scenarios

#### FAC-13-P1
- **Given** I lack FULFILL_EXCEPTION_MANAGE
- **When** I create/resolve
- **Then** denied

#### FAC-13-P2
- **Given** picker can report but not approve substitution
- **When** I approve substitute
- **Then** denied

### 5. Edge Cases

#### FAC-13-X1
- **Given** exception mid-pack
- **When** I resolve to re-pick
- **Then** pack state resets appropriately

#### FAC-13-X2
- **Given** alert delivery fails
- **When** exception still saved
- **Then** retry notification without losing exception


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-047, US-050, US-078 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-13-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-13*
