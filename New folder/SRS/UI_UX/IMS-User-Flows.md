# Inventory Management System User Flows

## Purpose

This document defines user flows for each major feature of the Inventory Management System. The flows are screen-oriented and are intended to support UX design, wireframes, interaction design, and future usability validation.

## Scope

The flows are based on the major features already identified across the BRD, use cases, screen inventory, navigation structure, and user journeys. Each flow includes:

1. Starting screen
2. User actions
3. Navigation path
4. Decision points
5. Destination screen

Each flow is represented as a text-based diagram from the user's perspective.

---

## 1. Product Catalog Management

- **Starting screen:** `Home > Products > Product Catalog`
- **User actions:** Search product, create product, edit product, update status, save record
- **Navigation path:** `Product Catalog -> Product Detail / Create Product -> Save -> Product Detail`
- **Decision points:** New product or existing product? Duplicate detected? Active, inactive, or discontinued?
- **Destination screen:** `Product Detail`

```text
Product Catalog
  -> Search by SKU / name / category
  -> [Decision: Product exists?]
     -> No -> Create Product
           -> Enter product attributes
           -> [Decision: Duplicate detected?]
              -> Yes -> Review duplicate resolution
              -> No -> Save
           -> Product Detail
     -> Yes -> Product Detail
           -> Edit Product
           -> Update attributes / status
           -> Save
           -> Product Detail
```

## 2. Product Import

- **Starting screen:** `Home > Products > Product Import`
- **User actions:** Download template, upload file, review validation, confirm import
- **Navigation path:** `Product Import -> Upload File -> Validation Results -> Import Completion`
- **Decision points:** File valid? Errors blocking import? Proceed with approved records only?
- **Destination screen:** `Import Completion`

```text
Product Import
  -> Upload File
  -> Validation Results
  -> [Decision: Validation passed?]
     -> No -> Correct file -> Re-upload
     -> Yes -> Confirm Import
           -> Import Completion
```

## 3. Location and Warehouse Management

- **Starting screen:** `Home > Locations > Location Directory`
- **User actions:** Create location, edit hierarchy, configure storage positions, activate location
- **Navigation path:** `Location Directory -> Location Detail -> Storage Positions / Hierarchy -> Activate`
- **Decision points:** New or existing location? Ready for activation? Opening balances complete?
- **Destination screen:** `Location Detail`

```text
Location Directory
  -> [Decision: Create new location?]
     -> Yes -> Create Location
           -> Enter location details
           -> Configure hierarchy
           -> Configure storage positions
           -> [Decision: Ready to activate?]
              -> No -> Save draft -> Location Detail
              -> Yes -> Activate Location
                     -> Location Detail
     -> No -> Location Detail
           -> Edit Hierarchy / Storage Positions / Status
           -> Save
           -> Location Detail
```

## 4. Stock Policy and Threshold Management

- **Starting screen:** `Home > Products > Stock Policies`
- **User actions:** Select product-location pair, review policy, update thresholds, save
- **Navigation path:** `Stock Policies -> Product-Location Policy Detail -> Save`
- **Decision points:** Use existing policy? Update reorder level? Adjust safety stock?
- **Destination screen:** `Product-Location Policy Detail`

```text
Stock Policies
  -> Search product and location
  -> Product-Location Policy Detail
  -> Update reorder level / minimum / safety stock
  -> [Decision: Values acceptable?]
     -> No -> Revise values
     -> Yes -> Save
           -> Product-Location Policy Detail
```

## 5. ABC Classification Management

- **Starting screen:** `Home > Products > ABC Classification`
- **User actions:** Review products, assign class, save classification
- **Navigation path:** `ABC Classification -> Classification Review -> Save`
- **Decision points:** Class A, B, or C? Reclassify now or defer?
- **Destination screen:** `ABC Classification`

```text
ABC Classification
  -> Review product performance indicators
  -> Select product
  -> Assign A / B / C class
  -> [Decision: Classification final?]
     -> No -> Continue review
     -> Yes -> Save
           -> ABC Classification
```

