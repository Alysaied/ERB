# Inventory Management System Low-Fidelity Wireframe Specifications

## Purpose

This document defines low-fidelity wireframe specifications for every identified Inventory Management System screen. The specifications are text-based and describe structural content only. They do not define visual styling, spacing, branding, or high-fidelity interaction behavior.

## Structure Standard

Each screen specification includes:

1. Header
2. Navigation
3. Main content
4. Forms
5. Tables
6. Action buttons
7. Footer (if applicable)

## Shared Layout Assumptions

- The application uses a persistent top header.
- Main navigation is available globally.
- Secondary navigation appears at module level when applicable.
- Breadcrumbs appear below the header on all non-home screens.
- Most operational screens use a list-detail or dashboard-workbench structure.
- Footer is optional and used mainly for system metadata, help links, and record timestamps.

---

## UI-001 Sign In / Session Entry

### Header
- Product name
- Environment indicator
- Optional help link

### Navigation
- No primary application navigation before authentication

### Main Content
- Centered sign-in panel
- Brief system purpose statement
- Optional support/contact note

### Forms
- Username / email
- Password
- Optional remember session checkbox

### Tables
- None

### Action Buttons
- `Sign In`
- `Forgot Password` or `Need Help`

### Footer
- Version
- Security/privacy notice

---

## UI-002 Operational Home Dashboard

### Header
- Page title
- Global search
- Notification icon
- My tasks / approvals shortcut
- User menu

### Navigation
- Main navigation
- Optional role-based quick links

### Main Content
- KPI summary cards
- Stock health summary
- Alert snapshot
- Task / approval snapshot
- Shortcut tiles to core workflows

### Forms
- Dashboard filter bar: location, date range, role scope

### Tables
- Recent alerts table
- Pending tasks table

### Action Buttons
- `View Alerts`
- `Open Approvals`
- `Go to Inventory`
- `Refresh`

### Footer
- Last refreshed timestamp

---

## UI-003 Executive KPI Dashboard

### Header
- Dashboard title
- Reporting period selector
- Export option

### Navigation
- Main navigation
- Secondary navigation for dashboards/reports
- Breadcrumbs

### Main Content
- Executive KPI cards
- Trend summaries
- Variance/target indicators
- Drill-down summaries

### Forms
- Filter controls: period, business unit, location group

### Tables
- KPI summary table

### Action Buttons
- `Apply Filters`
- `Export Dashboard`
- `View Detail`

### Footer
- Data as-of timestamp

---

## UI-004 Notification Center

### Header
- Page title
- Unread count

### Navigation
- Main navigation
- Breadcrumbs

### Main Content
- Notification inbox layout
- Left filter panel or top filter bar
- Selected notification detail pane

### Forms
- Filter controls: type, priority, module, status, date

### Tables
- Notification list table

### Action Buttons
- `Open Related Record`
- `Mark as Handled`
- `Acknowledge`
- `Refresh`

### Footer
- Optional archive retention note

---

## UI-005 Product Catalog Management

### Header
- Page title
- Create product shortcut

### Navigation
- Main navigation
- Products secondary navigation
- Breadcrumbs

### Main Content
- Search/filter toolbar
- Product results list
- Product detail side panel or full detail region

### Forms
- Search fields: SKU, name, category, status, ABC class
- Product form fields: SKU, name, description, UOM, category, barcode, lifecycle status

### Tables
- Product catalog table

### Action Buttons
- `Create Product`
- `Edit`
- `Save`
- `Change Status`
- `Resolve Duplicate`

### Footer
- Created/updated metadata

---

## UI-006 Product Import Workspace

### Header
- Page title
- Import instructions link

### Navigation
- Main navigation
- Products secondary navigation
- Breadcrumbs

### Main Content
- Import steps panel
- Template download area
- Upload zone
- Validation results region
- Completion summary region

### Forms
- File upload field
- Optional import type selector

