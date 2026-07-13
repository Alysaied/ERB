# Implementation Plan — F-16: Count Variance Investigation & Approval

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-16 |
| **Feature Name** | Count Variance Investigation & Approval |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-09 Inventory Accuracy |
| **Required previous features** | `F-14|F-15`, `F-03`, `F-28`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Investigate count variances and approve/reject adjustments with SoD and thresholds.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Correct balances only through independent approval (BO-02, BO-19).

---

## 3. User Stories

- US-033
- US-034
- US-037

Primary story references: **US-033, US-034, US-037** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-033 identify
- AC-034 investigate/approve
- AC-037 threshold routing

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `accuracy.count_variances` | Variance lines |
| `accuracy adjustment case tables` | Investigation case |

### Relationships

- variance → count; case → variances

### Constraints

- counter cannot approve own count BR-019
- threshold → elevated approver

### Migration Tasks (Flyway)

- V1_72__count_variances_adjustment_cases.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- InventoryAdjustmentCase (AR)
- CountVariance

### Value Objects
- VarianceQuantity
- InvestigationFinding
- ApprovalDecision

### Repositories
- AdjustmentCaseRepository
- VarianceRepository

### DTOs (application/API layer)
**Request:** `CreateAdjustmentCaseRequest`, `InvestigateCaseRequest`, `ApproveVarianceRequest`  
**Response:** `AdjustmentCaseResponse`, `PendingApprovalsResponse`

### Validation
- SoD API-031
- approval thresholds API-029

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- VarianceInvestigationService
- ApprovalRoutingService

### Controllers
- AdjustmentCaseController

### Exception Handling
- SoDViolationException
- ApprovalThresholdNotMetException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['VARIANCE_INVESTIGATE', 'VARIANCE_APPROVE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inventory/variances
- inventory/variances/:caseId

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- VarianceInvestigationApprovalPage (UI-025)

### Components
- VarianceTable
- InvestigationForm
- ApprovalActions

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- VarianceCaseVm

### Services
- VarianceApiService
- VarianceFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- InvestigationForm
- ApprovalForm

### Validation
- findings required before approve

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['pending approvals queue']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-116–119
- API-123
- API-029
- API-031

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateAdjustmentCaseRequest
- InvestigateCaseRequest
- ApproveVarianceRequest

### Response DTOs
- AdjustmentCaseResponse
- PendingApprovalsResponse

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
- self-approval blocked
- threshold routes to OD/Finance

### API Tests
- API-116–119, 123

### UI Tests
- UI-025

---

## 10. Dependencies

### Required features
`F-14|F-15`, `F-03`, `F-28`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-16`.

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

*Generated for Technical Lead delivery planning — F-16*
