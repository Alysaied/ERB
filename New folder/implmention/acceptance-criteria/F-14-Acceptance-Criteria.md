# Acceptance Criteria — F-14: Cycle Counting

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-14 |
| **Feature Name** | Cycle Counting |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-030, US-031, US-071 |
| **Primary roles** | Inventory Controller, Warehouse Staff |
| **Format** | Given / When / Then |
| **Criteria count** | 13 (H3 / V3 / E2 / P3 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-14** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-14-H1
- **Given** I schedule and assign cycle counts
- **When** assignees open workbench
- **Then** assigned blind counts appear

#### FAC-14-H2
- **Given** I am a counter
- **When** I enter physical qty without seeing system qty
- **Then** result submits and variances generate when mismatch

#### FAC-14-H3
- **Given** counts complete over a period
- **When** accuracy report runs
- **Then** count performance metrics are available

### 2. Validation Scenarios

#### FAC-14-V1
- **Given** assignment missing user/location/sku
- **When** I create count
- **Then** validation fails

#### FAC-14-V2
- **Given** negative count qty
- **When** I submit
- **Then** validation fails

#### FAC-14-V3
- **Given** UI attempts to display system qty to counter
- **When** blind mode
- **Then** system qty is not shown

### 3. Error Scenarios

#### FAC-14-E1
- **Given** submit twice
- **When** I resubmit
- **Then** rejected as already submitted

#### FAC-14-E2
- **Given** count for unknown SKU
- **When** I submit
- **Then** rejected

### 4. Permission Scenarios

#### FAC-14-P1
- **Given** I lack CYCLE_COUNT_EXECUTE
- **When** I submit count
- **Then** denied

#### FAC-14-P2
- **Given** I lack CYCLE_COUNT_MANAGE
- **When** I schedule counts
- **Then** denied

#### FAC-14-P3
- **Given** assigned to another user
- **When** I open my queue
- **Then** I do not see others' assignments

### 5. Edge Cases

#### FAC-14-X1
- **Given** ABC-A counted more frequently
- **When** schedule generated
- **Then** A items appear more often than C

#### FAC-14-X2
- **Given** zero physical found
- **When** I enter 0
- **Then** variance equals full system qty


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-030, US-031, US-071 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-14-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-14*
