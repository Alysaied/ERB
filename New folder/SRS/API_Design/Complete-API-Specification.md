# Complete API Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-009 |
| **Document Title** | Complete REST API Specification |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Backend Architect |
| **Source Documents** | SRS-API-001 through SRS-API-008 |
| **Date** | July 6, 2026 |
| **Base URL** | `https://{host}/api/v1` |
| **Scope** | All 178 REST endpoints — full contract per endpoint |

### Purpose

Single authoritative specification combining HTTP contract, validation, authorization, business rules, and examples for every IMS REST API.

### Specification Template (18 Fields)

Every endpoint section uses fields **1–18** in identical order. Cross-references: Request detail → SRS-API-002/004; Response shapes → SRS-API-003; Errors → SRS-API-005; Auth → SRS-API-007; Collection queries → SRS-API-006.

---

## Global Conventions

### Standard Request Headers

| Header | Required | Applies To | Description |
|--------|----------|------------|-------------|
| `Authorization` | Yes* | All except API-175 | `Bearer {access_token}` from IdP (SVC-01) |
| `Content-Type` | Yes | POST/PATCH/PUT with body | `application/json` |
| `Accept` | Recommended | All | `application/json` |
| `X-Trace-Id` | Optional | All | Client correlation UUID; echoed in errors |
| `Idempotency-Key` | Recommended | Stock mutation, reservation, payment commands | UUID; 24h deduplication window |
| `X-API-Major-Version` | Optional | All | Client-declared major version (default `1`) |

\* API-176–178 use OAuth2 **Client Credentials** (`Authorization: Bearer {client_token}`).

### Standard Success Headers

| Header | Description |
|--------|-------------|
| `X-API-Version` | Contract release e.g. `1.0.0` |
| `X-Trace-Id` | Server trace ID |
| `Location` | On `201 Created` — URI of created resource |
| `ETag` | On mutable resources — optimistic lock version |

### Standard Error Responses (All Endpoints)

`Content-Type: application/problem+json`

| HTTP | When | Typical `errorCode` |
|------|------|---------------------|
| 400 | Validation failure | `VAL_REQUEST_INVALID`, `VAL_REQUIRED_FIELD` |
| 401 | Missing/invalid auth | `AUTH_MISSING_CREDENTIALS`, `AUTH_TOKEN_EXPIRED` |
| 403 | Permission or location scope denied | `AUTHZ_INSUFFICIENT_PERMISSION`, `AUTHZ_LOCATION_SCOPE_DENIED` |
| 404 | Resource not found | `NF_*` per resource type |
| 409 | Duplicate, state conflict, optimistic lock | `CONF_*` |
| 422 | Business rule violation | `BIZ_*` |
| 500 | Unhandled error | `SYS_INTERNAL_ERROR` |
| 503 | Dependency unavailable | `SYS_DATABASE_UNAVAILABLE` |

**Standard error body (reference for all APIs):**

```json
{
  "type": "https://api.ims.example/problems/validation-error",
  "title": "Validation Failed",
  "status": 400,
  "detail": "The request contains validation errors.",
  "instance": "/api/v1/{path}",
  "errorCode": "VAL_REQUEST_INVALID",
  "traceId": "7f3c9a2e-4b1d-4e8a-9c0f-2a8b6d4e1f30",
  "timestamp": "2026-07-06T14:30:00.000Z",
  "errors": [{ "field": "fieldName", "code": "VAL_REQUIRED_FIELD", "message": "..." }]
}
```

### Standard Pagination Query (Collection GETs)

| Parameter | Type | Default | Max | Description |
|-----------|------|---------|-----|-------------|
| `page` | integer | 1 | — | 1-based page index |
| `pageSize` | integer | 20 | 100 | Records per page |

See SRS-API-006 for endpoint-specific filters, sort, and search parameters.

---

## M-01 — Product Catalog

---

