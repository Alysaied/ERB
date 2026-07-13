# Response DTO Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-003 |
| **Document Title** | Response DTO Specification — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Backend Architect |
| **Source Documents** | SRS-API-001 (REST API Catalog), SRS-API-002 (Request DTOs), SRS-VR-001, SRS-DM-002 |
| **Date** | July 6, 2026 |
| **Scope** | Success response DTOs only — error responses follow RFC 7807 Problem Details (separate contract) |

### Purpose

Defines the **success response structure** for every REST API in SRS-API-001: HTTP status code, response fields, nested objects, and example JSON. Naming aligns with SRS-API-002 request DTOs.

### HTTP Status Code Conventions

| Operation | Success Status | Response Body |
|-----------|----------------|---------------|
| `POST` — resource creation | `201 Created` | Created resource or creation result |
| `GET` — single resource | `200 OK` | Resource detail |
| `GET` — collection / search | `200 OK` | Paginated or array wrapper |
| `PATCH` / `PUT` | `200 OK` | Updated resource |
| `POST` — command / action | `200 OK` | Command result with updated state |
| `DELETE` | `200 OK` | Revocation result (or `204 No Content` when no body — IMS uses `200` with body for traceability) |

### Shared Response Wrappers

#### `PagedResponse<T>`

| Field | Type | Description |
|-------|------|-------------|
| `data` | Array\<T\> | Page of result items |
| `page` | Integer | Current page number (1-based) |
| `pageSize` | Integer | Page size |
| `totalElements` | Long | Total matching records |
| `totalPages` | Integer | Total pages |

#### `CommandResultResponse`

Used by approve, reject, cancel, acknowledge, and similar action endpoints.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Affected resource identifier |
| `status` | String | New resource status after command |
| `processedAt` | Instant | Command processing timestamp |
| `message` | String | Optional human-readable confirmation |

#### `AuditInfoResponse`

| Field | Type | Description |
|-------|------|-------------|
| `createdAt` | Instant | Record creation timestamp |
| `createdBy` | String | Creating user ID |
| `updatedAt` | Instant | Last update timestamp |
| `updatedBy` | String | Last updating user ID |

### Shared Nested Response Objects

#### `QuantityResponse`

| Field | Type | Description |
|-------|------|-------------|
| `amount` | BigDecimal | Quantity amount |
| `unitOfMeasure` | String | UoM code |

#### `MonetaryAmountResponse`

| Field | Type | Description |
|-------|------|-------------|
| `amount` | BigDecimal | Monetary value |
| `currencyCode` | String | ISO 4217 currency |

#### `LotIdentityResponse`

| Field | Type | Description |
|-------|------|-------------|
| `lotNumber` | String | Lot/batch number |
| `expirationDate` | LocalDate | Expiration date |

#### `StockAvailabilityResponse`

| Field | Type | Description |
|-------|------|-------------|
| `onHand` | QuantityResponse | Physical on-hand quantity |
| `reserved` | QuantityResponse | Reserved quantity |
| `quarantined` | QuantityResponse | Quarantined quantity |
| `atp` | QuantityResponse | Available-to-promise |
| `ownershipType` | String | `OWNED` or `CONSIGNMENT` |

#### `AddressResponse`

| Field | Type | Description |
|-------|------|-------------|
| `line1` | String | Address line 1 |
| `line2` | String | Address line 2 |
| `city` | String | City |
| `stateProvince` | String | State or province |
| `postalCode` | String | Postal code |
| `countryCode` | String | ISO country code |

#### `ProductSummaryResponse`

| Field | Type | Description |
|-------|------|-------------|
| `sku` | String | Product SKU |
| `name` | String | Product name |
| `lifecycleStatus` | String | `ACTIVE`, `INACTIVE`, `DISCONTINUED` |
| `abcClass` | String | `A`, `B`, `C`, or null |
| `unitOfMeasure` | String | Primary UoM |

#### `ProductDetailResponse` *(extends summary)*

| Field | Type | Description |
|-------|------|-------------|
| *(all ProductSummaryResponse fields)* | | |
| `description` | String | Product description |
| `categoryCode` | String | Category code |
| `barcode` | String | Primary barcode |
| `isTraceable` | Boolean | Lot/batch required |
| `rotationPolicy` | String | `FIFO` or `FEFO` |
| `shelfLifeManaged` | Boolean | MRSL applies |
| `mrslThresholdDays` | Integer | MRSL threshold days |
| `audit` | AuditInfoResponse | Audit metadata |

#### `LocationSummaryResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location code |
| `name` | String | Location name |
| `locationType` | String | Location type enum |
| `operationalStatus` | String | Operational status |
| `parentLocationCode` | String | Parent location code |

#### `EligibilityResponse`

| Field | Type | Description |
|-------|------|-------------|
| `eligible` | Boolean | Whether transaction is permitted |
| `transactionType` | String | Evaluated transaction type |
| `reason` | String | Ineligibility reason when `eligible=false` |
| `lifecycleStatus` | String | Current product lifecycle status |

---

## M-01 — Product Catalog

### API-001 — `POST /api/v1/products`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `201 Created` |
| **Response DTO** | `ProductDetailResponse` |
| **Nested Objects** | `AuditInfoResponse` |

**Example:**
```json
{
  "sku": "SKU-WIDGET-001",
  "name": "Industrial Widget 100mm",
  "lifecycleStatus": "ACTIVE",
  "abcClass": null,
  "unitOfMeasure": "EA",
  "description": "Standard 100mm widget",
  "categoryCode": "HARDW",
  "barcode": "0123456789012",
  "isTraceable": false,
  "rotationPolicy": "FIFO",
  "shelfLifeManaged": false,
  "mrslThresholdDays": null,
  "audit": {
    "createdAt": "2026-07-06T14:30:00Z",
    "createdBy": "usr-inv-ctrl-01",
    "updatedAt": "2026-07-06T14:30:00Z",
    "updatedBy": "usr-inv-ctrl-01"
  }
}
```

---

### API-002 — `GET /api/v1/products`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `PagedResponse<ProductSummaryResponse>` |
| **Nested Objects** | `ProductSummaryResponse` |

**Example:**
```json
{
  "data": [
    {
      "sku": "SKU-WIDGET-001",
      "name": "Industrial Widget 100mm",
      "lifecycleStatus": "ACTIVE",
      "abcClass": "A",
      "unitOfMeasure": "EA"
    }
  ],
  "page": 1,
  "pageSize": 20,
  "totalElements": 1,
  "totalPages": 1
}
```

---

### API-003 — `GET /api/v1/products/{sku}`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `ProductDetailResponse` |
| **Nested Objects** | `AuditInfoResponse` |

**Example:** Same structure as API-001 response.

---

### API-004 — `PATCH /api/v1/products/{sku}`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `ProductDetailResponse` |
| **Nested Objects** | `AuditInfoResponse` |

**Example:** Same structure as API-001 with updated fields.

---

### API-005 — `POST /api/v1/products/{sku}/lifecycle-status`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `ProductStatusChangeResponse` |

| Field | Type | Description |
|-------|------|-------------|
| `sku` | String | Product SKU |
| `priorStatus` | String | Previous lifecycle status |
| `newStatus` | String | New lifecycle status |
| `effectiveDate` | LocalDate | Effective date |
| `changedAt` | Instant | Change timestamp |
| `changedBy` | String | User who made the change |

**Example:**
```json
{
  "sku": "SKU-WIDGET-001",
  "priorStatus": "ACTIVE",
  "newStatus": "DISCONTINUED",
  "effectiveDate": "2026-07-06",
  "changedAt": "2026-07-06T14:35:00Z",
  "changedBy": "usr-inv-ctrl-01"
}
```

---

### API-006 — `PUT /api/v1/products/{sku}/abc-classification`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `AbcClassificationResponse` |

| Field | Type | Description |
|-------|------|-------------|
| `sku` | String | Product SKU |
| `abcClass` | String | Assigned class `A`, `B`, or `C` |
| `classificationBasis` | String | Basis for classification |
| `effectiveDate` | LocalDate | Effective date |
| `assignedAt` | Instant | Assignment timestamp |

**Example:**
```json
{
  "sku": "SKU-WIDGET-001",
  "abcClass": "A",
  "classificationBasis": "REVENUE",
  "effectiveDate": "2026-07-06",
  "assignedAt": "2026-07-06T14:36:00Z"
}
```

---

### API-007 — `GET /api/v1/products/{sku}/eligibility`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `EligibilityResponse` |

**Example:**
```json
{
  "eligible": true,
  "transactionType": "RESERVATION",
  "reason": null,
  "lifecycleStatus": "ACTIVE"
}
```

---

### API-008 — `GET /api/v1/products/categories/{categoryCode}/products`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `PagedResponse<ProductSummaryResponse>` |

**Example:** Same structure as API-002.

---

### API-009 — `POST /api/v1/products/duplicate-resolutions`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `DuplicateResolutionResponse` |

| Field | Type | Description |
|-------|------|-------------|
| `resolutionAction` | String | Action taken |
| `sourceSku` | String | Source SKU |
| `targetSku` | String | Target SKU when merged |
| `resolvedAt` | Instant | Resolution timestamp |
| `resolvedBy` | String | Resolving user |

**Example:**
```json
{
  "resolutionAction": "MERGE",
  "sourceSku": "SKU-WIDGET-OLD",
  "targetSku": "SKU-WIDGET-001",
  "resolvedAt": "2026-07-06T14:40:00Z",
  "resolvedBy": "usr-inv-ctrl-01"
}
```

---

### API-010 — `POST /api/v1/products/import`

| Attribute | Value |
|-----------|-------|
| **HTTP Status** | `200 OK` |
| **Response DTO** | `BulkImportResultResponse` |

| Field | Type | Description |
|-------|------|-------------|
| `importMode` | String | Import mode executed |
| `totalRecords` | Integer | Records processed |
| `successCount` | Integer | Successfully imported |
| `failureCount` | Integer | Failed records |
| `errors` | Array\<ImportErrorResponse\> | Per-record errors |

**`ImportErrorResponse`:** `rowIndex` (Integer), `sku` (String), `errorCode` (String), `message` (String)

**Example:**
```json
{
  "importMode": "UPSERT",
  "totalRecords": 100,
  "successCount": 98,
  "failureCount": 2,
  "errors": [
    {
      "rowIndex": 15,
      "sku": "SKU-DUP-001",
      "errorCode": "DUPLICATE_SKU",
      "message": "SKU already exists"
    }
  ]
}
```

---

## M-02 — Warehouse Network

### API-011 — `POST /api/v1/locations`

| HTTP Status | `201 Created` | **DTO:** `LocationDetailResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location code |
| `name` | String | Location name |
| `locationType` | String | Type enum |
| `operationalStatus` | String | Status enum |
| `parentLocationCode` | String | Parent code |
| `address` | AddressResponse | Physical address |
| `plannedGoLiveDate` | LocalDate | Planned go-live |
| `isFrozen` | Boolean | Freeze flag |
| `audit` | AuditInfoResponse | Audit metadata |

**Example:**
```json
{
  "locationCode": "WH-EAST-01",
  "name": "East Coast Distribution Center",
  "locationType": "WAREHOUSE",
  "operationalStatus": "PLANNED",
  "parentLocationCode": "NET-US-EAST",
  "address": {
    "line1": "100 Warehouse Blvd",
    "line2": null,
    "city": "Newark",
    "stateProvince": "NJ",
    "postalCode": "07102",
    "countryCode": "US"
  },
  "plannedGoLiveDate": "2026-08-01",
  "isFrozen": false,
  "audit": {
    "createdAt": "2026-07-06T14:45:00Z",
    "createdBy": "usr-inv-ctrl-01",
    "updatedAt": "2026-07-06T14:45:00Z",
    "updatedBy": "usr-inv-ctrl-01"
  }
}
```

---

### API-012 — `GET /api/v1/locations`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<LocationSummaryResponse>`

