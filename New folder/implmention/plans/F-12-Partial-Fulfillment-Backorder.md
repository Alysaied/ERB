# Implementation Plan — F-12: Partial Fulfillment & Backorder Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-12 |
| **Feature Name** | Partial Fulfillment & Backorder Management |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-07 Order Fulfillment |
| **Required previous features** | `F-10`, `F-11` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Partial ship available qty, create acknowledged backorders, and prioritize fulfillment when stock arrives.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Maximize fill rate under shortage without silent short-ships (BO-06).

---

## 3. User Stories

- US-045
- US-046

Primary story references: **US-045, US-046** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-045 partial ship MVP
- AC-046 backorder priority P2

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `fulfillment.backorders` | Backorder queue |

### Relationships

- backorder → order line

### Constraints

- backorder qty > 0; customer ack flag for partial

### Migration Tasks (Flyway)

- V1_63__backorders.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- Backorder
- CustomerOrderFulfillment

### Value Objects
- BackorderPriority
- PartialFulfillmentPlan

### Repositories
- BackorderRepository

### DTOs (application/API layer)
**Request:** `PartialFulfillmentRequest`, `CreateBackorderRequest`, `FulfillBackorderRequest`  
**Response:** `PartialFulfillmentResponse`, `BackorderResponse`, `BackorderBoardResponse`

### Validation
- partial requires ack
- priority sequencing

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- PartialFulfillmentService
- BackorderService

### Controllers
- BackorderController

### Exception Handling
- PartialWithoutAckException
- BackorderNotFulfillableException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['BACKORDER_MANAGE', 'ORDER_FULFILL']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- fulfillment/partial-backorders

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- PartialFulfillmentBackorderPage (UI-032)

### Components
- PartialShipWizard
- BackorderQueue
- PriorityEditor

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- BackorderVm
- PartialPlanVm

### Services
- BackorderApiService
- PartialFulfillmentFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- PartialFulfillmentForm
- CustomerAckForm

### Validation
- ack required
- ship qty <= available

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['partial draft, backorder list']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-093–095
- API-164

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- PartialFulfillmentRequest
- CreateBackorderRequest
- FulfillBackorderRequest

### Response DTOs
- PartialFulfillmentResponse
- BackorderResponse
- BackorderBoardResponse

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
- partial + backorder created
- auto-reserve when stock arrives P2

### API Tests
- API-093–095, 164

### UI Tests
- UI-032

---

## 10. Dependencies

### Required features
`F-10`, `F-11`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-12`.

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

*Generated for Technical Lead delivery planning — F-12*
