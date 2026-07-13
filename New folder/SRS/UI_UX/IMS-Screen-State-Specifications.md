# Inventory Management System Screen State Specifications

## Purpose

This document defines the expected user experience for key screen states across every Inventory Management System screen. It covers:

1. Loading state
2. Empty state
3. Error state
4. Success state
5. No-permission state

The goal is to ensure every screen behaves consistently and gives users clear guidance when data is loading, absent, successful, blocked, or unavailable.

## Shared UX Principles

- **Loading:** Preserve page structure with skeletons or placeholders so users understand what is coming.
- **Empty:** Explain why nothing is shown and what the user can do next.
- **Error:** State what went wrong in user language, preserve work where possible, and offer recovery.
- **Success:** Confirm completion clearly and update the affected data or workflow immediately.
- **No-permission:** Explain access limits without exposing sensitive detail and point users to the right next action.

---

## UI-001 Sign In / Session Entry

### Loading state
- Show a disabled sign-in button with inline spinner after submit.
- Keep username visible and mask password.
- Message: `Signing you in...`

### Empty state
- Not applicable as a data state.
- Default first-load experience acts as the neutral state.

### Error state
- Show a form-level error for invalid credentials or session problems.
- Preserve username/email; clear password.
- Offer retry and help link.

### Success state
- Show brief transition feedback such as `Sign-in successful`.
- Redirect immediately to the correct landing screen.

### No-permission state
- If authentication succeeds but the account has no usable access, show:
  - `Your account is active, but no application access has been assigned.`
  - Action: `Contact Administrator`

---

## UI-002 Operational Home Dashboard

### Loading state
- Show skeleton KPI cards, placeholder alert rows, and shortcut tile skeletons.
- Keep page header and navigation visible.

### Empty state
- If there are no alerts or tasks, show:
  - `You are up to date.`
  - Explain that no urgent items or pending tasks exist.

### Error state
- Show banner: `We could not load the dashboard right now.`
- Keep navigation available.
- Offer `Retry`.

### Success state
- After refresh or task completion, show a non-blocking success banner:
  - `Dashboard updated successfully.`

### No-permission state
- If user can access home but not some widgets, show available widgets and replace restricted ones with:
  - `You do not have access to this data.`

---

## UI-003 Executive KPI Dashboard

### Loading state
- Show KPI card skeletons and trend placeholders.
- Preserve selected period if already chosen.

### Empty state
- Show:
  - `No KPI data is available for the selected period.`
  - Suggest changing period or scope.

### Error state
- Show banner: `KPI data could not be loaded.`
- Keep filters intact.
- Offer `Retry`.

### Success state
- After filters change, update KPI cards and show subtle confirmation:
  - `Dashboard updated.`

### No-permission state
- Show:
  - `You do not have permission to view executive KPI data.`
  - Offer return to `Home`.

---

## UI-004 Notification Center

### Loading state
- Show placeholder notification rows and a blank detail pane with shimmer state.

### Empty state
- Show:
  - `No notifications to review.`
  - Explain that alerts, approvals, and operational notices will appear here.

### Error state
- Show:
  - `Notifications could not be loaded.`
  - Preserve current filters if any.

### Success state
- After acknowledge/handle:
  - Remove or update the item in place.
  - Show `Notification updated.`

### No-permission state
- Show:
  - `You do not have permission to view this notification set.`
  - If partial access exists, show only allowed items.

---

## UI-005 Product Catalog Management

### Loading state
- Show product table skeleton and product detail placeholder.
- Keep search/filter bar visible.

### Empty state
- If catalog is empty:
  - `No products have been created yet.`
  - Primary action: `Create Product`
- If search returns no matches:
  - `No products match these filters.`

### Error state
- For catalog load failure:
  - `Products could not be loaded.`
- For save failure:
  - Preserve form values and show inline plus banner errors.

### Success state
- After create/update:
  - Show `Product saved successfully.`
  - Refresh detail and table row.

### No-permission state
- Read-only users see product data without edit actions.
- Fully blocked users see:
  - `You do not have permission to manage products.`

---

## UI-006 Product Import Workspace

### Loading state
- Show step progress placeholder, upload area active, validation/result panels skeletonized while processing.

### Empty state
- Show:
  - `No import file uploaded yet.`
  - Provide template guidance and upload prompt.

