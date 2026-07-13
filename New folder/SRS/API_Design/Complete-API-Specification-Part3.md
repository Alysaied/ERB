# Complete API Specification — Part 3
## M-08 through Platform (API-098 – API-178)

**Parent document:** `Complete-API-Specification.md` (SRS-API-009)  
**Conventions:** Global headers, errors, and pagination apply from Part 1. All URLs are prefixed with `/api/v1`.

---

## M-08 — Network Transfer

### API-098: Request Stock Transfer

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/transfers` |
| **3** | **Purpose** | Request inter-location stock transfer to resolve local shortage |
| **4** | **Authentication** | Required — Bearer JWT |
| **5** | **Required Permission** | `PERM-071` — `OPS_DIR`, `WH_MGR`, `REG_MGR` |
| **6** | **Request Headers** | `Authorization`, `Content-Type: application/json`, optional `Idempotency-Key`, `X-Trace-Id` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | None |
| **9** | **Request Body** | `sourceLocationCode`, `destinationLocationCode`, `justification`, `lines[]` (`sku`, `requestedQuantity`); optional `priority`, `requiredByDate` |
| **10** | **Validation Rules** | VR-128–VR-130; source ≠ destination; qty ≤ source ATP; respects source minimum (VR-140) |
| **11** | **Success Response** | `StockTransferDetailResponse` — `transferId`, `status: REQUESTED`, lines, audit |
| **12** | **Error Responses** | 400 validation; 401; 403 location scope; 422 `BIZ_INSUFFICIENT_ATP`, `BIZ_SOURCE_MINIMUM_BREACH` |
| **13** | **HTTP Status Codes** | Success: **201 Created**; Errors: 400, 401, 403, 422, 500 |
| **14** | **Business Rules Applied** | **BR-011**, **BR-012** |
| **15** | **Related Use Case** | UC-031 |

**16. Example Request**

```http
POST /api/v1/transfers HTTP/1.1
Authorization: Bearer eyJ...
Content-Type: application/json

{
  "sourceLocationCode": "WH-WEST",
  "destinationLocationCode": "WH-EAST",
  "justification": "East warehouse below safety stock for BOLT-M10",
  "lines": [{ "sku": "BOLT-M10", "requestedQuantity": { "amount": 50, "unitOfMeasure": "EA" } }]
}
```

**17. Example Success** — `201`

```json
{
  "transferId": "TRF-2026-0042",
  "status": "REQUESTED",
  "sourceLocationCode": "WH-WEST",
  "destinationLocationCode": "WH-EAST",
  "lines": [{ "sku": "BOLT-M10", "requestedQuantity": { "amount": 50, "unitOfMeasure": "EA" }, "approvedQuantity": null }]
}
```

**18. Example Error** — `422`

```json
{
  "status": 422,
  "errorCode": "BIZ_SOURCE_MINIMUM_BREACH",
  "businessRuleId": "BR-012",
  "detail": "Transfer would reduce WH-WEST below minimum stock level."
}
```

### API-099: List Stock Transfers
| 1 | `GET` | 2 | `/api/v1/transfers` | 3 | List transfers with status and location filters | 4 | Bearer | 5 | `PERM-075` | 6 | `Authorization` | 7 | — | 8 | `status`, `sourceLocationCode`, `destinationLocationCode`, `startDate`, `endDate`, `page`, `pageSize` | 9 | — | 10 | VR-136 date range; user location scope | 11 | `PagedResponse<StockTransferSummaryResponse>` | 12 | 400,401,403 | 13 | **200** | 14 | — | 15 | UC-031, UC-033 |
**16** GET `?status=IN_TRANSIT&destinationLocationCode=WH-EAST`  
**17** `200` paged transfer list  
**18** `400 VAL_INVALID_DATE_RANGE`

### API-100: Get Stock Transfer
| 1 | `GET` | 2 | `/api/v1/transfers/{transferId}` | 3 | Transfer detail and in-transit state | 4 | Bearer | 5 | `PERM-075` | 6 | `Authorization` | 7 | `transferId` | 8 | — | 9 | — | 10 | Transfer exists; user scope | 11 | `StockTransferDetailResponse` | 12 | 401,403,404 | 13 | **200** | 14 | — | 15 | UC-031, UC-033 |
**16–18** GET by id → 200 detail; 404 `NF_TRANSFER_NOT_FOUND`

### API-101: Approve Transfer
| 1 | `POST` | 2 | `/api/v1/transfers/{transferId}/approve` | 3 | Approve after source capacity validation | 4 | Bearer | 5 | `PERM-072` (`OPS_DIR`, `COO`) | 6 | `Authorization`, `Content-Type` | 7 | `transferId` | 8 | — | 9 | optional `approvalNotes`, `approvedLines[]` | 10 | VR-132, VR-141; status `REQUESTED`; approver ≠ requester (SoD) | 11 | `CommandResultResponse` + transfer detail | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-012** | 15 | UC-032 |
**16** POST approve `{}`  
**17** `200` `{ "transferId": "TRF-2026-0042", "status": "APPROVED" }`  
**18** `403 AUTHZ_INSUFFICIENT_PERMISSION` if requester approves own transfer

### API-102: Reject Transfer
| 1 | `POST` | 2 | `/api/v1/transfers/{transferId}/reject` | 3 | Reject transfer with documented reason | 4 | Bearer | 5 | `PERM-072` | 6 | `Authorization`, `Content-Type` | 7 | `transferId` | 8 | — | 9 | `rejectionReason` (required) | 10 | VR-131; status `REQUESTED` | 11 | `CommandResultResponse` | 12 | 400,403,404 | 13 | **200** | 14 | — | 15 | UC-032 |
**16–18** POST reject with reason → 200; 400 missing `rejectionReason`

### API-103: Dispatch Transfer
| 1 | `POST` | 2 | `/api/v1/transfers/{transferId}/dispatch` | 3 | Dispatch from source; create in-transit state | 4 | Bearer | 5 | `PERM-073` (`WH_MGR`) | 6 | `Authorization`, `Content-Type`, `Idempotency-Key` | 7 | `transferId` | 8 | — | 9 | `dispatchLines[]` (min 1) | 10 | VR-133; status `APPROVED`; source not frozen; dispatched ≤ approved | 11 | `StockTransferDetailResponse` (`status: IN_TRANSIT`) | 12 | 400,403,404,422 | 13 | **200** | 14 | — | 15 | UC-033 |
**16–18** POST dispatch lines → 200 in-transit; 422 location frozen

### API-104: Confirm Transfer Receipt
| 1 | `POST` | 2 | `/api/v1/transfers/{transferId}/receive` | 3 | Confirm receipt at destination | 4 | Bearer | 5 | `PERM-074` (`WH_MGR`) | 6 | `Authorization`, `Content-Type`, `Idempotency-Key` | 7 | `transferId` | 8 | — | 9 | `receiptLines[]` (min 1); optional `varianceNotes` | 10 | VR-134, VR-135; status `IN_TRANSIT`; variance notes when qty mismatch | 11 | `StockTransferDetailResponse` (`status: RECEIVED`) | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-020** (variance) | 15 | UC-033 |
**16–18** POST receipt lines → 200 received; 422 if not in-transit

### API-105: Cancel In-Transit Transfer
| 1 | `POST` | 2 | `/api/v1/transfers/{transferId}/cancel` | 3 | Cancel in-transit transfer with reversal | 4 | Bearer | 5 | `PERM-073` | 6 | `Authorization`, `Content-Type` | 7 | `transferId` | 8 | — | 9 | `cancellationReason` (required) | 10 | Eligible in-transit status | 11 | `CommandResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | — | 15 | UC-033 |
**16–18** POST cancel → 200; 422 if not cancellable state

