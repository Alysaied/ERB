# System Permissions: Inventory Management System

**Document Owner:** Security Engineer  
**Purpose:** Define all business-action permissions required by the Inventory Management System based on functional requirements  
**Audience:** Security engineers, solution architects, product owners, and access control designers  
**Scope:** Permission catalog only — role-to-permission mappings are addressed in a subsequent access control matrix  
**Based On:** Functional Requirements (FR-001–FR-090) and Feature Catalog (F-01–F-30)

---

## Document Conventions

| Convention | Meaning |
|------------|---------|
| **PERM-xxx** | System permission identifier |
| **F-xx** | Related feature from Feature Catalog |
| **FR-xxx** | Supporting functional requirement(s) |

Permissions are named using business verbs (Create, Approve, View, Transfer, etc.) and describe enforceable actions the system must authorize before execution. Permissions are independent of user roles; roles are mapped to permissions in a later design step.

### Permission Categories

| Category | Prefix Range | Description |
|----------|--------------|-------------|
| Master Data & Governance | PERM-001 – PERM-016 | Product, location, policy, and reference data |
| Inventory Visibility | PERM-017 – PERM-023 | Read-only stock and movement inquiry |
| Inbound & Purchasing | PERM-024 – PERM-036 | Purchase orders, receiving, and inbound supply |
| Inventory Control | PERM-037 – PERM-050 | Counting, adjustments, write-offs, and quarantine |
| Order Fulfillment | PERM-051 – PERM-063 | Availability, reservation, picking, and shipping |
| Replenishment | PERM-064 – PERM-070 | Alerts, requisitions, and safety stock overrides |
| Network Transfers | PERM-071 – PERM-076 | Inter-location stock movement and rebalancing |
| Returns | PERM-077 – PERM-082 | Customer return lifecycle |
| Reporting & Analytics | PERM-083 – PERM-091 | Dashboards, reports, and exports |
| Commercial Readiness | PERM-092 – PERM-093 | Campaign and launch stock planning |
| Financial Alignment | PERM-094 | Operational-to-financial reconciliation |
| Administration & Audit | PERM-095 – PERM-100 | User management, activity logs, and audit evidence |

---

## Permission Index

| ID | Permission Name | Category | Feature |
|----|-----------------|----------|---------|
| PERM-001 | Create Product | Master Data | F-01 |
| PERM-002 | Update Product | Master Data | F-01 |
| PERM-003 | Manage Product Status | Master Data | F-01 |
| PERM-004 | Lookup Product | Master Data | F-01 |
| PERM-005 | Resolve Duplicate Product | Master Data | F-01 |
| PERM-006 | Create Location | Master Data | F-02 |
| PERM-007 | Update Location | Master Data | F-02 |
| PERM-008 | Manage Location Hierarchy | Master Data | F-02 |
| PERM-009 | Plan Location Closure and Disposition | Master Data | F-02 |
| PERM-010 | Establish Opening Stock Balance | Master Data | F-02 |
| PERM-011 | Define Stock Thresholds | Master Data | F-03 |
| PERM-012 | Classify Products (ABC) | Master Data | F-03 |
| PERM-013 | Manage Inventory Governance Policies | Master Data | F-03 |
| PERM-014 | Manage Reason Codes | Master Data | F-17 |
| PERM-015 | Import Initial Master Data | Master Data | F-30 |
| PERM-016 | Approve Initial Data Import | Master Data | F-30 |
| PERM-017 | View On-Hand Inventory | Visibility | F-04 |
| PERM-018 | View Available-to-Promise | Visibility | F-04 |
| PERM-019 | View Reserved Stock | Visibility | F-04 |
| PERM-020 | View Stock Status Indicators | Visibility | F-04 |
| PERM-021 | Search and Filter Inventory | Visibility | F-04 |
| PERM-022 | View Network and Inbound Availability | Visibility | F-04 |
| PERM-023 | View Inventory Movement History | Visibility | F-05 |
| PERM-024 | Create Purchase Order | Inbound | F-07 |
| PERM-025 | Amend Purchase Order | Inbound | F-07 |
| PERM-026 | Cancel Purchase Order | Inbound | F-07 |
| PERM-027 | View Expected Inbound Deliveries | Inbound | F-07 |
| PERM-028 | Receive Goods | Inbound | F-05 |
| PERM-029 | Document Receipt Discrepancy | Inbound | F-05 |
| PERM-030 | Resolve Receipt Discrepancy | Inbound | F-05 |
| PERM-031 | Approve Ad-Hoc Receipt | Inbound | F-05 |
| PERM-032 | Approve Receipt Beyond Tolerance | Inbound | F-05 |
| PERM-033 | Confirm Put-Away | Inbound | F-06 |
| PERM-034 | Receive Return Inbound | Inbound | F-05, F-21 |
| PERM-035 | View Inbound Supply Status | Inbound | F-07 |
| PERM-036 | View Supplier Delivery Performance | Inbound | F-07 |
| PERM-037 | Schedule Cycle Count | Control | F-14 |
| PERM-038 | Perform Cycle Count | Control | F-14 |
| PERM-039 | Initiate Full Physical Count | Control | F-15 |
| PERM-040 | View Count Variances | Control | F-16 |
| PERM-041 | Investigate Count Variance | Control | F-16 |
| PERM-042 | Approve Count Adjustment | Control | F-16 |
| PERM-043 | Request Stock Adjustment | Control | F-17 |
| PERM-044 | Approve Stock Adjustment | Control | F-17 |
| PERM-045 | Request Inventory Write-Off | Control | F-17 |
| PERM-046 | Approve Inventory Write-Off | Control | F-17 |
| PERM-047 | Place Stock on Quarantine or Hold | Control | F-18 |
| PERM-048 | Release Stock from Quarantine or Hold | Control | F-18 |
| PERM-049 | View Shrinkage and Loss Analysis | Control | F-19 |
| PERM-050 | Review Obsolete and Slow-Moving Stock | Control | F-19 |
| PERM-051 | Confirm Order Availability | Fulfillment | F-10 |
| PERM-052 | Reserve Inventory | Fulfillment | F-10 |
| PERM-053 | Release Inventory Reservation | Fulfillment | F-10 |
| PERM-054 | Release Order to Fulfillment | Fulfillment | F-11 |
| PERM-055 | Execute Pick and Pack | Fulfillment | F-11 |
| PERM-056 | Confirm Shipment | Fulfillment | F-11 |
| PERM-057 | Process Partial Fulfillment | Fulfillment | F-12 |
| PERM-058 | Manage Backorder Queue | Fulfillment | F-12 |
| PERM-059 | Report Fulfillment Exception | Fulfillment | F-13 |
| PERM-060 | Resolve Fulfillment Exception | Fulfillment | F-13 |
| PERM-061 | Allocate Multi-Location Fulfillment | Fulfillment | F-10 |
| PERM-062 | View Order Fulfillment Status | Fulfillment | F-11 |
| PERM-063 | Approve Product Substitution | Fulfillment | F-13 |
| PERM-064 | View Low-Stock Alerts | Replenishment | F-20 |
| PERM-065 | Acknowledge or Dismiss Stock Alert | Replenishment | F-20 |
| PERM-066 | View Replenishment Suggestions | Replenishment | F-20 |
| PERM-067 | Create Purchase Requisition | Replenishment | F-20 |
| PERM-068 | Approve Purchase Requisition | Replenishment | F-20 |
| PERM-069 | Approve Purchase Order | Replenishment | F-07 |
| PERM-070 | Override Safety Stock Protection | Replenishment | F-03 |
| PERM-071 | Request Stock Transfer | Transfers | F-08 |
| PERM-072 | Approve Stock Transfer | Transfers | F-08 |
| PERM-073 | Dispatch Stock Transfer | Transfers | F-08 |
| PERM-074 | Receive Stock Transfer | Transfers | F-08 |
| PERM-075 | View In-Transit Inventory | Transfers | F-08 |
| PERM-076 | View Network Rebalancing Recommendations | Transfers | F-09 |
| PERM-077 | Authorize Customer Return | Returns | F-21 |
| PERM-078 | Receive Returned Goods | Returns | F-21 |
| PERM-079 | Inspect Returned Goods | Returns | F-21 |
| PERM-080 | Restock Returned Inventory | Returns | F-21 |
| PERM-081 | Write Off Returned Inventory | Returns | F-21 |
| PERM-082 | View Return Processing Status | Returns | F-21 |
| PERM-083 | View Inventory Dashboard | Reporting | F-22 |
| PERM-084 | View Stock Movement Reports | Reporting | F-22 |
| PERM-085 | View Stockout and Overstock Reports | Reporting | F-22 |
| PERM-086 | View Inventory Accuracy Reports | Reporting | F-14, F-22 |
| PERM-087 | View Location Performance Reports | Reporting | F-22 |
| PERM-088 | View Inventory Performance KPIs | Reporting | F-23 |
| PERM-089 | View Replenishment Reports | Reporting | F-20, F-22 |
| PERM-090 | View Inventory Valuation Reports | Reporting | F-24 |
| PERM-091 | Export Reports | Reporting | F-22 |
| PERM-092 | Review Campaign Stock Readiness | Commercial | F-25 |
| PERM-093 | Ring-Fence Promotional Stock | Commercial | F-25 |
| PERM-094 | Perform Financial Inventory Reconciliation | Financial | F-24 |
| PERM-095 | Manage User Accounts | Administration | F-27 |
| PERM-096 | Assign User Roles and Location Scope | Administration | F-27 |
| PERM-097 | View User Activity Log | Administration | F-28 |
| PERM-098 | View Inventory Audit Trail | Audit | F-29 |
| PERM-099 | Query Audit Evidence | Audit | F-29 |
| PERM-100 | View Control Policy Breach Records | Audit | F-29 |