## 6. Governance Policies and Reason Codes

- **Starting screen:** `Home > Governance & Audit > Governance Policies`
- **User actions:** Create or update policy, manage reason code, publish changes
- **Navigation path:** `Governance Policies -> Policy Detail / Reason Code Detail -> Publish`
- **Decision points:** New policy or update? Retire reason code? Threshold change required?
- **Destination screen:** `Governance Policies`

```text
Governance Policies
  -> [Decision: Manage policy or reason code?]
     -> Policy -> Policy Detail
               -> Update thresholds / tolerances
               -> Publish
               -> Governance Policies
     -> Reason Code -> Reason Code Detail
                    -> Create / edit / retire code
                    -> Save
                    -> Governance Policies
```

## 7. Supplier Management

- **Starting screen:** `Home > Procurement > Suppliers`
- **User actions:** Search supplier, create supplier, edit terms, deactivate supplier
- **Navigation path:** `Suppliers -> Supplier Detail -> Save / Deactivate`
- **Decision points:** New or existing supplier? Supplier still active?
- **Destination screen:** `Supplier Detail`

```text
Suppliers
  -> Search supplier
  -> [Decision: Supplier exists?]
     -> No -> Create Supplier
           -> Enter supplier details
           -> Save
           -> Supplier Detail
     -> Yes -> Supplier Detail
           -> Edit terms / lead time / status
           -> [Decision: Deactivate supplier?]
              -> Yes -> Confirm deactivation -> Supplier Detail
              -> No -> Save updates -> Supplier Detail
```

## 8. Purchase Requisition Management

- **Starting screen:** `Home > Procurement > Purchase Requisitions`
- **User actions:** Review requisition, approve, reject, convert to PO
- **Navigation path:** `Purchase Requisitions -> Requisition Detail -> Approve / Reject / Convert`
- **Decision points:** Approve or reject? Ready to convert to PO?
- **Destination screen:** `Requisition Detail` or `Purchase Order Detail`

```text
Purchase Requisitions
  -> Select requisition
  -> Requisition Detail
  -> [Decision: Approve?]
     -> No -> Reject with reason
           -> Requisition Detail
     -> Yes -> Approve
           -> [Decision: Convert to PO now?]
              -> No -> Requisition Detail
              -> Yes -> Convert to PO
                     -> Purchase Order Detail
```

## 9. Purchase Order Management

- **Starting screen:** `Home > Procurement > Purchase Orders`
- **User actions:** Create PO, edit PO, cancel PO, review open PO
- **Navigation path:** `Purchase Orders -> Purchase Order Detail -> Save / Cancel`
- **Decision points:** Create from requisition or manual? Amend or cancel?
- **Destination screen:** `Purchase Order Detail`

```text
Purchase Orders
  -> [Decision: Create new PO?]
     -> Yes -> Create Purchase Order
           -> Enter supplier / lines / dates
           -> Save
           -> Purchase Order Detail
     -> No -> Purchase Order Detail
           -> [Decision: Amend or cancel?]
              -> Amend -> Update lines / dates -> Save -> Purchase Order Detail
              -> Cancel -> Confirm cancel -> Purchase Order Detail
```

## 10. Inbound Delivery Planning

- **Starting screen:** `Home > Procurement > Inbound Delivery Planning`
- **User actions:** Select PO, update expected delivery, confirm plan
- **Navigation path:** `Inbound Delivery Planning -> Purchase Order Detail -> Save expected delivery`
- **Decision points:** Delivery confirmed? Delay or change received?
- **Destination screen:** `Inbound Delivery Planning`

```text
Inbound Delivery Planning
  -> Select purchase order
  -> Review expected delivery
  -> Update shipment date / carrier / destination
  -> [Decision: Delivery plan final?]
     -> No -> Continue editing
     -> Yes -> Save
           -> Inbound Delivery Planning
```

## 11. Goods Receipt Workbench

