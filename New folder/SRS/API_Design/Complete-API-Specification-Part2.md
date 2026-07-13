# Complete API Specification — Part 2
## M-03 through M-07 (API-022 – API-097)

**Parent document:** `Complete-API-Specification.md` (SRS-API-009)  
**Conventions:** Global headers, errors, and pagination apply from Part 1.

---

## M-03 — Inventory Governance

### API-022: Create Reason Code
| 1 | `POST` | 2 | `/api/v1/governance/reason-codes` | 3 | Create standardized reason code | 4 | Bearer JWT | 5 | `PERM-014` / `INV_CTRL` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `code`, `description`, `transactionTypes[]`, `isActive` | 10 | VR-026, VR-027; unique code | 11 | `ReasonCodeResponse` | 12 | 400,403,409 | 13 | **201** | 14 | **BR-020** | 15 | UC-005 |
**16** POST `{ "code": "DAMAGE_RCPT", "description": "Damaged at receipt", "transactionTypes": ["RECEIPT_DISCREPANCY"] }`  
**17** `201` reason code object  
**18** `409` duplicate code

### API-023: List Reason Codes
| 1 | `GET` | 2 | `/api/v1/governance/reason-codes` | 3 | List active reason codes | 4 | Bearer | 5 | `PERM-014` | 6 | `Authorization` | 7 | — | 8 | `transactionType`, `isActive`, `page`, `pageSize` | 9 | — | 10 | VR-026 | 11 | `PagedResponse<ReasonCodeResponse>` | 12 | 400,401,403 | 13 | **200** | 14 | BR-020 | 15 | UC-005, UC-017 |
**16–18** GET `?transactionType=ADJUSTMENT` → 200 paged list; 400 invalid enum

### API-024: Retire Reason Code
| 1 | `POST` | 2 | `/api/v1/governance/reason-codes/{code}/retire` | 3 | Retire reason code | 4 | Bearer | 5 | `PERM-014` | 6 | `Authorization`, `Content-Type` | 7 | `code` | 8 | — | 9 | `retirementReason`, `effectiveDate` | 10 | VR-027 | 11 | `CommandResultResponse` | 12 | 400,403,404 | 13 | **200** | 14 | BR-020 | 15 | UC-005 |
**16–18** POST retire → 200; 404 unknown code

### API-025: Validate Reason Code
| 1 | `GET` | 2 | `/api/v1/governance/reason-codes/{code}/validate` | 3 | Validate code for transaction type | 4 | Bearer | 5 | `PERM-014` | 6 | `Authorization` | 7 | `code` | 8 | `transactionType` (required) | 9 | — | 10 | VR-026, VR-027 | 11 | `{ "valid": true, "applicable": true }` | 12 | 400,401 | 13 | **200** | 14 | BR-020 | 15 | UC-017 |
**16–18** GET validate → 200 `{ "valid": true }`

### API-026: Publish Governance Policy
| 1 | `POST` | 2 | `/api/v1/governance/policies` | 3 | Publish policy version | 4 | Bearer | 5 | `PERM-013` / `OPS_DIR`,`COO` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `policyName`, `effectiveFrom`, `parameters[]` | 10 | VR-028 no overlap | 11 | `GovernancePolicyResponse` | 12 | 400,403,409 | 13 | **201** | 14 | Governance | 15 | UC-005 |
**16–18** POST policy → 201; 409 overlapping effective dates

### API-027: Update Approval Thresholds
| 1 | `PATCH` | 2 | `/api/v1/governance/policies/{policyId}/approval-thresholds` | 3 | Update approval thresholds | 4 | Bearer | 5 | `PERM-013` | 6 | `Authorization`, `Content-Type` | 7 | `policyId` | 8 | — | 9 | `transactionType`, `effectiveFrom`, thresholds | 10 | VR-020, VR-082 | 11 | `GovernancePolicyResponse` | 12 | 400,403,404 | 13 | **200** | 14 | **BR-021** | 15 | UC-005 |
**16–18** PATCH thresholds → 200

