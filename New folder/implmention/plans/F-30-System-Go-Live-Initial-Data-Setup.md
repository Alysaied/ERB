# Implementation Plan — F-30: System Go-Live & Initial Data Setup

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-30 |
| **Feature Name** | System Go-Live & Initial Data Setup |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-01 + M-04 + M-02 |
| **Required previous features** | `F-01`, `F-02`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Controlled bulk import of products and opening balances with validation and activation gates.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Enable practical go-live without embedding bad opening data (BO-01, BO-21).

---

## 3. User Stories

- US-090

Primary story references: **US-090** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-090-* upload, validate, review errors, approve, activate location

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `Staging import tables optional` | import_batches / import_errors |
| `catalog.products` | Bulk upsert |
| `inventory.stock_positions` | Opening balances |

### Relationships

- import batch → rows; activation requires approved openings

### Constraints

- opening qty >= 0; SKU must resolve; dual control approve

### Migration Tasks (Flyway)

- V1_95__import_batches.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- ImportBatch
- Product
- StockPosition opening

### Value Objects
- ImportRowResult
- OpeningBalance

### Repositories
- ImportBatchRepository
- OpeningBalanceRepository

### DTOs (application/API layer)
**Request:** `ProductImportRequest (multipart)`, `OpeningBalanceRequest`, `ActivateLocationRequest`  
**Response:** `ImportResultResponse`, `OpeningBalanceResultResponse`, `ActivationResultResponse`

### Validation
- file schema
- duplicate SKUs in file
- opening balance substantiation

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- ProductImportService
- OpeningBalanceService
- GoLiveActivationService

### Controllers
- ProductImportController
- OpeningBalanceController

### Exception Handling
- ImportValidationException
- OpeningBalanceNotApprovedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['DATA_IMPORT', 'OPENING_BALANCE_APPROVE', 'LOCATION_ACTIVATE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- products/import

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- ProductImportWorkspacePage (UI-006)

### Components
- UploadDropzone
- ValidationErrorTable
- ImportProgress
- ActivationChecklist

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- ImportBatchVm
- ImportErrorVm

### Services
- ImportApiService
- ImportFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- UploadForm
- ApproveImportForm

### Validation
- file type/size
- confirm approve

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['batch status, errors, approval step']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-010
- API-032
- API-017

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- ProductImportRequest (multipart)
- OpeningBalanceRequest
- ActivateLocationRequest

### Response DTOs
- ImportResultResponse
- OpeningBalanceResultResponse
- ActivationResultResponse

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
- invalid rows blocked
- activation blocked until openings approved

### API Tests
- API-010/032/017

### UI Tests
- UI-006 wizard

---

## 10. Dependencies

### Required features
`F-01`, `F-02`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-30`.

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

*Generated for Technical Lead delivery planning — F-30*
