# Request DTO Validation Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-004 |
| **Document Title** | Request DTO Validation Specification |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Backend Architect |
| **Source Documents** | SRS-API-002 (Request DTOs), SRS-VR-001 (Validation Rules), SRS-BR-001 (Business Rules) |
| **Date** | July 6, 2026 |
| **Scope** | Input validation for all Request DTOs — success-path only; error contract is RFC 7807 |

### Purpose

Defines **enforceable validation** for every Request DTO field across all 178 REST APIs. Each constraint is classified as required, length, format, business, or cross-field validation and traced to **BR-xxx** (business rule) and/or **VR-xxx** (validation rule).

### Coverage Summary

| Module | API Range | DTOs | Validation Depth |
|--------|-----------|------|------------------|
| M-01 Product Catalog | API-001 – API-010 | 10 | Field matrix + profiles |
| M-02 Warehouse Network | API-011 – API-021 | 11 | Field matrix + profiles |
| M-03 Inventory Governance | API-022 – API-031 | 10 | Validation profiles |
| M-04 Inventory Balance | API-032 – API-048 | 17 | Validation profiles |
| M-05 Procurement & Supplier | API-049 – API-065 | 17 | Validation profiles |
| M-06 Inbound Receiving | API-066 – API-080 | 15 | Validation profiles |
| M-07 Order Fulfillment | API-081 – API-097 | 17 | Validation profiles |
| M-08 Network Transfer | API-098 – API-107 | 10 | Validation profiles |
| M-09 Inventory Accuracy | API-108 – API-123 | 16 | Validation profiles |
| M-10 Returns Management | API-124 – API-131 | 8 | Validation profiles |
| M-11 Commercial Campaign | API-132 – API-139 | 8 | Validation profiles |
| M-12 Identity & Access | API-140 – API-149 | 10 | Validation profiles |
| M-13 Inventory Intelligence | API-150 – API-172 | 23 | Query validation profiles |
| Platform & Integration | API-173 – API-178 | 6 | Validation profiles |
| **Total** | **API-001 – API-178** | **178** | — |

### Validation Execution Layers

| Layer | Responsibility | Examples |
|-------|----------------|----------|
| **L1 — Structural** | Required, length, format, enum | `@NotBlank`, `@Size`, `@Pattern`, `@DecimalMin` |
| **L2 — Referential** | FK existence, catalog lookup | Product exists, location active |
| **L3 — Business** | Domain invariants, BR enforcement | ATP check, SoD check, freeze guard |
| **L4 — Cross-field** | Multi-field logic | `startDate ≤ endDate`, PO **or** ad-hoc auth |

L1–L2 run at API/presentation boundary; L3–L4 run in application/domain services.

### Validation Matrix Legend

| Column | Meaning |
|--------|---------|
| **Req** | `R`=Required, `O`=Optional, `C`=Conditional |
| **Length** | Max/min character or numeric bounds |
| **Format** | Pattern, enum, ISO type |
| **Business Validation** | L2/L3 domain checks |
| **Cross-Field** | L4 dependencies |
| **BR** | Business rule ID(s) |
| **VR** | Validation rule ID(s) |

---

## Shared Primitive Validation

| Primitive | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-----------|-----|--------|--------|---------------------|-------------|----|----|
| `ProductSku` | R when present | 1–50 chars | `^[A-Z0-9][A-Z0-9_-]*$` | Must exist in catalog when mutating stock | — | — | VR-001, VR-002, VR-007 |
| `LocationCode` | R when present | 1–30 chars | `^[A-Z0-9][A-Z0-9_-]*$` | Must exist; user location scope; not frozen for mutations | — | BR-024 | VR-011, VR-012, VR-053 |
| `SupplierCode` | R when present | 1–30 chars | `^[A-Z0-9][A-Z0-9_-]*$` | Must exist; active for new PO | — | — | VR-030 |
| `ReasonCode` | R when present | 1–20 chars | `^[A-Z0-9_]+$` | Must be active; applicable to transaction type | — | BR-020 | VR-026, VR-027 |
| `Quantity.amount` | R | scale ≤4 | decimal ≥0 | Must not exceed on-hand for decreases | `unitOfMeasure` required | — | VR-018, VR-023, VR-070 |
| `PositiveQuantity.amount` | R | scale ≤4 | decimal >0 | Must not exceed ATP/reservation/PO open qty per context | `unitOfMeasure` required | BR-001, BR-002 | VR-032, VR-035, VR-066 |
| `CurrencyCode` | R when present | exactly 3 | `^[A-Z]{3}$` ISO 4217 | Must match org or supplier currency policy | — | — | — |
| `LocalDate` | R when present | — | ISO `YYYY-MM-DD` | Not unreasonably past for delivery schedules | ≤ paired end date | — | VR-033, VR-062 |
| `Instant` | R when present | — | ISO-8601 UTC | Future when used as expiry | — | — | — |
| `Uuid` | R when present | 36 chars | RFC 4122 | Referenced entity must exist | — | — | — |
| `AbcClass` | R when present | 1 char | enum `A`,`B`,`C` | Product must exist | — | BR-032 | VR-021 |
| `LifecycleStatus` | R when present | — | enum `ACTIVE`,`INACTIVE`,`DISCONTINUED` | Valid state transition | — | BR-027 | VR-004–VR-006 |
| `PageNumber` | O | — | integer ≥1 | default 1 | — | — | — |
| `PageSize` | O | — | integer 1–100 | default 20 | — | — | — |

---

## Shared Nested DTO Validation

### `QuantityDto`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `amount` | R | scale ≤4 | decimal ≥0 | Context-specific ceiling | — | — | VR-018 |
| `unitOfMeasure` | R | 1–10 | alphanumeric | Must match product primary UoM or approved alternate | Both required together | — | VR-001 |

### `PositiveQuantityDto`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `amount` | R | scale ≤4 | decimal >0 | ≤ ATP, reservation, PO remaining per API | — | BR-001, BR-002 | VR-032, VR-092 |
| `unitOfMeasure` | R | 1–10 | alphanumeric | Match product UoM | Required with amount | — | VR-001 |

### `LotIdentityDto`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `lotNumber` | R | 1–50 | non-blank | Required only for traceable products | — | BR-017 | — |
| `expirationDate` | O | — | ISO date | Required for shelf-life products at receipt | ≤ product shelf policy | BR-014, BR-016 | VR-035 |

### `ShelfLifeProfileDto`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `expirationDate` | R | — | ISO date | Remaining life ≥ MRSL threshold | `manufactureDate ≤ expirationDate` | BR-016 | VR-035 |
| `manufactureDate` | O | — | ISO date | On or before expiration | — | — | — |
| `remainingShelfLifeDays` | O | — | integer ≥0 | Must meet MRSL when shelf-life managed | Computed from dates if omitted | BR-016 | — |

### `MonetaryAmountDto`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `amount` | R | scale 2 | decimal ≥0 | Used for approval threshold evaluation | `currencyCode` required | BR-021 | VR-082 |
| `currencyCode` | R | 3 | ISO 4217 | Match PO/invoice currency | Required with amount | BR-008 | — |

