# Inventory Management System Screen Inventory

## Document Purpose

This document identifies the screens required for the Inventory Management System based on the approved BRD, use-case package, and API design package. It defines the screen inventory only and intentionally does not propose layouts, navigation, or wireframes.

## Scope Notes

- The screen list covers MVP plus approved future-phase capabilities already defined in the BRD, use cases, and API catalog.
- Screens are defined at page/workspace level. Closely related actions such as create, edit, review, and approve are grouped into one screen when they belong to the same user task.
- Where the API review identified an unresolved endpoint gap, the affected screen references the current APIs plus the noted gap.

---

## Access and Shared Experience

### UI-001
- **Screen name:** Sign In / Session Entry
- **Purpose:** Authenticate the user and establish the authorized IMS session and role/location context before any protected function is accessed.
- **Primary users:** All internal IMS users
- **Related use cases:** UC-045
- **Related APIs:** API-173 `GET /api/v1/auth/session`, API-174 `POST /api/v1/auth/logout`

### UI-002
- **Screen name:** Operational Home Dashboard
- **Purpose:** Provide the day-to-day landing view for operational users with inventory summary, stock health, alert counts, and shortcuts into core workflows.
- **Primary users:** Operations Director, Inventory Controller, Warehouse Manager, Purchasing Manager, Sales Manager
- **Related use cases:** UC-012, UC-037, UC-047
- **Related APIs:** API-150 `GET /api/v1/intelligence/dashboard`, API-151 `GET /api/v1/intelligence/stock-status/summary`, API-152 `GET /api/v1/intelligence/stock-status/board`, API-158 `GET /api/v1/intelligence/alerts`

### UI-003
- **Screen name:** Executive KPI Dashboard
- **Purpose:** Present strategic inventory KPIs, trends, target comparisons, and drill-downs for executive review.
- **Primary users:** Chief Executive Officer, Chief Operating Officer, Chief Financial Officer, Operations Director, Finance Manager
- **Related use cases:** UC-038
- **Related APIs:** API-170 `GET /api/v1/intelligence/kpis`

### UI-004
- **Screen name:** Notification Center
- **Purpose:** Centralize low-stock alerts, pending approvals, transfer issues, inbound delays, and campaign readiness notifications so users can review and act on them.
- **Primary users:** Warehouse Manager, Purchasing Manager, Operations Director, Buyer, Marketing Manager, Customer Service Representative
- **Related use cases:** UC-028, UC-032, UC-047
- **Related APIs:** API-158 `GET /api/v1/intelligence/alerts`, API-159 `POST /api/v1/intelligence/alerts/{alertId}/acknowledge`, API-106 `GET /api/v1/transfers/pending-approvals`, API-123 `GET /api/v1/accuracy/pending-approvals`, API-163 `GET /api/v1/intelligence/procurement/inbound-delays`, API-169 `GET /api/v1/intelligence/campaigns/readiness`

---

## Master Data and Governance

### UI-005
- **Screen name:** Product Catalog Management
- **Purpose:** Search, create, update, review, and maintain product master records including lifecycle status and identifiers.
- **Primary users:** Inventory Controller
- **Related use cases:** UC-001
- **Related APIs:** API-001 `POST /api/v1/products`, API-002 `GET /api/v1/products`, API-003 `GET /api/v1/products/{sku}`, API-004 `PATCH /api/v1/products/{sku}`, API-005 `POST /api/v1/products/{sku}/lifecycle-status`, API-008 `GET /api/v1/products/categories/{categoryCode}/products`, API-009 `POST /api/v1/products/duplicate-resolutions`

### UI-006
- **Screen name:** Product Import Workspace
- **Purpose:** Upload, validate, review, and complete bulk product and opening data imports during go-live or controlled data loads.
- **Primary users:** Inventory Controller, System Administrator
- **Related use cases:** UC-046
- **Related APIs:** API-010 `POST /api/v1/products/import`, API-032 `POST /api/v1/inventory/opening-balances`, API-017 `POST /api/v1/locations/{locationCode}/activate`

