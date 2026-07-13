# Inventory Management System Navigation Structure

## Purpose

This document defines the application's navigation structure for the Inventory Management System. It is based on the approved BRD, use cases, API design, and the screen inventory. It describes how users move through the application but does not define visual layout or page wireframes.

## Navigation Model

- **Primary navigation:** Persistent top-level modules used to move across major business domains.
- **Secondary navigation:** Section-level navigation within a selected module.
- **Breadcrumbs:** Hierarchical path showing where the user is and enabling quick backtracking.
- **Contextual navigation:** In-page task links, related records, status-driven actions, and work queues.
- **Role-specific menus:** Navigation visibility and priority adapted to each user role.

---

## Main Navigation

The main navigation should present the following top-level modules:

1. `Home`
2. `Inventory`
3. `Products`
4. `Locations`
5. `Procurement`
6. `Inbound`
7. `Fulfillment`
8. `Transfers`
9. `Returns`
10. `Reports & Analytics`
11. `Governance & Audit`
12. `Administration`

Supporting persistent utilities:

- `Notifications`
- `Global Search`
- `My Tasks / Approvals`
- `User Menu / Session`

---

## Secondary Navigation

Secondary navigation should appear after a user enters a main module.

### Home
- `Operational Dashboard`
- `Executive KPI Dashboard`
- `My Notifications`
- `My Approvals`

### Inventory
- `Inventory Status Monitor`
- `Availability Inquiry`
- `Movement History`
- `Cycle Counts`
- `Physical Counts`
- `Variance Approvals`
- `Stock Adjustments`
- `Write-Offs`
- `Quarantine & Holds`
- `Shrinkage & Obsolescence`

### Products
- `Product Catalog`
- `Product Import`
- `ABC Classification`
- `Stock Policies`

### Locations
- `Location Directory`
- `Location Hierarchy`
- `Storage Positions`
- `Location Activation / Closure`

### Procurement
- `Suppliers`
- `Purchase Requisitions`
- `Purchase Orders`
- `Inbound Delivery Planning`
- `Inbound Supply Tracking`
- `Low-Stock Alerts`
- `Replenishment Planning`

### Inbound
- `Goods Receipt Workbench`
- `Receipt Discrepancies`
- `Put-Away Workbench`
- `Non-PO Receipt Intake`

### Fulfillment
- `Order Reservation`
- `Pick / Pack / Ship`
- `Partial Fulfillment & Backorders`
- `Fulfillment Exceptions`
- `Order Status`
- `Multi-Location Fulfillment`

### Transfers
- `Transfer Requests`
- `Transfer Approvals`
- `Transfer Execution`
- `In-Transit Tracking`
- `Network Rebalancing`

### Returns
- `Return Authorizations`
- `Return Inspection & Disposition`

### Reports & Analytics
- `Operational Reports`
- `Inventory Dashboard`
- `KPI Dashboard`
- `Valuation Reconciliation`
- `Promotional Readiness`

### Governance & Audit
- `Governance Policies`
- `Reason Codes`
- `Audit Workspace`
- `Audit Trail Query`
- `Approvals Inbox`

### Administration
- `User Accounts`
- `Roles & Access Control`

---

## Breadcrumbs

Breadcrumbs should reflect the navigation hierarchy in the format:

`Home > Module > Section > Record / Action`

Examples:

- `Home > Inventory > Inventory Status Monitor`
- `Home > Products > Product Catalog > SKU-100245`
- `Home > Procurement > Purchase Orders > PO-2026-00418`
- `Home > Inbound > Goods Receipt Workbench > GR-2026-00291`
- `Home > Fulfillment > Order Status > SO-2026-01872`
- `Home > Transfers > Transfer Requests > TR-2026-00088`
- `Home > Returns > Return Authorizations > RA-2026-00116`
- `Home > Governance & Audit > Audit Trail Query > Export Results`
- `Home > Administration > User Accounts > User Profile > Edit Role Assignments`

Breadcrumb behavior:

- The first crumb should always return to `Home`.
- Intermediate crumbs should return to the parent list or workspace.
- The final crumb should represent the current screen, record, or action state.
- Modal or side-panel actions should not replace the breadcrumb unless they open as full screens.

---

## Contextual Navigation

Contextual navigation should be available within screens to help users complete related tasks without returning to module menus.

### Inventory contexts
- From `Inventory Status Monitor`:
  - `View Product`
  - `View Location`
  - `Open Movement History`
  - `Create Adjustment`
  - `Request Transfer`
  - `Open Replenishment Planning`

