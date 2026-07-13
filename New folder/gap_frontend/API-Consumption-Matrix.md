# API Consumption Matrix

**Project:** IMS Frontend vs. Approved API Specification  
**Specification Source:** `SRS/Inventory-Management-System-SRS.md` (SRS-API-001, API-001–API-178)  
**Implementation Source:** `ims-frontend/src/app/`  
**Report Date:** July 7, 2026

---

## Executive Summary

| Metric | Value |
|--------|-------|
| APIs in approved specification | **178** |
| APIs consumed via `HttpClient` | **0** (0%) |
| APIs with mock/local substitute | **~12 screen data shapes** via `MockDataService` |
| Auth APIs integrated | **0** — `AuthService` uses hardcoded demo users |
| Angular API service classes | **0** |
| `provideHttpClient` configured | **No** |
| HTTP interceptors (auth, error) | **0** |
| Environment / API base URL | **Not configured** |
| **Overall API integration** | **0%** |

### Current Data Layer

| Service | Path | Role |
|---------|------|------|
| `MockDataService` | `core/services/mock-data.service.ts` | In-memory `Record<string, unknown>` keyed by `UI-001`–`UI-050`; no HTTP |
| `AuthService` | `core/services/auth.service.ts` | Client-side demo login; `sessionStorage` persistence; no `GET /auth/session` |

### Integration Status Legend

| Status | Meaning |
|--------|---------|
| **No** | Not called; no service exists |
| **Mock** | Approximate static data in `MockDataService` for a related screen |
| **Partial** | Local behavior substitutes part of the API contract (e.g. demo auth) |
| **Yes** | Production HTTP integration with correct service |

---

## Cross-Cutting Findings

### Missing Infrastructure (Required Before Any API)

1. Add `provideHttpClient(withInterceptors([...]))` to `app.config.ts`
2. Create `core/http/api-base-url.token.ts` or `environments/environment.ts` with `apiBaseUrl`
3. Implement `AuthInterceptor` — attach bearer token / session cookie from `AuthService`
4. Implement `ErrorInterceptor` — map API error envelopes to `SuccessWarningErrorBanner`
5. Create domain `*ApiService` classes under `features/{domain}/data-access/` or `core/api/`
6. Replace `MockDataService` screen-by-screen with facades calling real APIs

### Incorrect / Non-Spec Implementations

| Area | Current behavior | Spec expectation | Gap |
|------|------------------|------------------|-----|
| Authentication | Hardcoded `demoUsers` map; password length ≥ 4 | `GET /api/v1/auth/session`, IdP/OAuth flow | No server session validation |
| Logout | Clears `sessionStorage` only | `POST /api/v1/auth/logout` | No server session termination |
| Dashboard KPIs | Static mock in `UI-002` | `API-150`, `151`, `152`, `158` | Wrong data source and shape |
| Product list | Mock `products[]` in `UI-005` | `API-002` search with pagination | No search/filter/pagination |
| Alerts | Hardcoded `notificationCount = 12` in header | `API-158` | Not synchronized with alert API |
| Task widget | Hardcoded 15 pending tasks | `API-106`, `123`, `158` | Static links, no API feed |

### Known Spec Gaps (Backend — Frontend Should Plan For)

| Gap ID | Missing endpoint | Affected screens | Frontend note |
|--------|------------------|------------------|---------------|
| GAP-API-01 (C-03) | `GET /api/v1/procurement/requisitions` (list) | UI-013, UI-037 | Queue browse blocked until API-179 added |
| GAP-API-02 (C-01) | Location-level pick queue | UI-031 | Use `API-089` per-order only as workaround |
| GAP-API-03 (C-04) | Canonical return receipt path | UI-043 | Prefer `API-128` over `API-076` per SRS |

---

## M-01 — Product Catalog (API-001 – API-010)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-001 | `/api/v1/products` | POST | Register new product SKU | No | — | `ProductApiService.create()` | — | Wire UI-005 create flow; map `CreateProductRequest` DTO |
| API-002 | `/api/v1/products` | GET | Search/filter products | **Mock** | `MockDataService` | `ProductApiService.search()` | Mock is static array, not search API | Replace UI-005 mock with paginated `GET`; add filter query params |
| API-003 | `/api/v1/products/{sku}` | GET | Get product by SKU | No | — | `ProductApiService.getBySku()` | — | Detail route `/products/catalog/:sku` |
| API-004 | `/api/v1/products/{sku}` | PATCH | Update product attributes | No | — | `ProductApiService.update()` | — | Edit form on catalog detail |
| API-005 | `/api/v1/products/{sku}/lifecycle-status` | POST | Change lifecycle status | No | — | `ProductApiService.changeStatus()` | — | Lifecycle actions on UI-005 |
| API-006 | `/api/v1/products/{sku}/abc-classification` | PUT | Assign ABC class | No | — | `AbcClassificationApiService.assign()` | — | Wire UI-009 bulk classification |
| API-007 | `/api/v1/products/{sku}/eligibility` | GET | Validate product eligibility | No | — | `ProductApiService.checkEligibility()` | — | Use in PO/reservation validation |
| API-008 | `/api/v1/products/categories/{categoryCode}/products` | GET | List products by category | No | — | `ProductApiService.listByCategory()` | — | Category browse on UI-005 |
| API-009 | `/api/v1/products/duplicate-resolutions` | POST | Resolve duplicate conflict | No | — | `ProductApiService.resolveDuplicate()` | — | Duplicate resolution workflow |
| API-010 | `/api/v1/products/import` | POST | Bulk product import | **Mock** | `MockDataService` (`UI-006`) | `ProductImportApiService.import()` | Mock shows fake import jobs only | Wire file upload on UI-006; handle validation errors |

