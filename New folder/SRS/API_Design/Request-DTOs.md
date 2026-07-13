# Request DTO Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-002 |
| **Document Title** | Request DTO Specification — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Backend Architect |
| **Source Documents** | SRS-API-001 (REST API Catalog), SRS-VR-001 (Validation Rules), SRS-DM-002 (Value Objects), SRS-DB (Database Design) |
| **Date** | July 6, 2026 |
| **Scope** | Request DTOs only — path parameters, query parameters, and request bodies. Response DTOs are out of scope. |

### Purpose

This document defines the **request data transfer object** for every REST API in SRS-API-001. Each field specifies name, data type, required/optional status, validation rules, and business description. Validation rule references use **VR-xxx** from SRS-VR-001 and **BR-xxx** from the Business Rule Catalog where applicable.

### Request Composition Conventions

| Layer | Convention |
|-------|------------|
| **Path parameters** | Included in every applicable API's Request DTO |
| **Query parameters** | Used for `GET` list, search, and filter operations |
| **Request body** | Used for `POST`, `PUT`, `PATCH` command operations |
| **Headers** | `Authorization: Bearer <token>` required on all APIs except API-175; not repeated per DTO |
| **Idempotency** | Optional `Idempotency-Key` header (UUID) on financial and reservation commands — documented per API where recommended |

### Shared Primitive Types

| Type | Java/Spring Mapping | Validation |
|------|---------------------|------------|
| `ProductSku` | `String` | Required when present; max 50 chars; pattern `^[A-Z0-9][A-Z0-9_-]*$` (VR-001, VR-007) |
| `LocationCode` | `String` | Required when present; max 30 chars; pattern `^[A-Z0-9][A-Z0-9_-]*$` (VR-011) |
| `SupplierCode` | `String` | Required when present; max 30 chars; pattern `^[A-Z0-9][A-Z0-9_-]*$` |
| `ReasonCode` | `String` | Required when present; max 20 chars; must reference active reason code (VR-026, VR-027) |
| `Quantity` | `BigDecimal` | Scale ≤ 4; min 0 (VR-018, VR-023, VR-070) |
| `PositiveQuantity` | `BigDecimal` | Scale ≤ 4; min exclusive 0 (VR-032, VR-035, VR-066) |
| `CurrencyCode` | `String` | ISO 4217; exactly 3 uppercase letters |
| `LocalDate` | `LocalDate` | ISO-8601 `YYYY-MM-DD` |
| `Instant` | `Instant` | ISO-8601 UTC datetime |
| `Uuid` | `UUID` | RFC 4122 format |
| `AbcClass` | `String` | Enum: `A`, `B`, `C` (VR-021) |
| `LifecycleStatus` | `String` | Enum: `ACTIVE`, `INACTIVE`, `DISCONTINUED` (VR-004–VR-006) |
| `PageNumber` | `Integer` | Min 1; default 1 |
| `PageSize` | `Integer` | Min 1; max 100; default 20 |

### Shared Nested DTOs

Reused across multiple API request bodies.

#### `PaginationQuery` (query)

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `page` | Integer | Optional | Min 1; default 1 | Page number for paginated results |
| `pageSize` | Integer | Optional | Min 1; max 100; default 20 | Number of records per page |
| `sortBy` | String | Optional | Max 50 chars; allowed values per resource | Sort field name |
| `sortDirection` | String | Optional | Enum: `ASC`, `DESC`; default `ASC` | Sort direction |

#### `DateRangeQuery` (query)

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `startDate` | LocalDate | Required | Valid date; on or before `endDate` (VR-062, VR-153) | Period start (inclusive) |
| `endDate` | LocalDate | Required | Valid date; on or after `startDate` | Period end (inclusive) |

#### `QuantityDto` (body)

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `amount` | BigDecimal | Required | Scale ≤ 4; min 0 | Numeric quantity amount |
| `unitOfMeasure` | String | Required | Max 10 chars; must match product UoM or approved alternate | Unit of measure code |

#### `PositiveQuantityDto` (body)

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `amount` | BigDecimal | Required | Scale ≤ 4; min exclusive 0 (VR-032) | Numeric quantity greater than zero |
| `unitOfMeasure` | String | Required | Max 10 chars | Unit of measure code |

#### `LotIdentityDto` (body)

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lotNumber` | String | Required | Max 50 chars; non-blank (BR-017) | Lot or batch identifier |
| `expirationDate` | LocalDate | Optional | Future or present when product is shelf-life managed | Lot expiration date for FEFO |

#### `ShelfLifeProfileDto` (body)

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `expirationDate` | LocalDate | Required | Valid date; remaining life must meet MRSL (BR-016, VR-035) | Product expiration date at receipt |
| `manufactureDate` | LocalDate | Optional | On or before `expirationDate` | Manufacture date when available |
| `remainingShelfLifeDays` | Integer | Optional | Min 0 | Remaining shelf life in days at capture |

#### `MonetaryAmountDto` (body)

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `amount` | BigDecimal | Required | Scale 2; min 0 | Monetary value |
| `currencyCode` | CurrencyCode | Required | ISO 4217 3-letter code | Currency of the amount |

#### `RoleAssignmentDto` (body)

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `roleCode` | String | Required | Max 50 chars; must be valid system role | Role to assign |
| `locationCodes` | Array\<LocationCode\> | Optional | Each valid `LocationCode`; empty means network-wide where role permits | Location scope for the role |
| `effectiveFrom` | LocalDate | Optional | Valid date; default today | Role assignment effective start |
| `effectiveTo` | LocalDate | Optional | On or after `effectiveFrom` when provided | Role assignment effective end |

---

## M-01 — Product Catalog

### API-001 — `POST /api/v1/products`

**DTO:** `CreateProductRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Unique across catalog (VR-002); duplicate check on similar name/barcode (VR-009) | Stock keeping unit identifier |
| `name` | String | Required | Max 200 chars; non-blank (VR-001) | Product display name |
| `description` | String | Optional | Max 2000 chars | Product description |
| `unitOfMeasure` | String | Required | Max 10 chars; non-blank (VR-001) | Primary counting and ordering unit |
| `categoryCode` | String | Optional | Max 30 chars; must exist when provided | Product category reference |
| `barcode` | String | Optional | Max 50 chars | Primary barcode for operational lookup |
| `isTraceable` | Boolean | Optional | Default `false`; when `true`, `rotationPolicy` required | Whether lot/batch capture is mandatory |
| `rotationPolicy` | String | Conditional | Required if `isTraceable=true`; enum: `FIFO`, `FEFO` | Stock rotation discipline |
| `shelfLifeManaged` | Boolean | Optional | Default `false` | Whether MRSL rules apply at receipt |
| `mrslThresholdDays` | Integer | Conditional | Required if `shelfLifeManaged=true`; min 1 | Minimum remaining shelf life days at receipt |

---

### API-002 — `GET /api/v1/products`

**DTO:** `SearchProductsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `name` | String | Optional | Max 200 chars; partial match | Filter by product name |
| `sku` | ProductSku | Optional | Exact or prefix match | Filter by SKU |
| `categoryCode` | String | Optional | Max 30 chars | Filter by category |
| `lifecycleStatus` | LifecycleStatus | Optional | Valid enum value | Filter by lifecycle status |
| `abcClass` | AbcClass | Optional | `A`, `B`, or `C` (VR-021) | Filter by ABC classification |
| `barcode` | String | Optional | Max 50 chars | Lookup by barcode (VR-007) |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |
| `sortBy` | String | Optional | Enum: `sku`, `name`, `categoryCode`, `lifecycleStatus` | Sort field |
| `sortDirection` | String | Optional | `ASC` or `DESC` | Sort direction |

---

### API-003 — `GET /api/v1/products/{sku}`

**DTO:** `GetProductBySkuRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Path param; must exist (VR-007) | Product SKU to retrieve |

---

### API-004 — `PATCH /api/v1/products/{sku}`

**DTO:** `UpdateProductAttributesRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Path param; must exist | Product SKU to update |
| `name` | String | Optional | Max 200 chars; non-blank when provided | Updated product name |
| `description` | String | Optional | Max 2000 chars | Updated description |
| `unitOfMeasure` | String | Optional | Max 10 chars; non-blank when provided | Updated primary UoM |
| `categoryCode` | String | Optional | Max 30 chars | Updated category |
| `barcode` | String | Optional | Max 50 chars | Updated barcode |
| `isTraceable` | Boolean | Optional | When set `true`, `rotationPolicy` required | Updated traceability flag |
| `rotationPolicy` | String | Conditional | Enum: `FIFO`, `FEFO` | Updated rotation policy |
| `shelfLifeManaged` | Boolean | Optional | — | Updated shelf-life management flag |
| `mrslThresholdDays` | Integer | Conditional | Min 1 when `shelfLifeManaged=true` | Updated MRSL threshold |

*At least one body field must be present.*

---

### API-005 — `POST /api/v1/products/{sku}/lifecycle-status`

**DTO:** `ChangeProductLifecycleStatusRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Path param; must exist | Product SKU |
| `newStatus` | LifecycleStatus | Required | Valid transition; `DISCONTINUED` blocks replenishment (VR-004, VR-005) | Target lifecycle status |
| `reason` | String | Optional | Max 500 chars | Business reason for status change |
| `effectiveDate` | LocalDate | Optional | Default today | Date status change takes effect |

---

### API-006 — `PUT /api/v1/products/{sku}/abc-classification`

**DTO:** `AssignAbcClassificationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Path param; product must exist (VR-022) | Product SKU |
| `abcClass` | AbcClass | Required | `A`, `B`, or `C` (VR-021) | ABC priority class |
| `classificationBasis` | String | Optional | Max 100 chars; enum: `REVENUE`, `VELOCITY`, `CRITICALITY` | Basis used for classification |
| `effectiveDate` | LocalDate | Optional | Default today | Classification effective date |

---

### API-007 — `GET /api/v1/products/{sku}/eligibility`

**DTO:** `ValidateProductEligibilityQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Path param | Product SKU |
| `transactionType` | String | Required | Enum: `PROCUREMENT`, `RESERVATION`, `FULFILLMENT`, `TRANSFER` | Transaction context to evaluate |
| `locationCode` | LocationCode | Optional | Required for location-scoped transactions; user must have scope (VR-008) | Location context |

---

### API-008 — `GET /api/v1/products/categories/{categoryCode}/products`

**DTO:** `ListProductsByCategoryQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `categoryCode` | String | Required | Path param; max 30 chars | Category code |
| `lifecycleStatus` | LifecycleStatus | Optional | Valid enum | Filter by status within category |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-009 — `POST /api/v1/products/duplicate-resolutions`

**DTO:** `ResolveDuplicateProductConflictRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `resolutionAction` | String | Required | Enum: `MERGE`, `REJECT_NEW`, `KEEP_BOTH` | Resolution decision |
| `sourceSku` | ProductSku | Required | Must exist | SKU proposed as duplicate or merge source |
| `targetSku` | ProductSku | Conditional | Required if `resolutionAction=MERGE`; must exist | Canonical SKU to merge into |
| `mergeAuthorizationReference` | String | Conditional | Required when both SKUs have on-hand stock (VR-010) | Inventory Controller approval reference |
| `notes` | String | Optional | Max 1000 chars | Resolution notes |

---

### API-010 — `POST /api/v1/products/import`

**DTO:** `BulkProductImportRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `importMode` | String | Required | Enum: `VALIDATE_ONLY`, `UPSERT`, `CREATE_ONLY` | Import execution mode |
| `sourceReference` | String | Optional | Max 100 chars | External file or batch reference |
| `products` | Array\<BulkProductLineDto\> | Required | Min 1 item; max 5000 items per request | Product records to import |

**`BulkProductLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Unique within batch; catalog rules (VR-001, VR-002) | Product SKU |
| `name` | String | Required | Max 200 chars | Product name |
| `unitOfMeasure` | String | Required | Max 10 chars | Primary UoM |
| `categoryCode` | String | Optional | Max 30 chars | Category code |
| `barcode` | String | Optional | Max 50 chars | Barcode |
| `lifecycleStatus` | LifecycleStatus | Optional | Default `ACTIVE` | Initial lifecycle status |
| `abcClass` | AbcClass | Optional | `A`, `B`, or `C` | ABC classification |

---

## M-02 — Warehouse Network

### API-011 — `POST /api/v1/locations`

**DTO:** `CreateInventoryLocationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Unique; max 30 chars (VR-011) | Location identifier |
| `name` | String | Required | Max 200 chars; non-blank (VR-011) | Location display name |
| `locationType` | String | Required | Enum: `WAREHOUSE`, `STORE`, `DISTRIBUTION_CENTER`, `TRANSIT` (VR-011) | Location type |
| `operationalStatus` | String | Required | Enum: `PLANNED`, `ACTIVE`, `CLOSING`, `INACTIVE` | Initial operational status |
| `parentLocationCode` | LocationCode | Optional | Must not create circular hierarchy (VR-014, VR-015) | Parent location in hierarchy |
| `addressLine1` | String | Optional | Max 200 chars | Street address line 1 |
| `addressLine2` | String | Optional | Max 200 chars | Street address line 2 |
| `city` | String | Optional | Max 100 chars | City |
| `stateProvince` | String | Optional | Max 100 chars | State or province |
| `postalCode` | String | Optional | Max 20 chars | Postal or ZIP code |
| `countryCode` | String | Optional | ISO 3166-1 alpha-2 | Country code |
| `plannedGoLiveDate` | LocalDate | Optional | Valid date | Planned activation date |

---

### API-012 — `GET /api/v1/locations`

**DTO:** `ListActiveLocationsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `operationalStatus` | String | Optional | Enum: `PLANNED`, `ACTIVE`, `CLOSING`, `INACTIVE`; default `ACTIVE` | Filter by status |
| `locationType` | String | Optional | Valid location type enum | Filter by type |
| `parentLocationCode` | LocationCode | Optional | Valid location code | Filter by parent |
| `name` | String | Optional | Max 200 chars; partial match | Filter by name |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-013 — `GET /api/v1/locations/{locationCode}`

