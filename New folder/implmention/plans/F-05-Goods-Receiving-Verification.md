# Implementation Plan — F-05: Goods Receiving & Verification

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-05 |
| **Feature Name** | Goods Receiving & Verification |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-06 Inbound Receiving |
| **Required previous features** | `F-01`, `F-02`, `F-03`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Receive and verify inbound goods, capture discrepancies, support non-PO/return intake, and emit immutable movement history.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Ensure on-hand reflects physical reality from entry and protect supplier accountability (BO-03).

---

## 3. User Stories

- US-015
- US-016
- US-017
- US-019
- US-020
- US-029

Primary story references: **US-015, US-016, US-017, US-019, US-020, US-029** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-015–017 receiving
- AC-019 non-PO/return
- AC-020 tolerance P2
- AC-029 movement history

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `inbound.goods_receipts` | Receipt header |
| `inbound.goods_receipt_lines` | Lines + lots/shelf life |
| `inbound.receipt_discrepancies` | Shortage/over/wrong/damage |
| `audit.inventory_movement_records` | Immutable movements |

### Relationships

- goods_receipt_lines → goods_receipts
- discrepancies → goods_receipts
- optional FK purchase_order_id

### Constraints

- positive line qty; reason code on discrepancy
- PO validate-for-receipt when PO-backed (BR-007)

### Migration Tasks (Flyway)

- V1_40__inbound_schema.sql
- V1_41__goods_receipts.sql
- V1_42__discrepancies.sql
- V1_43__movement_records.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- GoodsReceipt (AR)
- ReceiptDiscrepancy
- GoodsReceiptLine

### Value Objects
- PositiveQuantity
- LotIdentity
- ShelfLifeProfile
- ReasonCodeAttribution

### Repositories
- GoodsReceiptRepository
- InventoryMovementRecordRepository

### DTOs (application/API layer)
**Request:** `CreateGoodsReceiptRequest`, `VerifyGoodsReceiptRequest`, `CreateDiscrepancyRequest`, `ResolveDiscrepancyRequest`, `AdHocReceiptRequest`, `ReturnReceiptRequest`  
**Response:** `GoodsReceiptResponse`, `DiscrepancyResponse`, `MovementHistoryResponse`, `PagedResponse`

### Validation
- PO authorization
- lot required if traceable BR-017
- tolerance BR-006/008
- reason codes

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- GoodsReceivingService
- DiscrepancyService
- MovementRecordingService

### Controllers
- GoodsReceiptController
- AdHocReceiptController
- MovementIntelligenceController

### Exception Handling
- PoNotValidForReceiptException
- ReceiptVerificationFailedException
- DiscrepancyResolutionInvalidException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['RECEIVE_GOODS', 'RESOLVE_DISCREPANCY', 'location-scoped']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inbound/goods-receipts
- inbound/goods-receipts/:id
- inbound/discrepancies
- inbound/non-po-receipts
- inventory/movement-history

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- GoodsReceiptWorkbenchPage (UI-015)
- DiscrepancyResolutionPage (UI-016)
- NonPoReturnIntakePage (UI-018)
- MovementHistoryPage (UI-022)

### Components
- ReceiptLineEditor
- VerifyPanel
- DiscrepancyForm
- LotCaptureFields
- MovementFilter

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- GoodsReceiptVm
- DiscrepancyVm
- MovementVm

### Services
- InboundApiService
- GoodsReceiptFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- ReceiptCreateForm
- VerifyForm
- DiscrepancyForm
- AdHocReceiptForm

### Validation
- line qty > 0
- lot if required
- reason code required on discrepancy

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['active receipt, lines, discrepancy queue']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-065 validate-for-receipt
- API-066–072 goods receipts + discrepancies
- API-075/076 ad-hoc + return receipts
- API-025/030 reason/tolerance
- API-155 movements

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateGoodsReceiptRequest
- VerifyGoodsReceiptRequest
- CreateDiscrepancyRequest
- ResolveDiscrepancyRequest
- AdHocReceiptRequest
- ReturnReceiptRequest

### Response DTOs
- GoodsReceiptResponse
- DiscrepancyResponse
- MovementHistoryResponse
- PagedResponse

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
- PO receipt happy path
- discrepancy resolve
- movement immutable

### API Tests
- API-065–076, 155

### UI Tests
- UI-015/016/018/022 E2E

---

## 10. Dependencies

### Required features
`F-01`, `F-02`, `F-03`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-05`.

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

*Generated for Technical Lead delivery planning — F-05*
