# Acceptance Criteria — F-22: Inventory Reporting & Dashboards

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-22 |
| **Feature Name** | Inventory Reporting & Dashboards |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-068, US-069, US-070, US-072, US-074 |
| **Primary roles** | Ops Director, COO, Inventory Controller, Warehouse Manager, Purchasing |
| **Format** | Given / When / Then |
| **Criteria count** | 14 (H5 / V2 / E2 / P3 / X2) |

---

## Purpose

Define testable acceptance criteria for **F-22** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-22-H1
- **Given** operational data exists
- **When** I open operational dashboard
- **Then** KPIs/stock health/alerts/tasks load for my scope

#### FAC-22-H2
- **Given** I run movement report for a period
- **When** filters applied
- **Then** movements by type/product/location returned

#### FAC-22-H3
- **Given** stockouts/overstocks exist
- **When** I run stock health report
- **Then** items listed with status

#### FAC-22-H4
- **Given** counts/variances exist
- **When** I run accuracy report
- **Then** accuracy metrics display

#### FAC-22-H5
- **Given** Phase 2 location performance
- **When** I open location snapshot
- **Then** per-location metrics shown

### 2. Validation Scenarios

#### FAC-22-V1
- **Given** invalid date range
- **When** I run report
- **Then** validation fails

#### FAC-22-V2
- **Given** export without required filters
- **When** I export
- **Then** validation fails

### 3. Error Scenarios

#### FAC-22-E1
- **Given** report API timeout
- **When** I load dashboard
- **Then** error state per widget, not blank fake zeros without indicator

#### FAC-22-E2
- **Given** no data in period
- **When** I run
- **Then** empty successful result

### 4. Permission Scenarios

#### FAC-22-P1
- **Given** I lack DASHBOARD_VIEW / REPORT_VIEW
- **When** I open
- **Then** denied

#### FAC-22-P2
- **Given** scoped user
- **When** I view dashboard
- **Then** only scoped locations

#### FAC-22-P3
- **Given** executive-only widgets
- **When** warehouse user
- **Then** does not see exec-only tiles

### 5. Edge Cases

#### FAC-22-X1
- **Given** drill-down from KPI
- **When** I click stockout card
- **Then** navigates to filtered status monitor

#### FAC-22-X2
- **Given** refresh
- **When** I refresh
- **Then** data reloads with timestamp


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-068, US-069, US-070, US-072, US-074 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-22-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-22*
