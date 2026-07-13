# API Authorization Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-007 |
| **Document Title** | API Authorization Specification — RBAC Mapping |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Backend Architect |
| **Source Documents** | SRS-API-001, `project_business/Permissions/rbac-matrix.md`, `project_business/Permissions/system-permissions.md`, SRS-API-005 |
| **Date** | July 6, 2026 |
| **Scope** | Authorization requirements for all 178 REST APIs |

### Purpose

Maps every REST API to the **RBAC model** (UR-01–UR-19, PERM-001–PERM-100). For each endpoint specifies authentication, authorized roles, required permissions, sensitive-operation classification, and business justification.

### Authorization Model

```
Request → Authenticate (JWT / Client Credentials)
        → Resolve user roles + location scope
        → Check PERM-xxx (any assigned role grants permission)
        → Enforce location scope on transactional APIs
        → Evaluate SoD on approval APIs (API-031, dual-control endpoints)
        → Execute or 401/403
```

| Mechanism | Detail |
|-----------|--------|
| **Authentication** | OAuth 2.0 Bearer JWT (SVC-01 IdP) for users; Client Credentials for integration principals |
| **Authorization** | Permission-based (`PERM-xxx`); roles are permission bundles |
| **Location scope** | Transactional APIs require `locationCode` ∈ user's assigned locations (except network-scoped roles) |
| **SoD** | Initiator ≠ approver enforced at domain layer; pre-checked via API-031 where applicable |
| **Deny default** | No permission → `403 AUTHZ_INSUFFICIENT_PERMISSION` |

### Role Code Reference

| Code | UR | Role |
|------|-----|------|
| `CEO` | UR-01 | Chief Executive Officer |
| `COO` | UR-02 | Chief Operating Officer |
| `CFO` | UR-03 | Chief Financial Officer |
| `OPS_DIR` | UR-04 | Operations Director |
| `INV_CTRL` | UR-05 | Inventory Controller |
| `WH_MGR` | UR-06 | Warehouse Manager |
| `RCV_CLK` | UR-07 | Receiving Clerk |
| `PIK_PAK` | UR-08 | Warehouse Picker / Packer |
| `WH_STF` | UR-09 | Warehouse Staff |
| `REG_MGR` | UR-10 | Regional / Store Manager |
| `SAL_MGR` | UR-11 | Sales Manager |
| `SAL_REP` | UR-12 | Sales Representative |
| `CS_REP` | UR-13 | Customer Service Representative |
| `MKT_MGR` | UR-14 | Marketing Manager |
| `PUR_MGR` | UR-15 | Purchasing Manager |
| `BUYER` | UR-16 | Buyer / Procurement Officer |
| `FIN_MGR` | UR-17 | Finance Manager / Accountant |
| `INT_AUD` | UR-18 | Internal Auditor |
| `EXT_AUD` | UR-19 | External Auditor |
| `SYS_ADMIN` | — | System Administrator (technical; PERM-095/096 only) |
| `INT_SALES` | — | Integration principal — Sales/CRM (EXT-01) |
| `INT_MKT` | — | Integration principal — Marketing (EXT-07) |

### Sensitive Operation Categories

| Code | Category | Examples |
|------|----------|----------|
| **—** | Not sensitive | Read-only visibility, lookups |
| **S1** | Approval | PO, transfer, adjustment, write-off approvals |
| **S2** | Control override | Ad-hoc receipt, tolerance override, safety stock override |
| **S3** | Governance / policy | Policies, thresholds, reason codes, location closure |
| **S4** | Financial | Valuation, reconciliation, invoice payment |
| **S5** | Audit / compliance | Audit trail, evidence export, breach records |
| **S6** | Master data mutation | Product, location, supplier create/update |
| **S7** | Identity / admin | User provisioning, role assignment |
| **S8** | Stock mutation | Reservation, shipment, transfer dispatch, adjustments |

**Location scope key:** `NET` = network-wide; `LOC` = assigned location(s); `NONE` = not location-bound; `SELF` = own session/profile only.

---

## M-01 — Product Catalog

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-001 | POST `/products` | Yes | PERM-001 | INV_CTRL | S6 | NET | Product master integrity centralized with Inventory Controller (BR catalog identity) |
| API-002 | GET `/products` | Yes | PERM-004 | COO, OPS_DIR, INV_CTRL, WH_MGR, RCV_CLK, PIK_PAK, WH_STF, REG_MGR, SAL_MGR, SAL_REP, CS_REP, MKT_MGR, PUR_MGR, BUYER, FIN_MGR | — | NET | Operational lookup without master-data mutation rights |
| API-003 | GET `/products/{sku}` | Yes | PERM-004 | Same as API-002 | — | NET | Single-product retrieval for transactions and inquiries |
| API-004 | PATCH `/products/{sku}` | Yes | PERM-002 | INV_CTRL | S6 | NET | Attribute changes affect all locations; restricted to control owner |
| API-005 | POST `.../lifecycle-status` | Yes | PERM-003 | INV_CTRL | S6 | NET | Discontinued status blocks replenishment (BR-027) |
| API-006 | PUT `.../abc-classification` | Yes | PERM-012 | INV_CTRL | S3 | NET | ABC drives monitoring priority (BR-032) |
| API-007 | GET `.../eligibility` | Yes | PERM-004 | Same as API-002 | — | LOC | Pre-check before procurement/reservation/fulfillment |
| API-008 | GET `.../categories/.../products` | Yes | PERM-004 | Same as API-002 | — | NET | Category browse for catalog navigation |
| API-009 | POST `/products/duplicate-resolutions` | Yes | PERM-005 | INV_CTRL | S6 | NET | Merge affects on-hand identity; requires control owner + merge auth when stock exists |
| API-010 | POST `/products/import` | Yes | PERM-015 | OPS_DIR, INV_CTRL | S6 | NET | Bulk cutover data; OpsDir submits, InvCtrl approves via separate flow (PERM-016) |