### Tables
- Validation errors table
- Import summary table

### Action Buttons
- `Download Template`
- `Upload File`
- `Validate`
- `Confirm Import`
- `Cancel`

### Footer
- Supported file format note

---

## UI-007 Location and Warehouse Management

### Header
- Page title
- Create location shortcut

### Navigation
- Main navigation
- Locations secondary navigation
- Breadcrumbs

### Main Content
- Location directory panel
- Hierarchy view
- Location detail view
- Storage positions subsection

### Forms
- Location form: code, name, type, parent, status
- Storage position form: zone, aisle, bin, status

### Tables
- Location list table
- Storage positions table

### Action Buttons
- `Create Location`
- `Edit`
- `Save`
- `Activate`
- `Deactivate`
- `Close Location`

### Footer
- Location lifecycle metadata

---

## UI-008 Stock Policy and Threshold Management

### Header
- Page title

### Navigation
- Main navigation
- Products secondary navigation
- Breadcrumbs

### Main Content
- Product-location selector
- Current stock policy summary
- Threshold editing area

### Forms
- Search fields: product, location
- Policy form: reorder level, minimum threshold, safety stock, effective date

### Tables
- Existing policy table by product/location

### Action Buttons
- `Search`
- `Edit Policy`
- `Save`
- `Reset`

### Footer
- Policy version/effective timestamp

---

## UI-009 ABC Classification Management

### Header
- Page title

### Navigation
- Main navigation
- Products secondary navigation
- Breadcrumbs

### Main Content
- Classification summary
- Product review list
- Classification detail panel

### Forms
- Filter fields: category, current class, activity status
- Classification edit fields: ABC class, reason, effective date

### Tables
- Product classification table

### Action Buttons
- `Assign Class`
- `Save`
- `Bulk Update`

### Footer
- Classification last-updated metadata

---

## UI-010 Governance Policies and Reason Codes

### Header
- Page title
- Tab switcher for policies/reason codes

### Navigation
- Main navigation
- Governance & Audit secondary navigation
- Breadcrumbs

### Main Content
- Policy list and detail area
- Reason code list and detail area

### Forms
- Policy form: name, version, thresholds, tolerances, effective date, status
- Reason code form: code, category, description, active status

### Tables
- Governance policies table
- Reason codes table

### Action Buttons
- `Create Policy`
- `Publish`
- `Create Reason Code`
- `Retire`
- `Save`

### Footer
- Version and publication metadata

---

## UI-011 Supplier Management

### Header
- Page title
- Create supplier shortcut

### Navigation
- Main navigation
- Procurement secondary navigation
- Breadcrumbs

### Main Content
- Supplier list
- Supplier detail panel

### Forms
- Supplier form: code, name, contact, payment terms, lead time, active status

### Tables
- Supplier table

### Action Buttons
- `Create Supplier`
- `Edit`
- `Save`
- `Deactivate`

### Footer
- Supplier update metadata

---

## UI-012 Purchase Order Management

### Header
- Page title
- Create purchase order shortcut

### Navigation
- Main navigation
- Procurement secondary navigation
- Breadcrumbs

### Main Content
- PO search/filter area
- PO list
- PO detail and line items section

### Forms
- PO header form: supplier, destination, expected date, status
- PO lines form: product, quantity, unit, price, notes

### Tables
- Purchase orders table
- PO line items table

### Action Buttons
- `Create PO`
- `Save Draft`
- `Submit`
- `Amend`
- `Cancel PO`

### Footer
- Approval/status metadata

---

## UI-013 Purchase Requisition Management

### Header
- Page title

### Navigation
- Main navigation
- Procurement secondary navigation
- Breadcrumbs

### Main Content
- Requisition queue
- Requisition detail panel
- Status history section

### Forms
- Requisition form: product, quantity, required date, destination, rationale

### Tables
- Requisition table

### Action Buttons
- `Create Requisition`
- `Approve`
- `Reject`
- `Convert to PO`
- `Save`

