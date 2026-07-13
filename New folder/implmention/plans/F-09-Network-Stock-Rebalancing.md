# Implementation Plan — F-09: Network Stock Rebalancing

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-09 |
| **Feature Name** | Network Stock Rebalancing |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-13 Inventory Intelligence |
| **Required previous features** | `F-04`, `F-08`, `F-20` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Analyze network imbalance and recommend redistribution convertible to transfer requests.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Optimize enterprise stock distribution (Phase 3 / deferred).

---

## 3. User Stories

- US-062

Primary story references: **US-062** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-062-* imbalance analysis and recommendation → transfer

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `Read models over inventory.stock_positions + stock_policies` | No dedicated write tables |

### Relationships

- Recommendations create transfer.transfer_requests

### Constraints

- Recommendations must respect source minimums

### Migration Tasks (Flyway)

- Optional V3_01__rebalance_recommendation_cache.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- None (query service); may use recommendation DTO aggregate

### Value Objects
- ImbalanceScore
- RebalanceRecommendation

### Repositories
- NetworkImbalanceQueryRepository

### DTOs (application/API layer)
**Request:** `RebalanceAnalysisQuery`  
**Response:** `NetworkImbalanceResponse`, `RebalanceRecommendationResponse`

### Validation
- sku/location filters

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- NetworkRebalancingService

### Controllers
- NetworkIntelligenceController

### Exception Handling
- InsufficientDataForRebalanceException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['NETWORK_REBALANCE_VIEW', 'TRANSFER_REQUEST to act']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- transfers/network-rebalancing

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- NetworkRebalancingAnalysisPage (UI-041)

### Components
- ImbalanceHeatmap
- RecommendationTable
- ConvertToTransferAction

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- ImbalanceVm
- RecommendationVm

### Services
- RebalanceApiService
- RebalanceFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- RebalanceFilterForm

### Validation
- date/network filters

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['analysis results, selected recommendations']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-036
- API-160
- API-166

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- RebalanceAnalysisQuery

### Response DTOs
- NetworkImbalanceResponse
- RebalanceRecommendationResponse

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
- Recommendation respects BR-012

### API Tests
- API-166

### UI Tests
- UI-041 convert to transfer

---

## 10. Dependencies

### Required features
`F-04`, `F-08`, `F-20`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-09`.

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

*Generated for Technical Lead delivery planning — F-09*
