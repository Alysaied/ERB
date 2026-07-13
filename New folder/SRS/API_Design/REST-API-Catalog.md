# REST API Catalog
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-001 |
| **Document Title** | REST API Catalog — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Backend Architect |
| **Source Documents** | BRD-IMS-001 (v1.0), SRS-UC-001 (Use Case Catalog), SRS-DM-003 (Domain Aggregates), SRS-ES-002 (Domain Commands), SRS-ES-005 (Read Models), SRS-SA-003 (System Modules Design), SRS-SA-005 (Integration Architecture Design), SRS-DB (Database Design) |
| **Date** | July 6, 2026 |
| **Scope** | REST API identification only — endpoints, methods, purpose, and traceability. Request/response structures are out of scope. |

### Purpose

This catalog identifies **all REST APIs** required to support the Inventory Management System. Each API is traced to a business module, use case, and domain aggregate derived from approved business and architecture artifacts. APIs align with the 13 logical system modules (M-01–M-13) and expose the published commands and queries defined in the System Modules Design.

### API Conventions

| Convention | Rule |
|------------|------|
| **Base path** | `/api/v1` |
| **Resource naming** | Plural nouns, kebab-case path segments |
| **Identifiers** | `ProductSku`, `LocationCode`, and other published-language identifiers in path or query |
| **Command actions** | `POST` to sub-resource action paths (e.g., `/orders/{id}/confirm`) |
| **Queries** | `GET` with filter query parameters |
| **Idempotency** | Safe retries on `PUT` and idempotent `POST` where saga compensation applies |
| **Authorization** | All endpoints require authenticated session (SVC-01 IdP); location-scoped RBAC enforced per UC-045 |

### Traceability Legend

| Reference | Meaning |
|-----------|---------|
| UC-xxx | Use Case (SRS-UC-001) |
| M-xx | Business Module (SRS-SA-003) |
| CMD-xxx | Domain Command (SRS-ES-002) — write API origin |
| RM-xxx | Read Model (SRS-ES-005) — query API origin |

### API Catalog Summary

| Business Module | API ID Range | Count |
|-----------------|--------------|-------|
| M-01 Product Catalog | API-001 – API-010 | 10 |
| M-02 Warehouse Network | API-011 – API-021 | 11 |
| M-03 Inventory Governance | API-022 – API-031 | 10 |
| M-04 Inventory Balance | API-032 – API-048 | 17 |
| M-05 Procurement & Supplier | API-049 – API-065 | 17 |
| M-06 Inbound Receiving | API-066 – API-080 | 15 |
| M-07 Order Fulfillment | API-081 – API-097 | 17 |
| M-08 Network Transfer | API-098 – API-107 | 10 |
| M-09 Inventory Accuracy | API-108 – API-123 | 16 |
| M-10 Returns Management | API-124 – API-131 | 8 |
| M-11 Commercial Campaign | API-132 – API-139 | 8 |
| M-12 Identity & Access | API-140 – API-149 | 10 |
| M-13 Inventory Intelligence | API-150 – API-172 | 23 |
| Platform & Integration | API-173 – API-178 | 6 |
| **Total** | | **178** |

---

## M-01 — Product Catalog

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-001 | Product Catalog | `/api/v1/products` | POST | Register a new product SKU with mandatory catalog attributes | UC-001, UC-046 | Product Catalog |
| API-002 | Product Catalog | `/api/v1/products` | GET | Search and filter products by name, category, status, and ABC class | UC-001, UC-013 | Product Catalog |
| API-003 | Product Catalog | `/api/v1/products/{sku}` | GET | Retrieve product master record by SKU | UC-001, UC-013 | Product Catalog |
| API-004 | Product Catalog | `/api/v1/products/{sku}` | PATCH | Update product attributes (name, category, UoM, traceability settings) | UC-001 | Product Catalog |
| API-005 | Product Catalog | `/api/v1/products/{sku}/lifecycle-status` | POST | Change product lifecycle status (active, inactive, discontinued) | UC-001 | Product Catalog |
| API-006 | Product Catalog | `/api/v1/products/{sku}/abc-classification` | PUT | Assign or update ABC operational priority classification | UC-004 | Product Catalog |
| API-007 | Product Catalog | `/api/v1/products/{sku}/eligibility` | GET | Validate whether product is eligible for procurement, reservation, or fulfillment | UC-006, UC-021, UC-022 | Product Catalog |
| API-008 | Product Catalog | `/api/v1/products/categories/{categoryCode}/products` | GET | List products belonging to a category for catalog browse | UC-001 | Product Catalog |
| API-009 | Product Catalog | `/api/v1/products/duplicate-resolutions` | POST | Resolve duplicate product identity conflict (merge or reject) | UC-001 | Product Catalog |
| API-010 | Product Catalog | `/api/v1/products/import` | POST | Bulk import product master data at location or system go-live | UC-046 | Product Catalog |

---

## M-02 — Warehouse Network

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-011 | Warehouse Network | `/api/v1/locations` | POST | Register a new inventory location (warehouse, store, distribution point) | UC-002 | Inventory Location |
| API-012 | Warehouse Network | `/api/v1/locations` | GET | List active locations in the inventory network | UC-002, UC-012, UC-013 | Inventory Location |
| API-013 | Warehouse Network | `/api/v1/locations/{locationCode}` | GET | Retrieve location master, hierarchy, and operational status | UC-002 | Inventory Location |
| API-014 | Warehouse Network | `/api/v1/locations/{locationCode}/hierarchy` | PATCH | Update location hierarchy (parent assignment, zones, layout) | UC-002 | Inventory Location |
| API-015 | Warehouse Network | `/api/v1/locations/{locationCode}/storage-positions` | POST | Configure or update a storage position (zone, aisle, bin) within a location | UC-002, UC-010 | Inventory Location |
| API-016 | Warehouse Network | `/api/v1/locations/{locationCode}/storage-positions` | GET | List storage positions available for put-away and pick assignment | UC-010 | Inventory Location |
| API-017 | Warehouse Network | `/api/v1/locations/{locationCode}/activate` | POST | Activate location for inventory operations after go-live readiness | UC-002, UC-046 | Inventory Location |
| API-018 | Warehouse Network | `/api/v1/locations/{locationCode}/deactivate` | POST | Deactivate location and begin closure workflow | UC-002 | Inventory Location |
| API-019 | Warehouse Network | `/api/v1/locations/{locationCode}/close` | POST | Finalize location closure after stock disposition confirmation | UC-002 | Inventory Location |
| API-020 | Warehouse Network | `/api/v1/locations/{locationCode}/freeze-status` | GET | Check whether location is under physical inventory freeze | UC-015 | Inventory Location |
| API-021 | Warehouse Network | `/api/v1/locations/{locationCode}/operational-status` | GET | Check whether location accepts transactional inventory activity | UC-002 | Inventory Location |

