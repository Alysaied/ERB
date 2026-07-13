# Error Response Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-005 |
| **Document Title** | Standard Error Response Model — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Backend Architect |
| **Source Documents** | SRS-API-001, SRS-API-004, SRS-BR-001, SRS-VR-001, Cross-Cutting Concerns (Exception Handling) |
| **Date** | July 6, 2026 |
| **Scope** | All REST APIs under `/api/v1` |

### Purpose

Defines the **standard error response contract** for every REST API. All error responses conform to [RFC 7807 Problem Details for HTTP APIs](https://datatracker.ietf.org/doc/html/rfc7807) with IMS extensions for machine-readable error codes, field-level validation, business rule traceability, and operational correlation.

### Design Principles

| Principle | Detail |
|-----------|--------|
| **RFC 7807 baseline** | `type`, `title`, `status`, `detail`, `instance` on every response |
| **Machine + human** | `errorCode` for clients/automation; `detail` / `message` for operators |
| **No leakage** | `500` responses never expose stack traces, SQL, or internal paths |
| **Traceability** | `traceId` on every error; `businessRuleId` / `validationRuleId` when applicable |
| **Layer mapping** | Presentation maps domain/application exceptions — domain never emits HTTP codes |

---

## Standard Envelope

### `ProblemDetailResponse` (base)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | String (URI) | Yes | Problem type URI — stable identifier for error category |
| `title` | String | Yes | Short, human-readable summary of the problem type |
| `status` | Integer | Yes | HTTP status code (duplicate of response status for convenience) |
| `detail` | String | Yes | Human-readable explanation specific to this occurrence |
| `instance` | String (URI) | Yes | Request path that triggered the error (e.g. `/api/v1/products`) |
| `errorCode` | String | Yes | IMS machine-readable error code (see naming convention) |
| `traceId` | String (UUID) | Yes | Distributed trace / correlation ID for support and logs |
| `timestamp` | String (Instant) | Yes | ISO-8601 UTC time the error was generated |
| `details` | Object | No | Structured context — shape varies by error category |
| `errors` | Array\<FieldError\> | No | Field-level validation errors (400 only) |

### `FieldError` (validation extension)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `field` | String | Yes | JSON path to the invalid field (e.g. `lines[2].quantity.amount`) |
| `code` | String | Yes | Field-level validation error code |
| `message` | String | Yes | Human-readable field error |
| `rejectedValue` | Any | No | Submitted value when safe to return (omit secrets) |

### Problem Type URI Convention

```
https://api.{environment}.ims.example/problems/{category}
```

| Category slug | HTTP Status | Used for |
|---------------|-------------|----------|
| `validation-error` | 400 | Request syntactic / structural validation |
| `authentication-error` | 401 | Missing or invalid credentials |
| `authorization-error` | 403 | Authenticated but not permitted |
| `not-found` | 404 | Resource does not exist or not visible |
| `conflict` | 409 | State conflict, duplicate, concurrency |
| `business-rule-violation` | 422 | Domain business rule or invariant failure |
| `internal-server-error` | 500 | Unexpected unhandled failure |
| `service-unavailable` | 503 | Infrastructure / dependency unavailable |

### Error Code Naming Convention

```
{CATEGORY}_{DOMAIN}_{REASON}
```

| Prefix | Category |
|--------|----------|
| `VAL_` | Validation (400) |
| `AUTH_` | Authentication (401) |
| `AUTHZ_` | Authorization (403) |
| `NF_` | Not Found (404) |
| `CONF_` | Conflict (409) |
| `BIZ_` | Business rule (422) |
| `SYS_` | System / internal (500, 503) |

---

## Error Category Catalog

---

## 1. Validation Errors — `400 Bad Request`

**When:** Request fails syntactic validation (L1–L2) before or during command dispatch. Bean Validation, FluentValidation, or request binder failures.

| Attribute | Value |
|-----------|-------|
| **HTTP Status Code** | `400` |
| **Problem Type** | `https://api.ims.example/problems/validation-error` |
| **Exception Source** | `ValidationException` (Presentation / Application) |

### Standard Error Codes

| Error Code | Error Message (title/detail pattern) | Trigger |
|------------|--------------------------------------|---------|
| `VAL_REQUEST_INVALID` | The request contains one or more validation errors. | Generic wrapper when multiple field errors |
| `VAL_REQUIRED_FIELD` | Required field is missing or blank. | `@NotNull`, `@NotBlank` |
| `VAL_INVALID_FORMAT` | Field value does not match the required format. | Pattern, type coercion failure |
| `VAL_OUT_OF_RANGE` | Value is outside the allowed range. | Min/max, scale violations |
| `VAL_INVALID_ENUM` | Value is not a permitted enumeration member. | Unknown enum value |
| `VAL_INVALID_DATE_RANGE` | Start date must be on or before end date. | Cross-field date (VR-062, VR-153) |
| `VAL_PATCH_NO_FIELDS` | At least one field must be provided for update. | Empty PATCH body |
| `VAL_QUERY_FILTER_REQUIRED` | At least one filter parameter is required. | e.g. `sku` OR `locationCode` (VR-054) |

### Details Object Shape

```json
{
  "details": {
    "requestId": "optional-client-correlation"
  }
}
```

### Example JSON Response

```json
{
  "type": "https://api.ims.example/problems/validation-error",
  "title": "Validation Failed",
  "status": 400,
  "detail": "The request contains 2 validation errors. Correct the highlighted fields and resubmit.",
  "instance": "/api/v1/products",
  "errorCode": "VAL_REQUEST_INVALID",
  "traceId": "7f3c9a2e-4b1d-4e8a-9c0f-2a8b6d4e1f30",
  "timestamp": "2026-07-06T14:30:00.000Z",
  "errors": [
    {
      "field": "sku",
      "code": "VAL_INVALID_FORMAT",
      "message": "SKU must match pattern ^[A-Z0-9][A-Z0-9_-]*$ and be 1–50 characters.",
      "rejectedValue": "widget-01"
    },
    {
      "field": "mrslThresholdDays",
      "code": "VAL_REQUIRED_FIELD",
      "message": "Minimum remaining shelf life days is required when shelfLifeManaged is true.",
      "rejectedValue": null
    }
  ]
}
```

**Business rule link:** Validation enforces VR-xxx constraints defined in SRS-API-004; field `code` may mirror VR ID (e.g. `VR-001`).

---

## 2. Business Errors — `422 Unprocessable Entity`

**When:** Request is well-formed but violates a domain invariant or business rule (L3–L4). Aggregate refuses the command.

| Attribute | Value |
|-----------|-------|
| **HTTP Status Code** | `422` |
| **Problem Type** | `https://api.ims.example/problems/business-rule-violation` |
| **Exception Source** | `BusinessRuleViolationException` (Domain) |

### Standard Error Codes

| Error Code | Error Message | BR | VR |
|------------|---------------|----|----|
| `BIZ_INSUFFICIENT_ATP` | Cannot commit quantity exceeding available-to-promise. | BR-001 | VR-092 |
| `BIZ_RESERVATION_EXCEEDS_ATP` | Reservation quantity exceeds available stock at this location. | BR-001, BR-002 | VR-092 |
| `BIZ_SAFETY_STOCK_BREACH` | Operation would breach safety stock. Provide an authorized exception reference. | BR-010 | VR-124, VR-125 |
| `BIZ_LOCATION_FROZEN` | Location is frozen for inventory transactions. | BR-024 | VR-053 |
| `BIZ_PRODUCT_DISCONTINUED` | Product is discontinued and cannot be ordered or replenished. | BR-027 | VR-004, VR-120 |
| `BIZ_PO_REQUIRED_FOR_RECEIPT` | A valid purchase order is required before receiving supplier goods. | BR-007 | VR-040 |
| `BIZ_VERIFY_BEFORE_ACCEPTANCE` | Goods must be verified before acceptance into inventory. | BR-004 | VR-035 |
| `BIZ_PUT_AWAY_REQUIRED` | Stock is not available until put-away is complete. | BR-005 | VR-043 |
| `BIZ_MRSL_NON_COMPLIANT` | Remaining shelf life does not meet minimum receiving threshold. | BR-016 | VR-035 |
| `BIZ_LOT_REQUIRED` | Lot or batch capture is required for this traceable product. | BR-017 | — |
| `BIZ_SEGREGATION_OF_DUTIES` | Proposed approver cannot approve this transaction due to segregation of duties. | BR-019, BR-021 | VR-075, VR-083 |
| `BIZ_INVESTIGATION_REQUIRED` | Variance must be investigated before adjustment submission. | BR-022 | VR-076 |
| `BIZ_BACKORDER_ACK_REQUIRED` | Customer acknowledgment is required before recording a backorder. | BR-028 | VR-101 |
| `BIZ_SOURCE_MINIMUM_PROTECTED` | Transfer would breach minimum stock at the source location. | BR-012 | VR-140 |
| `BIZ_NETWORK_TRANSFER_DECLINED` | Network transfer evaluation must be documented before purchase approval. | BR-011 | VR-118 |
| `BIZ_THREE_WAY_MATCH_INCOMPLETE` | Payment cannot be authorized until three-way match is complete. | BR-008 | — |
| `BIZ_RETURN_AUTH_REQUIRED` | Return authorization is required before receiving customer returns. | BR-025 | VR-045 |
| `BIZ_PROMOTIONAL_RING_FENCE` | Quantity exceeds promotional ring-fenced allocation. | BR-029 | VR-127 |

### Details Object Extensions

| Field | Type | Description |
|-------|------|-------------|
| `businessRuleId` | String | BR-xxx identifier when applicable |
| `validationRuleId` | String | VR-xxx identifier when applicable |
| `details` | Object | Domain-specific context (SKU, quantities, statuses) |

### Example JSON Response

```json
{
  "type": "https://api.ims.example/problems/business-rule-violation",
  "title": "Business Rule Violation",
  "status": 422,
  "detail": "Cannot reserve 100 units. Only 45 units are available to promise at this location.",
  "instance": "/api/v1/inventory/stock-positions/WH-EAST/WIDGET-01/reservations",
  "errorCode": "BIZ_INSUFFICIENT_ATP",
  "traceId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "timestamp": "2026-07-06T14:35:12.456Z",
  "businessRuleId": "BR-001",
  "validationRuleId": "VR-092",
  "details": {
    "sku": "WIDGET-01",
    "locationCode": "WH-EAST",
    "orderId": "ORD-2026-004521",
    "orderLineId": "LINE-003",
    "requestedQuantity": {
      "amount": 100.0000,
      "unitOfMeasure": "EA"
    },
    "availableToPromise": {
      "amount": 45.0000,
      "unitOfMeasure": "EA"
    },
    "onHand": {
      "amount": 120.0000,
      "unitOfMeasure": "EA"
    },
    "reserved": {
      "amount": 60.0000,
      "unitOfMeasure": "EA"
    },
    "quarantined": {
      "amount": 15.0000,
      "unitOfMeasure": "EA"
    }
  }
}
```

---

## 3. Authentication Errors — `401 Unauthorized`

**When:** Request lacks valid credentials, token is expired, or authentication fails. **No resource existence is implied.**

| Attribute | Value |
|-----------|-------|
| **HTTP Status Code** | `401` |
| **Problem Type** | `https://api.ims.example/problems/authentication-error` |
| **Exception Source** | `UnauthorizedException` (Application) |
| **Response Header** | `WWW-Authenticate: Bearer realm="ims-api"` when applicable |

### Standard Error Codes

| Error Code | Error Message | Details |
|------------|---------------|---------|
| `AUTH_MISSING_CREDENTIALS` | Authentication credentials were not provided. | No `Authorization` header |
| `AUTH_INVALID_TOKEN` | The access token is invalid or malformed. | JWT parse/signature failure |
| `AUTH_TOKEN_EXPIRED` | The access token has expired. | `exp` claim in the past |
| `AUTH_SESSION_TERMINATED` | The session has been terminated. | Logout or admin revocation |
| `AUTH_ACCOUNT_SUSPENDED` | The user account is suspended. | Account status check |
| `AUTH_ACCOUNT_DEACTIVATED` | The user account is deactivated. | Account status check |
| `AUTH_INTEGRATION_CREDENTIAL_INVALID` | Integration client credentials are invalid. | API-176 ACL inbound |

### Example JSON Response

```json
{
  "type": "https://api.ims.example/problems/authentication-error",
  "title": "Authentication Required",
  "status": 401,
  "detail": "The access token has expired. Obtain a new token and retry the request.",
  "instance": "/api/v1/fulfillment/orders/3fa85f64-5717-4562-b3fc-2c963f66afa6/confirm",
  "errorCode": "AUTH_TOKEN_EXPIRED",
  "traceId": "c4d5e6f7-8901-2345-6789-abcdef012345",
  "timestamp": "2026-07-06T14:40:00.000Z",
  "details": {
    "tokenExpiredAt": "2026-07-06T14:38:22.000Z"
  }
}
```

**Security note:** Do not reveal whether a user ID exists. Use generic messages for credential failures.

---

## 4. Authorization Errors — `403 Forbidden`

**When:** Caller is authenticated but lacks permission, location scope, or role for the action.

| Attribute | Value |
|-----------|-------|
| **HTTP Status Code** | `403` |
| **Problem Type** | `https://api.ims.example/problems/authorization-error` |
| **Exception Source** | `ForbiddenException` (Application) |

### Standard Error Codes

| Error Code | Error Message | Details |
|------------|---------------|---------|
| `AUTHZ_INSUFFICIENT_PERMISSION` | You do not have permission to perform this action. | Missing role/permission |
| `AUTHZ_LOCATION_SCOPE_DENIED` | You are not authorized to access this location. | VR-008, VR-053 |
| `AUTHZ_RESOURCE_SCOPE_DENIED` | You are not authorized to access this resource. | Row-level / ownership |
| `AUTHZ_APPROVAL_THRESHOLD` | This transaction requires independent approval above your authority. | BR-021, VR-082 |
| `AUTHZ_PO_AMENDMENT_DENIED` | You are not authorized to amend or cancel this purchase order. | VR-051 |
| `AUTHZ_ROLE_ASSIGNMENT_DENIED` | You are not authorized to assign or revoke this role. | VR-083 |
| `AUTHZ_INTEGRATION_NOT_REGISTERED` | The integration source system is not registered or enabled. | API-176, API-177 |

### Example JSON Response

```json
{
  "type": "https://api.ims.example/problems/authorization-error",
  "title": "Access Denied",
  "status": 403,
  "detail": "You are not authorized to perform inventory transactions at location WH-WEST.",
  "instance": "/api/v1/inventory/stock-positions/WH-WEST/BOLT-M10/reservations",
  "errorCode": "AUTHZ_LOCATION_SCOPE_DENIED",
  "traceId": "d5e6f7a8-9012-3456-7890-bcdef0123456",
  "timestamp": "2026-07-06T14:42:18.789Z",
  "validationRuleId": "VR-053",
  "details": {
    "userId": "picker.jones",
    "locationCode": "WH-WEST",
    "requiredPermission": "INVENTORY_RESERVE",
    "authorizedLocations": ["WH-EAST", "WH-CENTRAL"]
  }
}
```

---

## 5. Resource Not Found — `404 Not Found`

**When:** Requested resource does not exist, or exists but is not visible to the caller (optional policy: return 404 instead of 403 to prevent enumeration).

| Attribute | Value |
|-----------|-------|
| **HTTP Status Code** | `404` |
| **Problem Type** | `https://api.ims.example/problems/not-found` |
| **Exception Source** | `NotFoundException` (Application) |

### Standard Error Codes

| Error Code | Error Message | Resource |
|------------|---------------|----------|
| `NF_PRODUCT_NOT_FOUND` | Product not found. | SKU (VR-007) |
| `NF_LOCATION_NOT_FOUND` | Location not found. | LocationCode |
| `NF_ORDER_NOT_FOUND` | Customer order not found. | orderId (VR-108) |
| `NF_PURCHASE_ORDER_NOT_FOUND` | Purchase order not found. | purchaseOrderId |
| `NF_GOODS_RECEIPT_NOT_FOUND` | Goods receipt not found. | goodsReceiptId |
| `NF_RESERVATION_NOT_FOUND` | Reservation not found. | reservationId |
| `NF_TRANSFER_NOT_FOUND` | Stock transfer not found. | transferId |
| `NF_ADJUSTMENT_CASE_NOT_FOUND` | Adjustment case not found. | caseId |
| `NF_RETURN_AUTHORIZATION_NOT_FOUND` | Return authorization not found. | VR-149 |
| `NF_USER_NOT_FOUND` | User account not found. | userId |
| `NF_RESOURCE_NOT_FOUND` | The requested resource was not found. | Generic fallback |

### Example JSON Response

```json
{
  "type": "https://api.ims.example/problems/not-found",
  "title": "Resource Not Found",
  "status": 404,
  "detail": "No product exists with SKU 'UNKNOWN-SKU'.",
  "instance": "/api/v1/products/UNKNOWN-SKU",
  "errorCode": "NF_PRODUCT_NOT_FOUND",
  "traceId": "e6f7a8b9-0123-4567-8901-cdef01234567",
  "timestamp": "2026-07-06T14:45:00.000Z",
  "validationRuleId": "VR-007",
  "details": {
    "resourceType": "Product",
    "sku": "UNKNOWN-SKU"
  }
}
```

---

## 6. Conflict — `409 Conflict`

**When:** Request conflicts with current resource state — duplicates, optimistic locking, illegal state transition, or concurrent modification.

| Attribute | Value |
|-----------|-------|
| **HTTP Status Code** | `409` |
| **Problem Type** | `https://api.ims.example/problems/conflict` |
| **Exception Source** | `ConflictException` (Application / Domain) |

### Standard Error Codes

| Error Code | Error Message | Scenario |
|------------|---------------|----------|
| `CONF_DUPLICATE_SKU` | A product with this SKU already exists. | API-001 (VR-002) |
| `CONF_DUPLICATE_BARCODE` | A product with this barcode already exists. | VR-009 |
| `CONF_DUPLICATE_LOCATION` | A location with this code already exists. | VR-011 |
| `CONF_DUPLICATE_SUPPLIER` | A supplier with this code already exists. | VR-030 |
| `CONF_DUPLICATE_INVOICE` | An invoice with this number already exists for the supplier. | API-077 |
| `CONF_OPTIMISTIC_LOCK` | The resource was modified by another user. Refresh and retry. | ETag / version mismatch |
| `CONF_INVALID_STATE_TRANSITION` | The operation is not valid for the current resource status. | e.g. ship unconfirmed order |
| `CONF_IDEMPOTENCY_KEY_REUSED` | Idempotency key was reused with a different request payload. | Financial/reservation commands |
| `CONF_ORDER_ALREADY_CONFIRMED` | Order is already confirmed. | API-085 |
| `CONF_RECEIPT_ALREADY_VERIFIED` | Goods receipt is already verified. | API-069 |
| `CONF_TRANSFER_NOT_APPROVED` | Transfer must be approved before dispatch. | API-103 |

### Example JSON Response

```json
{
  "type": "https://api.ims.example/problems/conflict",
  "title": "Resource Conflict",
  "status": 409,
  "detail": "A product with SKU 'BOLT-M10' already exists in the catalog.",
  "instance": "/api/v1/products",
  "errorCode": "CONF_DUPLICATE_SKU",
  "traceId": "f7a8b9c0-1234-5678-9012-def012345678",
  "timestamp": "2026-07-06T14:48:33.210Z",
  "validationRuleId": "VR-002",
  "details": {
    "resourceType": "Product",
    "sku": "BOLT-M10",
    "existingResourceId": "BOLT-M10",
    "conflictType": "DUPLICATE_KEY"
  }
}
```

### Optimistic Locking Example

```json
{
  "type": "https://api.ims.example/problems/conflict",
  "title": "Resource Conflict",
  "status": 409,
  "detail": "Purchase order was updated by another user. Retrieve the latest version and retry.",
  "instance": "/api/v1/procurement/purchase-orders/8b2e4f1a-9c3d-4e5f-a6b7-c8d9e0f1a2b3",
  "errorCode": "CONF_OPTIMISTIC_LOCK",
  "traceId": "0a1b2c3d-4e5f-6789-0abc-def123456789",
  "timestamp": "2026-07-06T14:50:00.000Z",
  "details": {
    "resourceType": "PurchaseOrder",
    "resourceId": "8b2e4f1a-9c3d-4e5f-a6b7-c8d9e0f1a2b3",
    "expectedVersion": 3,
    "actualVersion": 4
  }
}
```

---

## 7. Internal Server Errors — `500 Internal Server Error`

**When:** Unexpected unhandled exception. Programming defect, unhandled edge case, or non-transient failure not classified as 503.

| Attribute | Value |
|-----------|-------|
| **HTTP Status Code** | `500` |
| **Problem Type** | `https://api.ims.example/problems/internal-server-error` |
| **Exception Source** | Unhandled `Exception` (any layer) |
| **Logging** | Full stack trace logged server-side with `traceId` (EXC-04) |

### Standard Error Codes

| Error Code | Error Message | Client exposure |
|------------|---------------|-----------------|
| `SYS_INTERNAL_ERROR` | An unexpected error occurred. Contact support with the trace ID. | Generic only |
| `SYS_DATA_INTEGRITY_ERROR` | An unexpected data integrity error occurred. | Generic only |
| `SYS_MAPPING_ERROR` | An unexpected error occurred while processing the response. | Generic only |

### Example JSON Response

```json
{
  "type": "https://api.ims.example/problems/internal-server-error",
  "title": "Internal Server Error",
  "status": 500,
  "detail": "An unexpected error occurred while processing your request. Contact support and provide the trace ID.",
  "instance": "/api/v1/inbound/goods-receipts/1a2b3c4d-5e6f-7890-abcd-ef1234567890/verify",
  "errorCode": "SYS_INTERNAL_ERROR",
  "traceId": "1a2b3c4d-5e6f-7890-abcd-ef1234567890",
  "timestamp": "2026-07-06T14:55:00.000Z",
  "details": {
    "supportReference": "1a2b3c4d-5e6f-7890-abcd-ef1234567890"
  }
}
```

**Prohibited in 500 responses:** `exception`, `stackTrace`, `sql`, `cause`, file paths, connection strings.

---

## 8. Service Unavailable — `503 Service Unavailable`

**When:** Transient infrastructure failure — database unreachable, message broker down, dependency timeout after retries exhausted.

| Attribute | Value |
|-----------|-------|
| **HTTP Status Code** | `503` |
| **Problem Type** | `https://api.ims.example/problems/service-unavailable` |
| **Exception Source** | `InfrastructureException` (Infrastructure) |
| **Response Header** | `Retry-After: <seconds>` when retry is advisable |

### Standard Error Codes

| Error Code | Error Message |
|------------|---------------|
| `SYS_DATABASE_UNAVAILABLE` | The service is temporarily unavailable. Please retry later. |
| `SYS_DEPENDENCY_TIMEOUT` | A dependent service did not respond in time. Please retry later. |
| `SYS_MAINTENANCE_MODE` | The system is under maintenance. Please retry later. |

### Example JSON Response

```json
{
  "type": "https://api.ims.example/problems/service-unavailable",
  "title": "Service Unavailable",
  "status": 503,
  "detail": "The service is temporarily unavailable due to a database connectivity issue. Please retry after 30 seconds.",
  "instance": "/api/v1/inventory/availability/WIDGET-01",
  "errorCode": "SYS_DATABASE_UNAVAILABLE",
  "traceId": "2b3c4d5e-6f70-8901-bcde-f12345678901",
  "timestamp": "2026-07-06T15:00:00.000Z",
  "details": {
    "retryAfterSeconds": 30
  }
}
```

---

## HTTP Status Code Summary

| Category | HTTP Status | Problem Type Slug | Primary `errorCode` Prefix |
|----------|-------------|-------------------|----------------------------|
| Validation | `400` | `validation-error` | `VAL_` |
| Authentication | `401` | `authentication-error` | `AUTH_` |
| Authorization | `403` | `authorization-error` | `AUTHZ_` |
| Not Found | `404` | `not-found` | `NF_` |
| Conflict | `409` | `conflict` | `CONF_` |
| Business Rule | `422` | `business-rule-violation` | `BIZ_` |
| Internal Server | `500` | `internal-server-error` | `SYS_` |
| Service Unavailable | `503` | `service-unavailable` | `SYS_` |

---

## Exception-to-HTTP Mapping (Implementation Reference)

Aligns with Cross-Cutting Concerns §5.3.

| Java Exception | HTTP | `errorCode` family |
|----------------|------|-------------------|
| `ValidationException` | 400 | `VAL_*` |
| `UnauthorizedException` | 401 | `AUTH_*` |
| `ForbiddenException` | 403 | `AUTHZ_*` |
| `NotFoundException` | 404 | `NF_*` |
| `ConflictException` | 409 | `CONF_*` |
| `BusinessRuleViolationException` | 422 | `BIZ_*` |
| `InfrastructureException` (transient) | 503 | `SYS_*` |
| `Exception` (unhandled) | 500 | `SYS_INTERNAL_ERROR` |

### Domain Exception Examples → Error Codes

| Domain Exception | Error Code | BR |
|------------------|------------|-----|
| `InsufficientAtpException` | `BIZ_INSUFFICIENT_ATP` | BR-001 |
| `LocationFrozenException` | `BIZ_LOCATION_FROZEN` | BR-024 |
| `SegregationOfDutiesViolationException` | `BIZ_SEGREGATION_OF_DUTIES` | BR-019 |
| `MrslNonComplianceException` | `BIZ_MRSL_NON_COMPLIANT` | BR-016 |
| `DiscontinuedProductException` | `BIZ_PRODUCT_DISCONTINUED` | BR-027 |

---

## Response Headers

| Header | When | Value |
|--------|------|-------|
| `Content-Type` | Always | `application/problem+json` |
| `WWW-Authenticate` | 401 | `Bearer realm="ims-api"` |
| `Retry-After` | 503 | Seconds until retry advised |
| `X-Trace-Id` | Always | Same value as `traceId` in body |
| `ETag` | 409 optimistic lock | Current resource version when available |

---

## Bulk / Partial Success Errors

Import and sync endpoints (API-010, API-147) return **200 OK** with per-row errors in the success body for non-blocking validation. **Blocking** failures use standard error envelope:

| Scenario | HTTP | Pattern |
|----------|------|---------|
| Entire request invalid (empty batch, bad mode) | 400 | Standard `ProblemDetailResponse` |
| Batch has blocking errors on activate | 422 | `BIZ_IMPORT_BLOCKED` with error count in `details` |
| Per-row errors in validate-only mode | 200 | `errors[]` in success response (SRS-API-003) |

---

## OpenAPI Schema Sketch

```yaml
ProblemDetailResponse:
  type: object
  required: [type, title, status, detail, instance, errorCode, traceId, timestamp]
  properties:
    type: { type: string, format: uri }
    title: { type: string }
    status: { type: integer }
    detail: { type: string }
    instance: { type: string }
    errorCode: { type: string }
    traceId: { type: string, format: uuid }
    timestamp: { type: string, format: date-time }
    businessRuleId: { type: string, pattern: '^BR-\\d{3}$' }
    validationRuleId: { type: string, pattern: '^VR-\\d{3}$' }
    details: { type: object, additionalProperties: true }
    errors:
      type: array
      items:
        $ref: '#/components/schemas/FieldError'

FieldError:
  type: object
  required: [field, code, message]
  properties:
    field: { type: string }
    code: { type: string }
    message: { type: string }
    rejectedValue: {}
```

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Backend Architect | | | |
| Solution Architect | | | |
| Tech Lead | | | |
| Product Owner | | | |

---

*End of Error Response Specification*

*Document ID: SRS-API-005 | Version 1.0 | July 6, 2026*