### Footer
- Approval trail summary

---

## UI-014 Inbound Delivery Planning

### Header
- Page title

### Navigation
- Main navigation
- Procurement secondary navigation
- Breadcrumbs

### Main Content
- Expected deliveries calendar/list
- Selected delivery detail panel

### Forms
- Delivery planning fields: PO reference, shipment date, ETA, carrier, destination

### Tables
- Inbound deliveries table

### Action Buttons
- `Update Delivery`
- `Save`
- `Notify Receiving`

### Footer
- Latest supplier update timestamp

---

## UI-015 Goods Receipt Workbench

### Header
- Page title
- Location context

### Navigation
- Main navigation
- Inbound secondary navigation
- Breadcrumbs

### Main Content
- Pending receipt queue
- Receipt detail section
- Verification area

### Forms
- Receipt identification fields: PO/reference, supplier, dock, receipt type
- Verification fields: item scan, quantity received, condition, lot/batch, shelf-life

### Tables
- Pending receipts table
- Receipt line items table

### Action Buttons
- `Open Receipt`
- `Verify`
- `Log Discrepancy`
- `Confirm Receipt`
- `Send to Put-Away`

### Footer
- Receipt confirmation metadata

---

## UI-016 Receipt Discrepancy Resolution

### Header
- Page title

### Navigation
- Main navigation
- Inbound secondary navigation
- Breadcrumbs

### Main Content
- Open discrepancies queue
- Discrepancy detail panel
- Evidence/notes section

### Forms
- Discrepancy form: discrepancy type, quantity variance, reason code, notes, evidence reference
- Resolution form: accepted quantity, resolution note, approver note

### Tables
- Discrepancies table

### Action Buttons
- `Save Discrepancy`
- `Resolve`
- `Escalate`
- `Close`

### Footer
- Resolution history

---

## UI-017 Put-Away Workbench

### Header
- Page title
- Current location context

### Navigation
- Main navigation
- Inbound secondary navigation
- Breadcrumbs

### Main Content
- Pending put-away task queue
- Task detail section
- Destination confirmation section

### Forms
- Put-away fields: receipt reference, product, quantity, suggested location, actual location

### Tables
- Pending put-away table

### Action Buttons
- `Open Task`
- `Confirm Location`
- `Complete Put-Away`
- `Reassign Location`

### Footer
- Task completion timestamp

---

## UI-018 Non-PO and Return Receipt Intake

### Header
- Page title

### Navigation
- Main navigation
- Inbound secondary navigation
- Breadcrumbs

### Main Content
- Receipt type selector
- Intake form area
- Verification results area

### Forms
- Receipt type: non-PO / authorized return
- Reference fields: approval number / return authorization
- Verification fields: product, quantity, condition, notes

### Tables
- Optional received line items table

### Action Buttons
- `Start Intake`
- `Verify`
- `Confirm Receipt`
- `Cancel`

### Footer
- Intake transaction metadata

---

## UI-019 Inbound Supply Tracking

### Header
- Page title

### Navigation
- Main navigation
- Procurement secondary navigation
- Breadcrumbs

### Main Content
- Open inbound supply overview
- Delay status indicators
- PO detail drill-in panel

### Forms
- Filter controls: supplier, location, status, expected date range

### Tables
- Open PO/inbound supply table

### Action Buttons
- `View PO`
- `Update Delivery Status`
- `Refresh`

### Footer
- Data refresh timestamp

---

## UI-020 Inventory Status Monitor

### Header
- Page title
- Location/network scope

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Status summary cards
- Stock status board
- Detail drill-down area

### Forms
- Filter controls: location, category, product, status, ABC class

### Tables
- Inventory status table

### Action Buttons
- `View Detail`
- `Request Transfer`
- `Open Replenishment`
- `Create Adjustment`
- `Refresh`

### Footer
- Last reviewed/refresh timestamp