---

## M-03 — Inventory Governance

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-022 | Inventory Governance | `/api/v1/governance/reason-codes` | POST | Create a standardized reason code for adjustments and exceptions | UC-005 | Inventory Governance |
| API-023 | Inventory Governance | `/api/v1/governance/reason-codes` | GET | List active reason codes selectable for transactions | UC-005, UC-017, UC-009 | Inventory Governance |
| API-024 | Inventory Governance | `/api/v1/governance/reason-codes/{code}/retire` | POST | Retire a reason code from active use while preserving history | UC-005 | Inventory Governance |
| API-025 | Inventory Governance | `/api/v1/governance/reason-codes/{code}/validate` | GET | Validate reason code is active and applicable to a transaction type | UC-017, UC-009 | Inventory Governance |
| API-026 | Inventory Governance | `/api/v1/governance/policies` | POST | Publish a new governance policy version with effective date | UC-005 | Inventory Governance |
| API-027 | Inventory Governance | `/api/v1/governance/policies/{policyId}/approval-thresholds` | PATCH | Update financial or quantity approval thresholds | UC-005 | Inventory Governance |
| API-028 | Inventory Governance | `/api/v1/governance/policies/{policyId}/receipt-tolerances` | PATCH | Update receipt quantity tolerance limits for auto-accept vs. discrepancy | UC-005, UC-009 | Inventory Governance |
| API-029 | Inventory Governance | `/api/v1/governance/approval-thresholds` | GET | Retrieve effective approval threshold for a transaction context | UC-017, UC-018 | Inventory Governance |
| API-030 | Inventory Governance | `/api/v1/governance/receipt-tolerances` | GET | Retrieve effective receipt tolerance for discrepancy evaluation | UC-008, UC-009 | Inventory Governance |
| API-031 | Inventory Governance | `/api/v1/governance/segregation-of-duties/evaluate` | POST | Evaluate segregation-of-duties compliance between initiator and approver | UC-045 | Inventory Governance |

---

## M-04 — Inventory Balance

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-032 | Inventory Balance | `/api/v1/inventory/opening-balances` | POST | Establish verified opening on-hand balances at location go-live | UC-046 | Stock Position |
| API-033 | Inventory Balance | `/api/v1/inventory/stock-positions` | GET | Retrieve on-hand, reserved, and ATP for product at location | UC-012, UC-013 | Stock Position |
| API-034 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}` | GET | Retrieve stock position detail for a specific product-location pair | UC-012, UC-013 | Stock Position |
| API-035 | Inventory Balance | `/api/v1/inventory/availability/{sku}` | GET | Retrieve ATP for a SKU at a location (hot-path availability inquiry) | UC-013, UC-021 | Stock Position |
| API-036 | Inventory Balance | `/api/v1/inventory/availability/{sku}/network` | GET | Retrieve network-wide ATP rollup across all locations | UC-013, UC-021, UC-034 | Stock Position |
| API-037 | Inventory Balance | `/api/v1/inventory/stock-status/{locationCode}/{sku}` | GET | Retrieve derived stock status indicator (in stock, low, out, overstock) | UC-012, UC-028 | Stock Position |
| API-038 | Inventory Balance | `/api/v1/inventory/stock-policies` | POST | Define replenishment thresholds for a product at a location | UC-003 | Stock Policy |
| API-039 | Inventory Balance | `/api/v1/inventory/stock-policies/{locationCode}/{sku}` | GET | Retrieve stock policy thresholds for a product-location pair | UC-003, UC-028 | Stock Policy |
| API-040 | Inventory Balance | `/api/v1/inventory/stock-policies/{locationCode}/{sku}` | PATCH | Update stock policy thresholds with effective dating | UC-003 | Stock Policy |
| API-041 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/lots` | GET | Retrieve lot/batch-level quantity breakdown for traceable products | UC-024, UC-033 | Stock Position |
| API-042 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity` | GET | Evaluate spare quantity above source minimum available for transfer | UC-031, UC-032 | Stock Position, Stock Policy |
| API-043 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations` | POST | Reserve stock and reduce ATP for a confirmed order line | UC-022 | Stock Position |
| API-044 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations/{reservationId}/release` | POST | Release reserved stock and restore ATP on order cancellation | UC-023 | Stock Position |
| API-045 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds` | POST | Apply quarantine hold and exclude quantity from sellable ATP | UC-019 | Stock Position |
| API-046 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds/{holdId}/release` | POST | Release quarantine hold and restore quantity to sellable ATP | UC-019 | Stock Position |
| API-047 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/consignment-ownership` | POST | Transfer consignment ownership to organization-owned upon consumption | UC-039 | Stock Position |
| API-048 | Inventory Balance | `/api/v1/inventory/stock-positions/{locationCode}/{sku}/promotional-segregation` | POST | Segregate ATP for promotional ring-fence (event-driven from campaign) | UC-040 | Stock Position |

---