**Target screens:** UI-005, UI-006, UI-009

---

## M-02 — Warehouse Network (API-011 – API-021)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-011 | `/api/v1/locations` | POST | Register location | No | — | `LocationApiService.create()` | — | UI-007 create location |
| API-012 | `/api/v1/locations` | GET | List locations | **Mock** | `MockDataService` (`UI-007`) | `LocationApiService.list()` | Static 3 locations | Lookup service for dropdowns across app |
| API-013 | `/api/v1/locations/{locationCode}` | GET | Get location detail | No | — | `LocationApiService.get()` | — | Detail panel UI-007 |
| API-014 | `/api/v1/locations/{locationCode}/hierarchy` | PATCH | Update hierarchy | No | — | `LocationApiService.updateHierarchy()` | — | Hierarchy editor |
| API-015 | `/api/v1/locations/{locationCode}/storage-positions` | POST | Configure storage position | No | — | `StoragePositionApiService.create()` | — | UI-007, UI-017 put-away |
| API-016 | `/api/v1/locations/{locationCode}/storage-positions` | GET | List storage positions | No | — | `StoragePositionApiService.list()` | — | Put-away destination picker |
| API-017 | `/api/v1/locations/{locationCode}/activate` | POST | Activate location | No | — | `LocationApiService.activate()` | — | Go-live / UI-006 completion |
| API-018 | `/api/v1/locations/{locationCode}/deactivate` | POST | Deactivate location | No | — | `LocationApiService.deactivate()` | — | Status actions UI-007 |
| API-019 | `/api/v1/locations/{locationCode}/close` | POST | Close location | No | — | `LocationApiService.close()` | — | Closure workflow |
| API-020 | `/api/v1/locations/{locationCode}/freeze-status` | GET | Physical count freeze status | No | — | `LocationFreezeApiService.get()` | — | UI-024 freeze banner |
| API-021 | `/api/v1/locations/{locationCode}/operational-status` | GET | Operational status | No | — | `LocationApiService.getOperationalStatus()` | — | Transaction gating checks |

**Target screens:** UI-006, UI-007, UI-017, UI-024

---

## M-03 — Inventory Governance (API-022 – API-031)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-022 | `/api/v1/governance/reason-codes` | POST | Create reason code | No | — | `ReasonCodeApiService.create()` | — | UI-010 |
| API-023 | `/api/v1/governance/reason-codes` | GET | List reason codes | **Mock** | `MockDataService` (`UI-010`) | `ReasonCodeLookupService.list()` | Static reason code strings | Shared lookup for adjustments, discrepancies |
| API-024 | `/api/v1/governance/reason-codes/{code}/retire` | POST | Retire reason code | No | — | `ReasonCodeApiService.retire()` | — | UI-010 |
| API-025 | `/api/v1/governance/reason-codes/{code}/validate` | GET | Validate reason code | No | — | `ReasonCodeLookupService.validate()` | — | Form validation UI-016, UI-026 |
| API-026 | `/api/v1/governance/policies` | POST | Publish policy version | No | — | `GovernancePolicyApiService.publish()` | — | UI-010 |
| API-027 | `/api/v1/governance/policies/{policyId}/approval-thresholds` | PATCH | Update approval thresholds | No | — | `GovernancePolicyApiService.updateThresholds()` | — | UI-010 thresholds tab |
| API-028 | `/api/v1/governance/policies/{policyId}/receipt-tolerances` | PATCH | Update receipt tolerances | No | — | `GovernancePolicyApiService.updateTolerances()` | — | UI-010 tolerances tab |
| API-029 | `/api/v1/governance/approval-thresholds` | GET | Get approval thresholds | No | — | `ApprovalThresholdApiService.get()` | — | Adjustment routing UI-026, UI-027 |
| API-030 | `/api/v1/governance/receipt-tolerances` | GET | Get receipt tolerances | No | — | `ReceiptToleranceApiService.get()` | — | Discrepancy evaluation UI-016 |
| API-031 | `/api/v1/governance/segregation-of-duties/evaluate` | POST | Evaluate SoD compliance | No | — | `AuthorizationEvaluationApiService.evaluateSoD()` | — | UI-050; block self-approval |

**Target screens:** UI-010, UI-016, UI-026, UI-027, UI-050

---