### UI-007
- **Screen name:** Location and Warehouse Management
- **Purpose:** Configure inventory locations, location hierarchy, storage positions, and operating status for the network.
- **Primary users:** Inventory Controller, Operations Director
- **Related use cases:** UC-002
- **Related APIs:** API-011 `POST /api/v1/locations`, API-012 `GET /api/v1/locations`, API-013 `GET /api/v1/locations/{locationCode}`, API-014 `PATCH /api/v1/locations/{locationCode}/hierarchy`, API-015 `POST /api/v1/locations/{locationCode}/storage-positions`, API-016 `GET /api/v1/locations/{locationCode}/storage-positions`, API-017 `POST /api/v1/locations/{locationCode}/activate`, API-018 `POST /api/v1/locations/{locationCode}/deactivate`, API-019 `POST /api/v1/locations/{locationCode}/close`, API-021 `GET /api/v1/locations/{locationCode}/operational-status`

### UI-008
- **Screen name:** Stock Policy and Threshold Management
- **Purpose:** Define and maintain reorder levels, minimum thresholds, and safety stock settings by product and location.
- **Primary users:** Inventory Controller, Purchasing Manager
- **Related use cases:** UC-003
- **Related APIs:** API-038 `POST /api/v1/inventory/stock-policies`, API-039 `GET /api/v1/inventory/stock-policies/{locationCode}/{sku}`, API-040 `PATCH /api/v1/inventory/stock-policies/{locationCode}/{sku}`

### UI-009
- **Screen name:** ABC Classification Management
- **Purpose:** Assign and review ABC product classes to support differentiated monitoring and counting discipline.
- **Primary users:** Inventory Controller
- **Related use cases:** UC-004
- **Related APIs:** API-006 `PUT /api/v1/products/{sku}/abc-classification`, API-002 `GET /api/v1/products`

### UI-010
- **Screen name:** Governance Policies and Reason Codes
- **Purpose:** Maintain standardized reason codes, approval thresholds, receipt tolerances, and governance policy versions.
- **Primary users:** Inventory Controller, Internal Auditor, Finance Manager, Operations Director
- **Related use cases:** UC-005
- **Related APIs:** API-022 `POST /api/v1/governance/reason-codes`, API-023 `GET /api/v1/governance/reason-codes`, API-024 `POST /api/v1/governance/reason-codes/{code}/retire`, API-025 `GET /api/v1/governance/reason-codes/{code}/validate`, API-026 `POST /api/v1/governance/policies`, API-027 `PATCH /api/v1/governance/policies/{policyId}/approval-thresholds`, API-028 `PATCH /api/v1/governance/policies/{policyId}/receipt-tolerances`, API-029 `GET /api/v1/governance/approval-thresholds`, API-030 `GET /api/v1/governance/receipt-tolerances`

---

## Procurement and Inbound

### UI-011
- **Screen name:** Supplier Management
- **Purpose:** Maintain supplier master data and supplier operational status used by procurement workflows.
- **Primary users:** Buyer, Purchasing Manager
- **Related use cases:** UC-006
- **Related APIs:** API-049 `POST /api/v1/suppliers`, API-050 `GET /api/v1/suppliers`, API-051 `GET /api/v1/suppliers/{supplierCode}`, API-052 `PATCH /api/v1/suppliers/{supplierCode}`, API-053 `POST /api/v1/suppliers/{supplierCode}/deactivate`

### UI-012
- **Screen name:** Purchase Order Management
- **Purpose:** Create, review, approve-state track, amend, and cancel purchase orders.
- **Primary users:** Buyer, Purchasing Manager
- **Related use cases:** UC-006
- **Related APIs:** API-059 `POST /api/v1/procurement/purchase-orders`, API-060 `GET /api/v1/procurement/purchase-orders`, API-061 `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}`, API-062 `PATCH /api/v1/procurement/purchase-orders/{purchaseOrderId}`, API-063 `POST /api/v1/procurement/purchase-orders/{purchaseOrderId}/cancel`, API-065 `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}/validate-for-receipt`, API-161 `GET /api/v1/intelligence/procurement/open-pos`