### API-028: Update Receipt Tolerances
| 1 | `PATCH` | 2 | `/api/v1/governance/policies/{policyId}/receipt-tolerances` | 3 | Update receipt tolerances | 4 | Bearer | 5 | `PERM-013` | 6 | `Authorization`, `Content-Type` | 7 | `policyId` | 8 | — | 9 | tolerance fields, `effectiveFrom` | 10 | VR-048 | 11 | `GovernancePolicyResponse` | 12 | 400,403 | 13 | **200** | 14 | **BR-006** | 15 | UC-005, UC-009 |
**16–18** PATCH tolerance percent → 200

### API-029: Get Approval Thresholds
| 1 | `GET` | 2 | `/api/v1/governance/approval-thresholds` | 3 | Lookup effective threshold | 4 | Bearer | 5 | `PERM-013` | 6 | `Authorization` | 7 | — | 8 | `transactionType`, `locationCode`, `asOfDate` | 9 | — | 10 | VR-082 | 11 | `ApprovalThresholdResponse` | 12 | 401,403 | 13 | **200** | 14 | BR-021 | 15 | UC-017 |
**16–18** GET → 200 threshold object

### API-030: Get Receipt Tolerances
| 1 | `GET` | 2 | `/api/v1/governance/receipt-tolerances` | 3 | Lookup receipt tolerance | 4 | Bearer | 5 | `PERM-032` / `WH_MGR` | 6 | `Authorization` | 7 | — | 8 | `locationCode`, `supplierCode`, `asOfDate` | 9 | — | 10 | VR-048 | 11 | `ReceiptToleranceResponse` | 12 | 401,403 | 13 | **200** | 14 | BR-006 | 15 | UC-008 |
**16–18** GET → 200 tolerance

### API-031: Evaluate Segregation of Duties
| 1 | `POST` | 2 | `/api/v1/governance/segregation-of-duties/evaluate` | 3 | SoD compliance check | 4 | Bearer | 5 | `PERM-013` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `initiatorUserId`, `approverUserId`, `transactionType` | 10 | VR-075, VR-083; approver≠initiator | 11 | `{ "compliant": false, "violations": [] }` | 12 | 400,401 | 13 | **200** | 14 | **BR-019**, **BR-021** | 15 | UC-045 |
**16** POST evaluate SoD  
**17** `{ "compliant": false, "violations": ["SOD_INITIATOR_APPROVER_SAME"] }`  
**18** `400` missing `approverUserId`

---

## M-04 — Inventory Balance

### API-032: Establish Opening Balances
| 1 | `POST` | 2 | `/api/v1/inventory/opening-balances` | 3 | Set go-live opening balances | 4 | Bearer | 5 | `PERM-010` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `locationCode`, `balanceLines[]`, `approvalReference` | 10 | VR-024, VR-025; lot if traceable | 11 | `OpeningBalanceResultResponse` | 12 | 400,403,422 | 13 | **201** | 14 | BR-017 | 15 | UC-046 |
**16–18** POST balances → 201; 422 location not pre-activation

### API-033: List Stock Positions
| 1 | `GET` | 2 | `/api/v1/inventory/stock-positions` | 3 | Search stock positions | 4 | Bearer | 5 | `PERM-017`,`PERM-021` | 6 | `Authorization` | 7 | — | 8 | `sku`, `locationCode`, `stockStatus`, `abcClass`, pagination | 9 | — | 10 | VR-054 at least one filter; VR-053 scope | 11 | `PagedResponse<StockPositionSummaryResponse>` | 12 | 400,403 | 13 | **200** | 14 | — | 15 | UC-012, UC-013 |
**16–18** GET `?locationCode=WH-EAST` → 200 paged positions