---

## M-02 — Warehouse Network

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-011 | POST `/locations` | Yes | PERM-006 | COO, OPS_DIR | S6 | NET | Location network structure is executive/ops leadership responsibility |
| API-012 | GET `/locations` | Yes | PERM-004 | All roles with visibility (PERM-017+) | — | NET/LOC | List locations within user scope |
| API-013 | GET `/locations/{code}` | Yes | PERM-004 | Same as API-012 | — | LOC | Location detail for operational context |
| API-014 | PATCH `.../hierarchy` | Yes | PERM-008 | COO, OPS_DIR | S6 | NET | Hierarchy changes affect reporting and accountability |
| API-015 | POST `.../storage-positions` | Yes | PERM-007 | COO, OPS_DIR | S6 | LOC | Storage layout owned by ops; WH_MGR uses positions operationally |
| API-016 | GET `.../storage-positions` | Yes | PERM-004 | WH_MGR, RCV_CLK, WH_STF, OPS_DIR, INV_CTRL + visibility roles | — | LOC | Put-away and pick face lookup |
| API-017 | POST `.../activate` | Yes | PERM-007 | COO, OPS_DIR | S3 | LOC | Go-live enables transactions; requires opening balance readiness |
| API-018 | POST `.../deactivate` | Yes | PERM-007 | COO, OPS_DIR | S3 | LOC | Stops new transactions at location |
| API-019 | POST `.../close` | Yes | PERM-009 | CEO, COO, OPS_DIR | S3 | LOC | Strategic closure with disposition planning |
| API-020 | GET `.../freeze-status` | Yes | PERM-040 | OPS_DIR, INV_CTRL, WH_MGR, CEO, CFO, FIN_MGR, INT_AUD, EXT_AUD, REG_MGR | — | LOC | Physical count freeze visibility (BR-024) |
| API-021 | GET `.../operational-status` | Yes | PERM-004 | Same as API-012 | — | LOC | Transaction eligibility check |

---

## M-03 — Inventory Governance

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-022 | POST `/governance/reason-codes` | Yes | PERM-014 | INV_CTRL | S3 | NET | Reason codes substantiate adjustments (BR-020) |
| API-023 | GET `/governance/reason-codes` | Yes | PERM-014 | INV_CTRL, OPS_DIR + transactional roles using codes | — | NET | Selectable codes for transactions |
| API-024 | POST `.../reason-codes/{code}/retire` | Yes | PERM-014 | INV_CTRL | S3 | NET | Retire obsolete codes while preserving history |
| API-025 | GET `.../reason-codes/{code}/validate` | Yes | PERM-014 | All roles posting adjustments/receipts | — | NET | Pre-validate code applicability (VR-026) |
| API-026 | POST `/governance/policies` | Yes | PERM-013 | OPS_DIR, COO | S3 | NET | Policy versions govern thresholds and tolerances network-wide |
| API-027 | PATCH `.../approval-thresholds` | Yes | PERM-013 | OPS_DIR, COO | S3 | NET | Approval thresholds enforce SoD and materiality (BR-021) |
| API-028 | PATCH `.../receipt-tolerances` | Yes | PERM-013 | OPS_DIR, COO | S3 | NET | Receipt tolerance affects payment and inventory acceptance |
| API-029 | GET `/governance/approval-thresholds` | Yes | PERM-013 | OPS_DIR, COO, INV_CTRL, WH_MGR, FIN_MGR | — | NET/LOC | Threshold lookup before submission |
| API-030 | GET `/governance/receipt-tolerances` | Yes | PERM-032 | WH_MGR, OPS_DIR, COO | — | LOC | Tolerance evaluation at receipt |
| API-031 | POST `/governance/segregation-of-duties/evaluate` | Yes | PERM-013 | OPS_DIR, COO, INV_CTRL, FIN_MGR, INT_AUD | S3 | NET | SoD pre-check (BR-019, BR-021); no mutation |

---