## M-05 — Procurement & Supplier

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-049 | Procurement & Supplier | `/api/v1/suppliers` | POST | Register a new supplier master record | UC-006 | Supplier |
| API-050 | Procurement & Supplier | `/api/v1/suppliers` | GET | List suppliers with optional status filter | UC-006, UC-029 | Supplier |
| API-051 | Procurement & Supplier | `/api/v1/suppliers/{supplierCode}` | GET | Retrieve supplier master, terms, and consignment indicator | UC-006 | Supplier |
| API-052 | Procurement & Supplier | `/api/v1/suppliers/{supplierCode}` | PATCH | Update supplier payment terms, lead time, and consignment flag | UC-006 | Supplier |
| API-053 | Procurement & Supplier | `/api/v1/suppliers/{supplierCode}/deactivate` | POST | Deactivate supplier and block new purchase order creation | UC-006 | Supplier |
| API-054 | Procurement & Supplier | `/api/v1/procurement/requisitions` | POST | Create internal purchase requisition for replenishment need | UC-029 | Purchase Requisition |
| API-055 | Procurement & Supplier | `/api/v1/procurement/requisitions/{requisitionId}` | GET | Retrieve purchase requisition status and line detail | UC-029 | Purchase Requisition |
| API-056 | Procurement & Supplier | `/api/v1/procurement/requisitions/{requisitionId}/approve` | POST | Approve purchase requisition after network availability validation | UC-029 | Purchase Requisition |
| API-057 | Procurement & Supplier | `/api/v1/procurement/requisitions/{requisitionId}/reject` | POST | Reject purchase requisition with documented reason | UC-029 | Purchase Requisition |
| API-058 | Procurement & Supplier | `/api/v1/procurement/requisitions/{requisitionId}/convert-to-po` | POST | Convert approved requisition into a purchase order | UC-029, UC-006 | Purchase Requisition, Purchase Order |
| API-059 | Procurement & Supplier | `/api/v1/procurement/purchase-orders` | POST | Place purchase order as authorized commercial commitment to supplier | UC-006 | Purchase Order |
| API-060 | Procurement & Supplier | `/api/v1/procurement/purchase-orders` | GET | List open purchase orders for inbound pipeline visibility | UC-006, UC-030 | Purchase Order |
| API-061 | Procurement & Supplier | `/api/v1/procurement/purchase-orders/{purchaseOrderId}` | GET | Retrieve purchase order header, lines, and received quantities | UC-006, UC-008, UC-030 | Purchase Order |
| API-062 | Procurement & Supplier | `/api/v1/procurement/purchase-orders/{purchaseOrderId}` | PATCH | Amend purchase order lines or delivery schedule | UC-006 | Purchase Order |
| API-063 | Procurement & Supplier | `/api/v1/procurement/purchase-orders/{purchaseOrderId}/cancel` | POST | Cancel purchase order with receipt implications | UC-006 | Purchase Order |
| API-064 | Procurement & Supplier | `/api/v1/procurement/purchase-orders/{purchaseOrderId}/expected-deliveries` | POST | Schedule or update expected inbound delivery dates | UC-007, UC-030 | Purchase Order |
| API-065 | Procurement & Supplier | `/api/v1/procurement/purchase-orders/{purchaseOrderId}/validate-for-receipt` | GET | Validate purchase order authorizes goods receipt (BR-007) | UC-008 | Purchase Order |

---

## M-06 — Inbound Receiving

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-066 | Inbound Receiving | `/api/v1/inbound/goods-receipts` | POST | Initiate goods receipt against purchase order or ad-hoc authorization | UC-008, UC-011 | Goods Receipt |
| API-067 | Inbound Receiving | `/api/v1/inbound/goods-receipts` | GET | List goods receipts with status and location filters | UC-008, UC-010 | Goods Receipt |
| API-068 | Inbound Receiving | `/api/v1/inbound/goods-receipts/{goodsReceiptId}` | GET | Retrieve goods receipt status, lines, and put-away state | UC-008, UC-010 | Goods Receipt |
| API-069 | Inbound Receiving | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/verify` | POST | Verify inbound quantity, product identity, and condition at dock | UC-008, UC-011 | Goods Receipt |
| API-070 | Inbound Receiving | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies` | POST | Document receipt discrepancy with classification and evidence | UC-009 | Goods Receipt |
| API-071 | Inbound Receiving | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies` | GET | List open discrepancies for a goods receipt | UC-009 | Goods Receipt |
| API-072 | Inbound Receiving | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies/{discrepancyId}/resolve` | POST | Resolve receipt discrepancy with documented outcome | UC-009 | Goods Receipt |
| API-073 | Inbound Receiving | `/api/v1/inbound/goods-receipts/{goodsReceiptId}/put-away` | POST | Confirm put-away to storage position, completing inbound workflow | UC-010 | Goods Receipt |
| API-074 | Inbound Receiving | `/api/v1/inbound/pending-put-away` | GET | List receipts awaiting storage placement at a location | UC-010 | Goods Receipt |
| API-075 | Inbound Receiving | `/api/v1/inbound/ad-hoc-receipts` | POST | Record non-PO inbound receipt with governance authorization | UC-011 | Goods Receipt |
| API-076 | Inbound Receiving | `/api/v1/inbound/return-receipts` | POST | Accept physical customer return shipment at receiving dock | UC-011, UC-036 | Goods Receipt, Customer Return Case |
| API-077 | Inbound Receiving | `/api/v1/inbound/supplier-invoices` | POST | Register supplier billing document for financial control | UC-039 | Supplier Invoice |
| API-078 | Inbound Receiving | `/api/v1/inbound/supplier-invoices/{invoiceId}` | GET | Retrieve supplier invoice and three-way match status | UC-039 | Supplier Invoice |
| API-079 | Inbound Receiving | `/api/v1/inbound/supplier-invoices/{invoiceId}/three-way-match` | POST | Execute three-way match evaluation against PO and goods receipt | UC-039 | Supplier Invoice |
| API-080 | Inbound Receiving | `/api/v1/inbound/supplier-invoices/{invoiceId}/authorize-payment` | POST | Authorize invoice payment after successful three-way match | UC-039 | Supplier Invoice |

---