### API-106: List Pending Transfer Approvals
| 1 | `GET` | 2 | `/api/v1/transfers/pending-approvals` | 3 | Approval queue for transfers | 4 | Bearer | 5 | `PERM-072` | 6 | `Authorization` | 7 | — | 8 | `sourceLocationCode`, `page`, `pageSize` | 9 | — | 10 | VR-136; network scope | 11 | `PagedResponse<StockTransferSummaryResponse>` | 12 | 401,403 | 13 | **200** | 14 | — | 15 | UC-032, UC-047 |
**16–18** GET pending queue → 200 paged list

### API-107: List In-Transit Transfers
| 1 | `GET` | 2 | `/api/v1/transfers/in-transit` | 3 | In-transit pipeline by location | 4 | Bearer | 5 | `PERM-075` | 6 | `Authorization` | 7 | — | 8 | `locationCode`, `overdueOnly`, `page`, `pageSize` | 9 | — | 10 | VR-137 overdue filter; location scope | 11 | `PagedResponse<InTransitTransferResponse>` | 12 | 401,403 | 13 | **200** | 14 | — | 15 | UC-030, UC-033 |
**16–18** GET `?locationCode=WH-EAST&overdueOnly=true` → 200 pipeline

---

## M-09 — Inventory Accuracy

### API-108: Schedule Cycle Count
| 1 | `POST` | 2 | `/api/v1/accuracy/cycle-counts` | 3 | Schedule cycle count assignment | 4 | Bearer | 5 | `PERM-037` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `locationCode`, `sku`, `scheduledDate`; optional `priority` | 10 | VR-067, VR-068; active location/product | 11 | `CycleCountAssignmentResponse` | 12 | 400,403,422 | 13 | **201** | 14 | **BR-018**, **BR-032** | 15 | UC-014 |
**16–18** POST schedule → 201 assignment id; 422 inactive SKU

### API-109: List Cycle Counts
| 1 | `GET` | 2 | `/api/v1/accuracy/cycle-counts` | 3 | List count assignments | 4 | Bearer | 5 | `PERM-037` | 6 | `Authorization` | 7 | — | 8 | `locationCode`, `status`, `startDate`, `endDate`, `page`, `pageSize` | 9 | — | 10 | Date range cross-field; user scope | 11 | `PagedResponse<CycleCountSummaryResponse>` | 12 | 400,401,403 | 13 | **200** | 14 | BR-018 | 15 | UC-014 |
**16–18** GET by location/status → 200 paged list

### API-110: Get Cycle Count Assignment
| 1 | `GET` | 2 | `/api/v1/accuracy/cycle-counts/{cycleCountId}` | 3 | Blind count assignment (no system qty) | 4 | Bearer | 5 | `PERM-038` | 6 | `Authorization` | 7 | `cycleCountId` | 8 | — | 9 | — | 10 | VR-069; response must not expose expected quantity | 11 | `CycleCountAssignmentResponse` (blind) | 12 | 401,403,404 | 13 | **200** | 14 | **BR-018** | 15 | UC-014 |
**17** `{ "cycleCountId": "...", "sku": "BOLT-M10", "locationCode": "WH-EAST", "status": "SCHEDULED" }` (no `expectedQuantity`)  
**18** 404 `NF_CYCLE_COUNT_NOT_FOUND`

### API-111: Submit Cycle Count Result
| 1 | `POST` | 2 | `/api/v1/accuracy/cycle-counts/{cycleCountId}/result` | 3 | Submit blind physical count result | 4 | Bearer | 5 | `PERM-038` | 6 | `Authorization`, `Content-Type` | 7 | `cycleCountId` | 8 | — | 9 | `physicalQuantity` (required) | 10 | VR-070; status scheduled/in-progress; counter ≠ approver (SoD) | 11 | `CycleCountResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-018** | 15 | UC-014 |
**16** POST `{ "physicalQuantity": { "amount": 98, "unitOfMeasure": "EA" } }`  
**17** `200` `{ "status": "VARIANCE_DETECTED", "varianceQuantity": { "amount": -2, "unitOfMeasure": "EA" } }`  
**18** `422` invalid count status

### API-112: Initiate Physical Inventory Count
| 1 | `POST` | 2 | `/api/v1/accuracy/physical-counts` | 3 | Wall-to-wall count; impose location freeze | 4 | Bearer | 5 | `PERM-039` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `locationCode`, `plannedStartDate`, `plannedEndDate` | 10 | VR-071; end ≥ start | 11 | `PhysicalCountResponse` | 12 | 400,403,409,422 | 13 | **201** | 14 | **BR-024** | 15 | UC-015 |
**16–18** POST physical count → 201 freeze active; 409 count already in progress

### API-113: Get Physical Count Status
| 1 | `GET` | 2 | `/api/v1/accuracy/physical-counts/{physicalCountId}` | 3 | Count progress and freeze window | 4 | Bearer | 5 | `PERM-039` | 6 | `Authorization` | 7 | `physicalCountId` | 8 | — | 9 | — | 10 | Exists | 11 | `PhysicalCountStatusResponse` | 12 | 401,403,404 | 13 | **200** | 14 | **BR-024** | 15 | UC-015 |
**17** `{ "physicalCountId": "...", "freezeActive": true, "completionPercent": 45 }`  
**18** 404 not found

### API-114: Record Physical Count Result
| 1 | `POST` | 2 | `/api/v1/accuracy/physical-counts/{physicalCountId}/results` | 3 | Submit line results during freeze | 4 | Bearer | 5 | `PERM-039` | 6 | `Authorization`, `Content-Type` | 7 | `physicalCountId` | 8 | — | 9 | `countLines[]` (min 1) | 10 | VR-070, VR-071; location frozen | 11 | `PhysicalCountResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-024** | 15 | UC-015 |
**16–18** POST count lines → 200; 422 if freeze not active

