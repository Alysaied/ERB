# Acceptance Criteria — F-28: Operational Accountability & Controls

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-28 |
| **Feature Name** | Operational Accountability & Controls |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-083, US-084 |
| **Primary roles** | All users (enforced); Admin/Auditor configure |
| **Format** | Given / When / Then |
| **Criteria count** | 10 (H3 / V1 / E2 / P2 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-28** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-28-H1
- **Given** I perform a material action (adjust/approve/receive)
- **When** action completes
- **Then** activity/audit record captures user, action, entity, timestamp

#### FAC-28-H2
- **Given** initiator and approver are different authorized users
- **When** approval proceeds
- **Then** SoD evaluation passes

#### FAC-28-H3
- **Given** conflicting roles on one user
- **When** user attempts conflicting action pair
- **Then** blocked by SoD policy

### 2. Validation Scenarios

#### FAC-28-V1
- **Given** SoD evaluate missing actor/action
- **When** I call evaluate
- **Then** validation fails

### 3. Error Scenarios

#### FAC-28-E1
- **Given** same user initiates and approves
- **When** I approve
- **Then** SoD violation 422/403

#### FAC-28-E2
- **Given** location scope mismatch on action
- **When** I act on out-of-scope location
- **Then** blocked

### 4. Permission Scenarios

#### FAC-28-P1
- **Given** user with only submit rights
- **When** I approve
- **Then** denied

#### FAC-28-P2
- **Given** auditor can view activity but not approve inventory
- **When** I approve adjustment
- **Then** denied

### 5. Edge Cases

#### FAC-28-X1
- **Given** break-glass emergency override exists
- **When** override used
- **Then** requires elevated role and is heavily audited

#### FAC-28-X2
- **Given** read-only views
- **When** I view stock
- **Then** may log access if policy requires; no SoD on reads


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-083, US-084 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-28-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-28*