**Example:**
```json
{
  "data": [
    {
      "locationCode": "WH-EAST-01",
      "name": "East Coast Distribution Center",
      "locationType": "WAREHOUSE",
      "operationalStatus": "ACTIVE",
      "parentLocationCode": "NET-US-EAST"
    }
  ],
  "page": 1,
  "pageSize": 20,
  "totalElements": 1,
  "totalPages": 1
}
```

---

### API-013 — `GET /api/v1/locations/{locationCode}`

| HTTP Status | `200 OK` | **DTO:** `LocationDetailResponse` — same as API-011.

---

### API-014 — `PATCH /api/v1/locations/{locationCode}/hierarchy`

| HTTP Status | `200 OK` | **DTO:** `LocationDetailResponse` — updated hierarchy fields.

---

### API-015 — `POST /api/v1/locations/{locationCode}/storage-positions`

| HTTP Status | `201 Created` | **DTO:** `StoragePositionResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Parent location |
| `positionCode` | String | Position code |
| `zone` | String | Zone |
| `aisle` | String | Aisle |
| `bin` | String | Bin |
| `positionType` | String | Position type |
| `isActive` | Boolean | Active flag |
| `configuredAt` | Instant | Configuration timestamp |

**Example:**
```json
{
  "locationCode": "WH-EAST-01",
  "positionCode": "A-01-001",
  "zone": "A",
  "aisle": "01",
  "bin": "001",
  "positionType": "PICK_FACE",
  "isActive": true,
  "configuredAt": "2026-07-06T14:50:00Z"
}
```

---

### API-016 — `GET /api/v1/locations/{locationCode}/storage-positions`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<StoragePositionResponse>`

---

### API-017 — `POST /api/v1/locations/{locationCode}/activate`

| HTTP Status | `200 OK` | **DTO:** `LocationDetailResponse` with `operationalStatus: "ACTIVE"`.

---

### API-018 — `POST /api/v1/locations/{locationCode}/deactivate`

| HTTP Status | `200 OK` | **DTO:** `LocationDetailResponse` with `operationalStatus: "INACTIVE"`.

---

### API-019 — `POST /api/v1/locations/{locationCode}/close`

| HTTP Status | `200 OK` | **DTO:** `LocationClosureResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Closed location |
| `operationalStatus` | String | `INACTIVE` |
| `closureDate` | LocalDate | Closure date |
| `dispositionPlanReference` | String | Disposition plan ref |
| `closedAt` | Instant | Closure timestamp |

**Example:**
```json
{
  "locationCode": "WH-EAST-01",
  "operationalStatus": "INACTIVE",
  "closureDate": "2026-07-06",
  "dispositionPlanReference": "DISP-PLAN-2026-042",
  "closedAt": "2026-07-06T15:00:00Z"
}
```

---

### API-020 — `GET /api/v1/locations/{locationCode}/freeze-status`

| HTTP Status | `200 OK` | **DTO:** `LocationFreezeStatusResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location code |
| `isFrozen` | Boolean | Whether location is frozen |
| `freezeReason` | String | Reason when frozen |
| `frozenSince` | Instant | Freeze start time |
| `physicalCountId` | UUID | Linked physical count when applicable |

**Example:**
```json
{
  "locationCode": "WH-EAST-01",
  "isFrozen": true,
  "freezeReason": "PHYSICAL_INVENTORY_COUNT",
  "frozenSince": "2026-07-06T08:00:00Z",
  "physicalCountId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

---

### API-021 — `GET /api/v1/locations/{locationCode}/operational-status`

| HTTP Status | `200 OK` | **DTO:** `LocationOperationalStatusResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location code |
| `operationalStatus` | String | Current status |
| `transactionallyActive` | Boolean | Accepts inventory transactions |
| `openingBalanceApproved` | Boolean | Opening balance approved |

**Example:**
```json
{
  "locationCode": "WH-EAST-01",
  "operationalStatus": "ACTIVE",
  "transactionallyActive": true,
  "openingBalanceApproved": true
}
```

---

## M-03 — Inventory Governance

### API-022 — `POST /api/v1/governance/reason-codes`

| HTTP Status | `201 Created` | **DTO:** `ReasonCodeResponse`

| Field | Type | Description |
|-------|------|-------------|
| `code` | String | Reason code |
| `description` | String | Description |
| `transactionTypes` | Array\<String\> | Applicable transaction types |
| `isActive` | Boolean | Active flag |
| `audit` | AuditInfoResponse | Audit metadata |

**Example:**
```json
{
  "code": "ADJ-DAMAGE",
  "description": "Damaged goods adjustment",
  "transactionTypes": ["ADJUSTMENT", "WRITE_OFF"],
  "isActive": true,
  "audit": {
    "createdAt": "2026-07-06T15:05:00Z",
    "createdBy": "usr-inv-ctrl-01",
    "updatedAt": "2026-07-06T15:05:00Z",
    "updatedBy": "usr-inv-ctrl-01"
  }
}
```

---

### API-023 — `GET /api/v1/governance/reason-codes`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<ReasonCodeResponse>`

---

### API-024 — `POST /api/v1/governance/reason-codes/{code}/retire`

| HTTP Status | `200 OK` | **DTO:** `ReasonCodeResponse` with `isActive: false`

---

### API-025 — `GET /api/v1/governance/reason-codes/{code}/validate`

| HTTP Status | `200 OK` | **DTO:** `ReasonCodeValidationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `code` | String | Reason code |
| `valid` | Boolean | Valid for transaction type |
| `transactionType` | String | Evaluated type |
| `message` | String | Invalid reason when `valid=false` |

**Example:**
```json
{
  "code": "ADJ-DAMAGE",
  "valid": true,
  "transactionType": "ADJUSTMENT",
  "message": null
}
```

---

### API-026 — `POST /api/v1/governance/policies`

| HTTP Status | `201 Created` | **DTO:** `GovernancePolicyResponse`

| Field | Type | Description |
|-------|------|-------------|
| `policyId` | UUID | Policy identifier |
| `policyName` | String | Policy name |
| `effectiveFrom` | Instant | Effective start |
| `effectiveTo` | Instant | Effective end |
| `parameters` | Array\<PolicyParameterResponse\> | Policy parameters |
| `audit` | AuditInfoResponse | Audit metadata |

**Example:**
```json
{
  "policyId": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "policyName": "FY2026 Adjustment Policy",
  "effectiveFrom": "2026-07-01T00:00:00Z",
  "effectiveTo": null,
  "parameters": [
    {
      "parameterKey": "ADJUSTMENT_QTY_THRESHOLD",
      "parameterValue": "50",
      "parameterType": "QUANTITY"
    }
  ],
  "audit": {
    "createdAt": "2026-07-06T15:10:00Z",
    "createdBy": "usr-inv-ctrl-01",
    "updatedAt": "2026-07-06T15:10:00Z",
    "updatedBy": "usr-inv-ctrl-01"
  }
}
```

---

### API-027 — `PATCH /api/v1/governance/policies/{policyId}/approval-thresholds`

| HTTP Status | `200 OK` | **DTO:** `ApprovalThresholdResponse`

| Field | Type | Description |
|-------|------|-------------|
| `policyId` | UUID | Policy ID |
| `transactionType` | String | Transaction type |
| `quantityThreshold` | BigDecimal | Quantity threshold |
| `monetaryThreshold` | MonetaryAmountResponse | Monetary threshold |
| `effectiveFrom` | LocalDate | Effective date |

---

### API-028 — `PATCH /api/v1/governance/policies/{policyId}/receipt-tolerances`

| HTTP Status | `200 OK` | **DTO:** `ReceiptToleranceResponse`

| Field | Type | Description |
|-------|------|-------------|
| `policyId` | UUID | Policy ID |
| `quantityTolerancePercent` | BigDecimal | Percent tolerance |
| `quantityToleranceAbsolute` | BigDecimal | Absolute tolerance |
| `autoAcceptWithinTolerance` | Boolean | Auto-accept flag |
| `effectiveFrom` | LocalDate | Effective date |

---

### API-029 — `GET /api/v1/governance/approval-thresholds`

| HTTP Status | `200 OK` | **DTO:** `ApprovalThresholdResponse`

---

### API-030 — `GET /api/v1/governance/receipt-tolerances`

| HTTP Status | `200 OK` | **DTO:** `ReceiptToleranceResponse`

---

### API-031 — `POST /api/v1/governance/segregation-of-duties/evaluate`

| HTTP Status | `200 OK` | **DTO:** `SegregationOfDutiesEvaluationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `compliant` | Boolean | SoD compliant |
| `initiatorUserId` | String | Initiator user |
| `approverUserId` | String | Approver user |
| `transactionType` | String | Transaction type |
| `violationCode` | String | Violation code when non-compliant |
| `message` | String | Explanation |

**Example:**
```json
{
  "compliant": false,
  "initiatorUserId": "usr-wh-staff-05",
  "approverUserId": "usr-wh-staff-05",
  "transactionType": "COUNT_VARIANCE_APPROVAL",
  "violationCode": "SOD_COUNTER_APPROVER",
  "message": "Counter cannot approve own count variance"
}
```

---

## M-04 — Inventory Balance

### API-032 — `POST /api/v1/inventory/opening-balances`

| HTTP Status | `201 Created` | **DTO:** `OpeningBalancesResultResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location |
| `linesProcessed` | Integer | Lines established |
| `totalOnHandValue` | MonetaryAmountResponse | Optional total value |
| `establishedAt` | Instant | Establishment timestamp |
| `approvalReference` | String | Approval reference |

**Example:**
```json
{
  "locationCode": "WH-EAST-01",
  "linesProcessed": 250,
  "totalOnHandValue": { "amount": 1250000.00, "currencyCode": "USD" },
  "establishedAt": "2026-07-06T15:15:00Z",
  "approvalReference": "OB-APPR-2026-001"
}
```

---

### API-033 — `GET /api/v1/inventory/stock-positions`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<StockPositionSummaryResponse>`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location |
| `sku` | String | Product SKU |
| `productName` | String | Product name |
| `availability` | StockAvailabilityResponse | Quantity breakdown |
| `stockStatus` | String | Status indicator |
| `abcClass` | String | ABC class |
| `lastMovementAt` | Instant | Last movement date |

**Example:**
```json
{
  "data": [
    {
      "locationCode": "WH-EAST-01",
      "sku": "SKU-WIDGET-001",
      "productName": "Industrial Widget 100mm",
      "availability": {
        "onHand": { "amount": 500, "unitOfMeasure": "EA" },
        "reserved": { "amount": 30, "unitOfMeasure": "EA" },
        "quarantined": { "amount": 0, "unitOfMeasure": "EA" },
        "atp": { "amount": 470, "unitOfMeasure": "EA" },
        "ownershipType": "OWNED"
      },
      "stockStatus": "IN_STOCK",
      "abcClass": "A",
      "lastMovementAt": "2026-07-06T12:00:00Z"
    }
  ],
  "page": 1,
  "pageSize": 20,
  "totalElements": 1,
  "totalPages": 1
}
```

---

### API-034 — `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}`

| HTTP Status | `200 OK` | **DTO:** `StockPositionDetailResponse`

Extends summary with: `lots` (Array\<LotQuantityResponse\>), `activeHolds` (Array\<QuarantineHoldSummaryResponse\>), `policy` (StockPolicySummaryResponse), `audit` (AuditInfoResponse).

