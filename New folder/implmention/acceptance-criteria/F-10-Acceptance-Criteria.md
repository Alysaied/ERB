# Acceptance Criteria — F-10: Order Availability & Reservation

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-10 |
| **Feature Name** | Order Availability & Reservation |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-041, US-042, US-043, US-048 |
| **Primary roles** | Sales Representative, CSR, Sales Manager |
| **Format** | Given / When / Then |
| **Criteria count** | 16 (H4 / V3 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-10** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-10-H1
- **Given** ATP is sufficient at a location
- **When** I confirm availability for an order
- **Then** confirmation succeeds with ATP snapshot

#### FAC-10-H2
- **Given** availability confirmed
- **When** I confirm the order
- **Then** reservations are created and ATP decreases

#### FAC-10-H3
- **Given** order is cancelled before ship
- **When** I cancel
- **Then** reservations release and ATP restores

#### FAC-10-H4
- **Given** single location ATP insufficient (Phase 2)
- **When** I create multi-location plan
- **Then** plan allocates across locations without overselling

### 2. Validation Scenarios

#### FAC-10-V1
- **Given** order lines empty or qty <= 0
- **When** I confirm availability
- **Then** validation fails

#### FAC-10-V2
- **Given** product inactive/discontinued
- **When** I reserve
- **Then** blocked unless authorized exception

#### FAC-10-V3
- **Given** requested qty > ATP
- **When** I confirm
- **Then** fails with insufficient ATP

### 3. Error Scenarios

#### FAC-10-E1
- **Given** concurrent reservations exhaust ATP
- **When** second confirm runs
- **Then** one succeeds; other fails with conflict/insufficient ATP

#### FAC-10-E2
- **Given** order already cancelled
- **When** I reserve again
- **Then** state error

#### FAC-10-E3
- **Given** promotional ring-fence reduces general ATP
- **When** I reserve general stock
- **Then** cannot consume ring-fenced qty

### 4. Permission Scenarios

#### FAC-10-P1
- **Given** I lack ORDER_RESERVE
- **When** I confirm order
- **Then** denied

#### FAC-10-P2
- **Given** order location outside my scope
- **When** I view/reserve
- **Then** denied or filtered

#### FAC-10-P3
- **Given** unauthenticated
- **When** I call availability API
- **Then** 401

### 5. Edge Cases

#### FAC-10-X1
- **Given** partial line availability
- **When** I confirm
- **Then** system reports which lines fail

#### FAC-10-X2
- **Given** release after partial fulfill
- **When** I cancel remaining
- **Then** only open reservations release

#### FAC-10-X3
- **Given** idempotent confirm retry with same key
- **When** I retry
- **Then** no double reservation


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-041, US-042, US-043, US-048 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-10-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-10*