## M-04 — Inventory Balance (API-032 – API-048)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-032 | `/api/v1/inventory/opening-balances` | POST | Establish opening balances | No | — | `OpeningBalanceApiService.create()` | — | UI-006 go-live import |
| API-033 | `/api/v1/inventory/stock-positions` | GET | List stock positions | No | — | `StockPositionApiService.list()` | — | UI-020 status monitor |
| API-034 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}` | GET | Get stock position detail | No | — | `StockPositionApiService.get()` | — | Detail drawer UI-020 |
| API-035 | `/api/v1/inventory/availability/{sku}` | GET | ATP by SKU at location | No | — | `AvailabilityApiService.get()` | — | UI-021 availability inquiry |
| API-036 | `/api/v1/inventory/availability/{sku}/network` | GET | Network ATP rollup | No | — | `AvailabilityApiService.getNetwork()` | — | UI-021, UI-035 split planner |
| API-037 | `/api/v1/inventory/stock-status/{locationCode}/{sku}` | GET | Stock status indicator | No | — | `StockStatusApiService.get()` | — | UI-020, UI-036 alerts |
| API-038 | `/api/v1/inventory/stock-policies` | POST | Define stock policy | No | — | `StockPolicyApiService.create()` | — | UI-008 |
| API-039 | `/api/v1/inventory/stock-policies/{locationCode}/{sku}` | GET | Get stock policy | **Mock** | `MockDataService` (`UI-008`) | `StockPolicyApiService.get()` | Static policy rows | Policy editor UI-008 |
| API-040 | `/api/v1/inventory/stock-policies/{locationCode}/{sku}` | PATCH | Update stock policy | No | — | `StockPolicyApiService.update()` | — | Threshold editor UI-008 |
| API-041 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/lots` | GET | Lot/batch breakdown | No | — | `LotBreakdownApiService.get()` | — | Pick verification UI-031 |
| API-042 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity` | GET | Transfer spare capacity | No | — | `TransferCapacityApiService.get()` | — | UI-038, UI-039 |
| API-043 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations` | POST | Reserve stock | No | — | `ReservationApiService.reserve()` | — | UI-030 reservation workbench |
| API-044 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations/{reservationId}/release` | POST | Release reservation | No | — | `ReservationApiService.release()` | — | UI-030 cancel/release |
| API-045 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds` | POST | Apply quarantine hold | No | — | `QuarantineHoldApiService.apply()` | — | UI-028, UI-033 |
| API-046 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds/{holdId}/release` | POST | Release quarantine hold | No | — | `QuarantineHoldApiService.release()` | — | UI-028 |
| API-047 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/consignment-ownership` | POST | Transfer consignment ownership | No | — | `ConsignmentOwnershipApiService.transfer()` | — | UI-045 valuation |
| API-048 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/promotional-segregation` | POST | Segregate promotional stock | No | — | `CampaignRingFenceApiService.segregate()` | — | UI-046 campaign allocation |

**Target screens:** UI-006, UI-008, UI-020, UI-021, UI-028, UI-030, UI-031, UI-035, UI-038, UI-039, UI-045, UI-046

---

## M-05 — Procurement & Supplier (API-049 – API-065)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-049 | `/api/v1/suppliers` | POST | Register supplier | No | — | `SupplierApiService.create()` | — | UI-011 |
| API-050 | `/api/v1/suppliers` | GET | List suppliers | **Mock** | `MockDataService` (`UI-011`) | `SupplierApiService.list()` | Static supplier list | Supplier directory UI-011 |
| API-051 | `/api/v1/suppliers/{supplierCode}` | GET | Get supplier detail | No | — | `SupplierApiService.get()` | — | Supplier detail panel |
| API-052 | `/api/v1/suppliers/{supplierCode}` | PATCH | Update supplier | No | — | `SupplierApiService.update()` | — | Supplier editor |
| API-053 | `/api/v1/suppliers/{supplierCode}/deactivate` | POST | Deactivate supplier | No | — | `SupplierApiService.deactivate()` | — | Supplier lifecycle |
| API-054 | `/api/v1/procurement/requisitions` | POST | Create requisition | No | — | `PurchaseRequisitionApiService.create()` | — | UI-037 replenishment |
| API-055 | `/api/v1/procurement/requisitions/{requisitionId}` | GET | Get requisition detail | **Mock** | `MockDataService` (`UI-013`) | `PurchaseRequisitionApiService.get()` | Single static requisition | Detail view UI-013 |
| API-056 | `/api/v1/procurement/requisitions/{requisitionId}/approve` | POST | Approve requisition | No | — | `PurchaseRequisitionApiService.approve()` | — | Approval panel UI-013 |
| API-057 | `/api/v1/procurement/requisitions/{requisitionId}/reject` | POST | Reject requisition | No | — | `PurchaseRequisitionApiService.reject()` | — | Approval panel UI-013 |
| API-058 | `/api/v1/procurement/requisitions/{requisitionId}/convert-to-po` | POST | Convert to PO | No | — | `PurchaseRequisitionApiService.convertToPo()` | — | UI-013 convert panel |
| API-059 | `/api/v1/procurement/purchase-orders` | POST | Create purchase order | No | — | `PurchaseOrderApiService.create()` | — | UI-012 |
| API-060 | `/api/v1/procurement/purchase-orders` | GET | List open POs | **Mock** | `MockDataService` (`UI-012`, `UI-019`) | `PurchaseOrderApiService.list()` | Static PO array | PO list UI-012, supply tracking UI-019 |
| API-061 | `/api/v1/procurement/purchase-orders/{purchaseOrderId}` | GET | Get PO detail | No | — | `PurchaseOrderApiService.get()` | — | PO detail/amend UI-012 |
| API-062 | `/api/v1/procurement/purchase-orders/{purchaseOrderId}` | PATCH | Amend PO | No | — | `PurchaseOrderApiService.amend()` | — | PO editor UI-012 |
| API-063 | `/api/v1/procurement/purchase-orders/{purchaseOrderId}/cancel` | POST | Cancel PO | No | — | `PurchaseOrderApiService.cancel()` | — | PO lifecycle UI-012 |
| API-064 | `/api/v1/procurement/purchase-orders/{purchaseOrderId}/expected-deliveries` | POST | Schedule expected delivery | No | — | `PurchaseOrderApiService.scheduleDelivery()` | — | UI-014 inbound planning |
| API-065 | `/api/v1/procurement/purchase-orders/{purchaseOrderId}/validate-for-receipt` | GET | Validate PO for receipt | No | — | `PurchaseOrderValidationApiService.validate()` | — | UI-015 goods receipt |

**Target screens:** UI-011, UI-012, UI-013, UI-014, UI-015, UI-019, UI-037

**Spec gap:** No `GET /api/v1/procurement/requisitions` list endpoint — blocks UI-013/UI-037 queue browse (GAP-API-01).

---

## M-06 — Inbound Receiving (API-066 – API-080)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-066 | `/api/v1/inbound/goods-receipts` | POST | Initiate goods receipt | No | — | `GoodsReceiptApiService.create()` | — | UI-015 |
| API-067 | `/api/v1/inbound/goods-receipts` | GET | List goods receipts | No | — | `GoodsReceiptApiService.list()` | — | Receipt queue UI-015 |
| API-068 | `/api/v1/inbound/goods-receipts/{goodsReceiptId}` | GET | Get receipt detail | No | — | `GoodsReceiptApiService.get()` | — | Receipt workbench detail |
| API-069 | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/verify` | POST | Verify receipt lines | No | — | `GoodsReceiptApiService.verify()` | — | Line verification UI-015 |
| API-070 | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies` | POST | Document discrepancy | No | — | `ReceiptDiscrepancyApiService.create()` | — | UI-016 |
| API-071 | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies` | GET | List discrepancies | No | — | `ReceiptDiscrepancyApiService.list()` | — | UI-016 |
| API-072 | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies/{discrepancyId}/resolve` | POST | Resolve discrepancy | No | — | `ReceiptDiscrepancyApiService.resolve()` | — | Resolution panel UI-016 |
| API-073 | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/put-away` | POST | Confirm put-away | No | — | `PutAwayApiService.confirm()` | — | UI-017 |
| API-074 | `/api/v1/inbound/pending-put-away` | GET | List pending put-away | No | — | `PutAwayApiService.listPending()` | — | Put-away queue UI-017 |
| API-075 | `/api/v1/inbound/ad-hoc-receipts` | POST | Non-PO ad-hoc receipt | No | — | `AdHocReceiptApiService.create()` | — | UI-018 |
| API-076 | `/api/v1/inbound/return-receipts` | POST | Return receipt at dock | No | — | `ReturnReceiptApiService.create()` | — | UI-018; prefer API-128 for UI-043 |
| API-077 | `/api/v1/inbound/supplier-invoices` | POST | Register supplier invoice | No | — | `SupplierInvoiceApiService.create()` | — | UI-045 valuation |
| API-078 | `/api/v1/inbound/supplier-invoices/{invoiceId}` | GET | Get invoice / match status | No | — | `SupplierInvoiceApiService.get()` | — | Three-way match UI-045 |
| API-079 | `/api/v1/inbound/supplier-invoices/{invoiceId}/three-way-match` | POST | Execute three-way match | No | — | `SupplierInvoiceApiService.threeWayMatch()` | — | UI-045 |
| API-080 | `/api/v1/inbound/supplier-invoices/{invoiceId}/authorize-payment` | POST | Authorize payment | No | — | `SupplierInvoiceApiService.authorizePayment()` | — | UI-045 finance panel |