**Example:**
```json
{
  "locationCode": "WH-EAST-01",
  "sku": "SKU-WIDGET-001",
  "productName": "Industrial Widget 100mm",
  "availability": {
    "onHand": { "amount": 500, "unitOfMeasure": "EA" },
    "reserved": { "amount": 30, "unitOfMeasure": "EA" },
    "quarantined": { "amount": 0, "unitOfMeasure": "EA" },
    "atp": { "amount": 470, "unitOfMeasure": "EA" },
    "ownershipType": "OWNED"
  },
  "stockStatus": "IN_STOCK",
  "lots": [],
  "activeHolds": [],
  "policy": {
    "reorderLevel": 100,
    "minimumThreshold": 50,
    "safetyStock": 25
  },
  "audit": {
    "createdAt": "2026-07-01T00:00:00Z",
    "createdBy": "system",
    "updatedAt": "2026-07-06T12:00:00Z",
    "updatedBy": "usr-rcv-01"
  }
}
```

---

### API-035 — `GET /api/v1/inventory/availability/{sku}`

| HTTP Status | `200 OK` | **DTO:** `AvailabilityInquiryResponse`

| Field | Type | Description |
|-------|------|-------------|
| `sku` | String | Product SKU |
| `locationCode` | String | Location |
| `atp` | QuantityResponse | Available quantity |
| `canFulfillRequested` | Boolean | Meets requested qty when provided |
| `requestedQuantity` | QuantityResponse | Requested qty evaluated |
| `inquiredAt` | Instant | Inquiry timestamp |

**Example:**
```json
{
  "sku": "SKU-WIDGET-001",
  "locationCode": "WH-EAST-01",
  "atp": { "amount": 470, "unitOfMeasure": "EA" },
  "canFulfillRequested": true,
  "requestedQuantity": { "amount": 100, "unitOfMeasure": "EA" },
  "inquiredAt": "2026-07-06T15:20:00Z"
}
```

---

### API-036 — `GET /api/v1/inventory/availability/{sku}/network`

| HTTP Status | `200 OK` | **DTO:** `NetworkAvailabilityResponse`

| Field | Type | Description |
|-------|------|-------------|
| `sku` | String | Product SKU |
| `networkAtp` | QuantityResponse | Total network ATP |
| `locations` | Array\<LocationAvailabilityResponse\> | Per-location ATP |

**Example:**
```json
{
  "sku": "SKU-WIDGET-001",
  "networkAtp": { "amount": 1200, "unitOfMeasure": "EA" },
  "locations": [
    {
      "locationCode": "WH-EAST-01",
      "atp": { "amount": 470, "unitOfMeasure": "EA" },
      "stockStatus": "IN_STOCK"
    },
    {
      "locationCode": "WH-WEST-01",
      "atp": { "amount": 730, "unitOfMeasure": "EA" },
      "stockStatus": "IN_STOCK"
    }
  ]
}
```

---

### API-037 — `GET /api/v1/inventory/stock-status/{locationCode}/{sku}`

| HTTP Status | `200 OK` | **DTO:** `StockStatusIndicatorResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `stockStatus` | String | `IN_STOCK`, `LOW_STOCK`, `OUT_OF_STOCK`, `OVERSTOCK` |
| `atp` | QuantityResponse | Current ATP |
| `reorderLevel` | BigDecimal | Reorder threshold |
| `minimumThreshold` | BigDecimal | Minimum threshold |

---

### API-038 — `POST /api/v1/inventory/stock-policies`

| HTTP Status | `201 Created` | **DTO:** `StockPolicyResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `reorderLevel` | BigDecimal | Reorder level |
| `minimumThreshold` | BigDecimal | Minimum |
| `safetyStock` | BigDecimal | Safety stock |
| `maximumThreshold` | BigDecimal | Maximum |
| `leadTimeDays` | Integer | Lead time |
| `effectiveFrom` | LocalDate | Effective date |
| `audit` | AuditInfoResponse | Audit metadata |

---

### API-039 — `GET /api/v1/inventory/stock-policies/{locationCode}/{sku}`

| HTTP Status | `200 OK` | **DTO:** `StockPolicyResponse`

---

### API-040 — `PATCH /api/v1/inventory/stock-policies/{locationCode}/{sku}`

| HTTP Status | `200 OK` | **DTO:** `StockPolicyResponse` with updated thresholds.

---

### API-041 — `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/lots`

| HTTP Status | `200 OK` | **DTO:** `LotBreakdownResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `lots` | Array\<LotQuantityResponse\> | Lot-level quantities |

**`LotQuantityResponse`:** `lotIdentity` (LotIdentityResponse), `onHand` (QuantityResponse), `reserved` (QuantityResponse), `atp` (QuantityResponse), `isQuarantined` (Boolean)

---

### API-042 — `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity`

| HTTP Status | `200 OK` | **DTO:** `TransferCapacityResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Source location |
| `sku` | String | SKU |
| `onHand` | QuantityResponse | On-hand |
| `minimumThreshold` | BigDecimal | Source minimum |
| `safetyStock` | BigDecimal | Safety stock |
| `maxTransferable` | QuantityResponse | Max spare transferable |
| `canFulfillRequested` | Boolean | Meets requested qty |

**Example:**
```json
{
  "locationCode": "WH-WEST-01",
  "sku": "SKU-WIDGET-001",
  "onHand": { "amount": 730, "unitOfMeasure": "EA" },
  "minimumThreshold": 100,
  "safetyStock": 50,
  "maxTransferable": { "amount": 580, "unitOfMeasure": "EA" },
  "canFulfillRequested": true
}
```

---

### API-043 — `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations`

| HTTP Status | `201 Created` | **DTO:** `ReservationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `reservationId` | UUID | Reservation ID |
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `reservedQuantity` | QuantityResponse | Reserved qty |
| `orderId` | String | Order reference |
| `orderLineId` | String | Order line reference |
| `reservedAt` | Instant | Reservation time |
| `expiresAt` | Instant | Expiry time |
| `remainingAtp` | QuantityResponse | ATP after reservation |

**Example:**
```json
{
  "reservationId": "c3d4e5f6-a7b8-9012-cdef-123456789012",
  "locationCode": "WH-EAST-01",
  "sku": "SKU-WIDGET-001",
  "reservedQuantity": { "amount": 50, "unitOfMeasure": "EA" },
  "orderId": "ORD-2026-0042",
  "orderLineId": "LINE-001",
  "reservedAt": "2026-07-06T15:25:00Z",
  "expiresAt": "2026-07-13T15:25:00Z",
  "remainingAtp": { "amount": 420, "unitOfMeasure": "EA" }
}
```

---

### API-044 — `POST .../reservations/{reservationId}/release`

| HTTP Status | `200 OK` | **DTO:** `ReservationReleaseResponse`

| Field | Type | Description |
|-------|------|-------------|
| `reservationId` | UUID | Released reservation |
| `releasedQuantity` | QuantityResponse | Released qty |
| `releaseReason` | String | Release reason |
| `releasedAt` | Instant | Release timestamp |
| `restoredAtp` | QuantityResponse | ATP after release |

---

### API-045 — `POST .../quarantine-holds`

| HTTP Status | `201 Created` | **DTO:** `QuarantineHoldResponse`

| Field | Type | Description |
|-------|------|-------------|
| `holdId` | UUID | Hold ID |
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `heldQuantity` | QuantityResponse | Held qty |
| `holdReason` | String | Hold reason |
| `reasonCode` | String | Reason code |
| `appliedAt` | Instant | Applied timestamp |
| `remainingAtp` | QuantityResponse | ATP after hold |

---

### API-046 — `POST .../quarantine-holds/{holdId}/release`

| HTTP Status | `200 OK` | **DTO:** `QuarantineHoldReleaseResponse` — `holdId`, `releasedQuantity`, `disposition`, `releasedAt`, `restoredAtp`.

---

### API-047 — `POST .../consignment-ownership`

| HTTP Status | `200 OK` | **DTO:** `ConsignmentOwnershipTransferResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `transferredQuantity` | QuantityResponse | Qty transferred |
| `consumptionReference` | String | Consumption ref |
| `transferredAt` | Instant | Transfer timestamp |
| `newOwnershipType` | String | `OWNED` |

---

### API-048 — `POST .../promotional-segregation`

| HTTP Status | `200 OK` | **DTO:** `PromotionalSegregationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `campaignId` | String | Campaign ID |
| `segregatedQuantity` | QuantityResponse | Ring-fenced qty |
| `generalAtp` | QuantityResponse | Remaining general ATP |
| `segregatedAt` | Instant | Segregation timestamp |

---

## M-05 — Procurement & Supplier

### API-049 — `POST /api/v1/suppliers`

| HTTP Status | `201 Created` | **DTO:** `SupplierDetailResponse`

| Field | Type | Description |
|-------|------|-------------|
| `supplierCode` | String | Supplier code |
| `name` | String | Supplier name |
| `contactEmail` | String | Contact email |
| `contactPhone` | String | Contact phone |
| `paymentTermsDays` | Integer | Payment terms |
| `defaultLeadTimeDays` | Integer | Lead time |
| `isConsignment` | Boolean | Consignment flag |
| `isActive` | Boolean | Active flag |
| `currencyCode` | String | Default currency |
| `audit` | AuditInfoResponse | Audit metadata |

**Example:**
```json
{
  "supplierCode": "SUP-ACME-01",
  "name": "Acme Industrial Supply",
  "contactEmail": "orders@acme.example.com",
  "contactPhone": "+1-555-0100",
  "paymentTermsDays": 30,
  "defaultLeadTimeDays": 14,
  "isConsignment": false,
  "isActive": true,
  "currencyCode": "USD",
  "audit": {
    "createdAt": "2026-07-06T15:30:00Z",
    "createdBy": "usr-buyer-01",
    "updatedAt": "2026-07-06T15:30:00Z",
    "updatedBy": "usr-buyer-01"
  }
}
```

---

### API-050 — `GET /api/v1/suppliers`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<SupplierSummaryResponse>` — `supplierCode`, `name`, `isActive`, `isConsignment`.

---

### API-051 — `GET /api/v1/suppliers/{supplierCode}`

| HTTP Status | `200 OK` | **DTO:** `SupplierDetailResponse`

---

### API-052 — `PATCH /api/v1/suppliers/{supplierCode}`

| HTTP Status | `200 OK` | **DTO:** `SupplierDetailResponse` (updated).

---

### API-053 — `POST /api/v1/suppliers/{supplierCode}/deactivate`

| HTTP Status | `200 OK` | **DTO:** `SupplierDetailResponse` with `isActive: false`.

---

### API-054 — `POST /api/v1/procurement/requisitions`

| HTTP Status | `201 Created` | **DTO:** `PurchaseRequisitionResponse`

| Field | Type | Description |
|-------|------|-------------|
| `requisitionId` | UUID | Requisition ID |
| `status` | String | `SUBMITTED` |
| `receivingLocationCode` | String | Target location |
| `justification` | String | Justification |
| `lines` | Array\<RequisitionLineResponse\> | Line items |
| `submittedAt` | Instant | Submission time |
| `audit` | AuditInfoResponse | Audit metadata |

**`RequisitionLineResponse`:** `lineId`, `sku`, `productName`, `requestedQuantity` (QuantityResponse), `neededByDate`

**Example:**
```json
{
  "requisitionId": "d4e5f6a7-b8c9-0123-def0-123456789abc",
  "status": "SUBMITTED",
  "receivingLocationCode": "WH-EAST-01",
  "justification": "Class A SKU below reorder level",
  "lines": [
    {
      "lineId": "e5f6a7b8-c9d0-1234-ef01-234567890bcd",
      "sku": "SKU-WIDGET-001",
      "productName": "Industrial Widget 100mm",
      "requestedQuantity": { "amount": 200, "unitOfMeasure": "EA" },
      "neededByDate": "2026-07-20"
    }
  ],
  "submittedAt": "2026-07-06T15:35:00Z",
  "audit": {
    "createdAt": "2026-07-06T15:35:00Z",
    "createdBy": "usr-buyer-01",
    "updatedAt": "2026-07-06T15:35:00Z",
    "updatedBy": "usr-buyer-01"
  }
}
```