## M-04 — Inventory Balance

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-032 | POST `/inventory/opening-balances` | Yes | PERM-010 | OPS_DIR, INV_CTRL | S3 | LOC | Go-live balances embed baseline accuracy (BA-16) |
| API-033 | GET `/inventory/stock-positions` | Yes | PERM-017, PERM-021 | All visibility roles (PG-03) | — | LOC | On-hand inquiry scoped to authorized locations |
| API-034 | GET `.../stock-positions/{loc}/{sku}` | Yes | PERM-017 | PG-03 roles | — | LOC | Detail position for operational decisions |
| API-035 | GET `/inventory/availability/{sku}` | Yes | PERM-018 | PG-03 except WH_STF, PIK_PAK (no ATP for some) | — | LOC | ATP hot-path for sales/fulfillment (BR-001) |
| API-036 | GET `.../availability/{sku}/network` | Yes | PERM-022 | Network-scoped visibility roles | — | NET | Network ATP for transfer/buy decisions (BR-011) |
| API-037 | GET `.../stock-status/{loc}/{sku}` | Yes | PERM-020 | PG-03 roles | — | LOC | Derived status for replenishment alerts |
| API-038 | POST `/inventory/stock-policies` | Yes | PERM-011 | INV_CTRL, OPS_DIR | S3 | LOC | Thresholds drive replenishment (BR-009, BR-010) |
| API-039 | GET `.../stock-policies/{loc}/{sku}` | Yes | PERM-011 | INV_CTRL, OPS_DIR, WH_MGR, PUR_MGR | — | LOC | Policy lookup |
| API-040 | PATCH `.../stock-policies/{loc}/{sku}` | Yes | PERM-011 | INV_CTRL, OPS_DIR | S3 | LOC | Threshold changes affect network replenishment |
| API-041 | GET `.../lots` | Yes | PERM-017 | PG-03 with location scope | — | LOC | Lot traceability (BR-017) |
| API-042 | GET `.../transfer-capacity` | Yes | PERM-076 | COO, OPS_DIR, INV_CTRL, REG_MGR, PUR_MGR, FIN_MGR, INT_AUD, EXT_AUD | — | LOC | Source spare capacity before transfer (BR-012) |
| API-043 | POST `.../reservations` | Yes | PERM-052 | COO, OPS_DIR, WH_MGR | S8 | LOC | ATP commitment (BR-001, BR-002); may need PERM-070 if safety stock breach |
| API-044 | POST `.../reservations/.../release` | Yes | PERM-053 | COO, OPS_DIR, WH_MGR | S8 | LOC | Release on cancel/change (BR-002) |
| API-045 | POST `.../quarantine-holds` | Yes | PERM-047 | OPS_DIR, INV_CTRL, WH_MGR | S8 | LOC | Exclude from sellable ATP (BR-013) |
| API-046 | POST `.../quarantine-holds/.../release` | Yes | PERM-048 | OPS_DIR, INV_CTRL, WH_MGR | S2 | LOC | Restore requires inspection for resellable (BR-026) |
| API-047 | POST `.../consignment-ownership` | Yes | PERM-017 | FIN_MGR, CFO (operational trigger via finance) | S4 | LOC | Consignment consumption accounting (BR-031) |
| API-048 | POST `.../promotional-segregation` | Yes | PERM-093 | COO, OPS_DIR, MKT_MGR | S2 | LOC | Ring-fence ATP (BR-029); event-driven from campaign |

---

## M-05 — Procurement & Supplier

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-049 | POST `/suppliers` | Yes | PERM-024 | PUR_MGR | S6 | NET | Supplier master enables PO placement |
| API-050 | GET `/suppliers` | Yes | PERM-035 | PG-03 + PG-06 visibility roles | — | NET | Supplier selection for procurement |
| API-051 | GET `/suppliers/{code}` | Yes | PERM-035 | Same as API-050 | — | NET | Supplier terms lookup |
| API-052 | PATCH `/suppliers/{code}` | Yes | PERM-025 | PUR_MGR | S6 | NET | Terms affect payment and lead time |
| API-053 | POST `.../deactivate` | Yes | PERM-026 | PUR_MGR | S3 | NET | Block unauthorized new POs to inactive supplier |
| API-054 | POST `/procurement/requisitions` | Yes | PERM-067 | PUR_MGR, BUYER | — | LOC | Replenishment need documentation (BR-011) |
| API-055 | GET `/procurement/requisitions/{id}` | Yes | PERM-067, PERM-068 | PUR_MGR, BUYER, COO, OPS_DIR | — | NET | Requisition status tracking |
| API-056 | POST `.../approve` | Yes | PERM-068 | PUR_MGR | S1 | NET | Spend commitment approval; Buyer cannot approve (SoD) |
| API-057 | POST `.../reject` | Yes | PERM-068 | PUR_MGR | — | NET | Documented rejection (VR-131) |
| API-058 | POST `.../convert-to-po` | Yes | PERM-024 | PUR_MGR, BUYER | — | LOC | Convert approved need to commercial commitment |
| API-059 | POST `/procurement/purchase-orders` | Yes | PERM-024 | PUR_MGR, BUYER | S1 | LOC | PO creates binding supplier commitment (BR-007) |
| API-060 | GET `/procurement/purchase-orders` | Yes | PERM-027, PERM-035 | PG-06 visibility roles | — | LOC | Inbound pipeline visibility |
| API-061 | GET `/procurement/purchase-orders/{id}` | Yes | PERM-027 | PG-06 visibility roles | — | LOC | PO detail for receipt and finance |
| API-062 | PATCH `/procurement/purchase-orders/{id}` | Yes | PERM-025 | PUR_MGR, BUYER | S1 | LOC | Amendment affects commitment; authorized roles only (VR-051) |
| API-063 | POST `.../cancel` | Yes | PERM-026 | PUR_MGR, BUYER | S1 | LOC | Cancellation with receipt implications |
| API-064 | POST `.../expected-deliveries` | Yes | PERM-027 | PUR_MGR, BUYER, WH_MGR | — | LOC | Inbound planning (UC-007) |
| API-065 | GET `.../validate-for-receipt` | Yes | PERM-028 | WH_MGR, RCV_CLK | — | LOC | PO authorization check before receipt (BR-007) |