### API-115: Certify Physical Count
| 1 | `POST` | 2 | `/api/v1/accuracy/physical-counts/{physicalCountId}/certify` | 3 | Certify complete; release freeze | 4 | Bearer | 5 | `PERM-039` | 6 | `Authorization`, `Content-Type` | 7 | `physicalCountId` | 8 | — | 9 | optional `certificationNotes` | 10 | VR-072; all SKUs counted | 11 | `CommandResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-024** | 15 | UC-015 |
**16–18** POST certify → 200 freeze released; 422 incomplete count

### API-116: Open Adjustment Case
| 1 | `POST` | 2 | `/api/v1/accuracy/adjustment-cases` | 3 | Open case from variance or direct request | 4 | Bearer | 5 | `PERM-043` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `originType`, `locationCode`, `sku`, `reasonCode`; conditional `varianceId`, direction/qty | 10 | VR-077–VR-079 | 11 | `AdjustmentCaseResponse` | 12 | 400,403,422 | 13 | **201** | 14 | **BR-020**, **BR-022** | 15 | UC-016, UC-017 |
**16–18** POST case → 201 caseId

### API-117: Get Adjustment Case
| 1 | `GET` | 2 | `/api/v1/accuracy/adjustment-cases/{caseId}` | 3 | Case investigation and approval state | 4 | Bearer | 5 | `PERM-040` | 6 | `Authorization` | 7 | `caseId` | 8 | — | 9 | — | 10 | Exists | 11 | `AdjustmentCaseDetailResponse` | 12 | 401,403,404 | 13 | **200** | 14 | — | 15 | UC-016, UC-017 |
**16–18** GET → 200 case detail

### API-118: Investigate Variance
| 1 | `POST` | 2 | `/api/v1/accuracy/adjustment-cases/{caseId}/investigate` | 3 | Document root cause investigation | 4 | Bearer | 5 | `PERM-041` | 6 | `Authorization`, `Content-Type` | 7 | `caseId` | 8 | — | 9 | `rootCauseCategory`, `investigationFindings` | 10 | VR-076; findings 1–5000 chars | 11 | `AdjustmentCaseResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-022** | 15 | UC-016 |
**16–18** POST investigation → 200; 422 if investigation already complete

### API-119: Approve Count Variance
| 1 | `POST` | 2 | `/api/v1/accuracy/adjustment-cases/{caseId}/variances/{varianceId}/approve` | 3 | Approve variance with independent approver | 4 | Bearer | 5 | `PERM-042` | 6 | `Authorization`, `Content-Type` | 7 | `caseId`, `varianceId` | 8 | — | 9 | `approvedAdjustmentQuantity` | 10 | VR-075; approver ≠ counter | 11 | `CommandResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-019** | 15 | UC-016 |
**16–18** POST approve variance → 200; 422 `BIZ_SEGREGATION_OF_DUTIES`

### API-120: Submit Adjustment for Approval
| 1 | `POST` | 2 | `/api/v1/accuracy/adjustment-cases/{caseId}/submit` | 3 | Submit adjustment/write-off for governance approval | 4 | Bearer | 5 | `PERM-043`, `PERM-045` | 6 | `Authorization`, `Content-Type` | 7 | `caseId` | 8 | — | 9 | `adjustmentType`, `quantity`, `reasonCode`; optional `evidenceReference` | 10 | VR-077, VR-080, VR-081; write-off evidence required | 11 | `AdjustmentCaseResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-020**, **BR-023** | 15 | UC-017, UC-018 |
**16–18** POST submit → 200 pending approval

### API-121: Approve Adjustment
| 1 | `POST` | 2 | `/api/v1/accuracy/adjustment-cases/{caseId}/approve` | 3 | Approve adjustment after threshold validation | 4 | Bearer | 5 | `PERM-044`, `PERM-046` | 6 | `Authorization`, `Content-Type` | 7 | `caseId` | 8 | — | 9 | optional `approvalNotes`, `approvedQuantity` | 10 | VR-083; approver ≠ initiator and counter | 11 | `CommandResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-021** | 15 | UC-017, UC-018 |
**16** POST approve  
**17** `200` `{ "caseId": "...", "status": "APPROVED" }`  
**18** `422 BIZ_SEGREGATION_OF_DUTIES`

### API-122: Reject Adjustment
| 1 | `POST` | 2 | `/api/v1/accuracy/adjustment-cases/{caseId}/reject` | 3 | Reject proposed adjustment | 4 | Bearer | 5 | `PERM-044` | 6 | `Authorization`, `Content-Type` | 7 | `caseId` | 8 | — | 9 | `rejectionReason` (required, 1–2000) | 10 | Case in pending approval | 11 | `CommandResultResponse` | 12 | 400,403,404 | 13 | **200** | 14 | — | 15 | UC-017, UC-018 |
**16–18** POST reject → 200

### API-123: List Pending Approvals
| 1 | `GET` | 2 | `/api/v1/accuracy/pending-approvals` | 3 | Adjustment cases awaiting approval | 4 | Bearer | 5 | `PERM-044`, `PERM-046` | 6 | `Authorization` | 7 | — | 8 | `caseType`, `locationCode`, `page`, `pageSize` | 9 | — | 10 | User location scope | 11 | `PagedResponse<AdjustmentCaseSummaryResponse>` | 12 | 401,403 | 13 | **200** | 14 | — | 15 | UC-016, UC-017, UC-047 |
**16–18** GET approval queue → 200 paged list

---

## M-10 — Returns Management

### API-124: Issue Return Authorization
| 1 | `POST` | 2 | `/api/v1/returns/authorizations` | 3 | Issue RMA linked to original order | 4 | Bearer | 5 | `PERM-077` (`CS_REP`) | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `originalOrderId`, `returnReason`, `lines[]` | 10 | VR-142, VR-143; qty ≤ shipped; order return-eligible | 11 | `ReturnAuthorizationResponse` | 12 | 400,403,404,422 | 13 | **201** | 14 | **BR-025** | 15 | UC-035 |
**16** POST RMA for order line  
**17** `201` `{ "returnAuthorizationId": "RMA-2026-001", "status": "AUTHORIZED" }`  
**18** `422` no valid order reference

### API-125: List Return Authorizations
| 1 | `GET` | 2 | `/api/v1/returns/authorizations` | 3 | List RMAs with status filter | 4 | Bearer | 5 | `PERM-082` | 6 | `Authorization` | 7 | — | 8 | `status`, `originalOrderId`, `page`, `pageSize` | 9 | — | 10 | Query filters | 11 | `PagedResponse<ReturnAuthorizationSummaryResponse>` | 12 | 401,403 | 13 | **200** | 14 | BR-025 | 15 | UC-035, UC-036 |
**16–18** GET `?status=AUTHORIZED` → 200 paged list

### API-126: Get Return Authorization
| 1 | `GET` | 2 | `/api/v1/returns/authorizations/{returnAuthorizationId}` | 3 | RMA detail and order reference | 4 | Bearer | 5 | `PERM-082` | 6 | `Authorization` | 7 | `returnAuthorizationId` | 8 | — | 9 | — | 10 | VR-149; exists | 11 | `ReturnAuthorizationDetailResponse` | 12 | 401,403,404 | 13 | **200** | 14 | **BR-025** | 15 | UC-035 |
**16–18** GET → 200 detail; 404 not found

### API-127: Cancel Return Authorization
| 1 | `POST` | 2 | `/api/v1/returns/authorizations/{returnAuthorizationId}/cancel` | 3 | Cancel unused RMA | 4 | Bearer | 5 | `PERM-077` | 6 | `Authorization`, `Content-Type` | 7 | `returnAuthorizationId` | 8 | — | 9 | `cancellationReason` (required) | 10 | Open/unused RMA only | 11 | `CommandResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | — | 15 | UC-035 |
**16–18** POST cancel → 200; 422 if already received