### API-001: Register Product

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/products` |
| **3** | **Purpose** | Register a new product SKU with mandatory catalog attributes |
| **4** | **Authentication** | Required — Bearer JWT |
| **5** | **Required Permission** | `PERM-001` (Create Product) — Role: `INV_CTRL` |
| **6** | **Request Headers** | `Authorization`, `Content-Type: application/json`, optional `X-Trace-Id` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `CreateProductRequest` — `sku`, `name`, `unitOfMeasure` (required); `description`, `categoryCode`, `barcode`, `isTraceable`, `rotationPolicy`, `shelfLifeManaged`, `mrslThresholdDays` (optional/conditional) |
| **10** | **Validation Rules** | `sku` 1–50, pattern `^[A-Z0-9][A-Z0-9_-]*$`, unique (VR-001, VR-002); `name` 1–200 non-blank; `unitOfMeasure` 1–10; if `isTraceable=true` → `rotationPolicy` required; if `shelfLifeManaged=true` → `mrslThresholdDays` ≥1 (VR-035) |
| **11** | **Success Response** | `ProductDetailResponse` — full product with `audit` |
| **12** | **Error Responses** | 400 validation; 401 auth; 403 `INV_CTRL` only; 409 `CONF_DUPLICATE_SKU`; 422 discontinued rules N/A on create |
| **13** | **HTTP Status Codes** | Success: **201 Created**; Errors: 400, 401, 403, 409, 500 |
| **14** | **Business Rules Applied** | BR-014, BR-015, BR-016, BR-017 (traceability attributes at definition) |
| **15** | **Related Use Case** | UC-001, UC-046 |

**16. Example Request**

```http
POST /api/v1/products HTTP/1.1
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
Content-Type: application/json

{
  "sku": "BOLT-M10",
  "name": "M10 Hex Bolt",
  "unitOfMeasure": "EA",
  "categoryCode": "FAST",
  "isTraceable": false
}
```

**17. Example Success Response** — `201 Created`

```json
{
  "sku": "BOLT-M10",
  "name": "M10 Hex Bolt",
  "lifecycleStatus": "ACTIVE",
  "abcClass": null,
  "unitOfMeasure": "EA",
  "description": null,
  "categoryCode": "FAST",
  "barcode": null,
  "isTraceable": false,
  "rotationPolicy": "FIFO",
  "shelfLifeManaged": false,
  "mrslThresholdDays": null,
  "audit": {
    "createdAt": "2026-07-06T14:00:00.000Z",
    "createdBy": "inv.controller",
    "updatedAt": "2026-07-06T14:00:00.000Z",
    "updatedBy": "inv.controller"
  }
}
```

**18. Example Error Response** — `409 Conflict`

```json
{
  "type": "https://api.ims.example/problems/conflict",
  "title": "Resource Conflict",
  "status": 409,
  "detail": "A product with SKU 'BOLT-M10' already exists in the catalog.",
  "instance": "/api/v1/products",
  "errorCode": "CONF_DUPLICATE_SKU",
  "traceId": "f7a8b9c0-1234-5678-9012-def012345678",
  "timestamp": "2026-07-06T14:01:00.000Z",
  "validationRuleId": "VR-002"
}
```

---

### API-002: Search Products

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/products` |
| **3** | **Purpose** | Search and filter products by name, category, status, ABC class |
| **4** | **Authentication** | Required — Bearer JWT |
| **5** | **Required Permission** | `PERM-004` (Lookup Product) |
| **6** | **Request Headers** | `Authorization`, optional `Accept` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | `name` (partial), `sku` (prefix), `categoryCode`, `lifecycleStatus`, `abcClass`, `barcode`, `q` (search name/sku/barcode), `page`, `pageSize`, `sortBy` (`sku`,`name`,`categoryCode`,`lifecycleStatus`), `sortDirection` (`ASC`,`DESC`) |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | `page`≥1; `pageSize` 1–100; valid enums for status/ABC; `sortBy` whitelist (VR-054) |
| **11** | **Success Response** | `PagedResponse<ProductSummaryResponse>` |
| **12** | **Error Responses** | 400 invalid query; 401; 403 |
| **13** | **HTTP Status Codes** | Success: **200 OK** |
| **14** | **Business Rules Applied** | BR-027 (filter by discontinued via `lifecycleStatus`) |
| **15** | **Related Use Case** | UC-001, UC-013 |