---

## M-06 — Inbound Receiving

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-066 | POST `/inbound/goods-receipts` | Yes | PERM-028 | WH_MGR, RCV_CLK | — | LOC | Initiate receipt against PO (BR-007) |
| API-067 | GET `/inbound/goods-receipts` | Yes | PERM-028 | WH_MGR, RCV_CLK, PUR_MGR, BUYER | — | LOC | Receipt status tracking |
| API-068 | GET `/inbound/goods-receipts/{id}` | Yes | PERM-028 | Same as API-067 | — | LOC | Receipt detail |
| API-069 | POST `.../verify` | Yes | PERM-028 | WH_MGR, RCV_CLK | S8 | LOC | Verify before acceptance (BR-004) |
| API-070 | POST `.../discrepancies` | Yes | PERM-029 | WH_MGR, RCV_CLK | — | LOC | Document discrepancies (BR-006) |
| API-071 | GET `.../discrepancies` | Yes | PERM-029 | WH_MGR, RCV_CLK, PUR_MGR, BUYER | — | LOC | Open discrepancy list |
| API-072 | POST `.../discrepancies/.../resolve` | Yes | PERM-030 | WH_MGR, PUR_MGR, BUYER | S1 | LOC | Resolution affects acceptance and supplier claim |
| API-073 | POST `.../put-away` | Yes | PERM-033 | WH_MGR, WH_STF | S8 | LOC | ATP increases only after put-away (BR-005) |
| API-074 | GET `/inbound/pending-put-away` | Yes | PERM-033 | WH_MGR, WH_STF, RCV_CLK | — | LOC | Put-away queue |
| API-075 | POST `/inbound/ad-hoc-receipts` | Yes | PERM-031 | WH_MGR | S2 | LOC | Non-PO receipt bypasses procurement controls |
| API-076 | POST `/inbound/return-receipts` | Yes | PERM-034 | WH_MGR, RCV_CLK | — | LOC | Return dock receipt (BR-025) |
| API-077 | POST `/inbound/supplier-invoices` | Yes | PERM-094 | FIN_MGR, CFO | S4 | NET | Invoice registration for three-way match |
| API-078 | GET `/inbound/supplier-invoices/{id}` | Yes | PERM-094 | FIN_MGR, CFO, INT_AUD | S4 | NET | Match status visibility |
| API-079 | POST `.../three-way-match` | Yes | PERM-094 | FIN_MGR, CFO | S4 | NET | PO–receipt–invoice match (BR-008) |
| API-080 | POST `.../authorize-payment` | Yes | PERM-094 | FIN_MGR, CFO | S1 | NET | Payment only after successful match (BR-008) |

---