### API-128: Receive Customer Return
| 1 | `POST` | 2 | `/api/v1/returns/{returnId}/receive` | 3 | Record physical receipt of return | 4 | Bearer | 5 | `PERM-078` | 6 | `Authorization`, `Content-Type` | 7 | `returnId` | 8 | — | 9 | `receivingLocationCode`, `receivedLines[]` | 10 | VR-144, VR-145; SKU matches auth; qty ≤ authorized | 11 | `CustomerReturnCaseResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-025** | 15 | UC-036 |
**16–18** POST receive lines → 200; 422 qty exceeds authorized

### API-129: Inspect Returned Goods
| 1 | `POST` | 2 | `/api/v1/returns/{returnId}/inspect` | 3 | Inspect and record condition grade | 4 | Bearer | 5 | `PERM-079` | 6 | `Authorization`, `Content-Type` | 7 | `returnId` | 8 | — | 9 | `inspectionLines[]` (min 1) | 10 | VR-146; inspect before restock | 11 | `InspectionResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-026** | 15 | UC-036 |
**16–18** POST inspection grades → 200

### API-130: Disposition Return
| 1 | `POST` | 2 | `/api/v1/returns/{returnId}/disposition` | 3 | Route to restock, quarantine, or write-off | 4 | Bearer | 5 | `PERM-080`, `PERM-081` | 6 | `Authorization`, `Content-Type` | 7 | `returnId` | 8 | — | 9 | `dispositionAction`, `dispositionLines[]` | 10 | VR-147, VR-148; sum = inspected qty; write-off refs | 11 | `DispositionResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-023**, **BR-026** | 15 | UC-036 |
**16–18** POST RESTOCK/WRITE_OFF disposition → 200

### API-131: List Pending Return Receipts
| 1 | `GET` | 2 | `/api/v1/returns/pending-receipts` | 3 | Authorized returns awaiting receipt | 4 | Bearer | 5 | `PERM-078` | 6 | `Authorization` | 7 | — | 8 | `locationCode`, `page`, `pageSize` | 9 | — | 10 | User location scope | 11 | `PagedResponse<PendingReturnReceiptResponse>` | 12 | 401,403 | 13 | **200** | 14 | — | 15 | UC-036 |
**16–18** GET pending receipts → 200 paged list

---

## M-11 — Commercial Campaign

### API-132: Create Promotional Allocation
| 1 | `POST` | 2 | `/api/v1/campaigns/allocations` | 3 | Create ring-fenced promotional allocation | 4 | Bearer | 5 | `PERM-093` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `campaignId`, `campaignName`, `locationCode`, `sku`, `allocatedQuantity`, `campaignStartDate`, `campaignEndDate` | 10 | VR-126, VR-127; allocated ≤ ATP; end ≥ start | 11 | `PromotionalAllocationResponse` | 12 | 400,403,422 | 13 | **201** | 14 | **BR-029** | 15 | UC-040 |
**16** POST allocation 500 EA ring-fence  
**17** `201` allocation with `allocationId`  
**18** `422 BIZ_PROMOTIONAL_RING_FENCE` exceeds ATP

### API-133: List Promotional Allocations
| 1 | `GET` | 2 | `/api/v1/campaigns/allocations` | 3 | List allocations by campaign/status | 4 | Bearer | 5 | `PERM-092` | 6 | `Authorization` | 7 | — | 8 | `campaignId`, `status`, `locationCode`, `page`, `pageSize` | 9 | — | 10 | User scope | 11 | `PagedResponse<PromotionalAllocationSummaryResponse>` | 12 | 401,403 | 13 | **200** | 14 | BR-029 | 15 | UC-040 |
**16–18** GET allocations → 200 paged list

### API-134: Get Promotional Allocation
| 1 | `GET` | 2 | `/api/v1/campaigns/allocations/{allocationId}` | 3 | Allocation detail and ring-fenced qty | 4 | Bearer | 5 | `PERM-092` | 6 | `Authorization` | 7 | `allocationId` | 8 | — | 9 | — | 10 | Exists; user scope | 11 | `PromotionalAllocationDetailResponse` | 12 | 401,403,404 | 13 | **200** | 14 | **BR-029** | 15 | UC-040 |
**16–18** GET → 200 detail

### API-135: Amend Promotional Allocation
| 1 | `PATCH` | 2 | `/api/v1/campaigns/allocations/{allocationId}` | 3 | Amend quantity or campaign period | 4 | Bearer | 5 | `PERM-093` | 6 | `Authorization`, `Content-Type` | 7 | `allocationId` | 8 | — | 9 | `amendmentReason`; ≥1 of `allocatedQuantity`, dates | 10 | VR-127; increased qty ≤ ATP | 11 | `PromotionalAllocationResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-029** | 15 | UC-040 |
**16–18** PATCH amend → 200

### API-136: Evaluate Campaign Readiness
| 1 | `POST` | 2 | `/api/v1/campaigns/allocations/{allocationId}/readiness` | 3 | Evaluate stock readiness before launch | 4 | Bearer | 5 | `PERM-092` | 6 | `Authorization`, `Content-Type` | 7 | `allocationId` | 8 | — | 9 | optional `targetQuantity` | 10 | VR-126; defaults to allocated qty | 11 | `CampaignReadinessResponse` | 12 | 400,403,404 | 13 | **200** | 14 | BR-029 | 15 | UC-040, UC-047 |
**17** `{ "ready": true, "shortfallQuantity": null }`  
**18** 404 allocation not found

### API-137: Release Promotional Allocation
| 1 | `POST` | 2 | `/api/v1/campaigns/allocations/{allocationId}/release` | 3 | Release unconsumed ring-fence after campaign | 4 | Bearer | 5 | `PERM-093` | 6 | `Authorization`, `Content-Type` | 7 | `allocationId` | 8 | — | 9 | `releaseReason` (enum) | 10 | Allocation releasable state | 11 | `CommandResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-029** | 15 | UC-040 |
**16–18** POST release → 200 ATP restored

### API-138: Authorize Promotional Override
| 1 | `POST` | 2 | `/api/v1/campaigns/allocations/{allocationId}/override` | 3 | Override ring-fence for non-promotional order | 4 | Bearer | 5 | `PERM-093` | 6 | `Authorization`, `Content-Type` | 7 | `allocationId` | 8 | — | 9 | `orderId`, `overrideQuantity`, `authorizationReference`, `justification` | 10 | Override ≤ ring-fenced remaining | 11 | `PromotionalOverrideResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | **BR-029** | 15 | UC-040 |
**16–18** POST override → 200; 422 exceeds ring-fence