**Total: 100 permissions**

---

## Master Data & Governance

---

### PERM-001: Create Product

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-001 |
| **Permission Name** | Create Product |
| **Description** | Create new product master records including SKU, name, description, unit of measure, category, and inventory tracking attributes. |
| **Business Reason** | Establishes a single, consistent product identity across all locations and departments; prevents duplicate catalog entries that cause ordering and fulfillment errors. |
| **Related Feature** | F-01: Product Catalog Management |
| **Related Functional Requirements** | FR-001, FR-004 |

---

### PERM-002: Update Product

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-002 |
| **Permission Name** | Update Product |
| **Description** | Modify existing product master record attributes such as name, description, category, unit of measure, and tracking parameters. |
| **Business Reason** | Keeps product reference data current as supplier specifications, merchandising, and operational needs change. |
| **Related Feature** | F-01: Product Catalog Management |
| **Related Functional Requirements** | FR-001, FR-004 |

---

### PERM-003: Manage Product Status

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-003 |
| **Permission Name** | Manage Product Status |
| **Description** | Change product lifecycle status across active, inactive, and discontinued states, controlling whether products may be received, ordered, reserved, or fulfilled. |
| **Business Reason** | Prevents obsolete or withdrawn products from re-entering the supply chain and supports clearance planning for discontinued items. |
| **Related Feature** | F-01: Product Catalog Management |
| **Related Functional Requirements** | FR-002 |

---

### PERM-004: Lookup Product

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-004 |
| **Permission Name** | Lookup Product |
| **Description** | Search and identify products by SKU, barcode, or other assigned identifier during receiving, counting, picking, and inquiry activities. |
| **Business Reason** | Reduces identification errors on the warehouse floor and speeds operational transactions without manual cross-referencing. |
| **Related Feature** | F-01: Product Catalog Management |
| **Related Functional Requirements** | FR-003 |

---

### PERM-005: Resolve Duplicate Product

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-005 |
| **Permission Name** | Resolve Duplicate Product |
| **Description** | Review potential duplicate product records and correct or merge them without creating parallel product identities. |
| **Business Reason** | Prevents fragmented stock records for the same physical product, which causes inaccurate availability and reconciliation effort. |
| **Related Feature** | F-01: Product Catalog Management |
| **Related Functional Requirements** | FR-004 |

---

### PERM-006: Create Location

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-006 |
| **Permission Name** | Create Location |
| **Description** | Define new inventory-holding locations including warehouses, stores, and distribution points with name, type, and operational status. |
| **Business Reason** | Establishes the organizational structure required to assign, track, and report stock at the correct network level. |
| **Related Feature** | F-02: Location & Network Setup |
| **Related Functional Requirements** | FR-005 |

---

### PERM-007: Update Location

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-007 |
| **Permission Name** | Update Location |
| **Description** | Modify location attributes, operational status, and accountable manager assignment; deactivate locations when no longer operational. |
| **Business Reason** | Maintains accurate location network data as sites open, change scope, or cease operations. |
| **Related Feature** | F-02: Location & Network Setup |
| **Related Functional Requirements** | FR-005 |

---

### PERM-008: Manage Location Hierarchy

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-008 |
| **Permission Name** | Manage Location Hierarchy |
| **Description** | Define and maintain parent-child and regional relationships between inventory locations within the distribution network. |
| **Business Reason** | Enables network-level reporting, accountability assignment, and structured stock redistribution decisions. |
| **Related Feature** | F-02: Location & Network Setup |
| **Related Functional Requirements** | FR-006 |

---

### PERM-009: Plan Location Closure and Disposition

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-009 |
| **Permission Name** | Plan Location Closure and Disposition |
| **Description** | Plan and execute stock disposition when a location is closed or consolidated, including transfer out, sell-through, or write-off of remaining inventory. |
| **Business Reason** | Prevents stranded inventory and record orphans when locations exit the network; protects asset value during network changes. |
| **Related Feature** | F-02: Location & Network Setup |
| **Related Functional Requirements** | FR-007 |

---

### PERM-010: Establish Opening Stock Balance

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-010 |
| **Permission Name** | Establish Opening Stock Balance |
| **Description** | Enter and confirm verified opening stock balances from physical count results before a new location is activated for transactions. |
| **Business Reason** | Prevents go-live with embedded inventory errors that undermine trust and cause cascading fulfillment failures. |
| **Related Feature** | F-02: Location & Network Setup |
| **Related Functional Requirements** | FR-010 |

---

### PERM-011: Define Stock Thresholds

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-011 |
| **Permission Name** | Define Stock Thresholds |
| **Description** | Define and maintain reorder levels, minimum stock thresholds, and safety stock parameters per product and location. |
| **Business Reason** | Enables proactive low-stock identification and aligns purchasing with operational needs, reducing reactive stockouts. |
| **Related Feature** | F-03: Stock Policy & Product Classification |
| **Related Functional Requirements** | FR-008 |

---

### PERM-012: Classify Products (ABC)

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-012 |
| **Permission Name** | Classify Products (ABC) |
| **Description** | Assign and maintain ABC product classification based on revenue, velocity, and criticality for count scheduling and alert prioritization. |
| **Business Reason** | Directs operational effort toward high-impact items, improving fill rate on priority products while optimizing counting effort. |
| **Related Feature** | F-03: Stock Policy & Product Classification |
| **Related Functional Requirements** | FR-009 |