### Error state
- If file-level failure:
  - `The import could not be processed.`
- If validation fails:
  - Keep file summary and display row-level issues clearly.

### Success state
- Show created/updated counts and any non-blocking warnings.
- Message: `Import completed successfully.`

### No-permission state
- Show:
  - `You do not have permission to import product data.`
  - Hide upload control.

---

## UI-007 Location and Warehouse Management

### Loading state
- Show location list skeleton, hierarchy tree placeholders, and empty detail shell.

### Empty state
- `No locations have been configured yet.`
- Primary action: `Create Location`

### Error state
- On load: `Locations could not be loaded.`
- On save/activate/close: preserve edits and show relevant field or business-rule errors.

### Success state
- `Location saved successfully.`
- `Location activated successfully.` or equivalent action-specific feedback.

### No-permission state
- Show read-only location directory if view-only access exists.
- Otherwise show blocked-state message with return navigation.

---

## UI-008 Stock Policy and Threshold Management

### Loading state
- Show filter shell and policy-detail skeleton.

### Empty state
- `No stock policy exists for this product and location.`
- Action: `Create Policy`

### Error state
- Show invalid threshold relationships inline.
- For load failures, preserve current filter values.

### Success state
- `Stock policy saved successfully.`
- Refresh effective thresholds summary.

### No-permission state
- `You do not have permission to manage stock policies.`

---

## UI-009 ABC Classification Management

### Loading state
- Show classification table skeleton and summary placeholders.

### Empty state
- `No products are available for classification in this view.`
- Suggest adjusting filters.

### Error state
- `Classifications could not be loaded.`
- Save errors preserve class selections.

### Success state
- `Classification updated successfully.`
- Updated class appears immediately in the list.

### No-permission state
- `You do not have permission to manage ABC classifications.`

---

## UI-010 Governance Policies and Reason Codes

### Loading state
- Show tabs and table skeletons; keep module shell visible.

### Empty state
- Policies tab: `No governance policies have been published yet.`
- Reason codes tab: `No reason codes are available yet.`

### Error state
- `Governance data could not be loaded.`
- Publish/update failures preserve draft values.

### Success state
- `Policy published successfully.` or `Reason code saved successfully.`

### No-permission state
- If read-only audit access exists, disable editing and publishing.
- Otherwise show blocked-state panel.

---

## UI-011 Supplier Management

### Loading state
- Show supplier table skeleton and detail placeholder.

### Empty state
- `No suppliers have been added yet.`
- Primary action: `Create Supplier`

### Error state
- `Suppliers could not be loaded.`
- Save/deactivate errors preserve the form.

### Success state
- `Supplier saved successfully.`
- Deactivation uses action-specific confirmation.

### No-permission state
- `You do not have permission to manage suppliers.`

---

## UI-012 Purchase Order Management

### Loading state
- Show PO table skeleton and line-item placeholder rows.

### Empty state
- Default list:
  - `No purchase orders found.`
  - Action: `Create Purchase Order`
- Filtered view:
  - `No purchase orders match the selected filters.`

### Error state
- Load error: `Purchase orders could not be loaded.`
- Save/amend/cancel errors preserve all draft line items.

### Success state
- `Purchase order saved successfully.`
- `Purchase order canceled successfully.` as applicable.

### No-permission state
- View-only users can inspect orders without edit actions.
- No-access users see a blocked-state panel.

---

## UI-013 Purchase Requisition Management

### Loading state
- Show requisition queue skeleton and detail pane placeholder.

### Empty state
- `No requisitions are available in this view.`
- If user has create access, show `Create Requisition`.

### Error state
- `Requisitions could not be loaded.`
- Approval/rejection/conversion failures preserve decision notes.

### Success state
- `Requisition submitted successfully.`
- `Requisition approved successfully.`
- `Purchase order created successfully.` when converted.

### No-permission state
- `You do not have permission to manage requisitions.`

---

## UI-014 Inbound Delivery Planning

### Loading state
- Show inbound schedule table skeleton and selected delivery detail placeholder.

### Empty state
- `No inbound deliveries are scheduled for this view.`
- Suggest selecting a different period or open PO set.

### Error state
- `Inbound delivery plans could not be loaded.`
- Save errors preserve entered schedule values.

### Success state
- `Inbound delivery plan updated successfully.`

### No-permission state
- `You do not have permission to plan inbound deliveries.`