### `RoleAssignmentDto`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `roleCode` | R | 1–50 | known role enum | Must not create SoD conflict | — | BR-019, BR-021 | VR-083 |
| `locationCodes[]` | O | each 1–30 | LocationCode | Each location active; user admin scope | — | — | VR-008 |
| `effectiveFrom` | O | — | ISO date | default today | `effectiveTo ≥ effectiveFrom` | — | — |
| `effectiveTo` | O | — | ISO date | Future end optional | ≥ `effectiveFrom` | — | — |

### `PaginationQuery` / `DateRangeQuery`

| DTO | Cross-Field | BR | VR |
|-----|-------------|----|----|
| `PaginationQuery` | `sortDirection` required when `sortBy` set | — | — |
| `DateRangeQuery` | `startDate ≤ endDate`; max range 365 days for exports | — | VR-062, VR-153 |

---

## M-01 — Product Catalog

### API-001 — `CreateProductRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `sku` | R | 1–50 | ProductSku pattern | Unique across catalog | — | — | VR-001, VR-002, VR-009 |
| `name` | R | 1–200 | non-blank | — | — | — | VR-001 |
| `description` | O | 0–2000 | text | — | — | — | — |
| `unitOfMeasure` | R | 1–10 | non-blank | Valid UoM code in reference data | — | — | VR-001 |
| `categoryCode` | O | 1–30 | alphanumeric | Category exists if provided | — | — | — |
| `barcode` | O | 1–50 | — | No duplicate barcode (VR-009) | — | — | VR-009 |
| `isTraceable` | O | — | boolean | default false | If true → `rotationPolicy` R | BR-017 | — |
| `rotationPolicy` | C | — | `FIFO`,`FEFO` | Required for traceable | Required when `isTraceable=true` | BR-014, BR-015 | — |
| `shelfLifeManaged` | O | — | boolean | default false | If true → `mrslThresholdDays` R | BR-016 | — |
| `mrslThresholdDays` | C | — | integer ≥1 | — | Required when `shelfLifeManaged=true` | BR-016 | — |

**Cross-field:** (`isTraceable=true` → `rotationPolicy` required); (`shelfLifeManaged=true` → `mrslThresholdDays` required).  
**Business rules:** BR-014, BR-015, BR-016, BR-017 (traceability attributes at catalog definition).

---

### API-002 — `SearchProductsQuery`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `name` | O | 1–200 | partial match | — | — | — | VR-054 |
| `sku` | O | 1–50 | ProductSku | — | — | — | VR-007 |
| `categoryCode` | O | 1–30 | — | — | — | — | — |
| `lifecycleStatus` | O | — | LifecycleStatus enum | — | — | BR-027 | — |
| `abcClass` | O | 1 | AbcClass enum | — | — | BR-032 | VR-021 |
| `barcode` | O | 1–50 | — | — | — | — | VR-007 |
| `page`,`pageSize`,`sortBy`,`sortDirection` | O | per PaginationQuery | — | — | sort pair rule | — | — |

---

### API-003 — `GetProductBySkuRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `sku` (path) | R | 1–50 | ProductSku | Product must exist | — | — | VR-007 |

---

### API-004 — `UpdateProductAttributesRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `sku` (path) | R | 1–50 | ProductSku | Product exists | — | — | VR-007 |
| body fields | O* | per API-001 | — | At least one field present | Traceability cross-rules same as API-001 | BR-014–BR-017 | VR-003 |

**Cross-field:** At least one mutable field required; traceability rules mirror API-001.

---

### API-005 — `ChangeProductLifecycleStatusRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `sku` (path) | R | 1–50 | ProductSku | Product exists | — | — | VR-007 |
| `newStatus` | R | — | LifecycleStatus | Valid transition; audit attribution | — | BR-027 | VR-004, VR-005 |
| `reason` | O | 0–500 | text | — | — | — | VR-005 |
| `effectiveDate` | O | — | ISO date | default today | — | — | VR-005 |

**Business validation:** `DISCONTINUED` blocks new PO/requisition (BR-027). Status change records user+date (VR-005).

---

### API-006 — `AssignAbcClassificationRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `sku` (path) | R | 1–50 | ProductSku | Product exists, not invalid ref | — | BR-032 | VR-021, VR-022 |
| `abcClass` | R | 1 | `A`,`B`,`C` | — | — | BR-032 | VR-021 |
| `classificationBasis` | O | 1–100 | enum basis | — | — | BR-032 | — |
| `effectiveDate` | O | — | ISO date | default today | — | — | — |

---

### API-007 — `ValidateProductEligibilityQuery`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `sku` (path) | R | 1–50 | ProductSku | Product exists | — | — | VR-007 |
| `transactionType` | R | — | enum | Evaluated per type | Location R for location-scoped types | BR-027 | VR-004, VR-006 |
| `locationCode` | C | 1–30 | LocationCode | User scope | Required for RESERVATION/FULFILLMENT | — | VR-008 |

---

### API-008 — `ListProductsByCategoryQuery`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `categoryCode` (path) | R | 1–30 | — | Category exists | — | — | — |
| `lifecycleStatus` | O | — | enum | — | — | — | — |
| pagination | O | per PaginationQuery | — | — | — | — | — |

---

### API-009 — `ResolveDuplicateProductConflictRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `resolutionAction` | R | — | `MERGE`,`REJECT_NEW`,`KEEP_BOTH` | Authorized role | — | — | VR-009, VR-010 |
| `sourceSku` | R | 1–50 | ProductSku | Exists | — | — | VR-009 |
| `targetSku` | C | 1–50 | ProductSku | Exists | Required if `MERGE` | — | VR-010 |
| `mergeAuthorizationReference` | C | 1–100 | — | Inventory Controller approval | Required if both SKUs have on-hand | — | VR-010 |
| `notes` | O | 0–1000 | — | — | — | — | — |

---

### API-010 — `BulkProductImportRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `importMode` | R | — | `VALIDATE_ONLY`,`UPSERT`,`CREATE_ONLY` | — | — | — | — |
| `sourceReference` | O | 0–100 | — | — | — | — | — |
| `products[]` | R | 1–5000 items | array | Each line validates as API-001 | Unique SKU within batch | BR-014–BR-017 | VR-001, VR-002 |

**`BulkProductLineDto`:** same rules as API-001 per line.

---

## M-02 — Warehouse Network

### API-011 — `CreateInventoryLocationRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `locationCode` | R | 1–30 | LocationCode | Unique | — | — | VR-011 |
| `name` | R | 1–200 | non-blank | — | — | — | VR-011 |
| `locationType` | R | — | location type enum | — | — | — | VR-011 |
| `operationalStatus` | R | — | status enum | — | — | — | VR-011 |
| `parentLocationCode` | O | 1–30 | LocationCode | Parent exists; no circular hierarchy | ≠ `locationCode` | — | VR-014, VR-015 |
| address fields | O | per AddressDto | — | — | — | — | — |
| `plannedGoLiveDate` | O | — | ISO date | — | — | — | — |

---

### API-012 — `ListActiveLocationsQuery`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| filters | O | per field | enums | User location scope on results | — | — | VR-053, VR-061 |
| pagination | O | PaginationQuery | — | — | — | — | — |

---