### Product contexts
- From `Product Catalog` or a product detail:
  - `Edit Product`
  - `View Stock by Location`
  - `Open Stock Policy`
  - `Open ABC Classification`
  - `View Movement History`
  - `Import Related Data`

### Procurement contexts
- From `Low-Stock Alerts`:
  - `Acknowledge Alert`
  - `Review Network Availability`
  - `Create Requisition`
  - `Create Transfer Request`
- From `Purchase Requisition`:
  - `Approve`
  - `Reject`
  - `Convert to PO`

### Inbound contexts
- From `Goods Receipt Workbench`:
  - `Verify Receipt`
  - `Log Discrepancy`
  - `Send to Put-Away`
  - `View PO`

### Fulfillment contexts
- From `Order Reservation`:
  - `Check Availability`
  - `Reserve Stock`
  - `Release Reservation`
  - `Open Split Fulfillment`
- From `Pick / Pack / Ship`:
  - `Verify Pick`
  - `View Lot / Batch`
  - `Raise Exception`
  - `Confirm Shipment`

### Transfer contexts
- From `Transfer Request`:
  - `Approve / Reject`
  - `View Source Capacity`
  - `Dispatch Transfer`
  - `Receive Transfer`

### Returns contexts
- From `Return Authorization`:
  - `View Original Order`
  - `Receive Return`
  - `Inspect Return`
  - `Disposition Return`

### Audit and admin contexts
- From `Audit Trail Query`:
  - `Open Record`
  - `Export Evidence`
- From `User Account Management`:
  - `Assign Role`
  - `Suspend User`
  - `Deactivate User`
  - `View Access Scope`

---

## Role-Specific Menus

Role-specific menus should simplify navigation by exposing only relevant modules and prioritizing frequent tasks.

### Executive roles
Roles:
- `Chief Executive Officer`
- `Chief Operating Officer`
- `Chief Financial Officer`

Priority menu:
- `Home`
- `Reports & Analytics`
- `Governance & Audit`

Common secondary focus:
- `Executive KPI Dashboard`
- `Operational Reports`
- `Valuation Reconciliation`
- `Audit Trail Query`

### Inventory control roles
Roles:
- `Inventory Controller`
- `Operations Director`

Priority menu:
- `Home`
- `Inventory`
- `Products`
- `Locations`
- `Transfers`
- `Reports & Analytics`
- `Governance & Audit`

Common secondary focus:
- `Inventory Status Monitor`
- `Cycle Counts`
- `Physical Counts`
- `Variance Approvals`
- `Stock Adjustments`
- `Quarantine & Holds`
- `Shrinkage & Obsolescence`

### Warehouse operations roles
Roles:
- `Warehouse Manager`
- `Receiving Clerk`
- `Warehouse Staff`
- `Warehouse Picker / Packer`

Priority menu:
- `Home`
- `Inbound`
- `Inventory`
- `Fulfillment`
- `Transfers`
- `Returns`

Common secondary focus:
- `Goods Receipt Workbench`
- `Put-Away Workbench`
- `Cycle Counts`
- `Pick / Pack / Ship`
- `Fulfillment Exceptions`
- `Transfer Execution`
- `Return Inspection & Disposition`

### Procurement roles
Roles:
- `Purchasing Manager`
- `Buyer / Procurement Officer`

Priority menu:
- `Home`
- `Procurement`
- `Inventory`
- `Transfers`
- `Reports & Analytics`

Common secondary focus:
- `Suppliers`
- `Purchase Requisitions`
- `Purchase Orders`
- `Inbound Delivery Planning`
- `Inbound Supply Tracking`
- `Low-Stock Alerts`
- `Replenishment Planning`

### Commercial roles
Roles:
- `Sales Manager`
- `Sales Representative`
- `Customer Service Representative`
- `Marketing Manager`

Priority menu:
- `Home`
- `Inventory`
- `Fulfillment`
- `Returns`
- `Reports & Analytics`

Common secondary focus:
- `Availability Inquiry`
- `Order Reservation`
- `Order Status`
- `Partial Fulfillment & Backorders`
- `Return Authorizations`
- `Promotional Readiness`

### Audit and compliance roles
Roles:
- `Internal Auditor`
- `External Auditor`

Priority menu:
- `Home`
- `Governance & Audit`
- `Reports & Analytics`

Common secondary focus:
- `Audit Workspace`
- `Audit Trail Query`
- `Valuation Reconciliation`
- `Operational Reports`