---

## UI-021 Inventory Availability Inquiry

### Header
- Page title

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Search panel
- Results list
- Availability detail view

### Forms
- Search fields: SKU, name, barcode, category
- Optional location scope selector

### Tables
- Product search results table
- Availability by location table

### Action Buttons
- `Search`
- `View Network Availability`
- `Reserve from Order`

### Footer
- Inquiry timestamp

---

## UI-022 Inventory Movement History

### Header
- Page title

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Search/filter region
- Movement list
- Transaction detail view

### Forms
- Filter fields: SKU, location, transaction type, user, date range

### Tables
- Movement history table

### Action Buttons
- `Search`
- `Open Transaction`
- `Export`

### Footer
- Export/query metadata

---

## UI-023 Cycle Count Workbench

### Header
- Page title
- Assigned user / location context

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Assigned count queue
- Count entry panel
- Submission confirmation area

### Forms
- Count entry fields: SKU, location, counted quantity, notes

### Tables
- Assigned cycle counts table

### Action Buttons
- `Open Count`
- `Submit Count`
- `Save Draft`

### Footer
- Assignment and submission timestamps

---

## UI-024 Physical Inventory Count Management

### Header
- Page title
- Count session status badge

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Count session summary
- Progress by area/team
- Zone/task breakdown
- Certification panel

### Forms
- Session fields: location, freeze start, count scope
- Certification fields: unresolved issues note, certifier

### Tables
- Count progress table
- Zone/team assignments table

### Action Buttons
- `Start Count`
- `Assign Teams`
- `Monitor Progress`
- `Certify Count`
- `Release Freeze`

### Footer
- Session audit metadata

---

## UI-025 Variance Investigation and Approval

### Header
- Page title
- Pending approvals count

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Variance queue
- Variance comparison panel
- Investigation notes and evidence area

### Forms
- Investigation form: root cause, notes, supporting evidence
- Approval form: decision, approver note

### Tables
- Variance cases table

### Action Buttons
- `Investigate`
- `Approve`
- `Reject`
- `Escalate`

### Footer
- Approval history

---

## UI-026 Stock Adjustment Management

### Header
- Page title

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Adjustment cases list
- Adjustment form
- Approval/status summary

### Forms
- Adjustment fields: product, location, direction, quantity, reason code, note

### Tables
- Adjustment cases table

### Action Buttons
- `Create Adjustment`
- `Submit`
- `Approve`
- `Reject`
- `Apply`

### Footer
- Adjustment audit metadata

---

## UI-027 Write-Off Authorization

### Header
- Page title

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Write-off request list
- Write-off request detail
- Evidence and finance acknowledgment section

### Forms
- Request fields: reason, quantity, value impact, evidence reference, finance note

### Tables
- Pending write-offs table

### Action Buttons
- `Review`
- `Approve`
- `Reject`
- `Request More Info`

### Footer
- Authorization metadata

---

## UI-028 Quarantine and Hold Register

### Header
- Page title

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Hold/quarantine register
- Selected hold detail
- Apply/release panel

### Forms
- Hold form: product, location, quantity, hold type, reason, expected disposition

### Tables
- Quarantine/hold table

### Action Buttons
- `Apply Hold`
- `Release Hold`
- `View Product`

### Footer
- Hold duration and update metadata

---

## UI-029 Shrinkage, Loss, and Obsolescence Analysis

### Header
- Page title

### Navigation
- Main navigation
- Inventory secondary navigation
- Breadcrumbs

### Main Content
- Trend summary cards
- Analysis charts/summary placeholders
- Recommendations section

### Forms
- Filter controls: date range, location, category, reason code

### Tables
- Shrinkage summary table
- Aging/obsolete items table

### Action Buttons
- `Apply Filters`
- `Export`
- `Open Adjustment Cases`

### Footer
- Report generation timestamp

---

## UI-030 Order Reservation Workbench