### API-034: Get Stock Position
| 1 | `GET` | 2 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}` | 3 | Position detail | 4 | Bearer | 5 | `PERM-017` | 6 | `Authorization` | 7 | `locationCode`, `sku` | 8 | — | 9 | — | 10 | VR-053, VR-054 | 11 | `StockPositionDetailResponse` | 12 | 403,404 | 13 | **200** | 14 | — | 15 | UC-012 |
**16–18** GET → 200 with `StockAvailabilityResponse`

### API-035: Get Availability by SKU
| 1 | `GET` | 2 | `/api/v1/inventory/availability/{sku}` | 3 | ATP inquiry | 4 | Bearer | 5 | `PERM-018` | 6 | `Authorization` | 7 | `sku` | 8 | `locationCode` (required), `requestedQuantity` | 9 | — | 10 | VR-055 | 11 | `AvailabilityResponse` | 12 | 400,403 | 13 | **200** | 14 | **BR-001** | 15 | UC-013, UC-021 |
**17** `{ "sku": "BOLT-M10", "atp": { "amount": 45, "unitOfMeasure": "EA" }, "canFulfill": true }`

### API-036: Get Network Availability
| 1 | `GET` | 2 | `/api/v1/inventory/availability/{sku}/network` | 3 | Network ATP rollup | 4 | Bearer | 5 | `PERM-022` | 6 | `Authorization` | 7 | `sku` | 8 | `locationCodes[]`, `excludeQuarantined`, `excludePromotionalRingFence` | 9 | — | 10 | VR-056, VR-064 | 11 | `NetworkAvailabilityResponse` | 12 | 401,403 | 13 | **200** | 14 | **BR-001**, **BR-013** | 15 | UC-013, UC-034 |
**16–18** GET network ATP → 200 rollup by location

### API-037: Get Stock Status Indicator
| 1 | `GET` | 2 | `/api/v1/inventory/stock-status/{locationCode}/{sku}` | 3 | Derived stock status | 4 | Bearer | 5 | `PERM-020` | 6 | `Authorization` | 7 | `locationCode`, `sku` | 8 | — | 9 | — | 10 | VR-059 policy exists | 11 | `StockStatusIndicatorResponse` | 12 | 404 | 13 | **200** | 14 | **BR-009** | 15 | UC-012, UC-028 |
**17** `{ "stockStatus": "LOW_STOCK", "reorderLevel": 100, "atp": 25 }`

### API-038: Define Stock Policy
| 1 | `POST` | 2 | `/api/v1/inventory/stock-policies` | 3 | Create stock policy | 4 | Bearer | 5 | `PERM-011` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `locationCode`, `sku`, thresholds, `effectiveFrom` | 10 | VR-018–VR-020 | 11 | `StockPolicyResponse` | 12 | 400,403 | 13 | **201** | 14 | **BR-009**, **BR-010** | 15 | UC-003 |
**16–18** POST policy → 201

### API-039: Get Stock Policy
| 1 | `GET` | 2 | `/api/v1/inventory/stock-policies/{locationCode}/{sku}` | 3 | Get effective policy | 4 | Bearer | 5 | `PERM-011` | 6 | `Authorization` | 7 | `locationCode`, `sku` | 8 | `asOfDate` | 9 | — | 10 | VR-020 | 11 | `StockPolicyResponse` | 12 | 404 | 13 | **200** | 14 | BR-009 | 15 | UC-003 |
**16–18** GET → 200 policy

### API-040: Update Stock Policy
| 1 | `PATCH` | 2 | `/api/v1/inventory/stock-policies/{locationCode}/{sku}` | 3 | Update thresholds | 4 | Bearer | 5 | `PERM-011` | 6 | `Authorization`, `Content-Type` | 7 | `locationCode`, `sku` | 8 | — | 9 | threshold fields, `effectiveFrom` | 10 | VR-018–VR-020; ≥1 field | 11 | `StockPolicyResponse` | 12 | 400,403 | 13 | **200** | 14 | BR-009, BR-010 | 15 | UC-003 |
**16–18** PATCH reorder level → 200

### API-041: Get Lot Breakdown
| 1 | `GET` | 2 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/lots` | 3 | Lot-level quantities | 4 | Bearer | 5 | `PERM-017` | 6 | `Authorization` | 7 | `locationCode`, `sku` | 8 | `includeQuarantined` | 9 | — | 10 | Product traceable | 11 | `BoundedListResponse<LotQuantityResponse>` | 12 | 404 | 13 | **200** | 14 | **BR-017** | 15 | UC-024 |
**16–18** GET lots → 200 lot array