---

### PERM-013: Manage Inventory Governance Policies

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-013 |
| **Permission Name** | Manage Inventory Governance Policies |
| **Description** | Create and maintain inventory management policy parameters including approval thresholds, count tolerances, reservation timing, and partial shipment rules. |
| **Business Reason** | Establishes formal accountability and consistent decision-making across locations; addresses lack of formal inventory governance. |
| **Related Feature** | F-03: Stock Policy & Product Classification |
| **Related Functional Requirements** | FR-012 |

---

### PERM-014: Manage Reason Codes

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-014 |
| **Permission Name** | Manage Reason Codes |
| **Description** | Maintain the controlled list of reason codes for inventory adjustments, write-offs, receipt discrepancies, and operational exceptions. |
| **Business Reason** | Enables shrinkage analysis, trend identification, and audit substantiation; uncategorized adjustments are analytically useless. |
| **Related Feature** | F-17: Stock Adjustments & Write-Offs |
| **Related Functional Requirements** | FR-011 |

---

### PERM-015: Import Initial Master Data

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-015 |
| **Permission Name** | Import Initial Master Data |
| **Description** | Submit controlled bulk import of product master data and opening stock balances for go-live preparation. |
| **Business Reason** | Accelerates deployment at primary locations without manual entry of entire product catalogs. |
| **Related Feature** | F-30: System Go-Live & Initial Data Setup |
| **Related Functional Requirements** | FR-090 |

---

### PERM-016: Approve Initial Data Import

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-016 |
| **Permission Name** | Approve Initial Data Import |
| **Description** | Review, validate, and authorize activation of imported product and opening stock data before it becomes operational. |
| **Business Reason** | Prevents unverified bulk data from entering production inventory records; maintains segregation between data submission and activation. |
| **Related Feature** | F-30: System Go-Live & Initial Data Setup |
| **Related Functional Requirements** | FR-090 |

---

## Inventory Visibility

---

### PERM-017: View On-Hand Inventory

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-017 |
| **Permission Name** | View On-Hand Inventory |
| **Description** | View real-time on-hand inventory quantity for products at authorized locations reflecting all recorded movements. |
| **Business Reason** | Delivers the foundational single source of truth enabling any authorized user to answer what stock exists and where. |
| **Related Feature** | F-04: Inventory Visibility & Search |
| **Related Functional Requirements** | FR-023 |

---

### PERM-018: View Available-to-Promise

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-018 |
| **Permission Name** | View Available-to-Promise |
| **Description** | View available-to-promise quantity representing stock not reserved, committed, quarantined, or otherwise unavailable for new customer commitments. |
| **Business Reason** | Prevents overselling and overpromising; primary input for sales availability confirmation. |
| **Related Feature** | F-04: Inventory Visibility & Search |
| **Related Functional Requirements** | FR-024 |

---

### PERM-019: View Reserved Stock

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-019 |
| **Permission Name** | View Reserved Stock |
| **Description** | View inventory quantities reserved or committed to confirmed orders, linked to originating order references. |
| **Business Reason** | Explains why available stock differs from on-hand; reduces disputes between sales and warehouse teams. |
| **Related Feature** | F-04: Inventory Visibility & Search |
| **Related Functional Requirements** | FR-025 |

---

### PERM-020: View Stock Status Indicators

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-020 |
| **Permission Name** | View Stock Status Indicators |
| **Description** | View derived stock status indicators (in stock, low stock, out of stock) based on thresholds and current availability. |
| **Business Reason** | Enables rapid identification of problem items without manual threshold comparison during daily operational reviews. |
| **Related Feature** | F-04: Inventory Visibility & Search |
| **Related Functional Requirements** | FR-026 |

---

### PERM-021: Search and Filter Inventory

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-021 |
| **Permission Name** | Search and Filter Inventory |
| **Description** | Search and filter inventory views by product, location, category, status, ABC class, and other defined attributes. |
| **Business Reason** | Reduces time to find relevant stock information and decreases warehouse interruption from ad-hoc stock inquiries. |
| **Related Feature** | F-04: Inventory Visibility & Search |
| **Related Functional Requirements** | FR-027 |

---

### PERM-022: View Network and Inbound Availability

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-022 |
| **Permission Name** | View Network and Inbound Availability |
| **Description** | View expected inbound stock from open purchase orders and network-wide availability aggregated across all locations for a product. |
| **Business Reason** | Enables network-level replenishment decisions and gives sales realistic dates for out-of-stock recovery. |
| **Related Feature** | F-04: Inventory Visibility & Search |
| **Related Functional Requirements** | FR-028 |

---

### PERM-023: View Inventory Movement History

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-023 |
| **Permission Name** | View Inventory Movement History |
| **Description** | View complete transaction history of inventory movements including receipts, transfers, adjustments, fulfillments, and returns with user and timestamp attribution. |
| **Business Reason** | Supports accountability, root-cause investigation, and audit substantiation for all inventory changes. |
| **Related Feature** | F-05: Goods Receiving & Verification |
| **Related Functional Requirements** | FR-029 |

---

## Inbound & Purchasing

---

### PERM-024: Create Purchase Order

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-024 |
| **Permission Name** | Create Purchase Order |
| **Description** | Create purchase orders capturing product, quantity, expected delivery, supplier reference, and receiving location. |
| **Business Reason** | Establishes committed inbound expected stock for receiving verification and availability projections. |
| **Related Feature** | F-07: Purchase Order & Inbound Supply Management |
| **Related Functional Requirements** | FR-013 |

---

### PERM-025: Amend Purchase Order

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-025 |
| **Permission Name** | Amend Purchase Order |
| **Description** | Modify open purchase order lines including quantity, delivery date, or product before receipt is complete. |
| **Business Reason** | Keeps inbound projections aligned with actual supplier commitments when demand or delivery schedules change. |
| **Related Feature** | F-07: Purchase Order & Inbound Supply Management |
| **Related Functional Requirements** | FR-021 |

---

### PERM-026: Cancel Purchase Order

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-026 |
| **Permission Name** | Cancel Purchase Order |
| **Description** | Cancel open purchase orders or individual lines before receipt is complete, updating expected inbound quantities. |
| **Business Reason** | Prevents receiving against obsolete orders and eliminates duplicate or unnecessary supplier commitments. |
| **Related Feature** | F-07: Purchase Order & Inbound Supply Management |
| **Related Functional Requirements** | FR-021 |

---

### PERM-027: View Expected Inbound Deliveries

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-027 |
| **Permission Name** | View Expected Inbound Deliveries |
| **Description** | View scheduled inbound deliveries by location and date including expected products and quantities. |
| **Business Reason** | Enables receiving dock preparation and gives operations realistic inbound availability dates. |
| **Related Feature** | F-07: Purchase Order & Inbound Supply Management |
| **Related Functional Requirements** | FR-014 |

---

### PERM-028: Receive Goods

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-028 |
| **Permission Name** | Receive Goods |
| **Description** | Record goods receipt by verifying inbound shipment quantity, product identity, and condition against delivery documentation and purchase order reference. |
| **Business Reason** | Ensures on-hand balances reflect physical reality from point of entry; prevents phantom inventory. |
| **Related Feature** | F-05: Goods Receiving & Verification |
| **Related Functional Requirements** | FR-015, FR-017 |

---