---

## UI-015 Goods Receipt Workbench

### Loading state
- Show receipt queue skeleton and receipt-line placeholders.

### Empty state
- `No inbound receipts are waiting at this location.`
- If location-scoped, confirm the active location context.

### Error state
- Load error: `Goods receipts could not be loaded.`
- Verify error: preserve scanned/entered quantities and line context.

### Success state
- `Receipt verified successfully.`
- Task updates to put-away-ready state.

### No-permission state
- `You do not have permission to receive inventory at this location.`

---

## UI-016 Receipt Discrepancy Resolution

### Loading state
- Show discrepancy queue skeleton and detail placeholder.

### Empty state
- `No receipt discrepancies are waiting for review.`

### Error state
- `Discrepancies could not be loaded.`
- Resolution errors preserve notes, reason code, and evidence references.

### Success state
- `Discrepancy resolved successfully.`
- Queue count updates immediately.

### No-permission state
- `You do not have permission to resolve receipt discrepancies.`

---

## UI-017 Put-Away Workbench

### Loading state
- Show pending-task skeleton rows and destination placeholders.

### Empty state
- `No put-away tasks are waiting at this location.`

### Error state
- `Put-away tasks could not be loaded.`
- Completion errors preserve selected location and quantities.

### Success state
- `Put-away completed successfully.`
- Completed task disappears from queue or moves to completed section.

### No-permission state
- `You do not have permission to perform put-away at this location.`

---

## UI-018 Non-PO and Return Receipt Intake

### Loading state
- Show intake form shell and disabled submit while authorization/reference data loads.

### Empty state
- Neutral form state:
  - `Select a receipt type to begin.`

### Error state
- Show invalid authorization/reference errors inline and at form level.
- Preserve all entered values.

### Success state
- `Receipt recorded successfully.`
- Route the user to the next applicable status or reset form for next intake.

### No-permission state
- `You do not have permission to record this type of inbound receipt.`

---

## UI-019 Inbound Supply Tracking

### Loading state
- Show PO pipeline table skeleton and delay-status placeholders.

### Empty state
- `No inbound supply records are available for this view.`

### Error state
- `Inbound supply information could not be loaded.`
- Preserve filters and open detail state if possible.

### Success state
- After a delivery update:
  - `Inbound status updated successfully.`

### No-permission state
- `You do not have permission to view inbound supply tracking.`

---

## UI-020 Inventory Status Monitor

### Loading state
- Show status cards, board, and detail table skeletons.

### Empty state
- If no inventory exists in scope:
  - `No inventory is available in this view.`
- If filters remove all results:
  - `No stock records match these filters.`

### Error state
- `Inventory status could not be loaded.`
- Keep current filters and scope visible.

### Success state
- After refresh or action return:
  - `Inventory view updated.`

### No-permission state
- `You do not have permission to view inventory for this scope.`

---

## UI-021 Inventory Availability Inquiry

### Loading state
- Show search results placeholder and network availability skeleton after search.

### Empty state
- Before search: `Search for a product to view availability.`
- After no match: `No matching product was found.`

### Error state
- `Availability could not be retrieved.`
- Preserve search input and location scope.

### Success state
- Results load with a subtle confirmation:
  - `Availability updated.`

### No-permission state
- `You do not have permission to view availability for this location or product scope.`

---

## UI-022 Inventory Movement History

### Loading state
- Show query bar and movement row skeletons.

### Empty state
- Before search: `Enter filters to view movement history.`
- After no results: `No movement records match this search.`

### Error state
- `Movement history could not be loaded.`
- Preserve entered filters.

### Success state
- Results refresh in place after query or export preparation.

### No-permission state
- `You do not have permission to review movement history in this scope.`

---

## UI-023 Cycle Count Workbench

### Loading state
- Show assigned-task skeleton list and count-entry placeholder.

### Empty state
- `No cycle counts are assigned to you right now.`

### Error state
- `Cycle count assignments could not be loaded.`
- Submission errors preserve entered count quantity.

### Success state
- `Count submitted successfully.`
- Move user to next assignment where applicable.

### No-permission state
- `You do not have permission to perform cycle counts for this location.`

---

## UI-024 Physical Inventory Count Management

### Loading state
- Show count-session status placeholders and zone progress skeletons.