- **Starting screen:** `Home > Inbound > Goods Receipt Workbench`
- **User actions:** Open expected receipt, verify items, confirm receipt
- **Navigation path:** `Goods Receipt Workbench -> Goods Receipt Detail -> Verify -> Send to Put-Away`
- **Decision points:** PO match? Traceability data required? Discrepancy found?
- **Destination screen:** `Goods Receipt Detail`

```text
Goods Receipt Workbench
  -> Select arriving shipment
  -> Goods Receipt Detail
  -> Scan / verify items and quantities
  -> [Decision: Discrepancy found?]
     -> Yes -> Receipt Discrepancy Detail
           -> Resolve / document
           -> Return to Goods Receipt Detail
     -> No -> Confirm Receipt
           -> Send to Put-Away
           -> Goods Receipt Detail
```

## 12. Receipt Discrepancy Resolution

- **Starting screen:** `Home > Inbound > Receipt Discrepancies`
- **User actions:** Select discrepancy, review, resolve, close
- **Navigation path:** `Receipt Discrepancies -> Discrepancy Detail -> Resolve`
- **Decision points:** Accept quantity? Escalate? Hold for supplier follow-up?
- **Destination screen:** `Discrepancy Detail`

```text
Receipt Discrepancies
  -> Select discrepancy
  -> Discrepancy Detail
  -> Review variance and notes
  -> [Decision: Resolve now?]
     -> No -> Leave open / escalate
     -> Yes -> Record resolution
           -> Close discrepancy
           -> Discrepancy Detail
```

## 13. Put-Away Workbench

- **Starting screen:** `Home > Inbound > Put-Away Workbench`
- **User actions:** Select task, move stock, confirm location, complete task
- **Navigation path:** `Put-Away Workbench -> Put-Away Task Detail -> Confirm`
- **Decision points:** Suggested location valid? Rotation rule applies? Quantity mismatch?
- **Destination screen:** `Put-Away Task Detail`

```text
Put-Away Workbench
  -> Select pending task
  -> Put-Away Task Detail
  -> Move goods to storage
  -> Confirm quantity and destination
  -> [Decision: Location / quantity valid?]
     -> No -> Correct issue / choose alternate location
     -> Yes -> Complete Put-Away
           -> Put-Away Task Detail
```

## 14. Inventory Status Monitor

- **Starting screen:** `Home > Inventory > Inventory Status Monitor`
- **User actions:** Filter results, drill into stock detail, route next action
- **Navigation path:** `Inventory Status Monitor -> Product Stock Detail / Location Stock Detail -> Related action`
- **Decision points:** Low stock? Overstock? Investigate, transfer, replenish, or adjust?
- **Destination screen:** `Product Stock Detail`, `Transfer Request`, `Replenishment Planning`, or `Stock Adjustments`

```text
Inventory Status Monitor
  -> Filter by location / status / category
  -> Review stock board
  -> Select product or location
  -> Product Stock Detail
  -> [Decision: What action is needed?]
     -> Replenish -> Replenishment Planning
     -> Transfer -> Transfer Request
     -> Investigate -> Movement History
     -> Correct stock -> Stock Adjustments
```

## 15. Availability Inquiry

- **Starting screen:** `Home > Inventory > Availability Inquiry`
- **User actions:** Search product, view ATP, check network availability
- **Navigation path:** `Availability Inquiry -> Search Results -> Network Availability Detail`
- **Decision points:** Enough ATP? Need network view? Customer-ready answer available?
- **Destination screen:** `Network Availability Detail`

```text
Availability Inquiry
  -> Search product
  -> Search Results
  -> Select product
  -> View ATP / reserved / on-hand
  -> [Decision: Need network availability?]
     -> No -> Respond to customer
     -> Yes -> Network Availability Detail
                -> Respond to customer
```

## 16. Cycle Count Workbench

- **Starting screen:** `Home > Inventory > Cycle Counts`
- **User actions:** Open assigned count, enter quantity, submit result
- **Navigation path:** `Cycle Counts -> Count Submission -> Submit`
- **Decision points:** Count confident? Recount needed? Variance expected?
- **Destination screen:** `Cycle Counts`