---

### API-055 — `GET /api/v1/procurement/requisitions/{requisitionId}`

| HTTP Status | `200 OK` | **DTO:** `PurchaseRequisitionResponse`

---

### API-056 — `POST .../requisitions/{requisitionId}/approve`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `id`, `status: "APPROVED"`, `processedAt`, `message`

---

### API-057 — `POST .../requisitions/{requisitionId}/reject`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "REJECTED"`

---

### API-058 — `POST .../requisitions/{requisitionId}/convert-to-po`

| HTTP Status | `201 Created` | **DTO:** `PurchaseOrderResponse` (see API-059).

---

### API-059 — `POST /api/v1/procurement/purchase-orders`

| HTTP Status | `201 Created` | **DTO:** `PurchaseOrderResponse`

| Field | Type | Description |
|-------|------|-------------|
| `purchaseOrderId` | UUID | PO ID |
| `poNumber` | String | Business PO number |
| `status` | String | `OPEN` |
| `supplierCode` | String | Supplier |
| `supplierName` | String | Supplier name |
| `receivingLocationCode` | String | Receiving location |
| `expectedDeliveryDate` | LocalDate | Expected delivery |
| `currencyCode` | String | Currency |
| `totalAmount` | MonetaryAmountResponse | PO total |
| `lines` | Array\<PurchaseOrderLineResponse\> | PO lines |
| `audit` | AuditInfoResponse | Audit metadata |

**`PurchaseOrderLineResponse`:** `lineId`, `lineNumber`, `sku`, `productName`, `orderedQuantity`, `receivedQuantity`, `remainingQuantity`, `unitPrice`

**Example:**
```json
{
  "purchaseOrderId": "f6a7b8c9-d0e1-2345-f012-345678901cde",
  "poNumber": "PO-2026-0088",
  "status": "OPEN",
  "supplierCode": "SUP-ACME-01",
  "supplierName": "Acme Industrial Supply",
  "receivingLocationCode": "WH-EAST-01",
  "expectedDeliveryDate": "2026-07-20",
  "currencyCode": "USD",
  "totalAmount": { "amount": 5000.00, "currencyCode": "USD" },
  "lines": [
    {
      "lineId": "a7b8c9d0-e1f2-3456-0123-456789012def",
      "lineNumber": 1,
      "sku": "SKU-WIDGET-001",
      "productName": "Industrial Widget 100mm",
      "orderedQuantity": { "amount": 200, "unitOfMeasure": "EA" },
      "receivedQuantity": { "amount": 0, "unitOfMeasure": "EA" },
      "remainingQuantity": { "amount": 200, "unitOfMeasure": "EA" },
      "unitPrice": { "amount": 25.00, "currencyCode": "USD" }
    }
  ],
  "audit": {
    "createdAt": "2026-07-06T15:40:00Z",
    "createdBy": "usr-buyer-01",
    "updatedAt": "2026-07-06T15:40:00Z",
    "updatedBy": "usr-buyer-01"
  }
}
```

---

### API-060 — `GET /api/v1/procurement/purchase-orders`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<PurchaseOrderSummaryResponse>`

---

### API-061 — `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}`

| HTTP Status | `200 OK` | **DTO:** `PurchaseOrderResponse`

---

### API-062 — `PATCH /api/v1/procurement/purchase-orders/{purchaseOrderId}`

| HTTP Status | `200 OK` | **DTO:** `PurchaseOrderResponse` (amended).

---

### API-063 — `POST .../purchase-orders/{purchaseOrderId}/cancel`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "CANCELLED"`

---

### API-064 — `POST .../expected-deliveries`

| HTTP Status | `200 OK` | **DTO:** `InboundDeliveryScheduleResponse`

| Field | Type | Description |
|-------|------|-------------|
| `purchaseOrderId` | UUID | PO ID |
| `expectedArrivalDate` | LocalDate | Expected arrival |
| `carrierReference` | String | Carrier ref |
| `lineDeliveries` | Array\<LineDeliveryScheduleResponse\> | Per-line schedule |
| `scheduledAt` | Instant | Schedule timestamp |

---

### API-065 — `GET .../validate-for-receipt`

| HTTP Status | `200 OK` | **DTO:** `PoReceiptValidationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `purchaseOrderId` | UUID | PO ID |
| `validForReceipt` | Boolean | Receipt authorized |
| `poStatus` | String | PO status |
| `receivingLocationCode` | String | Authorized location |
| `message` | String | Invalid reason when false |

**Example:**
```json
{
  "purchaseOrderId": "f6a7b8c9-d0e1-2345-f012-345678901cde",
  "validForReceipt": true,
  "poStatus": "OPEN",
  "receivingLocationCode": "WH-EAST-01",
  "message": null
}
```

---

## M-06 — Inbound Receiving

### API-066 — `POST /api/v1/inbound/goods-receipts`

| HTTP Status | `201 Created` | **DTO:** `GoodsReceiptResponse`

| Field | Type | Description |
|-------|------|-------------|
| `goodsReceiptId` | UUID | Receipt ID |
| `receiptNumber` | String | Business receipt number |
| `status` | String | `DRAFT` |
| `purchaseOrderId` | UUID | Linked PO |
| `receivingLocationCode` | String | Location |
| `supplierCode` | String | Supplier |
| `lines` | Array\<GoodsReceiptLineResponse\> | Receipt lines |
| `audit` | AuditInfoResponse | Audit metadata |

**Example:**
```json
{
  "goodsReceiptId": "b8c9d0e1-f2a3-4567-8901-234567890abc",
  "receiptNumber": "GR-2026-0156",
  "status": "DRAFT",
  "purchaseOrderId": "f6a7b8c9-d0e1-2345-f012-345678901cde",
  "receivingLocationCode": "WH-EAST-01",
  "supplierCode": "SUP-ACME-01",
  "lines": [
    {
      "lineId": "c9d0e1f2-a3b4-5678-9012-345678901bcd",
      "sku": "SKU-WIDGET-001",
      "expectedQuantity": { "amount": 200, "unitOfMeasure": "EA" },
      "acceptedQuantity": { "amount": 0, "unitOfMeasure": "EA" },
      "putAwayStatus": "PENDING"
    }
  ],
  "audit": {
    "createdAt": "2026-07-06T16:00:00Z",
    "createdBy": "usr-rcv-01",
    "updatedAt": "2026-07-06T16:00:00Z",
    "updatedBy": "usr-rcv-01"
  }
}
```

---

### API-067 — `GET /api/v1/inbound/goods-receipts`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<GoodsReceiptSummaryResponse>`

---

### API-068 — `GET /api/v1/inbound/goods-receipts/{goodsReceiptId}`

| HTTP Status | `200 OK` | **DTO:** `GoodsReceiptResponse` (full detail with discrepancies, put-away state).

---

### API-069 — `POST .../verify`

| HTTP Status | `200 OK` | **DTO:** `GoodsReceiptResponse` with `status: "VERIFIED"`.

---

### API-070 — `POST .../discrepancies`

| HTTP Status | `201 Created` | **DTO:** `ReceiptDiscrepancyResponse`

| Field | Type | Description |
|-------|------|-------------|
| `discrepancyId` | UUID | Discrepancy ID |
| `goodsReceiptId` | UUID | Receipt ID |
| `lineId` | UUID | Line ID |
| `discrepancyType` | String | Type enum |
| `varianceQuantity` | QuantityResponse | Variance qty |
| `status` | String | `OPEN` |
| `recordedAt` | Instant | Recorded timestamp |

---

### API-071 — `GET .../discrepancies`

| HTTP Status | `200 OK` | **DTO:** `Array<ReceiptDiscrepancyResponse>` or `PagedResponse`

---

### API-072 — `POST .../discrepancies/{discrepancyId}/resolve`

| HTTP Status | `200 OK` | **DTO:** `ReceiptDiscrepancyResponse` with `status: "RESOLVED"`.

---

### API-073 — `POST .../put-away`

| HTTP Status | `200 OK` | **DTO:** `PutAwayCompletionResponse`

| Field | Type | Description |
|-------|------|-------------|
| `goodsReceiptId` | UUID | Receipt ID |
| `status` | String | `COMPLETED` |
| `putAwayLines` | Array\<PutAwayLineResultResponse\> | Put-away results |
| `stockAvailableAt` | Instant | When stock became ATP-available |

**Example:**
```json
{
  "goodsReceiptId": "b8c9d0e1-f2a3-4567-8901-234567890abc",
  "status": "COMPLETED",
  "putAwayLines": [
    {
      "receiptLineId": "c9d0e1f2-a3b4-5678-9012-345678901bcd",
      "quantity": { "amount": 200, "unitOfMeasure": "EA" },
      "storagePositionCode": "A-01-001",
      "putAwayAt": "2026-07-06T16:30:00Z"
    }
  ],
  "stockAvailableAt": "2026-07-06T16:30:00Z"
}
```

---

### API-074 — `GET /api/v1/inbound/pending-put-away`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<PendingPutAwayResponse>`

---

### API-075 — `POST /api/v1/inbound/ad-hoc-receipts`

| HTTP Status | `201 Created` | **DTO:** `GoodsReceiptResponse` (ad-hoc type).

---

### API-076 — `POST /api/v1/inbound/return-receipts`

| HTTP Status | `201 Created` | **DTO:** `ReturnReceiptResponse`

| Field | Type | Description |
|-------|------|-------------|
| `returnReceiptId` | UUID | Return receipt ID |
| `returnAuthorizationId` | UUID | RMA reference |
| `goodsReceiptId` | UUID | Linked goods receipt |
| `status` | String | `RECEIVED` |
| `lines` | Array\<ReturnReceiptLineResponse\> | Received lines |
| `receivedAt` | Instant | Receipt timestamp |

---

### API-077 — `POST /api/v1/inbound/supplier-invoices`

| HTTP Status | `201 Created` | **DTO:** `SupplierInvoiceResponse`

| Field | Type | Description |
|-------|------|-------------|
| `invoiceId` | UUID | Invoice ID |
| `invoiceNumber` | String | Supplier invoice number |
| `supplierCode` | String | Supplier |
| `purchaseOrderId` | UUID | PO reference |
| `status` | String | `REGISTERED` |
| `totalAmount` | MonetaryAmountResponse | Invoice total |
| `matchStatus` | String | `PENDING` |
| `lines` | Array\<InvoiceLineResponse\> | Invoice lines |
| `audit` | AuditInfoResponse | Audit metadata |

---

### API-078 — `GET /api/v1/inbound/supplier-invoices/{invoiceId}`

| HTTP Status | `200 OK` | **DTO:** `SupplierInvoiceResponse` with `matchStatus`, `threeWayMatchResult`.

---

### API-079 — `POST .../three-way-match`

| HTTP Status | `200 OK` | **DTO:** `ThreeWayMatchResultResponse`

| Field | Type | Description |
|-------|------|-------------|
| `invoiceId` | UUID | Invoice ID |
| `matchStatus` | String | `MATCHED` or `EXCEPTION` |
| `poMatch` | Boolean | PO aligned |
| `receiptMatch` | Boolean | Receipt aligned |
| `invoiceMatch` | Boolean | Invoice aligned |
| `exceptions` | Array\<MatchExceptionResponse\> | Line-level exceptions |
| `evaluatedAt` | Instant | Evaluation timestamp |

**Example:**
```json
{
  "invoiceId": "d0e1f2a3-b4c5-6789-0123-456789012def",
  "matchStatus": "MATCHED",
  "poMatch": true,
  "receiptMatch": true,
  "invoiceMatch": true,
  "exceptions": [],
  "evaluatedAt": "2026-07-06T17:00:00Z"
}
```

---

### API-080 — `POST .../authorize-payment`