### UI-013
- **Screen name:** Purchase Requisition Management
- **Purpose:** Review replenishment-driven requisitions, submit them for approval, and convert approved requisitions into purchase orders.
- **Primary users:** Buyer, Purchasing Manager
- **Related use cases:** UC-029
- **Related APIs:** API-054 `POST /api/v1/procurement/requisitions`, API-055 `GET /api/v1/procurement/requisitions/{requisitionId}`, API-056 `POST /api/v1/procurement/requisitions/{requisitionId}/approve`, API-057 `POST /api/v1/procurement/requisitions/{requisitionId}/reject`, API-058 `POST /api/v1/procurement/requisitions/{requisitionId}/convert-to-po`
- **API note:** API review item `C-03` identifies the missing requisition list endpoint needed for full queue browsing.

### UI-014
- **Screen name:** Inbound Delivery Planning
- **Purpose:** Plan, update, and communicate expected supplier deliveries to receiving locations.
- **Primary users:** Buyer, Warehouse Manager, Receiving Clerk
- **Related use cases:** UC-007, UC-030
- **Related APIs:** API-064 `POST /api/v1/procurement/purchase-orders/{purchaseOrderId}/expected-deliveries`, API-162 `GET /api/v1/intelligence/procurement/inbound-calendar`, API-163 `GET /api/v1/intelligence/procurement/inbound-delays`

### UI-015
- **Screen name:** Goods Receipt Workbench
- **Purpose:** Receive supplier goods, verify products and quantities, capture lot and shelf-life data, and stage stock for put-away.
- **Primary users:** Receiving Clerk
- **Related use cases:** UC-008
- **Related APIs:** API-065 `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}/validate-for-receipt`, API-066 `POST /api/v1/inbound/goods-receipts`, API-067 `GET /api/v1/inbound/goods-receipts`, API-068 `GET /api/v1/inbound/goods-receipts/{goodsReceiptId}`, API-069 `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/verify`

### UI-016
- **Screen name:** Receipt Discrepancy Resolution
- **Purpose:** Record, review, and resolve inbound discrepancies such as shortages, wrong items, damage, or tolerance breaches.
- **Primary users:** Receiving Clerk, Warehouse Manager, Buyer
- **Related use cases:** UC-009
- **Related APIs:** API-070 `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies`, API-071 `GET /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies`, API-072 `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies/{discrepancyId}/resolve`, API-025 `GET /api/v1/governance/reason-codes/{code}/validate`, API-030 `GET /api/v1/governance/receipt-tolerances`

### UI-017
- **Screen name:** Put-Away Workbench
- **Purpose:** Present pending put-away tasks, storage destination choices, and completion confirmation for received stock.
- **Primary users:** Warehouse Staff
- **Related use cases:** UC-010
- **Related APIs:** API-074 `GET /api/v1/inbound/pending-put-away`, API-073 `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/put-away`, API-015 `POST /api/v1/locations/{locationCode}/storage-positions`, API-016 `GET /api/v1/locations/{locationCode}/storage-positions`

### UI-018
- **Screen name:** Non-PO and Return Receipt Intake
- **Purpose:** Record authorized non-PO inbound stock and return-related inbound receipts that arrive outside standard supplier PO flow.
- **Primary users:** Receiving Clerk
- **Related use cases:** UC-011
- **Related APIs:** API-075 `POST /api/v1/inbound/ad-hoc-receipts`, API-076 `POST /api/v1/inbound/return-receipts`
- **API note:** API review item `C-04` recommends API-128 as the canonical returns-receipt path for returns UI.

### UI-019
- **Screen name:** Inbound Supply Tracking
- **Purpose:** Monitor open purchase orders, expected arrivals, delays, and outstanding inbound quantities for replenishment visibility.
- **Primary users:** Buyer, Purchasing Manager, Warehouse Manager
- **Related use cases:** UC-030
- **Related APIs:** API-060 `GET /api/v1/procurement/purchase-orders`, API-061 `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}`, API-064 `POST /api/v1/procurement/purchase-orders/{purchaseOrderId}/expected-deliveries`, API-107 `GET /api/v1/transfers/in-transit`, API-161 `GET /api/v1/intelligence/procurement/open-pos`, API-162 `GET /api/v1/intelligence/procurement/inbound-calendar`, API-163 `GET /api/v1/intelligence/procurement/inbound-delays`

