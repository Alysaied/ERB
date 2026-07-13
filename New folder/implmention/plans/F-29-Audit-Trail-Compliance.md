# Implementation Plan — F-29: Audit Trail & Compliance

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-29 |
| **Feature Name** | Audit Trail & Compliance |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-13 audit projections + movement writer |
| **Required previous features** | `F-28` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Immutable movement/audit trail, auditor query/export, and control breach detection.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Demonstrate 100% traceability for auditors (BO-19).

---

## 3. User Stories

- US-086
- US-087
- US-088

Primary story references: **US-086, US-087, US-088** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-086 trail MVP
- AC-087 query P2
- AC-088 breach detection P2

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `audit.inventory_movement_records` | Movements |
| `audit.audit_trail_records` | Field-level/audit events |

### Relationships

- append-only; no update/delete grants for app role

### Constraints

- immutable; chk_domain_movement_type

### Migration Tasks (Flyway)

- V1_03__inventory_movement_records.sql
- V1_02 audit trail
- DB REVOKE UPDATE/DELETE

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- InventoryMovementRecord
- AuditTrailRecord

### Value Objects
- MovementType
- AuditQuantitySnapshot
- BeforeAfterValues

### Repositories
- MovementRecordRepository
- AuditTrailQueryRepository

### DTOs (application/API layer)
**Request:** `AuditTrailQuery`, `MovementHistoryQuery`, `ExportAuditRequest`  
**Response:** `AuditTrailResponse`, `MovementHistoryResponse`, `ExportJobResponse`

### Validation
- query filters required for large ranges

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- AuditTrailQueryService
- ControlBreachDetectionService
- MovementAppendService

### Controllers
- AuditIntelligenceController

### Exception Handling
- AuditExportTooLargeException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['AUDIT_VIEW', 'AUDIT_EXPORT']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- reports/audit-workspace
- reports/audit-trail
- inventory/movement-history

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- AuditControlReviewPage (UI-047)
- AuditTrailQueryPage (UI-048)
- MovementHistoryPage (UI-022)

### Components
- AuditFilter
- BeforeAfterViewer
- ExportDialog
- BreachList

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- AuditEventVm
- MovementVm

### Services
- AuditApiService
- AuditFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- AuditQueryForm

### Validation
- date range max window

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['query results, export status']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-155
- API-156
- API-157

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- AuditTrailQuery
- MovementHistoryQuery
- ExportAuditRequest

### Response DTOs
- AuditTrailResponse
- MovementHistoryResponse
- ExportJobResponse

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
- movement appears for every qty change
- no edit API

### API Tests
- API-155–157

### UI Tests
- UI-047/048

---

## 10. Dependencies

### Required features
`F-28`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-29`.

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

*Generated for Technical Lead delivery planning — F-29*