| HTTP Status | `200 OK` | **DTO:** `InvoicePaymentAuthorizationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `invoiceId` | UUID | Invoice ID |
| `paymentAuthorized` | Boolean | Authorization granted |
| `authorizedAt` | Instant | Authorization time |
| `authorizedBy` | String | Authorizing user |
| `paymentDueDate` | LocalDate | Payment due date |

---

## M-07 — Order Fulfillment

### API-081 — `POST /api/v1/fulfillment/orders`

| HTTP Status | `201 Created` | **DTO:** `CustomerOrderResponse`

| Field | Type | Description |
|-------|------|-------------|
| `orderId` | UUID | Order ID |
| `orderNumber` | String | Business order number |
| `status` | String | `DRAFT` |
| `channel` | String | Sales channel |
| `customerReference` | String | Customer ref |
| `shipFromLocationCode` | String | Ship-from location |
| `lines` | Array\<OrderLineResponse\> | Order lines |
| `audit` | AuditInfoResponse | Audit metadata |

**Example:**
```json
{
  "orderId": "e1f2a3b4-c5d6-7890-1234-567890123def",
  "orderNumber": "ORD-2026-0042",
  "status": "DRAFT",
  "channel": "B2B",
  "customerReference": "CUST-ACME-001",
  "shipFromLocationCode": "WH-EAST-01",
  "lines": [
    {
      "lineId": "f2a3b4c5-d6e7-8901-2345-678901234ef0",
      "lineNumber": 1,
      "sku": "SKU-WIDGET-001",
      "productName": "Industrial Widget 100mm",
      "requestedQuantity": { "amount": 50, "unitOfMeasure": "EA" },
      "reservedQuantity": { "amount": 0, "unitOfMeasure": "EA" },
      "shippedQuantity": { "amount": 0, "unitOfMeasure": "EA" },
      "lineStatus": "OPEN"
    }
  ],
  "audit": {
    "createdAt": "2026-07-06T17:05:00Z",
    "createdBy": "usr-cs-01",
    "updatedAt": "2026-07-06T17:05:00Z",
    "updatedBy": "usr-cs-01"
  }
}
```

---

### API-082 — `GET /api/v1/fulfillment/orders`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<CustomerOrderSummaryResponse>`

---

### API-083 — `GET /api/v1/fulfillment/orders/{orderId}`

| HTTP Status | `200 OK` | **DTO:** `CustomerOrderResponse` (full detail).

---

### API-084 — `POST .../availability`

| HTTP Status | `200 OK` | **DTO:** `OrderAvailabilityResponse`

| Field | Type | Description |
|-------|------|-------------|
| `orderId` | UUID | Order ID |
| `fullyAvailable` | Boolean | All lines fulfillable |
| `lines` | Array\<LineAvailabilityResponse\> | Per-line ATP check |
| `confirmedAt` | Instant | Confirmation timestamp |

**`LineAvailabilityResponse`:** `lineId`, `sku`, `requestedQuantity`, `atp`, `canFulfill`, `shortfallQuantity`

**Example:**
```json
{
  "orderId": "e1f2a3b4-c5d6-7890-1234-567890123def",
  "fullyAvailable": true,
  "lines": [
    {
      "lineId": "f2a3b4c5-d6e7-8901-2345-678901234ef0",
      "sku": "SKU-WIDGET-001",
      "requestedQuantity": { "amount": 50, "unitOfMeasure": "EA" },
      "atp": { "amount": 470, "unitOfMeasure": "EA" },
      "canFulfill": true,
      "shortfallQuantity": null
    }
  ],
  "confirmedAt": "2026-07-06T17:10:00Z"
}
```

---

### API-085 — `POST .../confirm`

| HTTP Status | `200 OK` | **DTO:** `CustomerOrderResponse` with `status: "CONFIRMED"` and reservation IDs on lines.

---

### API-086 — `POST .../cancel`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "CANCELLED"`

---

### API-087 — `POST .../multi-location-plan`

| HTTP Status | `200 OK` | **DTO:** `MultiLocationFulfillmentPlanResponse`

| Field | Type | Description |
|-------|------|-------------|
| `orderId` | UUID | Order ID |
| `planId` | UUID | Plan ID |
| `allocations` | Array\<LocationAllocationResponse\> | Location allocations |
| `reservations` | Array\<ReservationResponse\> | Created reservations |
| `createdAt` | Instant | Plan creation time |

---

### API-088 — `POST .../pick-lists`

| HTTP Status | `201 Created` | **DTO:** `PickListResponse`

| Field | Type | Description |
|-------|------|-------------|
| `pickId` | UUID | Pick list ID |
| `orderId` | UUID | Order ID |
| `status` | String | `ASSIGNED` |
| `assignedToUserId` | String | Picker user |
| `pickLines` | Array\<PickLineResponse\> | Lines to pick |
| `assignedAt` | Instant | Assignment time |

---

### API-089 — `GET .../pick-lists/awaiting`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<PickListSummaryResponse>`

---

### API-090 — `POST .../picks/{pickId}/verify`

| HTTP Status | `200 OK` | **DTO:** `PickVerificationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `pickId` | UUID | Pick ID |
| `orderId` | UUID | Order ID |
| `status` | String | `VERIFIED` |
| `verifiedLines` | Array\<VerifiedPickLineResponse\> | Verified picks |
| `verifiedAt` | Instant | Verification time |

---

### API-091 — `POST .../pack`

| HTTP Status | `200 OK` | **DTO:** `PackCompletionResponse`

| Field | Type | Description |
|-------|------|-------------|
| `orderId` | UUID | Order ID |
| `status` | String | `PACKED` |
| `packages` | Array\<PackageResponse\> | Packed packages |
| `packedAt` | Instant | Pack completion time |

---

### API-092 — `POST .../shipments`

| HTTP Status | `201 Created` | **DTO:** `ShipmentResponse`

| Field | Type | Description |
|-------|------|-------------|
| `shipmentId` | UUID | Shipment ID |
| `orderId` | UUID | Order ID |
| `status` | String | `DISPATCHED` |
| `carrierCode` | String | Carrier |
| `trackingNumber` | String | Tracking number |
| `shipmentLines` | Array\<ShipmentLineResponse\> | Shipped lines |
| `shippedAt` | Instant | Dispatch time |

**Example:**
```json
{
  "shipmentId": "a3b4c5d6-e7f8-9012-3456-789012345abc",
  "orderId": "e1f2a3b4-c5d6-7890-1234-567890123def",
  "status": "DISPATCHED",
  "carrierCode": "FEDEX",
  "trackingNumber": "794612345678",
  "shipmentLines": [
    {
      "orderLineId": "f2a3b4c5-d6e7-8901-2345-678901234ef0",
      "sku": "SKU-WIDGET-001",
      "shippedQuantity": { "amount": 50, "unitOfMeasure": "EA" }
    }
  ],
  "shippedAt": "2026-07-06T18:00:00Z"
}
```

---

### API-093 — `POST .../partial-fulfillment`

| HTTP Status | `200 OK` | **DTO:** `PartialFulfillmentResponse`

| Field | Type | Description |
|-------|------|-------------|
| `orderId` | UUID | Order ID |
| `fulfilledLines` | Array\<FulfilledLineResponse\> | Fulfilled portion |
| `backorderCreated` | Boolean | Backorder created for remainder |
| `backorderId` | UUID | Backorder ID when created |
| `shipmentId` | UUID | Partial shipment ID |

---

### API-094 — `POST .../backorders`

| HTTP Status | `201 Created` | **DTO:** `BackorderResponse`

| Field | Type | Description |
|-------|------|-------------|
| `backorderId` | UUID | Backorder ID |
| `orderId` | UUID | Order ID |
| `status` | String | `OPEN` |
| `lines` | Array\<BackorderLineResponse\> | Backordered lines |
| `customerAcknowledgmentReference` | String | Customer ack ref |
| `createdAt` | Instant | Creation time |

---

### API-095 — `POST /api/v1/fulfillment/backorders/{backorderId}/fulfill`

| HTTP Status | `200 OK` | **DTO:** `BackorderFulfillmentResponse` — `backorderId`, `fulfilledQuantity`, `reservationId`, `shipmentId`, `fulfilledAt`.

---

### API-096 — `POST .../exceptions`

| HTTP Status | `201 Created` | **DTO:** `FulfillmentExceptionResponse`

| Field | Type | Description |
|-------|------|-------------|
| `exceptionId` | UUID | Exception ID |
| `orderId` | UUID | Order ID |
| `exceptionType` | String | Exception type |
| `status` | String | `OPEN` |
| `description` | String | Description |
| `raisedAt` | Instant | Raised timestamp |

---

### API-097 — `GET .../status`

| HTTP Status | `200 OK` | **DTO:** `OrderFulfillmentStatusResponse`

| Field | Type | Description |
|-------|------|-------------|
| `orderId` | UUID | Order ID |
| `orderNumber` | String | Order number |
| `overallStatus` | String | Aggregate status |
| `reservationStatus` | String | Reservation state |
| `pickStatus` | String | Pick state |
| `shipStatus` | String | Ship state |
| `lines` | Array\<LineFulfillmentStatusResponse\> | Per-line status |
| `lastUpdatedAt` | Instant | Last status update |

**Example:**
```json
{
  "orderId": "e1f2a3b4-c5d6-7890-1234-567890123def",
  "orderNumber": "ORD-2026-0042",
  "overallStatus": "SHIPPED",
  "reservationStatus": "FULFILLED",
  "pickStatus": "VERIFIED",
  "shipStatus": "DISPATCHED",
  "lines": [
    {
      "lineId": "f2a3b4c5-d6e7-8901-2345-678901234ef0",
      "sku": "SKU-WIDGET-001",
      "requestedQuantity": { "amount": 50, "unitOfMeasure": "EA" },
      "reservedQuantity": { "amount": 50, "unitOfMeasure": "EA" },
      "shippedQuantity": { "amount": 50, "unitOfMeasure": "EA" },
      "backorderedQuantity": { "amount": 0, "unitOfMeasure": "EA" },
      "lineStatus": "SHIPPED"
    }
  ],
  "lastUpdatedAt": "2026-07-06T18:00:00Z"
}
```

---

## M-08 — Network Transfer

### API-098 — `POST /api/v1/transfers`

| HTTP Status | `201 Created` | **DTO:** `StockTransferResponse`

| Field | Type | Description |
|-------|------|-------------|
| `transferId` | UUID | Transfer ID |
| `transferNumber` | String | Business transfer number |
| `status` | String | `REQUESTED` |
| `sourceLocationCode` | String | Source |
| `destinationLocationCode` | String | Destination |
| `justification` | String | Justification |
| `lines` | Array\<TransferLineResponse\> | Transfer lines |
| `requestedAt` | Instant | Request time |

**Example:**
```json
{
  "transferId": "b4c5d6e7-f8a9-0123-4567-890123456abc",
  "transferNumber": "TRF-2026-0033",
  "status": "REQUESTED",
  "sourceLocationCode": "WH-WEST-01",
  "destinationLocationCode": "WH-EAST-01",
  "justification": "East coast stockout; excess at west",
  "lines": [
    {
      "lineId": "c5d6e7f8-a9b0-1234-5678-901234567bcd",
      "sku": "SKU-WIDGET-001",
      "requestedQuantity": { "amount": 100, "unitOfMeasure": "EA" },
      "approvedQuantity": null,
      "dispatchedQuantity": null,
      "receivedQuantity": null
    }
  ],
  "requestedAt": "2026-07-06T18:10:00Z"
}
```

---

### API-099 — `GET /api/v1/transfers`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<StockTransferSummaryResponse>`

---

### API-100 — `GET /api/v1/transfers/{transferId}`

| HTTP Status | `200 OK` | **DTO:** `StockTransferResponse` (full with in-transit state).

---

### API-101 — `POST .../approve`

| HTTP Status | `200 OK` | **DTO:** `StockTransferResponse` with `status: "APPROVED"`.

