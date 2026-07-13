# Implementation Plan — F-21: Returns Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-21 |
| **Feature Name** | Returns Management |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-10 Returns Management |
| **Required previous features** | `F-10`, `F-11`, `F-05`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Return authorization, receive/inspect returned goods, and disposition to restock, quarantine, or write-off.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Track returns accurately without contaminating sellable stock (BO-06, BR-26).

---

## 3. User Stories

- US-064
- US-065
- US-066
- US-067

Primary story references: **US-064, US-065, US-066, US-067** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-064–067 full returns Phase 2

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `returns.return_authorizations (+ lines)` | RA |
| `returns.customer_returns (+ lines)` | Physical return |
| `returns.return_dispositions` | Disposition |

### Relationships

- RA → original order; return → RA; disposition → return

### Constraints

- chk_domain_disposition_decision; eligibility vs original order

### Migration Tasks (Flyway)

- V2_40__returns_schema.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- CustomerReturnCase (AR)
- ReturnAuthorization
- ReturnDisposition

### Value Objects
- ReturnEligibility
- InspectionResult
- DispositionDecision

### Repositories
- ReturnAuthorizationRepository
- CustomerReturnRepository

### DTOs (application/API layer)
**Request:** `CreateReturnAuthorizationRequest`, `CancelReturnAuthorizationRequest`, `ReceiveReturnRequest`, `InspectReturnRequest`, `DispositionReturnRequest`  
**Response:** `ReturnAuthorizationResponse`, `ReturnResponse`, `PendingReturnReceiptResponse`

### Validation
- order linkage
- qty <= shipped
- inspection before disposition

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- ReturnAuthorizationService
- ReturnInspectionService

### Controllers
- ReturnsController

### Exception Handling
- ReturnNotEligibleException
- DispositionInvalidException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['RETURN_AUTHORIZE', 'RETURN_RECEIVE', 'RETURN_DISPOSITION']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- returns/authorizations
- returns/inspection-disposition

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- ReturnAuthorizationPage (UI-042)
- ReturnInspectionDispositionPage (UI-043)

### Components
- RaForm
- PendingReturnsQueue
- InspectionForm
- DispositionActions

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- ReturnAuthorizationVm
- ReturnVm

### Services
- ReturnsApiService
- ReturnsFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- RaForm
- InspectForm
- DispositionForm

### Validation
- order required
- disposition reason

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['RA list, pending receipts']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-124–131
- API-076 alternate; prefer API-128 C-04

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateReturnAuthorizationRequest
- CancelReturnAuthorizationRequest
- ReceiveReturnRequest
- InspectReturnRequest
- DispositionReturnRequest

### Response DTOs
- ReturnAuthorizationResponse
- ReturnResponse
- PendingReturnReceiptResponse

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
- restock increases ATP; write-off path

### API Tests
- API-124–131

### UI Tests
- UI-042/043

---

## 10. Dependencies

### Required features
`F-10`, `F-11`, `F-05`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-21`.

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

*Generated for Technical Lead delivery planning — F-21*