### API-042: Evaluate Transfer Capacity
| 1 | `GET` | 2 | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity` | 3 | Max transferable spare | 4 | Bearer | 5 | `PERM-076` | 6 | `Authorization` | 7 | `locationCode`, `sku` | 8 | `requestedQuantity` | 9 | — | 10 | VR-140 | 11 | `TransferCapacityResponse` | 12 | 403 | 13 | **200** | 14 | **BR-012** | 15 | UC-031 |
**17** `{ "maxTransferable": { "amount": 30, "unitOfMeasure": "EA" } }`

### API-043: Reserve Stock

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations` |
| **3** | **Purpose** | Reserve stock; reduce ATP for order line |
| **4** | **Authentication** | Required |
| **5** | **Required Permission** | `PERM-052` — `COO`, `OPS_DIR`, `WH_MGR` |
| **6** | **Request Headers** | `Authorization`, `Content-Type`, **`Idempotency-Key`** (recommended) |
| **7** | **Path Parameters** | `locationCode`, `sku` |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `quantity`, `orderId`, `orderLineId`; optional `reservationExpiry`, `safetyStockExceptionReference` |
| **10** | **Validation Rules** | VR-092, VR-093, VR-094; qty ≤ ATP; location not frozen |
| **11** | **Success Response** | `ReservationResponse` — `reservationId`, `reservedQuantity`, `remainingAtp` |
| **12** | **Error Responses** | 400; 403; 422 `BIZ_INSUFFICIENT_ATP`, `BIZ_SAFETY_STOCK_BREACH` |
| **13** | **HTTP Status Codes** | **201 Created** |
| **14** | **Business Rules Applied** | **BR-001**, **BR-002**, **BR-010** |
| **15** | **Related Use Case** | UC-022 |

**16. Example Request**

```http
POST /api/v1/inventory/stock-positions/WH-EAST/BOLT-M10/reservations HTTP/1.1
Authorization: Bearer eyJ...
Content-Type: application/json
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000

{
  "quantity": { "amount": 10, "unitOfMeasure": "EA" },
  "orderId": "ORD-2026-001",
  "orderLineId": "LINE-001"
}
```

**17. Example Success** — `201`

```json
{
  "reservationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "locationCode": "WH-EAST",
  "sku": "BOLT-M10",
  "reservedQuantity": { "amount": 10, "unitOfMeasure": "EA" },
  "remainingAtp": { "amount": 35, "unitOfMeasure": "EA" },
  "status": "ACTIVE"
}
```

**18. Example Error** — `422`

```json
{
  "type": "https://api.ims.example/problems/business-rule-violation",
  "title": "Business Rule Violation",
  "status": 422,
  "detail": "Cannot reserve 100 units. Only 45 units are available to promise.",
  "instance": "/api/v1/inventory/stock-positions/WH-EAST/BOLT-M10/reservations",
  "errorCode": "BIZ_INSUFFICIENT_ATP",
  "businessRuleId": "BR-001",
  "validationRuleId": "VR-092",
  "traceId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "timestamp": "2026-07-06T15:00:00.000Z"
}
```