---

### API-102 — `POST .../reject`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "REJECTED"`

---

### API-103 — `POST .../dispatch`

| HTTP Status | `200 OK` | **DTO:** `StockTransferResponse` with `status: "IN_TRANSIT"`.

---

### API-104 — `POST .../receive`

| HTTP Status | `200 OK` | **DTO:** `StockTransferResponse` with `status: "RECEIVED"`.

---

### API-105 — `POST .../cancel`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "CANCELLED"`

---

### API-106 — `GET /api/v1/transfers/pending-approvals`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<StockTransferSummaryResponse>`

---

### API-107 — `GET /api/v1/transfers/in-transit`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<InTransitStockResponse>`

| Field | Type | Description |
|-------|------|-------------|
| `transferId` | UUID | Transfer ID |
| `sku` | String | SKU |
| `sourceLocationCode` | String | Source |
| `destinationLocationCode` | String | Destination |
| `inTransitQuantity` | QuantityResponse | In-transit qty |
| `dispatchedAt` | Instant | Dispatch time |
| `isOverdue` | Boolean | Overdue flag |

---

## M-09 — Inventory Accuracy

### API-108 — `POST /api/v1/accuracy/cycle-counts`

| HTTP Status | `201 Created` | **DTO:** `CycleCountResponse`

| Field | Type | Description |
|-------|------|-------------|
| `cycleCountId` | UUID | Count ID |
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `status` | String | `SCHEDULED` |
| `scheduledDate` | LocalDate | Scheduled date |
| `assignedToUserId` | String | Counter |
| `priority` | String | Priority |

**Example:**
```json
{
  "cycleCountId": "d6e7f8a9-b0c1-2345-6789-012345678cde",
  "locationCode": "WH-EAST-01",
  "sku": "SKU-WIDGET-001",
  "status": "SCHEDULED",
  "scheduledDate": "2026-07-07",
  "assignedToUserId": "usr-wh-staff-03",
  "priority": "HIGH"
}
```

---

### API-109 — `GET /api/v1/accuracy/cycle-counts`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<CycleCountSummaryResponse>`

---

### API-110 — `GET /api/v1/accuracy/cycle-counts/{cycleCountId}`

| HTTP Status | `200 OK` | **DTO:** `CycleCountAssignmentResponse` — **excludes system quantity** (blind count).

| Field | Type | Description |
|-------|------|-------------|
| `cycleCountId` | UUID | Count ID |
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `productName` | String | Product name |
| `status` | String | Status |
| `scheduledDate` | LocalDate | Scheduled date |
| `storagePositionCode` | String | Position hint (optional) |

---

### API-111 — `POST .../result`

| HTTP Status | `200 OK` | **DTO:** `CycleCountResultResponse`

| Field | Type | Description |
|-------|------|-------------|
| `cycleCountId` | UUID | Count ID |
| `status` | String | `COMPLETED` or `VARIANCE_DETECTED` |
| `physicalQuantity` | QuantityResponse | Submitted count |
| `varianceQuantity` | QuantityResponse | Variance (returned after submission) |
| `varianceId` | UUID | Variance case ID when variance exists |
| `submittedAt` | Instant | Submission time |

**Example:**
```json
{
  "cycleCountId": "d6e7f8a9-b0c1-2345-6789-012345678cde",
  "status": "VARIANCE_DETECTED",
  "physicalQuantity": { "amount": 495, "unitOfMeasure": "EA" },
  "varianceQuantity": { "amount": -5, "unitOfMeasure": "EA" },
  "varianceId": "e7f8a9b0-c1d2-3456-7890-123456789def",
  "submittedAt": "2026-07-07T09:00:00Z"
}
```

---

### API-112 — `POST /api/v1/accuracy/physical-counts`

| HTTP Status | `201 Created` | **DTO:** `PhysicalInventoryCountResponse`

| Field | Type | Description |
|-------|------|-------------|
| `physicalCountId` | UUID | Count ID |
| `locationCode` | String | Location |
| `status` | String | `IN_PROGRESS` |
| `freezeImposed` | Boolean | `true` |
| `plannedStartDate` | LocalDate | Start date |
| `plannedEndDate` | LocalDate | End date |
| `startedAt` | Instant | Start timestamp |

---

### API-113 — `GET /api/v1/accuracy/physical-counts/{physicalCountId}`

| HTTP Status | `200 OK` | **DTO:** `PhysicalInventoryCountResponse` with progress metrics.

---

### API-114 — `POST .../results`

| HTTP Status | `200 OK` | **DTO:** `PhysicalCountLineResultResponse`

| Field | Type | Description |
|-------|------|-------------|
| `physicalCountId` | UUID | Count ID |
| `linesRecorded` | Integer | Lines recorded in batch |
| `totalLinesRecorded` | Integer | Cumulative lines |
| `recordedAt` | Instant | Batch timestamp |

---

### API-115 — `POST .../certify`

| HTTP Status | `200 OK` | **DTO:** `PhysicalCountCertificationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `physicalCountId` | UUID | Count ID |
| `status` | String | `CERTIFIED` |
| `freezeReleased` | Boolean | `true` |
| `varianceCount` | Integer | Variances identified |
| `varianceIds` | Array\<UUID\> | Variance case IDs |
| `certifiedAt` | Instant | Certification time |

---

### API-116 — `POST /api/v1/accuracy/adjustment-cases`

| HTTP Status | `201 Created` | **DTO:** `AdjustmentCaseResponse`

| Field | Type | Description |
|-------|------|-------------|
| `caseId` | UUID | Case ID |
| `caseNumber` | String | Business case number |
| `status` | String | `OPEN` |
| `originType` | String | Origin type |
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `reasonCode` | String | Reason code |
| `openedAt` | Instant | Open time |

---

### API-117 — `GET /api/v1/accuracy/adjustment-cases/{caseId}`

| HTTP Status | `200 OK` | **DTO:** `AdjustmentCaseDetailResponse` — includes investigation, approval chain, proposed adjustment.

---

### API-118 — `POST .../investigate`

| HTTP Status | `200 OK` | **DTO:** `AdjustmentCaseResponse` with `status: "UNDER_INVESTIGATION"`.

---

### API-119 — `POST .../variances/{varianceId}/approve`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "VARIANCE_APPROVED"`

---

### API-120 — `POST .../submit`

| HTTP Status | `200 OK` | **DTO:** `AdjustmentCaseResponse` with `status: "PENDING_APPROVAL"`.

---

### API-121 — `POST .../approve`

| HTTP Status | `200 OK` | **DTO:** `AdjustmentApprovalResponse`

| Field | Type | Description |
|-------|------|-------------|
| `caseId` | UUID | Case ID |
| `status` | String | `APPROVED` |
| `adjustmentType` | String | `ADJUSTMENT` or `WRITE_OFF` |
| `approvedQuantity` | QuantityResponse | Approved qty |
| `stockAdjustedAt` | Instant | When stock mutation applied |

**Example:**
```json
{
  "caseId": "f8a9b0c1-d2e3-4567-8901-234567890ef0",
  "status": "APPROVED",
  "adjustmentType": "ADJUSTMENT",
  "approvedQuantity": { "amount": 5, "unitOfMeasure": "EA" },
  "stockAdjustedAt": "2026-07-07T14:00:00Z"
}
```

---

### API-122 — `POST .../reject`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "REJECTED"`

---

### API-123 — `GET /api/v1/accuracy/pending-approvals`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<AdjustmentCaseSummaryResponse>`

---

## M-10 — Returns Management

### API-124 — `POST /api/v1/returns/authorizations`

| HTTP Status | `201 Created` | **DTO:** `ReturnAuthorizationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `returnAuthorizationId` | UUID | RMA ID |
| `rmaNumber` | String | RMA number |
| `status` | String | `AUTHORIZED` |
| `originalOrderId` | UUID | Original order |
| `originalOrderNumber` | String | Order number |
| `validUntil` | LocalDate | Authorization expiry |
| `lines` | Array\<ReturnAuthorizationLineResponse\> | Authorized lines |
| `issuedAt` | Instant | Issue time |

**Example:**
```json
{
  "returnAuthorizationId": "a9b0c1d2-e3f4-5678-9012-345678901abc",
  "rmaNumber": "RMA-2026-0012",
  "status": "AUTHORIZED",
  "originalOrderId": "e1f2a3b4-c5d6-7890-1234-567890123def",
  "originalOrderNumber": "ORD-2026-0042",
  "validUntil": "2026-07-20",
  "lines": [
    {
      "lineId": "b0c1d2e3-f4a5-6789-0123-456789012bcd",
      "sku": "SKU-WIDGET-001",
      "authorizedQuantity": { "amount": 5, "unitOfMeasure": "EA" }
    }
  ],
  "issuedAt": "2026-07-06T19:00:00Z"
}
```

---

### API-125 — `GET /api/v1/returns/authorizations`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<ReturnAuthorizationSummaryResponse>`

---

### API-126 — `GET /api/v1/returns/authorizations/{returnAuthorizationId}`

| HTTP Status | `200 OK` | **DTO:** `ReturnAuthorizationResponse`

---

### API-127 — `POST .../cancel`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "CANCELLED"`

---

### API-128 — `POST /api/v1/returns/{returnId}/receive`

| HTTP Status | `200 OK` | **DTO:** `CustomerReturnResponse` with `status: "RECEIVED"`.

---

### API-129 — `POST /api/v1/returns/{returnId}/inspect`

| HTTP Status | `200 OK` | **DTO:** `ReturnInspectionResponse`

| Field | Type | Description |
|-------|------|-------------|
| `returnId` | UUID | Return ID |
| `status` | String | `INSPECTED` |
| `inspectionLines` | Array\<InspectionLineResponse\> | Inspection results |
| `inspectedAt` | Instant | Inspection time |

---

### API-130 — `POST /api/v1/returns/{returnId}/disposition`

| HTTP Status | `200 OK` | **DTO:** `ReturnDispositionResponse`

| Field | Type | Description |
|-------|------|-------------|
| `returnId` | UUID | Return ID |
| `status` | String | `COMPLETED` |
| `dispositionAction` | String | `RESTOCK`, `QUARANTINE`, or `WRITE_OFF` |
| `dispositionLines` | Array\<DispositionLineResultResponse\> | Per-line results |
| `dispositionedAt` | Instant | Disposition time |

**Example:**
```json
{
  "returnId": "c1d2e3f4-a5b6-7890-1234-567890123cde",
  "status": "COMPLETED",
  "dispositionAction": "RESTOCK",
  "dispositionLines": [
    {
      "returnLineId": "d2e3f4a5-b6c7-8901-2345-678901234def",
      "quantity": { "amount": 5, "unitOfMeasure": "EA" },
      "outcome": "RESTOCKED",
      "restockLocationCode": "WH-EAST-01"
    }
  ],
  "dispositionedAt": "2026-07-06T19:30:00Z"
}
```

---

### API-131 — `GET /api/v1/returns/pending-receipts`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<PendingReturnReceiptResponse>`

---

## M-11 — Commercial Campaign

### API-132 — `POST /api/v1/campaigns/allocations`

| HTTP Status | `201 Created` | **DTO:** `PromotionalAllocationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `allocationId` | UUID | Allocation ID |
| `campaignId` | String | Campaign ID |
| `campaignName` | String | Campaign name |
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `allocatedQuantity` | QuantityResponse | Ring-fenced qty |
| `status` | String | `PLANNED` or `ACTIVE` |
| `campaignStartDate` | LocalDate | Start date |
| `campaignEndDate` | LocalDate | End date |
| `readinessStatus` | String | Readiness status |

**Example:**
```json
{
  "allocationId": "e3f4a5b6-c7d8-9012-3456-789012345def",
  "campaignId": "CAMP-SUMMER-2026",
  "campaignName": "Summer Promotion 2026",
  "locationCode": "WH-EAST-01",
  "sku": "SKU-WIDGET-001",
  "allocatedQuantity": { "amount": 100, "unitOfMeasure": "EA" },
  "status": "PLANNED",
  "campaignStartDate": "2026-07-15",
  "campaignEndDate": "2026-08-15",
  "readinessStatus": "PENDING"
}
```

---

### API-133 — `GET /api/v1/campaigns/allocations`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<PromotionalAllocationSummaryResponse>`

