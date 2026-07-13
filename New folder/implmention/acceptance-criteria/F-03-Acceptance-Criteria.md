# Acceptance Criteria — F-03: Stock Policy & Product Classification

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-03 |
| **Feature Name** | Stock Policy & Product Classification |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-008, US-009, US-012, US-056 |
| **Primary roles** | Inventory Controller, Purchasing Manager, Operations Director |
| **Format** | Given / When / Then |
| **Criteria count** | 18 (H5 / V4 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-03** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-03-H1
- **Given** product and location exist
- **When** I set reorder, minimum, and safety stock for that pair
- **Then** policy is saved with effective date and prior values retained in history

#### FAC-03-H2
- **Given** ATP crosses reorder level
- **When** stock status and alert engines evaluate policy
- **Then** LOW_STOCK / OOS indicators and alerts can fire

#### FAC-03-H3
- **Given** I am authorized (Phase 2)
- **When** I assign ABC class A/B/C to a product
- **Then** class is stored and available to counting/alert priority

#### FAC-03-H4
- **Given** I publish governance policy with reason codes and thresholds
- **When** effective date arrives
- **Then** new transactions use the new policy version

#### FAC-03-H5
- **Given** safety stock protection is enabled
- **When** a fulfillment attempt would breach safety stock without exception
- **Then** the system blocks or requires authorized exception + replenishment plan

### 2. Validation Scenarios

#### FAC-03-V1
- **Given** threshold values are negative
- **When** I save policy
- **Then** save is rejected

#### FAC-03-V2
- **Given** minimum exceeds reorder without authorized invert
- **When** I save
- **Then** validation fails

#### FAC-03-V3
- **Given** ABC value is not A/B/C
- **When** I assign classification
- **Then** validation fails

#### FAC-03-V4
- **Given** I try to use a retired reason code
- **When** I submit an adjustment
- **Then** selection is blocked

### 3. Error Scenarios

#### FAC-03-E1
- **Given** policy for location+sku does not exist
- **When** downstream status calculation runs
- **Then** status falls back to defined default (e.g., no threshold alerts) without crashing

#### FAC-03-E2
- **Given** two policy versions would overlap effective periods
- **When** I publish
- **Then** system rejects overlapping effectivity

#### FAC-03-E3
- **Given** receipt tolerance config is invalid
- **When** I save tolerances
- **Then** save fails with field errors

### 4. Permission Scenarios

#### FAC-03-P1
- **Given** I lack POLICY_MANAGE
- **When** I attempt to edit thresholds
- **Then** denied

#### FAC-03-P2
- **Given** I lack GOVERNANCE_MANAGE
- **When** I attempt to create reason codes or approval thresholds
- **Then** denied

#### FAC-03-P3
- **Given** I am Purchasing Manager with policy view
- **When** I view thresholds for my locations
- **Then** read succeeds; write denied

### 5. Edge Cases

#### FAC-03-X1
- **Given** threshold change is future-dated
- **When** current date is before effective date
- **Then** old thresholds remain in force until effective date

#### FAC-03-X2
- **Given** safety stock bypass is requested with documented approval
- **When** authorized user confirms
- **Then** bypass is allowed and auditable

#### FAC-03-X3
- **Given** ABC not yet assigned
- **When** cycle count scheduling runs
- **Then** product is treated as default priority class


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-008, US-009, US-012, US-056 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-03-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-03*