```text
Cycle Counts
  -> Select assigned count
  -> Count Submission
  -> Enter physical quantity
  -> [Decision: Recount needed?]
     -> Yes -> Recount -> Enter revised quantity
     -> No -> Submit
           -> Cycle Counts
```

## 17. Physical Count Management

- **Starting screen:** `Home > Inventory > Physical Counts`
- **User actions:** Start count, monitor progress, certify count
- **Navigation path:** `Physical Counts -> Count Session Detail -> Count Certification`
- **Decision points:** Freeze location? All areas counted? Certify now?
- **Destination screen:** `Count Certification`

```text
Physical Counts
  -> Start new count session
  -> Count Session Detail
  -> Monitor zones / teams / progress
  -> [Decision: Count complete?]
     -> No -> Continue counting
     -> Yes -> Count Certification
           -> Confirm certification
           -> Count Certification
```

## 18. Variance Investigation and Approval

- **Starting screen:** `Home > Inventory > Variance Approvals`
- **User actions:** Select variance, investigate, approve or reject
- **Navigation path:** `Variance Approvals -> Variance Investigation Detail -> Approval result`
- **Decision points:** Root cause clear? Approval threshold exceeded? Approve or reject?
- **Destination screen:** `Variance Investigation Detail`

```text
Variance Approvals
  -> Select variance case
  -> Variance Investigation Detail
  -> Review evidence / notes / quantity gap
  -> [Decision: Approve variance?]
     -> No -> Reject / escalate
           -> Variance Investigation Detail
     -> Yes -> Approve
           -> Route to Stock Adjustment
           -> Variance Investigation Detail
```

## 19. Stock Adjustment Management

- **Starting screen:** `Home > Inventory > Stock Adjustments`
- **User actions:** Create adjustment, select reason code, submit, approve if needed
- **Navigation path:** `Stock Adjustments -> Adjustment Case Detail -> Submit -> Approval / Apply`
- **Decision points:** Increase or decrease? Threshold approval needed? Apply now?
- **Destination screen:** `Adjustment Case Detail`

```text
Stock Adjustments
  -> Create Adjustment
  -> Adjustment Case Detail
  -> Enter quantity and reason code
  -> Submit
  -> [Decision: Approval required?]
     -> No -> Apply adjustment -> Adjustment Case Detail
     -> Yes -> Pending approval
           -> Approval result
           -> [Decision: Approved?]
              -> No -> Adjustment Case Detail
              -> Yes -> Apply adjustment -> Adjustment Case Detail
```

## 20. Write-Off Authorization

- **Starting screen:** `Home > Inventory > Write-Offs`
- **User actions:** Review request, inspect evidence, approve or reject
- **Navigation path:** `Write-Offs -> Write-Off Authorization Detail -> Approve / Reject`
- **Decision points:** Evidence sufficient? Finance acknowledgment needed? Approve?
- **Destination screen:** `Write-Off Authorization Detail`

```text
Write-Offs
  -> Select write-off request
  -> Write-Off Authorization Detail
  -> Review evidence / quantity / reason
  -> [Decision: Approve write-off?]
     -> No -> Reject
           -> Write-Off Authorization Detail
     -> Yes -> [Decision: Finance acknowledgment required?]
              -> Yes -> Await finance acknowledgment
              -> No -> Continue
           -> Approve and execute
           -> Write-Off Authorization Detail
```

## 21. Quarantine and Hold Register

- **Starting screen:** `Home > Inventory > Quarantine & Holds`
- **User actions:** Select stock, apply hold, release hold, view hold detail
- **Navigation path:** `Quarantine & Holds -> Hold Detail -> Apply / Release`
- **Decision points:** Apply hold or release? Quarantine or temporary hold?
- **Destination screen:** `Hold Detail`

```text
Quarantine & Holds
  -> Search product / location
  -> Hold Detail
  -> [Decision: Apply new hold or release existing hold?]
     -> Apply -> Select quantity / reason / type
             -> Confirm
             -> Hold Detail
     -> Release -> Review hold
               -> Confirm release
               -> Hold Detail
```