---

### API-134 — `GET /api/v1/campaigns/allocations/{allocationId}`

| HTTP Status | `200 OK` | **DTO:** `PromotionalAllocationResponse`

---

### API-135 — `PATCH /api/v1/campaigns/allocations/{allocationId}`

| HTTP Status | `200 OK` | **DTO:** `PromotionalAllocationResponse` (amended).

---

### API-136 — `POST .../readiness`

| HTTP Status | `200 OK` | **DTO:** `CampaignReadinessResponse`

| Field | Type | Description |
|-------|------|-------------|
| `allocationId` | UUID | Allocation ID |
| `readinessStatus` | String | `READY` or `GAP_IDENTIFIED` |
| `targetQuantity` | QuantityResponse | Target qty |
| `availableQuantity` | QuantityResponse | Ring-fenced available |
| `gapQuantity` | QuantityResponse | Shortfall when gap |
| `evaluatedAt` | Instant | Evaluation time |

---

### API-137 — `POST .../release`

| HTTP Status | `200 OK` | **DTO:** `CommandResultResponse` — `status: "RELEASED"`

---

### API-138 — `POST .../override`

| HTTP Status | `200 OK` | **DTO:** `PromotionalOverrideResponse`

| Field | Type | Description |
|-------|------|-------------|
| `allocationId` | UUID | Allocation ID |
| `orderId` | UUID | Consuming order |
| `overrideQuantity` | QuantityResponse | Overridden qty |
| `authorizationReference` | String | Authorization ref |
| `authorizedAt` | Instant | Authorization time |

---

### API-139 — `GET /api/v1/campaigns/ring-fence/{locationCode}/{sku}`

| HTTP Status | `200 OK` | **DTO:** `RingFenceStatusResponse`

| Field | Type | Description |
|-------|------|-------------|
| `locationCode` | String | Location |
| `sku` | String | SKU |
| `hasActiveRingFence` | Boolean | Active ring-fence exists |
| `allocations` | Array\<ActiveAllocationSummaryResponse\> | Active allocations |

**Example:**
```json
{
  "locationCode": "WH-EAST-01",
  "sku": "SKU-WIDGET-001",
  "hasActiveRingFence": true,
  "allocations": [
    {
      "allocationId": "e3f4a5b6-c7d8-9012-3456-789012345def",
      "campaignId": "CAMP-SUMMER-2026",
      "allocatedQuantity": { "amount": 100, "unitOfMeasure": "EA" },
      "campaignEndDate": "2026-08-15"
    }
  ]
}
```

---

## M-12 — Identity & Access

### API-140 — `POST /api/v1/users`

| HTTP Status | `201 Created` | **DTO:** `UserAccountResponse`

| Field | Type | Description |
|-------|------|-------------|
| `userId` | String | User ID |
| `email` | String | Email |
| `displayName` | String | Display name |
| `status` | String | `ACTIVE` |
| `roles` | Array\<RoleAssignmentResponse\> | Role assignments |
| `audit` | AuditInfoResponse | Audit metadata |

**Example:**
```json
{
  "userId": "usr-wh-mgr-02",
  "email": "j.smith@company.example.com",
  "displayName": "Jane Smith",
  "status": "ACTIVE",
  "roles": [
    {
      "roleAssignmentId": "f4a5b6c7-d8e9-0123-4567-890123456ef0",
      "roleCode": "WAREHOUSE_MANAGER",
      "locationCodes": ["WH-EAST-01"],
      "effectiveFrom": "2026-07-06",
      "effectiveTo": null
    }
  ],
  "audit": {
    "createdAt": "2026-07-06T20:00:00Z",
    "createdBy": "usr-admin-01",
    "updatedAt": "2026-07-06T20:00:00Z",
    "updatedBy": "usr-admin-01"
  }
}
```

---

### API-141 — `GET /api/v1/users`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<UserAccountSummaryResponse>`

---

### API-142 — `GET /api/v1/users/{userId}`

| HTTP Status | `200 OK` | **DTO:** `UserAccountResponse`

---

### API-143 — `POST /api/v1/users/{userId}/roles`

| HTTP Status | `201 Created` | **DTO:** `RoleAssignmentResponse`

---

### API-144 — `DELETE /api/v1/users/{userId}/roles/{roleAssignmentId}`

| HTTP Status | `200 OK` | **DTO:** `RoleRevocationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `roleAssignmentId` | UUID | Revoked assignment |
| `userId` | String | User ID |
| `revokedAt` | Instant | Revocation time |

---

### API-145 — `POST /api/v1/users/{userId}/suspend`

| HTTP Status | `200 OK` | **DTO:** `UserAccountResponse` with `status: "SUSPENDED"`.

---

### API-146 — `POST /api/v1/users/{userId}/deactivate`

| HTTP Status | `200 OK` | **DTO:** `UserAccountResponse` with `status: "DEACTIVATED"`.

---

### API-147 — `POST /api/v1/users/sync`

| HTTP Status | `200 OK` | **DTO:** `DirectorySyncResultResponse`

| Field | Type | Description |
|-------|------|-------------|
| `syncMode` | String | Sync mode |
| `usersCreated` | Integer | Created count |
| `usersUpdated` | Integer | Updated count |
| `usersDeactivated` | Integer | Deactivated count |
| `errors` | Array\<SyncErrorResponse\> | Sync errors |
| `syncedAt` | Instant | Sync completion time |

---

### API-148 — `POST /api/v1/authorization/actions/evaluate`

| HTTP Status | `200 OK` | **DTO:** `AuthorizationEvaluationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `authorized` | Boolean | Action permitted |
| `userId` | String | Evaluated user |
| `action` | String | Action code |
| `denialReason` | String | Reason when denied |

**Example:**
```json
{
  "authorized": true,
  "userId": "usr-wh-mgr-02",
  "action": "ADJUSTMENT_APPROVE",
  "denialReason": null
}
```

---

### API-149 — `POST /api/v1/authorization/location-scope/validate`

| HTTP Status | `200 OK` | **DTO:** `LocationScopeValidationResponse`

| Field | Type | Description |
|-------|------|-------------|
| `authorized` | Boolean | Location access granted |
| `userId` | String | User ID |
| `locationCode` | String | Location |
| `scopedLocations` | Array\<String\> | User's authorized locations |

---

## M-13 — Inventory Intelligence

### API-150 — `GET /api/v1/intelligence/dashboard`

| HTTP Status | `200 OK` | **DTO:** `InventoryDashboardResponse`

| Field | Type | Description |
|-------|------|-------------|
| `scope` | String | `LOCATION` or `NETWORK` |
| `locationCode` | String | Location when scoped |
| `asOfTimestamp` | Instant | Data freshness |
| `summary` | DashboardSummaryResponse | KPI summary tiles |
| `lowStockCount` | Integer | Low-stock SKUs |
| `outOfStockCount` | Integer | Out-of-stock SKUs |
| `pendingApprovals` | Integer | Pending approvals |
| `openAlerts` | Integer | Open alerts |

**Example:**
```json
{
  "scope": "LOCATION",
  "locationCode": "WH-EAST-01",
  "asOfTimestamp": "2026-07-06T20:30:00Z",
  "summary": {
    "totalSkus": 1250,
    "totalOnHandValue": { "amount": 2500000.00, "currencyCode": "USD" },
    "averageFillRate": 0.94
  },
  "lowStockCount": 23,
  "outOfStockCount": 5,
  "pendingApprovals": 7,
  "openAlerts": 12
}
```

---

### API-151 — `GET /api/v1/intelligence/stock-status/summary`

| HTTP Status | `200 OK` | **DTO:** `StockStatusSummaryResponse`

| Field | Type | Description |
|-------|------|-------------|
| `inStockCount` | Integer | In-stock positions |
| `lowStockCount` | Integer | Low-stock positions |
| `outOfStockCount` | Integer | Out-of-stock positions |
| `overstockCount` | Integer | Overstock positions |
| `totalOnHand` | QuantityResponse | Aggregated on-hand |
| `totalAtp` | QuantityResponse | Aggregated ATP |

---

### API-152 — `GET /api/v1/intelligence/stock-status/board`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<StockStatusBoardRowResponse>`

---

### API-153 — `GET /api/v1/intelligence/availability/inquiries`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<AvailabilityInquiryLogEntryResponse>`

---

### API-154 — `GET /api/v1/intelligence/quarantine-register`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<QuarantineRegisterEntryResponse>`

---

### API-155 — `GET /api/v1/intelligence/movements`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<MovementHistoryEntryResponse>`

| Field | Type | Description |
|-------|------|-------------|
| `movementId` | UUID | Movement ID |
| `sku` | String | SKU |
| `locationCode` | String | Location |
| `movementType` | String | Movement type |
| `quantity` | QuantityResponse | Quantity moved |
| `userId` | String | Acting user |
| `occurredAt` | Instant | Movement timestamp |
| `reference` | String | Source document reference |

**Example:**
```json
{
  "data": [
    {
      "movementId": "a5b6c7d8-e9f0-1234-5678-901234567abc",
      "sku": "SKU-WIDGET-001",
      "locationCode": "WH-EAST-01",
      "movementType": "SHIPMENT",
      "quantity": { "amount": 50, "unitOfMeasure": "EA" },
      "userId": "usr-pick-01",
      "occurredAt": "2026-07-06T18:00:00Z",
      "reference": "ORD-2026-0042"
    }
  ],
  "page": 1,
  "pageSize": 20,
  "totalElements": 1,
  "totalPages": 1
}
```

---

### API-156 — `GET /api/v1/intelligence/audit-trail`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<AuditTrailEntryResponse>`

| Field | Type | Description |
|-------|------|-------------|
| `auditId` | UUID | Audit entry ID |
| `entityType` | String | Entity type |
| `entityId` | String | Entity ID |
| `action` | String | Action performed |
| `userId` | String | Acting user |
| `occurredAt` | Instant | Timestamp |
| `beforeState` | Object | Prior state snapshot |
| `afterState` | Object | New state snapshot |

---

### API-157 — `GET /api/v1/intelligence/audit-trail/export`

| HTTP Status | `200 OK` | **DTO:** Binary file stream **or** `ExportJobResponse` for async export.

| Field | Type | Description |
|-------|------|-------------|
| `exportId` | UUID | Export job ID |
| `status` | String | `COMPLETED` |
| `format` | String | `CSV`, `JSON`, or `PDF` |
| `downloadUrl` | String | Signed download URL |
| `recordCount` | Integer | Records exported |
| `expiresAt` | Instant | URL expiry |

---

### API-158 — `GET /api/v1/intelligence/alerts`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<OperationalAlertResponse>`

| Field | Type | Description |
|-------|------|-------------|
| `alertId` | UUID | Alert ID |
| `alertType` | String | Alert type |
| `severity` | String | Severity |
| `sku` | String | SKU |
| `locationCode` | String | Location |
| `message` | String | Alert message |
| `acknowledged` | Boolean | Acknowledgment flag |
| `raisedAt` | Instant | Raised time |

---

### API-159 — `POST /api/v1/intelligence/alerts/{alertId}/acknowledge`

| HTTP Status | `200 OK` | **DTO:** `OperationalAlertResponse` with `acknowledged: true`.

---

### API-160 — `GET /api/v1/intelligence/replenishment/recommendations`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<ReplenishmentRecommendationResponse>`

---

