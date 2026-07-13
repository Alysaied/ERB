# Implementation Plan — F-20: Low-Stock Alerting & Replenishment

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-20 |
| **Feature Name** | Low-Stock Alerting & Replenishment |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-13 alerts + M-05 requisitions |
| **Required previous features** | `F-03`, `F-04`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Generate low/out-of-stock alerts, acknowledge them, suggest replenishment (transfer-before-buy), and manage purchase requisitions.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Move purchasing from crisis response to threshold-driven discipline (BO-05).

---

## 3. User Stories

- US-051
- US-052
- US-053
- US-054
- US-074

Primary story references: **US-051, US-052, US-053, US-054, US-074** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-051–053 MVP alerts/suggestions
- AC-054 requisitions P2
- AC-074 reporting

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `audit.operational_alerts` | Alerts |
| `procurement.purchase_requisitions (+ lines)` | Requisitions |

### Relationships

- alert may link sku/location; requisition from recommendation

### Constraints

- acknowledge requires user; network check before approve requisition BR-011

### Migration Tasks (Flyway)

- V1_80__operational_alerts.sql
- V2_12__purchase_requisitions.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- OperationalAlert
- PurchaseRequisition (AR)

### Value Objects
- AlertType
- ReplenishmentRecommendation
- RequisitionLine

### Repositories
- OperationalAlertRepository
- PurchaseRequisitionRepository

### DTOs (application/API layer)
**Request:** `AcknowledgeAlertRequest`, `CreateRequisitionRequest`, `ApproveRequisitionRequest`, `RejectRequisitionRequest`, `ConvertRequisitionToPoRequest`  
**Response:** `AlertResponse`, `ReplenishmentRecommendationResponse`, `RequisitionResponse`

### Validation
- threshold breach detection
- network availability before buy

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- StockAlertService
- ReplenishmentRecommendationService
- PurchaseRequisitionService

### Controllers
- AlertController
- RequisitionController
- ReplenishmentIntelligenceController

### Exception Handling
- AlertAlreadyAcknowledgedException
- RequisitionNetworkCheckFailedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['ALERT_REVIEW', 'REQUISITION_MANAGE', 'REQUISITION_APPROVE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- procurement/low-stock-alerts
- procurement/replenishment-planning
- procurement/requisitions

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- LowStockAlertReviewPage (UI-036)
- ReplenishmentPlanningPage (UI-037)
- PurchaseRequisitionPage (UI-013)

### Components
- AlertQueue
- AckDialog
- RecommendationCard
- RequisitionForm

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- AlertVm
- RecommendationVm
- RequisitionVm

### Services
- AlertApiService
- RequisitionApiService
- ReplenishmentFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- AckForm
- RequisitionForm

### Validation
- ack rationale when dismiss

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['alert list, recommendations, requisition draft']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-037/039
- API-158–160
- API-054–058
- API-166
- Gap C-03 list

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- AcknowledgeAlertRequest
- CreateRequisitionRequest
- ApproveRequisitionRequest
- RejectRequisitionRequest
- ConvertRequisitionToPoRequest

### Response DTOs
- AlertResponse
- ReplenishmentRecommendationResponse
- RequisitionResponse

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
- crossing reorder creates alert
- transfer suggested before PO

### API Tests
- API-158–160, 054–058

### UI Tests
- UI-036/037/013

---

## 10. Dependencies

### Required features
`F-03`, `F-04`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-20`.

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

*Generated for Technical Lead delivery planning — F-20*
