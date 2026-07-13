# Implementation Plan — F-07: Purchase Order & Inbound Supply Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-07 |
| **Feature Name** | Purchase Order & Inbound Supply Management |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-05 Procurement & Supplier |
| **Required previous features** | `F-01`, `F-02`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Supplier master, PO lifecycle, expected deliveries, inbound tracking, and delay visibility.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Give operations visibility into when shortages will be resolved (BO-05).

---

## 3. User Stories

- US-013
- US-014
- US-021
- US-022
- US-055
- US-079

Primary story references: **US-013, US-014, US-021, US-022, US-055, US-079** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-013/014 PO
- AC-021 amend/cancel
- AC-055 tracking
- AC-022 supplier performance P3
- AC-079 delay notify

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `procurement.suppliers` | Supplier master |
| `procurement.purchase_orders / purchase_order_lines` | PO commitment |
| `procurement.expected_inbound_deliveries (+ lines)` | Delivery plan |

### Relationships

- PO → supplier; expected delivery → PO; lines → sku

### Constraints

- uk supplier_code; chk_domain_po_status; active supplier for new PO

### Migration Tasks (Flyway)

- V2_10__procurement_suppliers.sql
- V2_11__purchase_orders.sql
- V2_12__expected_deliveries.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- Supplier
- PurchaseOrder (AR)
- ExpectedInboundDelivery

### Value Objects
- SupplierCode
- PaymentTerms
- LeadTimeDuration
- PurchaseOrderLine

### Repositories
- SupplierRepository
- PurchaseOrderRepository

### DTOs (application/API layer)
**Request:** `CreateSupplierRequest`, `CreatePurchaseOrderRequest`, `AmendPurchaseOrderRequest`, `CancelPurchaseOrderRequest`, `ScheduleExpectedDeliveryRequest`  
**Response:** `SupplierResponse`, `PurchaseOrderResponse`, `OpenPoBoardResponse`, `InboundCalendarResponse`, `InboundDelayResponse`

### Validation
- product active BR-027
- supplier active
- qty > 0

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- SupplierService
- PurchaseOrderService
- InboundSupplyQueryService

### Controllers
- SupplierController
- PurchaseOrderController
- ProcurementIntelligenceController

### Exception Handling
- SupplierInactiveException
- PoAmendNotAllowedException
- PoCancelBlockedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['SUPPLIER_MANAGE', 'PO_MANAGE', 'PO_VIEW']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- procurement/suppliers
- procurement/purchase-orders
- procurement/inbound-delivery-planning
- procurement/inbound-supply-tracking

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- SupplierManagementPage (UI-011)
- PurchaseOrderPage (UI-012)
- InboundDeliveryPlanningPage (UI-014)
- InboundSupplyTrackingPage (UI-019)

### Components
- PoLineEditor
- SupplierForm
- DeliveryCalendar
- OpenPoTable

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- SupplierVm
- PurchaseOrderVm
- ExpectedDeliveryVm

### Services
- ProcurementApiService
- PurchaseOrderFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- SupplierForm
- PoForm
- ExpectedDeliveryForm

### Validation
- supplier required
- line sku/qty

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['po list filters, selected PO, delivery draft']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-049–053 suppliers
- API-059–065 POs
- API-161–163 intelligence

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateSupplierRequest
- CreatePurchaseOrderRequest
- AmendPurchaseOrderRequest
- CancelPurchaseOrderRequest
- ScheduleExpectedDeliveryRequest

### Response DTOs
- SupplierResponse
- PurchaseOrderResponse
- OpenPoBoardResponse
- InboundCalendarResponse
- InboundDelayResponse

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
- Create PO → validate-for-receipt
- amend/cancel rules

### API Tests
- API-049–065, 161–163

### UI Tests
- UI-011/012/014/019

---

## 10. Dependencies

### Required features
`F-01`, `F-02`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-07`.

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

*Generated for Technical Lead delivery planning — F-07*