---

## Inventory Visibility and Control

### UI-020
- **Screen name:** Inventory Status Monitor
- **Purpose:** Give network-wide visibility into on-hand, reserved, ATP, low-stock, out-of-stock, overstock, and quarantined conditions.
- **Primary users:** Inventory Controller, Operations Director, Warehouse Manager, Purchasing Manager
- **Related use cases:** UC-012
- **Related APIs:** API-012 `GET /api/v1/locations`, API-033 `GET /api/v1/inventory/stock-positions`, API-034 `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}`, API-037 `GET /api/v1/inventory/stock-status/{locationCode}/{sku}`, API-151 `GET /api/v1/intelligence/stock-status/summary`, API-152 `GET /api/v1/intelligence/stock-status/board`

### UI-021
- **Screen name:** Inventory Availability Inquiry
- **Purpose:** Allow sales and service users to quickly search products and confirm ATP and network availability during customer conversations.
- **Primary users:** Sales Representative, Customer Service Representative, Sales Manager
- **Related use cases:** UC-013, UC-021
- **Related APIs:** API-002 `GET /api/v1/products`, API-003 `GET /api/v1/products/{sku}`, API-035 `GET /api/v1/inventory/availability/{sku}`, API-036 `GET /api/v1/inventory/availability/{sku}/network`, API-084 `POST /api/v1/fulfillment/orders/{orderId}/availability`, API-153 `GET /api/v1/intelligence/availability/inquiries`

### UI-022
- **Screen name:** Inventory Movement History
- **Purpose:** Trace inventory transactions by product, location, user, type, and date for investigation and operational accountability.
- **Primary users:** Inventory Controller, Warehouse Manager, Finance Manager, Internal Auditor, Operations Director
- **Related use cases:** UC-042
- **Related APIs:** API-155 `GET /api/v1/intelligence/movements`

### UI-023
- **Screen name:** Cycle Count Workbench
- **Purpose:** Present assigned blind cycle counts, collect physical count results, and track submission status.
- **Primary users:** Warehouse Staff, Inventory Controller
- **Related use cases:** UC-014
- **Related APIs:** API-108 `POST /api/v1/accuracy/cycle-counts`, API-109 `GET /api/v1/accuracy/cycle-counts`, API-110 `GET /api/v1/accuracy/cycle-counts/{cycleCountId}`, API-111 `POST /api/v1/accuracy/cycle-counts/{cycleCountId}/result`, API-168 `GET /api/v1/intelligence/accuracy/count-performance`

### UI-024
- **Screen name:** Physical Inventory Count Management
- **Purpose:** Initiate, monitor, and close wall-to-wall counts including freeze status, team progress, and certification.
- **Primary users:** Inventory Controller, Warehouse Manager, Warehouse Staff, Operations Director
- **Related use cases:** UC-015
- **Related APIs:** API-020 `GET /api/v1/locations/{locationCode}/freeze-status`, API-112 `POST /api/v1/accuracy/physical-counts`, API-113 `GET /api/v1/accuracy/physical-counts/{physicalCountId}`, API-114 `POST /api/v1/accuracy/physical-counts/{physicalCountId}/results`, API-115 `POST /api/v1/accuracy/physical-counts/{physicalCountId}/certify`, API-168 `GET /api/v1/intelligence/accuracy/count-performance`

### UI-025
- **Screen name:** Variance Investigation and Approval
- **Purpose:** Review count variances, capture investigation findings, and approve or reject quantity adjustments through proper independent controls.
- **Primary users:** Warehouse Manager, Inventory Controller, Operations Director
- **Related use cases:** UC-016
- **Related APIs:** API-116 `POST /api/v1/accuracy/adjustment-cases`, API-117 `GET /api/v1/accuracy/adjustment-cases/{caseId}`, API-118 `POST /api/v1/accuracy/adjustment-cases/{caseId}/investigate`, API-119 `POST /api/v1/accuracy/adjustment-cases/{caseId}/variances/{varianceId}/approve`, API-123 `GET /api/v1/accuracy/pending-approvals`