**16. Example Request**

```http
GET /api/v1/products?lifecycleStatus=ACTIVE&page=1&pageSize=20&sortBy=sku HTTP/1.1
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
```

**17. Example Success Response** — `200 OK`

```json
{
  "data": [
    { "sku": "BOLT-M10", "name": "M10 Hex Bolt", "lifecycleStatus": "ACTIVE", "abcClass": "B", "unitOfMeasure": "EA" }
  ],
  "page": 1,
  "pageSize": 20,
  "totalElements": 1,
  "totalPages": 1
}
```

**18. Example Error Response** — `400 Bad Request`

```json
{
  "type": "https://api.ims.example/problems/validation-error",
  "title": "Validation Failed",
  "status": 400,
  "detail": "Invalid sortBy value.",
  "instance": "/api/v1/products",
  "errorCode": "VAL_INVALID_ENUM",
  "traceId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "timestamp": "2026-07-06T14:05:00.000Z",
  "errors": [{ "field": "sortBy", "code": "VAL_INVALID_ENUM", "message": "sortBy must be one of: sku, name, categoryCode, lifecycleStatus" }]
}
```

---

### API-003: Get Product by SKU

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/products/{sku}` |
| **3** | **Purpose** | Retrieve product master record by SKU |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-004` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | `sku` (string, required) — ProductSku pattern |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | `sku` format VR-001; must exist VR-007 |
| **11** | **Success Response** | `ProductDetailResponse` |
| **12** | **Error Responses** | 401; 403; 404 `NF_PRODUCT_NOT_FOUND` |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-001, UC-013 |

**16. Example Request:** `GET /api/v1/products/BOLT-M10`  
**17. Example Success Response:** Same structure as API-001 success body.  
**18. Example Error Response:** `404` with `errorCode: NF_PRODUCT_NOT_FOUND`, `validationRuleId: VR-007`.

---

### API-004: Update Product Attributes

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `PATCH` |
| **2** | **URL** | `/api/v1/products/{sku}` |
| **3** | **Purpose** | Update mutable product attributes |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-002` — `INV_CTRL` |
| **6** | **Request Headers** | `Authorization`, `Content-Type`, optional `If-Match` (ETag) |
| **7** | **Path Parameters** | `sku` (required) |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `UpdateProductAttributesRequest` — at least one of: `name`, `description`, `unitOfMeasure`, `categoryCode`, `barcode`, `isTraceable`, `rotationPolicy`, `shelfLifeManaged`, `mrslThresholdDays` |
| **10** | **Validation Rules** | Same field rules as API-001; at least one field required; traceability cross-rules (VR-003) |
| **11** | **Success Response** | `ProductDetailResponse` |
| **12** | **Error Responses** | 400; 401; 403; 404; 409 `CONF_OPTIMISTIC_LOCK` |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | BR-014–BR-017 |
| **15** | **Related Use Case** | UC-001 |

**16–18:** PATCH body with `name` update; 200 returns updated `ProductDetailResponse`; 400 if empty body (`VAL_PATCH_NO_FIELDS`).

---

### API-005: Change Product Lifecycle Status

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/products/{sku}/lifecycle-status` |
| **3** | **Purpose** | Change lifecycle status (ACTIVE, INACTIVE, DISCONTINUED) |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-003` — `INV_CTRL` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | `sku` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `newStatus` (required), `reason` (optional), `effectiveDate` (optional) |
| **10** | **Validation Rules** | Valid status transition VR-004, VR-005; `reason` max 500 |
| **11** | **Success Response** | `CommandResultResponse` + embedded `ProductDetailResponse` |
| **12** | **Error Responses** | 400; 403; 404; 422 invalid transition |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | **BR-027** (DISCONTINUED blocks replenishment) |
| **15** | **Related Use Case** | UC-001 |

**16. Example Request**

```json
{ "newStatus": "DISCONTINUED", "reason": "Supplier end-of-life", "effectiveDate": "2026-07-15" }
```

**17. Example Success:** `{ "id": "BOLT-M10", "status": "DISCONTINUED", "processedAt": "2026-07-06T14:10:00.000Z", "message": "Lifecycle status updated." }`  
**18. Example Error:** `422` `BIZ_PRODUCT_DISCONTINUED` / invalid transition per VR-005.

---

### API-006: Assign ABC Classification

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `PUT` |
| **2** | **URL** | `/api/v1/products/{sku}/abc-classification` |
| **3** | **Purpose** | Assign or update ABC priority classification |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-012` — `INV_CTRL` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | `sku` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `abcClass` (required: A/B/C), `classificationBasis` (optional), `effectiveDate` (optional) |
| **10** | **Validation Rules** | VR-021, VR-022; product exists |
| **11** | **Success Response** | `ProductDetailResponse` |
| **12** | **Error Responses** | 400; 403; 404 |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | **BR-032** (Class A priority monitoring) |
| **15** | **Related Use Case** | UC-004 |

