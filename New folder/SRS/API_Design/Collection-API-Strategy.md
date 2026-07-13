# Collection API Strategy
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-006 |
| **Document Title** | Collection API Strategy — Pagination, Filtering, Sorting, Searching |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Backend Architect |
| **Source Documents** | SRS-API-001, SRS-API-002, SRS-API-003, SRS-API-004, SRS-API-005 |
| **Date** | July 6, 2026 |
| **Scope** | All `GET` collection, search, and list endpoints under `/api/v1` |

### Purpose

Defines a **consistent, REST-aligned strategy** for paginating, filtering, sorting, and searching collection responses across the IMS API surface. Every collection endpoint follows one of five collection profiles with explicit query parameters, defaults, limits, and response metadata.

---

## Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Resource-oriented URLs** | Collections at plural nouns (`/products`, `/transfers`); filters as query params, not path segments |
| **Predictable pagination** | Offset (`page`/`pageSize`) by default; cursor for high-volume feeds |
| **Whitelist sorting** | `sortBy` accepts only documented fields per endpoint — unknown values → `400` |
| **Explicit filter semantics** | Each filter documents match type: exact, prefix, partial, range, enum |
| **Scope by default** | Results constrained to caller's authorized locations unless network-scoped |
| **Empty is success** | `200 OK` with empty `data[]` — never `404` for zero matches |
| **Stable ordering** | Tie-breaker sort on primary key (`sku`, `id`) when not explicitly sorted |
| **No over-fetching** | `pageSize` capped per profile; export endpoints use separate limits |

---

## Global Query Parameter Standards

### Pagination (Offset — Profile `P`)

| Parameter | Type | Default | Limits | Description |
|-----------|------|---------|--------|-------------|
| `page` | integer | `1` | min `1` | 1-based page index |
| `pageSize` | integer | `20` | min `1`, max per profile | Records per page |

**Behavior:** `totalPages = ceil(totalElements / pageSize)`. Requesting `page` beyond `totalPages` returns `200` with empty `data[]` and correct metadata.

### Pagination (Cursor — Profile `C`)

| Parameter | Type | Default | Limits | Description |
|-----------|------|---------|--------|-------------|
| `cursor` | string | — | opaque token | Position from prior response `links.next` |
| `limit` | integer | `100` | min `1`, max `500` | Records per page |

**Behavior:** No `totalElements` guarantee. Response includes `hasMore` boolean and `nextCursor`.

### Sorting

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `sortBy` | string | per endpoint | Whitelisted field name |
| `sortDirection` | string | per endpoint | `ASC` or `DESC` |

**Rules:**
- Invalid `sortBy` → `400 VAL_INVALID_ENUM`
- `sortDirection` without `sortBy` → ignored; default sort applies
- Compound default: primary business field ASC + `id` ASC as tie-breaker

### Filtering Conventions

| Match Type | Syntax | Example |
|------------|--------|---------|
| **Exact** | param=value | `sku=WIDGET-01` |
| **Prefix** | param=value (documented) | `sku=WID` matches `WIDGET-01` |
| **Partial (contains)** | param=value, case-insensitive | `name=bolt` |
| **Enum** | param=ENUM_VALUE | `status=OPEN` |
| **Boolean** | param=true\|false | `isActive=true` |
| **Date range** | `from`/`to` or `startDate`/`endDate` | inclusive both ends |
| **Multi-value** | repeat param or comma-separated | `locationCode=WH-EAST&locationCode=WH-WEST` |
| **Null-safe** | omit param = no filter | — |

### Searching

| Parameter | Type | Description |
|-----------|------|-------------|
| `q` | string | Cross-field search where supported (max 200 chars) |
| `search` | string | Alternate name on user directory — same semantics as `q` |

**Rules:** `q` applies OR across documented fields. Combining `q` with field filters = AND logic. Minimum 2 characters for `q` unless exact ID lookup field is used.

### Common Date Range Parameters

| Parameter | Required | Max Range | Used By |
|-----------|----------|-----------|---------|
| `startDate` / `endDate` | varies | 365 days (audit); 90 days (calendar) | Logs, movements, KPIs |
| `*From` / `*To` | optional pairs | same | PO delivery, transfers, counts |

---

## Response Metadata Standards

### `PagedResponse<T>` (Offset — extends SRS-API-003)