### UI-026
- **Screen name:** Stock Adjustment Management
- **Purpose:** Submit, approve-route, and finalize stock adjustments with mandatory reason codes and full traceability.
- **Primary users:** Warehouse Manager, Inventory Controller, Operations Director
- **Related use cases:** UC-017
- **Related APIs:** API-023 `GET /api/v1/governance/reason-codes`, API-029 `GET /api/v1/governance/approval-thresholds`, API-116 `POST /api/v1/accuracy/adjustment-cases`, API-117 `GET /api/v1/accuracy/adjustment-cases/{caseId}`, API-120 `POST /api/v1/accuracy/adjustment-cases/{caseId}/submit`, API-121 `POST /api/v1/accuracy/adjustment-cases/{caseId}/approve`, API-122 `POST /api/v1/accuracy/adjustment-cases/{caseId}/reject`

### UI-027
- **Screen name:** Write-Off Authorization
- **Purpose:** Review write-off requests, supporting evidence, and finance acknowledgment before permanent inventory removal.
- **Primary users:** Operations Director, Finance Manager, Inventory Controller, Warehouse Manager
- **Related use cases:** UC-018
- **Related APIs:** API-117 `GET /api/v1/accuracy/adjustment-cases/{caseId}`, API-120 `POST /api/v1/accuracy/adjustment-cases/{caseId}/submit`, API-121 `POST /api/v1/accuracy/adjustment-cases/{caseId}/approve`, API-122 `POST /api/v1/accuracy/adjustment-cases/{caseId}/reject`

### UI-028
- **Screen name:** Quarantine and Hold Register
- **Purpose:** Apply, review, and release quarantine or hold status while showing non-sellable quantities and reasons.
- **Primary users:** Warehouse Manager, Inventory Controller, Operations Director
- **Related use cases:** UC-019
- **Related APIs:** API-045 `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds`, API-046 `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds/{holdId}/release`, API-154 `GET /api/v1/intelligence/quarantine-register`

### UI-029
- **Screen name:** Shrinkage, Loss, and Obsolescence Analysis
- **Purpose:** Analyze loss trends, obsolete stock, and slow-moving inventory to support corrective action and working-capital decisions.
- **Primary users:** Inventory Controller, Finance Manager, Operations Director, Purchasing Manager
- **Related use cases:** UC-020
- **Related APIs:** API-167 `GET /api/v1/intelligence/accuracy/shrinkage`

---

## Order Fulfillment

### UI-030
- **Screen name:** Order Reservation Workbench
- **Purpose:** Confirm order readiness, reserve inventory, and release reservations when orders are changed or canceled.
- **Primary users:** Customer Service Representative, Sales Representative
- **Related use cases:** UC-021, UC-022, UC-023
- **Related APIs:** API-081 `POST /api/v1/fulfillment/orders`, API-084 `POST /api/v1/fulfillment/orders/{orderId}/availability`, API-085 `POST /api/v1/fulfillment/orders/{orderId}/confirm`, API-086 `POST /api/v1/fulfillment/orders/{orderId}/cancel`, API-043 `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations`, API-044 `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations/{reservationId}/release`, API-139 `GET /api/v1/campaigns/ring-fence/{locationCode}/{sku}`

### UI-031
- **Screen name:** Pick, Pack, and Ship Workbench
- **Purpose:** Show warehouse fulfillment queues, guide pick verification and packing, and confirm shipment handoff.
- **Primary users:** Warehouse Picker / Packer, Warehouse Manager
- **Related use cases:** UC-024
- **Related APIs:** API-088 `POST /api/v1/fulfillment/orders/{orderId}/pick-lists`, API-089 `GET /api/v1/fulfillment/orders/{orderId}/pick-lists/awaiting`, API-090 `POST /api/v1/fulfillment/orders/{orderId}/picks/{pickId}/verify`, API-091 `POST /api/v1/fulfillment/orders/{orderId}/pack`, API-092 `POST /api/v1/fulfillment/orders/{orderId}/shipments`, API-041 `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/lots`
- **API note:** API review item `C-01` identifies the missing location-level pick queue endpoint required for a complete warehouse workbench.