### API-013 to API-014 — Location read/update

| DTO | Key business validation | BR | VR |
|-----|-------------------------|----|----|
| `GetLocationByCodeRequest` | Location exists; user scope | — | VR-053 |
| `UpdateLocationHierarchyRequest` | No self/ancestor parent (VR-014); single parent | — | VR-014, VR-015 |

---

### API-015 — `ConfigureStoragePositionRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `locationCode` (path) | R | 1–30 | LocationCode | Location active | — | BR-024 | VR-012 |
| `positionCode` | R | 1–30 | unique per location | — | — | — | — |
| `zone`,`aisle`,`bin` | O | 1–30 each | — | — | — | — | — |
| `positionType` | O | — | position enum | — | — | — | — |
| `isActive` | O | — | boolean | default true | — | — | — |

---

### API-016 — `GetStoragePositionsQuery`

Pagination + location scope; `locationCode` path required.

---

### API-017 — `ActivateInventoryLocationRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `locationCode` (path) | R | 1–30 | LocationCode | Opening balance approved when policy applies | `openingBalanceApprovalReference` C | — | VR-013, VR-025 |
| `openingBalanceApprovalReference` | C | 1–100 | — | Valid approval record | Required per go-live policy | — | VR-025 |
| `activationDate` | O | — | ISO date | — | — | — | — |

---

### API-018 — `DeactivateInventoryLocationRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `locationCode` (path) | R | 1–30 | LocationCode | No new transactions after deactivation | — | — | VR-012, VR-017 |
| `reason` | R | 1–500 | non-blank | — | — | — | — |

---

### API-019 — `CloseInventoryLocationRequest`

| Field | Req | Length | Format | Business Validation | Cross-Field | BR | VR |
|-------|-----|--------|--------|---------------------|-------------|----|----|
| `locationCode` (path) | R | 1–30 | LocationCode | No on-hand unless disposition | `dispositionPlanReference` OR `closureWaiverReference` when stock remains | — | VR-016 |
| `dispositionPlanReference` | C | 1–100 | — | Valid plan | Required if on-hand > 0 | — | VR-016 |
| `closureWaiverReference` | C | 1–100 | — | Executive waiver | Alternative to disposition plan | — | VR-016 |

---

### API-020 / API-021 — Freeze and operational status

Path-only `locationCode` (R, LocationCode, exists, user scope). No body validation.

---

## M-03 — Inventory Governance

### API-022 — `CreateReasonCodeRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `code`, `description`, `transactionTypes` (min 1) | BR-020 | VR-026 |
| **Length** | `code` 1–20; `description` 1–200 | — | — |
| **Format** | `code` uppercase alphanumeric+underscore; `transactionTypes[]` ∈ {`ADJUSTMENT`,`WRITE_OFF`,`RECEIPT_DISCREPANCY`,`RETURN`,`TRANSFER_EXCEPTION`,`FULFILLMENT_EXCEPTION`} | — | VR-027 |
| **Business** | `code` unique; `isActive` default true | BR-020 | VR-026 |
| **Cross-field** | — | — | — |

### API-023 — `GetActiveReasonCodesQuery`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | None (all optional) | — | — |
| **Length** | Pagination per shared | — | — |
| **Format** | `transactionType` valid enum; `isActive` boolean | — | VR-026 |
| **Business** | Default `isActive=true` | — | — |
| **Cross-field** | — | — | — |

### API-024 — `RetireReasonCodeRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `code` (path) | — | VR-026 |
| **Length** | `retirementReason` 0–500 | — | — |
| **Format** | `code` ReasonCode; `effectiveDate` ISO date | — | — |
| **Business** | Code exists and active; retired codes blocked for new transactions | BR-020 | VR-027 |
| **Cross-field** | — | — | — |

### API-025 — `ValidateReasonCodeQuery`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `code` (path), `transactionType` | BR-020 | VR-026 |
| **Format** | `transactionType` valid enum | — | VR-026, VR-027 |
| **Business** | Code active and applicable to transaction type | BR-020 | VR-027 |

### API-026 — `PublishGovernancePolicyRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `policyName`, `effectiveFrom`, `parameters` (min 1) | — | VR-028 |
| **Length** | `policyName` 1–100; `description` 0–1000; param key 1–50; value 1–500 | — | — |
| **Format** | `effectiveFrom`/`effectiveTo` ISO instant; `parameterType` enum | — | VR-028 |
| **Business** | No overlapping effective policy version | — | VR-028 |
| **Cross-field** | `effectiveTo` > `effectiveFrom` when provided | — | VR-028 |

### API-027 — `UpdateApprovalThresholdRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `policyId` (path), `transactionType`, `effectiveFrom`; at least one threshold | BR-021 | VR-020, VR-082 |
| **Length** | — | — | — |
| **Format** | `transactionType` ∈ {`ADJUSTMENT`,`WRITE_OFF`,`TRANSFER`,`REQUISITION`}; thresholds ≥0 | — | VR-082 |
| **Business** | Policy exists; threshold drives independent approval | BR-021 | VR-082 |
| **Cross-field** | At least one of `quantityThreshold` or `monetaryThreshold` | BR-021 | — |

### API-028 — `UpdateReceiptToleranceRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `policyId` (path), `effectiveFrom` | BR-006 | VR-048 |
| **Format** | `quantityTolerancePercent` 0–100; absolutes ≥0 | — | VR-048 |
| **Business** | Tolerance governs auto-accept of receipt variances | BR-006 | VR-048 |
| **Cross-field** | At least one tolerance field when amending | — | — |

### API-029 / API-030 — Threshold/tolerance queries

| DTO | Required | Business | BR | VR |
|-----|----------|----------|----|----|
| `GetEffectiveApprovalThresholdQuery` | `transactionType` | User location scope | BR-021 | VR-082 |
| `GetReceiptToleranceQuery` | None | User location scope; supplier exists if provided | BR-006 | VR-048 |

### API-031 — `EvaluateSegregationOfDutiesRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `initiatorUserId`, `approverUserId`, `transactionType` | BR-019, BR-021 | VR-075, VR-083 |
| **Length** | User IDs 1–50; `transactionReference` 0–100 | — | — |
| **Format** | `transactionType` ∈ {`COUNT_VARIANCE_APPROVAL`,`ADJUSTMENT_APPROVAL`,`WRITE_OFF_APPROVAL`,`ROLE_ASSIGNMENT`} | — | VR-083 |
| **Business** | Both users exist; approver ≠ initiator | BR-019, BR-021 | VR-075, VR-083 |
| **Cross-field** | `approverUserId` ≠ `initiatorUserId` | BR-019 | VR-075 |

---

## M-04 — Inventory Balance

### API-032 — `EstablishOpeningBalancesRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `locationCode`, `balanceLines` (min 1); `approvalReference` conditional | — | VR-024, VR-025 |
| **Business** | Location `PLANNED`/pre-activation; SKU exists; lot required if traceable | BR-017 | VR-024, VR-025 |
| **Cross-field** | `approvalReference` required before activation policy | — | VR-025 |

**`OpeningBalanceLineDto`:** `sku` R; `quantity` R (≥0); `lotIdentity` C if traceable; `ownershipType` enum default `OWNED` (BR-031).

