# Acceptance Criteria — F-27: User Access & Role Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-27 |
| **Feature Name** | User Access & Role Management |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-081, US-082, US-085 |
| **Primary roles** | IMS Administrator, Ops Director |
| **Format** | Given / When / Then |
| **Criteria count** | 16 (H4 / V3 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-27** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-27-H1
- **Given** valid credentials for active user
- **When** I sign in
- **Then** session established with roles and location scope

#### FAC-27-H2
- **Given** I create a user and assign roles/locations
- **When** user activates
- **Then** user can access permitted functions only

#### FAC-27-H3
- **Given** I suspend or deactivate a user
- **When** user attempts login
- **Then** access blocked

#### FAC-27-H4
- **Given** I sign out
- **When** session ends
- **Then** protected routes require login again

### 2. Validation Scenarios

#### FAC-27-V1
- **Given** missing username/password
- **When** I sign in
- **Then** validation fails

#### FAC-27-V2
- **Given** assign unknown role code
- **When** I assign
- **Then** validation fails

#### FAC-27-V3
- **Given** user without location scope where required
- **When** I save
- **Then** validation fails or warns per policy

### 3. Error Scenarios

#### FAC-27-E1
- **Given** invalid credentials
- **When** I sign in
- **Then** 401 with generic message (no user enumeration)

#### FAC-27-E2
- **Given** suspended user
- **When** I sign in
- **Then** denied with suspended reason

#### FAC-27-E3
- **Given** expired/invalid token
- **When** I call API
- **Then** 401

### 4. Permission Scenarios

#### FAC-27-P1
- **Given** non-admin
- **When** I open user admin
- **Then** denied

#### FAC-27-P2
- **Given** admin cannot assign roles above policy without elevated right
- **When** I assign
- **Then** denied

#### FAC-27-P3
- **Given** user cannot escalate own permissions
- **When** I self-assign ADMIN
- **Then** denied

### 5. Edge Cases

#### FAC-27-X1
- **Given** IdP sync updates roles
- **When** sync runs
- **Then** local assignments reconcile per sync rules

#### FAC-27-X2
- **Given** remember-session optional
- **When** I check remember
- **Then** session duration follows policy

#### FAC-27-X3
- **Given** concurrent sessions
- **When** logout-all if supported
- **Then** other sessions invalidated per design


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-081, US-082, US-085 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-27-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-27*
