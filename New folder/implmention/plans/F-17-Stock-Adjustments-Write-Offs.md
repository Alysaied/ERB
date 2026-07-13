# Implementation Plan — F-17: Stock Adjustments & Write-Offs

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-17 |
| **Feature Name** | Stock Adjustments & Write-Offs |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-09 + M-03 |
| **Required previous features** | `F-03`, `F-04`, `F-28`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Reason-coded stock adjustments and write-offs with approval workflow and audit trail.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Correct inventory with accountability for damage, shrinkage, obsolescence, and data errors (BO-02, BO-19).

---

## 3. User Stories

- US-011
- US-035
- US-036
- US-077

Primary story references: **US-011, US-035, US-036, US-077** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-011 reason codes
- AC-035 adjustments
- AC-036 write-offs
- AC-077 approval notifications

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `accuracy.stock_adjustments` | Adjustments |
| `accuracy.inventory_write_offs` | Write-offs |
| `governance.reason_codes` | Required codes |

### Relationships

- adjustment case → stock position identity; reason_code FK

### Constraints

- reason required BR-020
- approval status chk
- qty rules

### Migration Tasks (Flyway)

- V1_73__stock_adjustments_write_offs.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- InventoryAdjustmentCase
- StockAdjustment
- InventoryWriteOff

### Value Objects
- ReasonCode
- ApprovalThreshold
- EvidenceReference

### Repositories
- StockAdjustmentRepository
- WriteOffRepository

### DTOs (application/API layer)
**Request:** `SubmitAdjustmentRequest`, `ApproveAdjustmentRequest`, `RejectAdjustmentRequest`, `CreateReasonCodeRequest`  
**Response:** `AdjustmentCaseResponse`, `WriteOffResponse`, `CommandResultResponse`

### Validation
- active reason code
- threshold
- SoD

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- StockAdjustmentService
- WriteOffService

### Controllers
- AdjustmentController
- ReasonCodeController

### Exception Handling
- ReasonCodeRequiredException
- WriteOffNotAuthorizedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['ADJUST_SUBMIT', 'ADJUST_APPROVE', 'WRITE_OFF_AUTHORIZE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inventory/adjustments
- inventory/write-offs
- governance/policies

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- StockAdjustmentPage (UI-026)
- WriteOffAuthorizationPage (UI-027)
- GovernancePoliciesPage (UI-010)

### Components
- AdjustmentForm
- ReasonCodeSelect
- EvidenceUpload
- ApprovalPanel

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- AdjustmentVm
- WriteOffVm

### Services
- AdjustmentApiService
- AdjustmentFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- AdjustmentForm
- WriteOffForm

### Validation
- reason required
- qty != 0

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['draft adjustment, pending approvals']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-022–025
- API-029
- API-116/117
- API-120–122

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- SubmitAdjustmentRequest
- ApproveAdjustmentRequest
- RejectAdjustmentRequest
- CreateReasonCodeRequest

### Response DTOs
- AdjustmentCaseResponse
- WriteOffResponse
- CommandResultResponse

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
- adjust updates stock + movement
- write-off finance ack

### API Tests
- API-120–122

### UI Tests
- UI-026/027

---

## 10. Dependencies

### Required features
`F-03`, `F-04`, `F-28`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-17`.

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

*Generated for Technical Lead delivery planning — F-17*