### UI-032
- **Screen name:** Partial Fulfillment and Backorder Management
- **Purpose:** Manage split shipments, customer acknowledgment, and backorder follow-up when full quantity is unavailable.
- **Primary users:** Customer Service Representative, Sales Representative, Purchasing Manager
- **Related use cases:** UC-025
- **Related APIs:** API-093 `POST /api/v1/fulfillment/orders/{orderId}/partial-fulfillment`, API-094 `POST /api/v1/fulfillment/orders/{orderId}/backorders`, API-095 `POST /api/v1/fulfillment/backorders/{backorderId}/fulfill`, API-164 `GET /api/v1/intelligence/fulfillment/backorders`

### UI-033
- **Screen name:** Fulfillment Exception Management
- **Purpose:** Resolve pick failures, quantity mismatches, damaged picks, or other outbound exceptions and route the order back into the correct flow.
- **Primary users:** Warehouse Manager, Customer Service Representative
- **Related use cases:** UC-026
- **Related APIs:** API-096 `POST /api/v1/fulfillment/orders/{orderId}/exceptions`, API-165 `GET /api/v1/intelligence/fulfillment/exceptions`, API-045 `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds`

### UI-034
- **Screen name:** Order Fulfillment Status
- **Purpose:** Provide current reservation, picking, packing, shipment, exception, and backorder status for order inquiries.
- **Primary users:** Customer Service Representative, Sales Representative, Sales Manager, Warehouse Manager
- **Related use cases:** UC-027
- **Related APIs:** API-082 `GET /api/v1/fulfillment/orders`, API-083 `GET /api/v1/fulfillment/orders/{orderId}`, API-097 `GET /api/v1/fulfillment/orders/{orderId}/status`, API-177 `GET /api/v1/integrations/sales/fulfillment-status`

### UI-035
- **Screen name:** Multi-Location Split Fulfillment Planner
- **Purpose:** Plan and monitor fulfillment of a single order from multiple locations when no single location can satisfy it alone.
- **Primary users:** Warehouse Manager, Customer Service Representative, Operations Director
- **Related use cases:** UC-048
- **Related APIs:** API-036 `GET /api/v1/inventory/availability/{sku}/network`, API-087 `POST /api/v1/fulfillment/orders/{orderId}/multi-location-plan`

---

## Replenishment and Transfers

### UI-036
- **Screen name:** Low-Stock Alert Review
- **Purpose:** Review active replenishment alerts, prioritize them, and acknowledge follow-up actions.
- **Primary users:** Purchasing Manager, Buyer, Inventory Controller, Operations Director
- **Related use cases:** UC-028
- **Related APIs:** API-037 `GET /api/v1/inventory/stock-status/{locationCode}/{sku}`, API-039 `GET /api/v1/inventory/stock-policies/{locationCode}/{sku}`, API-158 `GET /api/v1/intelligence/alerts`, API-159 `POST /api/v1/intelligence/alerts/{alertId}/acknowledge`, API-160 `GET /api/v1/intelligence/replenishment/recommendations`

### UI-037
- **Screen name:** Replenishment Planning
- **Purpose:** Turn alerts and recommendations into replenishment decisions, including transfer-before-buy review and requisition creation.
- **Primary users:** Buyer, Purchasing Manager
- **Related use cases:** UC-029
- **Related APIs:** API-054 `POST /api/v1/procurement/requisitions`, API-055 `GET /api/v1/procurement/requisitions/{requisitionId}`, API-056 `POST /api/v1/procurement/requisitions/{requisitionId}/approve`, API-057 `POST /api/v1/procurement/requisitions/{requisitionId}/reject`, API-058 `POST /api/v1/procurement/requisitions/{requisitionId}/convert-to-po`, API-160 `GET /api/v1/intelligence/replenishment/recommendations`, API-166 `GET /api/v1/intelligence/network/imbalance`
- **API note:** Full list/queue browsing depends on the missing requisition list endpoint noted in API review item `C-03`.

### UI-038
- **Screen name:** Transfer Request
- **Purpose:** Submit inter-location transfer requests with source, destination, product, quantity, and business justification.
- **Primary users:** Regional / Store Manager, Warehouse Manager
- **Related use cases:** UC-031
- **Related APIs:** API-098 `POST /api/v1/transfers`, API-099 `GET /api/v1/transfers`, API-100 `GET /api/v1/transfers/{transferId}`, API-042 `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity`

