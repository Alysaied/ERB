# Acceptance Criteria — F-30: System Go-Live & Initial Data Setup

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-30 |
| **Feature Name** | System Go-Live & Initial Data Setup |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-090 |
| **Primary roles** | Inventory Controller, Ops Director, IMS Administrator |
| **Format** | Given / When / Then |
| **Criteria count** | 16 (H3 / V4 / E3 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-30** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-30-H1
- **Given** I upload a valid product import file
- **When** validation passes
- **Then** products created/updated in reviewable batch

#### FAC-30-H2
- **Given** I load verified opening balances
- **When** approver approves
- **Then** stock positions established

#### FAC-30-H3
- **Given** openings approved
- **When** I activate location
- **Then** location becomes operational

### 2. Validation Scenarios

#### FAC-30-V1
- **Given** file missing required columns
- **When** I upload
- **Then** validation errors per row/column

#### FAC-30-V2
- **Given** duplicate SKUs inside file
- **When** I upload
- **Then** rows flagged; batch not activated blindly

#### FAC-30-V3
- **Given** opening qty negative
- **When** I load
- **Then** rejected

#### FAC-30-V4
- **Given** activate without approved openings when required
- **When** I activate
- **Then** blocked

### 3. Error Scenarios

#### FAC-30-E1
- **Given** partial failure mid-import
- **When** I upload
- **Then** failed rows reported; no silent partial publish without report

#### FAC-30-E2
- **Given** SKU in openings missing from catalog
- **When** I load openings
- **Then** row errors; no orphan stock

#### FAC-30-E3
- **Given** approve already-activated batch incorrectly
- **When** I re-run
- **Then** idempotent/guarded behavior

### 4. Permission Scenarios

#### FAC-30-P1
- **Given** I lack DATA_IMPORT
- **When** I upload
- **Then** denied

#### FAC-30-P2
- **Given** I lack OPENING_BALANCE_APPROVE
- **When** I approve openings
- **Then** denied

#### FAC-30-P3
- **Given** importer cannot self-approve openings if SoD required
- **When** same user approves
- **Then** blocked

### 5. Edge Cases

#### FAC-30-X1
- **Given** re-import updates existing SKUs
- **When** I import
- **Then** updates applied per upsert rules with audit

#### FAC-30-X2
- **Given** dry-run/validate-only
- **When** I validate without commit
- **Then** errors shown; DB unchanged

#### FAC-30-X3
- **Given** production cutover after UAT
- **When** I load production openings
- **Then** uses same controls as test with dual control


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-090 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-30-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-30*