**Target screens:** UI-015, UI-016, UI-017, UI-018, UI-045

---

## M-07 — Order Fulfillment (API-081 – API-097)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-081 | `/api/v1/fulfillment/orders` | POST | Create/import order | No | — | `OrderApiService.create()` | — | UI-030 |
| API-082 | `/api/v1/fulfillment/orders` | GET | List orders | No | — | `OrderApiService.list()` | — | UI-034 order status search |
| API-083 | `/api/v1/fulfillment/orders/{orderId}` | GET | Get order detail | No | — | `OrderApiService.get()` | — | Order detail panels |
| API-084 | `/api/v1/fulfillment/orders/{orderId}/availability` | POST | Confirm availability | No | — | `AvailabilityApiService.checkOrder()` | — | UI-030, UI-021 |
| API-085 | `/api/v1/fulfillment/orders/{orderId}/confirm` | POST | Confirm order / reserve | No | — | `OrderApiService.confirm()` | — | UI-030 reservation |
| API-086 | `/api/v1/fulfillment/orders/{orderId}/cancel` | POST | Cancel order | No | — | `OrderApiService.cancel()` | — | UI-030 release flow |
| API-087 | `/api/v1/fulfillment/orders/{orderId}/multi-location-plan` | POST | Multi-location plan | No | — | `MultiLocationPlanApiService.create()` | — | UI-035 |
| API-088 | `/api/v1/fulfillment/orders/{orderId}/pick-lists` | POST | Assign pick work | No | — | `PickListApiService.create()` | — | UI-031 |
| API-089 | `/api/v1/fulfillment/orders/{orderId}/pick-lists/awaiting` | GET | Orders awaiting pick | No | — | `PickListApiService.listAwaiting()` | — | UI-031; per-order only (GAP-API-02) |
| API-090 | `/api/v1/fulfillment/orders/{orderId}/picks/{pickId}/verify` | POST | Verify pick | No | — | `PickVerificationApiService.verify()` | — | Pick verification UI-031 |
| API-091 | `/api/v1/fulfillment/orders/{orderId}/pack` | POST | Complete packing | No | — | `ShipmentApiService.pack()` | — | Packing panel UI-031 |
| API-092 | `/api/v1/fulfillment/orders/{orderId}/shipments` | POST | Dispatch shipment | No | — | `ShipmentApiService.ship()` | — | Shipment confirmation UI-031 |
| API-093 | `/api/v1/fulfillment/orders/{orderId}/partial-fulfillment` | POST | Partial fulfillment | No | — | `PartialFulfillmentApiService.create()` | — | UI-032 |
| API-094 | `/api/v1/fulfillment/orders/{orderId}/backorders` | POST | Create backorder | No | — | `BackorderApiService.create()` | — | UI-032 |
| API-095 | `/api/v1/fulfillment/backorders/{backorderId}/fulfill` | POST | Fulfill backorder | No | — | `BackorderApiService.fulfill()` | — | UI-032 |
| API-096 | `/api/v1/fulfillment/orders/{orderId}/exceptions` | POST | Raise exception | No | — | `FulfillmentExceptionApiService.create()` | — | UI-033 |
| API-097 | `/api/v1/fulfillment/orders/{orderId}/status` | GET | Get fulfillment status | No | — | `OrderStatusApiService.get()` | — | UI-034 timeline |

