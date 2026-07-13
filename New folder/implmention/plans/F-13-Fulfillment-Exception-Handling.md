# Implementation Plan — F-13: Fulfillment Exception Handling

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-13 |
| **Feature Name** | Fulfillment Exception Handling |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-07 + M-04 quarantine + M-13 alerts |
| **Required previous features** | `F-11`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Resolve pick failures, damage, cancellations, and optional substitutions; raise exception alerts.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Minimize customer impact and correct inventory when outbound breaks (BO-06).

---

## 3. User Stories

- US-047
- US-050
- US-078

Primary story references: **US-047, US-050, US-078** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-047 exceptions P2
- AC-050 substitution P3
- AC-078 alerts

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `Fulfillment exception fields / table` | Optional fulfillment.exceptions |
| `inventory.quarantine_holds` | Damage holds |

### Relationships

- exception → order; may create quarantine hold

### Constraints

- reason required; substitution requires approval

### Migration Tasks (Flyway)

- V2_20__fulfillment_exceptions.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- FulfillmentException
- CustomerOrderFulfillment

### Value Objects
- ExceptionType
- SubstitutionApproval

### Repositories
- FulfillmentExceptionRepository

### DTOs (application/API layer)
**Request:** `CreateFulfillmentExceptionRequest`, `ResolveExceptionRequest`, `SubstitutionRequest`  
**Response:** `ExceptionResponse`, `ExceptionBoardResponse`

### Validation
- reason code
- SoD for substitution

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- FulfillmentExceptionService

### Controllers
- FulfillmentExceptionController

### Exception Handling
- ExceptionAlreadyResolvedException
- SubstitutionNotAuthorizedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['FULFILL_EXCEPTION_MANAGE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- fulfillment/exceptions

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- FulfillmentExceptionManagementPage (UI-033)

### Components
- ExceptionQueue
- ResolveExceptionForm
- SubstitutionPanel

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- FulfillmentExceptionVm

### Services
- ExceptionApiService
- ExceptionFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- ExceptionForm
- ResolveForm

### Validation
- reason required

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['exception queue']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-096
- API-165
- API-045

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateFulfillmentExceptionRequest
- ResolveExceptionRequest
- SubstitutionRequest

### Response DTOs
- ExceptionResponse
- ExceptionBoardResponse

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
- damage → quarantine
- alert raised

### API Tests
- API-096, 165

### UI Tests
- UI-033

---

## 10. Dependencies

### Required features
`F-11`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-13`.

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

*Generated for Technical Lead delivery planning — F-13*