## M-07 — Order Fulfillment

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-081 | POST `/fulfillment/orders` | Yes | PERM-054 | COO, OPS_DIR, WH_MGR, SAL_MGR | — | LOC | Create/import order for fulfillment pipeline |
| API-082 | GET `/fulfillment/orders` | Yes | PERM-062 | PG-08 status viewers | — | LOC | Order list for operations and customer service |
| API-083 | GET `/fulfillment/orders/{id}` | Yes | PERM-062 | PG-08 status viewers | — | LOC | Order detail |
| API-084 | POST `.../availability` | Yes | PERM-051 | COO, OPS_DIR, WH_MGR, SAL_MGR, SAL_REP, CS_REP, MKT_MGR | — | LOC | ATP check before promise (BR-001) |
| API-085 | POST `.../confirm` | Yes | PERM-054 | COO, OPS_DIR, WH_MGR | S8 | LOC | Confirms order and reserves stock (BR-002); PERM-070 if safety override |
| API-086 | POST `.../cancel` | Yes | PERM-054 | COO, OPS_DIR, WH_MGR | S8 | LOC | Cancel releases reservation |
| API-087 | POST `.../multi-location-plan` | Yes | PERM-061 | COO, OPS_DIR | S8 | NET | Multi-location allocation when single-site ATP insufficient |
| API-088 | POST `.../pick-lists` | Yes | PERM-055 | WH_MGR | — | LOC | Assign pick work |
| API-089 | GET `.../pick-lists/awaiting` | Yes | PERM-055 | WH_MGR, PIK_PAK | — | LOC | Pick queue |
| API-090 | POST `.../picks/{id}/verify` | Yes | PERM-055 | WH_MGR, PIK_PAK | S8 | LOC | Verified pick before ship (BR-003); PERM-063 if substitution |
| API-091 | POST `.../pack` | Yes | PERM-055 | WH_MGR, PIK_PAK | — | LOC | Pack verified pick |
| API-092 | POST `.../shipments` | Yes | PERM-056 | WH_MGR, PIK_PAK | S8 | LOC | Shipment deducts inventory (BR-003) |
| API-093 | POST `.../partial-fulfillment` | Yes | PERM-057 | COO, OPS_DIR, WH_MGR | S8 | LOC | Partial ship with optional backorder (BR-028) |
| API-094 | POST `.../backorders` | Yes | PERM-058 | COO, OPS_DIR, WH_MGR, SAL_MGR, CS_REP, PUR_MGR | S1 | LOC | Backorder requires customer acknowledgment (BR-028) |
| API-095 | POST `/fulfillment/backorders/{id}/fulfill` | Yes | PERM-058 | COO, OPS_DIR, WH_MGR | S8 | LOC | Fulfill when ATP available |
| API-096 | POST `.../exceptions` | Yes | PERM-059 | WH_MGR, PIK_PAK | — | LOC | Report pick/ship exceptions |
| API-097 | GET `.../status` | Yes | PERM-062 | PG-08 status viewers + auditors | — | LOC | Fulfillment status for CS and audit |

---

## M-08 — Network Transfer

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-098 | POST `/transfers` | Yes | PERM-071 | OPS_DIR, WH_MGR, REG_MGR | — | LOC | Transfer request; source capacity validated (BR-012) |
| API-099 | GET `/transfers` | Yes | PERM-075 | PG-05 visibility roles | — | LOC | Transfer history and status |
| API-100 | GET `/transfers/{id}` | Yes | PERM-075 | PG-05 visibility roles | — | LOC | Transfer detail |
| API-101 | POST `.../approve` | Yes | PERM-072 | OPS_DIR, COO | S1 | NET | Approver ≠ requester (SoD); protects source minimum |
| API-102 | POST `.../reject` | Yes | PERM-072 | OPS_DIR, COO | — | NET | Documented rejection |
| API-103 | POST `.../dispatch` | Yes | PERM-073 | WH_MGR | S8 | LOC | Dispatch creates in-transit stock |
| API-104 | POST `.../receive` | Yes | PERM-074 | WH_MGR | S8 | LOC | Destination receipt completes transfer |
| API-105 | POST `.../cancel` | Yes | PERM-073 | OPS_DIR, WH_MGR | S8 | NET | Cancel in-transit with reversal |
| API-106 | GET `/transfers/pending-approvals` | Yes | PERM-072 | OPS_DIR, COO | — | NET | Approval queue (UC-047) |
| API-107 | GET `/transfers/in-transit` | Yes | PERM-075 | PG-05 visibility roles | — | LOC | Pipeline visibility (UC-030) |

---

## M-09 — Inventory Accuracy

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-108 | POST `/accuracy/cycle-counts` | Yes | PERM-037 | OPS_DIR, INV_CTRL | S3 | LOC | Schedule count program (BR-018) |
| API-109 | GET `/accuracy/cycle-counts` | Yes | PERM-037 | OPS_DIR, INV_CTRL, WH_MGR | — | LOC | Count assignment list |
| API-110 | GET `/accuracy/cycle-counts/{id}` | Yes | PERM-038 | WH_STF, REG_MGR, OPS_DIR, INV_CTRL | — | LOC | Blind count — no system qty exposed (BR-018) |
| API-111 | POST `.../result` | Yes | PERM-038 | WH_STF, REG_MGR | S8 | LOC | Submit blind count; counter cannot approve (SoD) |
| API-112 | POST `/accuracy/physical-counts` | Yes | PERM-039 | OPS_DIR | S3 | LOC | Wall-to-wall count imposes freeze (BR-024) |
| API-113 | GET `/accuracy/physical-counts/{id}` | Yes | PERM-039 | OPS_DIR, INV_CTRL, WH_MGR | — | LOC | Count progress during freeze |
| API-114 | POST `.../results` | Yes | PERM-039 | OPS_DIR, WH_STF (during freeze) | S8 | LOC | Line results during freeze window |
| API-115 | POST `.../certify` | Yes | PERM-039 | OPS_DIR | S1 | LOC | Certify complete; release freeze |
| API-116 | POST `/accuracy/adjustment-cases` | Yes | PERM-043 | OPS_DIR, INV_CTRL, WH_MGR | — | LOC | Open adjustment case (BR-022) |
| API-117 | GET `/accuracy/adjustment-cases/{id}` | Yes | PERM-040 | OPS_DIR, INV_CTRL, WH_MGR, CEO, CFO, FIN_MGR, INT_AUD, EXT_AUD, REG_MGR | — | LOC | Case investigation state |
| API-118 | POST `.../investigate` | Yes | PERM-041 | OPS_DIR, INV_CTRL | S3 | LOC | Investigation before adjustment (BR-022) |
| API-119 | POST `.../variances/.../approve` | Yes | PERM-042 | OPS_DIR, INV_CTRL, WH_MGR | S1 | LOC | Count variance approval; counter ≠ approver (BR-019) |
| API-120 | POST `.../submit` | Yes | PERM-043, PERM-045 | OPS_DIR, INV_CTRL, WH_MGR | S8 | LOC | Submit adjustment/write-off for approval |
| API-121 | POST `.../approve` | Yes | PERM-044, PERM-046 | OPS_DIR, COO, CFO | S1 | LOC | Independent material adjustment/write-off approval (BR-021) |
| API-122 | POST `.../reject` | Yes | PERM-044 | OPS_DIR, COO, CFO | — | LOC | Reject proposed adjustment |
| API-123 | GET `/accuracy/pending-approvals` | Yes | PERM-044, PERM-046 | OPS_DIR, COO, CFO, INV_CTRL | — | LOC | Approval queue (UC-047) |