**DTO:** `GetLocationByCodeRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; must exist; user location scope (VR-053) | Location code |

---

### API-014 — `PATCH /api/v1/locations/{locationCode}/hierarchy`

**DTO:** `UpdateLocationHierarchyRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location to update |
| `parentLocationCode` | LocationCode | Optional | No self/ancestor assignment (VR-014); single parent (VR-015) | New parent location |
| `zoneCode` | String | Optional | Max 30 chars | Zone within location layout |
| `layoutNotes` | String | Optional | Max 500 chars | Layout change notes |

*At least one body field must be present.*

---

### API-015 — `POST /api/v1/locations/{locationCode}/storage-positions`

**DTO:** `ConfigureStoragePositionRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; location must be active | Parent location |
| `positionCode` | String | Required | Max 30 chars; unique within location | Storage position identifier |
| `zone` | String | Optional | Max 30 chars | Zone code |
| `aisle` | String | Optional | Max 20 chars | Aisle identifier |
| `bin` | String | Optional | Max 20 chars | Bin identifier |
| `positionType` | String | Optional | Enum: `BULK`, `PICK_FACE`, `STAGING`, `QUARANTINE`, `BONDED` | Position purpose |
| `isActive` | Boolean | Optional | Default `true` | Whether position accepts put-away |

---

### API-016 — `GET /api/v1/locations/{locationCode}/storage-positions`

**DTO:** `GetStoragePositionsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `positionType` | String | Optional | Valid position type enum | Filter by position type |
| `zone` | String | Optional | Max 30 chars | Filter by zone |
| `isActive` | Boolean | Optional | Default `true` | Filter active positions only |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-017 — `POST /api/v1/locations/{locationCode}/activate`

**DTO:** `ActivateInventoryLocationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; opening balances approved when policy applies (VR-013, VR-025) | Location to activate |
| `openingBalanceApprovalReference` | String | Conditional | Required when go-live policy mandates approved opening balance | Approval reference for opening balances |
| `activationDate` | LocalDate | Optional | Default today | Effective activation date |
| `notes` | String | Optional | Max 500 chars | Activation notes |

---

### API-018 — `POST /api/v1/locations/{locationCode}/deactivate`

**DTO:** `DeactivateInventoryLocationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location to deactivate |
| `reason` | String | Required | Max 500 chars; non-blank | Reason for deactivation |
| `effectiveDate` | LocalDate | Optional | Default today | Deactivation effective date |

---

### API-019 — `POST /api/v1/locations/{locationCode}/close`

**DTO:** `CloseInventoryLocationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; no on-hand stock unless disposition plan (VR-016) | Location to close |
| `dispositionPlanReference` | String | Conditional | Required when on-hand stock remains | Documented stock disposition plan reference |
| `closureWaiverReference` | String | Conditional | Authorized waiver when closing with remaining stock | Executive waiver reference |
| `closureDate` | LocalDate | Optional | Default today | Final closure date |
| `notes` | String | Optional | Max 1000 chars | Closure notes |

---

### API-020 — `GET /api/v1/locations/{locationCode}/freeze-status`

**DTO:** `GetLocationFreezeStatusRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; user location scope | Location code |

---

### API-021 — `GET /api/v1/locations/{locationCode}/operational-status`

**DTO:** `GetLocationOperationalStatusRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |

---

## M-03 — Inventory Governance

### API-022 — `POST /api/v1/governance/reason-codes`

**DTO:** `CreateReasonCodeRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `code` | ReasonCode | Required | Unique; max 20 chars; uppercase alphanumeric and underscore | Reason code identifier |
| `description` | String | Required | Max 200 chars; non-blank | Human-readable description |
| `transactionTypes` | Array\<String\> | Required | Min 1; values from: `ADJUSTMENT`, `WRITE_OFF`, `RECEIPT_DISCREPANCY`, `RETURN`, `TRANSFER_EXCEPTION`, `FULFILLMENT_EXCEPTION` | Applicable transaction types |
| `isActive` | Boolean | Optional | Default `true` | Initial active status |

---

### API-023 — `GET /api/v1/governance/reason-codes`

**DTO:** `GetActiveReasonCodesQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `transactionType` | String | Optional | Valid transaction type enum | Filter codes applicable to transaction type |
| `isActive` | Boolean | Optional | Default `true` | Include only active codes |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-024 — `POST /api/v1/governance/reason-codes/{code}/retire`

**DTO:** `RetireReasonCodeRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `code` | ReasonCode | Required | Path param; must exist and be active | Reason code to retire |
| `retirementReason` | String | Optional | Max 500 chars | Reason for retiring the code |
| `effectiveDate` | LocalDate | Optional | Default today | Date code becomes inactive for new transactions |

---

### API-025 — `GET /api/v1/governance/reason-codes/{code}/validate`

**DTO:** `ValidateReasonCodeQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `code` | ReasonCode | Required | Path param | Reason code to validate |
| `transactionType` | String | Required | Valid transaction type enum (VR-026) | Transaction context |

---

### API-026 — `POST /api/v1/governance/policies`

**DTO:** `PublishGovernancePolicyRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `policyName` | String | Required | Max 100 chars; non-blank | Policy version name |
| `effectiveFrom` | Instant | Required | Must not overlap existing effective version (VR-028) | Policy effective start timestamp |
| `effectiveTo` | Instant | Optional | After `effectiveFrom` | Policy effective end; null means open-ended |
| `description` | String | Optional | Max 1000 chars | Policy description |
| `parameters` | Array\<PolicyParameterDto\> | Required | Min 1 parameter | Policy parameter definitions |

**`PolicyParameterDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `parameterKey` | String | Required | Max 50 chars | Parameter identifier |
| `parameterValue` | String | Required | Max 500 chars | Parameter value |
| `parameterType` | String | Required | Enum: `QUANTITY`, `MONETARY`, `PERCENTAGE`, `BOOLEAN`, `DURATION` | Value type |

---

### API-027 — `PATCH /api/v1/governance/policies/{policyId}/approval-thresholds`

**DTO:** `UpdateApprovalThresholdRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `policyId` | Uuid | Required | Path param; policy must exist | Governance policy identifier |
| `quantityThreshold` | BigDecimal | Optional | Min 0 (VR-082) | Quantity above which independent approval required |
| `monetaryThreshold` | MonetaryAmountDto | Optional | Amount min 0 | Financial value threshold for approval |
| `transactionType` | String | Required | Enum: `ADJUSTMENT`, `WRITE_OFF`, `TRANSFER`, `REQUISITION` | Transaction type threshold applies to |
| `effectiveFrom` | LocalDate | Required | Valid date (VR-020) | Threshold effective date |

---

### API-028 — `PATCH /api/v1/governance/policies/{policyId}/receipt-tolerances`

**DTO:** `UpdateReceiptToleranceRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `policyId` | Uuid | Required | Path param | Governance policy identifier |
| `quantityTolerancePercent` | BigDecimal | Optional | Min 0; max 100 | Percentage over/under receipt tolerance |
| `quantityToleranceAbsolute` | BigDecimal | Optional | Min 0 | Absolute quantity tolerance |
| `autoAcceptWithinTolerance` | Boolean | Optional | Default `true` (VR-048) | Auto-accept variances within tolerance |
| `effectiveFrom` | LocalDate | Required | Valid date | Tolerance effective date |

---

### API-029 — `GET /api/v1/governance/approval-thresholds`

**DTO:** `GetEffectiveApprovalThresholdQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `transactionType` | String | Required | Valid transaction type enum | Transaction context |
| `locationCode` | LocationCode | Optional | User location scope | Location-specific threshold lookup |
| `asOfDate` | LocalDate | Optional | Default today | Effective date for threshold evaluation |

---

### API-030 — `GET /api/v1/governance/receipt-tolerances`

**DTO:** `GetReceiptToleranceQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | User location scope | Receiving location context |
| `supplierCode` | SupplierCode | Optional | Valid supplier when provided | Supplier-specific tolerance |
| `asOfDate` | LocalDate | Optional | Default today | Effective date for tolerance |

---

### API-031 — `POST /api/v1/governance/segregation-of-duties/evaluate`

**DTO:** `EvaluateSegregationOfDutiesRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `initiatorUserId` | String | Required | Max 50 chars; must exist | User who initiated the transaction |
| `approverUserId` | String | Required | Max 50 chars; must exist; must differ from initiator (VR-075, VR-083) | Proposed approver user |
| `transactionType` | String | Required | Enum: `COUNT_VARIANCE_APPROVAL`, `ADJUSTMENT_APPROVAL`, `WRITE_OFF_APPROVAL`, `ROLE_ASSIGNMENT` | Transaction context for SoD check |
| `transactionReference` | String | Optional | Max 100 chars | Reference to underlying transaction |

---

## M-04 — Inventory Balance

### API-032 — `POST /api/v1/inventory/opening-balances`

**DTO:** `EstablishOpeningBalancesRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Location must be in `PLANNED` or pre-activation state (VR-024, VR-025) | Target location for opening balances |
| `approvalReference` | String | Conditional | Required before location activation (VR-025) | Authorized approval reference |
| `balanceLines` | Array\<OpeningBalanceLineDto\> | Required | Min 1 line | Opening balance per SKU |

**`OpeningBalanceLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Must exist in catalog (VR-024) | Product SKU |
| `quantity` | PositiveQuantityDto | Required | Amount min 0 (VR-023) | Verified opening on-hand quantity |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products | Lot/batch at go-live |
| `ownershipType` | String | Optional | Enum: `OWNED`, `CONSIGNMENT`; default `OWNED` | Ownership classification |

---

### API-033 — `GET /api/v1/inventory/stock-positions`

**DTO:** `GetStockPositionsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Optional | At least one of `sku` or `locationCode` required (VR-054) | Product filter |
| `locationCode` | LocationCode | Optional | User location scope (VR-053) | Location filter |
| `stockStatus` | String | Optional | Enum: `IN_STOCK`, `LOW_STOCK`, `OUT_OF_STOCK`, `OVERSTOCK` | Status filter |
| `abcClass` | AbcClass | Optional | `A`, `B`, or `C` | ABC class filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-034 — `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}`

**DTO:** `GetStockPositionRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; user location scope (VR-053) | Location code |
| `sku` | ProductSku | Required | Path param; must exist (VR-054) | Product SKU |

---

### API-035 — `GET /api/v1/inventory/availability/{sku}`

**DTO:** `GetAvailabilityBySkuQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Path param | Product SKU |
| `locationCode` | LocationCode | Required | Query param; user location scope (VR-055) | Fulfillment location for ATP inquiry |
| `requestedQuantity` | BigDecimal | Optional | Min 0 | Quantity to evaluate partial availability against |

---

### API-036 — `GET /api/v1/inventory/availability/{sku}/network`

**DTO:** `GetNetworkAvailabilityQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Path param | Product SKU |
| `locationCodes` | Array\<LocationCode\> | Optional | Subset of user-authorized locations only (VR-064) | Locations to include; default all authorized |
| `excludeQuarantined` | Boolean | Optional | Default `true` (VR-056) | Exclude quarantined from ATP rollup |
| `excludePromotionalRingFence` | Boolean | Optional | Default `false` | Exclude promotional ring-fenced quantity |

---

### API-037 — `GET /api/v1/inventory/stock-status/{locationCode}/{sku}`

**DTO:** `GetStockStatusIndicatorRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; stock policy must exist (VR-059) | Location code |
| `sku` | ProductSku | Required | Path param | Product SKU |

---

### API-038 — `POST /api/v1/inventory/stock-policies`

**DTO:** `DefineStockPolicyRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Active location | Policy location |
| `sku` | ProductSku | Required | Active product | Policy product |
| `reorderLevel` | BigDecimal | Required | Min 0 (VR-018) | ATP level triggering replenishment (BR-009) |
| `minimumThreshold` | BigDecimal | Required | Min 0; must not exceed `reorderLevel` unless inverted policy (VR-019) | Minimum stock threshold |
| `safetyStock` | BigDecimal | Required | Min 0 (VR-018, BR-010) | Safety stock buffer |
| `maximumThreshold` | BigDecimal | Optional | Min 0; must be ≥ `reorderLevel` when provided | Overstock threshold |
| `leadTimeDays` | Integer | Optional | Min 0 | Replenishment lead time in business days |
| `effectiveFrom` | LocalDate | Required | Valid date (VR-020) | Policy effective date |

---

### API-039 — `GET /api/v1/inventory/stock-policies/{locationCode}/{sku}`