### API-139: Check Ring-Fence Status
| 1 | `GET` | 2 | `/api/v1/campaigns/ring-fence/{locationCode}/{sku}` | 3 | Check active promotional ring-fence | 4 | Bearer | 5 | `PERM-092`, `PERM-051` | 6 | `Authorization` | 7 | `locationCode`, `sku` | 8 | `asOfDate` | 9 | — | 10 | BR-029 active allocation check | 11 | `RingFenceStatusResponse` | 12 | 401,403,404 | 13 | **200** | 14 | **BR-029** | 15 | UC-022, UC-040 |
**17** `{ "ringFenced": true, "allocatedQuantity": { "amount": 500, "unitOfMeasure": "EA" } }`  
**18** 404 unknown SKU/location

---

## M-12 — Identity & Access

### API-140: Provision User Account
| 1 | `POST` | 2 | `/api/v1/users` | 3 | Provision user with initial roles | 4 | Bearer | 5 | `PERM-095` (`SYS_ADMIN`) | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `userId`, `email`, `displayName`, `initialRoles[]` | 10 | VR-083; unique userId; no SoD in role set | 11 | `UserAccountResponse` | 12 | 400,403,409 | 13 | **201** | 14 | — | 15 | UC-044 |
**16–18** POST user → 201; 409 duplicate userId

### API-141: List User Accounts
| 1 | `GET` | 2 | `/api/v1/users` | 3 | List users with role/status filters | 4 | Bearer | 5 | `PERM-095` | 6 | `Authorization` | 7 | — | 8 | `status`, `roleCode`, `page`, `pageSize` | 9 | — | 10 | Pagination | 11 | `PagedResponse<UserAccountSummaryResponse>` | 12 | 401,403 | 13 | **200** | 14 | — | 15 | UC-044 |
**16–18** GET users → 200 paged list

### API-142: Get User Account
| 1 | `GET` | 2 | `/api/v1/users/{userId}` | 3 | User profile and role assignments | 4 | Bearer | 5 | `PERM-095` or self (`PERM-062`) | 6 | `Authorization` | 7 | `userId` | 8 | — | 9 | — | 10 | Exists; self-access allowed | 11 | `UserAccountDetailResponse` | 12 | 401,403,404 | 13 | **200** | 14 | — | 15 | UC-044, UC-045 |
**16–18** GET own profile → 200; 403 if non-admin reads other user

### API-143: Assign Role
| 1 | `POST` | 2 | `/api/v1/users/{userId}/roles` | 3 | Assign role with location scope | 4 | Bearer | 5 | `PERM-096` | 6 | `Authorization`, `Content-Type` | 7 | `userId` | 8 | — | 9 | `roleAssignment: { roleCode, locationCodes[], effectiveFrom }` | 10 | VR-083; account active; no SoD conflict | 11 | `RoleAssignmentResponse` | 12 | 400,403,404,422 | 13 | **201** | 14 | — | 15 | UC-044, UC-045 |
**16** POST `{ "roleAssignment": { "roleCode": "WAREHOUSE_MANAGER", "locationCodes": ["WH-EAST"], "effectiveFrom": "2026-07-06" } }`  
**17** `201` role assignment id  
**18** `403 AUTHZ_ROLE_ASSIGNMENT_DENIED`

### API-144: Revoke Role Assignment
| 1 | `DELETE` | 2 | `/api/v1/users/{userId}/roles/{roleAssignmentId}` | 3 | Revoke role from user | 4 | Bearer | 5 | `PERM-096` | 6 | `Authorization` | 7 | `userId`, `roleAssignmentId` | 8 | — | 9 | — | 10 | Assignment exists on user | 11 | `CommandResultResponse` | 12 | 401,403,404 | 13 | **200** | 14 | — | 15 | UC-044 |
**16–18** DELETE assignment → 200

### API-145: Suspend User Account
| 1 | `POST` | 2 | `/api/v1/users/{userId}/suspend` | 3 | Temporarily suspend access | 4 | Bearer | 5 | `PERM-095` | 6 | `Authorization`, `Content-Type` | 7 | `userId` | 8 | — | 9 | `suspensionReason` (required) | 10 | Account active | 11 | `CommandResultResponse` | 12 | 400,403,404,422 | 13 | **200** | 14 | — | 15 | UC-044 |
**16–18** POST suspend → 200

### API-146: Deactivate User Account
| 1 | `POST` | 2 | `/api/v1/users/{userId}/deactivate` | 3 | Permanently deactivate account | 4 | Bearer | 5 | `PERM-095` | 6 | `Authorization`, `Content-Type` | 7 | `userId` | 8 | — | 9 | `deactivationReason` (required) | 10 | Valid transition | 11 | `CommandResultResponse` | 12 | 400,403,404 | 13 | **200** | 14 | — | 15 | UC-044 |
**16–18** POST deactivate → 200

### API-147: Sync Users from Directory
| 1 | `POST` | 2 | `/api/v1/users/sync` | 3 | HR directory identity sync | 4 | Bearer | 5 | `PERM-095` | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `syncMode` (`FULL`/`INCREMENTAL`); `sinceTimestamp` when incremental | 10 | Cross-field incremental requires timestamp | 11 | `UserSyncResultResponse` | 12 | 400,403,500 | 13 | **200** | 14 | — | 15 | UC-044 |
**16–18** POST `{ "syncMode": "INCREMENTAL", "sinceTimestamp": "2026-07-01T00:00:00Z" }` → 200 sync summary

### API-148: Evaluate Authorization
| 1 | `POST` | 2 | `/api/v1/authorization/actions/evaluate` | 3 | Pre-check if user may execute command | 4 | Bearer | 5 | authenticated (`PERM-062` self) | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `action` (required); optional `userId`, `locationCode` | 10 | VR-008; user defaults to caller | 11 | `{ "permitted": true, "denialReason": null }` | 12 | 400,401 | 13 | **200** | 14 | — | 15 | UC-045 |
**16–18** POST evaluate → 200 `{ "permitted": false, "denialReason": "AUTHZ_LOCATION_SCOPE_DENIED" }`

### API-149: Validate Location Scope
| 1 | `POST` | 2 | `/api/v1/authorization/location-scope/validate` | 3 | Validate user authorized for location | 4 | Bearer | 5 | authenticated | 6 | `Authorization`, `Content-Type` | 7 | — | 8 | — | 9 | `locationCode` (required) | 10 | VR-008, VR-053; location exists | 11 | `{ "authorized": true, "locationCode": "WH-EAST" }` | 12 | 400,401,404 | 13 | **200** | 14 | — | 15 | UC-045 |
**16–18** POST validate → 200 authorized flag

---

## M-13 — Inventory Intelligence

*Read-only projections unless noted. Auth=Bearer; Headers=`Authorization`; Body=none for GET; standard errors 400,401,403,500.*

### API-150: Get Inventory Dashboard
| 1 | `GET` | 2 | `/api/v1/intelligence/dashboard` | 3 | Inventory summary dashboard | 4 | Bearer | 5 | `PERM-083` | 6 | `Authorization` | 7 | — | 8 | `scope` (`NETWORK`/`LOCATION`), `locationCode` (when scope=LOCATION) | 9 | — | 10 | VR-151; location required when scoped | 11 | `InventoryDashboardResponse` | 12 | 400,401,403 | 13 | **200** | 14 | — | 15 | UC-037 |
**16–18** GET `?scope=LOCATION&locationCode=WH-EAST` → 200 dashboard widgets