### UI-039
- **Screen name:** Transfer Approval Queue
- **Purpose:** Allow management to approve or reject transfer requests based on source capacity and network impact.
- **Primary users:** Operations Director
- **Related use cases:** UC-032
- **Related APIs:** API-101 `POST /api/v1/transfers/{transferId}/approve`, API-102 `POST /api/v1/transfers/{transferId}/reject`, API-106 `GET /api/v1/transfers/pending-approvals`, API-042 `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity`

### UI-040
- **Screen name:** Transfer Execution and In-Transit Tracking
- **Purpose:** Dispatch approved transfers, receive them at destination, and monitor in-transit stock movement.
- **Primary users:** Warehouse Staff, Warehouse Manager, Regional / Store Manager
- **Related use cases:** UC-033
- **Related APIs:** API-099 `GET /api/v1/transfers`, API-100 `GET /api/v1/transfers/{transferId}`, API-103 `POST /api/v1/transfers/{transferId}/dispatch`, API-104 `POST /api/v1/transfers/{transferId}/receive`, API-105 `POST /api/v1/transfers/{transferId}/cancel`, API-107 `GET /api/v1/transfers/in-transit`

### UI-041
- **Screen name:** Network Rebalancing Analysis
- **Purpose:** Analyze stock imbalance across locations and generate recommended redistribution actions.
- **Primary users:** Operations Director, Inventory Controller, Purchasing Manager
- **Related use cases:** UC-034
- **Related APIs:** API-036 `GET /api/v1/inventory/availability/{sku}/network`, API-160 `GET /api/v1/intelligence/replenishment/recommendations`, API-166 `GET /api/v1/intelligence/network/imbalance`

---

## Returns

### UI-042
- **Screen name:** Return Authorization Management
- **Purpose:** Look up original orders, validate return eligibility, and issue return authorizations.
- **Primary users:** Customer Service Representative
- **Related use cases:** UC-035
- **Related APIs:** API-124 `POST /api/v1/returns/authorizations`, API-125 `GET /api/v1/returns/authorizations`, API-126 `GET /api/v1/returns/authorizations/{returnAuthorizationId}`, API-127 `POST /api/v1/returns/authorizations/{returnAuthorizationId}/cancel`

### UI-043
- **Screen name:** Return Inspection and Disposition
- **Purpose:** Receive authorized returns, inspect their condition, and route them to restock, quarantine, or write-off.
- **Primary users:** Receiving Clerk, Warehouse Manager, Inventory Controller, Finance Manager
- **Related use cases:** UC-036
- **Related APIs:** API-128 `POST /api/v1/returns/{returnId}/receive`, API-129 `POST /api/v1/returns/{returnId}/inspect`, API-130 `POST /api/v1/returns/{returnId}/disposition`, API-131 `GET /api/v1/returns/pending-receipts`, API-076 `POST /api/v1/inbound/return-receipts`
- **API note:** API review item `C-04` recommends API-128 as the canonical receipt path for this screen.

---

## Reporting, Finance, Audit, and Administration

### UI-044
- **Screen name:** Operational Reports and Analytics
- **Purpose:** Access dashboard and operational reports for stock movement, stockout, overstock, accuracy, location performance, and related management analysis.
- **Primary users:** Operations Director, Chief Operating Officer, Inventory Controller, Warehouse Manager, Purchasing Manager, Sales Manager
- **Related use cases:** UC-037
- **Related APIs:** API-150 `GET /api/v1/intelligence/dashboard`, API-151 `GET /api/v1/intelligence/stock-status/summary`, API-152 `GET /api/v1/intelligence/stock-status/board`, API-154 `GET /api/v1/intelligence/quarantine-register`, API-155 `GET /api/v1/intelligence/movements`, API-167 `GET /api/v1/intelligence/accuracy/shrinkage`, API-168 `GET /api/v1/intelligence/accuracy/count-performance`

