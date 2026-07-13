# Implementation Plan — F-11: Pick, Pack & Ship Fulfillment

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-11 |
| **Feature Name** | Pick, Pack & Ship Fulfillment |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-07 Order Fulfillment |
| **Required previous features** | `F-10`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Assign pick work, verify picks, pack, and ship with inventory deduction at shipment confirmation.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Execute physical fulfillment with inventory matching goods dispatched (BO-03, BO-06).

---

## 3. User Stories

- US-044
- US-049

Primary story references: **US-044, US-049** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-044 pick/pack/ship
- AC-049 status visibility

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `fulfillment.fulfillment_executions` | Pick/pack state |
| `fulfillment.fulfillment_pick_lines` | Pick lines |
| `fulfillment.shipments / shipment_lines` | Shipments |

### Relationships

- execution → order; shipment → execution

### Constraints

- ship only after pack; lot required if traceable

### Migration Tasks (Flyway)

- V1_62__fulfillment_execution_shipments.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- CustomerOrderFulfillment
- FulfillmentExecution
- Shipment

### Value Objects
- PickLine
- ShipmentReference
- LotIdentity

### Repositories
- FulfillmentExecutionRepository
- ShipmentRepository

### DTOs (application/API layer)
**Request:** `CreatePickListRequest`, `VerifyPickRequest`, `PackOrderRequest`, `CreateShipmentRequest`  
**Response:** `PickListResponse`, `AwaitingPickResponse`, `ShipmentResponse`, `OrderStatusResponse`

### Validation
- pick qty <= reserved
- location not frozen

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- PickPackShipService
- OrderStatusQueryService

### Controllers
- FulfillmentExecutionController

### Exception Handling
- PickVerificationFailedException
- LocationFrozenException
- ShipmentNotAllowedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['FULFILL_PICK', 'FULFILL_SHIP']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- fulfillment/pick-pack-ship
- fulfillment/order-status

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- PickPackShipWorkbenchPage (UI-031)
- OrderFulfillmentStatusPage (UI-034)

### Components
- PickQueue
- PickVerifyScanner
- PackPanel
- ShipConfirm

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- PickListVm
- ShipmentVm
- OrderStatusVm

### Services
- FulfillmentExecutionApiService
- PickPackShipFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- PickVerifyForm
- ShipForm

### Validation
- scanned sku matches
- qty match

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['queue, active pick, ship draft']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-088–092
- API-082/083/097
- API-041 lots
- API-177
- Gap C-01 location pick queue

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreatePickListRequest
- VerifyPickRequest
- PackOrderRequest
- CreateShipmentRequest

### Response DTOs
- PickListResponse
- AwaitingPickResponse
- ShipmentResponse
- OrderStatusResponse

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
- on-hand decreases only on ship

### API Tests
- API-088–092, 097

### UI Tests
- UI-031/034 full flow

---

## 10. Dependencies

### Required features
`F-10`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-11`.

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

*Generated for Technical Lead delivery planning — F-11*