## 22. Order Reservation

- **Starting screen:** `Home > Fulfillment > Order Reservation`
- **User actions:** Open order, confirm availability, reserve stock, release if needed
- **Navigation path:** `Order Reservation -> Order Reservation Detail -> Reserve / Release`
- **Decision points:** ATP sufficient? Which location? Reservation or release?
- **Destination screen:** `Order Reservation Detail`

```text
Order Reservation
  -> Search / open order
  -> Order Reservation Detail
  -> Check availability
  -> [Decision: Enough ATP?]
     -> No -> Partial Fulfillment & Backorders
     -> Yes -> Select fulfillment location
           -> Reserve stock
           -> [Decision: Order changed / canceled later?]
              -> Yes -> Release reservation
              -> No -> Continue to warehouse queue
           -> Order Reservation Detail
```

## 23. Pick / Pack / Ship

- **Starting screen:** `Home > Fulfillment > Pick / Pack / Ship`
- **User actions:** Open pick queue, verify pick, pack order, confirm shipment
- **Navigation path:** `Pick Queue -> Pick Verification -> Packing -> Shipment Confirmation`
- **Decision points:** Pick mismatch? Raise exception? Shipment complete?
- **Destination screen:** `Shipment Confirmation`

```text
Pick / Pack / Ship
  -> Pick Queue
  -> Select order
  -> Pick Verification
  -> [Decision: Pick successful?]
     -> No -> Fulfillment Exception Detail
     -> Yes -> Packing
           -> Shipment Confirmation
           -> Confirm ship
           -> Shipment Confirmation
```

## 24. Partial Fulfillment and Backorders

- **Starting screen:** `Home > Fulfillment > Partial Fulfillment & Backorders`
- **User actions:** Open affected order, confirm partial plan, create backorder
- **Navigation path:** `Partial Fulfillment & Backorders -> Backorder Detail -> Confirm`
- **Decision points:** Customer accepts partial? Backorder or cancel remainder?
- **Destination screen:** `Backorder Detail`

```text
Partial Fulfillment & Backorders
  -> Select affected order
  -> Review available vs ordered quantity
  -> [Decision: Customer accepts partial fulfillment?]
     -> No -> Cancel or revise order
     -> Yes -> Confirm immediate shipment quantity
           -> Create backorder for remainder
           -> Backorder Detail
```

## 25. Fulfillment Exception Management

- **Starting screen:** `Home > Fulfillment > Fulfillment Exceptions`
- **User actions:** Open exception, choose resolution, route order
- **Navigation path:** `Fulfillment Exceptions -> Exception Detail -> Resolve`
- **Decision points:** Re-pick, partial ship, quarantine, substitute, or return to service team?
- **Destination screen:** `Exception Detail`

```text
Fulfillment Exceptions
  -> Select exception
  -> Exception Detail
  -> Review issue
  -> [Decision: Resolution path?]
     -> Re-pick -> Return to Pick Queue
     -> Partial ship -> Partial Fulfillment & Backorders
     -> Quarantine -> Quarantine & Holds
     -> Customer follow-up -> Order Status
```

## 26. Order Status Inquiry

- **Starting screen:** `Home > Fulfillment > Order Status`
- **User actions:** Search order, view status, drill into shipment or exception
- **Navigation path:** `Order Status -> Order Detail -> Shipment / Exception / Backorder detail`
- **Decision points:** Need shipment detail? Need backorder detail? Need customer follow-up?
- **Destination screen:** `Order Detail`

```text
Order Status
  -> Search order
  -> Order Detail
  -> Review line status
  -> [Decision: Need deeper detail?]
     -> Shipment -> Shipment Confirmation
     -> Exception -> Exception Detail
     -> Backorder -> Backorder Detail
     -> No -> Order Detail
```

## 27. Multi-Location Fulfillment