### UI-045
- **Screen name:** Inventory Valuation Reconciliation
- **Purpose:** Compare operational valuation with finance records, investigate variances, and finalize reconciliation status.
- **Primary users:** Finance Manager, Chief Financial Officer, Inventory Controller, Internal Auditor
- **Related use cases:** UC-039
- **Related APIs:** API-077 `POST /api/v1/inbound/supplier-invoices`, API-078 `GET /api/v1/inbound/supplier-invoices/{invoiceId}`, API-079 `POST /api/v1/inbound/supplier-invoices/{invoiceId}/three-way-match`, API-080 `POST /api/v1/inbound/supplier-invoices/{invoiceId}/authorize-payment`, API-047 `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/consignment-ownership`, API-171 `GET /api/v1/intelligence/valuation/snapshots`, API-172 `GET /api/v1/intelligence/valuation/reconciliation`

### UI-046
- **Screen name:** Promotional Stock Readiness
- **Purpose:** Allocate and ring-fence promotional stock, assess readiness, and confirm launch stock coverage.
- **Primary users:** Marketing Manager, Purchasing Manager, Warehouse Manager, Sales Manager, Operations Director
- **Related use cases:** UC-040
- **Related APIs:** API-132 `POST /api/v1/campaigns/allocations`, API-133 `GET /api/v1/campaigns/allocations`, API-134 `GET /api/v1/campaigns/allocations/{allocationId}`, API-135 `PATCH /api/v1/campaigns/allocations/{allocationId}`, API-136 `POST /api/v1/campaigns/allocations/{allocationId}/readiness`, API-137 `POST /api/v1/campaigns/allocations/{allocationId}/release`, API-138 `POST /api/v1/campaigns/allocations/{allocationId}/override`, API-139 `GET /api/v1/campaigns/ring-fence/{locationCode}/{sku}`, API-169 `GET /api/v1/intelligence/campaigns/readiness`, API-178 `POST /api/v1/integrations/marketing/campaign-plans`

### UI-047
- **Screen name:** Audit and Control Review Workspace
- **Purpose:** Let auditors define review scope, inspect transaction and approval populations, test control compliance, and document findings.
- **Primary users:** Internal Auditor, External Auditor, Finance Manager
- **Related use cases:** UC-041
- **Related APIs:** API-156 `GET /api/v1/intelligence/audit-trail`, API-157 `GET /api/v1/intelligence/audit-trail/export`

### UI-048
- **Screen name:** Audit Trail Query
- **Purpose:** Search immutable audit records by entity, date, user, and action and inspect before/after values.
- **Primary users:** Internal Auditor, External Auditor, Finance Manager, Operations Director
- **Related use cases:** UC-043
- **Related APIs:** API-156 `GET /api/v1/intelligence/audit-trail`, API-157 `GET /api/v1/intelligence/audit-trail/export`

### UI-049
- **Screen name:** User Account Management
- **Purpose:** Provision, modify, suspend, deactivate, and review user accounts and role assignments.
- **Primary users:** System Administrator
- **Related use cases:** UC-044
- **Related APIs:** API-140 `POST /api/v1/users`, API-141 `GET /api/v1/users`, API-142 `GET /api/v1/users/{userId}`, API-143 `POST /api/v1/users/{userId}/roles`, API-144 `DELETE /api/v1/users/{userId}/roles/{roleAssignmentId}`, API-145 `POST /api/v1/users/{userId}/suspend`, API-146 `POST /api/v1/users/{userId}/deactivate`, API-147 `POST /api/v1/users/sync`

### UI-050
- **Screen name:** Role and Access Control Administration
- **Purpose:** Configure role permissions, location scope rules, and access policy enforcement behavior.
- **Primary users:** System Administrator, Internal Auditor
- **Related use cases:** UC-045
- **Related APIs:** API-031 `POST /api/v1/governance/segregation-of-duties/evaluate`, API-148 `POST /api/v1/authorization/actions/evaluate`, API-149 `POST /api/v1/authorization/location-scope/validate`, API-173 `GET /api/v1/auth/session`

---

## Summary

- **Total screens identified:** 50
- **Coverage basis:** BRD scope and functional requirements, 48 use cases, and the REST API catalog
- **Design status:** Screen inventory only; no layout, navigation, or wireframes defined in this document

