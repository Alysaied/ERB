# Acceptance Criteria — F-25: Promotional & Launch Stock Readiness

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-25 |
| **Feature Name** | Promotional & Launch Stock Readiness |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-057, US-080 |
| **Primary roles** | Marketing Manager, Purchasing, Warehouse, Sales, Ops |
| **Format** | Given / When / Then |
| **Criteria count** | 12 (H4 / V2 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-25** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-25-H1
- **Given** campaign targets defined
- **When** I create allocation and ring-fence qty
- **Then** general ATP reduced; campaign ATP tracked

#### FAC-25-H2
- **Given** I run readiness check
- **When** coverage vs target shown
- **Then** go/no-go indicated

#### FAC-25-H3
- **Given** campaign ends
- **When** I release allocation
- **Then** qty returns to general ATP

#### FAC-25-H4
- **Given** readiness below threshold
- **When** campaign alert raised
- **Then** F-26 notifies stakeholders

### 2. Validation Scenarios

#### FAC-25-V1
- **Given** ring-fence qty > ATP
- **When** I allocate
- **Then** blocked

#### FAC-25-V2
- **Given** override without reason
- **When** I override
- **Then** blocked

### 3. Error Scenarios

#### FAC-25-E1
- **Given** release unknown allocation
- **When** I release
- **Then** 404

#### FAC-25-E2
- **Given** fulfillment tries to consume ring-fence for normal order
- **When** reserve
- **Then** blocked from ring-fence pool

### 4. Permission Scenarios

#### FAC-25-P1
- **Given** I lack CAMPAIGN_MANAGE
- **When** I create allocation
- **Then** denied

#### FAC-25-P2
- **Given** I lack CAMPAIGN_OVERRIDE
- **When** I override no-go
- **Then** denied

### 5. Edge Cases

#### FAC-25-X1
- **Given** multi-location allocation
- **When** readiness
- **Then** aggregates per location and total

#### FAC-25-X2
- **Given** partial release
- **When** I release subset
- **Then** remaining stays ring-fenced


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-057, US-080 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-25-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-25*