### API-161 — `GET /api/v1/intelligence/procurement/open-pos`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<OpenPurchaseOrderBoardRowResponse>`

---

### API-162 — `GET /api/v1/intelligence/procurement/inbound-calendar`

| HTTP Status | `200 OK` | **DTO:** `InboundSupplyCalendarResponse`

| Field | Type | Description |
|-------|------|-------------|
| `startDate` | LocalDate | Calendar start |
| `endDate` | LocalDate | Calendar end |
| `entries` | Array\<InboundCalendarEntryResponse\> | Calendar entries |

**`InboundCalendarEntryResponse`:** `date`, `purchaseOrderId`, `poNumber`, `supplierCode`, `sku`, `expectedQuantity`, `receivingLocationCode`

---

### API-163 — `GET /api/v1/intelligence/procurement/inbound-delays`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<InboundDelayLogEntryResponse>`

---

### API-164 — `GET /api/v1/intelligence/fulfillment/backorders`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<BackorderPipelineEntryResponse>`

---

### API-165 — `GET /api/v1/intelligence/fulfillment/exceptions`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<FulfillmentExceptionLogEntryResponse>`

---

### API-166 — `GET /api/v1/intelligence/network/imbalance`

| HTTP Status | `200 OK` | **DTO:** `NetworkImbalanceAnalysisResponse`

| Field | Type | Description |
|-------|------|-------------|
| `analyzedAt` | Instant | Analysis timestamp |
| `imbalances` | Array\<NetworkImbalanceEntryResponse\> | Imbalance entries |
| `recommendations` | Array\<TransferRecommendationResponse\> | Transfer recommendations |

**Example:**
```json
{
  "analyzedAt": "2026-07-06T21:00:00Z",
  "imbalances": [
    {
      "sku": "SKU-WIDGET-001",
      "shortageLocationCode": "WH-EAST-01",
      "shortageQuantity": { "amount": 50, "unitOfMeasure": "EA" },
      "excessLocationCode": "WH-WEST-01",
      "excessQuantity": { "amount": 200, "unitOfMeasure": "EA" }
    }
  ],
  "recommendations": [
    {
      "sku": "SKU-WIDGET-001",
      "sourceLocationCode": "WH-WEST-01",
      "destinationLocationCode": "WH-EAST-01",
      "recommendedQuantity": { "amount": 100, "unitOfMeasure": "EA" }
    }
  ]
}
```

---

### API-167 — `GET /api/v1/intelligence/accuracy/shrinkage`

| HTTP Status | `200 OK` | **DTO:** `ShrinkageAnalysisResponse`

| Field | Type | Description |
|-------|------|-------------|
| `periodStart` | LocalDate | Period start |
| `periodEnd` | LocalDate | Period end |
| `totalShrinkageValue` | MonetaryAmountResponse | Total shrinkage value |
| `shrinkageRate` | BigDecimal | Shrinkage rate % |
| `breakdown` | Array\<ShrinkageBreakdownRowResponse\> | Grouped breakdown |

---

### API-168 — `GET /api/v1/intelligence/accuracy/count-performance`

| HTTP Status | `200 OK` | **DTO:** `CountPerformanceMetricsResponse`

| Field | Type | Description |
|-------|------|-------------|
| `periodStart` | LocalDate | Period start |
| `periodEnd` | LocalDate | Period end |
| `accuracyRate` | BigDecimal | Inventory accuracy % |
| `cycleCountsCompleted` | Integer | Cycle counts done |
| `physicalCountsCompleted` | Integer | Physical counts done |
| `varianceCount` | Integer | Variances detected |

---

### API-169 — `GET /api/v1/intelligence/campaigns/readiness`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<CampaignReadinessStatusResponse>`

---

### API-170 — `GET /api/v1/intelligence/kpis`

| HTTP Status | `200 OK` | **DTO:** `InventoryKpiReportResponse`

| Field | Type | Description |
|-------|------|-------------|
| `periodStart` | LocalDate | Period start |
| `periodEnd` | LocalDate | Period end |
| `kpis` | Array\<KpiMetricResponse\> | KPI metrics |

**`KpiMetricResponse`:** `kpiCode`, `name`, `value`, `target`, `unit`, `trend`, `status` (`ON_TARGET`, `BELOW_TARGET`, `ABOVE_TARGET`)

**Example:**
```json
{
  "periodStart": "2026-06-01",
  "periodEnd": "2026-06-30",
  "kpis": [
    {
      "kpiCode": "FILL_RATE",
      "name": "Order Fill Rate",
      "value": 0.94,
      "target": 0.95,
      "unit": "PERCENT",
      "trend": "UP",
      "status": "BELOW_TARGET"
    },
    {
      "kpiCode": "INVENTORY_ACCURACY",
      "name": "Inventory Record Accuracy",
      "value": 0.97,
      "target": 0.95,
      "unit": "PERCENT",
      "trend": "STABLE",
      "status": "ON_TARGET"
    }
  ]
}
```

---

### API-171 — `GET /api/v1/intelligence/valuation/snapshots`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<ValuationSnapshotResponse>`

| Field | Type | Description |
|-------|------|-------------|
| `snapshotId` | UUID | Snapshot ID |
| `periodEndDate` | LocalDate | Period end |
| `totalValue` | MonetaryAmountResponse | Total inventory value |
| `locationCode` | String | Location scope |
| `lineCount` | Integer | Valuation lines |
| `preparedAt` | Instant | Preparation time |

---

### API-172 — `GET /api/v1/intelligence/valuation/reconciliation`

| HTTP Status | `200 OK` | **DTO:** `ValuationReconciliationReportResponse`

| Field | Type | Description |
|-------|------|-------------|
| `periodEndDate` | LocalDate | Period end |
| `operationalValue` | MonetaryAmountResponse | IMS valuation |
| `generalLedgerValue` | MonetaryAmountResponse | GL valuation |
| `variance` | MonetaryAmountResponse | Variance amount |
| `variancePercent` | BigDecimal | Variance % |
| `withinTolerance` | Boolean | Within tolerance |
| `lineVariances` | Array\<ValuationLineVarianceResponse\> | Line-level variances |

**Example:**
```json
{
  "periodEndDate": "2026-06-30",
  "operationalValue": { "amount": 2500000.00, "currencyCode": "USD" },
  "generalLedgerValue": { "amount": 2495000.00, "currencyCode": "USD" },
  "variance": { "amount": 5000.00, "currencyCode": "USD" },
  "variancePercent": 0.20,
  "withinTolerance": true,
  "lineVariances": []
}
```

---

## Platform & Integration

### API-173 — `GET /api/v1/auth/session`

| HTTP Status | `200 OK` | **DTO:** `SessionResponse`

| Field | Type | Description |
|-------|------|-------------|
| `userId` | String | Authenticated user |
| `email` | String | Email |
| `displayName` | String | Display name |
| `roles` | Array\<String\> | Role codes |
| `locationScope` | Array\<String\> | Authorized locations |
| `permissions` | Array\<String\> | Resolved permissions (when requested) |
| `sessionExpiresAt` | Instant | Session expiry |

**Example:**
```json
{
  "userId": "usr-wh-mgr-02",
  "email": "j.smith@company.example.com",
  "displayName": "Jane Smith",
  "roles": ["WAREHOUSE_MANAGER"],
  "locationScope": ["WH-EAST-01"],
  "permissions": ["STOCK_VIEW", "ADJUSTMENT_APPROVE"],
  "sessionExpiresAt": "2026-07-06T22:00:00Z"
}
```

---

### API-174 — `POST /api/v1/auth/logout`

| HTTP Status | `200 OK` | **DTO:** `LogoutResponse`

| Field | Type | Description |
|-------|------|-------------|
| `loggedOut` | Boolean | `true` |
| `loggedOutAt` | Instant | Logout timestamp |

**Example:**
```json
{
  "loggedOut": true,
  "loggedOutAt": "2026-07-06T21:45:00Z"
}
```

---

### API-175 — `GET /api/v1/health`

| HTTP Status | `200 OK` | **DTO:** `HealthCheckResponse`

| Field | Type | Description |
|-------|------|-------------|
| `status` | String | `UP` |
| `timestamp` | Instant | Check timestamp |
| `version` | String | Application version |
| `components` | Array\<HealthComponentResponse\> | Component health |

**Example:**
```json
{
  "status": "UP",
  "timestamp": "2026-07-06T21:50:00Z",
  "version": "1.0.0",
  "components": [
    { "name": "database", "status": "UP" },
    { "name": "eventBus", "status": "UP" }
  ]
}
```

---

### API-176 — `POST /api/v1/integrations/sales/orders`

| HTTP Status | `201 Created` | **DTO:** `SalesOrderImportResponse`

| Field | Type | Description |
|-------|------|-------------|
| `orderId` | UUID | Created IMS order ID |
| `orderNumber` | String | IMS order number |
| `externalOrderId` | String | CRM order ID |
| `status` | String | `DRAFT` |
| `correlationId` | String | Integration correlation ID |
| `importedAt` | Instant | Import timestamp |

**Example:**
```json
{
  "orderId": "f5a6b7c8-d9e0-1234-5678-901234567abc",
  "orderNumber": "ORD-2026-0043",
  "externalOrderId": "CRM-ORD-998877",
  "status": "DRAFT",
  "correlationId": "corr-20260706-001",
  "importedAt": "2026-07-06T21:55:00Z"
}
```

---

### API-177 — `GET /api/v1/integrations/sales/fulfillment-status`

| HTTP Status | `200 OK` | **DTO:** `PagedResponse<FulfillmentStatusFeedEntryResponse>`

| Field | Type | Description |
|-------|------|-------------|
| `externalOrderId` | String | CRM order ID |
| `orderNumber` | String | IMS order number |
| `status` | String | Fulfillment status |
| `shipmentTrackingNumber` | String | Tracking number |
| `shippedAt` | Instant | Ship time |
| `updatedAt` | Instant | Last update |

---

### API-178 — `POST /api/v1/integrations/marketing/campaign-plans`

| HTTP Status | `201 Created` | **DTO:** `CampaignPlanImportResponse`

| Field | Type | Description |
|-------|------|-------------|
| `campaignId` | String | Campaign ID |
| `allocationsCreated` | Integer | Allocations created |
| `allocationIds` | Array\<UUID\> | Created allocation IDs |
| `correlationId` | String | Correlation ID |
| `importedAt` | Instant | Import timestamp |

**Example:**
```json
{
  "campaignId": "CAMP-FALL-2026",
  "allocationsCreated": 15,
  "allocationIds": [
    "a6b7c8d9-e0f1-2345-6789-012345678abc",
    "b7c8d9e0-f1a2-3456-7890-123456789bcd"
  ],
  "correlationId": "corr-mkt-20260706-001",
  "importedAt": "2026-07-06T22:00:00Z"
}
```

---

## Response DTO Index

| Pattern | APIs | HTTP Status |
|---------|------|-------------|
| `ProductDetailResponse` | API-001, 003, 004 | 201 / 200 |
| `PagedResponse<T>` | API-002, 008, 012, 023, 033, 050, 060, 067, 082, 099, 109, 123, 125, 131, 133, 141, 152–165, 169, 171, 177 | 200 |
| `CommandResultResponse` | API-056, 057, 063, 086, 101, 102, 105, 119, 122, 127, 137 | 200 |
| `CustomerOrderResponse` | API-081, 083, 085 | 201 / 200 |
| `StockTransferResponse` | API-098, 100–104 | 201 / 200 |
| `GoodsReceiptResponse` | API-066–069, 075 | 201 / 200 |
| `PurchaseOrderResponse` | API-058, 059, 061, 062 | 201 / 200 |

**Total APIs documented:** 178

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Backend Architect | | | |
| Solution Architect | | | |
| Product Owner | | | |

---

*End of Response DTO Specification*

*Document ID: SRS-API-003 | Version 1.0 | July 6, 2026*