**DTO:** `GetStockPolicyRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param | Product SKU |
| `asOfDate` | LocalDate | Optional | Default today | Effective date for policy lookup |

---

### API-040 — `PATCH /api/v1/inventory/stock-policies/{locationCode}/{sku}`

**DTO:** `UpdateStockPolicyRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param | Product SKU |
| `reorderLevel` | BigDecimal | Optional | Min 0 (VR-018) | Updated reorder level |
| `minimumThreshold` | BigDecimal | Optional | Min 0 (VR-019) | Updated minimum threshold |
| `safetyStock` | BigDecimal | Optional | Min 0 | Updated safety stock |
| `maximumThreshold` | BigDecimal | Optional | Min 0 | Updated maximum threshold |
| `leadTimeDays` | Integer | Optional | Min 0 | Updated lead time |
| `effectiveFrom` | LocalDate | Required | Valid date; retains history (VR-020) | Effective date for threshold change |

*At least one threshold field must be present.*

---

### API-041 — `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/lots`

**DTO:** `GetLotBreakdownRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param; product must be traceable | Product SKU |
| `includeQuarantined` | Boolean | Optional | Default `false` | Include quarantined lot quantities |

---

### API-042 — `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity`

**DTO:** `EvaluateSourceTransferCapacityQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; source location | Source location code |
| `sku` | ProductSku | Required | Path param | Product SKU |
| `requestedQuantity` | BigDecimal | Optional | Min 0; evaluated against max transferable (VR-140) | Quantity to validate against source spare capacity |

---

### API-043 — `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations`

**DTO:** `ReserveStockRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param; location active and not frozen | Location code |
| `sku` | ProductSku | Required | Path param; product active (VR-006) | Product SKU |
| `quantity` | PositiveQuantityDto | Required | Must not exceed ATP (VR-092); safety stock rules (VR-094, BR-010) | Quantity to reserve |
| `orderId` | String | Required | Max 50 chars; valid order reference (VR-093) | Customer order identifier |
| `orderLineId` | String | Required | Max 50 chars | Order line identifier |
| `reservationExpiry` | Instant | Optional | Future timestamp | Reservation expiry for auto-release |
| `safetyStockExceptionReference` | String | Conditional | Required when reservation breaches safety stock (VR-124, VR-125) | Authorized safety stock exception |

---

### API-044 — `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations/{reservationId}/release`

**DTO:** `ReleaseReservationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param | Product SKU |
| `reservationId` | Uuid | Required | Path param; must exist | Reservation identifier |
| `releaseQuantity` | PositiveQuantityDto | Optional | Must not exceed reserved quantity (VR-095); default full release | Quantity to release |
| `releaseReason` | String | Required | Enum: `ORDER_CANCELLED`, `LINE_REMOVED`, `QUANTITY_CHANGED`, `FULFILLED`, `POLICY_EXPIRY` (VR-096) | Reason for release |

---

### API-045 — `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds`

**DTO:** `ApplyQuarantineHoldRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param | Product SKU |
| `quantity` | PositiveQuantityDto | Required | Must not exceed on-hand (VR-084) | Quantity to place on hold |
| `holdReason` | String | Required | Enum: `QUALITY`, `RECALL`, `CUSTOMS`, `BONDED`, `INVESTIGATION` (BR-013, BR-030) | Hold reason classification |
| `reasonCode` | ReasonCode | Required | Active reason code (VR-026) | Governance reason code |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products | Affected lot/batch |
| `notes` | String | Optional | Max 1000 chars | Hold documentation |

---

### API-046 — `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds/{holdId}/release`

**DTO:** `ReleaseQuarantineHoldRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param | Product SKU |
| `holdId` | Uuid | Required | Path param; hold must be active | Quarantine hold identifier |
| `releaseQuantity` | PositiveQuantityDto | Optional | Must not exceed held quantity; default full release | Quantity to release from hold |
| `disposition` | String | Required | Enum: `RESTORE_TO_SELLABLE`, `WRITE_OFF`, `RETURN_TO_SUPPLIER` (VR-085) | Post-release disposition |
| `inspectionOutcomeReference` | String | Conditional | Required for `RESTORE_TO_SELLABLE` (VR-085) | Quality inspection approval reference |
| `reasonCode` | ReasonCode | Required | Active reason code | Release reason code |

---

### API-047 — `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/consignment-ownership`

**DTO:** `TransferConsignmentOwnershipRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param; stock must be consignment (BR-031) | Product SKU |
| `quantity` | PositiveQuantityDto | Required | Must not exceed consignment on-hand | Quantity to transfer ownership |
| `consumptionReference` | String | Required | Max 100 chars | Sale or consumption event reference |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products | Affected lot |

---

### API-048 — `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/promotional-segregation`

**DTO:** `SegregatePromotionalStockRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param | Product SKU |
| `campaignId` | String | Required | Max 50 chars | Promotional campaign identifier |
| `allocationId` | Uuid | Required | Valid promotional allocation (BR-029) | Allocation triggering segregation |
| `quantity` | PositiveQuantityDto | Required | Must not exceed available ATP at allocation time (VR-127) | Quantity to ring-fence |

*Internal/event-driven API — typically invoked by campaign module, not end-user UI.*

---

## M-05 — Procurement & Supplier

### API-049 — `POST /api/v1/suppliers`

**DTO:** `RegisterSupplierRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `supplierCode` | SupplierCode | Required | Unique; max 30 chars | Supplier identifier |
| `name` | String | Required | Max 200 chars; non-blank | Supplier legal or trading name |
| `contactEmail` | String | Optional | Valid email format; max 254 chars | Primary contact email |
| `contactPhone` | String | Optional | Max 30 chars | Primary contact phone |
| `paymentTermsDays` | Integer | Required | Min 0 | Standard payment terms in days |
| `defaultLeadTimeDays` | Integer | Optional | Min 0 | Default procurement lead time |
| `isConsignment` | Boolean | Optional | Default `false` (BR-031) | Consignment agreement indicator |
| `currencyCode` | CurrencyCode | Optional | Default organization currency | Default transaction currency |

---

### API-050 — `GET /api/v1/suppliers`

**DTO:** `ListSuppliersQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `isActive` | Boolean | Optional | Default `true` | Filter by active status |
| `name` | String | Optional | Max 200 chars; partial match | Filter by supplier name |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-051 — `GET /api/v1/suppliers/{supplierCode}`

**DTO:** `GetSupplierByCodeRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `supplierCode` | SupplierCode | Required | Path param; must exist | Supplier code |

---

### API-052 — `PATCH /api/v1/suppliers/{supplierCode}`

**DTO:** `UpdateSupplierTermsRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `supplierCode` | SupplierCode | Required | Path param | Supplier code |
| `name` | String | Optional | Max 200 chars | Updated supplier name |
| `contactEmail` | String | Optional | Valid email format | Updated contact email |
| `contactPhone` | String | Optional | Max 30 chars | Updated contact phone |
| `paymentTermsDays` | Integer | Optional | Min 0 | Updated payment terms |
| `defaultLeadTimeDays` | Integer | Optional | Min 0 | Updated lead time |
| `isConsignment` | Boolean | Optional | — | Updated consignment flag |
| `currencyCode` | CurrencyCode | Optional | ISO 4217 | Updated currency |

*At least one body field must be present.*

---

### API-053 — `POST /api/v1/suppliers/{supplierCode}/deactivate`

**DTO:** `DeactivateSupplierRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `supplierCode` | SupplierCode | Required | Path param; no open POs unless policy allows | Supplier to deactivate |
| `reason` | String | Required | Max 500 chars | Deactivation reason |
| `effectiveDate` | LocalDate | Optional | Default today | Effective deactivation date |

---

### API-054 — `POST /api/v1/procurement/requisitions`

**DTO:** `CreatePurchaseRequisitionRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `receivingLocationCode` | LocationCode | Required | Active location (VR-119) | Target receiving location |
| `justification` | String | Required | Max 1000 chars; non-blank (VR-119) | Business justification |
| `lines` | Array\<RequisitionLineDto\> | Required | Min 1 line | Requisition line items |
| `triggeringAlertId` | Uuid | Optional | Valid alert when replenishment-triggered | Low-stock alert reference |

**`RequisitionLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Active product; not discontinued (VR-120, BR-027) | Product to requisition |
| `quantity` | PositiveQuantityDto | Required | Min exclusive 0 (VR-117) | Requested quantity |
| `neededByDate` | LocalDate | Optional | Valid future or present date | Required delivery date |

---

### API-055 — `GET /api/v1/procurement/requisitions/{requisitionId}`

**DTO:** `GetPurchaseRequisitionRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `requisitionId` | Uuid | Required | Path param; must exist | Requisition identifier |

---

### API-056 — `POST /api/v1/procurement/requisitions/{requisitionId}/approve`

**DTO:** `ApprovePurchaseRequisitionRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `requisitionId` | Uuid | Required | Path param; status must be submitted | Requisition identifier |
| `approvalNotes` | String | Optional | Max 1000 chars | Approver notes |
| `networkTransferDeclined` | Boolean | Optional | Required true when network stock exists and transfer not pursued (VR-118) | Confirms transfer-before-buy evaluation |
| `networkTransferDeclineReason` | String | Conditional | Required when `networkTransferDeclined=true` | Reason transfer was not selected |

---

### API-057 — `POST /api/v1/procurement/requisitions/{requisitionId}/reject`

**DTO:** `RejectPurchaseRequisitionRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `requisitionId` | Uuid | Required | Path param | Requisition identifier |
| `rejectionReason` | String | Required | Max 1000 chars; non-blank (VR-131) | Documented rejection reason |

---

### API-058 — `POST /api/v1/procurement/requisitions/{requisitionId}/convert-to-po`

**DTO:** `ConvertRequisitionToPurchaseOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `requisitionId` | Uuid | Required | Path param; must be approved | Requisition identifier |
| `supplierCode` | SupplierCode | Required | Active supplier | Selected supplier |
| `expectedDeliveryDate` | LocalDate | Required | Valid date not in distant past (VR-033) | Expected delivery date |
| `paymentTermsDays` | Integer | Optional | Overrides supplier default | PO payment terms |
| `lineOverrides` | Array\<PoLineOverrideDto\> | Optional | Quantity must not exceed requisition line | Optional line-level overrides |

**`PoLineOverrideDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `requisitionLineId` | Uuid | Required | Must match requisition line | Requisition line reference |
| `orderedQuantity` | PositiveQuantityDto | Optional | Min exclusive 0; ≤ requisition quantity | Override ordered quantity |
| `unitPrice` | MonetaryAmountDto | Optional | Amount min 0 | Line unit price |

---

### API-059 — `POST /api/v1/procurement/purchase-orders`

**DTO:** `PlacePurchaseOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `supplierCode` | SupplierCode | Required | Active supplier (VR-030) | Supplier code |
| `receivingLocationCode` | LocationCode | Required | Active location (VR-031) | Receiving location |
| `expectedDeliveryDate` | LocalDate | Required | Valid date (VR-033) | Expected delivery date |
| `currencyCode` | CurrencyCode | Optional | Default supplier currency | PO currency |
| `paymentTermsDays` | Integer | Optional | Min 0 | Payment terms |
| `lines` | Array\<PurchaseOrderLineDto\> | Required | Min 1 line (VR-030) | PO line items |
| `notes` | String | Optional | Max 1000 chars | PO notes |

**`PurchaseOrderLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Active product; not discontinued (VR-031, BR-027) | Ordered product |
| `orderedQuantity` | PositiveQuantityDto | Required | Min exclusive 0 (VR-032) | Ordered quantity |
| `unitPrice` | MonetaryAmountDto | Optional | Amount min 0 | Unit price |
| `lineNumber` | Integer | Optional | Min 1 | Client line sequence |

---

### API-060 — `GET /api/v1/procurement/purchase-orders`

**DTO:** `ListOpenPurchaseOrdersQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `status` | String | Optional | Enum: `OPEN`, `PARTIAL`, `CLOSED`, `CANCELLED`; default `OPEN`,`PARTIAL` | PO status filter |
| `supplierCode` | SupplierCode | Optional | Valid supplier | Supplier filter |
| `receivingLocationCode` | LocationCode | Optional | User location scope (VR-034) | Receiving location filter |
| `expectedDeliveryFrom` | LocalDate | Optional | On or before `expectedDeliveryTo` | Expected delivery range start |
| `expectedDeliveryTo` | LocalDate | Optional | On or after `expectedDeliveryFrom` | Expected delivery range end |
| `isOverdue` | Boolean | Optional | — | Filter overdue PO lines (VR-123) |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-061 — `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}`

**DTO:** `GetPurchaseOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `purchaseOrderId` | Uuid | Required | Path param; must exist | Purchase order identifier |

---

### API-062 — `PATCH /api/v1/procurement/purchase-orders/{purchaseOrderId}`

