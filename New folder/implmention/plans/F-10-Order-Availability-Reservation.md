# Implementation Plan — F-10: Order Availability & Reservation

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-10 |
| **Feature Name** | Order Availability & Reservation |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-07 Order Fulfillment + M-04 reservations |
| **Required previous features** | `F-04`, `F-01`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Confirm ATP, reserve stock for confirmed orders, release on cancel, and support multi-location plans.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Prevent overselling and double-allocation (BO-06).

---

## 3. User Stories

- US-041
- US-042
- US-043
- US-048

Primary story references: **US-041, US-042, US-043, US-048** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-041 availability
- AC-042 reserve
- AC-043 release
- AC-048 multi-location P2

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `fulfillment.customer_orders / customer_order_lines` | Orders |
| `fulfillment.inventory_reservations` | Reservations |

### Relationships

- reservation → order line + stock position identity

### Constraints

- reserved <= available; optimistic locking on stock_positions

### Migration Tasks (Flyway)

- V1_60__fulfillment_orders.sql
- V1_61__inventory_reservations.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- CustomerOrderFulfillment (AR)
- InventoryReservation

### Value Objects
- OrderLine
- ReservationId
- AtpSnapshot

### Repositories
- CustomerOrderRepository
- ReservationRepository

### DTOs (application/API layer)
**Request:** `CreateOrderRequest`, `ConfirmAvailabilityRequest`, `ConfirmOrderRequest`, `CancelOrderRequest`, `MultiLocationPlanRequest`, `CreateReservationRequest`, `ReleaseReservationRequest`  
**Response:** `OrderResponse`, `AvailabilityCheckResponse`, `ReservationResponse`, `MultiLocationPlanResponse`

### Validation
- product eligibility
- ATP sufficient BR-001
- inactive product blocked

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- OrderAvailabilityService
- ReservationSagaService

### Controllers
- FulfillmentOrderController
- ReservationController

### Exception Handling
- InsufficientAtpException
- ReservationConflictException
- OrderStateException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['ORDER_RESERVE', 'ORDER_VIEW', 'location-scoped']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- fulfillment/reservations
- fulfillment/split-planner
- inventory/availability

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- OrderReservationWorkbenchPage (UI-030)
- MultiLocationSplitPlannerPage (UI-035)
- AvailabilityInquiryPage

### Components
- AvailabilityResultPanel
- ReservationLines
- SplitPlanEditor

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- OrderVm
- ReservationVm
- AtpVm

### Services
- FulfillmentApiService
- ReservationFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- AvailabilityCheckForm
- ConfirmOrderForm

### Validation
- order lines qty > 0

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['order draft, ATP results, reservation ids']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-081, 084–087
- API-043/044
- API-036
- API-139

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateOrderRequest
- ConfirmAvailabilityRequest
- ConfirmOrderRequest
- CancelOrderRequest
- MultiLocationPlanRequest
- CreateReservationRequest
- ReleaseReservationRequest

### Response DTOs
- OrderResponse
- AvailabilityCheckResponse
- ReservationResponse
- MultiLocationPlanResponse

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
- confirm reduces ATP; cancel restores

### API Tests
- API-081–087, 043–044

### UI Tests
- UI-030 concurrent reservation conflict

---

## 10. Dependencies

### Required features
`F-04`, `F-01`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-10`.

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

*Generated for Technical Lead delivery planning — F-10*
