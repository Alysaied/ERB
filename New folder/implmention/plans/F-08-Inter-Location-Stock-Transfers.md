# Implementation Plan — F-08: Inter-Location Stock Transfers

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-08 |
| **Feature Name** | Inter-Location Stock Transfers |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-08 Network Transfer |
| **Required previous features** | `F-02`, `F-03`, `F-04`, `F-27`, `F-28` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Request, approve, dispatch, and receive inter-location transfers with source minimum protection and in-transit tracking.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Resolve local stockouts using network inventory without cascading shortages (BO-05, BR-011/012).

---

## 3. User Stories

- US-058
- US-059
- US-060
- US-061
- US-063

Primary story references: **US-058, US-059, US-060, US-061, US-063** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-058 request
- AC-059 approve/reject
- AC-060 execute
- AC-061 in-transit P2
- AC-063 source minimum

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `transfer.transfer_requests (+ lines)` | Request |
| `transfer.stock_transfers (+ lines)` | Execution |
| `transfer.in_transit_stock` | In-transit qty |

### Relationships

- request → transfer on approve; lines sku/qty; source/dest location codes

### Constraints

- source != dest; transfer capacity respects min threshold; SoD on approve

### Migration Tasks (Flyway)

- V1_50__transfer_schema.sql
- V1_51__transfer_requests.sql
- V1_52__stock_transfers_in_transit.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- StockTransfer (AR)
- TransferRequest state

### Value Objects
- TransferLine
- InTransitQuantity
- UserActionAttribution

### Repositories
- TransferRepository
- TransferQueryRepository

### DTOs (application/API layer)
**Request:** `CreateTransferRequest`, `ApproveTransferRequest`, `RejectTransferRequest`, `DispatchTransferRequest`, `ReceiveTransferRequest`  
**Response:** `TransferResponse`, `PendingApprovalResponse`, `InTransitResponse`, `TransferCapacityResponse`

### Validation
- capacity API-042
- SoD
- location operational

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- TransferService
- TransferCapacityService

### Controllers
- TransferController

### Exception Handling
- InsufficientTransferCapacityException
- SoDViolationException
- TransferStateException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['TRANSFER_REQUEST', 'TRANSFER_APPROVE', 'TRANSFER_EXECUTE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- transfers/requests
- transfers/approvals
- transfers/execution

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- TransferRequestPage (UI-038)
- TransferApprovalQueuePage (UI-039)
- TransferExecutionPage (UI-040)

### Components
- TransferLineEditor
- ApprovalQueue
- DispatchReceivePanel
- InTransitBoard

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- TransferVm
- TransferCapacityVm

### Services
- TransferApiService
- TransferFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- TransferRequestForm
- RejectReasonForm
- ReceiveForm

### Validation
- source != dest
- qty > 0
- justification required

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['request draft, approval queue, in-transit list']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-098–107
- API-042 transfer-capacity

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateTransferRequest
- ApproveTransferRequest
- RejectTransferRequest
- DispatchTransferRequest
- ReceiveTransferRequest

### Response DTOs
- TransferResponse
- PendingApprovalResponse
- InTransitResponse
- TransferCapacityResponse

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
- request→approve→dispatch→receive balances both sites
- source min blocks

### API Tests
- API-098–107, 042

### UI Tests
- UI-038–040

---

## 10. Dependencies

### Required features
`F-02`, `F-03`, `F-04`, `F-27`, `F-28`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-08`.

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

*Generated for Technical Lead delivery planning — F-08*