### PERM-029: Document Receipt Discrepancy

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-029 |
| **Permission Name** | Document Receipt Discrepancy |
| **Description** | Record receipt discrepancies including short shipment, over-shipment, wrong item, and damage with quantity variance and supporting notes. |
| **Business Reason** | Protects supplier accountability and prevents inaccurate inventory records from unresolved receipt variances. |
| **Related Feature** | F-05: Goods Receiving & Verification |
| **Related Functional Requirements** | FR-016 |

---

### PERM-030: Resolve Receipt Discrepancy

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-030 |
| **Permission Name** | Resolve Receipt Discrepancy |
| **Description** | Review, adjudicate, and close receipt discrepancy records including supplier credit, replacement, or acceptance decisions. |
| **Business Reason** | Completes the discrepancy lifecycle so inventory and financial records reflect agreed resolution outcomes. |
| **Related Feature** | F-05: Goods Receiving & Verification |
| **Related Functional Requirements** | FR-016, FR-022 |

---

### PERM-031: Approve Ad-Hoc Receipt

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-031 |
| **Permission Name** | Approve Ad-Hoc Receipt |
| **Description** | Authorize receipt of supplier shipments without a standard purchase order reference via controlled exception path with documented reason. |
| **Business Reason** | Maintains procurement control while allowing emergency receiving when operational necessity requires it. |
| **Related Feature** | F-05: Goods Receiving & Verification |
| **Related Functional Requirements** | FR-017 |

---

### PERM-032: Approve Receipt Beyond Tolerance

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-032 |
| **Permission Name** | Approve Receipt Beyond Tolerance |
| **Description** | Approve receipt of quantities exceeding defined tolerance limits compared to purchase order expected quantities. |
| **Business Reason** | Balances operational flexibility with control; prevents silent acceptance of material variances affecting payment and inventory accuracy. |
| **Related Feature** | F-05: Goods Receiving & Verification |
| **Related Functional Requirements** | FR-020 |

---

### PERM-033: Confirm Put-Away

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-033 |
| **Permission Name** | Confirm Put-Away |
| **Description** | Confirm that received stock has been moved to storage location and transition quantity from received to available sellable status. |
| **Business Reason** | Prevents promising stock that pickers cannot locate; reflects operational reality in available-to-promise. |
| **Related Feature** | F-06: Put-Away Management |
| **Related Functional Requirements** | FR-018 |

---

### PERM-034: Receive Return Inbound

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-034 |
| **Permission Name** | Receive Return Inbound |
| **Description** | Record inbound receipt of customer returns and other non-purchase-order inbound movements with appropriate reference linkage. |
| **Business Reason** | Captures all inventory increases in one system, maintaining complete movement history and accurate balances. |
| **Related Feature** | F-05: Goods Receiving & Verification; F-21: Returns Management |
| **Related Functional Requirements** | FR-019, FR-065 |

---

### PERM-035: View Inbound Supply Status

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-035 |
| **Permission Name** | View Inbound Supply Status |
| **Description** | View open purchase orders, expected delivery dates, received versus outstanding quantities, and delay notations. |
| **Business Reason** | Enables operations, sales, and customer service to communicate realistic restock dates and reduce unnecessary escalations. |
| **Related Feature** | F-07: Purchase Order & Inbound Supply Management |
| **Related Functional Requirements** | FR-055 |

---

### PERM-036: View Supplier Delivery Performance

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-036 |
| **Permission Name** | View Supplier Delivery Performance |
| **Description** | View supplier delivery timeliness, quantity accuracy, and discrepancy frequency metrics derived from receipt records. |
| **Business Reason** | Supports informed replenishment decisions and supplier relationship management based on actual performance data. |
| **Related Feature** | F-07: Purchase Order & Inbound Supply Management |
| **Related Functional Requirements** | FR-022 |

---

## Inventory Control

---

### PERM-037: Schedule Cycle Count

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-037 |
| **Permission Name** | Schedule Cycle Count |
| **Description** | Create and assign cycle count tasks by location, product category, or ABC class according to the count calendar. |
| **Business Reason** | Sustains inventory accuracy through rotating verification without disruptive full-wall counts. |
| **Related Feature** | F-14: Cycle Counting |
| **Related Functional Requirements** | FR-030 |

---

### PERM-038: Perform Cycle Count

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-038 |
| **Permission Name** | Perform Cycle Count |
| **Description** | Execute assigned cycle count tasks using blind count procedures, recording physical quantities without viewing expected system quantities during count. |
| **Business Reason** | Produces unbiased accuracy measurement; counts that validate bad data instead of detecting errors destroy metric credibility. |
| **Related Feature** | F-14: Cycle Counting |
| **Related Functional Requirements** | FR-031 |

---

### PERM-039: Initiate Full Physical Count

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-039 |
| **Permission Name** | Initiate Full Physical Count |
| **Description** | Initiate a full physical inventory count at a location including movement freeze enforcement and comprehensive variance reporting. |
| **Business Reason** | Establishes verified baseline for financial substantiation and corrects accumulated discrepancies. |
| **Related Feature** | F-15: Full Physical Inventory Count |
| **Related Functional Requirements** | FR-032 |

---

### PERM-040: View Count Variances

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-040 |
| **Permission Name** | View Count Variances |
| **Description** | View variances between physical count results and recorded system quantities, including tolerance classification and variance summaries. |
| **Business Reason** | Focuses investigation effort on material discrepancies and supports count program oversight. |
| **Related Feature** | F-16: Count Variance Investigation & Approval |
| **Related Functional Requirements** | FR-033 |

---

### PERM-041: Investigate Count Variance

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-041 |
| **Permission Name** | Investigate Count Variance |
| **Description** | Document root-cause investigation for material count variances including transaction history review and investigation notes. |
| **Business Reason** | Ensures adjustments are substantiated before application; supports loss prevention and process improvement. |
| **Related Feature** | F-16: Count Variance Investigation & Approval |
| **Related Functional Requirements** | FR-034 |

---

### PERM-042: Approve Count Adjustment

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-042 |
| **Permission Name** | Approve Count Adjustment |
| **Description** | Independently approve or reject count variance adjustments before inventory balances are updated, separate from the counter role. |
| **Business Reason** | Maintains segregation of duties between counter and approver; prevents unauthorized inventory changes. |
| **Related Feature** | F-16: Count Variance Investigation & Approval |
| **Related Functional Requirements** | FR-034, FR-037 |

---

### PERM-043: Request Stock Adjustment

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-043 |
| **Permission Name** | Request Stock Adjustment |
| **Description** | Submit stock adjustment requests (increase or decrease) with mandatory reason code, product identification, quantity, and supporting context. |
| **Business Reason** | Enables corrections for damage, shrinkage, data errors, and approved count variances with full accountability. |
| **Related Feature** | F-17: Stock Adjustments & Write-Offs |
| **Related Functional Requirements** | FR-035 |

---

### PERM-044: Approve Stock Adjustment

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-044 |
| **Permission Name** | Approve Stock Adjustment |
| **Description** | Review and approve or reject stock adjustment requests, including those exceeding defined quantity or value thresholds. |
| **Business Reason** | Provides oversight proportional to financial impact; prevents large-scale fraud or error through independent approval. |
| **Related Feature** | F-17: Stock Adjustments & Write-Offs |
| **Related Functional Requirements** | FR-035, FR-037 |

---

### PERM-045: Request Inventory Write-Off

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-045 |
| **Permission Name** | Request Inventory Write-Off |
| **Description** | Submit write-off requests for obsolete, damaged, stolen, or otherwise permanently removed inventory with documented evidence and reason code. |
| **Business Reason** | Formalizes permanent stock removal with accountability; supports shrinkage tracking and financial alignment. |
| **Related Feature** | F-17: Stock Adjustments & Write-Offs |
| **Related Functional Requirements** | FR-036 |