---

## M-10 — Returns Management

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-124 | POST `/returns/authorizations` | Yes | PERM-077 | CS_REP | S1 | NONE | RMA required before return (BR-025) |
| API-125 | GET `/returns/authorizations` | Yes | PERM-082 | CS_REP, WH_MGR, INV_CTRL, FIN_MGR, INT_AUD | — | NONE | RMA status list |
| API-126 | GET `/returns/authorizations/{id}` | Yes | PERM-082 | Same as API-125 | — | NONE | RMA detail |
| API-127 | POST `.../cancel` | Yes | PERM-077 | CS_REP | — | NONE | Cancel unused authorization |
| API-128 | POST `/returns/{id}/receive` | Yes | PERM-078 | WH_MGR, RCV_CLK | — | LOC | Physical return receipt |
| API-129 | POST `/returns/{id}/inspect` | Yes | PERM-079 | WH_MGR | S8 | LOC | Inspect before restock (BR-026) |
| API-130 | POST `/returns/{id}/disposition` | Yes | PERM-080, PERM-081 | WH_MGR, INV_CTRL | S1 | LOC | Restock or write-off; write-off needs approval refs (BR-023) |
| API-131 | GET `/returns/pending-receipts` | Yes | PERM-078 | WH_MGR, RCV_CLK | — | LOC | Returns awaiting dock receipt |

---

## M-11 — Commercial Campaign

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-132 | POST `/campaigns/allocations` | Yes | PERM-093 | COO, OPS_DIR, MKT_MGR | S2 | LOC | Ring-fence removes ATP from general pool (BR-029) |
| API-133 | GET `/campaigns/allocations` | Yes | PERM-092 | COO, OPS_DIR, SAL_MGR, MKT_MGR, PUR_MGR | — | LOC | Allocation visibility |
| API-134 | GET `/campaigns/allocations/{id}` | Yes | PERM-092 | Same as API-133 | — | LOC | Allocation detail |
| API-135 | PATCH `/campaigns/allocations/{id}` | Yes | PERM-093 | COO, OPS_DIR, MKT_MGR | S2 | LOC | Amend ring-fence quantity/period |
| API-136 | POST `.../readiness` | Yes | PERM-092 | COO, OPS_DIR, SAL_MGR, MKT_MGR, PUR_MGR | — | LOC | Campaign readiness evaluation (UC-040) |
| API-137 | POST `.../release` | Yes | PERM-093 | COO, OPS_DIR, MKT_MGR | S2 | LOC | Release unconsumed ring-fence |
| API-138 | POST `.../override` | Yes | PERM-093 | COO, OPS_DIR, MKT_MGR | S2 | LOC | Override ring-fence for non-promotional order |
| API-139 | GET `/campaigns/ring-fence/{loc}/{sku}` | Yes | PERM-092, PERM-051 | SAL_MGR, SAL_REP, WH_MGR, MKT_MGR | — | LOC | Check active ring-fence before availability |

---

