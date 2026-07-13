# Acceptance Criteria — F-18: Quarantine & Hold Stock Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-18 |
| **Feature Name** | Quarantine & Hold Stock Management |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-038 |
| **Primary roles** | Warehouse Manager, Inventory Controller |
| **Format** | Given / When / Then |
| **Criteria count** | 11 (H3 / V2 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-18** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-18-H1
- **Given** sellable stock exists
- **When** I apply quarantine hold with type/reason/qty
- **Then** ATP decreases; register shows hold

#### FAC-18-H2
- **Given** inspection complete
- **When** I release hold to available
- **Then** ATP restores

#### FAC-18-H3
- **Given** hold should be written off
- **When** I route to write-off
- **Then** F-17 path can consume held qty

### 2. Validation Scenarios

#### FAC-18-V1
- **Given** hold qty > available for hold
- **When** I apply
- **Then** blocked

#### FAC-18-V2
- **Given** missing hold type/reason
- **When** I apply
- **Then** validation fails

### 3. Error Scenarios

#### FAC-18-E1
- **Given** release unknown hold
- **When** I release
- **Then** 404

#### FAC-18-E2
- **Given** double release
- **When** I release again
- **Then** rejected

### 4. Permission Scenarios

#### FAC-18-P1
- **Given** I lack QUARANTINE_MANAGE
- **When** I apply/release
- **Then** denied

#### FAC-18-P2
- **Given** location outside scope
- **When** I view register
- **Then** not visible

### 5. Edge Cases

#### FAC-18-X1
- **Given** reserved qty exists
- **When** I apply hold
- **Then** cannot hold reserved qty beyond rules; reservation preserved

#### FAC-18-X2
- **Given** bonded/customs hold type
- **When** ATP excluded
- **Then** fulfillment blocked for that qty


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-038 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-18-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-18*
