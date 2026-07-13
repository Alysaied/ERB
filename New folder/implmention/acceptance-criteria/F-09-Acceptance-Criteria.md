# Acceptance Criteria — F-09: Network Stock Rebalancing

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-09 |
| **Feature Name** | Network Stock Rebalancing |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-062 |
| **Primary roles** | Operations Director, Inventory Controller |
| **Format** | Given / When / Then |
| **Criteria count** | 10 (H2 / V2 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-09** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-09-H1
- **Given** network has overstock and stockout sites for a SKU
- **When** I run rebalance analysis
- **Then** imbalance scores and recommendations appear

#### FAC-09-H2
- **Given** a recommendation is acceptable
- **When** I convert it to a transfer request
- **Then** F-08 request is created pre-filled

### 2. Validation Scenarios

#### FAC-09-V1
- **Given** no SKU/network filter when required
- **When** I run analysis
- **Then** validation requires scope

#### FAC-09-V2
- **Given** recommendation would breach source minimum
- **When** I convert
- **Then** blocked or adjusted qty proposed

### 3. Error Scenarios

#### FAC-09-E1
- **Given** insufficient data history
- **When** I run analysis
- **Then** clear unavailable message

#### FAC-09-E2
- **Given** intelligence service down
- **When** I open UI
- **Then** error state, no fake recommendations

### 4. Permission Scenarios

#### FAC-09-P1
- **Given** I lack NETWORK_REBALANCE_VIEW
- **When** I open analysis
- **Then** denied

#### FAC-09-P2
- **Given** I can view but lack TRANSFER_REQUEST
- **When** I convert recommendation
- **Then** convert denied

### 5. Edge Cases

#### FAC-09-X1
- **Given** multiple recommendations for same source
- **When** I convert several
- **Then** capacity is re-checked sequentially

#### FAC-09-X2
- **Given** all locations balanced
- **When** I run analysis
- **Then** empty recommendation set with success status


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-062 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-09-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-09*