**Target screens:** UI-030, UI-031, UI-032, UI-033, UI-034, UI-035

---

## M-08 — Network Transfer (API-098 – API-107)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-098 | `/api/v1/transfers` | POST | Request transfer | No | — | `TransferApiService.create()` | — | UI-038 |
| API-099 | `/api/v1/transfers` | GET | List transfers | No | — | `TransferApiService.list()` | — | UI-038, UI-040 |
| API-100 | `/api/v1/transfers/{transferId}` | GET | Get transfer detail | No | — | `TransferApiService.get()` | — | Transfer detail views |
| API-101 | `/api/v1/transfers/{transferId}/approve` | POST | Approve transfer | No | — | `TransferApprovalApiService.approve()` | — | UI-039 |
| API-102 | `/api/v1/transfers/{transferId}/reject` | POST | Reject transfer | No | — | `TransferApprovalApiService.reject()` | — | UI-039 |
| API-103 | `/api/v1/transfers/{transferId}/dispatch` | POST | Dispatch transfer | No | — | `TransferDispatchApiService.dispatch()` | — | UI-040 |
| API-104 | `/api/v1/transfers/{transferId}/receive` | POST | Receive transfer | No | — | `TransferReceiveApiService.receive()` | — | UI-040 |
| API-105 | `/api/v1/transfers/{transferId}/cancel` | POST | Cancel in-transit | No | — | `TransferApiService.cancel()` | — | UI-040 |
| API-106 | `/api/v1/transfers/pending-approvals` | GET | Pending approvals | No | — | `PendingTransferApprovalApiService.list()` | Task widget uses hardcoded link | Wire UI-039, UI-002 task widget, UI-004 |
| API-107 | `/api/v1/transfers/in-transit` | GET | In-transit pipeline | No | — | `TransferInTransitApiService.list()` | — | UI-019, UI-040 |

**Target screens:** UI-004, UI-019, UI-038, UI-039, UI-040, UI-041

---

## M-09 — Inventory Accuracy (API-108 – API-123)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-108 | `/api/v1/accuracy/cycle-counts` | POST | Schedule cycle count | No | — | `CycleCountApiService.schedule()` | — | UI-023 |
| API-109 | `/api/v1/accuracy/cycle-counts` | GET | List cycle counts | No | — | `CycleCountApiService.list()` | — | Count queue UI-023 |
| API-110 | `/api/v1/accuracy/cycle-counts/{cycleCountId}` | GET | Get assignment (blind) | No | — | `CycleCountApiService.get()` | — | Count task UI-023 |
| API-111 | `/api/v1/accuracy/cycle-counts/{cycleCountId}/result` | POST | Submit count result | No | — | `CycleCountApiService.submitResult()` | — | Submission UI-023 |
| API-112 | `/api/v1/accuracy/physical-counts` | POST | Initiate physical count | No | — | `PhysicalCountApiService.initiate()` | — | UI-024 |
| API-113 | `/api/v1/accuracy/physical-counts/{physicalCountId}` | GET | Get count progress | No | — | `PhysicalCountApiService.get()` | — | Session UI-024 |
| API-114 | `/api/v1/accuracy/physical-counts/{physicalCountId}/results` | POST | Submit count results | No | — | `PhysicalCountApiService.submitResults()` | — | Team progress UI-024 |
| API-115 | `/api/v1/accuracy/physical-counts/{physicalCountId}/certify` | POST | Certify count complete | No | — | `PhysicalCountApiService.certify()` | — | Certification UI-024 |
| API-116 | `/api/v1/accuracy/adjustment-cases` | POST | Open adjustment case | No | — | `AdjustmentCaseApiService.create()` | — | UI-025, UI-026 |
| API-117 | `/api/v1/accuracy/adjustment-cases/{caseId}` | GET | Get case detail | No | — | `AdjustmentCaseApiService.get()` | — | Case detail UI-025–027 |
| API-118 | `/api/v1/accuracy/adjustment-cases/{caseId}/investigate` | POST | Document investigation | No | — | `AdjustmentCaseApiService.investigate()` | — | UI-025 |
| API-119 | `/api/v1/accuracy/adjustment-cases/{caseId}/variances/{varianceId}/approve` | POST | Approve variance | No | — | `AdjustmentCaseApiService.approveVariance()` | — | UI-025 SoD approval |
| API-120 | `/api/v1/accuracy/adjustment-cases/{caseId}/submit` | POST | Submit for approval | No | — | `AdjustmentCaseApiService.submit()` | — | UI-026, UI-027 |
| API-121 | `/api/v1/accuracy/adjustment-cases/{caseId}/approve` | POST | Approve adjustment | No | — | `AdjustmentCaseApiService.approve()` | — | UI-026, UI-027 |
| API-122 | `/api/v1/accuracy/adjustment-cases/{caseId}/reject` | POST | Reject adjustment | No | — | `AdjustmentCaseApiService.reject()` | — | UI-026, UI-027 |
| API-123 | `/api/v1/accuracy/pending-approvals` | GET | Pending adjustment approvals | No | — | `PendingApprovalsApiService.list()` | Task widget hardcoded "Variance Approvals" | Wire UI-025, UI-002, UI-004 |

