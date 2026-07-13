# Implementation Plan — F-18: Quarantine & Hold Stock Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-18 |
| **Feature Name** | Quarantine & Hold Stock Management |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-04 Inventory Balance |
| **Required previous features** | `F-04`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Apply and release quarantine/hold so non-sellable qty is excluded from ATP.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Prevent shipping defective or uninspected goods (BO-06).

---

## 3. User Stories

- US-038

Primary story references: **US-038** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-038-* apply/release hold; ATP exclusion; register visibility

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `inventory.quarantine_holds` | Holds |

### Relationships

- hold → stock_position

### Constraints

- chk_domain_hold_type; qty <= on_hand - reserved

### Migration Tasks (Flyway)

- Already in V1_31; add indexes for register queries

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- StockPosition
- QuarantineHold

### Value Objects
- HoldReasonClassification
- HoldType

### Repositories
- QuarantineHoldRepository

### DTOs (application/API layer)
**Request:** `ApplyQuarantineHoldRequest`, `ReleaseQuarantineHoldRequest`  
**Response:** `QuarantineHoldResponse`, `QuarantineRegisterResponse`

### Validation
- reason/type required
- qty available

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- QuarantineHoldService

### Controllers
- QuarantineController
- IntelligenceQuarantineController

### Exception Handling
- InsufficientQtyForHoldException
- HoldNotFoundException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['QUARANTINE_MANAGE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inventory/quarantine

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- QuarantineHoldRegisterPage (UI-028)

### Components
- HoldForm
- QuarantineRegisterTable
- ReleaseAction

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- QuarantineHoldVm

### Services
- QuarantineApiService
- QuarantineFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- ApplyHoldForm
- ReleaseHoldForm

### Validation
- qty > 0
- reason required

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['register filters']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-045
- API-046
- API-154

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- ApplyQuarantineHoldRequest
- ReleaseQuarantineHoldRequest

### Response DTOs
- QuarantineHoldResponse
- QuarantineRegisterResponse

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
- ATP drops on hold; restores on release

### API Tests
- API-045/046/154

### UI Tests
- UI-028

---

## 10. Dependencies

### Required features
`F-04`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-18`.

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

*Generated for Technical Lead delivery planning — F-18*