- **Starting screen:** `Home > Fulfillment > Multi-Location Fulfillment`
- **User actions:** Open order, generate split plan, confirm allocation, release to locations
- **Navigation path:** `Multi-Location Fulfillment -> Split Fulfillment Plan -> Release`
- **Decision points:** Single location enough? Accept split plan? Adjust allocation?
- **Destination screen:** `Split Fulfillment Plan`

```text
Multi-Location Fulfillment
  -> Open order with shortage
  -> Generate split plan
  -> Split Fulfillment Plan
  -> [Decision: Accept proposed allocation?]
     -> No -> Adjust location quantities
     -> Yes -> Confirm
           -> Release to warehouse queues
           -> Split Fulfillment Plan
```

## 28. Low-Stock Alert Review

- **Starting screen:** `Home > Procurement > Low-Stock Alerts`
- **User actions:** Review alert, acknowledge, open related action
- **Navigation path:** `Low-Stock Alerts -> Alert Detail -> Replenishment Planning / Transfer Request`
- **Decision points:** Replenish, transfer, or monitor?
- **Destination screen:** `Alert Detail` or related action screen

```text
Low-Stock Alerts
  -> Select alert
  -> Alert Detail
  -> Review stock / threshold / open supply
  -> [Decision: Best next action?]
     -> Replenish -> Replenishment Planning
     -> Transfer -> Transfer Request
     -> Monitor -> Acknowledge alert -> Alert Detail
```

## 29. Replenishment Planning

- **Starting screen:** `Home > Procurement > Replenishment Planning`
- **User actions:** Review recommendation, create requisition, submit for approval
- **Navigation path:** `Replenishment Planning -> Replenishment Recommendation Detail -> Purchase Requisition`
- **Decision points:** Transfer-before-buy? Recommended quantity accepted? Submit now?
- **Destination screen:** `Requisition Detail`

```text
Replenishment Planning
  -> Review recommendations
  -> Replenishment Recommendation Detail
  -> [Decision: Transfer can solve need?]
     -> Yes -> Transfer Request
     -> No -> Create Purchase Requisition
           -> Submit for approval
           -> Requisition Detail
```

## 30. Transfer Request

- **Starting screen:** `Home > Transfers > Transfer Requests`
- **User actions:** Create request, select source and destination, submit
- **Navigation path:** `Transfer Requests -> Transfer Request Detail -> Submit`
- **Decision points:** Best source location? Quantity acceptable? Submit for approval?
- **Destination screen:** `Transfer Request Detail`

```text
Transfer Requests
  -> Create transfer request
  -> Transfer Request Detail
  -> Select source / destination / SKU / quantity
  -> Review transfer impact
  -> [Decision: Submit request?]
     -> No -> Save draft / cancel
     -> Yes -> Submit
           -> Transfer Request Detail
```

## 31. Transfer Approval

- **Starting screen:** `Home > Transfers > Transfer Approvals`
- **User actions:** Open request, review impact, approve or reject
- **Navigation path:** `Transfer Approvals -> Approval Detail -> Approve / Reject`
- **Decision points:** Protect source threshold? Approve?
- **Destination screen:** `Approval Detail`

```text
Transfer Approvals
  -> Select pending transfer
  -> Approval Detail
  -> Review source and destination impact
  -> [Decision: Approve transfer?]
     -> No -> Reject
           -> Approval Detail
     -> Yes -> Approve
           -> Approval Detail
```

## 32. Transfer Execution

- **Starting screen:** `Home > Transfers > Transfer Execution`
- **User actions:** Dispatch stock, receive stock, confirm completion
- **Navigation path:** `Transfer Execution -> Dispatch Detail -> Receipt Detail`
- **Decision points:** Dispatch correct quantity? Destination receives full quantity?
- **Destination screen:** `Receipt Detail`

```text
Transfer Execution
  -> Select approved transfer
  -> Dispatch Detail
  -> Pick and verify transfer stock
  -> Confirm dispatch
  -> Receipt Detail
  -> [Decision: Destination received full transfer?]
     -> No -> Investigate discrepancy
     -> Yes -> Confirm receipt
           -> Receipt Detail
```