### API-044: Release Reservation
| 1 | `POST` | 2 | `.../reservations/{reservationId}/release` | 3 | Release reserved stock | 4 | Bearer | 5 | `PERM-053` | 6 | `Authorization`, `Content-Type`, `Idempotency-Key` | 7 | `locationCode`, `sku`, `reservationId` | 8 | — | 9 | `releaseReason`, optional `releaseQuantity` | 10 | VR-095, VR-096 | 11 | `CommandResultResponse` | 12 | 400,404,422 | 13 | **200** | 14 | **BR-002** | 15 | UC-023 |
**16–18** POST release → 200; 422 exceeds reserved qty

### API-045: Apply Quarantine Hold
| 1 | `POST` | 2 | `.../quarantine-holds` | 3 | Place stock on quarantine | 4 | Bearer | 5 | `PERM-047` | 6 | `Authorization`, `Content-Type` | 7 | `locationCode`, `sku` | 8 | — | 9 | `quantity`, `holdReason`, `reasonCode`, `lotIdentity` | 10 | VR-084, VR-026 | 11 | `QuarantineHoldResponse` | 12 | 422 | 13 | **201** | 14 | **BR-013**, **BR-030** | 15 | UC-019 |
**16–18** POST hold → 201 holdId

### API-046: Release Quarantine Hold
| 1 | `POST` | 2 | `.../quarantine-holds/{holdId}/release` | 3 | Release quarantine | 4 | Bearer | 5 | `PERM-048` | 6 | `Authorization`, `Content-Type` | 7 | `locationCode`, `sku`, `holdId` | 8 | — | 9 | `disposition`, `reasonCode`, `inspectionOutcomeReference` | 10 | VR-085 | 11 | `CommandResultResponse` | 12 | 422 | 13 | **200** | 14 | **BR-026** | 15 | UC-019 |
**16–18** POST RESTORE_TO_SELLABLE with inspection ref → 200

### API-047: Transfer Consignment Ownership
| 1 | `POST` | 2 | `.../consignment-ownership` | 3 | Transfer consignment to owned | 4 | Bearer | 5 | `PERM-017` / finance | 6 | `Authorization`, `Content-Type` | 7 | `locationCode`, `sku` | 8 | — | 9 | `quantity`, `consumptionReference` | 10 | consignment on-hand | 11 | `CommandResultResponse` | 12 | 422 | 13 | **200** | 14 | **BR-031** | 15 | UC-039 |
**16–18** POST consumption → 200

### API-048: Segregate Promotional Stock
| 1 | `POST` | 2 | `.../promotional-segregation` | 3 | Ring-fence ATP for campaign | 4 | Bearer / internal | 5 | `PERM-093` | 6 | `Authorization`, `Content-Type` | 7 | `locationCode`, `sku` | 8 | — | 9 | `campaignId`, `allocationId`, `quantity` | 10 | VR-127 | 11 | `CommandResultResponse` | 12 | 422 | 13 | **200** | 14 | **BR-029** | 15 | UC-040 |
**16–18** Event-driven ring-fence → 200

---

## M-05 — Procurement & Supplier (API-049 – API-065)