**Target screens:** UI-023, UI-024, UI-025, UI-026, UI-027, UI-004

---

## M-10 — Returns Management (API-124 – API-131)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-124 | `/api/v1/returns/authorizations` | POST | Issue RMA | No | — | `ReturnAuthorizationApiService.create()` | — | UI-042 |
| API-125 | `/api/v1/returns/authorizations` | GET | List RMAs | No | — | `ReturnAuthorizationApiService.list()` | — | UI-042 |
| API-126 | `/api/v1/returns/authorizations/{returnAuthorizationId}` | GET | Get RMA detail | No | — | `ReturnAuthorizationApiService.get()` | — | RMA detail UI-042 |
| API-127 | `/api/v1/returns/authorizations/{returnAuthorizationId}/cancel` | POST | Cancel RMA | No | — | `ReturnAuthorizationApiService.cancel()` | — | UI-042 |
| API-128 | `/api/v1/returns/{returnId}/receive` | POST | Receive return goods | No | — | `ReturnReceiptApiService.receive()` | — | UI-043 (canonical path) |
| API-129 | `/api/v1/returns/{returnId}/inspect` | POST | Inspect return condition | No | — | `ReturnInspectionApiService.inspect()` | — | UI-043 |
| API-130 | `/api/v1/returns/{returnId}/disposition` | POST | Route disposition | No | — | `ReturnDispositionApiService.disposition()` | — | UI-043 restock/quarantine/write-off |
| API-131 | `/api/v1/returns/pending-receipts` | GET | Pending return receipts | No | — | `ReturnProcessingApiService.listPending()` | — | Receipt queue UI-043 |

**Target screens:** UI-042, UI-043

---

## M-11 — Commercial Campaign (API-132 – API-139)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-132 | `/api/v1/campaigns/allocations` | POST | Create allocation | No | — | `CampaignAllocationApiService.create()` | — | UI-046 |
| API-133 | `/api/v1/campaigns/allocations` | GET | List allocations | No | — | `CampaignAllocationApiService.list()` | — | UI-046 |
| API-134 | `/api/v1/campaigns/allocations/{allocationId}` | GET | Get allocation | No | — | `CampaignAllocationApiService.get()` | — | Allocation detail |
| API-135 | `/api/v1/campaigns/allocations/{allocationId}` | PATCH | Amend allocation | No | — | `CampaignAllocationApiService.update()` | — | Editor UI-046 |
| API-136 | `/api/v1/campaigns/allocations/{allocationId}/readiness` | POST | Evaluate readiness | No | — | `CampaignReadinessApiService.evaluate()` | — | Readiness panel UI-046 |
| API-137 | `/api/v1/campaigns/allocations/{allocationId}/release` | POST | Release allocation | No | — | `CampaignAllocationApiService.release()` | — | Post-campaign release |
| API-138 | `/api/v1/campaigns/allocations/{allocationId}/override` | POST | Override ring-fence | No | — | `CampaignAllocationApiService.override()` | — | Override workflow |
| API-139 | `/api/v1/campaigns/ring-fence/{locationCode}/{sku}` | GET | Check ring-fence | No | — | `CampaignRingFenceApiService.get()` | — | UI-030 reservation check |

**Target screens:** UI-030, UI-046

---

## M-12 — Identity & Access (API-140 – API-149)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-140 | `/api/v1/users` | POST | Provision user | No | — | `UserAccountApiService.create()` | — | UI-049 |
| API-141 | `/api/v1/users` | GET | List users | **Mock** | `MockDataService` (`UI-049`) | `UserAccountApiService.list()` | Static 2 users | User directory UI-049 |
| API-142 | `/api/v1/users/{userId}` | GET | Get user profile | No | — | `UserAccountApiService.get()` | — | User detail UI-049 |
| API-143 | `/api/v1/users/{userId}/roles` | POST | Assign role | No | — | `RoleAssignmentApiService.assign()` | — | Role panel UI-049 |
| API-144 | `/api/v1/users/{userId}/roles/{roleAssignmentId}` | DELETE | Revoke role | No | — | `RoleAssignmentApiService.revoke()` | — | UI-049 |
| API-145 | `/api/v1/users/{userId}/suspend` | POST | Suspend user | No | — | `UserAccountApiService.suspend()` | — | UI-049 |
| API-146 | `/api/v1/users/{userId}/deactivate` | POST | Deactivate user | No | — | `UserAccountApiService.deactivate()` | — | UI-049 |
| API-147 | `/api/v1/users/sync` | POST | HR directory sync | No | — | `UserDirectorySyncService.sync()` | — | Admin bulk sync |
| API-148 | `/api/v1/authorization/actions/evaluate` | POST | Evaluate action permission | No | — | `AuthorizationEvaluationApiService.evaluateAction()` | No permission checks in UI | Route guards + button visibility |
| API-149 | `/api/v1/authorization/location-scope/validate` | POST | Validate location scope | No | — | `LocationScopeValidationApiService.validate()` | Session badge shows scope but no validation | Scope enforcement on location-scoped routes |

**Target screens:** UI-049, UI-050; global permission enforcement

---

## M-13 — Inventory Intelligence (API-150 – API-172)

Read-only projection APIs. None consumed; several have loose mock equivalents in `MockDataService`.

