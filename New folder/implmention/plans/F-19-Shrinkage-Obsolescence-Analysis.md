# Implementation Plan — F-19: Shrinkage & Obsolescence Analysis

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-19 |
| **Feature Name** | Shrinkage & Obsolescence Analysis |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-13 Inventory Intelligence |
| **Required previous features** | `F-17`, `F-04` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Analyze reason-coded loss trends and identify slow-moving/obsolete stock.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Drive loss prevention and working-capital recovery (BO-02).

---

## 3. User Stories

- US-039
- US-040

Primary story references: **US-039, US-040** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-039 shrinkage P2
- AC-040 obsolescence P3

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `Read: stock_adjustments, write_offs, movements, stock_positions` |  |

### Relationships

- Aggregation by reason_code, location, sku

### Constraints

- Read-only; no mutations

### Migration Tasks (Flyway)

- Optional materialized view V2_30__shrinkage_mv.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- None (query)

### Value Objects
- ShrinkageMetric
- ObsolescenceCandidate

### Repositories
- ShrinkageQueryRepository

### DTOs (application/API layer)
**Request:** `ShrinkageAnalysisQuery`, `DateRangeQuery`  
**Response:** `ShrinkageAnalysisResponse`

### Validation
- date range VR-062

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- ShrinkageAnalysisService

### Controllers
- AccuracyIntelligenceController

### Exception Handling
- InvalidDateRangeException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['SHRINKAGE_VIEW']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inventory/shrinkage-obsolescence

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- ShrinkageLossObsolescencePage (UI-029)

### Components
- ShrinkageChart
- ReasonBreakdownTable
- ObsoleteStockList

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- ShrinkageVm

### Services
- ShrinkageApiService
- ShrinkageFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- AnalysisFilterForm

### Validation
- start <= end

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['filters, chart data']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-167

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- ShrinkageAnalysisQuery
- DateRangeQuery

### Response DTOs
- ShrinkageAnalysisResponse

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
- totals match adjustments by reason

### API Tests
- API-167

### UI Tests
- UI-029

---

## 10. Dependencies

### Required features
`F-17`, `F-04`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-19`.

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

*Generated for Technical Lead delivery planning — F-19*