**DTO:** `AmendPurchaseOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `purchaseOrderId` | Uuid | Required | Path param; authorized user (VR-051) | Purchase order identifier |
| `expectedDeliveryDate` | LocalDate | Optional | Valid date (VR-033) | Updated expected delivery |
| `amendmentReason` | String | Required | Max 1000 chars; non-blank | Reason for amendment |
| `lineAmendments` | Array\<PoLineAmendmentDto\> | Optional | Cannot reduce below received qty (VR-050) | Line-level amendments |

**`PoLineAmendmentDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lineId` | Uuid | Required | Must exist on PO | PO line identifier |
| `orderedQuantity` | PositiveQuantityDto | Optional | ≥ received quantity (VR-050) | Amended ordered quantity |
| `unitPrice` | MonetaryAmountDto | Optional | Amount min 0 | Amended unit price |
| `action` | String | Optional | Enum: `UPDATE`, `CANCEL_LINE` | Line amendment action |

---

### API-063 — `POST /api/v1/procurement/purchase-orders/{purchaseOrderId}/cancel`

**DTO:** `CancelPurchaseOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `purchaseOrderId` | Uuid | Required | Path param; authorized user (VR-051) | Purchase order identifier |
| `cancellationReason` | String | Required | Max 1000 chars; non-blank | Cancellation reason |
| `effectiveDate` | LocalDate | Optional | Default today | Cancellation effective date |

---

### API-064 — `POST /api/v1/procurement/purchase-orders/{purchaseOrderId}/expected-deliveries`

**DTO:** `ScheduleInboundDeliveryRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `purchaseOrderId` | Uuid | Required | Path param; PO must be open | Purchase order identifier |
| `expectedArrivalDate` | LocalDate | Required | Valid date not in distant past (VR-033) | Expected arrival date |
| `carrierReference` | String | Optional | Max 100 chars | Carrier or shipment reference |
| `lineDeliveries` | Array\<LineDeliveryScheduleDto\> | Optional | Line must exist on PO | Per-line delivery schedule |

**`LineDeliveryScheduleDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lineId` | Uuid | Required | Valid PO line | PO line identifier |
| `expectedQuantity` | PositiveQuantityDto | Required | ≤ remaining open quantity | Expected quantity on this delivery |
| `expectedArrivalDate` | LocalDate | Optional | Overrides header date for line | Line-specific arrival date |

---

### API-065 — `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}/validate-for-receipt`

**DTO:** `ValidatePoForReceiptQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `purchaseOrderId` | Uuid | Required | Path param | Purchase order identifier |
| `receivingLocationCode` | LocationCode | Optional | Must match PO receiving location when provided | Intended receiving location |

---

## M-06 — Inbound Receiving

### API-066 — `POST /api/v1/inbound/goods-receipts`

**DTO:** `CreateGoodsReceiptRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `purchaseOrderId` | Uuid | Conditional | Required unless `adHocAuthorizationReference` provided (VR-040, BR-007) | Linked purchase order |
| `receivingLocationCode` | LocationCode | Required | Active location; not frozen (VR-012) | Receiving dock location |
| `supplierCode` | SupplierCode | Optional | Must match PO supplier when PO provided | Supplier reference |
| `carrierReference` | String | Optional | Max 100 chars | Carrier or ASN reference |
| `expectedReceiptDate` | LocalDate | Optional | Valid date | Expected receipt date |

---

### API-067 — `GET /api/v1/inbound/goods-receipts`

**DTO:** `ListGoodsReceiptsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `receivingLocationCode` | LocationCode | Optional | User location scope (VR-034) | Filter by receiving location |
| `status` | String | Optional | Enum: `DRAFT`, `VERIFIED`, `DISCREPANCY`, `PUT_AWAY_PENDING`, `COMPLETED` | Receipt status filter |
| `purchaseOrderId` | Uuid | Optional | Valid UUID | Filter by PO |
| `receivedFrom` | LocalDate | Optional | On or before `receivedTo` | Receipt date range start |
| `receivedTo` | LocalDate | Optional | On or after `receivedFrom` | Receipt date range end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-068 — `GET /api/v1/inbound/goods-receipts/{goodsReceiptId}`

**DTO:** `GetGoodsReceiptRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `goodsReceiptId` | Uuid | Required | Path param; must exist | Goods receipt identifier |

---

### API-069 — `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/verify`

**DTO:** `VerifyGoodsReceiptRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `goodsReceiptId` | Uuid | Required | Path param | Goods receipt identifier |
| `lines` | Array\<ReceiptVerificationLineDto\> | Required | Min 1 line (VR-035, VR-036) | Per-line verification results |

**`ReceiptVerificationLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lineId` | Uuid | Required | Must exist on receipt | Receipt line identifier |
| `sku` | ProductSku | Required | Must match PO line product (VR-036) | Verified product SKU |
| `acceptedQuantity` | PositiveQuantityDto | Required | ≤ physically verified qty (VR-035) | Accepted quantity |
| `rejectedQuantity` | QuantityDto | Optional | Min 0; default 0 (VR-037) | Rejected or damaged quantity |
| `conditionGrade` | String | Optional | Enum: `NEW`, `DAMAGED`, `EXPIRED` | Condition at receipt |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products (BR-017) | Lot/batch captured at receipt |
| `shelfLifeProfile` | ShelfLifeProfileDto | Conditional | Required for shelf-life products; MRSL check (BR-016) | Shelf-life attributes |

---

### API-070 — `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies`

**DTO:** `RecordReceiptDiscrepancyRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `goodsReceiptId` | Uuid | Required | Path param | Goods receipt identifier |
| `lineId` | Uuid | Required | Must exist on receipt | Affected receipt line |
| `discrepancyType` | String | Required | Enum: `SHORT_SHIPMENT`, `OVER_SHIPMENT`, `WRONG_ITEM`, `DAMAGE`, `SHELF_LIFE_NON_COMPLIANCE` (VR-038) | Discrepancy classification |
| `varianceQuantity` | PositiveQuantityDto | Required | Min exclusive 0 | Variance quantity |
| `reasonCode` | ReasonCode | Required | Active code (VR-026) | Reason code |
| `notes` | String | Required | Max 2000 chars; non-blank (VR-038) | Discrepancy documentation |
| `evidenceReference` | String | Optional | Max 200 chars | Photo or document reference |

---

### API-071 — `GET /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies`

**DTO:** `ListReceiptDiscrepanciesQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `goodsReceiptId` | Uuid | Required | Path param | Goods receipt identifier |
| `status` | String | Optional | Enum: `OPEN`, `RESOLVED`; default `OPEN` | Discrepancy status filter |

---

### API-072 — `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies/{discrepancyId}/resolve`

**DTO:** `ResolveReceiptDiscrepancyRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `goodsReceiptId` | Uuid | Required | Path param | Goods receipt identifier |
| `discrepancyId` | Uuid | Required | Path param; must be open | Discrepancy identifier |
| `resolutionOutcome` | String | Required | Enum: `ACCEPT_VARIANCE`, `REJECT_QUANTITY`, `SUPPLIER_CLAIM`, `CREDIT_NOTE` | Resolution decision |
| `resolvedQuantity` | QuantityDto | Optional | Min 0 | Quantity accepted after resolution |
| `resolutionNotes` | String | Required | Max 2000 chars; non-blank | Resolution documentation |
| `supplierClaimReference` | String | Optional | Max 100 chars | Supplier claim reference |

---

### API-073 — `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/put-away`

**DTO:** `CompletePutAwayRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `goodsReceiptId` | Uuid | Required | Path param; receipt must be verified | Goods receipt identifier |
| `putAwayLines` | Array\<PutAwayLineDto\> | Required | Min 1 line (VR-043, BR-005) | Put-away line assignments |

**`PutAwayLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `receiptLineId` | Uuid | Required | Must exist on receipt | Receipt line reference |
| `quantity` | PositiveQuantityDto | Required | ≤ unreceived put-away remaining qty (VR-043) | Quantity put away |
| `storagePositionCode` | String | Required | Max 30 chars; must exist at location | Target storage position |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products | Lot placed in position |

---

### API-074 — `GET /api/v1/inbound/pending-put-away`

**DTO:** `ListPendingPutAwayQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | User location scope | Receiving location |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-075 — `POST /api/v1/inbound/ad-hoc-receipts`

**DTO:** `ReceiveAdHocInboundRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `receivingLocationCode` | LocationCode | Required | Active location (VR-042) | Receiving location |
| `adHocAuthorizationReference` | String | Required | Max 100 chars; authorized approver (VR-042) | Governance authorization reference |
| `reasonCode` | ReasonCode | Required | Active code (VR-026) | Ad-hoc receipt reason |
| `sourceDescription` | String | Required | Max 500 chars | Source of inbound stock |
| `lines` | Array\<AdHocReceiptLineDto\> | Required | Min 1 line | Receipt lines |

**`AdHocReceiptLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Active product | Product received |
| `acceptedQuantity` | PositiveQuantityDto | Required | Min exclusive 0 (VR-035) | Accepted quantity |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products | Lot/batch |
| `storagePositionCode` | String | Optional | Valid position at location | Target storage position |

---

### API-076 — `POST /api/v1/inbound/return-receipts`

**DTO:** `ReceiveReturnInboundRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `returnAuthorizationId` | Uuid | Required | Valid open RMA (VR-045, BR-025) | Return authorization identifier |
| `receivingLocationCode` | LocationCode | Required | Active location | Receiving location |
| `carrierReference` | String | Optional | Max 100 chars | Return shipment carrier reference |
| `lines` | Array\<ReturnReceiptLineDto\> | Required | Min 1 line | Return receipt lines |

**`ReturnReceiptLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Must match RMA line (VR-145) | Returned product |
| `receivedQuantity` | PositiveQuantityDto | Required | ≤ authorized return qty (VR-046) | Received quantity |
| `conditionGrade` | String | Optional | Enum: `NEW`, `OPENED`, `DAMAGED` | Initial condition observation |

---

### API-077 — `POST /api/v1/inbound/supplier-invoices`

**DTO:** `RegisterSupplierInvoiceRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `supplierCode` | SupplierCode | Required | Active supplier | Supplier code |
| `invoiceNumber` | String | Required | Max 50 chars; unique per supplier | Supplier invoice number |
| `invoiceDate` | LocalDate | Required | Valid date | Invoice date |
| `purchaseOrderId` | Uuid | Required | Valid PO linked to supplier | Purchase order reference |
| `goodsReceiptId` | Uuid | Optional | Must reference same PO when provided | Goods receipt reference |
| `currencyCode` | CurrencyCode | Required | ISO 4217 | Invoice currency |
| `lines` | Array\<InvoiceLineDto\> | Required | Min 1 line | Invoice line items |

**`InvoiceLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Must exist on PO/receipt | Invoiced product |
| `quantity` | PositiveQuantityDto | Required | Min exclusive 0 | Invoiced quantity |
| `unitPrice` | MonetaryAmountDto | Required | Amount min 0 | Unit price |
| `poLineId` | Uuid | Optional | Must match PO line | PO line reference |

---

### API-078 — `GET /api/v1/inbound/supplier-invoices/{invoiceId}`

**DTO:** `GetSupplierInvoiceRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `invoiceId` | Uuid | Required | Path param; must exist | Supplier invoice identifier |

---

### API-079 — `POST /api/v1/inbound/supplier-invoices/{invoiceId}/three-way-match`

**DTO:** `PerformThreeWayMatchRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `invoiceId` | Uuid | Required | Path param | Supplier invoice identifier |
| `toleranceOverrideReference` | String | Optional | Max 100 chars; authorized when exceeding tolerance (VR-048) | Tolerance override authorization |
| `forceReevaluation` | Boolean | Optional | Default `false` | Force re-run of match evaluation |

---

### API-080 — `POST /api/v1/inbound/supplier-invoices/{invoiceId}/authorize-payment`

**DTO:** `AuthorizeInvoicePaymentRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `invoiceId` | Uuid | Required | Path param; three-way match must be completed (BR-008) | Supplier invoice identifier |
| `authorizationNotes` | String | Optional | Max 1000 chars | Payment authorization notes |
| `paymentDueDate` | LocalDate | Optional | On or after invoice date | Scheduled payment date |

---

## M-07 — Order Fulfillment

### API-081 — `POST /api/v1/fulfillment/orders`

**DTO:** `CreateCustomerOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `externalOrderReference` | String | Optional | Max 100 chars | CRM or channel order reference |
| `customerReference` | String | Optional | Max 100 chars | Customer account reference |
| `channel` | String | Required | Enum: `B2B`, `B2C`, `INTERNAL`, `MARKETPLACE` | Sales channel |
| `shipFromLocationCode` | LocationCode | Optional | Active location when specified | Preferred fulfillment location |
| `requestedShipDate` | LocalDate | Optional | Valid date | Requested ship date |
| `lines` | Array\<OrderLineDto\> | Required | Min 1 line | Order line items |

**`OrderLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lineNumber` | Integer | Required | Min 1 | Client line sequence |
| `sku` | ProductSku | Required | Active product (VR-006) | Ordered product |
| `requestedQuantity` | PositiveQuantityDto | Required | Min exclusive 0 | Requested order quantity |
| `substitutionAllowed` | Boolean | Optional | Default `false` | Whether substitution is permitted |

---

### API-082 — `GET /api/v1/fulfillment/orders`

**DTO:** `ListCustomerOrdersQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `status` | String | Optional | Enum: `DRAFT`, `AVAILABILITY_CHECKED`, `CONFIRMED`, `PICKING`, `SHIPPED`, `CANCELLED`, `EXCEPTION` | Order status filter |
| `shipFromLocationCode` | LocationCode | Optional | User location scope | Fulfillment location filter |
| `customerReference` | String | Optional | Max 100 chars | Customer reference filter |
| `externalOrderReference` | String | Optional | Max 100 chars | External order reference |
| `orderDateFrom` | LocalDate | Optional | On or before `orderDateTo` | Order date range start |
| `orderDateTo` | LocalDate | Optional | On or after `orderDateFrom` | Order date range end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-083 — `GET /api/v1/fulfillment/orders/{orderId}`

**DTO:** `GetCustomerOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param; must exist (VR-108) | Customer order identifier |

