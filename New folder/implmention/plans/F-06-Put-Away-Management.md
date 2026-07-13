# Implementation Plan — F-06: Put-Away Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-06 |
| **Feature Name** | Put-Away Management |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-06 Inbound Receiving |
| **Required previous features** | `F-05`, `F-02`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Confirm storage placement of received stock so sellable ATP reflects locatable inventory.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Prevent promising stock pickers cannot find (BO-03, BO-06).

---

## 3. User Stories

- US-018

Primary story references: **US-018** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-018-* pending put-away queue, confirm position, ATP update only after put-away

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `inbound.put_aways` | Put-away confirmation records |
| `network.storage_positions` | Destination bins |
| `inventory.stock_positions` | Availability state update |

### Relationships

- put_aways → goods_receipts; storage_position_id FK

### Constraints

- put-away only when receipt verified; position belongs to receipt location

### Migration Tasks (Flyway)

- V1_44__put_aways.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- GoodsReceipt (put-away method)
- PutAway record

### Value Objects
- StoragePositionCode
- Quantity

### Repositories
- PutAwayRepository
- GoodsReceiptRepository

### DTOs (application/API layer)
**Request:** `ConfirmPutAwayRequest`  
**Response:** `PutAwayResultResponse`, `PendingPutAwayResponse`

### Validation
- position exists at location
- qty matches pending

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- PutAwayService

### Controllers
- PutAwayController

### Exception Handling
- NoPendingPutAwayException
- InvalidStoragePositionException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['PUT_AWAY_EXECUTE', 'location-scoped']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inbound/put-away
- inbound/put-away/:goodsReceiptId

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- PutAwayWorkbenchPage (UI-017)

### Components
- PendingPutAwayQueue
- PositionPicker
- PutAwayConfirmForm

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- PendingPutAwayVm

### Services
- PutAwayApiService
- PutAwayFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- PutAwayForm

### Validation
- position required

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['pending queue, selected receipt']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-074 GET pending-put-away
- API-073 POST put-away
- API-015/016 storage positions

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- ConfirmPutAwayRequest

### Response DTOs
- PutAwayResultResponse
- PendingPutAwayResponse

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
- ATP increases only after put-away

### API Tests
- API-073/074

### UI Tests
- UI-017 complete task

---

## 10. Dependencies

### Required features
`F-05`, `F-02`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-06`.

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

*Generated for Technical Lead delivery planning — F-06*