## 33. Network Rebalancing Analysis

- **Starting screen:** `Home > Transfers > Network Rebalancing`
- **User actions:** Review imbalances, select recommendation, generate transfer request
- **Navigation path:** `Network Rebalancing -> Rebalancing Recommendation Detail -> Transfer Request`
- **Decision points:** Recommendation valid? Approve recommendation now?
- **Destination screen:** `Transfer Request Detail`

```text
Network Rebalancing
  -> Review imbalance dashboard
  -> Select recommendation
  -> Rebalancing Recommendation Detail
  -> [Decision: Approve recommendation?]
     -> No -> Return to dashboard
     -> Yes -> Generate transfer request
           -> Transfer Request Detail
```

## 34. Return Authorization Management

- **Starting screen:** `Home > Returns > Return Authorizations`
- **User actions:** Search order, validate return, issue authorization
- **Navigation path:** `Return Authorizations -> Return Authorization Detail -> Issue authorization`
- **Decision points:** Return eligible? Quantity allowed? Approve return?
- **Destination screen:** `Return Authorization Detail`

```text
Return Authorizations
  -> Search original order
  -> Return Authorization Detail
  -> Select items and quantity
  -> Validate return reason / policy
  -> [Decision: Eligible return?]
     -> No -> Decline request
     -> Yes -> Issue authorization
           -> Return Authorization Detail
```

## 35. Return Inspection and Disposition

- **Starting screen:** `Home > Returns > Return Inspection & Disposition`
- **User actions:** Receive return, inspect item, select disposition
- **Navigation path:** `Return Inspection & Disposition -> Return Receipt Detail -> Inspection Detail -> Disposition Detail`
- **Decision points:** Authorized return? Resalable, quarantine, or write-off?
- **Destination screen:** `Disposition Detail`

```text
Return Inspection & Disposition
  -> Select pending return
  -> Return Receipt Detail
  -> Verify received quantity
  -> Inspection Detail
  -> Assess condition
  -> [Decision: Disposition?]
     -> Restock -> Confirm restock
     -> Quarantine -> Quarantine & Holds
     -> Write-off -> Write-Off Authorization Detail
  -> Disposition Detail
```

## 36. Operational Reports and Analytics

- **Starting screen:** `Home > Reports & Analytics > Operational Reports`
- **User actions:** Select report, filter results, drill down, export
- **Navigation path:** `Operational Reports -> Report View -> Detail / Export`
- **Decision points:** Which report? Need drill-down? Export needed?
- **Destination screen:** `Report View`

```text
Operational Reports
  -> Select report type
  -> Report View
  -> Apply filters
  -> Review results
  -> [Decision: Need drill-down?]
     -> Yes -> Detail View
     -> No -> Continue
  -> [Decision: Export report?]
     -> Yes -> Export
     -> No -> Report View
```

## 37. Executive KPI Dashboard

- **Starting screen:** `Home > Executive KPI Dashboard`
- **User actions:** Change period, review KPIs, drill into issue
- **Navigation path:** `Executive KPI Dashboard -> KPI Detail -> Supporting report`
- **Decision points:** KPI on target? Drill into underperformance?
- **Destination screen:** `KPI Detail` or supporting analytics view

```text
Executive KPI Dashboard
  -> Select reporting period
  -> Review KPIs and trends
  -> [Decision: KPI underperforming?]
     -> No -> Continue review
     -> Yes -> KPI Detail
           -> Open supporting report / analysis
```

## 38. Inventory Valuation Reconciliation

- **Starting screen:** `Home > Reports & Analytics > Valuation Reconciliation`
- **User actions:** Select period, compare values, document notes, finalize
- **Navigation path:** `Valuation Reconciliation -> Reconciliation Detail -> Finalize`
- **Decision points:** Variance acceptable? Need deeper investigation?
- **Destination screen:** `Reconciliation Detail`