### API-033 — `GetStockPositionsQuery`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | At least one of `sku` or `locationCode` | — | VR-054 |
| **Business** | User location scope on `locationCode` | — | VR-053 |
| **Cross-field** | `sku` OR `locationCode` required | — | VR-054 |

### API-034 to API-037 — Stock read APIs

| API | DTO | Required | Business | BR | VR |
|-----|-----|----------|----------|----|----|
| API-034 | `GetStockPositionRequest` | `locationCode`, `sku` (path) | User scope; SKU exists | — | VR-053, VR-054 |
| API-035 | `GetAvailabilityBySkuQuery` | `sku` (path), `locationCode` (query) | ATP inquiry scope | BR-001 | VR-055 |
| API-036 | `GetNetworkAvailabilityQuery` | `sku` (path) | Authorized locations only; quarantine excluded default | BR-001, BR-013 | VR-056, VR-064 |
| API-037 | `GetStockStatusIndicatorRequest` | `locationCode`, `sku` (path) | Stock policy must exist | BR-009, BR-010 | VR-059 |

### API-038 — `DefineStockPolicyRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `locationCode`, `sku`, `reorderLevel`, `minimumThreshold`, `safetyStock`, `effectiveFrom` | BR-009, BR-010 | VR-018–VR-020 |
| **Format** | Thresholds ≥0; `maximumThreshold` ≥ `reorderLevel` when set | BR-009 | VR-019 |
| **Business** | Active location and product | BR-009, BR-010 | VR-018 |
| **Cross-field** | `minimumThreshold` ≤ `reorderLevel` unless inverted policy documented | BR-010 | VR-019 |

### API-039 — `GetStockPolicyRequest`

Path params R; `asOfDate` O (default today). Business: policy lookup effective date (VR-020).

### API-040 — `UpdateStockPolicyRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `locationCode`, `sku` (path), `effectiveFrom`; ≥1 threshold field | BR-009, BR-010 | VR-018–VR-020 |
| **Cross-field** | At least one threshold field; same ordering rules as API-038 | BR-009, BR-010 | VR-019 |

### API-041 — `GetLotBreakdownRequest`

Path `locationCode`, `sku` R; product traceable; `includeQuarantined` default false (BR-013, BR-017).

### API-042 — `EvaluateSourceTransferCapacityQuery`

Path params R; `requestedQuantity` O ≥0; evaluated against max transferable spare (BR-012, VR-140).

### API-043 — `ReserveStockRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `locationCode`, `sku`, `quantity`, `orderId`, `orderLineId` | BR-002 | VR-092–VR-094 |
| **Length** | `orderId`, `orderLineId` 1–50 | — | VR-093 |
| **Business** | Location active, not frozen; product active; qty ≤ ATP; safety stock protected | BR-001, BR-002, BR-010 | VR-006, VR-092, VR-094 |
| **Cross-field** | `safetyStockExceptionReference` required when breaching safety stock | BR-010 | VR-124, VR-125 |

### API-044 — `ReleaseReservationRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | path params, `releaseReason` | — | VR-095, VR-096 |
| **Business** | Reservation exists; release qty ≤ reserved | — | VR-095 |
| **Format** | `releaseReason` enum | — | VR-096 |

### API-045 — `ApplyQuarantineHoldRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `quantity`, `holdReason`, `reasonCode`; `lotIdentity` if traceable | BR-013, BR-030 | VR-026, VR-084 |
| **Business** | Qty ≤ on-hand; hold excludes from sellable ATP | BR-013 | VR-084, VR-056 |
| **Format** | `holdReason` ∈ {`QUALITY`,`RECALL`,`CUSTOMS`,`BONDED`,`INVESTIGATION`} | BR-030 | — |

### API-046 — `ReleaseQuarantineHoldRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | path params, `disposition`, `reasonCode` | BR-013, BR-026 | VR-085 |
| **Cross-field** | `inspectionOutcomeReference` required when `disposition=RESTORE_TO_SELLABLE` | BR-026 | VR-085 |

### API-047 — `TransferConsignmentOwnershipRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `quantity`, `consumptionReference`; `lotIdentity` if traceable | BR-031 | — |
| **Length** | `consumptionReference` 1–100 | — | — |
| **Business** | Stock must be consignment; qty ≤ consignment on-hand | BR-031 | — |

### API-048 — `SegregatePromotionalStockRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `campaignId`, `allocationId`, `quantity` | BR-029 | VR-127 |
| **Business** | Valid allocation; qty ≤ ATP at allocation time | BR-029 | VR-127 |

---

## M-05 — Procurement & Supplier

### API-049 — `RegisterSupplierRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `supplierCode`, `name`, `paymentTermsDays` | — | VR-030 |
| **Length** | `supplierCode` 1–30; `name` 1–200; email 0–254; phone 0–30 | — | — |
| **Format** | `supplierCode` pattern; email RFC; `currencyCode` ISO 4217 | — | — |
| **Business** | `supplierCode` unique; `isConsignment` flags consignment agreement | BR-031 | VR-030 |

### API-050 to API-053 — Supplier read/update/deactivate

| API | Key validation | BR | VR |
|-----|----------------|----|----|
| API-050 | Query filters; pagination | — | — |
| API-051 | `supplierCode` exists (path) | — | VR-030 |
| API-052 | ≥1 body field; email format | — | — |
| API-053 | `reason` R 1–500; no open POs unless policy | — | VR-030 |

### API-054 — `CreatePurchaseRequisitionRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `receivingLocationCode`, `justification`, `lines` (min 1) | BR-011, BR-027 | VR-117, VR-119, VR-120 |
| **Length** | `justification` 1–1000 | — | VR-119 |
| **Business** | Active location; SKU active, not discontinued | BR-027 | VR-006, VR-120 |
| **Cross-field** | Each line: `quantity` > 0 | — | VR-117 |

### API-055 — `GetPurchaseRequisitionRequest`

`requisitionId` (path) R; must exist.

### API-056 — `ApprovePurchaseRequisitionRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `requisitionId` (path); status submitted | BR-011 | VR-118 |
| **Cross-field** | `networkTransferDeclineReason` required when `networkTransferDeclined=true` | BR-011 | VR-118 |

### API-057 — `RejectPurchaseRequisitionRequest`

`requisitionId` R; `rejectionReason` R 1–1000 (VR-131).

### API-058 — `ConvertRequisitionToPurchaseOrderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `requisitionId`, `supplierCode`, `expectedDeliveryDate` | BR-007, BR-027 | VR-030, VR-033 |
| **Business** | Requisition approved; supplier active | BR-007 | VR-030 |
| **Cross-field** | Line override qty ≤ requisition line qty | — | VR-117 |

### API-059 — `PlacePurchaseOrderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `supplierCode`, `receivingLocationCode`, `expectedDeliveryDate`, `lines` (min 1) | BR-007, BR-027 | VR-030–VR-033 |
| **Business** | Supplier/location active; SKU not discontinued | BR-027 | VR-006, VR-031 |
| **Cross-field** | Each line `orderedQuantity` > 0 | — | VR-032 |

### API-060 — `ListOpenPurchaseOrdersQuery`