### Header
- Page title

### Navigation
- Main navigation
- Fulfillment secondary navigation
- Breadcrumbs

### Main Content
- Order search and queue
- Order line availability panel
- Reservation summary section

### Forms
- Search fields: order number, customer reference, date
- Reservation fields: location, quantity per line, release reason if applicable

### Tables
- Orders table
- Order line table

### Action Buttons
- `Check Availability`
- `Reserve Stock`
- `Release Reservation`
- `Open Split Fulfillment`

### Footer
- Reservation timestamps/status

---

## UI-031 Pick, Pack, and Ship Workbench

### Header
- Page title
- Location/shift context

### Navigation
- Main navigation
- Fulfillment secondary navigation
- Breadcrumbs

### Main Content
- Pick queue
- Pick verification panel
- Packing panel
- Shipment confirmation section

### Forms
- Verification fields: item scan, lot/batch, picked quantity
- Packing fields: package reference, carrier, notes

### Tables
- Pick queue table
- Pick line items table

### Action Buttons
- `Open Pick`
- `Verify Pick`
- `Pack`
- `Raise Exception`
- `Confirm Shipment`

### Footer
- Task/shipment metadata

---

## UI-032 Partial Fulfillment and Backorder Management

### Header
- Page title

### Navigation
- Main navigation
- Fulfillment secondary navigation
- Breadcrumbs

### Main Content
- Affected orders list
- Available vs ordered comparison
- Backorder plan section

### Forms
- Partial fulfillment fields: fulfill-now quantity, backorder quantity, customer acknowledgment note, expected date

### Tables
- Partial/backorder cases table

### Action Buttons
- `Confirm Partial Fulfillment`
- `Create Backorder`
- `Cancel Remainder`

### Footer
- Customer acknowledgment metadata

---

## UI-033 Fulfillment Exception Management

### Header
- Page title
- Open exceptions count

### Navigation
- Main navigation
- Fulfillment secondary navigation
- Breadcrumbs

### Main Content
- Exception queue
- Exception detail and context
- Resolution options panel

### Forms
- Resolution fields: resolution type, notes, reassignment, customer follow-up flag

### Tables
- Fulfillment exceptions table

### Action Buttons
- `Resolve`
- `Re-Pick`
- `Partial Ship`
- `Quarantine`
- `Route to Customer Service`

### Footer
- Resolution history

---

## UI-034 Order Fulfillment Status

### Header
- Page title

### Navigation
- Main navigation
- Fulfillment secondary navigation
- Breadcrumbs

### Main Content
- Order search area
- Order status summary
- Line-level progress view
- Shipment/backorder/exception detail tabs

### Forms
- Search fields: order ID, customer reference, date, status

### Tables
- Orders table
- Order lines status table

### Action Buttons
- `Search`
- `View Shipment`
- `View Exception`
- `View Backorder`

### Footer
- Live status timestamp

---

## UI-035 Multi-Location Split Fulfillment Planner

### Header
- Page title

### Navigation
- Main navigation
- Fulfillment secondary navigation
- Breadcrumbs

### Main Content
- Order shortage summary
- Proposed split allocation panel
- Location-specific reservation section

### Forms
- Allocation fields: source locations, quantities, shipping grouping, notes

### Tables
- Split allocation table

### Action Buttons
- `Generate Plan`
- `Adjust Allocation`
- `Confirm Split`
- `Release to Queues`

### Footer
- Plan creation metadata

---

## UI-036 Low-Stock Alert Review

### Header
- Page title
- Active alerts count

### Navigation
- Main navigation
- Procurement secondary navigation
- Breadcrumbs

### Main Content
- Alert priority summary
- Alert list
- Alert detail and recommended action panel

### Forms
- Filter controls: priority, location, category, status

### Tables
- Low-stock alerts table

### Action Buttons
- `Acknowledge`
- `Open Replenishment`
- `Create Transfer Request`
- `Refresh`