**16–18:** PUT `{ "abcClass": "A", "classificationBasis": "REVENUE" }` → 200 product with `abcClass: "A"`.

---

### API-007: Validate Product Eligibility

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/products/{sku}/eligibility` |
| **3** | **Purpose** | Evaluate product eligibility for procurement, reservation, fulfillment, transfer |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-004` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | `sku` |
| **8** | **Query Parameters** | `transactionType` (required enum), `locationCode` (conditional for location-scoped types) |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | VR-004, VR-006, VR-008; location scope |
| **11** | **Success Response** | `EligibilityResponse` |
| **12** | **Error Responses** | 400; 403 location scope |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | **BR-027** |
| **15** | **Related Use Case** | UC-006, UC-021, UC-022 |

**17. Example Success:** `{ "eligible": true, "transactionType": "RESERVATION", "reason": null, "lifecycleStatus": "ACTIVE" }`  
**18. Example Error:** `{ "eligible": false, "reason": "Product is discontinued" }` returned in **200** body (not error HTTP) when ineligible; HTTP 422 only on invalid query.

---

### API-008: List Products by Category

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/products/categories/{categoryCode}/products` |
| **3** | **Purpose** | List products in a category |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-004` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | `categoryCode` (required) |
| **8** | **Query Parameters** | `lifecycleStatus`, `page`, `pageSize`, `sortBy`, `sortDirection` |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | Category exists; pagination per SRS-API-006 |
| **11** | **Success Response** | `PagedResponse<ProductSummaryResponse>` |
| **12** | **Error Responses** | 400; 404 category |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-001 |

**16–18:** `GET .../categories/FAST/products?page=1` → paginated product list; 404 if category unknown.

---

### API-009: Resolve Duplicate Product Conflict

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/products/duplicate-resolutions` |
| **3** | **Purpose** | Merge, reject, or keep both duplicate SKUs |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-005` — `INV_CTRL` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `resolutionAction`, `sourceSku`, `targetSku` (if MERGE), `mergeAuthorizationReference` (conditional), `notes` |
| **10** | **Validation Rules** | VR-009, VR-010; merge auth when both have on-hand |
| **11** | **Success Response** | `CommandResultResponse` |
| **12** | **Error Responses** | 400; 403; 422 merge constraints |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | Catalog identity integrity |
| **15** | **Related Use Case** | UC-001 |

**16–18:** POST merge action with `mergeAuthorizationReference` when required; 200 command result.

---

### API-010: Bulk Product Import

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/products/import` |
| **3** | **Purpose** | Bulk import/validate product master at go-live |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-015` — `OPS_DIR`, `INV_CTRL` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `importMode` (`VALIDATE_ONLY`,`UPSERT`,`CREATE_ONLY`), `sourceReference`, `products[]` (1–5000 lines) |
| **10** | **Validation Rules** | Each line per API-001; unique SKU in batch VR-001, VR-002 |
| **11** | **Success Response** | `BulkImportResultResponse` — `importedCount`, `errorCount`, `errors[]` |
| **12** | **Error Responses** | 400 batch invalid; 403; 422 blocking errors on UPSERT |
| **13** | **HTTP Status Codes** | **200 OK** (validate/partial) or **201 Created** (pure create success) |
| **14** | **Business Rules Applied** | BR-014–BR-017; PERM-016 approval for activation |
| **15** | **Related Use Case** | UC-046 |