Date range cross-field; user location scope (VR-034); overdue filter (VR-123).

### API-061 — `GetPurchaseOrderRequest`

`purchaseOrderId` (path) R; exists.

### API-062 — `AmendPurchaseOrderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `purchaseOrderId`, `amendmentReason` | — | VR-050, VR-051 |
| **Length** | `amendmentReason` 1–1000 | — | — |
| **Business** | Authorized user; amended qty ≥ received qty | — | VR-050, VR-051 |

### API-063 — `CancelPurchaseOrderRequest`

`purchaseOrderId` R; `cancellationReason` R 1–1000; authorized user (VR-051).

### API-064 — `ScheduleInboundDeliveryRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `purchaseOrderId`, `expectedArrivalDate` | — | VR-033 |
| **Business** | PO open | — | — |
| **Cross-field** | Line `expectedQuantity` ≤ remaining open qty | — | VR-050 |

### API-065 — `ValidatePoForReceiptQuery`

`purchaseOrderId` R; `receivingLocationCode` must match PO when provided (BR-007, VR-040).

---

## M-06 — Inbound Receiving

### API-066 — `CreateGoodsReceiptRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `receivingLocationCode`; `purchaseOrderId` OR ad-hoc auth (via separate API) | BR-007 | VR-040, VR-012 |
| **Business** | Location active, not frozen; PO valid when provided | BR-007 | VR-040 |
| **Cross-field** | `supplierCode` must match PO supplier when PO set | BR-007 | VR-036 |

### API-067 — `ListGoodsReceiptsQuery`

Date range cross-field; user location scope (VR-034).

### API-068 — `GetGoodsReceiptRequest`

`goodsReceiptId` (path) R; exists.

### API-069 — `VerifyGoodsReceiptRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `lines` (min 1) per line: `lineId`, `sku`, `acceptedQuantity` | BR-004, BR-016, BR-017 | VR-035–VR-037 |
| **Business** | SKU matches PO; MRSL check for shelf-life; lot if traceable | BR-004, BR-016, BR-017 | VR-035, VR-036 |
| **Cross-field** | `acceptedQuantity` + `rejectedQuantity` ≤ physically verified | BR-004 | VR-037 |

### API-070 — `RecordReceiptDiscrepancyRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `lineId`, `discrepancyType`, `varianceQuantity`, `reasonCode`, `notes` | BR-006 | VR-038, VR-026 |
| **Length** | `notes` 1–2000; `evidenceReference` 0–200 | BR-006 | VR-038 |
| **Business** | Document before acceptance | BR-006 | VR-038 |

### API-071 — `ListReceiptDiscrepanciesQuery`

`goodsReceiptId` (path) R; `status` enum optional.

### API-072 — `ResolveReceiptDiscrepancyRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | path params, `resolutionOutcome`, `resolutionNotes` | BR-006 | VR-038 |
| **Length** | `resolutionNotes` 1–2000 | — | — |
| **Business** | Discrepancy open | BR-006 | — |

### API-073 — `CompletePutAwayRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `putAwayLines` (min 1): `receiptLineId`, `quantity`, `storagePositionCode` | BR-005 | VR-043 |
| **Business** | Receipt verified; position exists; ATP increases only after put-away | BR-005 | VR-043 |
| **Cross-field** | Put-away qty ≤ remaining unplaced per line | BR-005 | VR-043 |

### API-074 — `ListPendingPutAwayQuery`

`locationCode` R; user scope.

### API-075 — `ReceiveAdHocInboundRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `receivingLocationCode`, `adHocAuthorizationReference`, `reasonCode`, `sourceDescription`, `lines` | BR-007 | VR-042, VR-026 |
| **Length** | `adHocAuthorizationReference` 1–100; `sourceDescription` 1–500 | — | VR-042 |
| **Business** | Governed exception to PO requirement | BR-007 | VR-042 |

### API-076 — `ReceiveReturnInboundRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `returnAuthorizationId`, `receivingLocationCode`, `lines` | BR-025 | VR-045, VR-046 |
| **Business** | Valid open RMA; qty ≤ authorized | BR-025 | VR-145, VR-046 |

### API-077 — `RegisterSupplierInvoiceRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `supplierCode`, `invoiceNumber`, `invoiceDate`, `purchaseOrderId`, `currencyCode`, `lines` | BR-008 | — |
| **Length** | `invoiceNumber` 1–50 unique per supplier | — | — |
| **Business** | PO linked to supplier; lines match PO/receipt | BR-008 | — |

### API-078 — `GetSupplierInvoiceRequest`

`invoiceId` (path) R; exists.

### API-079 — `PerformThreeWayMatchRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `invoiceId` (path) | BR-008 | VR-048 |
| **Business** | Match PO–receipt–invoice; tolerance override authorized when exceeded | BR-008 | VR-048 |

### API-080 — `AuthorizeInvoicePaymentRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `invoiceId` (path) | BR-008 | — |
| **Business** | Three-way match completed | BR-008 | — |
| **Cross-field** | `paymentDueDate` ≥ `invoiceDate` | — | — |

---

## M-07 — Order Fulfillment

### API-081 — `CreateCustomerOrderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `channel`, `lines` (min 1); per line: `lineNumber`, `sku`, `requestedQuantity` | — | VR-006 |
| **Format** | `channel` ∈ {`B2B`,`B2C`,`INTERNAL`,`MARKETPLACE`} | — | — |
| **Business** | SKU active | — | VR-006 |

### API-082 — `ListCustomerOrdersQuery`

Date range cross-field; user location scope on `shipFromLocationCode`.

### API-083 — `GetCustomerOrderRequest`

`orderId` (path) R; exists (VR-108).

### API-084 — `ConfirmOrderAvailabilityRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `orderId` (path) | BR-001 | VR-090, VR-091 |
| **Business** | ATP-based availability; optional inbound supply flag | BR-001 | VR-090, VR-091 |

### API-085 — `ConfirmCustomerOrderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `orderId` (path) | BR-002 | VR-092 |
| **Business** | Availability confirmed; creates reservation | BR-001, BR-002 | VR-092 |
| **Cross-field** | `safetyStockExceptionReference` when breaching safety stock | BR-010 | VR-124 |

### API-086 — `CancelCustomerOrderRequest`

`orderId` R; `cancellationReason` R 1–1000 (VR-096); `lineIds` must exist on order.

### API-087 — `CreateMultiLocationFulfillmentPlanRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `allocations` (min 1) | BR-001 | VR-106, VR-107 |
| **Business** | Per-location ATP sufficient | BR-001 | VR-107 |
| **Cross-field** | Sum of allocations per line = line requested qty | — | VR-106 |

### API-088 — `AssignPickListRequest`

`orderId` R; order confirmed; `pickStrategy` default per product FIFO/FEFO (BR-014, BR-015).

### API-089 — `ListOrdersAwaitingPickQuery`

`orderId` (path) R; optional location scope.

### API-090 — `VerifyPickRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `pickLines` (min 1) | BR-003, BR-017 | VR-097–VR-099 |
| **Business** | Picked qty ≤ reserved; SKU match or approved substitute | BR-003 | VR-098, VR-110 |
| **Cross-field** | `substitutionReference` when SKU differs | — | VR-110, VR-111 |