### Footer
- Alert generation timestamp

---

## UI-037 Replenishment Planning

### Header
- Page title

### Navigation
- Main navigation
- Procurement secondary navigation
- Breadcrumbs

### Main Content
- Recommendation list
- Network availability comparison
- Requisition creation panel

### Forms
- Replenishment fields: product, suggested quantity, final quantity, required date, supplier, destination

### Tables
- Recommendations table
- Open supply/network availability table

### Action Buttons
- `Create Requisition`
- `Adjust Quantity`
- `View Open PO`
- `Open Transfer Option`

### Footer
- Recommendation calculation timestamp

---

## UI-038 Transfer Request

### Header
- Page title

### Navigation
- Main navigation
- Transfers secondary navigation
- Breadcrumbs

### Main Content
- Transfer request form
- Source impact summary
- Request status panel

### Forms
- Transfer fields: source, destination, SKU, quantity, justification

### Tables
- Recent transfer requests table

### Action Buttons
- `Check Capacity`
- `Submit Request`
- `Save Draft`

### Footer
- Request tracking metadata

---

## UI-039 Transfer Approval Queue

### Header
- Page title
- Pending approvals count

### Navigation
- Main navigation
- Transfers secondary navigation
- Breadcrumbs

### Main Content
- Approval queue
- Selected request detail
- Source/destination impact comparison

### Forms
- Decision fields: approve/reject, approver note

### Tables
- Transfer approvals table

### Action Buttons
- `Approve`
- `Reject`
- `View Source Capacity`

### Footer
- Approval history

---

## UI-040 Transfer Execution and In-Transit Tracking

### Header
- Page title
- Location context

### Navigation
- Main navigation
- Transfers secondary navigation
- Breadcrumbs

### Main Content
- Approved dispatch queue
- In-transit tracking section
- Destination receipt confirmation section

### Forms
- Dispatch fields: transfer ID, picked quantity, lot/batch if applicable
- Receipt fields: quantity received, variance note

### Tables
- Transfer queue table
- In-transit transfers table

### Action Buttons
- `Dispatch`
- `Confirm Receipt`
- `Cancel Transfer`

### Footer
- Transit status metadata

---

## UI-041 Network Rebalancing Analysis

### Header
- Page title

### Navigation
- Main navigation
- Transfers secondary navigation
- Breadcrumbs

### Main Content
- Network imbalance summary
- Recommendations list
- Impact preview section

### Forms
- Filter controls: location pair, product category, date range

### Tables
- Rebalancing recommendations table

### Action Buttons
- `Generate Recommendation`
- `Create Transfer`
- `Export`

### Footer
- Analysis timestamp

---

## UI-042 Return Authorization Management

### Header
- Page title

### Navigation
- Main navigation
- Returns secondary navigation
- Breadcrumbs

### Main Content
- Order search panel
- Return eligibility panel
- Authorization detail section

### Forms
- Search fields: order number, customer reference
- Authorization fields: item, quantity, reason, authorization notes

### Tables
- Eligible return lines table
- Return authorizations table

### Action Buttons
- `Validate Eligibility`
- `Issue Authorization`
- `Cancel Authorization`

### Footer
- Authorization status metadata

---

## UI-043 Return Inspection and Disposition

### Header
- Page title

### Navigation
- Main navigation
- Returns secondary navigation
- Breadcrumbs

### Main Content
- Pending returns queue
- Receipt verification section
- Inspection section
- Disposition selection section

### Forms
- Receipt fields: authorization reference, quantity received
- Inspection fields: condition, notes
- Disposition fields: restock/quarantine/write-off, reason code

### Tables
- Pending returns table

### Action Buttons
- `Receive Return`
- `Record Inspection`
- `Confirm Disposition`

### Footer
- Return processing metadata

---

## UI-044 Operational Reports and Analytics

### Header
- Page title
- Report selector