```json
{
  "data": [ ],
  "page": 1,
  "pageSize": 20,
  "totalElements": 156,
  "totalPages": 8,
  "sort": {
    "field": "name",
    "direction": "ASC"
  },
  "appliedFilters": {
    "lifecycleStatus": "ACTIVE"
  },
  "links": {
    "self": "/api/v1/products?page=1&pageSize=20&lifecycleStatus=ACTIVE",
    "first": "/api/v1/products?page=1&pageSize=20&lifecycleStatus=ACTIVE",
    "prev": null,
    "next": "/api/v1/products?page=2&pageSize=20&lifecycleStatus=ACTIVE",
    "last": "/api/v1/products?page=8&pageSize=20&lifecycleStatus=ACTIVE"
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `data` | array | Result items for current page |
| `page` | integer | Current page (echo) |
| `pageSize` | integer | Page size (echo) |
| `totalElements` | long | Total matching records |
| `totalPages` | integer | Total pages |
| `sort` | object | Applied sort field and direction |
| `appliedFilters` | object | Echo of non-pagination query params |
| `links` | object | RFC 8288-style pagination URIs (relative) |

### `CursorPagedResponse<T>` (Cursor)

```json
{
  "data": [ ],
  "limit": 100,
  "hasMore": true,
  "nextCursor": "eyJvcmRlcklkIjoiLi4uIn0",
  "sort": { "field": "updatedAt", "direction": "DESC" },
  "appliedFilters": { "status": "SHIPPED" }
}
```

### `BoundedListResponse<T>` (Small nested collections)

```json
{
  "data": [ ],
  "totalElements": 4,
  "truncated": false
}
```

Used when parent scope bounds result set (e.g. discrepancies on one receipt). Pagination optional; if `totalElements > maxPageSize`, pagination required.

### Response Headers

| Header | When |
|--------|------|
| `X-Total-Count` | Offset pagination — duplicates `totalElements` for simple clients |
| `Link` | Optional RFC 5988 equivalent of `links` object |

---

## Collection Profiles

| Profile | Code | Default `pageSize` | Max `pageSize` | Sort | Typical Use |
|---------|------|-------------------|----------------|------|-------------|
| **Standard Collection** | `P-STD` | 20 | 100 | Yes | Master data, transactional lists |
| **Operational Queue** | `P-OPS` | 20 | 50 | Yes | Pending approvals, put-away queues |
| **Audit / Log** | `P-LOG` | 50 | 100 | Yes (timestamp DESC) | Movements, audit trail, inquiries |
| **Intelligence Board** | `P-INT` | 20 | 100 | Yes | Dashboards, alerts, boards |
| **Integration Feed** | `C-FED` | 100 | 500 | Fixed | CRM fulfillment status feed |
| **Bounded Nested** | `B-NST` | all | 50 | Limited | Child collections under parent resource |
| **Report / Aggregate** | `R-AGG` | n/a | n/a | n/a | Summaries, calendars, KPIs — no pagination |

---

## Endpoint Catalog

Legend: **Profile** = collection profile code. **P/S/F** = Pagination / Sort / Filter supported.

---

### M-01 — Product Catalog

#### API-002 — `GET /api/v1/products`

| Attribute | Specification |
|-----------|---------------|
| **Profile** | `P-STD` |
| **DTO** | `SearchProductsQuery` |

| Parameter | Type | Match | Default | Notes |
|-----------|------|-------|---------|-------|
| `name` | string | partial | — | Display name contains |
| `sku` | string | prefix | — | SKU starts-with |
| `categoryCode` | string | exact | — | |
| `lifecycleStatus` | enum | exact | — | `ACTIVE`, `INACTIVE`, `DISCONTINUED` |
| `abcClass` | enum | exact | — | `A`, `B`, `C` |
| `barcode` | string | exact | — | |
| `q` | string | search | — | Searches `name`, `sku`, `barcode` (OR) |
| `page`, `pageSize` | int | — | 1, 20 | max 100 |
| `sortBy` | enum | — | `sku` | `sku`, `name`, `categoryCode`, `lifecycleStatus` |
| `sortDirection` | enum | — | `ASC` | |

**Default behavior:** All active products in catalog scope; sort `sku ASC`.  
**Response:** `PagedResponse<ProductSummaryResponse>`

---

#### API-008 — `GET /api/v1/products/categories/{categoryCode}/products`

| Attribute | Specification |
|-----------|---------------|
| **Profile** | `P-STD` |
| **Path filter** | `categoryCode` (exact, required) |

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `lifecycleStatus` | enum | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `sku` (`sku`, `name`) |
| `sortDirection` | enum | — | `ASC` |

**Default behavior:** Products in category; active only when `lifecycleStatus` omitted.  
**Response:** `PagedResponse<ProductSummaryResponse>`

---

### M-02 — Warehouse Network

#### API-012 — `GET /api/v1/locations`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `operationalStatus` | enum | exact | `ACTIVE` |
| `locationType` | enum | exact | — |
| `parentLocationCode` | string | exact | — |
| `name` | string | partial | — |
| `q` | string | search | — | `name`, `locationCode` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `locationCode` (`locationCode`, `name`, `operationalStatus`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD` | **Scope:** User-authorized locations  
**Response:** `PagedResponse<LocationSummaryResponse>`