### API-151: Get Stock Status Summary
| 1 | `GET` | 2 | `/api/v1/intelligence/stock-status/summary` | 3 | Aggregated on-hand, ATP, status counts | 4 | Bearer | 5 | `PERM-083` | 6 | `Authorization` | 7 | — | 8 | `locationCode`, `categoryCode`, `abcClass` | 9 | — | 10 | VR-151 authorized locations | 11 | `StockStatusSummaryResponse` | 12 | 401,403 | 13 | **200** | 14 | — | 15 | UC-012, UC-037 |
**16–18** GET summary → 200 aggregates

### API-152: Get Stock Status Board
| 1 | `GET` | 2 | `/api/v1/intelligence/stock-status/board` | 3 | Network stock status health board | 4 | Bearer | 5 | `PERM-085` | 6 | `Authorization` | 7 | — | 8 | `locationCodes[]`, `stockStatus`, `page`, `pageSize` | 9 | — | 10 | VR-151 | 11 | `PagedResponse<StockStatusBoardItemResponse>` | 12 | 401,403 | 13 | **200** | 14 | **BR-009** | 15 | UC-012, UC-037 |
**16–18** GET board → 200 paged health indicators

### API-153: Get Availability Inquiry Log
| 1 | `GET` | 2 | `/api/v1/intelligence/availability/inquiries` | 3 | Sales availability inquiry accountability log | 4 | Bearer | 5 | `PERM-018` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate`, `sku`, `userId`, `page`, `pageSize` | 9 | — | 10 | VR-062 date range | 11 | `PagedResponse<AvailabilityInquiryLogEntryResponse>` | 12 | 400,401,403 | 13 | **200** | 14 | **BR-001** | 15 | UC-013, UC-021 |
**16–18** GET inquiry log → 200 paged entries

### API-154: Get Quarantine Register
| 1 | `GET` | 2 | `/api/v1/intelligence/quarantine-register` | 3 | Quarantine and hold register | 4 | Bearer | 5 | `PERM-047` | 6 | `Authorization` | 7 | — | 8 | `locationCode`, `holdReason`, `page`, `pageSize` | 9 | — | 10 | Hold reason enum; location scope | 11 | `PagedResponse<QuarantineRegisterEntryResponse>` | 12 | 401,403 | 13 | **200** | 14 | **BR-013** | 15 | UC-019, UC-037 |
**16–18** GET register → 200 quarantine entries

### API-155: Search Movement History

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/intelligence/movements` |
| **3** | **Purpose** | Search inventory movement history by SKU, location, user, date |
| **4** | **Authentication** | Required — Bearer JWT |
| **5** | **Required Permission** | `PERM-023`, `PERM-084` |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | `startDate`, `endDate` (required); `sku`, `locationCode`, `userId`, `movementType`, `page`, `pageSize` |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | VR-153 date range; VR-154 at least one filter recommended; max 365-day range |
| **11** | **Success Response** | `PagedResponse<MovementHistoryEntryResponse>` |
| **12** | **Error Responses** | 400 invalid date range; 401; 403 location scope |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | Audit history — immutable projection |
| **15** | **Related Use Case** | UC-042 |

**16** `GET /api/v1/intelligence/movements?startDate=2026-07-01&endDate=2026-07-06&sku=BOLT-M10`  
**17** `200` paged movement entries with `movementType`, `quantity`, `performedBy`  
**18** `400 VAL_INVALID_DATE_RANGE`

### API-156: Query Audit Trail
| 1 | `GET` | 2 | `/api/v1/intelligence/audit-trail` | 3 | Immutable audit trail of inventory changes | 4 | Bearer | 5 | `PERM-098` (audit roles only) | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate`, `entityType`, `entityId`, `userId`, `page`, `pageSize` | 9 | — | 10 | VR-153; date range required | 11 | `PagedResponse<AuditTrailEntryResponse>` | 12 | 401,403 | 13 | **200** | 14 | S5 sensitive audit access | 15 | UC-043, UC-041 |
**18** `403 AUTHZ_INSUFFICIENT_PERMISSION` for operational roles

### API-157: Export Audit Evidence
| 1 | `GET` | 2 | `/api/v1/intelligence/audit-trail/export` | 3 | Export audit evidence package | 4 | Bearer | 5 | `PERM-099` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate`, `format` (`PDF`/`CSV`), `locationCodes[]` | 9 | — | 10 | VR-153, VR-154; max 365-day range | 11 | `ExportJobResponse` or file stream | 12 | 400,401,403 | 13 | **200** / **202** | 14 | S5 formal audit export | 15 | UC-041, UC-043 |
**16–18** GET export → 202 async job id; 400 range too large

### API-158: Get Operational Alerts
| 1 | `GET` | 2 | `/api/v1/intelligence/alerts` | 3 | Active operational alerts for user scope | 4 | Bearer | 5 | `PERM-064` | 6 | `Authorization` | 7 | — | 8 | `alertType`, `severity`, `locationCode`, `acknowledged`, `page`, `pageSize` | 9 | — | 10 | Enums; location scope | 11 | `PagedResponse<OperationalAlertResponse>` | 12 | 401,403 | 13 | **200** | 14 | **BR-009** | 15 | UC-028, UC-047 |
**16–18** GET alerts → 200 paged alerts

### API-159: Acknowledge Operational Alert
| 1 | `POST` | 2 | `/api/v1/intelligence/alerts/{alertId}/acknowledge` | 3 | Acknowledge alert (no stock mutation) | 4 | Bearer | 5 | `PERM-065` | 6 | `Authorization`, `Content-Type` | 7 | `alertId` | 8 | — | 9 | `actionTaken` (`REQUISITION`/`TRANSFER`/`DISMISS`/`DEFER`); `acknowledgmentNotes` when DISMISS/DEFER | 10 | VR-113–VR-115 | 11 | `CommandResultResponse` | 12 | 400,401,403,404 | 13 | **200** | 14 | BR-009 alert workflow | 15 | UC-028, UC-047 |
**16** POST `{ "actionTaken": "TRANSFER", "acknowledgmentNotes": "Transfer TRF-0042 raised" }`  
**17** `200` `{ "alertId": "...", "acknowledged": true }`  
**18** `400` missing notes for DISMISS