### Empty state
- `No physical inventory count session is active.`
- Action: `Start Count` if permitted.

### Error state
- `Physical count information could not be loaded.`
- Certification failure preserves review context and unresolved-item list.

### Success state
- `Physical count started successfully.`
- `Physical count certified successfully.`

### No-permission state
- `You do not have permission to start or certify physical counts.`

---

## UI-025 Variance Investigation and Approval

### Loading state
- Show pending-variance table skeleton and detail pane placeholder.

### Empty state
- `No variances are waiting for review.`

### Error state
- `Variance cases could not be loaded.`
- Approval/rejection errors preserve findings and notes.

### Success state
- `Variance decision saved successfully.`
- Case exits queue or updates status immediately.

### No-permission state
- `You do not have permission to approve variance cases.`

---

## UI-026 Stock Adjustment Management

### Loading state
- Show adjustment list skeleton and adjustment-form shell.

### Empty state
- List: `No adjustment cases are available in this view.`
- Create mode remains available if permitted.

### Error state
- `The adjustment could not be processed.`
- Preserve all fields, notes, and evidence references.

### Success state
- `Adjustment submitted successfully.`
- Or `Adjustment applied successfully.` depending on workflow state.

### No-permission state
- `You do not have permission to create or approve stock adjustments.`

---

## UI-027 Write-Off Authorization

### Loading state
- Show pending write-off skeleton rows and detail placeholder.

### Empty state
- `No write-off requests are waiting for review.`

### Error state
- `Write-off requests could not be loaded.`
- Decision errors preserve notes and acknowledgment state.

### Success state
- `Write-off decision recorded successfully.`

### No-permission state
- `You do not have permission to authorize write-offs.`

---

## UI-028 Quarantine and Hold Register

### Loading state
- Show hold register skeleton and detail card placeholder.

### Empty state
- `No stock is currently on hold or in quarantine.`

### Error state
- `Hold and quarantine records could not be loaded.`
- Apply/release errors preserve reason and quantity.

### Success state
- `Hold updated successfully.`
- Availability metrics refresh immediately.

### No-permission state
- `You do not have permission to manage quarantined or held stock.`

---

## UI-029 Shrinkage, Loss, and Obsolescence Analysis

### Loading state
- Show chart/card skeletons and analysis table placeholders.

### Empty state
- `No shrinkage or obsolescence data is available for the selected period.`

### Error state
- `The analysis could not be loaded.`
- Keep selected filters.

### Success state
- `Analysis updated.`
- If export succeeds, show `Analysis exported successfully.`

### No-permission state
- `You do not have permission to view shrinkage or obsolescence analysis.`

---

## UI-030 Order Reservation Workbench

### Loading state
- Show order queue skeleton, line-item placeholders, and disabled reserve actions until ATP loads.

### Empty state
- `No orders are waiting for reservation in this view.`

### Error state
- `Order reservation data could not be loaded.`
- Reservation failures preserve selected lines and quantities.

### Success state
- `Reservation completed successfully.`
- Queue and order status update immediately.

### No-permission state
- `You do not have permission to reserve or release inventory for orders.`

---

## UI-031 Pick, Pack, and Ship Workbench

### Loading state
- Show pick queue skeleton and task detail placeholder.

### Empty state
- `No orders are ready for pick, pack, or ship at this location.`

### Error state
- `Fulfillment tasks could not be loaded.`
- Verification/pack/ship errors preserve scanned values and task context.

### Success state
- `Pick verified successfully.`
- `Order packed successfully.`
- `Shipment confirmed successfully.`

### No-permission state
- `You do not have permission to perform fulfillment tasks at this location.`

---

## UI-032 Partial Fulfillment and Backorder Management

### Loading state
- Show affected-order skeletons and quantity comparison placeholders.

### Empty state
- `No partial fulfillment or backorder cases require attention.`

### Error state
- `The partial fulfillment workflow could not be completed.`
- Preserve quantities and customer acknowledgment reference.

### Success state
- `Partial fulfillment recorded successfully.`
- `Backorder created successfully.`

### No-permission state
- `You do not have permission to manage partial fulfillment or backorders.`

---

## UI-033 Fulfillment Exception Management

### Loading state
- Show exception queue skeleton and resolution panel placeholder.

### Empty state
- `No fulfillment exceptions are open right now.`