| API | Method | URL | Permission | UC | Success | Key BR |
|-----|--------|-----|------------|-----|---------|--------|
| **049** | POST | `/suppliers` | PERM-024 PUR_MGR | UC-006 | 201 SupplierResponse | — |
| **050** | GET | `/suppliers` | PERM-035 | UC-006 | 200 Paged | — |
| **051** | GET | `/suppliers/{supplierCode}` | PERM-035 | UC-006 | 200 Detail | — |
| **052** | PATCH | `/suppliers/{supplierCode}` | PERM-025 PUR_MGR | UC-006 | 200 Detail | — |
| **053** | POST | `/suppliers/{code}/deactivate` | PERM-026 PUR_MGR | UC-006 | 200 Command | — |
| **054** | POST | `/procurement/requisitions` | PERM-067 BUYER,PUR_MGR | UC-029 | 201 Requisition | BR-011, BR-027 |
| **055** | GET | `/procurement/requisitions/{id}` | PERM-067 | UC-029 | 200 Detail | — |
| **056** | POST | `.../approve` | PERM-068 PUR_MGR | UC-029 | 200 Command | BR-011 SoD |
| **057** | POST | `.../reject` | PERM-068 | UC-029 | 200 Command | — |
| **058** | POST | `.../convert-to-po` | PERM-024 | UC-029 | 201 PO | BR-007 |
| **059** | POST | `/procurement/purchase-orders` | PERM-024 BUYER | UC-006 | 201 PO | BR-007, BR-027 |
| **060** | GET | `/procurement/purchase-orders` | PERM-027 | UC-006 | 200 Paged | — |
| **061** | GET | `/procurement/purchase-orders/{id}` | PERM-027 | UC-006 | 200 Detail | — |
| **062** | PATCH | `/procurement/purchase-orders/{id}` | PERM-025 | UC-006 | 200 Detail | VR-051 |
| **063** | POST | `.../cancel` | PERM-026 | UC-006 | 200 Command | — |
| **064** | POST | `.../expected-deliveries` | PERM-027 | UC-007 | 200 Schedule | — |
| **065** | GET | `.../validate-for-receipt` | PERM-028 WH_MGR | UC-008 | 200 Validation | **BR-007** |

*Each API-049–065 follows the 18-field template: Auth=Bearer; Headers per Part 1; Validation per SRS-API-004; Errors=standard set; Example request=minimal HTTP+JSON for POST commands, query string for GET.*

**API-059 Example (Place PO):**

**16** `POST /api/v1/procurement/purchase-orders` + body `{ "supplierCode": "SUP-01", "receivingLocationCode": "WH-EAST", "expectedDeliveryDate": "2026-08-01", "lines": [{ "sku": "BOLT-M10", "orderedQuantity": { "amount": 500, "unitOfMeasure": "EA" } }] }`  
**17** `201` `PurchaseOrderDetailResponse` with `purchaseOrderId`, `status: OPEN`  
**18** `422 BIZ_PRODUCT_DISCONTINUED` if SKU discontinued (BR-027)

---

## M-06 — Inbound Receiving (API-066 – API-080)

| API | Method | URL | Permission | UC | Success | Key BR |
|-----|--------|-----|------------|-----|---------|--------|
| **066** | POST | `/inbound/goods-receipts` | PERM-028 | UC-008 | 201 Receipt | **BR-007** |
| **067** | GET | `/inbound/goods-receipts` | PERM-028 | UC-008 | 200 Paged | — |
| **068** | GET | `/inbound/goods-receipts/{id}` | PERM-028 | UC-008 | 200 Detail | — |
| **069** | POST | `.../verify` | PERM-028 | UC-008 | 200 Verified | **BR-004**, **BR-016**, **BR-017** |
| **070** | POST | `.../discrepancies` | PERM-029 | UC-009 | 201 Discrepancy | **BR-006** |
| **071** | GET | `.../discrepancies` | PERM-029 | UC-009 | 200 List | — |
| **072** | POST | `.../discrepancies/{id}/resolve` | PERM-030 | UC-009 | 200 Resolved | BR-006 |
| **073** | POST | `.../put-away` | PERM-033 | UC-010 | 200 Complete | **BR-005** |
| **074** | GET | `/inbound/pending-put-away` | PERM-033 | UC-010 | 200 Paged | — |
| **075** | POST | `/inbound/ad-hoc-receipts` | PERM-031 WH_MGR | UC-011 | 201 Receipt | **BR-007** override |
| **076** | POST | `/inbound/return-receipts` | PERM-034 | UC-011 | 201 Receipt | **BR-025** |
| **077** | POST | `/inbound/supplier-invoices` | PERM-094 FIN_MGR | UC-039 | 201 Invoice | — |
| **078** | GET | `/inbound/supplier-invoices/{id}` | PERM-094 | UC-039 | 200 Detail | — |
| **079** | POST | `.../three-way-match` | PERM-094 | UC-039 | 200 MatchResult | **BR-008** |
| **080** | POST | `.../authorize-payment` | PERM-094 CFO,FIN_MGR | UC-039 | 200 Authorized | **BR-008** |