### Navigation
- Main navigation
- Reports & Analytics secondary navigation
- Breadcrumbs

### Main Content
- Report filter bar
- Report result area
- Drill-down panel

### Forms
- Filter controls: report type, location, category, date range, status

### Tables
- Report output table

### Action Buttons
- `Run Report`
- `Export`
- `Open Detail`

### Footer
- Report run timestamp

---

## UI-045 Inventory Valuation Reconciliation

### Header
- Page title
- Period selector

### Navigation
- Main navigation
- Reports & Analytics secondary navigation
- Breadcrumbs

### Main Content
- Valuation summary cards
- Side-by-side comparison area
- Reconciliation notes section

### Forms
- Reconciliation fields: period, comment, variance explanation, status

### Tables
- Valuation comparison table
- Adjustment/variance detail table

### Action Buttons
- `Load Period`
- `Add Note`
- `Finalize Reconciliation`
- `Export`

### Footer
- Period close metadata

---

## UI-046 Promotional Stock Readiness

### Header
- Page title

### Navigation
- Main navigation
- Reports & Analytics secondary navigation
- Breadcrumbs

### Main Content
- Campaign selector
- Readiness summary cards
- Product readiness grid
- Gap/escalation section

### Forms
- Campaign fields: campaign, launch date, location scope
- Readiness confirmation fields: status, note, escalation reason

### Tables
- Campaign product readiness table

### Action Buttons
- `Check Readiness`
- `Confirm Readiness`
- `Escalate Gap`
- `Release Allocation`

### Footer
- Campaign readiness timestamp

---

## UI-047 Audit and Control Review Workspace

### Header
- Page title

### Navigation
- Main navigation
- Governance & Audit secondary navigation
- Breadcrumbs

### Main Content
- Audit scope setup area
- Sample/review workspace
- Findings panel

### Forms
- Scope fields: period, location, transaction type, reviewer
- Finding fields: issue type, severity, note, evidence reference

### Tables
- Reviewed transactions table
- Findings table

### Action Buttons
- `Start Review`
- `Record Finding`
- `Export Evidence`
- `Complete Review`

### Footer
- Audit session metadata

---

## UI-048 Audit Trail Query

### Header
- Page title

### Navigation
- Main navigation
- Governance & Audit secondary navigation
- Breadcrumbs

### Main Content
- Query filter panel
- Audit log result list
- Selected record before/after detail

### Forms
- Query fields: entity type, entity ID, user, date range, action type

### Tables
- Audit trail results table

### Action Buttons
- `Run Query`
- `Open Record`
- `Export Results`

### Footer
- Query/extract timestamp

---

## UI-049 User Account Management

### Header
- Page title
- Create user shortcut

### Navigation
- Main navigation
- Administration secondary navigation
- Breadcrumbs

### Main Content
- User directory
- User account detail panel
- Role assignment section

### Forms
- User fields: name, email, status, department
- Role assignment fields: role, location scope, effective status

### Tables
- Users table
- Role assignments table

### Action Buttons
- `Create User`
- `Save`
- `Suspend`
- `Deactivate`
- `Sync Users`

### Footer
- Account audit metadata

---

## UI-050 Role and Access Control Administration

### Header
- Page title

### Navigation
- Main navigation
- Administration secondary navigation
- Breadcrumbs

### Main Content
- Role list
- Permission matrix/detail panel
- Location scope rules section
- Conflict/SoD warning area

### Forms
- Role fields: role name, description, active status
- Permission fields: permission group, allow/deny, scope

### Tables
- Roles table
- Permissions matrix table

### Action Buttons
- `Edit Role`
- `Save Permissions`
- `Validate SoD`
- `Reset Changes`

### Footer
- Last updated metadata

---

## Notes

- These specifications are intentionally structural and low-fidelity.
- They should be used to create wireframes, not as final UI designs.
- Screen-level interaction states such as empty, loading, error, and success states should be added during detailed wireframe and prototype work.