### API-160: Get Replenishment Recommendations
| 1 | `GET` | 2 | `/api/v1/intelligence/replenishment/recommendations` | 3 | Replenishment recommendation log | 4 | Bearer | 5 | `PERM-066` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate`, `locationCode`, `recommendationAction`, `page`, `pageSize` | 9 | — | 10 | Date range; location scope | 11 | `PagedResponse<ReplenishmentRecommendationResponse>` | 12 | 400,401,403 | 13 | **200** | 14 | **BR-009**, **BR-011** | 15 | UC-028, UC-029, UC-034 |
**16–18** GET recommendations → 200 paged list

### API-161: Get Open Purchase Order Board
| 1 | `GET` | 2 | `/api/v1/intelligence/procurement/open-pos` | 3 | Open PO board for inbound pipeline | 4 | Bearer | 5 | `PERM-035` | 6 | `Authorization` | 7 | — | 8 | `locationCode`, `supplierCode`, `overdueOnly`, `page`, `pageSize` | 9 | — | 10 | VR-034 location scope; VR-123 overdue | 11 | `PagedResponse<OpenPurchaseOrderBoardItemResponse>` | 12 | 401,403 | 13 | **200** | 14 | — | 15 | UC-006, UC-030 |
**16–18** GET open POs → 200 board

### API-162: Get Inbound Supply Calendar
| 1 | `GET` | 2 | `/api/v1/intelligence/procurement/inbound-calendar` | 3 | Expected inbound supply calendar | 4 | Bearer | 5 | `PERM-027` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate` (required), `locationCode` | 9 | — | 10 | VR-033; max 90-day range | 11 | `InboundSupplyCalendarResponse` | 12 | 400,401,403 | 13 | **200** | 14 | — | 15 | UC-007, UC-030 |
**16–18** GET calendar → 200 delivery schedule

### API-163: Get Inbound Delivery Delays
| 1 | `GET` | 2 | `/api/v1/intelligence/procurement/inbound-delays` | 3 | Inbound delivery delay log | 4 | Bearer | 5 | `PERM-036` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate`, `supplierCode`, `locationCode`, `page`, `pageSize` | 9 | — | 10 | Date range; location scope | 11 | `PagedResponse<InboundDelayLogEntryResponse>` | 12 | 400,401,403 | 13 | **200** | 14 | — | 15 | UC-030, UC-047 |
**16–18** GET delays → 200 paged log

### API-164: Get Backorder Pipeline
| 1 | `GET` | 2 | `/api/v1/intelligence/fulfillment/backorders` | 3 | Backorder pipeline by policy priority | 4 | Bearer | 5 | `PERM-058` | 6 | `Authorization` | 7 | — | 8 | `locationCode`, `prioritySort`, `page`, `pageSize` | 9 | — | 10 | VR-102; location scope | 11 | `PagedResponse<BackorderPipelineItemResponse>` | 12 | 401,403 | 13 | **200** | 14 | **BR-028** | 15 | UC-025, UC-027 |
**16–18** GET backorders → 200 priority-sorted pipeline

### API-165: Get Fulfillment Exceptions
| 1 | `GET` | 2 | `/api/v1/intelligence/fulfillment/exceptions` | 3 | Open fulfillment exception log | 4 | Bearer | 5 | `PERM-059` | 6 | `Authorization` | 7 | — | 8 | `exceptionType`, `status`, `startDate`, `endDate`, `page`, `pageSize` | 9 | — | 10 | Enums; date range | 11 | `PagedResponse<FulfillmentExceptionLogEntryResponse>` | 12 | 400,401,403 | 13 | **200** | 14 | **BR-003** | 15 | UC-026, UC-027 |
**16–18** GET exceptions → 200 paged log

### API-166: Get Network Imbalance Analysis
| 1 | `GET` | 2 | `/api/v1/intelligence/network/imbalance` | 3 | Network imbalance and transfer recommendations | 4 | Bearer | 5 | `PERM-076` | 6 | `Authorization` | 7 | — | 8 | `sku`, `locationCodes[]` | 9 | — | 10 | VR-139; active locations/SKU | 11 | `NetworkImbalanceAnalysisResponse` | 12 | 401,403 | 13 | **200** | 14 | **BR-011** | 15 | UC-034 |
**16–18** GET imbalance → 200 surplus/deficit analysis

### API-167: Get Shrinkage Analysis
| 1 | `GET` | 2 | `/api/v1/intelligence/accuracy/shrinkage` | 3 | Shrinkage, loss, obsolete stock analysis | 4 | Bearer | 5 | `PERM-049` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate` (required), `locationCode`, `reasonCode` | 9 | — | 10 | VR-086, VR-087; financial sensitivity (S4) | 11 | `ShrinkageAnalysisResponse` | 12 | 401,403 | 13 | **200** | 14 | **BR-020** | 15 | UC-020 |
**16–18** GET shrinkage → 200 analysis; 403 for warehouse staff

### API-168: Get Count Performance Metrics
| 1 | `GET` | 2 | `/api/v1/intelligence/accuracy/count-performance` | 3 | Cycle/physical count accuracy metrics | 4 | Bearer | 5 | `PERM-086` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate`, `locationCode`, `countType` | 9 | — | 10 | VR-157, VR-158; exclude pending variances default | 11 | `CountPerformanceMetricsResponse` | 12 | 400,401,403 | 13 | **200** | 14 | **BR-018** | 15 | UC-014, UC-015, UC-037 |
**16–18** GET metrics → 200 accuracy KPIs

### API-169: Get Campaign Readiness Status
| 1 | `GET` | 2 | `/api/v1/intelligence/campaigns/readiness` | 3 | Promotional campaign readiness status | 4 | Bearer | 5 | `PERM-092` | 6 | `Authorization` | 7 | — | 8 | `campaignId`, `daysUntilStart` | 9 | — | 10 | VR-126; campaignId max 50 chars | 11 | `CampaignReadinessStatusResponse` | 12 | 401,403 | 13 | **200** | 14 | **BR-029** | 15 | UC-040, UC-047 |
**16–18** GET readiness → 200 campaign status rollup

### API-170: Get Inventory KPIs
| 1 | `GET` | 2 | `/api/v1/intelligence/kpis` | 3 | Executive inventory performance KPIs | 4 | Bearer | 5 | `PERM-088` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate`, `locationCodes[]`, `kpiCodes[]` | 9 | — | 10 | VR-151, VR-161, VR-162 | 11 | `InventoryKpiDashboardResponse` | 12 | 400,401,403 | 13 | **200** | 14 | — | 15 | UC-038 |
**16–18** GET KPIs → 200 executive metrics

### API-171: Get Valuation Snapshots
| 1 | `GET` | 2 | `/api/v1/intelligence/valuation/snapshots` | 3 | Period-end inventory valuation snapshots | 4 | Bearer | 5 | `PERM-090` | 6 | `Authorization` | 7 | — | 8 | `startDate`, `endDate`, `locationCode`, `page`, `pageSize` | 9 | — | 10 | Date range; finance/audit only (S4) | 11 | `PagedResponse<ValuationSnapshotResponse>` | 12 | 401,403 | 13 | **200** | 14 | Unit cost exposure | 15 | UC-039 |
**16–18** GET snapshots → 200 paged valuations; 403 ops roles

### API-172: Get Valuation Reconciliation
| 1 | `GET` | 2 | `/api/v1/intelligence/valuation/reconciliation` | 3 | Inventory vs. GL reconciliation report | 4 | Bearer | 5 | `PERM-094` (`CFO`, `FIN_MGR`) | 6 | `Authorization` | 7 | — | 8 | `periodEndDate` (required), `varianceThresholdPercent` | 9 | — | 10 | VR period end; threshold 0–100 | 11 | `ValuationReconciliationResponse` | 12 | 400,401,403 | 13 | **200** | 14 | **BR-008** finance alignment | 15 | UC-039 |
**16** GET `?periodEndDate=2026-06-30&varianceThresholdPercent=2`  
**17** `200` reconciliation with variances above threshold  
**18** `403 AUTHZ_INSUFFICIENT_PERMISSION`