| API | Endpoint | Method | Purpose | Consumed? | Mock screen | Service to create | Required improvements |
|-----|----------|--------|---------|-----------|-------------|-------------------|----------------------|
| API-150 | `/api/v1/intelligence/dashboard` | GET | Inventory summary dashboard | **Mock** | UI-002 | `DashboardApiService` | Replace KPI mock with live dashboard |
| API-151 | `/api/v1/intelligence/stock-status/summary` | GET | Aggregated stock status counts | **Mock** | UI-002 (`stockHealth`) | `StockStatusApiService` | Wire stock health panel |
| API-152 | `/api/v1/intelligence/stock-status/board` | GET | Network stock status board | No | — | `StockStatusApiService` | UI-020 status board |
| API-153 | `/api/v1/intelligence/availability/inquiries` | GET | Availability inquiry log | No | — | `AvailabilityInquiryLogApiService` | UI-021 history panel |
| API-154 | `/api/v1/intelligence/quarantine-register` | GET | Quarantine register | No | — | `QuarantineRegisterApiService` | UI-028, UI-044 |
| API-155 | `/api/v1/intelligence/movements` | GET | Movement history search | **Mock** | UI-022 | `MovementHistoryApiService` | Filterable query + export |
| API-156 | `/api/v1/intelligence/audit-trail` | GET | Audit trail query | **Mock** | UI-048 | `AuditTrailApiService` | UI-047, UI-048 |
| API-157 | `/api/v1/intelligence/audit-trail/export` | GET | Export audit evidence | No | — | `AuditEvidenceExportService` | Export action group |
| API-158 | `/api/v1/intelligence/alerts` | GET | Active operational alerts | **Mock** | UI-004 | `AlertApiService` | Replace header hardcoded count; UI-004 inbox |
| API-159 | `/api/v1/intelligence/alerts/{alertId}/acknowledge` | POST | Acknowledge alert | No | — | `AlertApiService.acknowledge()` | UI-004, UI-036 |
| API-160 | `/api/v1/intelligence/replenishment/recommendations` | GET | Replenishment recommendations | No | — | `ReplenishmentRecommendationApiService` | UI-036, UI-037, UI-041 |
| API-161 | `/api/v1/intelligence/procurement/open-pos` | GET | Open PO board | **Mock** | UI-012 | `OpenPurchaseOrdersApiService` | Inbound pipeline views |
| API-162 | `/api/v1/intelligence/procurement/inbound-calendar` | GET | Inbound supply calendar | No | — | `InboundCalendarApiService` | UI-014, UI-019 |
| API-163 | `/api/v1/intelligence/procurement/inbound-delays` | GET | Inbound delay log | **Mock** | UI-004 (alert type) | `InboundDelayApiService` | UI-014 delay panel |
| API-164 | `/api/v1/intelligence/fulfillment/backorders` | GET | Backorder pipeline | No | — | `BackorderApiService.listPipeline()` | UI-032, UI-034 |
| API-165 | `/api/v1/intelligence/fulfillment/exceptions` | GET | Fulfillment exceptions log | No | — | `FulfillmentExceptionApiService.list()` | UI-033 |
| API-166 | `/api/v1/intelligence/network/imbalance` | GET | Network imbalance analysis | No | — | `NetworkImbalanceApiService` | UI-041 rebalancing |
| API-167 | `/api/v1/intelligence/accuracy/shrinkage` | GET | Shrinkage analysis | **Mock** | UI-029 | `ShrinkageAnalysisApiService` | Report viewer integration |
| API-168 | `/api/v1/intelligence/accuracy/count-performance` | GET | Count accuracy metrics | No | — | `CountPerformanceApiService` | UI-023, UI-024, UI-044 |
| API-169 | `/api/v1/intelligence/campaigns/readiness` | GET | Campaign readiness status | No | — | `CampaignReadinessApiService` | UI-046, UI-004 |
| API-170 | `/api/v1/intelligence/kpis` | GET | Executive KPIs | **Mock** | UI-003 | `ExecutiveKpiApiService` | Executive dashboard UI-003 |
| API-171 | `/api/v1/intelligence/valuation/snapshots` | GET | Valuation snapshots | No | — | `ValuationSnapshotApiService` | UI-045 |
| API-172 | `/api/v1/intelligence/valuation/reconciliation` | GET | Valuation reconciliation | No | — | `ValuationReconciliationApiService` | UI-045 |

---

## Platform & Integration (API-173 – API-178)

| API | Endpoint | Method | Purpose | Consumed? | Service | Missing Integration | Incorrect Impl. | Required Improvements |
|-----|----------|--------|---------|-----------|---------|---------------------|-----------------|----------------------|
| API-173 | `/api/v1/auth/session` | GET | Validate session / user context | **Partial** | `AuthService` | `SessionService.loadSession()` | Reads `sessionStorage` only; no server validation | Call on app init and route guard; hydrate user from API |
| API-174 | `/api/v1/auth/logout` | POST | Terminate session | **Partial** | `AuthService.signOut()` | `SessionService.logout()` | Client-only clear; no `POST` | Invoke API before clearing local session |
| API-175 | `/api/v1/health` | GET | Health check | No | — | `HealthApiService` (ops only) | — | Optional dev status indicator |
| API-176 | `/api/v1/integrations/sales/orders` | POST | Import order from Sales/CRM | No | — | `SalesIntegrationService` | — | Backend ACL; not direct UI |
| API-177 | `/api/v1/integrations/sales/fulfillment-status` | GET | Fulfillment status feed | No | — | `FulfillmentStatusFeedService` | — | UI-034 external status tab |
| API-178 | `/api/v1/integrations/marketing/campaign-plans` | POST | Import campaign plan | No | — | `CampaignPlanIntegrationService` | — | UI-046 marketing integration |

