# Implementation Plan — F-15: Full Physical Inventory Count

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-15 |
| **Feature Name** | Full Physical Inventory Count |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-09 Inventory Accuracy |
| **Required previous features** | `F-02`, `F-04`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Wall-to-wall counts with location freeze, progress, and certification.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Establish verified baselines and financial substantiation (BO-02, BO-07).

---

## 3. User Stories

- US-032

Primary story references: **US-032** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-032-* freeze, capture, certify, variance reporting

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `accuracy.physical_inventory_counts` | Physical count |
| `network.inventory_locations.freeze` | Freeze flag |

### Relationships

- physical count → location

### Constraints

- freeze blocks receive/ship/transfer/adjust except count posts

### Migration Tasks (Flyway)

- V1_71__physical_inventory_counts.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- PhysicalInventoryCount (AR)
- InventoryLocation freeze

### Value Objects
- FreezeStatus
- CertificationRecord

### Repositories
- PhysicalCountRepository

### DTOs (application/API layer)
**Request:** `CreatePhysicalCountRequest`, `SubmitPhysicalCountResultsRequest`, `CertifyPhysicalCountRequest`  
**Response:** `PhysicalCountResponse`, `FreezeStatusResponse`

### Validation
- all zones complete before certify

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- PhysicalInventoryCountService
- LocationFreezeService

### Controllers
- PhysicalCountController

### Exception Handling
- LocationFreezeActiveException
- PhysicalCountIncompleteException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['PHYSICAL_COUNT_MANAGE', 'PHYSICAL_COUNT_CERTIFY']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inventory/physical-counts
- inventory/physical-counts/:id

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- PhysicalInventoryCountPage (UI-024)

### Components
- FreezeBanner
- CountProgress
- CertifyPanel

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- PhysicalCountVm

### Services
- PhysicalCountApiService
- PhysicalCountFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- PhysicalCountResultForm
- CertifyForm

### Validation
- completion checklist

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['active count, freeze flag']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-020
- API-112–115
- API-168

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreatePhysicalCountRequest
- SubmitPhysicalCountResultsRequest
- CertifyPhysicalCountRequest

### Response DTOs
- PhysicalCountResponse
- FreezeStatusResponse

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
- transactions blocked while frozen

### API Tests
- API-112–115, 020

### UI Tests
- UI-024

---

## 10. Dependencies

### Required features
`F-02`, `F-04`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-15`.

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

*Generated for Technical Lead delivery planning — F-15*