---

### API-084 — `POST /api/v1/fulfillment/orders/{orderId}/availability`

**DTO:** `ConfirmOrderAvailabilityRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param | Customer order identifier |
| `locationCode` | LocationCode | Optional | Default order ship-from location; ATP-based (VR-090, BR-001) | Location for availability check |
| `includeInboundSupply` | Boolean | Optional | Default `false` (VR-091) | Include approved inbound in commitment calculation |
| `lineOverrides` | Array\<AvailabilityLineCheckDto\> | Optional | Per-line location override | Per-line availability check parameters |

**`AvailabilityLineCheckDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lineId` | Uuid | Required | Must exist on order | Order line identifier |
| `locationCode` | LocationCode | Optional | User location scope | Line-specific fulfillment location |
| `requestedQuantity` | PositiveQuantityDto | Optional | Defaults to line quantity | Quantity to check |

---

### API-085 — `POST /api/v1/fulfillment/orders/{orderId}/confirm`

**DTO:** `ConfirmCustomerOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param; availability must be confirmed | Customer order identifier |
| `confirmationNotes` | String | Optional | Max 1000 chars | Confirmation notes |
| `reservationExpiry` | Instant | Optional | Future timestamp | Reservation expiry for all lines |
| `safetyStockExceptionReference` | String | Conditional | Required when reservation breaches safety stock (VR-124) | Safety stock override authorization |

---

### API-086 — `POST /api/v1/fulfillment/orders/{orderId}/cancel`

**DTO:** `CancelCustomerOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param | Customer order identifier |
| `cancellationReason` | String | Required | Max 1000 chars; non-blank (VR-096) | Cancellation reason |
| `lineIds` | Array\<Uuid\> | Optional | Must exist on order; empty means full order cancel | Specific lines to cancel |

---

### API-087 — `POST /api/v1/fulfillment/orders/{orderId}/multi-location-plan`

**DTO:** `CreateMultiLocationFulfillmentPlanRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param | Customer order identifier |
| `allocations` | Array\<LocationAllocationDto\> | Required | Min 1; sum must equal line qty (VR-106) | Per-location line allocations |

**`LocationAllocationDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderLineId` | Uuid | Required | Must exist on order | Order line identifier |
| `locationCode` | LocationCode | Required | ATP must suffice (VR-107) | Ship-from location |
| `quantity` | PositiveQuantityDto | Required | ≤ location ATP (VR-107) | Allocated quantity |

---

### API-088 — `POST /api/v1/fulfillment/orders/{orderId}/pick-lists`

**DTO:** `AssignPickListRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param; order must be confirmed | Customer order identifier |
| `assignedToUserId` | String | Optional | Max 50 chars; valid user | Picker user assignment |
| `priority` | String | Optional | Enum: `NORMAL`, `HIGH`, `URGENT` | Pick priority |
| `pickStrategy` | String | Optional | Enum: `FIFO`, `FEFO`; default per product policy (BR-014, BR-015) | Rotation strategy override |

---

### API-089 — `GET /api/v1/fulfillment/orders/{orderId}/pick-lists/awaiting`

**DTO:** `ListOrdersAwaitingPickQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param | Customer order identifier |
| `locationCode` | LocationCode | Optional | User location scope | Filter by fulfillment location |

---

### API-090 — `POST /api/v1/fulfillment/orders/{orderId}/picks/{pickId}/verify`

**DTO:** `VerifyPickRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param | Customer order identifier |
| `pickId` | Uuid | Required | Path param | Pick list identifier |
| `pickLines` | Array\<PickVerificationLineDto\> | Required | Min 1 line (VR-097, BR-003) | Verified pick lines |

**`PickVerificationLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderLineId` | Uuid | Required | Must exist on order | Order line identifier |
| `pickedQuantity` | PositiveQuantityDto | Required | ≤ reserved quantity (VR-098) | Verified picked quantity |
| `sku` | ProductSku | Required | Must match order line or approved substitute (VR-099, VR-110) | Picked product SKU |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products (BR-017) | Picked lot/batch |
| `substitutionReference` | String | Conditional | Required when SKU differs from order line (VR-110, VR-111) | Approved substitution reference |

---

### API-091 — `POST /api/v1/fulfillment/orders/{orderId}/pack`

**DTO:** `PackOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param; pick must be verified | Customer order identifier |
| `packages` | Array\<PackageDto\> | Required | Min 1 package | Packing details |

**`PackageDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `packageNumber` | Integer | Required | Min 1 | Package sequence |
| `weight` | BigDecimal | Optional | Min 0 | Package weight |
| `weightUnit` | String | Optional | Enum: `KG`, `LB` | Weight unit |
| `lineItems` | Array\<PackageLineDto\> | Required | Min 1 item | Contents of package |

**`PackageLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderLineId` | Uuid | Required | Must exist on order | Order line in package |
| `quantity` | PositiveQuantityDto | Required | ≤ picked quantity | Quantity in package |

---

### API-092 — `POST /api/v1/fulfillment/orders/{orderId}/shipments`

**DTO:** `DispatchShipmentRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param; pick verified (VR-097, BR-003) | Customer order identifier |
| `carrierCode` | String | Optional | Max 30 chars | Carrier identifier |
| `trackingNumber` | String | Optional | Max 100 chars | Shipment tracking number |
| `shippedAt` | Instant | Optional | Default now | Shipment dispatch timestamp |
| `shipmentLines` | Array\<ShipmentLineDto\> | Required | Min 1 line; ≤ reserved qty (VR-098) | Shipped line quantities |

**`ShipmentLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderLineId` | Uuid | Required | Must exist on order | Order line identifier |
| `shippedQuantity` | PositiveQuantityDto | Required | ≤ picked and reserved quantity | Shipped quantity |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products | Shipped lot/batch |

---

### API-093 — `POST /api/v1/fulfillment/orders/{orderId}/partial-fulfillment`

**DTO:** `CompletePartialFulfillmentRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param | Customer order identifier |
| `fulfillmentLines` | Array\<PartialFulfillmentLineDto\> | Required | Min 1 line (VR-100) | Lines to partially fulfill now |

**`PartialFulfillmentLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderLineId` | Uuid | Required | Must exist on order | Order line identifier |
| `fulfillQuantity` | PositiveQuantityDto | Required | > 0 and < full line qty (VR-100) | Quantity to ship now |
| `createBackorderForRemainder` | Boolean | Required | Default `true` | Whether remainder goes to backorder |
| `customerAcknowledgmentReference` | String | Conditional | Required when `createBackorderForRemainder=true` (VR-101, BR-028) | Customer acknowledgment reference |

---

### API-094 — `POST /api/v1/fulfillment/orders/{orderId}/backorders`

**DTO:** `RecordBackorderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param | Customer order identifier |
| `backorderLines` | Array\<BackorderLineDto\> | Required | Min 1 line (VR-103) | Backorder line items |

**`BackorderLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderLineId` | Uuid | Required | Must exist on order | Order line identifier |
| `backorderQuantity` | PositiveQuantityDto | Required | Equals unfulfilled remainder (VR-103) | Backordered quantity |
| `customerAcknowledgmentReference` | String | Required | Max 100 chars (VR-101, BR-028) | Customer acknowledgment reference |
| `expectedFulfillmentDate` | LocalDate | Optional | Valid date | Expected fulfillment date |

---

### API-095 — `POST /api/v1/fulfillment/backorders/{backorderId}/fulfill`

**DTO:** `FulfillBackorderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `backorderId` | Uuid | Required | Path param; must be open (VR-102) | Backorder identifier |
| `fulfillQuantity` | PositiveQuantityDto | Optional | ≤ backorder quantity; default full | Quantity to fulfill now |
| `locationCode` | LocationCode | Optional | ATP must suffice (VR-092) | Fulfillment location |
| `priorityOverrideReference` | String | Conditional | Required when fulfilling out of priority sequence (VR-102) | Priority override authorization |

---

### API-096 — `POST /api/v1/fulfillment/orders/{orderId}/exceptions`

**DTO:** `RaiseFulfillmentExceptionRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param | Customer order identifier |
| `exceptionType` | String | Required | Enum: `PICK_DISCREPANCY`, `SHELF_MISMATCH`, `DAMAGED_GOODS`, `SHORT_PICK` (VR-104) | Exception classification |
| `affectedLineId` | Uuid | Optional | Must exist on order when provided | Affected order line |
| `affectedQuantity` | PositiveQuantityDto | Optional | Min exclusive 0 when provided | Affected quantity |
| `description` | String | Required | Max 2000 chars; non-blank (VR-104) | Exception description |
| `proposedResolution` | String | Optional | Enum: `RE_PICK`, `PARTIAL_SHIP`, `CANCEL_LINE`, `ADJUST_INVENTORY` | Proposed resolution action |

---

### API-097 — `GET /api/v1/fulfillment/orders/{orderId}/status`

**DTO:** `GetOrderFulfillmentStatusRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `orderId` | Uuid | Required | Path param; must exist (VR-108) | Customer order identifier |
| `includeLineDetail` | Boolean | Optional | Default `true` | Include per-line status breakdown |

---

## M-08 — Network Transfer

### API-098 — `POST /api/v1/transfers`

**DTO:** `RequestStockTransferRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sourceLocationCode` | LocationCode | Required | Active; distinct from destination (VR-129) | Source location |
| `destinationLocationCode` | LocationCode | Required | Active; distinct from source (VR-129) | Destination location |
| `justification` | String | Required | Max 1000 chars; non-blank (VR-128) | Business justification |
| `lines` | Array\<TransferLineDto\> | Required | Min 1 line | Transfer line items |

**`TransferLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Active product | Product to transfer |
| `quantity` | PositiveQuantityDto | Required | ≤ source ATP (VR-130); respects source minimum (VR-140, BR-012) | Transfer quantity |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products (BR-017) | Lot/batch to transfer |

---

### API-099 — `GET /api/v1/transfers`

**DTO:** `ListStockTransfersQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `status` | String | Optional | Enum: `REQUESTED`, `APPROVED`, `DISPATCHED`, `IN_TRANSIT`, `RECEIVED`, `CANCELLED`, `REJECTED` | Transfer status filter |
| `sourceLocationCode` | LocationCode | Optional | User location scope | Source location filter |
| `destinationLocationCode` | LocationCode | Optional | User location scope | Destination location filter |
| `sku` | ProductSku | Optional | Valid SKU | Product filter |
| `requestedFrom` | LocalDate | Optional | On or before `requestedTo` | Request date range start |
| `requestedTo` | LocalDate | Optional | On or after `requestedFrom` | Request date range end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-100 — `GET /api/v1/transfers/{transferId}`

**DTO:** `GetStockTransferRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `transferId` | Uuid | Required | Path param; must exist | Transfer identifier |

---

### API-101 — `POST /api/v1/transfers/{transferId}/approve`

**DTO:** `ApproveTransferRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `transferId` | Uuid | Required | Path param; status `REQUESTED` | Transfer identifier |
| `approvalNotes` | String | Optional | Max 1000 chars | Approval notes |
| `approvedLines` | Array\<ApprovedTransferLineDto\> | Optional | Revalidated against source ATP (VR-132, VR-141) | Approved line quantities |

**`ApprovedTransferLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lineId` | Uuid | Required | Must exist on transfer | Transfer line identifier |
| `approvedQuantity` | PositiveQuantityDto | Required | ≤ requested and ≤ max transferable (VR-141) | Approved transfer quantity |

---

### API-102 — `POST /api/v1/transfers/{transferId}/reject`

**DTO:** `RejectTransferRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `transferId` | Uuid | Required | Path param | Transfer identifier |
| `rejectionReason` | String | Required | Max 1000 chars; non-blank (VR-131) | Documented rejection reason |

---

### API-103 — `POST /api/v1/transfers/{transferId}/dispatch`

**DTO:** `DispatchTransferRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `transferId` | Uuid | Required | Path param; status `APPROVED`; source not frozen | Transfer identifier |
| `dispatchedAt` | Instant | Optional | Default now | Dispatch timestamp |
| `carrierReference` | String | Optional | Max 100 chars | Carrier or shipment reference |
| `dispatchLines` | Array\<DispatchLineDto\> | Required | Min 1 line; ≤ approved qty (VR-133) | Dispatched line quantities |

**`DispatchLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lineId` | Uuid | Required | Must exist on transfer | Transfer line identifier |
| `dispatchedQuantity` | PositiveQuantityDto | Required | ≤ approved quantity (VR-133) | Dispatched quantity |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products | Dispatched lot/batch |

---

### API-104 — `POST /api/v1/transfers/{transferId}/receive`

**DTO:** `ConfirmTransferReceiptRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `transferId` | Uuid | Required | Path param; status `IN_TRANSIT` | Transfer identifier |
| `receivedAt` | Instant | Optional | Default now | Receipt timestamp |
| `receiptLines` | Array\<TransferReceiptLineDto\> | Required | Min 1 line (VR-134, VR-135) | Received line quantities |

