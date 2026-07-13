# Implementation Plan — F-28: Operational Accountability & Controls

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-28 |
| **Feature Name** | Operational Accountability & Controls |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-12 + M-03 SoD + audit |
| **Required previous features** | `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Enforce segregation of duties and record user activity for material actions.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Strengthen loss prevention and individual accountability (BO-19).

---

## 3. User Stories

- US-083
- US-084

Primary story references: **US-083, US-084** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-083 activity logging
- AC-084 SoD no self-approval / conflicting roles

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `audit.audit_trail_records` | Activity/audit |
| `governance policies SoD rules` | Evaluated via API-031 |

### Relationships

- audit references user_id + entity

### Constraints

- initiator != approver for governed actions

### Migration Tasks (Flyway)

- V1_02__audit_trail_records.sql
- SoD seed in governance

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- AuditTrailRecord
- SoDPolicy evaluation

### Value Objects
- UserActionAttribution
- SoDEvaluationResult

### Repositories
- AuditTrailRepository

### DTOs (application/API layer)
**Request:** `EvaluateSoDRequest`, `EvaluateActionRequest`, `ValidateLocationScopeRequest`  
**Response:** `SoDEvaluationResponse`, `AuthorizationDecisionResponse`

### Validation
- action + actor + subject required

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- SegregationOfDutiesService
- ActivityLoggingService
- ActionAuthorizationService

### Controllers
- GovernanceSoDController
- AuthorizationController

### Exception Handling
- SoDViolationException
- LocationScopeViolationException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['Called internally by all approval commands; admin configure roles']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- admin/roles-access (policy)
- cross-cutting on approval UIs

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- RoleAccessControlPage (UI-050) config; enforced on UI-025/026/027/039

### Components
- PermissionMatrix
- SoDWarningDialog

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- AuthorizationDecisionVm

### Services
- AuthorizationApiService
- used by all facades before approve

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- N/A primary; approve actions call evaluate

### Validation
- disable approve if SoD fails

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['permission catalog in core']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-031
- API-148
- API-149

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- EvaluateSoDRequest
- EvaluateActionRequest
- ValidateLocationScopeRequest

### Response DTOs
- SoDEvaluationResponse
- AuthorizationDecisionResponse

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
- counter cannot approve own variance
- conflicting roles blocked

### API Tests
- API-031/148/149

### UI Tests
- approval buttons disabled + error

---

## 10. Dependencies

### Required features
`F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-28`.

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

*Generated for Technical Lead delivery planning — F-28*