### System administration roles
Roles:
- `System Administrator`

Priority menu:
- `Home`
- `Administration`
- `Governance & Audit`

Common secondary focus:
- `User Accounts`
- `Roles & Access Control`
- `Reason Codes`

---

## Text-Based Sitemap

```text
Home
├── Operational Dashboard
├── Executive KPI Dashboard
├── Notifications
└── My Tasks / Approvals

Inventory
├── Inventory Status Monitor
│   ├── Product Stock Detail
│   ├── Location Stock Detail
│   ├── Request Transfer
│   ├── Create Adjustment
│   └── Open Replenishment Planning
├── Availability Inquiry
│   ├── Product Search Results
│   └── Network Availability Detail
├── Movement History
│   └── Transaction Detail
├── Cycle Counts
│   ├── Assigned Count Queue
│   └── Count Submission
├── Physical Counts
│   ├── Count Session Detail
│   └── Count Certification
├── Variance Approvals
│   └── Variance Investigation Detail
├── Stock Adjustments
│   └── Adjustment Case Detail
├── Write-Offs
│   └── Write-Off Authorization Detail
├── Quarantine & Holds
│   └── Hold Detail
└── Shrinkage & Obsolescence

Products
├── Product Catalog
│   ├── Product Detail
│   ├── Create Product
│   └── Edit Product
├── Product Import
│   ├── Upload File
│   ├── Validation Results
│   └── Import Completion
├── ABC Classification
└── Stock Policies
    └── Product-Location Policy Detail

Locations
├── Location Directory
│   └── Location Detail
├── Location Hierarchy
├── Storage Positions
└── Location Activation / Closure

Procurement
├── Suppliers
│   └── Supplier Detail
├── Purchase Requisitions
│   └── Requisition Detail
├── Purchase Orders
│   └── Purchase Order Detail
├── Inbound Delivery Planning
├── Inbound Supply Tracking
├── Low-Stock Alerts
│   └── Alert Detail
└── Replenishment Planning
    ├── Replenishment Recommendation Detail
    └── Convert to Requisition / PO

Inbound
├── Goods Receipt Workbench
│   └── Goods Receipt Detail
├── Receipt Discrepancies
│   └── Discrepancy Detail
├── Put-Away Workbench
│   └── Put-Away Task Detail
└── Non-PO Receipt Intake

Fulfillment
├── Order Reservation
│   └── Order Reservation Detail
├── Pick / Pack / Ship
│   ├── Pick Queue
│   ├── Pick Verification
│   ├── Packing
│   └── Shipment Confirmation
├── Partial Fulfillment & Backorders
│   └── Backorder Detail
├── Fulfillment Exceptions
│   └── Exception Detail
├── Order Status
│   └── Order Detail
└── Multi-Location Fulfillment
    └── Split Fulfillment Plan

Transfers
├── Transfer Requests
│   └── Transfer Request Detail
├── Transfer Approvals
│   └── Approval Detail
├── Transfer Execution
│   ├── Dispatch Detail
│   └── Receipt Detail
├── In-Transit Tracking
└── Network Rebalancing
    └── Rebalancing Recommendation Detail

Returns
├── Return Authorizations
│   └── Return Authorization Detail
└── Return Inspection & Disposition
    ├── Return Receipt Detail
    ├── Inspection Detail
    └── Disposition Detail

Reports & Analytics
├── Inventory Dashboard
├── Operational Reports
│   ├── Movement Report
│   ├── Stockout / Overstock Report
│   ├── Accuracy Report
│   └── Location Performance Report
├── Executive KPI Dashboard
├── Valuation Reconciliation
└── Promotional Readiness

Governance & Audit
├── Governance Policies
├── Reason Codes
├── Audit Workspace
│   └── Audit Review Detail
├── Audit Trail Query
│   └── Audit Record Detail
└── Approvals Inbox
    ├── Transfer Approvals
    └── Adjustment / Variance Approvals

Administration
├── User Accounts
│   └── User Account Detail
└── Roles & Access Control
    └── Role Permission Detail
```

---

## Navigation Principles

1. `Home` should act as the universal return point for all roles.
2. Modules should reflect business domains, not technical services.
3. Work-queue screens should be reachable from both module navigation and `My Tasks / Approvals`.
4. High-frequency operational screens should be no more than two clicks from the main navigation.
5. Role-based visibility should hide irrelevant modules rather than merely disabling them.
6. Contextual links should connect adjacent workflows such as alert to requisition, receipt to discrepancy, and order to shipment.

