# Implementation Plan — F-25: Promotional & Launch Stock Readiness

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-25 |
| **Feature Name** | Promotional & Launch Stock Readiness |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-11 Commercial Campaign |
| **Required previous features** | `F-04`, `F-10`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Allocate and ring-fence promotional stock; assess campaign readiness.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Ensure campaign/launch coverage without draining general ATP (deferred Phase 3).

---

## 3. User Stories

- US-057
- US-080

Primary story references: **US-057, US-080** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-057 readiness
- AC-080 campaign alerts

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `commercial.promotional_stock_allocations` | Allocations |
| `commercial.promotional_allocation_locations` | Per-location ring-fence |

### Relationships

- allocation → sku; locations child; may call stock segregation

### Constraints

- ring-fence qty <= ATP; override auditable

### Migration Tasks (Flyway)

- V3_30__commercial_allocations.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- PromotionalStockAllocation (AR)

### Value Objects
- CampaignId
- RingFenceQuantity
- ReadinessStatus

### Repositories
- PromotionalAllocationRepository

### DTOs (application/API layer)
**Request:** `CreateAllocationRequest`, `UpdateAllocationRequest`, `ReadinessCheckRequest`, `ReleaseAllocationRequest`, `OverrideAllocationRequest`  
**Response:** `AllocationResponse`, `ReadinessResponse`, `RingFenceResponse`

### Validation
- targets
- override authority

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- CampaignAllocationService
- ReadinessService

### Controllers
- CampaignController

### Exception Handling
- InsufficientAtpForRingFenceException
- OverrideNotAuthorizedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['CAMPAIGN_MANAGE', 'CAMPAIGN_OVERRIDE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- reports/promotional-readiness

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- PromotionalStockReadinessPage (UI-046)

### Components
- AllocationForm
- ReadinessGauge
- RingFenceTable

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- AllocationVm
- ReadinessVm

### Services
- CampaignApiService
- CampaignFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- AllocationForm
- OverrideForm

### Validation
- target qty > 0

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['allocations, readiness']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-132–139
- API-048
- API-169
- API-178

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateAllocationRequest
- UpdateAllocationRequest
- ReadinessCheckRequest
- ReleaseAllocationRequest
- OverrideAllocationRequest

### Response DTOs
- AllocationResponse
- ReadinessResponse
- RingFenceResponse

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
- ring-fence reduces general ATP

### API Tests
- API-132–139, 169

### UI Tests
- UI-046

---

## 10. Dependencies

### Required features
`F-04`, `F-10`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-25`.

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

*Generated for Technical Lead delivery planning — F-25*