### Error state
- `Exceptions could not be loaded.`
- Resolution failures preserve selected path and notes.

### Success state
- `Exception resolved successfully.`
- Item exits queue or changes status.

### No-permission state
- `You do not have permission to resolve fulfillment exceptions.`

---

## UI-034 Order Fulfillment Status

### Loading state
- Show order search results skeleton and line-status placeholders.

### Empty state
- Before search: `Search for an order to view fulfillment status.`
- No match: `No order matched your search.`

### Error state
- `Order status could not be loaded.`
- Keep search/filter context intact.

### Success state
- Refreshed view updates line and shipment status with subtle confirmation.

### No-permission state
- `You do not have permission to view this order or its fulfillment details.`

---

## UI-035 Multi-Location Split Fulfillment Planner

### Loading state
- Show allocation-plan skeleton and network-availability placeholders.

### Empty state
- `This order does not currently require multi-location fulfillment.`

### Error state
- `The split fulfillment plan could not be generated.`
- Preserve manual allocations if user edited them.

### Success state
- `Split fulfillment plan created successfully.`
- Location queues or reservation summaries refresh.

### No-permission state
- `You do not have permission to create multi-location fulfillment plans.`

---

## UI-036 Low-Stock Alert Review

### Loading state
- Show alert summary cards and alert list skeletons.

### Empty state
- `There are no active low-stock alerts in this view.`

### Error state
- `Low-stock alerts could not be loaded.`
- Acknowledge errors preserve selected action and notes.

### Success state
- `Alert acknowledged successfully.`
- Alert queue updates immediately.

### No-permission state
- `You do not have permission to review stock alerts.`

---

## UI-037 Replenishment Planning

### Loading state
- Show recommendation cards/table skeleton and supplier/open-PO placeholders.

### Empty state
- `No replenishment recommendations are available for this view.`

### Error state
- `Replenishment recommendations could not be loaded.`
- Requisition-creation errors preserve entered values.

### Success state
- `Requisition created successfully.`
- Recommendation status updates to reflect action taken.

### No-permission state
- `You do not have permission to create replenishment actions.`

---

## UI-038 Transfer Request

### Loading state
- Show request-form shell and transfer-capacity placeholder.

### Empty state
- Neutral form state with helper text:
  - `Enter transfer details to begin.`

### Error state
- Validation and capacity errors remain inline.
- Business-rule failures such as source-minimum breach show a form-level banner.

### Success state
- `Transfer request submitted successfully.`
- Show request reference and new status.

### No-permission state
- `You do not have permission to request stock transfers.`

---

## UI-039 Transfer Approval Queue

### Loading state
- Show approval queue skeleton and impact-comparison placeholder.

### Empty state
- `No transfer requests are waiting for approval.`

### Error state
- `Transfer approvals could not be loaded.`
- Decision errors preserve decision note and selection.

### Success state
- `Transfer decision saved successfully.`
- Queue count updates immediately.

### No-permission state
- `You do not have permission to approve or reject transfers.`

---

## UI-040 Transfer Execution and In-Transit Tracking

### Loading state
- Show dispatch/receipt queue skeletons and in-transit placeholders.

### Empty state
- Dispatch area: `No approved transfers are ready for dispatch.`
- In-transit area: `No stock is currently in transit.`

### Error state
- `Transfer execution data could not be loaded.`
- Dispatch/receipt failures preserve entered quantities and notes.

### Success state
- `Transfer dispatched successfully.`
- `Transfer received successfully.`

### No-permission state
- `You do not have permission to dispatch or receive transfers for this location.`

---

## UI-041 Network Rebalancing Analysis

### Loading state
- Show imbalance-summary skeletons and recommendation placeholders.

### Empty state
- `No network imbalances were identified for the selected scope.`

### Error state
- `Network rebalancing analysis could not be loaded.`
- Preserve filters.

### Success state
- `Recommendation generated successfully.` or `Transfer request created successfully.`

### No-permission state
- `You do not have permission to view network rebalancing analysis.`

---

## UI-042 Return Authorization Management

### Loading state
- Show order-search placeholder and return-line eligibility skeleton.

### Empty state
- Before search: `Search for an order to begin a return authorization.`
- No eligible lines: `No return-eligible items were found for this order.`

### Error state
- `The return authorization could not be completed.`
- Preserve selected order, lines, and quantities.

