# Acceptance Criteria — F-29: Audit Trail & Compliance

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-29 |
| **Feature Name** | Audit Trail & Compliance |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-086, US-087, US-088 |
| **Primary roles** | Internal/External Auditor, Finance, Ops Director |
| **Format** | Given / When / Then |
| **Criteria count** | 12 (H3 / V2 / E2 / P3 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-29** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-29-H1
- **Given** inventory qty changed via any mutator
- **When** I query movements/audit
- **Then** immutable record exists with before/after where applicable

#### FAC-29-H2
- **Given** I filter audit by entity/user/date (Phase 2)
- **When** results return
- **Then** export available within limits

#### FAC-29-H3
- **Given** control breach detected (Phase 2)
- **When** breach recorded
- **Then** visible in audit workspace

### 2. Validation Scenarios

#### FAC-29-V1
- **Given** query without mandatory filters on large dataset
- **When** I search
- **Then** validation requires narrowed scope

#### FAC-29-V2
- **Given** export exceeds size limit
- **When** I export
- **Then** rejected or async job required

### 3. Error Scenarios

#### FAC-29-E1
- **Given** attempt to update/delete audit row via API
- **When** I call update
- **Then** not allowed / 405/404

#### FAC-29-E2
- **Given** unauthorized export
- **When** I export
- **Then** denied

### 4. Permission Scenarios

#### FAC-29-P1
- **Given** I lack AUDIT_VIEW
- **When** I open audit trail
- **Then** denied

#### FAC-29-P2
- **Given** I lack AUDIT_EXPORT
- **When** I export
- **Then** denied

#### FAC-29-P3
- **Given** warehouse operator
- **When** I open auditor workspace
- **Then** denied

### 5. Edge Cases

#### FAC-29-X1
- **Given** high-volume day
- **When** I query
- **Then** pagination performs within NFR

#### FAC-29-X2
- **Given** movement and audit both exist for same event
- **When** I correlate via trace/entity ids
- **Then** consistent story


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-086, US-087, US-088 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-29-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-29*