**`TransferReceiptLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `lineId` | Uuid | Required | Must exist on transfer | Transfer line identifier |
| `receivedQuantity` | QuantityDto | Required | Min 0; variance triggers investigation (VR-135) | Received quantity |
| `storagePositionCode` | String | Optional | Valid at destination location | Destination storage position |
| `varianceNotes` | String | Conditional | Required when received ≠ dispatched | Receipt variance notes |

---

### API-105 — `POST /api/v1/transfers/{transferId}/cancel`

**DTO:** `CancelInTransitTransferRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `transferId` | Uuid | Required | Path param; must be in-transit or approved-not-dispatched | Transfer identifier |
| `cancellationReason` | String | Required | Max 1000 chars; non-blank | Cancellation reason |
| `reversalAction` | String | Optional | Enum: `RESTORE_SOURCE`, `INVESTIGATE_LOSS` | Reversal workflow action |

---

### API-106 — `GET /api/v1/transfers/pending-approvals`

**DTO:** `ListPendingTransferApprovalsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sourceLocationCode` | LocationCode | Optional | User location scope | Source location filter |
| `destinationLocationCode` | LocationCode | Optional | User location scope | Destination location filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-107 — `GET /api/v1/transfers/in-transit`

**DTO:** `ListInTransitStockQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | Source or destination; user scope (VR-136) | Location filter |
| `sku` | ProductSku | Optional | Valid SKU | Product filter |
| `isOverdue` | Boolean | Optional | — | Filter overdue in-transit (VR-137) |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

## M-09 — Inventory Accuracy

### API-108 — `POST /api/v1/accuracy/cycle-counts`

**DTO:** `ScheduleCycleCountRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Active location (VR-067) | Count location |
| `sku` | ProductSku | Required | Active product (VR-067) | Product to count |
| `scheduledDate` | LocalDate | Required | Valid date | Scheduled count date |
| `assignedToUserId` | String | Optional | Max 50 chars; valid user | Assigned counter |
| `priority` | String | Optional | Enum: `NORMAL`, `HIGH`; Class A default HIGH (VR-068, BR-032) | Count priority |

---

### API-109 — `GET /api/v1/accuracy/cycle-counts`

**DTO:** `ListCycleCountsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `status` | String | Optional | Enum: `SCHEDULED`, `IN_PROGRESS`, `COMPLETED`, `VARIANCE_DETECTED` | Count status filter |
| `sku` | ProductSku | Optional | Valid SKU | Product filter |
| `scheduledFrom` | LocalDate | Optional | On or before `scheduledTo` | Scheduled date range start |
| `scheduledTo` | LocalDate | Optional | On or after `scheduledFrom` | Scheduled date range end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-110 — `GET /api/v1/accuracy/cycle-counts/{cycleCountId}`

**DTO:** `GetCycleCountAssignmentRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `cycleCountId` | Uuid | Required | Path param; must exist | Cycle count identifier |

*Response must not include system expected quantity — blind count (VR-069, BR-018).*

---

### API-111 — `POST /api/v1/accuracy/cycle-counts/{cycleCountId}/result`

**DTO:** `SubmitCycleCountResultRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `cycleCountId` | Uuid | Required | Path param; status `SCHEDULED` or `IN_PROGRESS` | Cycle count identifier |
| `physicalQuantity` | QuantityDto | Required | Min 0 (VR-070) | Blind physical count result |
| `countNotes` | String | Optional | Max 1000 chars | Counter notes |
| `countedAt` | Instant | Optional | Default now | Count submission timestamp |

---

### API-112 — `POST /api/v1/accuracy/physical-counts`

**DTO:** `InitiatePhysicalInventoryCountRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Active location (VR-071) | Location for wall-to-wall count |
| `plannedStartDate` | LocalDate | Required | Valid date | Planned count start |
| `plannedEndDate` | LocalDate | Required | On or after `plannedStartDate` | Planned count end |
| `countScope` | String | Optional | Enum: `FULL_LOCATION`; default full | Count scope |
| `notes` | String | Optional | Max 1000 chars | Count initiation notes |

---

### API-113 — `GET /api/v1/accuracy/physical-counts/{physicalCountId}`

**DTO:** `GetPhysicalCountStatusRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `physicalCountId` | Uuid | Required | Path param; must exist | Physical count identifier |

---

### API-114 — `POST /api/v1/accuracy/physical-counts/{physicalCountId}/results`

**DTO:** `RecordPhysicalCountResultRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `physicalCountId` | Uuid | Required | Path param; location frozen (VR-071) | Physical count identifier |
| `countLines` | Array\<PhysicalCountLineDto\> | Required | Min 1 line | Line-level count results |

**`PhysicalCountLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Must have on-hand or receiving status at location | Product counted |
| `physicalQuantity` | QuantityDto | Required | Min 0 (VR-070) | Physical count quantity |
| `storagePositionCode` | String | Optional | Valid position at location | Storage position counted |
| `lotIdentity` | LotIdentityDto | Conditional | Required for traceable products | Lot-level count |

---

### API-115 — `POST /api/v1/accuracy/physical-counts/{physicalCountId}/certify`

**DTO:** `CertifyPhysicalInventoryCountRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `physicalCountId` | Uuid | Required | Path param; all SKUs counted (VR-072) | Physical count identifier |
| `certificationNotes` | String | Optional | Max 2000 chars | Certification notes |
| `certifiedByReference` | String | Optional | Max 100 chars | Certifying authority reference |

---

### API-116 — `POST /api/v1/accuracy/adjustment-cases`

**DTO:** `OpenAdjustmentCaseRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `originType` | String | Required | Enum: `COUNT_VARIANCE`, `DIRECT_ADJUSTMENT`, `FULFILLMENT_EXCEPTION` | Case origin type |
| `locationCode` | LocationCode | Required | User authorized at location (VR-079) | Affected location |
| `sku` | ProductSku | Required | Valid product | Affected product |
| `varianceId` | Uuid | Conditional | Required when `originType=COUNT_VARIANCE` | Linked count variance |
| `proposedAdjustmentQuantity` | BigDecimal | Conditional | Non-zero when direct adjustment; decrease ≤ on-hand (VR-078) | Proposed quantity change |
| `adjustmentDirection` | String | Conditional | Enum: `INCREASE`, `DECREASE`; required for direct adjustment | Adjustment direction |
| `reasonCode` | ReasonCode | Required | Active code (VR-077, BR-020) | Adjustment reason |
| `initialNotes` | String | Optional | Max 2000 chars | Initial case notes |

---

### API-117 — `GET /api/v1/accuracy/adjustment-cases/{caseId}`

**DTO:** `GetAdjustmentCaseRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `caseId` | Uuid | Required | Path param; must exist | Adjustment case identifier |

---

### API-118 — `POST /api/v1/accuracy/adjustment-cases/{caseId}/investigate`

**DTO:** `InvestigateVarianceRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `caseId` | Uuid | Required | Path param | Adjustment case identifier |
| `rootCauseCategory` | String | Required | Enum: `MISPLACEMENT`, `DAMAGE`, `THEFT`, `SYSTEM_ERROR`, `RECEIVING_ERROR`, `UNKNOWN` | Root cause category |
| `investigationFindings` | String | Required | Max 5000 chars; non-blank (VR-076, BR-022) | Investigation documentation |
| `correctiveAction` | String | Optional | Max 2000 chars | Proposed corrective action |

---

### API-119 — `POST /api/v1/accuracy/adjustment-cases/{caseId}/variances/{varianceId}/approve`

**DTO:** `ApproveCountVarianceRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `caseId` | Uuid | Required | Path param | Adjustment case identifier |
| `varianceId` | Uuid | Required | Path param | Count variance identifier |
| `approvalNotes` | String | Optional | Max 2000 chars | Approver notes |
| `approvedAdjustmentQuantity` | BigDecimal | Required | Non-zero; approver ≠ counter (VR-075, BR-019) | Approved adjustment quantity |

---

### API-120 — `POST /api/v1/accuracy/adjustment-cases/{caseId}/submit`

**DTO:** `SubmitAdjustmentForApprovalRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `caseId` | Uuid | Required | Path param; investigation complete (VR-076) | Adjustment case identifier |
| `adjustmentType` | String | Required | Enum: `ADJUSTMENT`, `WRITE_OFF` | Submission type |
| `quantity` | PositiveQuantityDto | Required | Decrease ≤ on-hand (VR-078, VR-081) | Adjustment or write-off quantity |
| `adjustmentDirection` | String | Conditional | Enum: `INCREASE`, `DECREASE`; required for `ADJUSTMENT` | Direction of adjustment |
| `reasonCode` | ReasonCode | Required | Active code (VR-077, BR-020) | Reason code |
| `evidenceReference` | String | Conditional | Required for write-off (VR-080, BR-023) | Supporting evidence reference |
| `financialValue` | MonetaryAmountDto | Optional | For threshold evaluation (VR-082) | Financial impact of adjustment |

---

### API-121 — `POST /api/v1/accuracy/adjustment-cases/{caseId}/approve`

**DTO:** `ApproveAdjustmentRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `caseId` | Uuid | Required | Path param; status submitted | Adjustment case identifier |
| `approvalNotes` | String | Optional | Max 2000 chars | Independent approver notes |
| `approvedQuantity` | PositiveQuantityDto | Optional | May differ from submitted within policy | Final approved quantity |

*Approver must differ from initiator and counter (VR-083, BR-021).*

---

### API-122 — `POST /api/v1/accuracy/adjustment-cases/{caseId}/reject`

**DTO:** `RejectAdjustmentRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `caseId` | Uuid | Required | Path param | Adjustment case identifier |
| `rejectionReason` | String | Required | Max 2000 chars; non-blank | Rejection reason |

---

### API-123 — `GET /api/v1/accuracy/pending-approvals`

**DTO:** `ListPendingApprovalsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `caseType` | String | Optional | Enum: `COUNT_VARIANCE`, `ADJUSTMENT`, `WRITE_OFF` | Case type filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

## M-10 — Returns Management

### API-124 — `POST /api/v1/returns/authorizations`

**DTO:** `IssueReturnAuthorizationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `originalOrderId` | Uuid | Required | Valid return-eligible order (VR-142, BR-025) | Original customer order |
| `returnReason` | String | Required | Max 500 chars; non-blank | Customer return reason |
| `returnWindowDays` | Integer | Optional | Min 1; default per policy | Authorization validity in days |
| `lines` | Array\<ReturnAuthorizationLineDto\> | Required | Min 1 line | Authorized return lines |

**`ReturnAuthorizationLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `originalOrderLineId` | Uuid | Required | Must exist on order | Original order line |
| `sku` | ProductSku | Required | Must match order line product | Return product |
| `authorizedQuantity` | PositiveQuantityDto | Required | ≤ originally shipped qty (VR-143) | Authorized return quantity |

---

### API-125 — `GET /api/v1/returns/authorizations`

**DTO:** `ListReturnAuthorizationsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `status` | String | Optional | Enum: `AUTHORIZED`, `IN_TRANSIT`, `RECEIVED`, `INSPECTING`, `COMPLETED`, `EXPIRED`, `CANCELLED` | RMA status filter |
| `originalOrderId` | Uuid | Optional | Valid UUID | Filter by original order |
| `customerReference` | String | Optional | Max 100 chars | Customer reference filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-126 — `GET /api/v1/returns/authorizations/{returnAuthorizationId}`

**DTO:** `GetReturnAuthorizationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `returnAuthorizationId` | Uuid | Required | Path param; must exist (VR-149) | Return authorization identifier |

---

### API-127 — `POST /api/v1/returns/authorizations/{returnAuthorizationId}/cancel`

**DTO:** `CancelReturnAuthorizationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `returnAuthorizationId` | Uuid | Required | Path param; must be open/unused | Return authorization identifier |
| `cancellationReason` | String | Required | Max 1000 chars; non-blank | Cancellation reason |

---

### API-128 — `POST /api/v1/returns/{returnId}/receive`

**DTO:** `ReceiveCustomerReturnRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `returnId` | Uuid | Required | Path param; valid open RMA (VR-144) | Customer return case identifier |
| `receivingLocationCode` | LocationCode | Required | Active location | Receiving location |
| `receivedLines` | Array\<ReturnReceiveLineDto\> | Required | Min 1 line | Received return lines |

**`ReturnReceiveLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `authorizationLineId` | Uuid | Required | Must exist on RMA | RMA line reference |
| `sku` | ProductSku | Required | Must match authorization (VR-145) | Received product |
| `receivedQuantity` | PositiveQuantityDto | Required | ≤ authorized qty (VR-046) | Received quantity |

---

### API-129 — `POST /api/v1/returns/{returnId}/inspect`

**DTO:** `InspectReturnedGoodsRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `returnId` | Uuid | Required | Path param; must be received | Customer return case identifier |
| `inspectionLines` | Array\<ReturnInspectionLineDto\> | Required | Min 1 line (VR-146, BR-026) | Inspection results |

