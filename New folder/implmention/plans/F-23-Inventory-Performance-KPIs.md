# Implementation Plan — F-23: Inventory Performance KPIs

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-23 |
| **Feature Name** | Inventory Performance KPIs |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-13 |
| **Required previous features** | `F-11`, `F-04`, `F-14`, `F-22` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Executive KPI dashboard for fill rate, turnover, days of supply, accuracy vs targets.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Track strategic inventory maturity (BO-18).

---

## 3. User Stories

- US-073

Primary story references: **US-073** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-073-* KPI calc, trends, targets

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `Optional audit/reporting KPI snapshot tables` |  |

### Relationships

- Derived from fulfillment, inventory, accuracy

### Constraints

- Read-only

### Migration Tasks (Flyway)

- V3_10__kpi_snapshots.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- None

### Value Objects
- KpiValue
- KpiTarget
- TrendPoint

### Repositories
- KpiQueryRepository

### DTOs (application/API layer)
**Request:** `KpiQuery`  
**Response:** `KpiDashboardResponse`

### Validation
- period required

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- KpiService

### Controllers
- KpiController

### Exception Handling
- KpiDataUnavailableException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['KPI_VIEW_EXEC']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- reports/executive-kpis

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- ExecutiveKpiDashboardPage (UI-003)

### Components
- KpiTrendChart
- TargetComparison
- DrilldownLink

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- KpiVm

### Services
- KpiApiService
- KpiFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- KpiPeriodForm

### Validation
- period

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['selected period, kpi set']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-170

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- KpiQuery

### Response DTOs
- KpiDashboardResponse

### Error Responses

| HTTP | Category | Typical `errorCode` prefix |
|------|----------|---------------------------|
| 400 | validation-error | `VAL_*` |
| 401 | authentication-error | `AUTH_*` |
| 403 | authorization-error | `AUTHZ_*` |
| 404 | not-found | `NOT_FOUND_*` |
| 409 | conflict | `CONFLICT_*` |
| 422 | business-rule-violation | `BIZ_*` / `BR-*` |
| 500 | internal-server-error | `SYS_*` |

Envelope: RFC 7807 `ProblemDetailResponse` (`type`, `title`, `status`, `detail`, `instance`, `errorCode`, `traceId`, `timestamp`, optional `errors[]`).


---

## 9. QA Tasks

### Functional Tests
- fill rate matches shipped/ordered

### API Tests
- API-170

### UI Tests
- UI-003

---

## 10. Dependencies

### Required features
`F-11`, `F-04`, `F-14`, `F-22`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-23`.

### Implementation sequence hint
Follow IMPL-DEP-001 optimal order; do not start UI polish before HTTP facade + auth for this module.

---

## 11. Definition of Done (Feature)

- [ ] Flyway migrations applied in CI
- [ ] Domain invariants covered by unit tests
- [ ] All listed APIs implemented + OpenAPI updated
- [ ] Angular routes/pages/facades wired (no mock-only)
- [ ] RBAC + location scope verified
- [ ] AC happy/validation/error/edge sampled in UAT pack
- [ ] Audit/movement side-effects verified (if mutating)
- [ ] Feature flagged or released per wave plan

---

*Generated for Technical Lead delivery planning — F-23*