## M-07 — Order Fulfillment

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-081 | Order Fulfillment | `/api/v1/fulfillment/orders` | POST | Import or create customer order for fulfillment processing | UC-021, UC-022 | Customer Order Fulfillment |
| API-082 | Order Fulfillment | `/api/v1/fulfillment/orders` | GET | List customer orders with status and location filters | UC-027 | Customer Order Fulfillment |
| API-083 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}` | GET | Retrieve customer order detail and line breakdown | UC-027 | Customer Order Fulfillment |
| API-084 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/availability` | POST | Confirm order availability using ATP before commercial commitment | UC-013, UC-021 | Customer Order Fulfillment |
| API-085 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/confirm` | POST | Confirm customer order and initiate stock reservation saga | UC-022 | Customer Order Fulfillment |
| API-086 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/cancel` | POST | Cancel customer order and release reserved stock | UC-023 | Customer Order Fulfillment |
| API-087 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/multi-location-plan` | POST | Create multi-location fulfillment plan when single location ATP is insufficient | UC-048 | Customer Order Fulfillment |
| API-088 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/pick-lists` | POST | Assign pick work to warehouse for order fulfillment | UC-024 | Customer Order Fulfillment |
| API-089 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/pick-lists/awaiting` | GET | List orders awaiting pick at a fulfillment location | UC-024 | Customer Order Fulfillment |
| API-090 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/picks/{pickId}/verify` | POST | Verify physical pick matches order requirements and capture lot/batch | UC-024 | Customer Order Fulfillment |
| API-091 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/pack` | POST | Complete packing step for verified pick | UC-024 | Customer Order Fulfillment |
| API-092 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/shipments` | POST | Dispatch shipment and trigger inventory deduction for picked goods | UC-024 | Customer Order Fulfillment |
| API-093 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/partial-fulfillment` | POST | Fulfill available quantity and route remainder to backorder workflow | UC-025 | Customer Order Fulfillment |
| API-094 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/backorders` | POST | Record backorder with customer acknowledgment for unfulfilled quantity | UC-025 | Customer Order Fulfillment |
| API-095 | Order Fulfillment | `/api/v1/fulfillment/backorders/{backorderId}/fulfill` | POST | Fulfill previously backordered quantity when stock becomes available | UC-025 | Customer Order Fulfillment |
| API-096 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/exceptions` | POST | Raise and document outbound fulfillment exception for manager resolution | UC-026 | Customer Order Fulfillment |
| API-097 | Order Fulfillment | `/api/v1/fulfillment/orders/{orderId}/status` | GET | Retrieve order fulfillment status (reservation, pick, ship, exception) | UC-027 | Customer Order Fulfillment |

---

## M-08 — Network Transfer

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-098 | Network Transfer | `/api/v1/transfers` | POST | Request inter-location stock transfer to resolve local shortage | UC-031 | Stock Transfer |
| API-099 | Network Transfer | `/api/v1/transfers` | GET | List stock transfers with status and location filters | UC-031, UC-033 | Stock Transfer |
| API-100 | Network Transfer | `/api/v1/transfers/{transferId}` | GET | Retrieve transfer request status, lines, and in-transit state | UC-031, UC-033 | Stock Transfer |
| API-101 | Network Transfer | `/api/v1/transfers/{transferId}/approve` | POST | Approve transfer request after source capacity validation | UC-032 | Stock Transfer |
| API-102 | Network Transfer | `/api/v1/transfers/{transferId}/reject` | POST | Reject transfer request with documented reason | UC-032 | Stock Transfer |
| API-103 | Network Transfer | `/api/v1/transfers/{transferId}/dispatch` | POST | Dispatch stock from source location and create in-transit state | UC-033 | Stock Transfer |
| API-104 | Network Transfer | `/api/v1/transfers/{transferId}/receive` | POST | Confirm receipt of transferred stock at destination location | UC-033 | Stock Transfer |
| API-105 | Network Transfer | `/api/v1/transfers/{transferId}/cancel` | POST | Cancel in-transit transfer with reversal workflow | UC-033 | Stock Transfer |
| API-106 | Network Transfer | `/api/v1/transfers/pending-approvals` | GET | List transfer requests awaiting management approval | UC-032, UC-047 | Stock Transfer |
| API-107 | Network Transfer | `/api/v1/transfers/in-transit` | GET | List in-transit stock pipeline by location | UC-030, UC-033 | Stock Transfer |

---

## M-09 — Inventory Accuracy

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-108 | Inventory Accuracy | `/api/v1/accuracy/cycle-counts` | POST | Schedule cycle count assignment for product at location | UC-014 | Cycle Count |
| API-109 | Inventory Accuracy | `/api/v1/accuracy/cycle-counts` | GET | List cycle count assignments by location and status | UC-014 | Cycle Count |
| API-110 | Inventory Accuracy | `/api/v1/accuracy/cycle-counts/{cycleCountId}` | GET | Retrieve cycle count assignment without revealing system quantity (blind count) | UC-014 | Cycle Count |
| API-111 | Inventory Accuracy | `/api/v1/accuracy/cycle-counts/{cycleCountId}/result` | POST | Submit blind cycle count physical result | UC-014 | Cycle Count |
| API-112 | Inventory Accuracy | `/api/v1/accuracy/physical-counts` | POST | Initiate wall-to-wall physical inventory count and impose location freeze | UC-015 | Physical Inventory Count |
| API-113 | Inventory Accuracy | `/api/v1/accuracy/physical-counts/{physicalCountId}` | GET | Retrieve physical count progress and freeze window status | UC-015 | Physical Inventory Count |
| API-114 | Inventory Accuracy | `/api/v1/accuracy/physical-counts/{physicalCountId}/results` | POST | Submit line-level count result during freeze period | UC-015 | Physical Inventory Count |
| API-115 | Inventory Accuracy | `/api/v1/accuracy/physical-counts/{physicalCountId}/certify` | POST | Certify physical count complete and release location freeze | UC-015 | Physical Inventory Count |
| API-116 | Inventory Accuracy | `/api/v1/accuracy/adjustment-cases` | POST | Open adjustment case from count variance or direct adjustment request | UC-016, UC-017 | Inventory Adjustment Case |
| API-117 | Inventory Accuracy | `/api/v1/accuracy/adjustment-cases/{caseId}` | GET | Retrieve adjustment case investigation and approval state | UC-016, UC-017 | Inventory Adjustment Case |
| API-118 | Inventory Accuracy | `/api/v1/accuracy/adjustment-cases/{caseId}/investigate` | POST | Document variance root cause investigation findings | UC-016 | Inventory Adjustment Case |
| API-119 | Inventory Accuracy | `/api/v1/accuracy/adjustment-cases/{caseId}/variances/{varianceId}/approve` | POST | Approve count variance for adjustment with independent approver | UC-016 | Inventory Adjustment Case |
| API-120 | Inventory Accuracy | `/api/v1/accuracy/adjustment-cases/{caseId}/submit` | POST | Submit adjustment or write-off for governance approval | UC-017, UC-018 | Inventory Adjustment Case |
| API-121 | Inventory Accuracy | `/api/v1/accuracy/adjustment-cases/{caseId}/approve` | POST | Approve inventory adjustment or write-off after threshold validation | UC-017, UC-018 | Inventory Adjustment Case |
| API-122 | Inventory Accuracy | `/api/v1/accuracy/adjustment-cases/{caseId}/reject` | POST | Reject proposed adjustment with documented reason | UC-017, UC-018 | Inventory Adjustment Case |
| API-123 | Inventory Accuracy | `/api/v1/accuracy/pending-approvals` | GET | List adjustment cases awaiting independent approval | UC-016, UC-017, UC-047 | Inventory Adjustment Case |

---

## M-10 — Returns Management

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-124 | Returns Management | `/api/v1/returns/authorizations` | POST | Issue return authorization (RMA) linked to original customer order | UC-035 | Customer Return Case |
| API-125 | Returns Management | `/api/v1/returns/authorizations` | GET | List return authorizations with status filter | UC-035, UC-036 | Customer Return Case |
| API-126 | Returns Management | `/api/v1/returns/authorizations/{returnAuthorizationId}` | GET | Retrieve RMA status, eligibility, and linked order reference | UC-035 | Customer Return Case |
| API-127 | Returns Management | `/api/v1/returns/authorizations/{returnAuthorizationId}/cancel` | POST | Cancel unused return authorization | UC-035 | Customer Return Case |
| API-128 | Returns Management | `/api/v1/returns/{returnId}/receive` | POST | Record physical receipt and verification of authorized return goods | UC-036 | Customer Return Case |
| API-129 | Returns Management | `/api/v1/returns/{returnId}/inspect` | POST | Inspect returned goods and record condition grade | UC-036 | Customer Return Case |
| API-130 | Returns Management | `/api/v1/returns/{returnId}/disposition` | POST | Route return to restock, quarantine, or write-off disposition | UC-036 | Customer Return Case |
| API-131 | Returns Management | `/api/v1/returns/pending-receipts` | GET | List authorized returns awaiting warehouse receipt | UC-036 | Customer Return Case |

---

## M-11 — Commercial Campaign

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-132 | Commercial Campaign | `/api/v1/campaigns/allocations` | POST | Create promotional stock allocation and ring-fence quantity | UC-040 | Promotional Stock Allocation |
| API-133 | Commercial Campaign | `/api/v1/campaigns/allocations` | GET | List promotional allocations by campaign period and status | UC-040 | Promotional Stock Allocation |
| API-134 | Commercial Campaign | `/api/v1/campaigns/allocations/{allocationId}` | GET | Retrieve promotional allocation status and ring-fenced quantity | UC-040 | Promotional Stock Allocation |
| API-135 | Commercial Campaign | `/api/v1/campaigns/allocations/{allocationId}` | PATCH | Amend allocated quantity or campaign period | UC-040 | Promotional Stock Allocation |
| API-136 | Commercial Campaign | `/api/v1/campaigns/allocations/{allocationId}/readiness` | POST | Confirm or evaluate campaign stock readiness before launch | UC-040, UC-047 | Promotional Stock Allocation |
| API-137 | Commercial Campaign | `/api/v1/campaigns/allocations/{allocationId}/release` | POST | Release unconsumed promotional allocation after campaign end | UC-040 | Promotional Stock Allocation |
| API-138 | Commercial Campaign | `/api/v1/campaigns/allocations/{allocationId}/override` | POST | Authorize non-promotional consumption of ring-fenced stock | UC-040 | Promotional Stock Allocation |
| API-139 | Commercial Campaign | `/api/v1/campaigns/ring-fence/{locationCode}/{sku}` | GET | Check whether SKU has active promotional ring-fence at location | UC-022, UC-040 | Promotional Stock Allocation |

---

## M-12 — Identity & Access

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-140 | Identity & Access | `/api/v1/users` | POST | Provision new user account with initial role assignments | UC-044 | User Account |
| API-141 | Identity & Access | `/api/v1/users` | GET | List user accounts with role and status filters | UC-044 | User Account |
| API-142 | Identity & Access | `/api/v1/users/{userId}` | GET | Retrieve user profile and role assignments | UC-044, UC-045 | User Account |
| API-143 | Identity & Access | `/api/v1/users/{userId}/roles` | POST | Assign role with location scope to user account | UC-044, UC-045 | User Account |
| API-144 | Identity & Access | `/api/v1/users/{userId}/roles/{roleAssignmentId}` | DELETE | Revoke role assignment from user account | UC-044 | User Account |
| API-145 | Identity & Access | `/api/v1/users/{userId}/suspend` | POST | Temporarily suspend user account access | UC-044 | User Account |
| API-146 | Identity & Access | `/api/v1/users/{userId}/deactivate` | POST | Permanently deactivate user account | UC-044 | User Account |
| API-147 | Identity & Access | `/api/v1/users/sync` | POST | Synchronize user identities from enterprise HR directory | UC-044 | User Account |
| API-148 | Identity & Access | `/api/v1/authorization/actions/evaluate` | POST | Evaluate whether authenticated user may execute a command | UC-045 | User Account |
| API-149 | Identity & Access | `/api/v1/authorization/location-scope/validate` | POST | Validate user is authorized for a specific location scope | UC-045 | User Account |

---

## M-13 — Inventory Intelligence

Read-only APIs serving dashboards, reports, movement history, audit trails, alerts, and valuation projections. No aggregate mutation.

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-150 | Inventory Intelligence | `/api/v1/intelligence/dashboard` | GET | Retrieve inventory summary dashboard by location or network | UC-037 | *(Read projection — no aggregate)* |
| API-151 | Inventory Intelligence | `/api/v1/intelligence/stock-status/summary` | GET | Retrieve aggregated on-hand, ATP, and status counts | UC-012, UC-037 | *(Read projection)* |
| API-152 | Inventory Intelligence | `/api/v1/intelligence/stock-status/board` | GET | Retrieve network stock status board with health indicators | UC-012, UC-037 | Stock Position *(projection)* |
| API-153 | Inventory Intelligence | `/api/v1/intelligence/availability/inquiries` | GET | Retrieve availability inquiry log for sales accountability | UC-013, UC-021 | Customer Order Fulfillment *(projection)* |
| API-154 | Inventory Intelligence | `/api/v1/intelligence/quarantine-register` | GET | Retrieve quarantine and hold register across locations | UC-019, UC-037 | Stock Position *(projection)* |
| API-155 | Inventory Intelligence | `/api/v1/intelligence/movements` | GET | Search inventory movement history by SKU, location, user, and date | UC-042 | *(Inventory Movement Record projection)* |
| API-156 | Inventory Intelligence | `/api/v1/intelligence/audit-trail` | GET | Query immutable audit trail of material inventory changes | UC-043, UC-041 | *(Audit Trail Record projection)* |
| API-157 | Inventory Intelligence | `/api/v1/intelligence/audit-trail/export` | GET | Export audit evidence package for internal or external audit | UC-041, UC-043 | *(Audit Trail Record projection)* |
| API-158 | Inventory Intelligence | `/api/v1/intelligence/alerts` | GET | Retrieve active operational alerts for user and location scope | UC-028, UC-047 | *(Operational Alert projection)* |
| API-159 | Inventory Intelligence | `/api/v1/intelligence/alerts/{alertId}/acknowledge` | POST | Acknowledge operational alert without mutating inventory state | UC-028, UC-047 | *(Operational Alert projection)* |
| API-160 | Inventory Intelligence | `/api/v1/intelligence/replenishment/recommendations` | GET | Retrieve replenishment recommendation log | UC-028, UC-029, UC-034 | *(Read projection)* |
| API-161 | Inventory Intelligence | `/api/v1/intelligence/procurement/open-pos` | GET | Retrieve open purchase order board for inbound pipeline | UC-006, UC-030 | Purchase Order *(projection)* |
| API-162 | Inventory Intelligence | `/api/v1/intelligence/procurement/inbound-calendar` | GET | Retrieve expected inbound supply calendar | UC-007, UC-030 | Purchase Order *(projection)* |
| API-163 | Inventory Intelligence | `/api/v1/intelligence/procurement/inbound-delays` | GET | Retrieve inbound delivery delay log | UC-030, UC-047 | Purchase Order *(projection)* |
| API-164 | Inventory Intelligence | `/api/v1/intelligence/fulfillment/backorders` | GET | Retrieve backorder pipeline sorted by policy priority | UC-025, UC-027 | Customer Order Fulfillment *(projection)* |
| API-165 | Inventory Intelligence | `/api/v1/intelligence/fulfillment/exceptions` | GET | Retrieve open fulfillment exception log | UC-026, UC-027 | Customer Order Fulfillment *(projection)* |
| API-166 | Inventory Intelligence | `/api/v1/intelligence/network/imbalance` | GET | Retrieve network imbalance analysis and transfer recommendations | UC-034 | *(Read projection)* |
| API-167 | Inventory Intelligence | `/api/v1/intelligence/accuracy/shrinkage` | GET | Retrieve shrinkage, loss, and obsolete stock analysis | UC-020 | Inventory Adjustment Case *(projection)* |
| API-168 | Inventory Intelligence | `/api/v1/intelligence/accuracy/count-performance` | GET | Retrieve cycle count and physical count accuracy metrics | UC-014, UC-015, UC-037 | Cycle Count, Physical Inventory Count *(projection)* |
| API-169 | Inventory Intelligence | `/api/v1/intelligence/campaigns/readiness` | GET | Retrieve promotional campaign readiness status | UC-040, UC-047 | Promotional Stock Allocation *(projection)* |
| API-170 | Inventory Intelligence | `/api/v1/intelligence/kpis` | GET | Retrieve executive inventory performance KPIs | UC-038 | *(KPI Dashboard projection)* |
| API-171 | Inventory Intelligence | `/api/v1/intelligence/valuation/snapshots` | GET | Retrieve period-end inventory valuation snapshots | UC-039 | *(Inventory Valuation Snapshot projection)* |
| API-172 | Inventory Intelligence | `/api/v1/intelligence/valuation/reconciliation` | GET | Retrieve inventory valuation vs. general ledger reconciliation report | UC-039 | *(Inventory Valuation Snapshot projection)* |

---

## Platform & Integration

Cross-cutting and external-integration APIs supporting authentication, health monitoring, and enterprise system boundaries.

| API ID | Business Module | Endpoint | HTTP Method | Purpose | Related Use Case | Related Aggregate |
|--------|-----------------|----------|-------------|---------|------------------|-------------------|
| API-173 | Identity & Access | `/api/v1/auth/session` | GET | Validate authenticated session and retrieve user context | UC-045 | User Account |
| API-174 | Identity & Access | `/api/v1/auth/logout` | POST | Terminate authenticated session | UC-045 | *(Infrastructure — no aggregate)* |
| API-175 | Platform | `/api/v1/health` | GET | Application health check for operations monitoring | — | *(Infrastructure)* |
| API-176 | Integration (EXT-01) | `/api/v1/integrations/sales/orders` | POST | Import customer order from Sales/CRM system (ACL inbound) | UC-021, UC-022 | Customer Order Fulfillment |
| API-177 | Integration (EXT-01) | `/api/v1/integrations/sales/fulfillment-status` | GET | Publish fulfillment status feed to Sales/CRM (ACL outbound) | UC-027 | Customer Order Fulfillment *(projection)* |
| API-178 | Integration (EXT-07) | `/api/v1/integrations/marketing/campaign-plans` | POST | Import campaign plan from marketing system (ACL inbound) | UC-040 | Promotional Stock Allocation |

---

## Use Case Coverage Matrix

All 48 use cases from SRS-UC-001 are supported by at least one REST API in this catalog.

| Use Case | Supporting API IDs |
|----------|------------------|
| UC-001 Manage Product Master Data | API-001 – API-009 |
| UC-002 Configure Inventory Locations | API-011 – API-021 |
| UC-003 Define Stock Policies and Thresholds | API-038 – API-040 |
| UC-004 Classify Products by ABC Priority | API-006 |
| UC-005 Maintain Governance Policies and Reason Codes | API-022 – API-031 |
| UC-006 Place and Manage Purchase Orders | API-049 – API-063, API-161 |
| UC-007 Plan Expected Inbound Deliveries | API-064, API-162 |
| UC-008 Receive and Verify Supplier Goods | API-065 – API-069 |
| UC-009 Document and Resolve Receipt Discrepancies | API-070 – API-072, API-025, API-030 |
| UC-010 Perform Stock Put-Away | API-073, API-074, API-015, API-016 |
| UC-011 Receive Return and Non-PO Inbound Stock | API-075, API-076, API-128 |
| UC-012 Monitor Inventory Status | API-033 – API-037, API-151, API-152 |
| UC-013 Inquire Inventory Availability | API-002, API-003, API-035, API-036, API-153 |
| UC-014 Perform Cycle Count | API-108 – API-111, API-168 |
| UC-015 Conduct Full Physical Inventory Count | API-112 – API-115, API-020 |
| UC-016 Investigate and Approve Count Variances | API-116 – API-119, API-123 |
| UC-017 Process Stock Adjustments | API-120 – API-122 |
| UC-018 Authorize and Process Inventory Write-Offs | API-120 – API-122 |
| UC-019 Manage Quarantine and Hold Stock | API-045, API-046, API-154 |
| UC-020 Analyze Shrinkage, Loss, and Obsolete Stock | API-167 |
| UC-021 Confirm Order Availability | API-035, API-036, API-084, API-176 |
| UC-022 Reserve Inventory for Confirmed Orders | API-043, API-085, API-139 |
| UC-023 Release Inventory Reservations | API-044, API-086 |
| UC-024 Pick, Pack, and Ship Orders | API-088 – API-092, API-041 |
| UC-025 Handle Partial Fulfillment and Backorders | API-093 – API-095, API-164 |
| UC-026 Handle Outbound Fulfillment Exceptions | API-096, API-165 |
| UC-027 View Order Fulfillment Status | API-082, API-083, API-097, API-177 |
| UC-028 Review Low-Stock and Out-of-Stock Alerts | API-037, API-158, API-159, API-160 |
| UC-029 Plan Replenishment and Create Purchase Requisitions | API-054 – API-058, API-160 |
| UC-030 Track Inbound Supply Status | API-060, API-061, API-064, API-107, API-161 – API-163 |
| UC-031 Request Inter-Location Stock Transfer | API-098 – API-100, API-042 |
| UC-032 Approve or Reject Transfer Requests | API-101, API-102, API-106 |
| UC-033 Execute and Record Inter-Location Transfer | API-103 – API-105, API-107 |
| UC-034 Analyze and Recommend Network Rebalancing | API-036, API-166, API-160 |
| UC-035 Authorize and Record Customer Returns | API-124 – API-127 |
| UC-036 Receive, Inspect, and Disposition Returned Goods | API-076, API-128 – API-131 |
| UC-037 Review Inventory Dashboards and Operational Reports | API-150 – API-152, API-154, API-168 |
| UC-038 Review Inventory Performance KPIs | API-170 |
| UC-039 Reconcile Inventory Valuation with Finance | API-077 – API-080, API-047, API-171, API-172 |
| UC-040 Confirm Promotional and Launch Stock Readiness | API-132 – API-139, API-169, API-178 |
| UC-041 Conduct Inventory Audit and Control Review | API-156, API-157 |
| UC-042 View Inventory Movement and Transaction History | API-155 |
| UC-043 Query and Review Audit Trail | API-156, API-157 |
| UC-044 Manage User Accounts and Role Assignments | API-140 – API-147 |
| UC-045 Enforce Role-Based and Location-Scoped Access | API-031, API-148, API-149, API-173 |
| UC-046 Import Initial Product and Stock Master Data | API-010, API-017, API-032 |
| UC-047 Receive and Respond to Operational Notifications | API-158, API-159, API-106, API-123, API-163, API-169 |
| UC-048 Support Multi-Location Split Fulfillment | API-036, API-087 |

---

## Aggregate Coverage Matrix

All 18 domain aggregates from SRS-DM-003 are accessed through at least one REST API. Read projections and infrastructure endpoints are noted separately.

| Aggregate | REST API IDs |
|-----------|--------------|
| Product Catalog | API-001 – API-010 |
| Inventory Location | API-011 – API-021 |
| Inventory Governance | API-022 – API-031 |
| Stock Position | API-032 – API-037, API-041 – API-048 |
| Stock Policy | API-038 – API-040, API-042 |
| Supplier | API-049 – API-053 |
| Purchase Requisition | API-054 – API-058 |
| Purchase Order | API-059 – API-065, API-161 – API-163 |
| Goods Receipt | API-066 – API-076 |
| Supplier Invoice | API-077 – API-080 |
| Customer Order Fulfillment | API-081 – API-097, API-153, API-164 – API-165, API-176, API-177 |
| Stock Transfer | API-098 – API-107 |
| Cycle Count | API-108 – API-111, API-168 |
| Physical Inventory Count | API-112 – API-115, API-168 |
| Inventory Adjustment Case | API-116 – API-123, API-167 |
| Customer Return Case | API-124 – API-131, API-076 |
| Promotional Stock Allocation | API-132 – API-139, API-169, API-178 |
| User Account | API-140 – API-149, API-173 |

---

## Domain Command to API Mapping

Write APIs trace to domain commands (SRS-ES-002). Internal reaction commands (triggered by domain events) are not exposed as public REST endpoints.

| Domain Command | REST API |
|----------------|----------|
| CMD-001 RegisterProduct | API-001 |
| CMD-002 ChangeProductStatus | API-005 |
| CMD-003 AssignABCClassification | API-006 |
| CMD-004 ActivateInventoryLocation | API-017 |
| CMD-005 DeactivateInventoryLocation | API-018 |
| CMD-006 ConfigureStoragePosition | API-015 |
| CMD-007 PublishGovernancePolicy | API-026 |
| CMD-008 RetireReasonCode | API-024 |
| CMD-009 StartPhysicalInventoryCount | API-112 |
| CMD-010 CertifyPhysicalInventoryCount | API-115 |
| CMD-011 UpdateStockPolicyThresholds | API-040 |
| CMD-012 ReserveStock | API-043, API-085 |
| CMD-013 ReleaseReservation | API-044, API-086 |
| CMD-014 ReceiveStock | *(Internal — API-073, API-104, API-130 trigger via events)* |
| CMD-015 ShipStock | *(Internal — API-092 triggers via event)* |
| CMD-016 ApplyApprovedAdjustment | *(Internal — API-121 triggers via event)* |
| CMD-017 ApplyApprovedWriteOff | *(Internal — API-121, API-130 trigger via events)* |
| CMD-018 ApplyQuarantineHold | API-045 |
| CMD-019 ReleaseQuarantineHold | API-046 |
| CMD-020 TransferConsignmentOwnership | API-047 |
| CMD-021 SubmitPurchaseRequisition | API-054 |
| CMD-022 ApprovePurchaseRequisition | API-056 |
| CMD-023 RejectPurchaseRequisition | API-057 |
| CMD-024 PlacePurchaseOrder | API-059 |
| CMD-025 CancelPurchaseOrder | API-063 |
| CMD-026 ScheduleInboundDelivery | API-064 |
| CMD-027 RecordInboundDelay | *(Intelligence projection — API-163)* |
| CMD-028 VerifyGoodsReceipt | API-069 |
| CMD-029 RecordReceiptDiscrepancy | API-070 |
| CMD-030 ResolveReceiptDiscrepancy | API-072 |
| CMD-031 CompletePutAway | API-073 |
| CMD-032 RecordSupplierInvoice | API-077 |
| CMD-033 EvaluateThreeWayMatch | API-079 |
| CMD-034 ConfirmOrderAvailability | API-084 |
| CMD-035 ConfirmCustomerOrder | API-085 |
| CMD-036 CancelCustomerOrder | API-086 |
| CMD-037 CreateMultiLocationFulfillmentPlan | API-087 |
| CMD-038 VerifyPick | API-090 |
| CMD-039 DispatchShipment | API-092 |
| CMD-040 CompletePartialFulfillment | API-093 |
| CMD-041 RecordBackorder | API-094 |
| CMD-042 FulfillBackorder | API-095 |
| CMD-043 RaiseFulfillmentException | API-096 |
| CMD-044 DispatchTransferStock | *(Internal — API-103 triggers via event)* |
| CMD-045 RequestStockTransfer | API-098 |
| CMD-046 ApproveTransferRequest | API-101 |
| CMD-047 RejectTransferRequest | API-102 |
| CMD-048 DispatchTransfer | API-103 |
| CMD-049 ConfirmTransferReceipt | API-104 |
| CMD-050 RecordTransferDelay | *(Intelligence projection — API-107)* |
| CMD-051 ScheduleCycleCount | API-108 |
| CMD-052 SubmitCycleCountResult | API-111 |
| CMD-053 ApproveCountVariance | API-119 |
| CMD-054 SubmitAdjustment | API-120 |
| CMD-055 ApproveAdjustment | API-121 |
| CMD-056 RejectAdjustment | API-122 |
| CMD-057 IdentifyCountVariance | *(Internal — API-111, API-115 trigger)* |
| CMD-058 EstablishOpeningBalances | API-032 |
| CMD-059 ApplyQuarantineFromReturn | *(Internal — API-130 triggers via event)* |
| CMD-060 RecordCountVarianceFromPhysicalCount | *(Internal — API-115 triggers)* |
| CMD-061 IssueReturnAuthorization | API-124 |
| CMD-062 ExpireReturnAuthorization | *(Policy-driven — no direct REST)* |
| CMD-063 ReceiveCustomerReturn | API-128 |
| CMD-064 InspectReturnedGoods | API-129 |
| CMD-065 RestockReturnedGoods | API-130 *(disposition: restock)* |
| CMD-066 QuarantineReturnedGoods | API-130 *(disposition: quarantine)* |
| CMD-067 WriteOffReturnedGoods | API-130 *(disposition: write-off)* |
| CMD-068 AllocatePromotionalStock | API-132 |
| CMD-069 ReleasePromotionalAllocation | API-137 |
| CMD-070 EvaluateStockStatus | *(Internal policy — surfaces via API-037, API-158)* |
| CMD-071 RecommendReplenishmentAction | *(Intelligence — API-160)* |
| CMD-072 EvaluatePromotionalReadiness | API-136 |
| CMD-073 AnalyzeNetworkBalance | *(Intelligence — API-166)* |
| CMD-074 PrepareValuationSnapshot | *(Intelligence — API-171)* |
| CMD-075 ReconcileInventoryValuation | *(Intelligence — API-172)* |
| CMD-076 ProvisionUserAccount | API-140 |
| CMD-077 ChangeRoleAssignment | API-143, API-144 |
| CMD-078 ValidateSegregationOfDuties | API-031, API-148 |

---

## Excluded from Public REST Exposure

The following capabilities are intentionally not exposed as REST APIs per architecture boundaries:

| Capability | Treatment | Rationale |
|------------|-----------|-----------|
| Internal domain event handlers (CMD-014–017, CMD-044, CMD-057–060) | Event-driven choreography | Cross-aggregate consistency via events, not direct client invocation |
| Notification delivery (email/SMS) | SVC-02 gateway | Infrastructure concern; Intelligence raises alerts, gateway delivers |
| SSO authentication handshake | SVC-01 IdP | Standard OIDC/SAML — not IMS domain API |
| Finance ERP file export (MVP) | Scheduled batch job | TEC-05 file export; Phase 3 moves to API-172 feed |
| Supplier EDI / carrier tracking (MVP) | Human-mediated | EXT-04, EXT-05 — no direct system integration in MVP |
| Database audit triggers | Persistence layer | SRS Database Audit Strategy — transparent to API consumers |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Backend Architect | | | |
| Solution Architect | | | |
| DDD Solution Architect | | | |
| Product Owner | | | |

---

*End of REST API Catalog*

*Document ID: SRS-API-001 | Version 1.0 | July 6, 2026*