---

### PERM-046: Approve Inventory Write-Off

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-046 |
| **Permission Name** | Approve Inventory Write-Off |
| **Description** | Review and authorize inventory write-offs per policy thresholds with documented approval before balances are reduced. |
| **Business Reason** | Protects against fraudulent disposal and ensures financial and operational records align on removed stock. |
| **Related Feature** | F-17: Stock Adjustments & Write-Offs |
| **Related Functional Requirements** | FR-036, FR-037 |

---

### PERM-047: Place Stock on Quarantine or Hold

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-047 |
| **Permission Name** | Place Stock on Quarantine or Hold |
| **Description** | Move specified inventory quantity to quarantine or hold status pending quality investigation, inspection, or regulatory clearance. |
| **Business Reason** | Prevents shipping defective, damaged, or uninspected goods; excludes held stock from sellable availability immediately. |
| **Related Feature** | F-18: Quarantine & Hold Stock Management |
| **Related Functional Requirements** | FR-038 |

---

### PERM-048: Release Stock from Quarantine or Hold

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-048 |
| **Permission Name** | Release Stock from Quarantine or Hold |
| **Description** | Release quarantined or held stock to available status or route to write-off based on inspection outcome. |
| **Business Reason** | Completes the hold lifecycle; restores sellable stock only after quality confirmation. |
| **Related Feature** | F-18: Quarantine & Hold Stock Management |
| **Related Functional Requirements** | FR-038 |

---

### PERM-049: View Shrinkage and Loss Analysis

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-049 |
| **Permission Name** | View Shrinkage and Loss Analysis |
| **Description** | View aggregated adjustment, write-off, and count variance data by reason code, location, and period with trend comparison. |
| **Business Reason** | Converts transaction data into actionable management insight for targeted loss prevention. |
| **Related Feature** | F-19: Shrinkage & Obsolescence Analysis |
| **Related Functional Requirements** | FR-039 |

---

### PERM-050: Review Obsolete and Slow-Moving Stock

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-050 |
| **Permission Name** | Review Obsolete and Slow-Moving Stock |
| **Description** | View and act on slow-moving and obsolete stock identified by aging analysis to support clearance, transfer, or write-off decisions. |
| **Business Reason** | Releases working capital trapped in dead stock and reduces carrying costs. |
| **Related Feature** | F-19: Shrinkage & Obsolescence Analysis |
| **Related Functional Requirements** | FR-040 |

---

## Order Fulfillment

---

### PERM-051: Confirm Order Availability

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-051 |
| **Permission Name** | Confirm Order Availability |
| **Description** | Verify that requested products are available in sufficient ATP quantity at the appropriate fulfillment location before confirming delivery commitments. |
| **Business Reason** | Prevents overpromising and order failures; reduces cancellations, complaints, and expedited shipping costs. |
| **Related Feature** | F-10: Order Availability & Reservation |
| **Related Functional Requirements** | FR-041 |

---

### PERM-052: Reserve Inventory

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-052 |
| **Permission Name** | Reserve Inventory |
| **Description** | Reserve specific inventory quantities against confirmed orders at the designated fulfillment location, reducing ATP immediately. |
| **Business Reason** | Prevents double-allocation of the same physical stock to multiple orders during the fulfillment window. |
| **Related Feature** | F-10: Order Availability & Reservation |
| **Related Functional Requirements** | FR-042 |

---

### PERM-053: Release Inventory Reservation

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-053 |
| **Permission Name** | Release Inventory Reservation |
| **Description** | Release inventory reservations when orders are cancelled, modified, expired per policy, or fully fulfilled, restoring ATP. |
| **Business Reason** | Prevents stock from being indefinitely locked to unfulfilled or cancelled orders, artificially reducing sellable availability. |
| **Related Feature** | F-10: Order Availability & Reservation |
| **Related Functional Requirements** | FR-043 |

---

### PERM-054: Release Order to Fulfillment

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-054 |
| **Permission Name** | Release Order to Fulfillment |
| **Description** | Release confirmed and reserved orders to the fulfillment pick queue for warehouse execution. |
| **Business Reason** | Controls fulfillment pacing and prioritization; initiates the physical pick-pack-ship cycle. |
| **Related Feature** | F-11: Pick, Pack & Ship Fulfillment |
| **Related Functional Requirements** | FR-044 |

---

### PERM-055: Execute Pick and Pack

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-055 |
| **Permission Name** | Execute Pick and Pack |
| **Description** | Execute pick list assignments, verify picked quantities, and pack orders per shipping standards. |
| **Business Reason** | Completes the physical fulfillment preparation cycle with verified product and quantity accuracy. |
| **Related Feature** | F-11: Pick, Pack & Ship Fulfillment |
| **Related Functional Requirements** | FR-044 |

---

### PERM-056: Confirm Shipment

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-056 |
| **Permission Name** | Confirm Shipment |
| **Description** | Record shipment confirmation with inventory deduction upon verified dispatch of packed orders. |
| **Business Reason** | Ensures inventory records match goods dispatched; updates order fulfillment status to shipped. |
| **Related Feature** | F-11: Pick, Pack & Ship Fulfillment |
| **Related Functional Requirements** | FR-044 |

---

### PERM-057: Process Partial Fulfillment

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-057 |
| **Permission Name** | Process Partial Fulfillment |
| **Description** | Ship available order quantity when full quantity is unavailable and place remaining lines on backorder with documented customer acknowledgment. |
| **Business Reason** | Balances customer service with inventory reality; avoids complete order holds when partial delivery is acceptable. |
| **Related Feature** | F-12: Partial Fulfillment & Backorder Management |
| **Related Functional Requirements** | FR-045 |

---

### PERM-058: Manage Backorder Queue

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-058 |
| **Permission Name** | Manage Backorder Queue |
| **Description** | Maintain backorder priority sequencing and process automatic or manual reservation when stock becomes available for backordered lines. |
| **Business Reason** | Ensures fair and policy-driven fulfillment of delayed orders; reduces manual backorder tracking. |
| **Related Feature** | F-12: Partial Fulfillment & Backorder Management |
| **Related Functional Requirements** | FR-046 |

---

### PERM-059: Report Fulfillment Exception

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-059 |
| **Permission Name** | Report Fulfillment Exception |
| **Description** | Report pick failures, stock-not-found, damaged items during pick, and other outbound fulfillment exceptions with order and product context. |
| **Business Reason** | Enables rapid exception resolution before customer impact; triggers inventory correction when physical reality differs from system. |
| **Related Feature** | F-13: Fulfillment Exception Handling |
| **Related Functional Requirements** | FR-047 |

---

### PERM-060: Resolve Fulfillment Exception

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-060 |
| **Permission Name** | Resolve Fulfillment Exception |
| **Description** | Resolve fulfillment exceptions through re-pick, cancellation, adjustment, or substitution paths and update order and inventory records accordingly. |
| **Business Reason** | Minimizes customer impact from operational disruptions; corrects inventory when exceptions reveal record inaccuracy. |
| **Related Feature** | F-13: Fulfillment Exception Handling |
| **Related Functional Requirements** | FR-047 |

---

### PERM-061: Allocate Multi-Location Fulfillment

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-061 |
| **Permission Name** | Allocate Multi-Location Fulfillment |
| **Description** | Allocate and reserve order lines across multiple fulfillment locations when no single location holds sufficient ATP for all lines. |
| **Business Reason** | Maximizes fill rate across the network; fulfills orders that would otherwise be rejected when aggregate network stock is sufficient. |
| **Related Feature** | F-10: Order Availability & Reservation |
| **Related Functional Requirements** | FR-048 |