## M-12 — Identity & Access

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-140 | POST `/users` | Yes | PERM-095 | SYS_ADMIN | S7 | NET | Account lifecycle outside business roles (RBAC §1) |
| API-141 | GET `/users` | Yes | PERM-095 | SYS_ADMIN | S7 | NET | User directory for administration |
| API-142 | GET `/users/{userId}` | Yes | PERM-095, PERM-062 | SYS_ADMIN; users may read SELF profile | S7 | SELF | Profile and role visibility |
| API-143 | POST `/users/{userId}/roles` | Yes | PERM-096 | SYS_ADMIN | S7 | NET | Role assignment determines all access boundaries |
| API-144 | DELETE `/users/.../roles/{id}` | Yes | PERM-096 | SYS_ADMIN | S7 | NET | Revoke access; prevents privilege retention |
| API-145 | POST `/users/{userId}/suspend` | Yes | PERM-095 | SYS_ADMIN | S7 | NET | Temporary access suspension |
| API-146 | POST `/users/{userId}/deactivate` | Yes | PERM-095 | SYS_ADMIN | S7 | NET | Permanent deactivation |
| API-147 | POST `/users/sync` | Yes | PERM-095 | SYS_ADMIN | S7 | NET | HR directory sync |
| API-148 | POST `/authorization/actions/evaluate` | Yes | PERM-062 | Any authenticated user (evaluate self) | — | LOC | Client-side permission pre-check (UC-045) |
| API-149 | POST `/authorization/location-scope/validate` | Yes | PERM-062 | Any authenticated user | — | LOC | Location scope validation before command |

---

## M-13 — Inventory Intelligence

Read-only projections. Write API-159 is command on alert acknowledgment.

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-150 | GET `/intelligence/dashboard` | Yes | PERM-083 | PG-11 dashboard roles | — | NET/LOC | Executive/ops dashboard (UC-037) |
| API-151 | GET `.../stock-status/summary` | Yes | PERM-083 | PG-11 roles | — | NET/LOC | Aggregated stock health |
| API-152 | GET `.../stock-status/board` | Yes | PERM-085 | PG-11 roles | — | NET/LOC | Stock status board |
| API-153 | GET `.../availability/inquiries` | Yes | PERM-018 | PG-03 sales/accountability roles | — | LOC | Sales inquiry accountability log |
| API-154 | GET `.../quarantine-register` | Yes | PERM-047 | OPS_DIR, INV_CTRL, WH_MGR + report roles | — | NET | Quarantine visibility (BR-013) |
| API-155 | GET `.../movements` | Yes | PERM-023, PERM-084 | PG-03 + PG-11 movement report roles | — | LOC | Movement history (UC-042) |
| API-156 | GET `.../audit-trail` | Yes | PERM-098 | FIN_MGR, INT_AUD, EXT_AUD | S5 | NET | Immutable change log — audit only |
| API-157 | GET `.../audit-trail/export` | Yes | PERM-099 | FIN_MGR, INT_AUD, EXT_AUD | S5 | NET | Formal audit evidence package |
| API-158 | GET `/intelligence/alerts` | Yes | PERM-064 | PG-11 + replenishment alert roles | — | LOC | Operational alerts (UC-047) |
| API-159 | POST `.../alerts/{id}/acknowledge` | Yes | PERM-065 | COO, OPS_DIR, PUR_MGR, SAL_MGR, MKT_MGR | — | LOC | Alert acknowledgment without stock mutation |
| API-160 | GET `.../replenishment/recommendations` | Yes | PERM-066 | COO, OPS_DIR, INV_CTRL, SAL_MGR, MKT_MGR, PUR_MGR, BUYER | — | NET | Replenishment recommendations |
| API-161 | GET `.../procurement/open-pos` | Yes | PERM-035 | PG-06 visibility roles | — | LOC | Open PO board |
| API-162 | GET `.../procurement/inbound-calendar` | Yes | PERM-027 | PG-06 visibility roles | — | LOC | Inbound supply calendar |
| API-163 | GET `.../procurement/inbound-delays` | Yes | PERM-036 | PG-06 + alert roles | — | LOC | Supplier delay log |
| API-164 | GET `.../fulfillment/backorders` | Yes | PERM-058 | PG-08 backorder viewers | — | LOC | Backorder pipeline (BR-028) |
| API-165 | GET `.../fulfillment/exceptions` | Yes | PERM-059 | WH_MGR, COO, OPS_DIR + status viewers | — | LOC | Exception log |
| API-166 | GET `.../network/imbalance` | Yes | PERM-076 | COO, OPS_DIR, INV_CTRL, REG_MGR, PUR_MGR, FIN_MGR, INT_AUD | — | NET | Rebalancing analysis (UC-034) |
| API-167 | GET `.../accuracy/shrinkage` | Yes | PERM-049 | CEO, COO, CFO, OPS_DIR, INV_CTRL, WH_MGR, FIN_MGR, INT_AUD, EXT_AUD | S4 | NET | Shrinkage analysis — financial sensitivity |
| API-168 | GET `.../accuracy/count-performance` | Yes | PERM-086 | PG-11 accuracy report roles | — | NET | Count accuracy metrics |
| API-169 | GET `.../campaigns/readiness` | Yes | PERM-092 | COO, OPS_DIR, SAL_MGR, MKT_MGR, PUR_MGR | — | NET | Campaign readiness status |
| API-170 | GET `/intelligence/kpis` | Yes | PERM-088 | CEO, COO, CFO, OPS_DIR, INV_CTRL, SAL_MGR, FIN_MGR, INT_AUD | — | NET | Executive KPIs (UC-038) |
| API-171 | GET `.../valuation/snapshots` | Yes | PERM-090 | CEO, COO, CFO, FIN_MGR, INT_AUD, EXT_AUD | S4 | NET | Unit cost exposure — finance/audit only |
| API-172 | GET `.../valuation/reconciliation` | Yes | PERM-094 | CFO, FIN_MGR | S4 | NET | GL reconciliation — finance independence |