### Success state
- `Return authorization issued successfully.`
- Show authorization reference clearly.

### No-permission state
- `You do not have permission to authorize returns.`

---

## UI-043 Return Inspection and Disposition

### Loading state
- Show pending-return queue skeleton and receipt/inspection/disposition placeholders.

### Empty state
- `No returns are waiting to be received or inspected.`

### Error state
- `Return processing could not be completed.`
- Preserve received quantities, condition entries, and disposition choices.

### Success state
- `Return received successfully.`
- `Inspection recorded successfully.`
- `Disposition completed successfully.`

### No-permission state
- `You do not have permission to process returns at this location.`

---

## UI-044 Operational Reports and Analytics

### Loading state
- Show report filter shell and table/chart skeletons.

### Empty state
- Before run: `Select filters and run a report.`
- After no data: `No report data is available for the selected filters.`

### Error state
- `The report could not be generated.`
- Preserve filters and chosen report type.

### Success state
- `Report updated successfully.`
- `Export completed successfully.` when applicable.

### No-permission state
- `You do not have permission to view this report.`

---

## UI-045 Inventory Valuation Reconciliation

### Loading state
- Show valuation summary skeleton, comparison placeholders, and note area shell.

### Empty state
- `No valuation data is available for the selected period.`

### Error state
- `Valuation reconciliation could not be loaded.`
- Preserve selected period and unsaved notes.

### Success state
- `Reconciliation notes saved successfully.`
- `Reconciliation finalized successfully.`

### No-permission state
- `You do not have permission to view inventory valuation data.`

---

## UI-046 Promotional Stock Readiness

### Loading state
- Show campaign summary skeleton, readiness rows placeholder, and gap panel shell.

### Empty state
- `No promotional campaigns are available in this view.`

### Error state
- `Campaign readiness data could not be loaded.`
- Preserve selected campaign and unsaved notes.

### Success state
- `Readiness confirmed successfully.`
- `Allocation updated successfully.` as applicable.

### No-permission state
- `You do not have permission to view or manage promotional stock readiness.`

---

## UI-047 Audit and Control Review Workspace

### Loading state
- Show scope filter shell, transaction list skeleton, and findings placeholder.

### Empty state
- Before scope run: `Select an audit scope to begin review.`
- After no results: `No records matched this audit scope.`

### Error state
- `Audit review data could not be loaded.`
- Preserve scope filters and unsaved findings if possible.

### Success state
- `Finding recorded successfully.`
- `Audit review completed successfully.`

### No-permission state
- `You do not have permission to access the audit workspace.`

---

## UI-048 Audit Trail Query

### Loading state
- Show query filter shell and result-table skeleton.

### Empty state
- Before query: `Enter filters to search the audit trail.`
- No result: `No audit records match this query.`

### Error state
- `Audit trail results could not be loaded.`
- Preserve query filters and selected tab/detail context.

### Success state
- `Query completed successfully.`
- `Audit results exported successfully.` when applicable.

### No-permission state
- `You do not have permission to query audit trail data.`

---

## UI-049 User Account Management

### Loading state
- Show user-directory skeleton and account-detail placeholder.

### Empty state
- `No user accounts are available in this view.`
- If create allowed, show `Create User`.

### Error state
- `User accounts could not be loaded.`
- Save/suspend/deactivate errors preserve entered role assignments and notes.

### Success state
- `User account saved successfully.`
- `User suspended successfully.` or `User deactivated successfully.`

### No-permission state
- `You do not have permission to manage user accounts.`

---

## UI-050 Role and Access Control Administration

### Loading state
- Show role list skeleton and permission-matrix placeholder.

### Empty state
- `No role configuration is available in this view.`

### Error state
- `Role and access settings could not be loaded.`
- Save failures preserve matrix edits when possible.

### Success state
- `Permissions updated successfully.`
- `Segregation-of-duties validation completed.`

### No-permission state
- `You do not have permission to manage roles and access controls.`

---

## Notes

- These states should be implemented consistently with the API error model in `SRS/API_Design/Error-Response-Specification.md`.
- Field-level validation and transactional error handling for forms are further detailed in `SRS/UI_UX/IMS-Form-Specifications-and-Validation.md`.
- Detailed component behavior for banners, empty states, tables, skeletons, and dialogs should align with `SRS/UI_UX/IMS-Component-Inventory.md`.