---

### PERM-062: View Order Fulfillment Status

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-062 |
| **Permission Name** | View Order Fulfillment Status |
| **Description** | View order fulfillment status including reserved, picking, shipped, partially shipped, backordered, and cancelled states per order and line. |
| **Business Reason** | Reduces customer service inquiry time and prevents conflicting information given to customers about order status. |
| **Related Feature** | F-11: Pick, Pack & Ship Fulfillment |
| **Related Functional Requirements** | FR-049 |

---

### PERM-063: Approve Product Substitution

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-063 |
| **Permission Name** | Approve Product Substitution |
| **Description** | Authorize substitution of ordered products with approved alternate SKUs when primary product is unavailable, with documented approval. |
| **Business Reason** | Recovers revenue from orders that would otherwise fail fulfillment while maintaining control over acceptable substitutes. |
| **Related Feature** | F-13: Fulfillment Exception Handling |
| **Related Functional Requirements** | FR-050 |

---

## Replenishment

---

### PERM-064: View Low-Stock Alerts

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-064 |
| **Permission Name** | View Low-Stock Alerts |
| **Description** | View automatically generated low-stock and out-of-stock alerts with product, location, current ATP, threshold, and priority. |
| **Business Reason** | Converts passive monitoring into actionable signals enabling replenishment before customer-facing stockouts. |
| **Related Feature** | F-20: Low-Stock Alerting & Replenishment |
| **Related Functional Requirements** | FR-051, FR-076 |

---

### PERM-065: Acknowledge or Dismiss Stock Alert

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-065 |
| **Permission Name** | Acknowledge or Dismiss Stock Alert |
| **Description** | Review, acknowledge, or dismiss low-stock alerts with documented rationale for deferred or dismissed conditions. |
| **Business Reason** | Ensures alerts drive action rather than alert fatigue; distinguishes genuine replenishment needs from false positives. |
| **Related Feature** | F-20: Low-Stock Alerting & Replenishment |
| **Related Functional Requirements** | FR-052 |

---

### PERM-066: View Replenishment Suggestions

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-066 |
| **Permission Name** | View Replenishment Suggestions |
| **Description** | View system-generated replenishment suggestions including recommended order quantity, rationale, and network availability context. |
| **Business Reason** | Moves replenishment from reactive gut-feel to threshold-driven discipline. |
| **Related Feature** | F-20: Low-Stock Alerting & Replenishment |
| **Related Functional Requirements** | FR-053 |

---

### PERM-067: Create Purchase Requisition

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-067 |
| **Permission Name** | Create Purchase Requisition |
| **Description** | Create purchase requisitions from replenishment suggestions or manual requests with product, quantity, location, and justification. |
| **Business Reason** | Formalizes the handoff from replenishment planning to procurement with documented need. |
| **Related Feature** | F-20: Low-Stock Alerting & Replenishment |
| **Related Functional Requirements** | FR-054 |

---

### PERM-068: Approve Purchase Requisition

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-068 |
| **Permission Name** | Approve Purchase Requisition |
| **Description** | Review and approve or reject purchase requisitions per policy before conversion to purchase orders. |
| **Business Reason** | Maintains procurement approval accountability and spend control before supplier commitment. |
| **Related Feature** | F-20: Low-Stock Alerting & Replenishment |
| **Related Functional Requirements** | FR-054 |

---

### PERM-069: Approve Purchase Order

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-069 |
| **Permission Name** | Approve Purchase Order |
| **Description** | Review and approve purchase orders before they are issued to suppliers, per purchasing authority limits. |
| **Business Reason** | Enforces procurement governance and prevents unauthorized supplier commitments. |
| **Related Feature** | F-07: Purchase Order & Inbound Supply Management |
| **Related Functional Requirements** | FR-013, FR-054 |

---

### PERM-070: Override Safety Stock Protection

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-070 |
| **Permission Name** | Override Safety Stock Protection |
| **Description** | Authorize exceptions when reservations or transfers would consume safety stock below defined minimum, with documented reason and replenishment plan. |
| **Business Reason** | Allows controlled exceptions for urgent demand while preserving the buffer protecting against supply uncertainty. |
| **Related Feature** | F-03: Stock Policy & Product Classification |
| **Related Functional Requirements** | FR-056 |

---

## Network Transfers

---

### PERM-071: Request Stock Transfer

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-071 |
| **Permission Name** | Request Stock Transfer |
| **Description** | Initiate inter-location transfer requests specifying product, quantity, source location, destination location, and business justification. |
| **Business Reason** | Enables network balancing without waiting for supplier replenishment; corrects local stockouts using existing network inventory. |
| **Related Feature** | F-08: Inter-Location Stock Transfers |
| **Related Functional Requirements** | FR-058 |

---

### PERM-072: Approve Stock Transfer

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-072 |
| **Permission Name** | Approve Stock Transfer |
| **Description** | Review transfer requests and approve, reject, or modify proposed quantities with documented rationale, enforcing source minimum threshold protection. |
| **Business Reason** | Prevents unauthorized stock movements that create new imbalances or deplete source locations below service levels. |
| **Related Feature** | F-08: Inter-Location Stock Transfers |
| **Related Functional Requirements** | FR-059, FR-063 |

---

### PERM-073: Dispatch Stock Transfer

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-073 |
| **Permission Name** | Dispatch Stock Transfer |
| **Description** | Confirm dispatch of approved transfer quantities from the source location, deducting stock and recording in-transit status. |
| **Business Reason** | Ensures source location balance is accurate at point of shipment; initiates in-transit accountability. |
| **Related Feature** | F-08: Inter-Location Stock Transfers |
| **Related Functional Requirements** | FR-060 |

---

### PERM-074: Receive Stock Transfer

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-074 |
| **Permission Name** | Receive Stock Transfer |
| **Description** | Confirm receipt of transferred stock at the destination location, including partial receipt and variance handling. |
| **Business Reason** | Completes the transfer lifecycle with balanced updates at both locations; prevents stock appearing lost between sites. |
| **Related Feature** | F-08: Inter-Location Stock Transfers |
| **Related Functional Requirements** | FR-060 |

---

### PERM-075: View In-Transit Inventory

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-075 |
| **Permission Name** | View In-Transit Inventory |
| **Description** | View inventory in transit between locations by product, source, destination, and dispatch date including overdue shipment flags. |
| **Business Reason** | Provides network visibility during transfer lead time and supports accountability for goods between dispatch and receipt. |
| **Related Feature** | F-08: Inter-Location Stock Transfers |
| **Related Functional Requirements** | FR-061 |

---

### PERM-076: View Network Rebalancing Recommendations

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-076 |
| **Permission Name** | View Network Rebalancing Recommendations |
| **Description** | View system-generated network rebalancing analysis identifying excess and shortage locations by product with recommended transfer quantities. |
| **Business Reason** | Proactively reduces network-wide overstock and stockout conditions; optimizes inventory investment across the enterprise. |
| **Related Feature** | F-09: Network Stock Rebalancing |
| **Related Functional Requirements** | FR-062 |

---

## Returns Management

---

### PERM-077: Authorize Customer Return

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-077 |
| **Permission Name** | Authorize Customer Return |
| **Description** | Create return authorization records linked to original orders with product, quantity, reason, and expected resolution. |
| **Business Reason** | Connects physical returns to commercial transactions; prevents unauthorized returns and enables accurate resolution. |
| **Related Feature** | F-21: Returns Management |
| **Related Functional Requirements** | FR-064 |