**`ReturnInspectionLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `returnLineId` | Uuid | Required | Must exist on return | Return line identifier |
| `conditionGrade` | String | Required | Enum: `RESELLABLE`, `DAMAGED`, `DEFECTIVE`, `EXPIRED` | Condition assessment |
| `inspectedQuantity` | PositiveQuantityDto | Required | ≤ received quantity | Inspected quantity |
| `inspectionNotes` | String | Optional | Max 2000 chars | Inspection notes |

---

### API-130 — `POST /api/v1/returns/{returnId}/disposition`

**DTO:** `DispositionReturnRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `returnId` | Uuid | Required | Path param; inspection complete (VR-146) | Customer return case identifier |
| `dispositionAction` | String | Required | Enum: `RESTOCK`, `QUARANTINE`, `WRITE_OFF` | Disposition routing |
| `dispositionLines` | Array\<ReturnDispositionLineDto\> | Required | Min 1 line; sum must equal inspected qty (VR-147) | Per-line disposition |

**`ReturnDispositionLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `returnLineId` | Uuid | Required | Must exist on return | Return line identifier |
| `quantity` | PositiveQuantityDto | Required | ≤ inspected quantity | Disposition quantity |
| `restockLocationCode` | LocationCode | Conditional | Required when `dispositionAction=RESTOCK` | Restock target location |
| `reasonCode` | ReasonCode | Conditional | Required for `WRITE_OFF` (VR-148, BR-023) | Write-off reason code |
| `writeOffApprovalReference` | String | Conditional | Required for `WRITE_OFF` above threshold (VR-080) | Write-off approval reference |

---

### API-131 — `GET /api/v1/returns/pending-receipts`

**DTO:** `ListPendingReturnReceiptsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | User location scope | Receiving location filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

## M-11 — Commercial Campaign

### API-132 — `POST /api/v1/campaigns/allocations`

**DTO:** `CreatePromotionalAllocationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `campaignId` | String | Required | Max 50 chars | Campaign identifier |
| `campaignName` | String | Required | Max 200 chars; non-blank | Campaign display name |
| `locationCode` | LocationCode | Required | Active location | Allocation location |
| `sku` | ProductSku | Required | Active product | Allocated product |
| `allocatedQuantity` | PositiveQuantityDto | Required | ≤ available ATP at allocation (VR-127, BR-029) | Ring-fenced quantity |
| `channel` | String | Optional | Enum: `B2B`, `B2C`, `ALL`; default `ALL` | Channel designation |
| `campaignStartDate` | LocalDate | Required | Valid date (VR-126) | Campaign start date |
| `campaignEndDate` | LocalDate | Required | On or after `campaignStartDate` | Campaign end date |

---

### API-133 — `GET /api/v1/campaigns/allocations`

**DTO:** `ListPromotionalAllocationsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `campaignId` | String | Optional | Max 50 chars | Campaign filter |
| `status` | String | Optional | Enum: `PLANNED`, `ACTIVE`, `COMPLETED`, `RELEASED` | Allocation status |
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `activeOnDate` | LocalDate | Optional | Valid date | Allocations active on date |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-134 — `GET /api/v1/campaigns/allocations/{allocationId}`

**DTO:** `GetPromotionalAllocationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `allocationId` | Uuid | Required | Path param; must exist | Allocation identifier |

---

### API-135 — `PATCH /api/v1/campaigns/allocations/{allocationId}`

**DTO:** `AmendPromotionalAllocationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `allocationId` | Uuid | Required | Path param | Allocation identifier |
| `allocatedQuantity` | PositiveQuantityDto | Optional | ≤ available ATP when increasing | Amended allocated quantity |
| `campaignStartDate` | LocalDate | Optional | Valid date | Amended start date |
| `campaignEndDate` | LocalDate | Optional | On or after start date | Amended end date |
| `amendmentReason` | String | Required | Max 1000 chars; non-blank | Reason for amendment |

*At least one amendable field must be present.*

---

### API-136 — `POST /api/v1/campaigns/allocations/{allocationId}/readiness`

**DTO:** `EvaluateCampaignReadinessRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `allocationId` | Uuid | Required | Path param | Allocation identifier |
| `targetQuantity` | PositiveQuantityDto | Optional | Defaults to allocated quantity (VR-126) | Target quantity for readiness check |
| `readinessDeadline` | LocalDate | Optional | Valid date | Campaign commitment deadline |
| `confirmReadiness` | Boolean | Optional | Default `false` | Whether to certify readiness if sufficient |

---

### API-137 — `POST /api/v1/campaigns/allocations/{allocationId}/release`

**DTO:** `ReleasePromotionalAllocationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `allocationId` | Uuid | Required | Path param | Allocation identifier |
| `releaseReason` | String | Required | Enum: `CAMPAIGN_ENDED`, `MANUAL_RELEASE`, `CAMPAIGN_CANCELLED` | Release reason |
| `releaseNotes` | String | Optional | Max 1000 chars | Release notes |

---

### API-138 — `POST /api/v1/campaigns/allocations/{allocationId}/override`

**DTO:** `AuthorizePromotionalOverrideRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `allocationId` | Uuid | Required | Path param; allocation active | Allocation identifier |
| `orderId` | Uuid | Required | Valid customer order | Non-promotional order consuming ring-fence |
| `overrideQuantity` | PositiveQuantityDto | Required | ≤ ring-fenced remaining (BR-029) | Quantity to override |
| `authorizationReference` | String | Required | Max 100 chars; commercial leadership approval | Override authorization reference |
| `justification` | String | Required | Max 1000 chars; non-blank | Business justification |

---

### API-139 — `GET /api/v1/campaigns/ring-fence/{locationCode}/{sku}`

**DTO:** `CheckRingFenceQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Required | Path param | Location code |
| `sku` | ProductSku | Required | Path param | Product SKU |
| `asOfDate` | LocalDate | Optional | Default today | Date for active ring-fence check |

---

## M-12 — Identity & Access

### API-140 — `POST /api/v1/users`

**DTO:** `ProvisionUserAccountRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `userId` | String | Required | Max 50 chars; unique; alphanumeric and underscore | User identifier |
| `email` | String | Required | Valid email; max 254 chars | User email address |
| `displayName` | String | Required | Max 200 chars; non-blank | User display name |
| `initialRoles` | Array\<RoleAssignmentDto\> | Required | Min 1 role; no SoD conflicts (VR-083) | Initial role assignments |
| `externalDirectoryId` | String | Optional | Max 100 chars | HR/IdP directory reference |

---

### API-141 — `GET /api/v1/users`

**DTO:** `ListUserAccountsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `status` | String | Optional | Enum: `ACTIVE`, `SUSPENDED`, `DEACTIVATED` | Account status filter |
| `roleCode` | String | Optional | Max 50 chars | Filter by assigned role |
| `locationCode` | LocationCode | Optional | Filter users with scope at location | Location scope filter |
| `search` | String | Optional | Max 200 chars; matches name or email | Search term |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-142 — `GET /api/v1/users/{userId}`

**DTO:** `GetUserAccountRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `userId` | String | Required | Path param; must exist | User identifier |

---

### API-143 — `POST /api/v1/users/{userId}/roles`

**DTO:** `AssignRoleRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `userId` | String | Required | Path param; account must be active | User identifier |
| `roleAssignment` | RoleAssignmentDto | Required | No SoD conflict with existing roles (VR-083) | Role assignment details |

---

### API-144 — `DELETE /api/v1/users/{userId}/roles/{roleAssignmentId}`

**DTO:** `RevokeRoleAssignmentRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `userId` | String | Required | Path param | User identifier |
| `roleAssignmentId` | Uuid | Required | Path param; must exist on user | Role assignment identifier |
| `revocationReason` | String | Optional | Max 500 chars | Reason for revocation |

---

### API-145 — `POST /api/v1/users/{userId}/suspend`

**DTO:** `SuspendUserAccountRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `userId` | String | Required | Path param; must be active | User identifier |
| `suspensionReason` | String | Required | Max 1000 chars; non-blank | Suspension reason |
| `suspendedUntil` | LocalDate | Optional | Future date when temporary | Suspension end date |

---

### API-146 — `POST /api/v1/users/{userId}/deactivate`

**DTO:** `DeactivateUserAccountRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `userId` | String | Required | Path param | User identifier |
| `deactivationReason` | String | Required | Max 1000 chars; non-blank | Deactivation reason |
| `effectiveDate` | LocalDate | Optional | Default today | Deactivation effective date |

---

### API-147 — `POST /api/v1/users/sync`

**DTO:** `SyncUsersFromDirectoryRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `syncMode` | String | Required | Enum: `FULL`, `INCREMENTAL` | Directory sync mode |
| `sinceTimestamp` | Instant | Conditional | Required when `syncMode=INCREMENTAL` | Sync changes since timestamp |
| `dryRun` | Boolean | Optional | Default `false` | Validate without persisting changes |

---

### API-148 — `POST /api/v1/authorization/actions/evaluate`

**DTO:** `EvaluateAuthorizationRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `userId` | String | Optional | Max 50 chars; defaults to authenticated user | User to evaluate |
| `action` | String | Required | Max 100 chars; valid permission code | Action or command to authorize |
| `resourceType` | String | Optional | Max 50 chars | Resource type context |
| `resourceId` | String | Optional | Max 100 chars | Resource identifier |
| `locationCode` | LocationCode | Optional | Location scope for action | Location context |

---

### API-149 — `POST /api/v1/authorization/location-scope/validate`

**DTO:** `ValidateLocationScopeRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `userId` | String | Optional | Defaults to authenticated user | User to validate |
| `locationCode` | LocationCode | Required | Must exist (VR-008, VR-053) | Location to validate access |
| `requiredPermission` | String | Optional | Max 100 chars | Specific permission required at location |

---

## M-13 — Inventory Intelligence

All intelligence APIs are read-only. Request DTOs comprise path and query parameters only.

### API-150 — `GET /api/v1/intelligence/dashboard`

**DTO:** `GetInventoryDashboardQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `scope` | String | Optional | Enum: `LOCATION`, `NETWORK`; default `LOCATION` | Dashboard scope |
| `locationCode` | LocationCode | Conditional | Required when `scope=LOCATION`; user scope (VR-151) | Location for dashboard |
| `asOfTimestamp` | Instant | Optional | Default latest projection (VR-152) | Point-in-time for dashboard data |

---

### API-151 — `GET /api/v1/intelligence/stock-status/summary`

**DTO:** `GetStockStatusSummaryQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | User location scope (VR-151) | Location filter; omit for authorized network |
| `categoryCode` | String | Optional | Max 30 chars | Category filter |
| `abcClass` | AbcClass | Optional | `A`, `B`, or `C` | ABC class filter |

---

### API-152 — `GET /api/v1/intelligence/stock-status/board`

**DTO:** `GetStockStatusBoardQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCodes` | Array\<LocationCode\> | Optional | Authorized locations only (VR-151) | Locations to include |
| `stockStatus` | String | Optional | Enum: `IN_STOCK`, `LOW_STOCK`, `OUT_OF_STOCK`, `OVERSTOCK` | Status filter |
| `sku` | ProductSku | Optional | Valid SKU | Product filter |
| `abcClass` | AbcClass | Optional | ABC filter | ABC class filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-153 — `GET /api/v1/intelligence/availability/inquiries`

**DTO:** `GetAvailabilityInquiryLogQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Optional | Valid SKU | Product filter |
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `userId` | String | Optional | Max 50 chars | Inquiring user filter |
| `startDate` | LocalDate | Optional | On or before `endDate` (VR-062) | Inquiry period start |
| `endDate` | LocalDate | Optional | On or after `startDate` | Inquiry period end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-154 — `GET /api/v1/intelligence/quarantine-register`

**DTO:** `GetQuarantineRegisterQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `holdReason` | String | Optional | Enum: `QUALITY`, `RECALL`, `CUSTOMS`, `BONDED`, `INVESTIGATION` | Hold reason filter |
| `sku` | ProductSku | Optional | Valid SKU | Product filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-155 — `GET /api/v1/intelligence/movements`

**DTO:** `SearchMovementHistoryQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Optional | At least one filter recommended (VR-154) | Product filter |
| `locationCode` | LocationCode | Optional | User location scope (VR-154) | Location filter |
| `userId` | String | Optional | Max 50 chars | User attribution filter |
| `movementType` | String | Optional | Enum: `RECEIPT`, `SHIPMENT`, `ADJUSTMENT`, `TRANSFER`, `RESERVATION`, `WRITE_OFF`, `RETURN` | Movement type filter |
| `startDate` | LocalDate | Required | On or before `endDate` (VR-153) | Movement period start |
| `endDate` | LocalDate | Required | On or after `startDate` | Movement period end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-156 — `GET /api/v1/intelligence/audit-trail`

**DTO:** `QueryAuditTrailQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `entityType` | String | Optional | Max 50 chars | Entity type filter |
| `entityId` | String | Optional | Max 100 chars | Entity identifier filter |
| `userId` | String | Optional | Max 50 chars | Acting user filter |
| `action` | String | Optional | Max 100 chars | Action type filter |
| `startDate` | LocalDate | Required | On or before `endDate` (VR-153) | Audit period start |
| `endDate` | LocalDate | Required | On or after `startDate` | Audit period end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-157 — `GET /api/v1/intelligence/audit-trail/export`