```text
Valuation Reconciliation
  -> Select period
  -> Reconciliation Detail
  -> Compare operational vs finance view
  -> [Decision: Variance within tolerance?]
     -> Yes -> Finalize reconciliation
     -> No -> Investigate underlying drivers
           -> Document notes
           -> Finalize or escalate
```

## 39. Promotional Stock Readiness

- **Starting screen:** `Home > Reports & Analytics > Promotional Readiness`
- **User actions:** Open campaign, review readiness, confirm or escalate
- **Navigation path:** `Promotional Readiness -> Campaign Detail -> Confirm readiness / Escalate`
- **Decision points:** Stock sufficient? Inbound closes gap? Ready to confirm?
- **Destination screen:** `Campaign Detail`

```text
Promotional Readiness
  -> Select campaign
  -> Campaign Detail
  -> Review allocated / ring-fenced / inbound supply
  -> [Decision: Campaign stock ready?]
     -> No -> Escalate gap / update plan
     -> Yes -> Confirm readiness
           -> Campaign Detail
```

## 40. Audit Workspace

- **Starting screen:** `Home > Governance & Audit > Audit Workspace`
- **User actions:** Define scope, review records, document findings, export evidence
- **Navigation path:** `Audit Workspace -> Audit Review Detail -> Export`
- **Decision points:** Control issue found? Sample more records? Export evidence?
- **Destination screen:** `Audit Review Detail`

```text
Audit Workspace
  -> Define scope
  -> Audit Review Detail
  -> Review transactions / approvals / controls
  -> [Decision: Finding identified?]
     -> No -> Continue sampling / close review
     -> Yes -> Document finding
  -> [Decision: Export evidence?]
     -> Yes -> Export package
     -> No -> Audit Review Detail
```

## 41. Audit Trail Query

- **Starting screen:** `Home > Governance & Audit > Audit Trail Query`
- **User actions:** Enter search criteria, review log entries, inspect record details, export
- **Navigation path:** `Audit Trail Query -> Audit Record Detail -> Export`
- **Decision points:** Results found? Need before/after detail? Export required?
- **Destination screen:** `Audit Record Detail`

```text
Audit Trail Query
  -> Enter search criteria
  -> Review results
  -> [Decision: Matching records found?]
     -> No -> Refine search
     -> Yes -> Audit Record Detail
           -> Review before / after state
           -> [Decision: Export results?]
              -> Yes -> Export
              -> No -> Audit Record Detail
```

## 42. User Account Management

- **Starting screen:** `Home > Administration > User Accounts`
- **User actions:** Create user, edit user, assign role, suspend or deactivate account
- **Navigation path:** `User Accounts -> User Account Detail -> Save / Suspend / Deactivate`
- **Decision points:** New or existing user? Change role? Suspend or deactivate?
- **Destination screen:** `User Account Detail`

```text
User Accounts
  -> Search user
  -> [Decision: Existing user?]
     -> No -> Create User
           -> Enter profile and scope
           -> Save
           -> User Account Detail
     -> Yes -> User Account Detail
           -> Edit user / assign role / change scope
           -> [Decision: Suspend or deactivate?]
              -> Suspend -> Confirm -> User Account Detail
              -> Deactivate -> Confirm -> User Account Detail
              -> Neither -> Save changes -> User Account Detail
```

## 43. Roles and Access Control

- **Starting screen:** `Home > Administration > Roles & Access Control`
- **User actions:** Open role, review permissions, update scope rules, save
- **Navigation path:** `Roles & Access Control -> Role Permission Detail -> Save`
- **Decision points:** Permission conflict? Location scope valid? SoD breach?
- **Destination screen:** `Role Permission Detail`

```text
Roles & Access Control
  -> Select role
  -> Role Permission Detail
  -> Review permissions and location scope
  -> [Decision: SoD conflict detected?]
     -> Yes -> Revise permissions / scope
     -> No -> Save
           -> Role Permission Detail
```

---

## Notes

- These flows focus on major features rather than every minor interaction.
- Flows are aligned to previously defined screens and navigation structure.
- The diagrams can be used directly as the basis for task flows, page transitions, and low-fidelity UX design.