---

### PERM-078: Receive Returned Goods

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-078 |
| **Permission Name** | Receive Returned Goods |
| **Description** | Physically receive returned goods at the warehouse against return authorization and record received quantity and condition. |
| **Business Reason** | Captures return arrival in inventory records; initiates inspection workflow before restocking. |
| **Related Feature** | F-21: Returns Management |
| **Related Functional Requirements** | FR-065 |

---

### PERM-079: Inspect Returned Goods

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-079 |
| **Permission Name** | Inspect Returned Goods |
| **Description** | Perform inspection of returned goods and record outcome as restock, rework, or write-off before inventory status changes. |
| **Business Reason** | Ensures only resalable goods re-enter sellable inventory; prevents damaged returns from being shipped as new. |
| **Related Feature** | F-21: Returns Management |
| **Related Functional Requirements** | FR-065 |

---

### PERM-080: Restock Returned Inventory

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-080 |
| **Permission Name** | Restock Returned Inventory |
| **Description** | Apply disposition decision to increase on-hand and ATP for approved restock quantity at the designated location. |
| **Business Reason** | Recovers sellable value from returns; maintains accurate inventory reflecting true available stock. |
| **Related Feature** | F-21: Returns Management |
| **Related Functional Requirements** | FR-066 |

---

### PERM-081: Write Off Returned Inventory

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-081 |
| **Permission Name** | Write Off Returned Inventory |
| **Description** | Process write-off of non-resalable returned quantity with reason code and linkage to original return and order. |
| **Business Reason** | Accurately removes unsellable return quantity from inventory with full traceability. |
| **Related Feature** | F-21: Returns Management |
| **Related Functional Requirements** | FR-066 |

---

### PERM-082: View Return Processing Status

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-082 |
| **Permission Name** | View Return Processing Status |
| **Description** | View return processing status from authorization through receipt, inspection, disposition, and completion. |
| **Business Reason** | Enables accurate customer communication on refund, replacement, or credit timing. |
| **Related Feature** | F-21: Returns Management |
| **Related Functional Requirements** | FR-067 |

---

## Reporting & Analytics

---

### PERM-083: View Inventory Dashboard

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-083 |
| **Permission Name** | View Inventory Dashboard |
| **Description** | View inventory summary dashboard showing stock levels, low-stock and out-of-stock counts, and health indicators across authorized locations. |
| **Business Reason** | Gives management a single operational view of inventory health without manual report compilation. |
| **Related Feature** | F-22: Inventory Reporting & Dashboards |
| **Related Functional Requirements** | FR-068 |

---

### PERM-084: View Stock Movement Reports

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-084 |
| **Permission Name** | View Stock Movement Reports |
| **Description** | View and generate stock movement reports showing receipts, transfers, adjustments, fulfillments, and returns over a selectable period. |
| **Business Reason** | Supports operational review, audit substantiation, and trend analysis without manual movement reconstruction. |
| **Related Feature** | F-22: Inventory Reporting & Dashboards |
| **Related Functional Requirements** | FR-069 |

---

### PERM-085: View Stockout and Overstock Reports

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-085 |
| **Permission Name** | View Stockout and Overstock Reports |
| **Description** | View reports identifying products and locations in stockout or overstock condition with severity and demand context. |
| **Business Reason** | Directs purchasing and transfer action toward problem areas; reduces lost sales and trapped capital. |
| **Related Feature** | F-22: Inventory Reporting & Dashboards |
| **Related Functional Requirements** | FR-070 |

---

### PERM-086: View Inventory Accuracy Reports

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-086 |
| **Permission Name** | View Inventory Accuracy Reports |
| **Description** | View inventory accuracy and count variance reports by location and period including accuracy rate trends and recurring variance SKUs. |
| **Business Reason** | Measures progress toward accuracy objectives and identifies locations or SKUs requiring corrective attention. |
| **Related Feature** | F-14: Cycle Counting; F-22: Inventory Reporting & Dashboards |
| **Related Functional Requirements** | FR-071 |

---

### PERM-087: View Location Performance Reports

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-087 |
| **Permission Name** | View Location Performance Reports |
| **Description** | View location-level performance snapshots comparing accuracy, stockout frequency, shrinkage, and fulfillment metrics across the network. |
| **Business Reason** | Enables fair comparison and accountability across locations; addresses inconsistent process performance. |
| **Related Feature** | F-22: Inventory Reporting & Dashboards |
| **Related Functional Requirements** | FR-072 |

---

### PERM-088: View Inventory Performance KPIs

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-088 |
| **Permission Name** | View Inventory Performance KPIs |
| **Description** | View calculated inventory KPIs including fill rate, turnover, days of supply, and record accuracy with trend and target comparison. |
| **Business Reason** | Enables management to measure operational maturity and progress toward strategic inventory objectives. |
| **Related Feature** | F-23: Inventory Performance KPIs |
| **Related Functional Requirements** | FR-073 |

---

### PERM-089: View Replenishment Reports

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-089 |
| **Permission Name** | View Replenishment Reports |
| **Description** | View replenishment-focused reports showing items below threshold, active alerts, open requisitions, and expected inbound supply. |
| **Business Reason** | Consolidates replenishment decision information in one view; reduces time gathering data from multiple sources. |
| **Related Feature** | F-20: Low-Stock Alerting & Replenishment; F-22: Inventory Reporting & Dashboards |
| **Related Functional Requirements** | FR-074 |

---

### PERM-090: View Inventory Valuation Reports

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-090 |
| **Permission Name** | View Inventory Valuation Reports |
| **Description** | View inventory valuation summaries based on operational quantities and agreed unit costs for financial review and reconciliation. |
| **Business Reason** | Bridges operations and finance inventory records; reduces month-end reconciliation effort and misstatement risk. |
| **Related Feature** | F-24: Financial Inventory Reconciliation |
| **Related Functional Requirements** | FR-075 |

---

### PERM-091: Export Reports

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-091 |
| **Permission Name** | Export Reports |
| **Description** | Export authorized inventory reports and dashboard views for offline review, distribution, and audit substantiation. |
| **Business Reason** | Supports management meetings, audit packages, and finance workflows requiring portable data extracts. |
| **Related Feature** | F-22: Inventory Reporting & Dashboards |
| **Related Functional Requirements** | FR-069, FR-071, FR-074, FR-075 |

---

## Commercial Readiness

---

### PERM-092: Review Campaign Stock Readiness

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-092 |
| **Permission Name** | Review Campaign Stock Readiness |
| **Description** | Review stock readiness against promotional or launch targets, identifying gaps with lead-time-aware warnings and go/no-go indications. |
| **Business Reason** | Prevents campaign stockouts that damage marketing ROI and brand reputation. |
| **Related Feature** | F-25: Promotional & Launch Stock Readiness |
| **Related Functional Requirements** | FR-057, FR-080 |

---

### PERM-093: Ring-Fence Promotional Stock

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-093 |
| **Permission Name** | Ring-Fence Promotional Stock |
| **Description** | Allocate and ring-fence promotional inventory from general availability to protect campaign stock from routine fulfillment consumption. |
| **Business Reason** | Ensures marketed products remain available for campaign demand rather than being consumed by pre-campaign orders. |
| **Related Feature** | F-25: Promotional & Launch Stock Readiness |
| **Related Functional Requirements** | FR-057 |

---

## Financial Alignment

---