**17. Example Success:** `{ "importedCount": 498, "errorCount": 2, "errors": [{ "rowIndex": 15, "sku": "BAD SKU", "errorCode": "VAL_INVALID_FORMAT", "message": "..." }] }`  
**18. Example Error:** `400` when `products` empty or >5000 items.

---

## M-02 — Warehouse Network

---

### API-011: Register Location

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/locations` |
| **3** | **Purpose** | Register new inventory location (warehouse, store, DC) |
| **4** | **Authentication** | Required — Bearer JWT |
| **5** | **Required Permission** | `PERM-006` — `COO`, `OPS_DIR` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `locationCode`, `name`, `locationType`, `operationalStatus`; optional address fields, `parentLocationCode`, `plannedGoLiveDate` |
| **10** | **Validation Rules** | VR-011; unique `locationCode`; no circular hierarchy VR-014 |
| **11** | **Success Response** | `LocationDetailResponse` |
| **12** | **Error Responses** | 400; 401; 403; 409 `CONF_DUPLICATE_LOCATION` |
| **13** | **HTTP Status Codes** | **201 Created** |
| **14** | **Business Rules Applied** | Network structure governance |
| **15** | **Related Use Case** | UC-002 |

**16.** `POST /api/v1/locations` with `{ "locationCode": "WH-EAST", "name": "East Warehouse", "locationType": "WAREHOUSE", "operationalStatus": "PLANNED" }`  
**17.** `201` — `LocationDetailResponse` with `locationCode: WH-EAST`  
**18.** `409 CONF_DUPLICATE_LOCATION` — standard ProblemDetail envelope

---

### API-012: List Locations

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/locations` |
| **3** | **Purpose** | List locations with filters |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-004` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | `operationalStatus` (default ACTIVE), `locationType`, `parentLocationCode`, `name`, `q`, `page`, `pageSize`, `sortBy`, `sortDirection` |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | Pagination SRS-API-006; user location scope VR-053 |
| **11** | **Success Response** | `PagedResponse<LocationSummaryResponse>` |
| **12** | **Error Responses** | 400; 401; 403 |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-002, UC-012, UC-013 |

**16.** `GET /api/v1/locations?operationalStatus=ACTIVE&page=1`  
**17.** `200` paginated `LocationSummaryResponse[]`  
**18.** `400 VAL_INVALID_ENUM` for invalid `sortBy`

---

### API-013: Get Location

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/locations/{locationCode}` |
| **3** | **Purpose** | Retrieve location master and hierarchy |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-004` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | Exists; user scope VR-053 |
| **11** | **Success Response** | `LocationDetailResponse` |
| **12** | **Error Responses** | 401; 403; 404 `NF_LOCATION_NOT_FOUND` |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-002 |

**16–18:** `GET /api/v1/locations/WH-EAST` → 200 detail; 404 if not found or out of scope.

---

### API-014: Update Location Hierarchy

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `PATCH` |
| **2** | **URL** | `/api/v1/locations/{locationCode}/hierarchy` |
| **3** | **Purpose** | Update parent, zone, layout |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-008` — `COO`, `OPS_DIR` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | ≥1 of: `parentLocationCode`, `zoneCode`, `layoutNotes` |
| **10** | **Validation Rules** | VR-014, VR-015; no self/ancestor parent |
| **11** | **Success Response** | `LocationDetailResponse` |
| **12** | **Error Responses** | 400; 403; 404; 422 hierarchy violation |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-002 |

**16–18:** PATCH parent assignment → 200; 422 if circular hierarchy.

---