---

## Platform & Integration

### API-173: Get Session

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/auth/session` |
| **3** | **Purpose** | Validate session and return user context |
| **4** | **Authentication** | Required — Bearer JWT (any authenticated user) |
| **5** | **Required Permission** | — (authenticated principal) |
| **6** | **Request Headers** | `Authorization` |
| **7** | **Path Parameters** | None |
| **8** | **Query Parameters** | `includePermissions` (bool), `includeLocationScope` (bool, default true) |
| **9** | **Request Body** | None |
| **10** | **Validation Rules** | VR-008 via token |
| **11** | **Success Response** | `SessionResponse` — `userId`, `roles[]`, `locationScope[]`, optional `permissions[]` |
| **12** | **Error Responses** | 401 token expired/invalid |
| **13** | **HTTP Status Codes** | **200 OK** |
| **14** | **Business Rules Applied** | — |
| **15** | **Related Use Case** | UC-045 |

**16** `GET /api/v1/auth/session?includePermissions=true`  
**17** `{ "userId": "wh.manager", "roles": ["WAREHOUSE_MANAGER"], "locationScope": ["WH-EAST"], "permissions": ["PERM-052"] }`  
**18** `401 AUTH_TOKEN_EXPIRED`

### API-174: Logout
| 1 | `POST` | 2 | `/api/v1/auth/logout` | 3 | Terminate authenticated session | 4 | Bearer | 5 | — (authenticated) | 6 | `Authorization`, optional `Content-Type` | 7 | — | 8 | — | 9 | optional `logoutAllSessions` (bool) | 10 | Empty body accepted | 11 | `{ "message": "Session terminated" }` | 12 | 401 | 13 | **200** | 14 | — | 15 | UC-045 |
**16** POST `{}` or `{ "logoutAllSessions": true }`  
**17** `200` session terminated  
**18** `401` invalid token

### API-175: Health Check

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `GET` |
| **2** | **URL** | `/api/v1/health` |
| **3** | **Purpose** | Application health for operations monitoring |
| **4** | **Authentication** | **None** (public) |
| **5** | **Required Permission** | — |
| **6** | **Request Headers** | None required |
| **7–9** | None |
| **10** | — |
| **11** | `{ "status": "UP", "components": { "database": "UP" } }` |
| **12** | 503 when unhealthy |
| **13** | **200 OK** / **503 Service Unavailable** |
| **14–15** | — |

**16** `GET /api/v1/health` (no Authorization)  
**17** `{ "status": "UP" }`  
**18** `503` `{ "status": "DOWN" }`

### API-176: Import Sales Order (Integration)

| # | Field | Value |
|---|-------|-------|
| **1** | **HTTP Method** | `POST` |
| **2** | **URL** | `/api/v1/integrations/sales/orders` |
| **3** | **Purpose** | Import customer order from CRM (ACL inbound) |
| **4** | **Authentication** | **Client Credentials** — `INT_SALES` service principal |
| **5** | **Required Permission** | `PERM-054` |
| **6** | **Request Headers** | `Authorization: Bearer {client_token}`, `Content-Type`, **`Idempotency-Key`** (required), `X-Correlation-Id` |
| **7–8** | None |
| **9** | `externalOrderId`, `externalSystemCode`, `channel`, `lines[]`; optional `shipFromLocationCode`, `correlationId` |
| **10** | VR-007; idempotent on `externalOrderId`; SKU exists; qty > 0; channel ∈ {B2B,B2C,MARKETPLACE} |
| **11** | `CustomerOrderDetailResponse` |
| **12** | 400,401,403,409 duplicate external id,422 |
| **13** | **201 Created** |
| **14** | **BR-001** (downstream availability) |
| **15** | UC-021, UC-022 |

**16**
```json
POST /api/v1/integrations/sales/orders
Idempotency-Key: 7f3c9a2e-4b1d-4e8a-9c0f-2a8b6d4e1f30

{
  "externalOrderId": "CRM-99881",
  "externalSystemCode": "SALESFORCE",
  "channel": "B2B",
  "lines": [{ "externalLineId": "1", "sku": "BOLT-M10", "quantity": { "amount": 5, "unitOfMeasure": "EA" } }]
}
```
**17** `201` order with internal `orderId`  
**18** `401 AUTH_INTEGRATION_CREDENTIAL_INVALID`

### API-177: Get Fulfillment Status Feed
| 1 | `GET` | 2 | `/api/v1/integrations/sales/fulfillment-status` | 3 | Publish fulfillment status to CRM | 4 | Client Credentials (`INT_SALES`) | 5 | `PERM-062` | 6 | `Authorization` | 7 | — | 8 | `externalSystemCode` (required), `externalOrderId`, `updatedSince`, `status`, `cursor`, `limit` | 9 | — | 10 | VR external system registered; ISO `updatedSince` | 11 | `CursorPagedResponse<FulfillmentStatusFeedItem>` | 12 | 401,403 | 13 | **200** | 14 | — | 15 | UC-027 |
**16** GET `?externalSystemCode=SALESFORCE&updatedSince=2026-07-01T00:00:00Z`  
**17** cursor page of order fulfillment statuses  
**18** `403` unregistered external system

### API-178: Import Campaign Plan (Integration)
| 1 | `POST` | 2 | `/api/v1/integrations/marketing/campaign-plans` | 3 | Import campaign plan from marketing system | 4 | Client Credentials (`INT_MKT`) | 5 | `PERM-093` | 6 | `Authorization`, `Content-Type`, `Idempotency-Key` | 7 | — | 8 | — | 9 | `externalCampaignId`, `externalSystemCode`, `campaignName`, `campaignStartDate`, `campaignEndDate`, `allocationLines[]` | 10 | VR-126, VR-127; active SKU/location; end ≥ start | 11 | `PromotionalAllocationBatchResponse` | 12 | 400,401,403,422 | 13 | **201** | 14 | **BR-029** | 15 | UC-040 |
**16** POST campaign plan with allocation lines per location/SKU  
**17** `201` created allocation ids  
**18** `422` invalid SKU or location on allocation line

---

## Complete API Index (178 Endpoints)

| Range | Module | Document |
|-------|--------|----------|
| API-001 – 010 | M-01 Product Catalog | `Complete-API-Specification.md` |
| API-011 – 021 | M-02 Warehouse Network | `Complete-API-Specification.md` |
| API-022 – 097 | M-03 – M-07 | `Complete-API-Specification-Part2.md` |
| API-098 – 178 | M-08 – Platform | `Complete-API-Specification-Part3.md` (this document) |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Backend Architect | | | |
| Solution Architect | | | |
| Product Owner | | | |

*SRS-API-009 Part 3 | July 6, 2026 — Completes all 178 REST API specifications.*
