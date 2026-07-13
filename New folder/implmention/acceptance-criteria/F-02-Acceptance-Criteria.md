# Acceptance Criteria — F-02: Location & Network Setup

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-02 |
| **Feature Name** | Location & Network Setup |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-005, US-006, US-007, US-010 |
| **Primary roles** | Operations Director, Inventory Controller, Warehouse Manager |
| **Format** | Given / When / Then |
| **Criteria count** | 18 (H5 / V4 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-02** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-02-H1
- **Given** I am authorized
- **When** I create a warehouse/store/DC with code, name, type, and status
- **Then** the location is available for stock assignment and reporting

#### FAC-02-H2
- **Given** multiple locations exist
- **When** I assign a parent in the hierarchy
- **Then** roll-up visibility and accountability use the hierarchy path

#### FAC-02-H3
- **Given** a location has storage positions configured
- **When** I list positions for put-away
- **Then** zone/aisle/bin options are available for that location only

#### FAC-02-H4
- **Given** opening balances are verified and approved
- **When** I activate a location
- **Then** the location accepts transactional inventory activity

#### FAC-02-H5
- **Given** a location is closing with a disposition plan (Phase 2)
- **When** I execute closure after stock disposition
- **Then** the location is closed and no orphan stock remains

### 2. Validation Scenarios

#### FAC-02-V1
- **Given** location code or name is missing
- **When** I attempt to save
- **Then** save is blocked with required-field errors

#### FAC-02-V2
- **Given** I set a location as its own parent
- **When** I save hierarchy
- **Then** the system rejects the cyclic hierarchy

#### FAC-02-V3
- **Given** opening balances are not approved
- **When** I attempt to activate the location
- **Then** activation is blocked until openings are verified

#### FAC-02-V4
- **Given** on-hand stock remains without disposition
- **When** I attempt to close the location
- **Then** closure is blocked

### 3. Error Scenarios

#### FAC-02-E1
- **Given** location code already exists
- **When** I create a location
- **Then** creation fails with conflict and existing code is cited

#### FAC-02-E2
- **Given** a location is frozen for physical count
- **When** I attempt non-count transactions
- **Then** operations are blocked with freeze reason

#### FAC-02-E3
- **Given** storage position belongs to another location
- **When** I assign it on put-away for this site
- **Then** the system rejects the position

### 4. Permission Scenarios

#### FAC-02-P1
- **Given** I lack LOCATION_MANAGE
- **When** I attempt to create or edit locations
- **Then** action is denied (403)

#### FAC-02-P2
- **Given** I am a Regional Manager scoped to Region A
- **When** I list locations
- **Then** only locations in my scope are returned

#### FAC-02-P3
- **Given** I am not Operations Director
- **When** I attempt hierarchy redesign or closure
- **Then** action is denied

### 5. Edge Cases

#### FAC-02-X1
- **Given** a planned location exists before go-live
- **When** I view operational lists
- **Then** it does not accept receipts/reservations until activated

#### FAC-02-X2
- **Given** parent is deactivated
- **When** child locations still hold stock
- **Then** children remain operable until individually changed; roll-up notes inactive parent

#### FAC-02-X3
- **Given** I deactivate a location with open transfers in-transit
- **When** I confirm deactivation
- **Then** system warns and restricts new activity while allowing receipt of in-transit


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-005, US-006, US-007, US-010 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-02-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-02*