**DTO:** `ExportAuditEvidenceQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `startDate` | LocalDate | Required | On or before `endDate`; max 365-day range | Export period start |
| `endDate` | LocalDate | Required | On or after `startDate` | Export period end |
| `entityTypes` | Array\<String\> | Optional | Max 20 types | Entity types to include |
| `locationCodes` | Array\<LocationCode\> | Optional | User authorized only (VR-154) | Location scope for export |
| `format` | String | Optional | Enum: `CSV`, `JSON`, `PDF`; default `CSV` | Export file format |

---

### API-158 — `GET /api/v1/intelligence/alerts`

**DTO:** `GetOperationalAlertsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `alertType` | String | Optional | Enum: `LOW_STOCK`, `OUT_OF_STOCK`, `INBOUND_DELAY`, `TRANSFER_DELAY`, `FULFILLMENT_EXCEPTION`, `PROMOTIONAL_READINESS`, `PENDING_APPROVAL` | Alert type filter |
| `severity` | String | Optional | Enum: `INFO`, `WARNING`, `CRITICAL` | Severity filter |
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `acknowledged` | Boolean | Optional | Default `false` | Include acknowledged alerts |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-159 — `POST /api/v1/intelligence/alerts/{alertId}/acknowledge`

**DTO:** `AcknowledgeOperationalAlertRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `alertId` | Uuid | Required | Path param; must be active (VR-113) | Alert identifier |
| `actionTaken` | String | Required | Enum: `REQUISITION`, `TRANSFER`, `DISMISS`, `DEFER` (VR-115) | Action taken on alert |
| `acknowledgmentNotes` | String | Conditional | Required when `actionTaken=DISMISS` or `DEFER` (VR-114) | Acknowledgment rationale |

---

### API-160 — `GET /api/v1/intelligence/replenishment/recommendations`

**DTO:** `GetReplenishmentRecommendationsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `sku` | ProductSku | Optional | Valid SKU | Product filter |
| `recommendationAction` | String | Optional | Enum: `PURCHASE`, `TRANSFER`, `HOLD`, `NO_ACTION` | Recommended action filter |
| `acknowledged` | Boolean | Optional | — | Filter by acknowledgment status |
| `startDate` | LocalDate | Optional | On or before `endDate` | Recommendation period start |
| `endDate` | LocalDate | Optional | On or after `startDate` | Recommendation period end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-161 — `GET /api/v1/intelligence/procurement/open-pos`

**DTO:** `GetOpenPurchaseOrderBoardQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `receivingLocationCode` | LocationCode | Optional | User location scope (VR-034) | Receiving location filter |
| `supplierCode` | SupplierCode | Optional | Valid supplier | Supplier filter |
| `isOverdue` | Boolean | Optional | — | Overdue PO filter (VR-123) |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-162 — `GET /api/v1/intelligence/procurement/inbound-calendar`

**DTO:** `GetInboundSupplyCalendarQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `startDate` | LocalDate | Required | On or before `endDate` (VR-033) | Calendar period start |
| `endDate` | LocalDate | Required | On or after `startDate`; max 90-day range | Calendar period end |
| `receivingLocationCode` | LocationCode | Optional | User location scope | Receiving location filter |
| `supplierCode` | SupplierCode | Optional | Valid supplier | Supplier filter |

---

### API-163 — `GET /api/v1/intelligence/procurement/inbound-delays`

**DTO:** `GetInboundDeliveryDelayLogQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `receivingLocationCode` | LocationCode | Optional | User location scope | Location filter |
| `supplierCode` | SupplierCode | Optional | Valid supplier | Supplier filter |
| `startDate` | LocalDate | Optional | On or before `endDate` | Delay log period start |
| `endDate` | LocalDate | Optional | On or after `startDate` | Delay log period end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-164 — `GET /api/v1/intelligence/fulfillment/backorders`

**DTO:** `GetBackorderPipelineQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Optional | Valid SKU | Product filter |
| `locationCode` | LocationCode | Optional | User location scope | Fulfillment location filter |
| `prioritySort` | Boolean | Optional | Default `true` (VR-102) | Sort by backorder priority policy |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-165 — `GET /api/v1/intelligence/fulfillment/exceptions`

**DTO:** `GetFulfillmentExceptionLogQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `exceptionType` | String | Optional | Enum: `PICK_DISCREPANCY`, `SHELF_MISMATCH`, `DAMAGED_GOODS`, `SHORT_PICK` | Exception type filter |
| `status` | String | Optional | Enum: `OPEN`, `RESOLVED`; default `OPEN` | Exception status |
| `startDate` | LocalDate | Optional | On or before `endDate` | Exception period start |
| `endDate` | LocalDate | Optional | On or after `startDate` | Exception period end |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-166 — `GET /api/v1/intelligence/network/imbalance`

**DTO:** `GetNetworkImbalanceAnalysisQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Optional | Valid SKU; active product (VR-139) | Product filter |
| `sourceLocationCode` | LocationCode | Optional | Active location | Excess location filter |
| `destinationLocationCode` | LocationCode | Optional | Active location | Shortage location filter |
| `includeRecommendations` | Boolean | Optional | Default `true` | Include transfer recommendations |

---

### API-167 — `GET /api/v1/intelligence/accuracy/shrinkage`

**DTO:** `GetShrinkageAnalysisQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `startDate` | LocalDate | Required | On or before `endDate` (VR-086) | Analysis period start |
| `endDate` | LocalDate | Required | On or after `startDate` | Analysis period end |
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `categoryCode` | String | Optional | Max 30 chars | Category filter |
| `reasonCode` | ReasonCode | Optional | Valid reason code (VR-087) | Reason code filter |
| `groupBy` | String | Optional | Enum: `LOCATION`, `SKU`, `REASON_CODE`, `CATEGORY`; default `SKU` | Aggregation dimension |

---

### API-168 — `GET /api/v1/intelligence/accuracy/count-performance`

**DTO:** `GetCountPerformanceMetricsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `startDate` | LocalDate | Required | On or before `endDate` (VR-157) | Reporting period start |
| `endDate` | LocalDate | Required | On or after `startDate` | Reporting period end |
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `countType` | String | Optional | Enum: `CYCLE_COUNT`, `PHYSICAL_COUNT`, `ALL`; default `ALL` | Count type filter |
| `abcClass` | AbcClass | Optional | ABC filter | ABC class filter |
| `excludePendingVariances` | Boolean | Optional | Default `true` (VR-158) | Exclude unresolved variances from accuracy rate |

---

### API-169 — `GET /api/v1/intelligence/campaigns/readiness`

**DTO:** `GetCampaignReadinessStatusQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `campaignId` | String | Optional | Max 50 chars | Campaign filter |
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `readinessStatus` | String | Optional | Enum: `READY`, `GAP_IDENTIFIED`, `PENDING` | Readiness status filter |
| `daysUntilStart` | Integer | Optional | Min 0 | Campaigns starting within N days |

---

### API-170 — `GET /api/v1/intelligence/kpis`

**DTO:** `GetInventoryKpisQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `startDate` | LocalDate | Required | On or before `endDate` (VR-162) | KPI period start |
| `endDate` | LocalDate | Required | On or after `startDate` | KPI period end |
| `kpiCodes` | Array\<String\> | Optional | Valid configured KPI codes (VR-161) | Specific KPIs to retrieve |
| `locationCodes` | Array\<LocationCode\> | Optional | User authorized only (VR-151) | Location scope for KPIs |
| `compareToTarget` | Boolean | Optional | Default `true` | Include target comparison |

---

### API-171 — `GET /api/v1/intelligence/valuation/snapshots`

**DTO:** `GetValuationSnapshotsQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `periodEndDate` | LocalDate | Optional | Valid date | Specific period-end snapshot |
| `startDate` | LocalDate | Optional | On or before `endDate` | Snapshot period range start |
| `endDate` | LocalDate | Optional | On or after `startDate` | Snapshot period range end |
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-172 — `GET /api/v1/intelligence/valuation/reconciliation`

**DTO:** `GetValuationReconciliationQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `periodEndDate` | LocalDate | Required | Valid period-end date | Reconciliation period end |
| `locationCode` | LocationCode | Optional | User location scope | Location filter |
| `varianceThresholdPercent` | BigDecimal | Optional | Min 0; max 100; default per policy | Variance threshold for flagging |
| `includeGlComparison` | Boolean | Optional | Default `true` | Include general ledger comparison data |

---

## Platform & Integration

### API-173 — `GET /api/v1/auth/session`

**DTO:** `GetSessionRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `includePermissions` | Boolean | Optional | Default `false` | Include resolved permission list in response |
| `includeLocationScope` | Boolean | Optional | Default `true` | Include user's location scope |

*Authentication via `Authorization` header — no request body.*

---

### API-174 — `POST /api/v1/auth/logout`

**DTO:** `LogoutRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `logoutAllSessions` | Boolean | Optional | Default `false` | Terminate all active sessions for user |

*No request body required; empty body accepted.*

---

### API-175 — `GET /api/v1/health`

**DTO:** `HealthCheckRequest`

*No path parameters, query parameters, or request body. Public endpoint — no authentication required.*

---

### API-176 — `POST /api/v1/integrations/sales/orders`

**DTO:** `ImportSalesOrderRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `externalOrderId` | String | Required | Max 100 chars; idempotent on re-import | CRM external order identifier |
| `externalSystemCode` | String | Required | Max 30 chars; registered integration source | Source system code |
| `customerReference` | String | Optional | Max 100 chars | CRM customer reference |
| `channel` | String | Required | Enum: `B2B`, `B2C`, `MARKETPLACE` | Sales channel |
| `shipFromLocationCode` | LocationCode | Optional | Active location when specified | Preferred ship-from location |
| `requestedShipDate` | LocalDate | Optional | Valid date | Requested ship date |
| `correlationId` | String | Optional | Max 100 chars; traceability (IB-08) | Integration correlation identifier |
| `lines` | Array\<ExternalOrderLineDto\> | Required | Min 1 line | Order lines from CRM |

**`ExternalOrderLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `externalLineId` | String | Required | Max 50 chars | CRM line identifier |
| `sku` | ProductSku | Required | Must exist in catalog (VR-007) | Product SKU |
| `quantity` | PositiveQuantityDto | Required | Min exclusive 0 | Ordered quantity |
| `unitPrice` | MonetaryAmountDto | Optional | Amount min 0 | Line unit price from CRM |

---

### API-177 — `GET /api/v1/integrations/sales/fulfillment-status`

**DTO:** `GetFulfillmentStatusFeedQuery`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `externalSystemCode` | String | Required | Max 30 chars | Requesting CRM system code |
| `updatedSince` | Instant | Optional | ISO-8601 UTC | Return orders updated since timestamp |
| `externalOrderId` | String | Optional | Max 100 chars | Filter by external order |
| `status` | String | Optional | Enum: `CONFIRMED`, `PICKING`, `SHIPPED`, `CANCELLED`, `BACKORDERED`, `EXCEPTION` | Fulfillment status filter |
| `page` | PageNumber | Optional | Min 1 | Pagination page |
| `pageSize` | PageSize | Optional | Min 1; max 100 | Pagination size |

---

### API-178 — `POST /api/v1/integrations/marketing/campaign-plans`

**DTO:** `ImportCampaignPlanRequest`

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `externalCampaignId` | String | Required | Max 50 chars; idempotent on re-import | Marketing system campaign ID |
| `externalSystemCode` | String | Required | Max 30 chars | Source marketing system code |
| `campaignName` | String | Required | Max 200 chars | Campaign name |
| `campaignStartDate` | LocalDate | Required | Valid date (VR-126) | Campaign start date |
| `campaignEndDate` | LocalDate | Required | On or after start date | Campaign end date |
| `channel` | String | Optional | Enum: `B2B`, `B2C`, `ALL` | Target channel |
| `correlationId` | String | Optional | Max 100 chars | Integration correlation identifier |
| `allocationLines` | Array\<CampaignAllocationImportLineDto\> | Required | Min 1 line | Planned stock allocations |

**`CampaignAllocationImportLineDto`**

| Field | Type | Required | Validation Rules | Description |
|-------|------|----------|------------------|-------------|
| `sku` | ProductSku | Required | Active product | Campaign product |
| `locationCode` | LocationCode | Required | Active location | Allocation location |
| `targetQuantity` | PositiveQuantityDto | Required | Min exclusive 0 (VR-126) | Target promotional quantity |

---

## Request DTO Index

| API ID | DTO Name | HTTP Method | Has Body |
|--------|----------|-------------|----------|
| API-001 | `CreateProductRequest` | POST | Yes |
| API-002 | `SearchProductsQuery` | GET | No |
| API-003 | `GetProductBySkuRequest` | GET | No |
| API-004 | `UpdateProductAttributesRequest` | PATCH | Yes |
| API-005 | `ChangeProductLifecycleStatusRequest` | POST | Yes |
| API-006 | `AssignAbcClassificationRequest` | PUT | Yes |
| API-007 | `ValidateProductEligibilityQuery` | GET | No |
| API-008 | `ListProductsByCategoryQuery` | GET | No |
| API-009 | `ResolveDuplicateProductConflictRequest` | POST | Yes |
| API-010 | `BulkProductImportRequest` | POST | Yes |
| API-011 – API-178 | *(see sections above)* | — | — |

**Total APIs documented:** 178  
**Total shared nested DTOs:** 12  
**Validation rules referenced:** VR-001 through VR-162 (SRS-VR-001)

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Backend Architect | | | |
| Solution Architect | | | |
| Senior Business Analyst | | | |
| Product Owner | | | |

---

*End of Request DTO Specification*

*Document ID: SRS-API-002 | Version 1.0 | July 6, 2026*
