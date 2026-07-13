# Acceptance Criteria — F-16: Count Variance Investigation & Approval

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-16 |
| **Feature Name** | Count Variance Investigation & Approval |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-033, US-034, US-037 |
| **Primary roles** | Inventory Controller, Warehouse Manager, Ops Director |
| **Format** | Given / When / Then |
| **Criteria count** | 12 (H3 / V2 / E2 / P3 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-16** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-16-H1
- **Given** count results differ from system
- **When** variances appear in case
- **Then** classified vs tolerance

#### FAC-16-H2
- **Given** I investigate with findings
- **When** independent approver approves
- **Then** adjustment posts to stock

#### FAC-16-H3
- **Given** variance above threshold
- **When** routing sends to elevated approver
- **Then** approval by correct role required

### 2. Validation Scenarios

#### FAC-16-V1
- **Given** approve without investigation findings when required
- **When** I approve
- **Then** blocked

#### FAC-16-V2
- **Given** reject without reason
- **When** I reject
- **Then** validation fails

### 3. Error Scenarios

#### FAC-16-E1
- **Given** counter approves own count
- **When** I approve
- **Then** SoD violation blocked

#### FAC-16-E2
- **Given** approve already approved case
- **When** I approve again
- **Then** rejected

### 4. Permission Scenarios

#### FAC-16-P1
- **Given** I lack VARIANCE_INVESTIGATE
- **When** I add findings
- **Then** denied

#### FAC-16-P2
- **Given** I lack VARIANCE_APPROVE
- **When** I approve
- **Then** denied

#### FAC-16-P3
- **Given** threshold requires Finance
- **When** Ops Director approves high-value write-down
- **Then** blocked until Finance

### 5. Edge Cases

#### FAC-16-X1
- **Given** within tolerance auto-classify
- **When** case created
- **Then** may auto-route to simplified path per policy

#### FAC-16-X2
- **Given** pending approval notification
- **When** approver subscribed
- **Then** F-26 alert created


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-033, US-034, US-037 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-16-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-16*