---

## Platform & Integration

| API | Method | Auth | Permission(s) | Authorized Roles | Sensitive | Loc | Business Justification |
|-----|--------|------|---------------|------------------|-----------|-----|------------------------|
| API-173 | GET `/auth/session` | Yes | — (authenticated) | All authenticated users | — | SELF | Session validation and context (UC-045) |
| API-174 | POST `/auth/logout` | Yes | — (authenticated) | All authenticated users | — | SELF | Terminate session |
| API-175 | GET `/health` | **No** | — | Public (monitoring) | — | NONE | Operations health probe — no business data |
| API-176 | POST `/integrations/sales/orders` | Client Credentials | PERM-054 | INT_SALES service principal | S8 | LOC | CRM order import; machine identity with order release permission |
| API-177 | GET `/integrations/sales/fulfillment-status` | Client Credentials | PERM-062 | INT_SALES service principal | — | NET | CRM status feed — read fulfillment state |
| API-178 | POST `/integrations/marketing/campaign-plans` | Client Credentials | PERM-093 | INT_MKT service principal | S2 | LOC | Marketing campaign import triggers ring-fence planning |

---

## Sensitive Operations Summary

| Category | Count | API Examples | SoD / Control Notes |
|----------|-------|--------------|---------------------|
| **S1 Approval** | 18 | API-056, API-101, API-119, API-121, API-080 | Initiator ≠ approver enforced |
| **S2 Control override** | 8 | API-075, API-046, API-048, API-132, API-138 | WH_MGR / leadership only |
| **S3 Governance** | 14 | API-026–028, API-038, API-112, API-053 | Policy drift prevention |
| **S4 Financial** | 7 | API-077–080, API-171, API-172, API-047 | Finance independence from ops |
| **S5 Audit** | 2 | API-156, API-157 | Auditors read-only on operations |
| **S6 Master data** | 12 | API-001–005, API-011, API-049 | Centralized ownership |
| **S7 Identity** | 8 | API-140–147 | SYS_ADMIN only |
| **S8 Stock mutation** | 22 | API-043, API-092, API-103, API-111 | Location-scoped transactional |

---

## API-to-Permission Quick Index

| Permission | API IDs |
|------------|---------|
| PERM-001 | API-001 |
| PERM-002 | API-004 |
| PERM-003 | API-005 |
| PERM-004 | API-002, API-003, API-007, API-008, API-012–016, API-021 |
| PERM-005 | API-009 |
| PERM-006–009 | API-011, API-014–019 |
| PERM-010 | API-032, API-017 |
| PERM-011 | API-038–040 |
| PERM-012 | API-006 |
| PERM-013 | API-026–031 |
| PERM-014 | API-022–025 |
| PERM-015–016 | API-010 |
| PERM-017–023 | API-033–037, API-041, API-152–155 |
| PERM-024–027 | API-049, API-058–065, API-161–162 |
| PERM-028–034 | API-066–076 |
| PERM-035–036 | API-050–051, API-060–061, API-163 |
| PERM-037–042 | API-108–111, API-119 |
| PERM-043–046 | API-116, API-118, API-120–123 |
| PERM-047–048 | API-045–046, API-154 |
| PERM-049–050 | API-167 |
| PERM-051–063 | API-084–096, API-139 |
| PERM-064–066 | API-158–160 |
| PERM-067–069 | API-054–057 |
| PERM-070 | API-043, API-085 (conditional) |
| PERM-071–076 | API-098–107, API-042, API-166 |
| PERM-077–082 | API-124–131 |
| PERM-083–091 | API-150–152, API-157–158, API-168–170 |
| PERM-092–093 | API-132–139, API-178 |
| PERM-094 | API-077–080, API-172 |
| PERM-095–096 | API-140–147 |
| PERM-097–100 | API-156–157 (098–099); activity/breach via future APIs |
| Integration | API-176–178 |

---

## Enforcement Implementation Notes

1. **Spring Security:** `@PreAuthorize("hasAuthority('PERM-052')")` on controller methods; custom `LocationScopeAuthorizationManager` for `LOC` APIs.
2. **Integration clients:** Map `INT_SALES` / `INT_MKT` to OAuth client IDs with scoped permissions only — no human role assignment.
3. **Self-service:** API-142, API-148, API-149 allow `userId = principal` without PERM-095 for own profile.
4. **Dual control APIs:** API-119, API-121, API-056, API-101, API-080 — domain validates initiator ≠ approver after API-031 optional pre-check.
5. **Audit logging:** All **S1–S8** operations emit audit events with `userId`, `roles`, `permission`, `locationCode`, `traceId`.

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Backend Architect | | | |
| Security Engineer | | | |
| Solution Architect | | | |

---

*End of API Authorization Specification*

*Document ID: SRS-API-007 | Version 1.0 | July 6, 2026*
