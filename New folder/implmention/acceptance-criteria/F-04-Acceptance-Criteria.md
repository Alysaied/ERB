# Acceptance Criteria — F-04: Inventory Visibility & Search

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-04 |
| **Feature Name** | Inventory Visibility & Search |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-023, US-024, US-025, US-026, US-027, US-028 |
| **Primary roles** | Inventory Controller, Operations Director, Sales, CSR, Warehouse Manager |
| **Format** | Given / When / Then |
| **Criteria count** | 17 (H5 / V3 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-04** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-04-H1
- **Given** stock exists at my authorized location
- **When** I open inventory status for a SKU
- **Then** on-hand, reserved, and ATP are displayed

#### FAC-04-H2
- **Given** reservations and holds exist
- **When** I view ATP
- **Then** ATP equals on-hand minus reserved minus quarantined

#### FAC-04-H3
- **Given** thresholds exist
- **When** quantities cross bands
- **Then** status shows In Stock / Low / Out / Overstock correctly

#### FAC-04-H4
- **Given** I enter multi-criteria filters
- **When** I search inventory
- **Then** matching rows for my scope are returned

#### FAC-04-H5
- **Given** Phase 2 network view is enabled
- **When** I request network ATP for a SKU
- **Then** rollup across authorized locations is shown including expected inbound when available

### 2. Validation Scenarios

#### FAC-04-V1
- **Given** SKU is blank on availability inquiry
- **When** I submit
- **Then** validation requires SKU

#### FAC-04-V2
- **Given** page size exceeds max
- **When** I request a list
- **Then** request is rejected or capped per API rules

#### FAC-04-V3
- **Given** location filter is outside my scope
- **When** I submit
- **Then** filter is ignored or rejected; only scoped data returns

### 3. Error Scenarios

#### FAC-04-E1
- **Given** SKU does not exist
- **When** I inquire availability
- **Then** 404/not found with clear message

#### FAC-04-E2
- **Given** downstream stock service is unavailable
- **When** I open the monitor
- **Then** graceful error is shown; no fabricated balances

#### FAC-04-E3
- **Given** stock position missing for location+sku
- **When** I query detail
- **Then** empty/zero position semantics are clear (not a crash)

### 4. Permission Scenarios

#### FAC-04-P1
- **Given** I am not authenticated
- **When** I call stock APIs
- **Then** 401

#### FAC-04-P2
- **Given** I lack INVENTORY_VIEW
- **When** I open status monitor
- **Then** 403 / route blocked

#### FAC-04-P3
- **Given** I am scoped to Location A only
- **When** I query Location B
- **Then** no Location B data is returned

### 5. Edge Cases

#### FAC-04-X1
- **Given** on-hand is zero but inbound is expected (Phase 2)
- **When** I view availability
- **Then** inbound projection is separate from ATP sellable

#### FAC-04-X2
- **Given** lot-tracked product
- **When** I drill into position
- **Then** lot breakdown is available without changing ATP math

#### FAC-04-X3
- **Given** concurrent reservation updates ATP
- **When** I refresh the view
- **Then** updated ATP is shown after refresh


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-023, US-024, US-025, US-026, US-027, US-028 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-04-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-04*