---

## Consumption Summary by Module

| Module | API range | Count | HTTP consumed | Mock substitute | Partial (auth) |
|--------|-----------|-------|---------------|-----------------|----------------|
| M-01 Product Catalog | 001–010 | 10 | 0 | 2 | 0 |
| M-02 Warehouse Network | 011–021 | 11 | 0 | 1 | 0 |
| M-03 Inventory Governance | 022–031 | 10 | 0 | 1 | 0 |
| M-04 Inventory Balance | 032–048 | 17 | 0 | 1 | 0 |
| M-05 Procurement & Supplier | 049–065 | 17 | 0 | 4 | 0 |
| M-06 Inbound Receiving | 066–080 | 15 | 0 | 0 | 0 |
| M-07 Order Fulfillment | 081–097 | 17 | 0 | 0 | 0 |
| M-08 Network Transfer | 098–107 | 10 | 0 | 0 | 0 |
| M-09 Inventory Accuracy | 108–123 | 16 | 0 | 0 | 0 |
| M-10 Returns Management | 124–131 | 8 | 0 | 0 | 0 |
| M-11 Commercial Campaign | 132–139 | 8 | 0 | 0 | 0 |
| M-12 Identity & Access | 140–149 | 10 | 0 | 1 | 0 |
| M-13 Inventory Intelligence | 150–172 | 23 | 0 | 9 | 0 |
| Platform & Integration | 173–178 | 6 | 0 | 0 | 2 |
| **Total** | | **178** | **0** | **~19 shapes** | **2** |

---

## MockDataService → API Mapping

`MockDataService` does not call APIs. The table below maps which mock screen data **loosely corresponds** to which APIs once integrated.

| Mock key | Related APIs | Integration priority |
|----------|--------------|---------------------|
| UI-002 | API-150, 151, 152, 158 | P0 — landing dashboard |
| UI-003 | API-170 | P1 — executive KPIs |
| UI-004 | API-158, 159, 106, 123, 163, 169 | P0 — notification center |
| UI-005 | API-002, 003 | P0 — product catalog |
| UI-006 | API-010, 032, 017 | P1 — import workspace |
| UI-007 | API-012, 013 | P0 — locations |
| UI-008 | API-039, 040 | P1 — stock policies |
| UI-009 | API-006, 002 | P1 — ABC classification |
| UI-010 | API-023, 026–030 | P1 — governance |
| UI-011 | API-050, 051 | P1 — suppliers |
| UI-012 | API-060, 061, 161 | P0 — purchase orders |
| UI-013 | API-055–058 | P1 — requisitions (list gap) |
| UI-022 | API-155 | P1 — movement history |
| UI-029 | API-167 | P2 — shrinkage |
| UI-048 | API-156, 157 | P1 — audit trail |
| UI-049 | API-141, 142 | P1 — user admin |

All other UI mock keys (UI-014–021, UI-023–028, UI-030–047, UI-050) have **no mock data shapes** that meaningfully substitute for their API sets.

---

## Recommended Service Layer Architecture

```text
src/app/
├── core/
│   ├── http/
│   │   ├── api-client.ts              # Base HttpClient wrapper
│   │   ├── auth.interceptor.ts
│   │   ├── error.interceptor.ts
│   │   └── api-error.model.ts
│   └── session/
│       ├── session.service.ts         # API-173, API-174
│       └── session.model.ts
├── shared/
│   └── data-access/
│       ├── lookup/
│       │   ├── location-lookup.service.ts    # API-012
│       │   └── reason-code-lookup.service.ts # API-023
│       └── dto/                       # Shared response envelopes
└── features/
    └── {domain}/
        └── data-access/
            ├── {entity}.api.service.ts
            ├── {entity}.facade.ts
            ├── dto/
            └── mappers/
```

### Implementation Waves

| Wave | APIs | Rationale |
|------|------|-----------|
| **Wave 0** | API-173, 174, 148, 149 | Auth, session, permissions — prerequisite for all screens |
| **Wave 1** | API-150–152, 158–159, 002, 012, 033–037, 060 | Dashboard, catalog, locations, inventory visibility |
| **Wave 2** | API-066–074, 081–092, 098–107 | Inbound, fulfillment, transfers — operational core |
| **Wave 3** | API-108–123, 116–122 | Inventory accuracy and approvals |
| **Wave 4** | API-124–131, 132–139 | Returns and campaigns |
| **Wave 5** | API-140–147, 031, 155–157, 170–172 | Admin, audit, executive reporting |
| **Wave 6** | API-077–080, 171–172, 176–178 | Finance valuation and integrations |

### Deprecation Path for MockDataService

1. Introduce feature facades that delegate to `*ApiService`
2. Keep `MockDataService` behind `useMockData` environment flag during transition
3. Remove mock keys as each screen reaches API parity
4. Delete `MockDataService` when all 50 screens are integrated

---

## Document References

| Document | Path |
|----------|------|
| API Catalog (SRS) | `SRS/Inventory-Management-System-SRS.md` § API-001–178 |
| Detailed API specs | `SRS/API_Design/Complete-API-Specification*.md` |
| API gap analysis | `SRS/API_Design/API-Design-Architecture-Review.md` |
| Frontend services | `ims-frontend/src/app/core/services/` |
| Screen Coverage Matrix | `gap_frontend/Screen-Coverage-Matrix.md` |
| Component Coverage Matrix | `gap_frontend/Component-Coverage-Matrix.md` |

---

*End of matrix.*