### API-091 — `PackOrderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `packages` (min 1); each package `lineItems` (min 1) | BR-003 | — |
| **Cross-field** | Package line qty ≤ picked qty per order line | BR-003 | — |

### API-092 — `DispatchShipmentRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `shipmentLines` (min 1) | BR-003 | VR-097, VR-098 |
| **Business** | Pick verified; shipped qty ≤ picked/reserved | BR-003 | VR-097, VR-098 |
| **Cross-field** | Lot required if traceable | BR-017 | — |

### API-093 — `CompletePartialFulfillmentRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `fulfillmentLines`; `createBackorderForRemainder` | BR-028 | VR-100, VR-101 |
| **Cross-field** | `fulfillQuantity` > 0 and < full line; `customerAcknowledgmentReference` when backorder | BR-028 | VR-101 |

### API-094 — `RecordBackorderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `backorderLines`; `customerAcknowledgmentReference` per line | BR-028 | VR-101, VR-103 |
| **Business** | Backorder qty = unfulfilled remainder | BR-028 | VR-103 |

### API-095 — `FulfillBackorderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `backorderId` (path) | BR-028 | VR-102, VR-092 |
| **Business** | Backorder open; ATP sufficient | BR-001 | VR-092 |
| **Cross-field** | `priorityOverrideReference` when out of sequence | — | VR-102 |

### API-096 — `RaiseFulfillmentExceptionRequest`

`orderId` R; `exceptionType` R; `description` R 1–2000 (VR-104).

### API-097 — `GetOrderFulfillmentStatusRequest`

`orderId` (path) R; exists (VR-108).

---

## M-08 — Network Transfer

### API-098 — `RequestStockTransferRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `sourceLocationCode`, `destinationLocationCode`, `justification`, `lines` | BR-011, BR-012 | VR-128–VR-130 |
| **Length** | `justification` 1–1000 | — | VR-128 |
| **Business** | Qty ≤ source ATP; respects source minimum | BR-012 | VR-130, VR-140 |
| **Cross-field** | Source ≠ destination | — | VR-129 |

### API-099 — `ListStockTransfersQuery`

Date range cross-field; user location scope.

### API-100 — `GetStockTransferRequest`

`transferId` (path) R; exists.

### API-101 — `ApproveTransferRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `transferId` (path); status `REQUESTED` | BR-012 | VR-132, VR-141 |
| **Business** | Revalidated ATP; approved qty ≤ max transferable | BR-012 | VR-141 |

### API-102 — `RejectTransferRequest`

`transferId` R; `rejectionReason` R 1–1000 (VR-131).

### API-103 — `DispatchTransferRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `dispatchLines` (min 1) | — | VR-133 |
| **Business** | Status `APPROVED`; source not frozen; dispatched ≤ approved | — | VR-133 |

### API-104 — `ConfirmTransferReceiptRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `receiptLines` (min 1) | — | VR-134, VR-135 |
| **Business** | Status `IN_TRANSIT` | — | — |
| **Cross-field** | `varianceNotes` when received ≠ dispatched | BR-020 | VR-135 |

### API-105 — `CancelInTransitTransferRequest`

`transferId` R; `cancellationReason` R 1–1000; eligible status.

### API-106 / API-107 — Transfer list queries

User location scope (VR-136); overdue in-transit (VR-137).

---

## M-09 — Inventory Accuracy

### API-108 — `ScheduleCycleCountRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `locationCode`, `sku`, `scheduledDate` | BR-018, BR-032 | VR-067, VR-068 |
| **Business** | Active location/product; Class A default HIGH priority | BR-032 | VR-068 |

### API-109 — `ListCycleCountsQuery`

Date range cross-field; user scope.

### API-110 — `GetCycleCountAssignmentRequest`

`cycleCountId` R; response must not expose expected qty (BR-018, VR-069).

### API-111 — `SubmitCycleCountResultRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `physicalQuantity` | BR-018 | VR-070 |
| **Business** | Blind count submission; status scheduled/in-progress | BR-018 | VR-069 |

### API-112 — `InitiatePhysicalInventoryCountRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `locationCode`, `plannedStartDate`, `plannedEndDate` | BR-024 | VR-071 |
| **Cross-field** | `plannedEndDate` ≥ `plannedStartDate` | BR-024 | VR-071 |

### API-113 — `GetPhysicalCountStatusRequest`

`physicalCountId` (path) R.

### API-114 — `RecordPhysicalCountResultRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `countLines` (min 1) | BR-018, BR-024 | VR-070, VR-071 |
| **Business** | Location frozen during count | BR-024 | VR-071 |

### API-115 — `CertifyPhysicalInventoryCountRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `physicalCountId` (path) | BR-024 | VR-072 |
| **Business** | All SKUs counted before certification | BR-024 | VR-072 |

### API-116 — `OpenAdjustmentCaseRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `originType`, `locationCode`, `sku`, `reasonCode` | BR-020, BR-022 | VR-077, VR-079 |
| **Cross-field** | `varianceId` when `originType=COUNT_VARIANCE`; direction/qty for direct | BR-022 | VR-078 |

### API-117 — `GetAdjustmentCaseRequest`

`caseId` (path) R.

### API-118 — `InvestigateVarianceRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `rootCauseCategory`, `investigationFindings` | BR-022 | VR-076 |
| **Length** | `investigationFindings` 1–5000 | BR-022 | VR-076 |
| **Business** | Investigation before adjustment | BR-022 | VR-076 |

### API-119 — `ApproveCountVarianceRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | path params, `approvedAdjustmentQuantity` | BR-019 | VR-075 |
| **Business** | Approver ≠ counter | BR-019 | VR-075 |

### API-120 — `SubmitAdjustmentForApprovalRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `adjustmentType`, `quantity`, `reasonCode` | BR-020, BR-023 | VR-077, VR-080, VR-081 |
| **Cross-field** | `evidenceReference` for write-off; decrease ≤ on-hand | BR-023 | VR-080, VR-078 |

### API-121 — `ApproveAdjustmentRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `caseId` (path) | BR-021 | VR-083 |
| **Business** | Approver ≠ initiator and counter; independent approval | BR-019, BR-021 | VR-083, VR-075 |

### API-122 — `RejectAdjustmentRequest`

`caseId` R; `rejectionReason` R 1–2000.

### API-123 — `ListPendingApprovalsQuery`

User location scope; optional case type filter.

---

## M-10 — Returns Management

### API-124 — `IssueReturnAuthorizationRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `originalOrderId`, `returnReason`, `lines` | BR-025 | VR-142, VR-143 |
| **Length** | `returnReason` 1–500 | — | — |
| **Business** | Order return-eligible; authorized qty ≤ shipped | BR-025 | VR-143 |

### API-125 to API-127 — RMA list/get/cancel

| API | Key validation | BR | VR |
|-----|----------------|----|----|
| API-125 | Query filters | — | — |
| API-126 | `returnAuthorizationId` exists | BR-025 | VR-149 |
| API-127 | `cancellationReason` R 1–1000; open/unused RMA | — | — |

### API-128 — `ReceiveCustomerReturnRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `returnId`, `receivingLocationCode`, `receivedLines` | BR-025 | VR-144, VR-145, VR-046 |
| **Business** | SKU matches authorization; qty ≤ authorized | BR-025 | VR-145 |

### API-129 — `InspectReturnedGoodsRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `inspectionLines` (min 1) | BR-026 | VR-146 |
| **Business** | Inspect before restocking | BR-026 | VR-146 |

### API-130 — `DispositionReturnRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `dispositionAction`, `dispositionLines` | BR-023, BR-026 | VR-147, VR-148 |
| **Cross-field** | Sum disposition qty = inspected qty; `restockLocationCode` if RESTOCK; write-off refs if WRITE_OFF | BR-023, BR-026 | VR-147, VR-080 |

### API-131 — `ListPendingReturnReceiptsQuery`

Optional `locationCode`; user scope.

---

## M-11 — Commercial Campaign

### API-132 — `CreatePromotionalAllocationRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `campaignId`, `campaignName`, `locationCode`, `sku`, `allocatedQuantity`, `campaignStartDate`, `campaignEndDate` | BR-029 | VR-126, VR-127 |
| **Length** | `campaignId` 1–50; `campaignName` 1–200 | — | — |
| **Business** | Allocated qty ≤ ATP | BR-029 | VR-127 |
| **Cross-field** | `campaignEndDate` ≥ `campaignStartDate` | — | VR-126 |

### API-133 / API-134 — Allocation list/get

Standard query/path validation; user scope (BR-029).

### API-135 — `AmendPromotionalAllocationRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `allocationId`, `amendmentReason`; ≥1 amendable field | BR-029 | VR-127 |
| **Business** | Increased qty ≤ available ATP | BR-029 | VR-127 |

### API-136 — `EvaluateCampaignReadinessRequest`

`allocationId` R; `targetQuantity` defaults to allocated (VR-126).

### API-137 — `ReleasePromotionalAllocationRequest`

`allocationId` R; `releaseReason` R enum.

### API-138 — `AuthorizePromotionalOverrideRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `allocationId`, `orderId`, `overrideQuantity`, `authorizationReference`, `justification` | BR-029 | — |
| **Business** | Override qty ≤ ring-fenced remaining; commercial leadership auth | BR-029 | — |

### API-139 — `CheckRingFenceQuery`

Path `locationCode`, `sku` R; optional `asOfDate` (BR-029).

---

## M-12 — Identity & Access

### API-140 — `ProvisionUserAccountRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `userId`, `email`, `displayName`, `initialRoles` (min 1) | — | VR-083 |
| **Length** | `userId` 1–50; `email` 1–254; `displayName` 1–200 | — | — |
| **Format** | `userId` alphanumeric+underscore; valid email | — | — |
| **Business** | `userId` unique; no SoD in role set | — | VR-083 |

### API-141 to API-142 — User list/get

Standard pagination; `userId` exists for get.

### API-143 — `AssignRoleRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `userId` (path), `roleAssignment` | — | VR-083 |
| **Business** | Account active; no SoD conflict | — | VR-083 |

### API-144 — `RevokeRoleAssignmentRequest`

Path params R; assignment exists on user.

### API-145 — `SuspendUserAccountRequest`

`userId` R; `suspensionReason` R 1–1000; account active.

### API-146 — `DeactivateUserAccountRequest`

`userId` R; `deactivationReason` R 1–1000.

### API-147 — `SyncUsersFromDirectoryRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `syncMode` | — | — |
| **Format** | `syncMode` ∈ {`FULL`,`INCREMENTAL`} | — | — |
| **Cross-field** | `sinceTimestamp` required when `INCREMENTAL` | — | — |

### API-148 — `EvaluateAuthorizationRequest`

`action` R 1–100; optional user defaults to caller; location scope when provided (VR-008).

### API-149 — `ValidateLocationScopeRequest`

`locationCode` R; exists; user access check (VR-008, VR-053).

---

## M-13 — Inventory Intelligence (Read-Only)

All intelligence DTOs: path/query only. Common patterns:

| Pattern | Validation | BR | VR |
|---------|------------|----|----|
| Location scope | User authorized locations only | — | VR-151, VR-154 |
| Date range | `startDate` ≤ `endDate`; max 365 days for export | — | VR-062, VR-153 |
| Pagination | Shared `PaginationQuery` | — | — |
| Point-in-time | `asOfTimestamp` default latest projection | — | VR-152 |

### API-150 — `GetInventoryDashboardQuery`

| Cross-field | `locationCode` required when `scope=LOCATION` | VR-151 |

### API-151 to API-152 — Stock status summary/board

Optional location/category/ABC filters; authorized locations (VR-151).

### API-153 — `GetAvailabilityInquiryLogQuery`

Date range cross-field (VR-062); user/location scope.

### API-154 — `GetQuarantineRegisterQuery`

Hold reason enum; location scope (BR-013).

### API-155 — `SearchMovementHistoryQuery`

| Required | `startDate`, `endDate` |
| Cross-field | At least one filter recommended (VR-154) |

### API-156 — `QueryAuditTrailQuery`

`startDate`, `endDate` R; date range (VR-153).

### API-157 — `ExportAuditEvidenceQuery`

`startDate`, `endDate` R; max 365-day range; authorized locations (VR-153, VR-154).

### API-158 — `GetOperationalAlertsQuery`

Alert type/severity enums; location scope.

### API-159 — `AcknowledgeOperationalAlertRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `alertId` (path), `actionTaken` | BR-009 | VR-113, VR-115 |
| **Format** | `actionTaken` ∈ {`REQUISITION`,`TRANSFER`,`DISMISS`,`DEFER`} | — | VR-115 |
| **Cross-field** | `acknowledgmentNotes` required when `actionTaken` ∈ {`DISMISS`,`DEFER`} | — | VR-114 |

### API-160 — `GetReplenishmentRecommendationsQuery`

Date range cross-field; user location scope; `recommendationAction` enum (BR-009, BR-011).

### API-161 — `GetOpenPurchaseOrderBoardQuery`

User location scope (VR-034); overdue filter (VR-123).

### API-162 — `GetInboundSupplyCalendarQuery`

| Required | `startDate`, `endDate` |
| Cross-field | `startDate` ≤ `endDate`; max 90-day range | VR-033 |

### API-163 — `GetInboundDeliveryDelayLogQuery`

Date range cross-field; location/supplier filters; user scope.

### API-164 — `GetBackorderPipelineQuery`

`prioritySort` default true (VR-102, BR-028); location scope.

### API-165 — `GetFulfillmentExceptionLogQuery`

Exception type/status enums; date range cross-field (BR-003).

### API-166 — `GetNetworkImbalanceAnalysisQuery`

Active locations; optional SKU active (VR-139, BR-011).

### API-167 — `GetShrinkageAnalysisQuery`

| Required | `startDate`, `endDate` |
| Business | Reason code filter if provided (BR-020) | VR-086, VR-087 |

### API-168 — `GetCountPerformanceMetricsQuery`

| Required | `startDate`, `endDate` |
| Business | Exclude pending variances default (BR-018) | VR-157, VR-158 |

### API-169 — `GetCampaignReadinessStatusQuery`

