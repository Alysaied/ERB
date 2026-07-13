# Acceptance Criteria — F-24: Financial Inventory Reconciliation

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-24 |
| **Feature Name** | Financial Inventory Reconciliation |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-075, US-089 |
| **Primary roles** | Finance Manager, CFO, Inventory Controller, Auditor |
| **Format** | Given / When / Then |
| **Criteria count** | 12 (H4 / V2 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-24** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-24-H1
- **Given** PO, GR, and invoice exist
- **When** I run three-way match
- **Then** match result success/fail recorded

#### FAC-24-H2
- **Given** match succeeds
- **When** I authorize payment
- **Then** authorization stored

#### FAC-24-H3
- **Given** period close
- **When** I generate valuation snapshot
- **Then** quantities/values available for recon

#### FAC-24-H4
- **Given** operational vs finance variance
- **When** I reconcile and sign off
- **Then** status finalized with audit

### 2. Validation Scenarios

#### FAC-24-V1
- **Given** invoice lines don't reference PO
- **When** I register
- **Then** validation fails

#### FAC-24-V2
- **Given** authorize payment before match
- **When** I authorize
- **Then** blocked

### 3. Error Scenarios

#### FAC-24-E1
- **Given** qty mismatch PO/GR/invoice
- **When** I match
- **Then** fail with detailed differences

#### FAC-24-E2
- **Given** consignment not owned
- **When** valuation treats correctly
- **Then** not counted as owned until ownership transfer

### 4. Permission Scenarios

#### FAC-24-P1
- **Given** I lack FINANCE_INVOICE / RECONCILE
- **When** I match or sign off
- **Then** denied

#### FAC-24-P2
- **Given** I am an Ops user without finance roles
- **When** I open valuation
- **Then** read-only or denied per role

### 5. Edge Cases

#### FAC-24-X1
- **Given** partial GR vs invoice
- **When** match
- **Then** partial match states supported

#### FAC-24-X2
- **Given** re-open closed period requires elevated auth
- **When** I attempt
- **Then** denied or special override audited


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-075, US-089 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-24-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-24*
