# Acceptance Criteria — F-20: Low-Stock Alerting & Replenishment

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-20 |
| **Feature Name** | Low-Stock Alerting & Replenishment |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-051, US-052, US-053, US-054, US-074 |
| **Primary roles** | Purchasing Manager, Buyer, Inventory Controller |
| **Format** | Given / When / Then |
| **Criteria count** | 17 (H5 / V3 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-20** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-20-H1
- **Given** ATP reaches reorder level
- **When** alert is generated
- **Then** appears in alert review with SKU/location/severity

#### FAC-20-H2
- **Given** I acknowledge an alert
- **When** ack stored
- **Then** alert leaves unread / requires rationale if dismissed

#### FAC-20-H3
- **Given** network has surplus elsewhere
- **When** I view recommendation
- **Then** transfer-before-buy suggested

#### FAC-20-H4
- **Given** I create requisition from recommendation (Phase 2)
- **When** approval then convert to PO
- **Then** traceable replenishment path

#### FAC-20-H5
- **Given** I open replenishment reporting
- **When** period metrics show
- **Then** alerts acted vs ignored

### 2. Validation Scenarios

#### FAC-20-V1
- **Given** dismiss without rationale when required
- **When** I dismiss
- **Then** blocked

#### FAC-20-V2
- **Given** requisition line qty <= 0
- **When** I submit
- **Then** validation fails

#### FAC-20-V3
- **Given** approve requisition without network check
- **When** system evaluates
- **Then** must consider transfer options (BR-011)

### 3. Error Scenarios

#### FAC-20-E1
- **Given** acknowledge unknown alert
- **When** I ack
- **Then** 404

#### FAC-20-E2
- **Given** convert unapproved requisition to PO
- **When** I convert
- **Then** blocked

#### FAC-20-E3
- **Given** duplicate alert storm for same breach
- **When** generation runs
- **Then** deduped/coalesced per policy

### 4. Permission Scenarios

#### FAC-20-P1
- **Given** I lack ALERT_REVIEW
- **When** I ack
- **Then** denied

#### FAC-20-P2
- **Given** I lack REQUISITION_APPROVE
- **When** I approve
- **Then** denied

#### FAC-20-P3
- **Given** buyer can create requisition but not convert
- **When** I convert
- **Then** denied

### 5. Edge Cases

#### FAC-20-X1
- **Given** threshold changed after alert
- **When** I review
- **Then** alert shows snapshot vs current policy

#### FAC-20-X2
- **Given** OOS vs low-stock
- **When** both fire
- **Then** distinct severities

#### FAC-20-X3
- **Given** C-03 list API missing
- **When** queue UX limited
- **Then** not accepted as complete until list endpoint exists


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-051, US-052, US-053, US-054, US-074 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-20-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-20*