`campaignId` max 50; `daysUntilStart` ≥ 0 (BR-029, VR-126).

### API-170 — `GetInventoryKpisQuery`

| Required | `startDate`, `endDate` |
| Business | Authorized `locationCodes[]`; valid `kpiCodes[]` | VR-151, VR-161, VR-162 |

### API-171 — `GetValuationSnapshotsQuery`

Date range cross-field; user location scope.

### API-172 — `GetValuationReconciliationQuery`

| Required | `periodEndDate` |
| Format | `varianceThresholdPercent` 0–100 | BR-008 |

---

## Platform & Integration

### API-173 — `GetSessionRequest`

Optional query flags only; auth via `Authorization` header (VR-008).

### API-174 — `LogoutRequest`

`logoutAllSessions` optional boolean; empty body accepted.

### API-175 — `HealthCheckRequest`

No parameters; public endpoint — no validation.

### API-176 — `ImportSalesOrderRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `externalOrderId`, `externalSystemCode`, `channel`, `lines` (min 1) | — | VR-007 |
| **Length** | `externalOrderId` 1–100; `externalSystemCode` 1–30 | — | — |
| **Format** | `channel` ∈ {`B2B`,`B2C`,`MARKETPLACE`} | — | — |
| **Business** | Idempotent re-import; SKU exists; qty > 0 per line | BR-001 | VR-006, VR-007 |

**`ExternalOrderLineDto`:** `externalLineId` R 1–50; `sku` R; `quantity` R > 0.

### API-177 — `GetFulfillmentStatusFeedQuery`

| Required | `externalSystemCode` |
| Length | `externalSystemCode` 1–30; `externalOrderId` 0–100 |
| Format | `updatedSince` ISO instant; `status` enum |

### API-178 — `ImportCampaignPlanRequest`

| Category | Rule | BR | VR |
|----------|------|----|----|
| **Required** | `externalCampaignId`, `externalSystemCode`, `campaignName`, `campaignStartDate`, `campaignEndDate`, `allocationLines` (min 1) | BR-029 | VR-126 |
| **Length** | `externalCampaignId` 1–50; `campaignName` 1–200 | — | — |
| **Cross-field** | `campaignEndDate` ≥ `campaignStartDate` | — | VR-126 |
| **Business** | Active SKU/location per allocation line; target qty > 0 | BR-029 | VR-127 |

---

## Business Rule Traceability Index

Maps each **BR-xxx** to Request DTOs where it is enforced.

| BR | Rule Name | Enforced In (API IDs) |
|----|-----------|----------------------|
| BR-001 | ATP-Only Customer Commitment | API-035, API-036, API-043, API-084, API-085, API-087, API-095, API-098, API-176 |
| BR-002 | Reservation at Order Confirmation | API-043, API-085, API-164 |
| BR-003 | Verified Pick Before Shipment | API-090, API-091, API-092 |
| BR-004 | Verify Before Inventory Acceptance | API-069 |
| BR-005 | Put-Away Before Availability | API-073 |
| BR-006 | Document Receipt Discrepancies | API-028, API-070, API-072 |
| BR-007 | Purchase Order Required for Supplier Receipt | API-058, API-059, API-065, API-066, API-075 |
| BR-008 | Three-Way Match Before Payment | API-077, API-079, API-080 |
| BR-009 | Reorder at Reorder Level | API-038, API-040, API-159 |
| BR-010 | Safety Stock Protection | API-038, API-040, API-043, API-085 |
| BR-011 | Network Check Before Purchase | API-054, API-056, API-098 |
| BR-012 | Protect Source Location Minimum | API-042, API-098, API-101 |
| BR-013 | Quarantine Exclusion from Sellable Stock | API-036, API-045, API-046, API-154 |
| BR-014 | FEFO Rotation for Shelf-Life Products | API-001, API-004, API-088, API-090 |
| BR-015 | FIFO Rotation for Standard Goods | API-001, API-004, API-088, API-090 |
| BR-016 | Minimum Remaining Shelf Life at Receipt | API-001, API-004, API-069 |
| BR-017 | Lot or Batch Capture for Traceable Products | API-001, API-004, API-032, API-045, API-069, API-090, API-092, API-098, API-103 |
| BR-018 | Blind Cycle Counting | API-108, API-110, API-111, API-114, API-168 |
| BR-019 | Independent Count Approval | API-031, API-119, API-121 |
| BR-020 | Mandatory Adjustment Reason Codes | API-022, API-024, API-104, API-116, API-120, API-167 |
| BR-021 | Independent Approval for Material Adjustments | API-027, API-031, API-121 |
| BR-022 | Investigate Before Adjusting | API-116, API-118 |
| BR-023 | Documented Write-Off Authorization | API-120, API-130 |
| BR-024 | Physical Inventory Freeze | API-112, API-114, API-115 |
| BR-025 | Return Authorization Required | API-076, API-124, API-126, API-128 |
| BR-026 | Inspect Returns Before Restocking | API-046, API-129, API-130 |
| BR-027 | No Reorder of Discontinued Products | API-005, API-007, API-054, API-059 |
| BR-028 | Backorder Customer Acknowledgment | API-093, API-094, API-095 |
| BR-029 | Promotional Stock Ring-Fencing | API-048, API-132, API-135, API-138, API-139, API-169, API-178 |
| BR-030 | Bonded Inventory Customs Clearance | API-045 |
| BR-031 | Consignment Ownership at Consumption | API-032, API-047, API-049 |
| BR-032 | Class A Priority Monitoring | API-006, API-108, API-168 |

---

## Validation Rule Cross-Reference Index

| VR Range | Domain | Primary APIs |
|----------|--------|--------------|
| VR-001–VR-010 | Product catalog | API-001–API-010 |
| VR-011–VR-017 | Locations | API-011–API-021 |
| VR-018–VR-028 | Governance & thresholds | API-026–API-031, API-038–API-040 |
| VR-030–VR-051 | Procurement & PO | API-049–API-065, API-062–API-063 |
| VR-035–VR-048 | Receiving & matching | API-066–API-080 |
| VR-053–VR-056, VR-059 | Stock positions & ATP | API-033–API-037 |
| VR-062, VR-153–VR-154 | Date ranges & audit queries | API-153–API-157, intelligence APIs |
| VR-066–VR-072 | Physical accuracy | API-108–API-115 |
| VR-075–VR-085 | Adjustments & quarantine | API-045–API-046, API-116–API-122 |
| VR-090–VR-111 | Fulfillment | API-081–API-096 |
| VR-117–VR-125 | Requisition & replenishment | API-054–API-056, API-043, API-085 |
| VR-126–VR-127 | Promotional | API-048, API-132–API-138, API-178 |
| VR-128–VR-141 | Transfers | API-042, API-098–API-107 |
| VR-142–VR-149 | Returns | API-124–API-130, API-076 |
| VR-151–VR-162 | Intelligence scope & KPIs | API-150–API-172 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Backend Architect | | | |
| Solution Architect | | | |
| Senior Business Analyst | | | |
| Product Owner | | | |

---

*End of Request DTO Validation Specification*

*Document ID: SRS-API-004 | Version 1.0 | July 6, 2026*