### PERM-094: Perform Financial Inventory Reconciliation

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-094 |
| **Permission Name** | Perform Financial Inventory Reconciliation |
| **Description** | Execute operational-to-financial inventory reconciliation using period-end quantity summaries, adjustment logs, and valuation views aligned with finance reporting periods. |
| **Business Reason** | Enables timely month-end close and reduces operations-finance misalignment on inventory balances. |
| **Related Feature** | F-24: Financial Inventory Reconciliation |
| **Related Functional Requirements** | FR-089 |

---

## Administration & Audit

---

### PERM-095: Manage User Accounts

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-095 |
| **Permission Name** | Manage User Accounts |
| **Description** | Create, deactivate, and maintain user accounts including account status changes for onboarding and offboarding. |
| **Business Reason** | Ensures system access reflects current organizational membership; prevents orphaned accounts after staff turnover. |
| **Related Feature** | F-27: User Access & Role Management |
| **Related Functional Requirements** | FR-085 |

---

### PERM-096: Assign User Roles and Location Scope

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-096 |
| **Permission Name** | Assign User Roles and Location Scope |
| **Description** | Assign and modify user role memberships and location access scope including network-wide or multi-location authority. |
| **Business Reason** | Aligns system access with organizational accountability and operational location boundaries. |
| **Related Feature** | F-27: User Access & Role Management |
| **Related Functional Requirements** | FR-081, FR-082, FR-085 |

---

### PERM-097: View User Activity Log

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-097 |
| **Permission Name** | View User Activity Log |
| **Description** | Query user activity logs for inventory transactions, approvals, configuration changes, and login events. |
| **Business Reason** | Enables traceability of who performed each action; strengthens loss prevention and security investigation. |
| **Related Feature** | F-28: Operational Accountability & Controls |
| **Related Functional Requirements** | FR-083 |

---

### PERM-098: View Inventory Audit Trail

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-098 |
| **Permission Name** | View Inventory Audit Trail |
| **Description** | View the complete, immutable audit trail of inventory quantity changes including before/after balances, reason codes, users, and timestamps. |
| **Business Reason** | Provides evidence for internal and external audit, dispute resolution, and root-cause investigation. |
| **Related Feature** | F-29: Audit Trail & Compliance |
| **Related Functional Requirements** | FR-086 |

---

### PERM-099: Query Audit Evidence

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-099 |
| **Permission Name** | Query Audit Evidence |
| **Description** | Run structured audit queries and export evidence packages covering transactions, adjustment approvals, count records, and control compliance. |
| **Business Reason** | Reduces audit preparation effort and demonstrates control effectiveness to internal and external auditors. |
| **Related Feature** | F-29: Audit Trail & Compliance |
| **Related Functional Requirements** | FR-087 |

---

### PERM-100: View Control Policy Breach Records

| Attribute | Description |
|-----------|-------------|
| **Permission ID** | PERM-100 |
| **Permission Name** | View Control Policy Breach Records |
| **Description** | View recorded instances where operational actions breached defined control policies or were processed as authorized exceptions. |
| **Business Reason** | Makes control weaknesses visible for corrective action rather than discoverable only at audit time. |
| **Related Feature** | F-29: Audit Trail & Compliance |
| **Related Functional Requirements** | FR-088 |

---

## Permission-to-Feature Coverage Matrix

| Feature | Permissions |
|---------|-------------|
| F-01 Product Catalog Management | PERM-001 – PERM-005 |
| F-02 Location & Network Setup | PERM-006 – PERM-010 |
| F-03 Stock Policy & Classification | PERM-011 – PERM-013, PERM-070 |
| F-04 Inventory Visibility & Search | PERM-017 – PERM-022 |
| F-05 Goods Receiving & Verification | PERM-023, PERM-028 – PERM-032, PERM-034 |
| F-06 Put-Away Management | PERM-033 |
| F-07 Purchase Order & Inbound Supply | PERM-024 – PERM-027, PERM-035 – PERM-036, PERM-069 |
| F-08 Inter-Location Stock Transfers | PERM-071 – PERM-075 |
| F-09 Network Stock Rebalancing | PERM-076 |
| F-10 Order Availability & Reservation | PERM-051 – PERM-053, PERM-061 |
| F-11 Pick, Pack & Ship Fulfillment | PERM-054 – PERM-056, PERM-062 |
| F-12 Partial Fulfillment & Backorders | PERM-057 – PERM-058 |
| F-13 Fulfillment Exception Handling | PERM-059 – PERM-060, PERM-063 |
| F-14 Cycle Counting | PERM-037 – PERM-038, PERM-086 |
| F-15 Full Physical Inventory Count | PERM-039 |
| F-16 Count Variance Investigation | PERM-040 – PERM-042 |
| F-17 Stock Adjustments & Write-Offs | PERM-014, PERM-043 – PERM-046 |
| F-18 Quarantine & Hold Management | PERM-047 – PERM-048 |
| F-19 Shrinkage & Obsolescence Analysis | PERM-049 – PERM-050 |
| F-20 Low-Stock Alerting & Replenishment | PERM-064 – PERM-068, PERM-089 |
| F-21 Returns Management | PERM-034, PERM-077 – PERM-082 |
| F-22 Inventory Reporting & Dashboards | PERM-083 – PERM-087, PERM-089, PERM-091 |
| F-23 Inventory Performance KPIs | PERM-088 |
| F-24 Financial Inventory Reconciliation | PERM-090, PERM-094 |
| F-25 Promotional Stock Readiness | PERM-092 – PERM-093 |
| F-27 User Access & Role Management | PERM-095 – PERM-096 |
| F-28 Operational Accountability & Controls | PERM-097 |
| F-29 Audit Trail & Compliance | PERM-098 – PERM-100 |
| F-30 System Go-Live & Initial Data Setup | PERM-015 – PERM-016 |

---

## Design Notes

### Segregation of Duties Pairs

The following permission pairs are designed for segregation-of-duties enforcement per FR-084. The system must prevent the same user from holding conflicting permissions in the same session unless an authorized exception applies:

| Initiate Permission | Approve Permission |
|--------------------|------------------|
| PERM-038 Perform Cycle Count | PERM-042 Approve Count Adjustment |
| PERM-043 Request Stock Adjustment | PERM-044 Approve Stock Adjustment |
| PERM-045 Request Inventory Write-Off | PERM-046 Approve Inventory Write-Off |
| PERM-067 Create Purchase Requisition | PERM-068 Approve Purchase Requisition |
| PERM-024 Create Purchase Order | PERM-069 Approve Purchase Order |
| PERM-071 Request Stock Transfer | PERM-072 Approve Stock Transfer |
| PERM-015 Import Initial Master Data | PERM-016 Approve Initial Data Import |
| PERM-028 Receive Goods (beyond tolerance) | PERM-032 Approve Receipt Beyond Tolerance |

### Notification Delivery

Operational notifications (FR-076–FR-080) are system-delivered capabilities tied to F-26. Notification receipt is driven by role configuration and subscribed events rather than standalone permissions. Users receive notifications when they hold permissions that make them accountable for the underlying action (e.g., PERM-072 holders receive transfer approval notifications per FR-077).

### Location Scoping

All transactional and visibility permissions are subject to location scope enforcement per FR-082. Location scope is assigned through PERM-096 and applied as a cross-cutting constraint across permissions — not as individual per-location permission instances.

---

## Document Summary

This catalog defines **100 system permissions** derived from **90 functional requirements** organized across **30 features**. Permissions use business-action naming and are intentionally independent of user roles. Role-to-permission mapping, location scope defaults, and segregation-of-duties rules should be addressed in the subsequent access control matrix design.

---

*End of System Permissions Document*