---

#### API-016 — `GET /api/v1/locations/{locationCode}/storage-positions`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `positionType` | enum | exact | — |
| `zone` | string | exact | — |
| `isActive` | boolean | exact | `true` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `positionCode` (`positionCode`, `zone`, `aisle`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD` | **Path:** `locationCode` required  
**Response:** `PagedResponse<StoragePositionResponse>`

---

### M-03 — Inventory Governance

#### API-023 — `GET /api/v1/governance/reason-codes`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `transactionType` | enum | exact | — |
| `isActive` | boolean | exact | `true` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `code` (`code`, `description`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD` (reference data, typically small)  
**Response:** `PagedResponse<ReasonCodeResponse>`

---

### M-04 — Inventory Balance

#### API-033 — `GET /api/v1/inventory/stock-positions`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `sku` | string | exact/prefix | — |
| `locationCode` | string | exact | — |
| `stockStatus` | enum | exact | — | `IN_STOCK`, `LOW_STOCK`, `OUT_OF_STOCK`, `OVERSTOCK` |
| `abcClass` | enum | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `sku` (`sku`, `locationCode`, `atp`, `stockStatus`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD` | **Required:** at least one of `sku` or `locationCode` (VR-054)  
**Scope:** User location scope on `locationCode`  
**Response:** `PagedResponse<StockPositionSummaryResponse>`

---

#### API-041 — `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/lots`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `includeQuarantined` | boolean | exact | `false` |
| `page`, `pageSize` | int | — | 1, 20 (optional) |
| `sortBy` | enum | — | `expirationDate` (`expirationDate`, `lotNumber`) |
| `sortDirection` | enum | — | `ASC` (FEFO-friendly) |

**Profile:** `B-NST` | max 50 lots; pagination required if > 50  
**Response:** `BoundedListResponse<LotQuantityResponse>` or `PagedResponse` when paginated

---

### M-05 — Procurement & Supplier

#### API-050 — `GET /api/v1/suppliers`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `isActive` | boolean | exact | `true` |
| `name` | string | partial | — |
| `q` | string | search | — | `name`, `supplierCode` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `supplierCode` (`supplierCode`, `name`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD`  
**Response:** `PagedResponse<SupplierSummaryResponse>`

---

#### API-060 — `GET /api/v1/procurement/purchase-orders`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `status` | enum | exact | `OPEN`,`PARTIAL` |
| `supplierCode` | string | exact | — |
| `receivingLocationCode` | string | exact | — |
| `expectedDeliveryFrom` | date | range start | — |
| `expectedDeliveryTo` | date | range end | — |
| `isOverdue` | boolean | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `expectedDeliveryDate` (`expectedDeliveryDate`, `purchaseOrderId`, `supplierCode`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD` | **Cross-field:** delivery date range  
**Scope:** User location scope  
**Response:** `PagedResponse<PurchaseOrderSummaryResponse>`

---

### M-06 — Inbound Receiving

#### API-067 — `GET /api/v1/inbound/goods-receipts`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `receivingLocationCode` | string | exact | — |
| `status` | enum | exact | — |
| `purchaseOrderId` | uuid | exact | — |
| `receivedFrom` / `receivedTo` | date | range | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `receivedAt` (`receivedAt`, `goodsReceiptId`, `status`) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-STD`  
**Response:** `PagedResponse<GoodsReceiptSummaryResponse>`

---

#### API-071 — `GET /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `status` | enum | exact | `OPEN` |
| `page`, `pageSize` | int | — | 1, 20 (optional) |
| `sortBy` | enum | — | `recordedAt` (`recordedAt`, `discrepancyType`) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `B-NST` | max 50 without pagination  
**Response:** `BoundedListResponse<ReceiptDiscrepancyResponse>`

---

#### API-074 — `GET /api/v1/inbound/pending-put-away`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | required |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `verifiedAt` (`verifiedAt`, `goodsReceiptId`) |
| `sortDirection` | enum | — | `ASC` (FIFO queue) |

**Profile:** `P-OPS` | max pageSize 50  
**Response:** `PagedResponse<PendingPutAwayResponse>`

---

### M-07 — Order Fulfillment

#### API-082 — `GET /api/v1/fulfillment/orders`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `status` | enum | exact | — |
| `shipFromLocationCode` | string | exact | — |
| `customerReference` | string | exact | — |
| `externalOrderReference` | string | exact | — |
| `orderDateFrom` / `orderDateTo` | date | range | — |
| `q` | string | search | — | `externalOrderReference`, `customerReference`, `orderId` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `orderDate` (`orderDate`, `status`, `orderId`) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-STD`  
**Response:** `PagedResponse<CustomerOrderSummaryResponse>`

---

#### API-089 — `GET /api/v1/fulfillment/orders/{orderId}/pick-lists/awaiting`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | — |

**Profile:** `B-NST` | No pagination — returns pick lists for single order (typically ≤ 10)  
**Response:** `BoundedListResponse<PickListSummaryResponse>`

---

### M-08 — Network Transfer

#### API-099 — `GET /api/v1/transfers`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `status` | enum | exact | — |
| `sourceLocationCode` | string | exact | — |
| `destinationLocationCode` | string | exact | — |
| `sku` | string | exact | — |
| `requestedFrom` / `requestedTo` | date | range | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `requestedAt` (`requestedAt`, `status`, `transferId`) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-STD`  
**Response:** `PagedResponse<StockTransferSummaryResponse>`

---

#### API-106 — `GET /api/v1/transfers/pending-approvals`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `sourceLocationCode` | string | exact | — |
| `destinationLocationCode` | string | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `requestedAt` (fixed whitelist) |
| `sortDirection` | enum | — | `ASC` (oldest first) |

**Profile:** `P-OPS` | max pageSize 50 | implicit filter `status=REQUESTED`  
**Response:** `PagedResponse<StockTransferSummaryResponse>`

---

#### API-107 — `GET /api/v1/transfers/in-transit`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | — | source OR destination |
| `sku` | string | exact | — |
| `isOverdue` | boolean | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `dispatchedAt` (`dispatchedAt`, `transferId`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-OPS` | implicit filter `status=IN_TRANSIT`  
**Response:** `PagedResponse<InTransitStockResponse>`

---

### M-09 — Inventory Accuracy

#### API-109 — `GET /api/v1/accuracy/cycle-counts`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | — |
| `status` | enum | exact | — |
| `sku` | string | exact | — |
| `scheduledFrom` / `scheduledTo` | date | range | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `scheduledDate` (`scheduledDate`, `priority`, `status`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD`  
**Response:** `PagedResponse<CycleCountSummaryResponse>`

---

#### API-123 — `GET /api/v1/accuracy/pending-approvals`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | — |
| `caseType` | enum | exact | — | `COUNT_VARIANCE`, `ADJUSTMENT`, `WRITE_OFF` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `submittedAt` (`submittedAt`, `caseType`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-OPS` | max pageSize 50  
**Response:** `PagedResponse<AdjustmentCaseSummaryResponse>`

---

### M-10 — Returns Management

#### API-125 — `GET /api/v1/returns/authorizations`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `status` | enum | exact | — |
| `originalOrderId` | uuid | exact | — |
| `customerReference` | string | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `authorizedAt` (`authorizedAt`, `status`) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-STD`  
**Response:** `PagedResponse<ReturnAuthorizationSummaryResponse>`

---

#### API-131 — `GET /api/v1/returns/pending-receipts`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `authorizedAt` |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-OPS` | implicit filter status `AUTHORIZED`/`IN_TRANSIT`  
**Response:** `PagedResponse<PendingReturnReceiptResponse>`

---

### M-11 — Commercial Campaign

#### API-133 — `GET /api/v1/campaigns/allocations`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `campaignId` | string | exact | — |
| `status` | enum | exact | — |
| `locationCode` | string | exact | — |
| `activeOnDate` | date | exact | — | allocations active on date |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `campaignStartDate` (`campaignStartDate`, `campaignId`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD`  
**Response:** `PagedResponse<PromotionalAllocationSummaryResponse>`

---

### M-12 — Identity & Access

#### API-141 — `GET /api/v1/users`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `status` | enum | exact | — |
| `roleCode` | string | exact | — |
| `locationCode` | string | exact | — | users with scope at location |
| `search` | string | partial | — | `displayName`, `email`, `userId` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `displayName` (`displayName`, `userId`, `email`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-STD` | Admin scope required  
**Response:** `PagedResponse<UserAccountSummaryResponse>`

---

### M-13 — Inventory Intelligence

#### API-152 — `GET /api/v1/intelligence/stock-status/board`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCodes` | string[] | exact multi | authorized locations |
| `stockStatus` | enum | exact | — |
| `sku` | string | exact/prefix | — |
| `abcClass` | enum | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `stockStatus` (`stockStatus`, `sku`, `atp`) |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-INT`  
**Response:** `PagedResponse<StockStatusBoardItemResponse>`

---

#### API-153 — `GET /api/v1/intelligence/availability/inquiries`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `sku` | string | exact | — |
| `locationCode` | string | exact | — |
| `userId` | string | exact | — |
| `startDate` / `endDate` | date | range | last 30 days |
| `page`, `pageSize` | int | — | 1, 50 |
| `sortBy` | enum | — | `inquiredAt` (fixed) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-LOG` | max range 365 days  
**Response:** `PagedResponse<AvailabilityInquiryLogEntryResponse>`

---

#### API-154 — `GET /api/v1/intelligence/quarantine-register`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | — |
| `holdReason` | enum | exact | — |
| `sku` | string | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `heldAt` (`heldAt`, `sku`, `holdReason`) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-INT`  
**Response:** `PagedResponse<QuarantineRegisterEntryResponse>`

---

#### API-155 — `GET /api/v1/intelligence/movements`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `sku` | string | exact | — |
| `locationCode` | string | exact | — |
| `userId` | string | exact | — |
| `movementType` | enum | exact | — |
| `startDate` / `endDate` | date | range | **required**; max 365 days |
| `page`, `pageSize` | int | — | 1, 50 |
| `sortBy` | enum | — | `occurredAt` (fixed) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-LOG` | Recommend ≥1 filter (VR-154)  
**Response:** `PagedResponse<MovementHistoryEntryResponse>`

---

#### API-156 — `GET /api/v1/intelligence/audit-trail`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `entityType` | string | exact | — |
| `entityId` | string | exact | — |
| `userId` | string | exact | — |
| `action` | string | exact | — |
| `startDate` / `endDate` | date | range | **required**; max 365 days |
| `page`, `pageSize` | int | — | 1, 50 |
| `sortBy` | enum | — | `occurredAt` (fixed) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-LOG`  
**Response:** `PagedResponse<AuditTrailEntryResponse>`

---

#### API-157 — `GET /api/v1/intelligence/audit-trail/export`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `startDate` / `endDate` | date | range | **required**; max 365 days |
| `entityTypes` | string[] | multi | max 20 types |
| `locationCodes` | string[] | multi | authorized only |
| `format` | enum | exact | `CSV` |

**Profile:** `R-AGG` | No pagination — async export if > 100k rows; returns `202` with `exportJobId`  
**Response:** File stream (`200`) or `ExportJobResponse` (`202`)

---

#### API-158 — `GET /api/v1/intelligence/alerts`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `alertType` | enum | exact | — |
| `severity` | enum | exact | — |
| `locationCode` | string | exact | — |
| `acknowledged` | boolean | exact | `false` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `severity` (`severity`, `raisedAt`) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-INT` | Severity sort: CRITICAL → WARNING → INFO  
**Response:** `PagedResponse<OperationalAlertResponse>`

---

#### API-160 — `GET /api/v1/intelligence/replenishment/recommendations`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | — |
| `sku` | string | exact | — |
| `recommendationAction` | enum | exact | — |
| `acknowledged` | boolean | exact | — |
| `startDate` / `endDate` | date | range | optional |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `recommendedAt` |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-INT`  
**Response:** `PagedResponse<ReplenishmentRecommendationResponse>`

---

#### API-161 — `GET /api/v1/intelligence/procurement/open-pos`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `receivingLocationCode` | string | exact | — |
| `supplierCode` | string | exact | — |
| `isOverdue` | boolean | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `expectedDeliveryDate` |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-INT` | Projection of open PO lines  
**Response:** `PagedResponse<OpenPurchaseOrderBoardItemResponse>`

---

#### API-162 — `GET /api/v1/intelligence/procurement/inbound-calendar`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `startDate` / `endDate` | date | range | **required**; max **90 days** |
| `receivingLocationCode` | string | exact | — |
| `supplierCode` | string | exact | — |

**Profile:** `R-AGG` | Calendar buckets by date — no pagination  
**Response:** `InboundSupplyCalendarResponse` (date-keyed arrays)

---

#### API-163 — `GET /api/v1/intelligence/procurement/inbound-delays`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `receivingLocationCode` | string | exact | — |
| `supplierCode` | string | exact | — |
| `startDate` / `endDate` | date | range | optional |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `delayDays` (`delayDays`, `expectedArrivalDate`) |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-LOG`  
**Response:** `PagedResponse<InboundDelayLogEntryResponse>`

---

#### API-164 — `GET /api/v1/intelligence/fulfillment/backorders`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `sku` | string | exact | — |
| `locationCode` | string | exact | — |
| `prioritySort` | boolean | exact | `true` |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | policy priority when `prioritySort=true`; else `backorderDate` |
| `sortDirection` | enum | — | `ASC` |

**Profile:** `P-OPS` | BR-028 priority policy (VR-102)  
**Response:** `PagedResponse<BackorderPipelineItemResponse>`

---

#### API-165 — `GET /api/v1/intelligence/fulfillment/exceptions`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `locationCode` | string | exact | — |
| `exceptionType` | enum | exact | — |
| `status` | enum | exact | `OPEN` |
| `startDate` / `endDate` | date | range | optional |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `raisedAt` |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-LOG`  
**Response:** `PagedResponse<FulfillmentExceptionLogEntryResponse>`

---

#### API-166 — `GET /api/v1/intelligence/network/imbalance`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `sku` | string | exact | — |
| `sourceLocationCode` | string | exact | — |
| `destinationLocationCode` | string | exact | — |
| `includeRecommendations` | boolean | exact | `true` |

**Profile:** `R-AGG` | Analysis result — no pagination; max 500 imbalance rows inline  
**Response:** `NetworkImbalanceAnalysisResponse`

---

#### API-167 — `GET /api/v1/intelligence/accuracy/shrinkage`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `startDate` / `endDate` | date | range | **required** |
| `locationCode` | string | exact | — |
| `categoryCode` | string | exact | — |
| `reasonCode` | string | exact | — |
| `groupBy` | enum | exact | `SKU` |

**Profile:** `R-AGG` | Aggregated analysis — no pagination  
**Response:** `ShrinkageAnalysisResponse`

---

#### API-168 — `GET /api/v1/intelligence/accuracy/count-performance`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `startDate` / `endDate` | date | range | **required** |
| `locationCode` | string | exact | — |
| `countType` | enum | exact | `ALL` |
| `abcClass` | enum | exact | — |
| `excludePendingVariances` | boolean | exact | `true` |

**Profile:** `R-AGG`  
**Response:** `CountPerformanceMetricsResponse`

---

#### API-169 — `GET /api/v1/intelligence/campaigns/readiness`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `campaignId` | string | exact | — |
| `locationCode` | string | exact | — |
| `readinessStatus` | enum | exact | — |
| `daysUntilStart` | integer | max | — |

**Profile:** `P-INT` | Optional pagination when result > 100: `page`, `pageSize`  
**Response:** `PagedResponse<CampaignReadinessStatusResponse>` or array if ≤ 100

---

#### API-170 — `GET /api/v1/intelligence/kpis`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `startDate` / `endDate` | date | range | **required** |
| `kpiCodes` | string[] | multi | all configured |
| `locationCodes` | string[] | multi | authorized |
| `compareToTarget` | boolean | exact | `true` |

**Profile:** `R-AGG`  
**Response:** `InventoryKpisResponse`

---

#### API-171 — `GET /api/v1/intelligence/valuation/snapshots`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `periodEndDate` | date | exact | — |
| `startDate` / `endDate` | date | range | optional |
| `locationCode` | string | exact | — |
| `page`, `pageSize` | int | — | 1, 20 |
| `sortBy` | enum | — | `periodEndDate` |
| `sortDirection` | enum | — | `DESC` |

**Profile:** `P-INT`  
**Response:** `PagedResponse<ValuationSnapshotSummaryResponse>`

---

#### API-172 — `GET /api/v1/intelligence/valuation/reconciliation`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `periodEndDate` | date | exact | **required** |
| `locationCode` | string | exact | — |
| `varianceThresholdPercent` | decimal | min/max | policy default |
| `includeGlComparison` | boolean | exact | `true` |

**Profile:** `R-AGG`  
**Response:** `ValuationReconciliationResponse`

---

#### API-150 / API-151 — Dashboard & summary (non-paginated)

| API | Profile | Key Parameters | Response |
|-----|---------|----------------|----------|
| API-150 | `R-AGG` | `scope`, `locationCode` (conditional), `asOfTimestamp` | `InventoryDashboardResponse` |
| API-151 | `R-AGG` | `locationCode`, `categoryCode`, `abcClass` | `StockStatusSummaryResponse` |

---

### Platform & Integration

#### API-177 — `GET /api/v1/integrations/sales/fulfillment-status`

| Parameter | Type | Match | Default |
|-----------|------|-------|---------|
| `externalSystemCode` | string | exact | **required** |
| `updatedSince` | instant | range start | — |
| `externalOrderId` | string | exact | — |
| `status` | enum | exact | — |
| `cursor` | string | — | — |
| `limit` | int | — | 100 |

**Profile:** `C-FED` | Cursor pagination; sort fixed `updatedAt DESC`  
**Response:** `CursorPagedResponse<FulfillmentStatusFeedItemResponse>`

---

## Collection Endpoint Index

| API | Endpoint | Profile | Pagination | Sort | Filter | Search (`q`) |
|-----|----------|---------|------------|------|--------|--------------|
| API-002 | `/products` | P-STD | ✓ | ✓ | ✓ | ✓ |
| API-008 | `/products/categories/{code}/products` | P-STD | ✓ | ✓ | ✓ | — |
| API-012 | `/locations` | P-STD | ✓ | ✓ | ✓ | ✓ |
| API-016 | `/locations/{code}/storage-positions` | P-STD | ✓ | ✓ | ✓ | — |
| API-023 | `/governance/reason-codes` | P-STD | ✓ | ✓ | ✓ | — |
| API-033 | `/inventory/stock-positions` | P-STD | ✓ | ✓ | ✓ | — |
| API-041 | `/inventory/.../lots` | B-NST | optional | ✓ | ✓ | — |
| API-050 | `/suppliers` | P-STD | ✓ | ✓ | ✓ | ✓ |
| API-060 | `/procurement/purchase-orders` | P-STD | ✓ | ✓ | ✓ | — |
| API-067 | `/inbound/goods-receipts` | P-STD | ✓ | ✓ | ✓ | — |
| API-071 | `/inbound/.../discrepancies` | B-NST | optional | ✓ | ✓ | — |
| API-074 | `/inbound/pending-put-away` | P-OPS | ✓ | ✓ | ✓ | — |
| API-082 | `/fulfillment/orders` | P-STD | ✓ | ✓ | ✓ | ✓ |
| API-089 | `/fulfillment/orders/{id}/pick-lists/awaiting` | B-NST | — | — | ✓ | — |
| API-099 | `/transfers` | P-STD | ✓ | ✓ | ✓ | — |
| API-106 | `/transfers/pending-approvals` | P-OPS | ✓ | ✓ | ✓ | — |
| API-107 | `/transfers/in-transit` | P-OPS | ✓ | ✓ | ✓ | — |
| API-109 | `/accuracy/cycle-counts` | P-STD | ✓ | ✓ | ✓ | — |
| API-123 | `/accuracy/pending-approvals` | P-OPS | ✓ | ✓ | ✓ | — |
| API-125 | `/returns/authorizations` | P-STD | ✓ | ✓ | ✓ | — |
| API-131 | `/returns/pending-receipts` | P-OPS | ✓ | ✓ | ✓ | — |
| API-133 | `/campaigns/allocations` | P-STD | ✓ | ✓ | ✓ | — |
| API-141 | `/users` | P-STD | ✓ | ✓ | ✓ | ✓ (`search`) |
| API-152 | `/intelligence/stock-status/board` | P-INT | ✓ | ✓ | ✓ | — |
| API-153 | `/intelligence/availability/inquiries` | P-LOG | ✓ | fixed | ✓ | — |
| API-154 | `/intelligence/quarantine-register` | P-INT | ✓ | ✓ | ✓ | — |
| API-155 | `/intelligence/movements` | P-LOG | ✓ | fixed | ✓ | — |
| API-156 | `/intelligence/audit-trail` | P-LOG | ✓ | fixed | ✓ | — |
| API-157 | `/intelligence/audit-trail/export` | R-AGG | — | — | ✓ | — |
| API-158 | `/intelligence/alerts` | P-INT | ✓ | ✓ | ✓ | — |
| API-160 | `/intelligence/replenishment/recommendations` | P-INT | ✓ | ✓ | ✓ | — |
| API-161 | `/intelligence/procurement/open-pos` | P-INT | ✓ | ✓ | ✓ | — |
| API-162 | `/intelligence/procurement/inbound-calendar` | R-AGG | — | — | ✓ | — |
| API-163 | `/intelligence/procurement/inbound-delays` | P-LOG | ✓ | ✓ | ✓ | — |
| API-164 | `/intelligence/fulfillment/backorders` | P-OPS | ✓ | policy | ✓ | — |
| API-165 | `/intelligence/fulfillment/exceptions` | P-LOG | ✓ | ✓ | ✓ | — |
| API-166 | `/intelligence/network/imbalance` | R-AGG | — | — | ✓ | — |
| API-167 | `/intelligence/accuracy/shrinkage` | R-AGG | — | — | ✓ | — |
| API-168 | `/intelligence/accuracy/count-performance` | R-AGG | — | — | ✓ | — |
| API-169 | `/intelligence/campaigns/readiness` | P-INT | conditional | — | ✓ | — |
| API-170 | `/intelligence/kpis` | R-AGG | — | — | ✓ | — |
| API-171 | `/intelligence/valuation/snapshots` | P-INT | ✓ | ✓ | ✓ | — |
| API-172 | `/intelligence/valuation/reconciliation` | R-AGG | — | — | ✓ | — |
| API-150 | `/intelligence/dashboard` | R-AGG | — | — | ✓ | — |
| API-151 | `/intelligence/stock-status/summary` | R-AGG | — | — | ✓ | — |
| API-177 | `/integrations/sales/fulfillment-status` | C-FED | cursor | fixed | ✓ | — |

**Total collection/search endpoints:** 44

---

## Error Handling for Collection Queries

| Condition | HTTP | Error Code |
|-----------|------|------------|
| Invalid `page` or `pageSize` | 400 | `VAL_OUT_OF_RANGE` |
| Invalid `sortBy` | 400 | `VAL_INVALID_ENUM` |
| Invalid date range | 400 | `VAL_INVALID_DATE_RANGE` |
| Date range exceeds max | 400 | `VAL_OUT_OF_RANGE` |
| Missing required filter | 400 | `VAL_QUERY_FILTER_REQUIRED` |
| Unauthorized location in filter | 403 | `AUTHZ_LOCATION_SCOPE_DENIED` |

---

## Implementation Notes

1. **Link generation:** Preserve all query parameters except `page`/`cursor` when building `links.next` / `links.prev`.
2. **Count query:** Execute `COUNT(*)` with same WHERE clause; cache counts ≤ 30s for intelligence endpoints.
3. **Index alignment:** Every `sortBy` whitelist field must have a supporting database index or composite index leading column.
4. **OpenAPI:** Document per-endpoint `sortBy` enum and filter match types in parameter descriptions.
5. **Versioning:** New sort/filter fields are additive; removing fields requires API version bump.

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Backend Architect | | | |
| Solution Architect | | | |
| Tech Lead | | | |

---

*End of Collection API Strategy*

*Document ID: SRS-API-006 | Version 1.0 | July 6, 2026*