**API-069 Verify Example:**

**16** POST verify lines with `acceptedQuantity`, `lotIdentity` for traceable SKU  
**17** `200` `{ "goodsReceiptId": "...", "status": "VERIFIED" }`  
**18** `422 BIZ_MRSL_NON_COMPLIANT` (BR-016)

---

## M-07 — Order Fulfillment (API-081 – API-097)

| API | Method | URL | Permission | UC | Success | Key BR |
|-----|--------|-----|------------|-----|---------|--------|
| **081** | POST | `/fulfillment/orders` | PERM-054 | UC-021 | 201 Order | — |
| **082** | GET | `/fulfillment/orders` | PERM-062 | UC-027 | 200 Paged | — |
| **083** | GET | `/fulfillment/orders/{id}` | PERM-062 | UC-027 | 200 Detail | — |
| **084** | POST | `.../availability` | PERM-051 | UC-021 | 200 Availability | **BR-001** |
| **085** | POST | `.../confirm` | PERM-054 | UC-022 | 200 Confirmed | **BR-002** |
| **086** | POST | `.../cancel` | PERM-054 | UC-023 | 200 Cancelled | — |
| **087** | POST | `.../multi-location-plan` | PERM-061 | UC-048 | 200 Plan | BR-001 |
| **088** | POST | `.../pick-lists` | PERM-055 WH_MGR | UC-024 | 201 PickList | BR-014/015 |
| **089** | GET | `.../pick-lists/awaiting` | PERM-055 | UC-024 | 200 List | — |
| **090** | POST | `.../picks/{id}/verify` | PERM-055 | UC-024 | 200 Verified | **BR-003**, **BR-017** |
| **091** | POST | `.../pack` | PERM-055 | UC-024 | 200 Packed | BR-003 |
| **092** | POST | `.../shipments` | PERM-056 | UC-024 | 201 Shipment | **BR-003** |
| **093** | POST | `.../partial-fulfillment` | PERM-057 | UC-025 | 200 Partial | **BR-028** |
| **094** | POST | `.../backorders` | PERM-058 | UC-025 | 201 Backorder | **BR-028** |
| **095** | POST | `/fulfillment/backorders/{id}/fulfill` | PERM-058 | UC-025 | 200 Fulfilled | BR-001 |
| **096** | POST | `.../exceptions` | PERM-059 | UC-026 | 201 Exception | — |
| **097** | GET | `.../status` | PERM-062 | UC-027 | 200 Status | — |

**API-092 Dispatch Shipment (full example):**

| # | Field | Value |
|---|-------|-------|
| **1–5** | POST `/api/v1/fulfillment/orders/{orderId}/shipments` — Auth Bearer — `PERM-056` (`WH_MGR`, `PIK_PAK`) |
| **6–9** | Headers: `Authorization`, `Content-Type`, `Idempotency-Key`; body: `shipmentLines[]`, optional `carrierCode`, `trackingNumber` |
| **10** | VR-097, VR-098; pick verified; qty ≤ reserved |
| **11–13** | `201` `ShipmentResponse`; errors 400,403,422 |
| **14** | **BR-003** |
| **15** | UC-024 |

**16** POST shipment with `shipmentLines[{ orderLineId, shippedQuantity, lotIdentity }]`  
**17** `201` `{ "shipmentId": "...", "status": "SHIPPED", "shippedAt": "2026-07-06T16:00:00Z" }`  
**18** `422 BIZ_*` pick not verified

---

*Continued in `Complete-API-Specification-Part3.md` — API-098 through API-178 (M-08 Network Transfer through Platform & Integration)*
