# Implementation Plan — F-22: Inventory Reporting & Dashboards

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-22 |
| **Feature Name** | Inventory Reporting & Dashboards |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-13 Inventory Intelligence |
| **Required previous features** | `F-04` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Operational dashboard and reports for stock health, movements, stockouts, accuracy, and location performance.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Give leaders inventory visibility without manual compilation (BO-01, BO-04).

---

## 3. User Stories

- US-068
- US-069
- US-070
- US-072
- US-074

Primary story references: **US-068, US-069, US-070, US-072, US-074** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-068–070 MVP reports
- AC-072 location P2
- AC-074 replenishment reporting

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `Projections / optional reporting views` |  |

### Relationships

- Read-only joins across modules by identity

### Constraints

- Location-scope filtering on all queries

### Migration Tasks (Flyway)

- V1_90__intelligence_views.sql (optional)

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- None (query services)

### Value Objects
- DashboardKpi
- MovementReportRow
- StockoutRow

### Repositories
- DashboardQueryRepository
- MovementQueryRepository

### DTOs (application/API layer)
**Request:** `ReportFilterQuery`, `DateRangeQuery`  
**Response:** `DashboardResponse`, `StockStatusSummaryResponse`, `MovementReportResponse`, `CountPerformanceResponse`

### Validation
- date range
- authorized locations

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- DashboardService
- OperationalReportService

### Controllers
- IntelligenceDashboardController
- IntelligenceReportController

### Exception Handling
- UnauthorizedReportScopeException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['REPORT_VIEW', 'DASHBOARD_VIEW']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- home/operations
- reports/operational

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- OperationalDashboardPage (UI-002)
- OperationalReportsPage (UI-044)

### Components
- KpiSummaryCard
- StockHealthPanel
- ReportFilterBar
- ExportButton

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- DashboardVm
- ReportRowVm

### Services
- DashboardApiService
- ReportsFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- ReportFilterForm

### Validation
- date range

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['dashboard widgets, report results']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-150–152
- API-154–155
- API-167–168

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- ReportFilterQuery
- DateRangeQuery

### Response DTOs
- DashboardResponse
- StockStatusSummaryResponse
- MovementReportResponse
- CountPerformanceResponse

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
- KPI cards match underlying APIs
- export

### API Tests
- API-150–152, 155

### UI Tests
- UI-002/044

---

## 10. Dependencies

### Required features
`F-04`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-22`.

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

*Generated for Technical Lead delivery planning — F-22*