### API-015: Configure Storage Position

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/locations/{locationCode}/storage-positions` |
| **3** | **Purpose** | Create/configure storage position |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-007` — `COO`, `OPS_DIR` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `positionCode` (required); `zone`, `aisle`, `bin`, `positionType`, `isActive` |
| **10** | **Validation Rules** | Location active VR-012; unique position per location |
| **11** | **Success Response** | `StoragePositionResponse` |
| **12** | **Error Responses** | 400; 403; 404; 409 duplicate position |
| **13** | **HTTP Status Codes** | **201 Created** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-002, UC-010 |

**16–18:** POST position `RCV-STAGE-01` → 201; 404 inactive location.

---

### API-016: List Storage Positions

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/locations/{locationCode}/storage-positions` |
| **3** | **Purpose** | List storage positions for put-away/pick |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-004` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | `positionType`, `zone`, `isActive`, `page`, `pageSize`, `sortBy` |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | SRS-API-006 pagination |
| **11** | **Success Response** | `PagedResponse<StoragePositionResponse>` |
| **12** | **Error Responses** | 401; 403; 404 |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-010 |

**16–18:** GET with `zone=RCV` → 200 paged positions.

---

### API-017: Activate Location

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/locations/{locationCode}/activate` |
| **3** | **Purpose** | Activate location for inventory operations |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-007` — `COO`, `OPS_DIR` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `openingBalanceApprovalReference` (conditional), `activationDate`, `notes` |
| **10** | **Validation Rules** | VR-013, VR-025 opening balance policy |
| **11** | **Success Response** | `CommandResultResponse` |
| **12** | **Error Responses** | 400; 403; 422 missing approval |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | Go-live integrity (BA-16) |
| **15** | **Related Use Case** | UC-002, UC-046 |

**16–18:** POST activate → 200 `{ "status": "ACTIVE" }`; 422 without approved opening balance.

---

### API-018: Deactivate Location

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/locations/{locationCode}/deactivate` |
| **3** | **Purpose** | Deactivate location; block new transactions |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-007` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `reason` (required), `effectiveDate` |
| **10** | **Validation Rules** | VR-012, VR-017 |
| **11** | **Success Response** | `CommandResultResponse` |
| **12** | **Error Responses** | 400; 403; 409 active transactions |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-002 |

**16–18:** POST with reason → 200 deactivated status.

---

### API-019: Close Location

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/locations/{locationCode}/close` |
| **3** | **Purpose** | Finalize location closure after disposition |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-009` — `CEO`, `COO`, `OPS_DIR` |
| **6** | **Request Headers** | `Authorization`, `Content-Type` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `dispositionPlanReference` or `closureWaiverReference` (conditional), `closureDate`, `notes` |
| **10** | **Validation Rules** | VR-016; required when on-hand > 0 |
| **11** | **Success Response** | `CommandResultResponse` |
| **12** | **Error Responses** | 400; 403; 422 remaining stock |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | Strategic closure governance |
| **15** | **Related Use Case** | UC-002 |

**16–18:** POST close with disposition plan → 200; 422 if stock remains without plan.

---

### API-020: Get Freeze Status

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/locations/{locationCode}/freeze-status` |
| **3** | **Purpose** | Check physical inventory freeze state |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-040` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | Location scope VR-053 |
| **11** | **Success Response** | `LocationFreezeStatusResponse` — `frozen`, `freezeReason`, `freezeUntil` |
| **12** | **Error Responses** | 401; 403; 404 |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | **BR-024** |
| **15** | **Related Use Case** | UC-015 |

**16–18:** GET → `{ "frozen": true, "freezeReason": "PHYSICAL_COUNT", "freezeUntil": "2026-07-10" }`

---

### API-021: Get Operational Status

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/locations/{locationCode}/operational-status` |
| **3** | **Purpose** | Check if location accepts transactions |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-004` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | `locationCode` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | — |
| **11** | **Success Response** | `LocationOperationalStatusResponse` |
| **12** | **Error Responses** | 401; 403; 404 |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-002 |

**16–18:** GET → `{ "operationalStatus": "ACTIVE", "acceptsTransactions": true }`

---

*Continued — M-03 through M-07 in `Complete-API-Specification-Part2.md`; M-08 through Platform in `Complete-API-Specification-Part3.md`*
