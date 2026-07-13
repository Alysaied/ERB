# Inventory Management System User Journeys

## Purpose

This document defines user journeys for the major business processes in the Inventory Management System. Each journey is written from the user's perspective and focuses on the user's goal, decision points, friction, and successful outcome rather than internal system behavior.

## Scope

The journeys below cover the major business processes defined in the approved BRD:

1. Product master data management
2. Location and warehouse setup
3. Stock policy and threshold definition
4. Goods receipt and verification
5. Receipt discrepancy resolution
6. Stock put-away
7. Inventory status monitoring
8. Inventory availability inquiry
9. Cycle counting
10. Full physical inventory count
11. Variance investigation and approval
12. Stock adjustment
13. Inventory write-off
14. Quarantine and hold management
15. Order availability confirmation
16. Inventory reservation
17. Pick, pack, and ship
18. Partial fulfillment and backorder handling
19. Low-stock alert review
20. Replenishment planning
21. Inter-location transfer request
22. Transfer approval
23. Transfer execution
24. Customer return authorization
25. Return inspection and disposition
26. Reporting and operational review
27. Inventory valuation reconciliation
28. Promotional stock readiness
29. Audit and control review
30. User account and access management

---

## 1. Product Master Data Management

- **User role:** Inventory Controller
- **Goal:** Create or maintain an accurate product record so every team works from one trusted SKU definition.
- **Steps:**
  1. Open the product catalog.
  2. Search for the product to confirm it does not already exist.
  3. Create a new product or open an existing one for update.
  4. Enter or revise SKU, name, category, unit of measure, barcode, and status.
  5. Review the record for completeness.
  6. Save the product and confirm it is available for operations.
- **Decisions:**
  - Is this a new product or an update to an existing one?
  - Is there a possible duplicate that should be resolved before saving?
  - Should the product be active, inactive, or discontinued?
- **Pain points:**
  - Duplicate products create confusion and downstream errors.
  - Missing attributes can block receiving, reservation, or reporting later.
  - Product status decisions may affect purchasing and sales unexpectedly.
- **Success outcome:** A complete, unique, and trusted product record is available for all inventory processes.

## 2. Location and Warehouse Setup

- **User role:** Inventory Controller
- **Goal:** Configure a location correctly so stock can be assigned, counted, received, moved, and reported there.
- **Steps:**
  1. Open location management.
  2. Create a new location or update an existing one.
  3. Define the location type, hierarchy, and operational status.
  4. Configure storage positions if needed.
  5. Load or confirm opening balances for go-live.
  6. Activate the location for daily operations.
- **Decisions:**
  - Is the location operationally ready for activation?
  - Does it belong under an existing parent location?
  - Are opening balances verified enough to trust the location at go-live?
- **Pain points:**
  - Poor setup causes inventory to be tracked in the wrong place.
  - Unclear hierarchy can affect reporting and transfer flows.
  - Inaccurate opening balances create immediate mistrust in the system.
- **Success outcome:** The location is correctly configured, active, and ready for controlled stock activity.

## 3. Stock Policy and Threshold Definition

- **User role:** Inventory Controller
- **Goal:** Set thresholds that help the business replenish on time without overstocking.
- **Steps:**
  1. Open stock policy management.
  2. Find the product and relevant location.
  3. Review current stock levels, demand expectations, and service needs.
  4. Set reorder level, minimum threshold, and safety stock.
  5. Save the policy.
  6. Confirm the policy is active for monitoring and alerts.
- **Decisions:**
  - Does this product need a location-specific policy?
  - Is current safety stock sufficient or too conservative?
  - Should thresholds change because demand or lead time changed?
- **Pain points:**
  - Users may lack confidence in the data behind threshold decisions.
  - Overly low thresholds increase stockout risk.
  - Overly high thresholds tie up working capital.
- **Success outcome:** The product is governed by clear thresholds that support proactive replenishment.

## 4. Goods Receipt and Verification

- **User role:** Receiving Clerk
- **Goal:** Receive incoming supplier goods accurately so only verified stock enters inventory.
- **Steps:**
  1. Open the goods receipt workbench.
  2. Locate the expected purchase order or shipment.
  3. Scan or enter received items.
  4. Verify item identity, quantity, and visible condition.
  5. Capture lot, batch, or shelf-life details when required.
  6. Confirm the receipt and stage stock for put-away.
- **Decisions:**
  - Does the shipment match the purchase order?
  - Is there damage, shortage, wrong product, or shelf-life issue?
  - Can the receipt be accepted as normal or does it require discrepancy handling?
- **Pain points:**
  - Matching paperwork to physical goods can be slow.
  - Traceable products add extra data-entry pressure.
  - Receiving the wrong item creates immediate process interruption.
- **Success outcome:** Verified goods are accurately received and ready for the next step without compromising stock accuracy.

## 5. Receipt Discrepancy Resolution

- **User role:** Receiving Clerk
- **Goal:** Record and resolve inbound differences without losing supplier accountability or inventory control.
- **Steps:**
  1. Identify a mismatch during receiving.
  2. Open discrepancy logging for the affected receipt line.
  3. Record discrepancy type, quantity impact, and notes.
  4. Attach evidence if needed.
  5. Escalate for manager review or resolution.
  6. Complete the receipt with accepted quantities and documented variance.
- **Decisions:**
  - Is the issue a shortage, overage, wrong item, damage, or tolerance breach?
  - Should the quantity be accepted, partially accepted, or held for review?
  - Does the discrepancy require manager approval or supplier follow-up?
- **Pain points:**
  - Users can feel pressured to keep receiving moving quickly.
  - Incomplete evidence makes later disputes harder to resolve.
  - Rework increases when discrepancies are documented inconsistently.
- **Success outcome:** The discrepancy is fully documented, the accepted stock is correct, and the issue can be followed through to closure.

## 6. Stock Put-Away

- **User role:** Warehouse Staff
- **Goal:** Move received goods into the correct storage location so they become available for fulfillment and tracking.
- **Steps:**
  1. Open the put-away task queue.
  2. Select the next receipt awaiting storage.
  3. Move goods from receiving to the suggested storage position.
  4. Confirm product, quantity, and storage location.
  5. Complete put-away confirmation.
  6. Verify the task is cleared from the queue.
- **Decisions:**
  - Is the suggested location appropriate and available?
  - Does product rotation require FIFO or FEFO handling?
  - Is there any mismatch between the staged quantity and the physical goods?
- **Pain points:**
  - Storage congestion can force manual workaround decisions.
  - Incorrect placement causes future pick failures and count problems.
  - Staff may lose time if receiving and storage labeling are unclear.
- **Success outcome:** Stock is in the right location, properly recorded, and available for downstream use.

## 7. Inventory Status Monitoring

- **User role:** Inventory Controller
- **Goal:** Understand overall stock health and identify issues before they disrupt operations.
- **Steps:**
  1. Open the inventory status monitor.
  2. Filter by location, product type, or status.
  3. Review low-stock, out-of-stock, overstock, and quarantined items.
  4. Drill into a product or location when something looks wrong.
  5. Decide whether follow-up action is needed.
  6. Route the issue to replenishment, transfer, adjustment, or investigation.
- **Decisions:**
  - Is this a temporary issue or something that requires immediate action?
  - Should the next action be replenishment, transfer, or investigation?
  - Is the problem local to one location or network-wide?
- **Pain points:**
  - Users may see symptoms before they see the root cause.
  - Too many alerts can make prioritization difficult.
  - Network-level visibility can be overwhelming without filtering.
- **Success outcome:** The user quickly identifies stock risks and knows what action to take next.

## 8. Inventory Availability Inquiry

- **User role:** Sales Representative
- **Goal:** Answer a customer stock question confidently without needing to call the warehouse.
- **Steps:**
  1. Open availability inquiry.
  2. Search by SKU, product name, or barcode.
  3. Review on-hand, reserved, and ATP figures.
  4. Check relevant locations or network-wide availability.
  5. Confirm stock status and expected inbound if needed.
  6. Respond to the customer.
- **Decisions:**
  - Is there enough ATP to support a commitment?
  - Should the answer be location-specific or network-wide?
  - Is expected inbound relevant to the customer conversation?
- **Pain points:**
  - Users need fast answers during live customer conversations.
  - Confusion between on-hand and ATP can lead to bad promises.
  - If stock is fragmented across locations, the answer may be less straightforward.
- **Success outcome:** The customer receives a fast, accurate, and credible availability answer.

## 9. Cycle Counting

- **User role:** Warehouse Staff
- **Goal:** Count assigned stock accurately without being biased by system quantities.
- **Steps:**
  1. Open assigned cycle counts.
  2. Go to the specified product and storage location.
  3. Count the physical stock.
  4. Enter the counted quantity.
  5. Submit the result.
  6. Move to the next assignment.
- **Decisions:**
  - Does the physical stock clearly match one count result, or should it be recounted?
  - Is the storage area clear enough to count confidently?
  - Should an unusual condition be noted for later investigation?
- **Pain points:**
  - Cluttered or mixed storage slows counting.
  - Staff may worry about making mistakes that trigger investigations.
  - Repeated counting tasks can feel disruptive to warehouse throughput.
- **Success outcome:** The physical count is submitted accurately and supports improved inventory confidence.

## 10. Full Physical Inventory Count

- **User role:** Inventory Controller
- **Goal:** Complete a controlled wall-to-wall count that establishes a trusted inventory baseline.
- **Steps:**
  1. Start a physical inventory count session.
  2. Confirm the location is frozen for normal movement.
  3. Assign teams or zones for counting.
  4. Monitor progress as counts are entered.
  5. Identify any incomplete or questionable areas.
  6. Close and certify the count session.
- **Decisions:**
  - Is the location ready to enter freeze mode?
  - Are all areas fully counted and verified?
  - Can the count be certified now or should unresolved issues be addressed first?
- **Pain points:**
  - Full counts are operationally disruptive.
  - Users must coordinate many people under time pressure.
  - Incomplete counts reduce trust in the final result.
- **Success outcome:** The location completes a reliable full count and generates a trustworthy variance baseline.

## 11. Variance Investigation and Approval

- **User role:** Warehouse Manager
- **Goal:** Understand why a count variance happened and approve only justified corrections.
- **Steps:**
  1. Open the pending variance queue.
  2. Select a variance case.
  3. Review system quantity versus counted quantity.
  4. Investigate likely causes with notes and evidence.
  5. Decide whether to approve, escalate, or reject the proposed correction.
  6. Route the case to the proper next step.
- **Decisions:**
  - Is the variance caused by process error, damage, shrinkage, or timing?
  - Does the variance exceed an approval threshold?
  - Is more investigation needed before approval?
- **Pain points:**
  - Root causes are not always obvious.
  - The user may be balancing speed against control discipline.
  - Large variances can create pressure from multiple stakeholders.
- **Success outcome:** Only justified variances move forward, preserving control and data accuracy.

## 12. Stock Adjustment

- **User role:** Warehouse Manager
- **Goal:** Correct recorded stock safely when reality does not match the system.
- **Steps:**
  1. Open stock adjustment management.
  2. Identify the product and location.
  3. Enter increase or decrease quantity.
  4. Select the required reason code and add notes.
  5. Submit for approval if threshold rules require it.
  6. Confirm the adjustment is applied.
- **Decisions:**
  - Is an adjustment truly needed or should the item be investigated first?
  - Which reason code best explains the change?
  - Does the value or quantity require independent approval?
- **Pain points:**
  - Users may choose vague reason codes under time pressure.
  - Incorrect adjustments can worsen the data instead of fixing it.
  - Approval delays can block urgent corrections.
- **Success outcome:** Stock is corrected with proper justification, traceability, and governance.

## 13. Inventory Write-Off

- **User role:** Operations Director
- **Goal:** Remove unsellable inventory in a controlled way with clear accountability.
- **Steps:**
  1. Open pending write-off requests.
  2. Review the affected inventory, quantity, and supporting evidence.
  3. Check financial and operational implications.
  4. Approve or reject the write-off.
  5. Confirm finance acknowledgment if required.
  6. Complete write-off execution.
- **Decisions:**
  - Is the inventory truly unsellable or should another disposition be used?
  - Is the evidence strong enough to support write-off?
  - Does finance need to review before final approval?
- **Pain points:**
  - Write-offs can be sensitive and highly visible.
  - Weak documentation makes decisions harder.
  - Users may want better root-cause context before approval.
- **Success outcome:** Unsellable stock is removed with defensible authorization and a full audit trail.

## 14. Quarantine and Hold Management

- **User role:** Warehouse Manager
- **Goal:** Prevent questionable or restricted stock from being used or sold until it is cleared.
- **Steps:**
  1. Open quarantine and hold management.
  2. Locate the affected stock.
  3. Apply hold or quarantine status with a reason.
  4. Confirm the quantity is excluded from sellable stock.
  5. Monitor the hold until resolution.
  6. Release or disposition the stock when authorized.
- **Decisions:**
  - Should the stock be quarantined, held temporarily, or written off?
  - How much quantity is affected?
  - Is the issue quality-related, regulatory, or operational?
- **Pain points:**
  - Users need to move fast to avoid accidental sale or shipment.
  - Unclear ownership of follow-up can leave stock stuck in hold.
  - Long-running holds reduce usable inventory and frustrate teams.
- **Success outcome:** Risky stock is contained quickly and kept out of normal operations until resolved.

## 15. Order Availability Confirmation

- **User role:** Sales Representative
- **Goal:** Determine whether the business can commit to a customer's requested order.
- **Steps:**
  1. Open order availability confirmation.
  2. Review the requested products and quantities.
  3. Trigger an ATP check.
  4. Review line-by-line availability results.
  5. Consider location options or partial availability.
  6. Communicate the commitment position to the customer.
- **Decisions:**
  - Is the order fully available, partially available, or unavailable?
  - Should the promise be made from one location or across the network?
  - Should the next step be reservation, split fulfillment, or backorder discussion?
- **Pain points:**
  - Customer expectations are often immediate.
  - Users need clarity on what can actually be promised.
  - Network stock can complicate what seems like a simple answer.
- **Success outcome:** The user gives a realistic and supportable commitment based on ATP, not guesswork.

## 16. Inventory Reservation

- **User role:** Customer Service Representative
- **Goal:** Reserve confirmed stock so it is protected for a specific customer order.
- **Steps:**
  1. Open the confirmed order.
  2. Review availability and selected fulfillment location.
  3. Reserve the needed quantity.
  4. Confirm the reservation result.
  5. Release the order to warehouse fulfillment.
  6. Revisit the reservation later if the order changes.
- **Decisions:**
  - Which location should fulfill the order?
  - Is there enough ATP for all lines?
  - Should a reservation be released if the customer changes or cancels the order?
- **Pain points:**
  - Reservation mistakes can create downstream fulfillment issues.
  - Users need confidence that ATP is current at the moment of reservation.
  - Changing orders can require tedious reservation cleanup.
- **Success outcome:** Stock is securely committed to the order and protected from double allocation.

## 17. Pick, Pack, and Ship

- **User role:** Warehouse Picker / Packer
- **Goal:** Fulfill the order accurately and get it shipped without causing stock errors.
- **Steps:**
  1. Open the pick queue.
  2. Select the assigned order or task.
  3. Pick items from the indicated locations.
  4. Verify the picked products and quantities.
  5. Pack the shipment.
  6. Confirm shipment handoff and complete the task.
- **Decisions:**
  - Does the shelf stock match what the task expects?
  - Is the picked quantity correct and complete?
  - If something is wrong, should the task be stopped and an exception raised?
- **Pain points:**
  - Pick failures are disruptive and time-sensitive.
  - Staff need accurate location guidance to move fast.
  - Errors discovered late in packing waste effort and delay shipment.
- **Success outcome:** The correct order is shipped accurately and inventory is deducted at the right moment.

## 18. Partial Fulfillment and Backorder Handling

- **User role:** Customer Service Representative
- **Goal:** Save as much of the order as possible when full quantity cannot be supplied immediately.
- **Steps:**
  1. Open the affected order.
  2. Review available quantity versus ordered quantity.
  3. Discuss options with the customer.
  4. Record the customer's acceptance of a partial shipment if applicable.
  5. Confirm immediate fulfillment for available quantity.
  6. Create or monitor the backorder for the remainder.
- **Decisions:**
  - Is partial shipment acceptable to the customer?
  - Should the remainder be backordered or canceled?
  - Is an expected future date credible enough to communicate?
- **Pain points:**
  - Customer conversations can be sensitive and time-consuming.
  - Users may not always know when the remainder will be available.
  - Splitting an order adds coordination overhead.
- **Success outcome:** The customer receives a clear, agreed plan and the available stock still moves forward.

## 19. Low-Stock Alert Review

- **User role:** Purchasing Manager
- **Goal:** Notice and prioritize stock risks early enough to prevent service problems.
- **Steps:**
  1. Open low-stock alerts.
  2. Review active alerts by severity and product importance.
  3. Drill into the most urgent items.
  4. Check current stock, open supply, and network alternatives.
  5. Acknowledge each alert and assign next action.
  6. Monitor remaining unresolved alerts.
- **Decisions:**
  - Which alert needs action first?
  - Should the answer be transfer, purchase, or watchful waiting?
  - Is the issue local or network-wide?
- **Pain points:**
  - Too many alerts can create noise.
  - Users need enough context to act, not just know there is a problem.
  - Prioritization is harder when many SKUs are at risk simultaneously.
- **Success outcome:** Critical alerts are acknowledged quickly and turned into concrete next actions.

## 20. Replenishment Planning

- **User role:** Buyer
- **Goal:** Convert stock signals into the right replenishment action at the right time.
- **Steps:**
  1. Open replenishment planning.
  2. Review recommended reorder items.
  3. Check whether another location can cover the need first.
  4. Decide to create a requisition or take another action.
  5. Submit the requisition for approval.
  6. Follow it through to purchase order conversion.
- **Decisions:**
  - Should the need be covered by transfer or purchase?
  - Is the recommended quantity appropriate?
  - Does the product remain eligible for reorder?
- **Pain points:**
  - Users must balance urgency, cost, and available alternatives.
  - Data gaps in lead times or demand can reduce confidence.
  - Approval delay can keep urgent replenishment from moving fast enough.
- **Success outcome:** A justified replenishment action is created and ready for procurement execution.

## 21. Inter-Location Transfer Request

- **User role:** Regional / Store Manager
- **Goal:** Solve a local shortage by using stock already available elsewhere in the network.
- **Steps:**
  1. Open transfer request.
  2. Select destination location, source location, product, and quantity.
  3. Review source availability and transfer impact.
  4. Enter the business reason.
  5. Submit the request for approval.
  6. Track the request status.
- **Decisions:**
  - Which source location can spare the stock?
  - Is transfer better than purchasing new stock?
  - Is the requested quantity appropriate and sustainable for the source?
- **Pain points:**
  - Users may not always know the best source location.
  - Transfer urgency can conflict with approval latency.
  - Poor network visibility can lead to unnecessary transfers.
- **Success outcome:** A well-justified transfer request is submitted to relieve the shortage with minimal network disruption.

## 22. Transfer Approval

- **User role:** Operations Director
- **Goal:** Approve only transfers that help the network without harming the source location.
- **Steps:**
  1. Open the transfer approval queue.
  2. Review source and destination need.
  3. Check source stock after transfer.
  4. Decide to approve or reject.
  5. Record the decision.
  6. Notify locations through workflow status.
- **Decisions:**
  - Will this transfer create a new risk at the source?
  - Is the shortage urgent enough to justify movement?
  - Should the request be approved as-is or rejected?
- **Pain points:**
  - The approver must think network-wide, not locally.
  - Approval queues can become bottlenecks.
  - Incomplete justification makes confident decisions harder.
- **Success outcome:** The best transfer requests move forward while risky ones are stopped before causing new problems.

## 23. Transfer Execution

- **User role:** Warehouse Staff
- **Goal:** Move stock from one location to another accurately and keep both locations' inventory correct.
- **Steps:**
  1. Open approved transfer tasks.
  2. Pick the transfer quantity at the source.
  3. Verify and dispatch the stock.
  4. Send or hand off the stock for transport.
  5. Receive and verify it at the destination.
  6. Confirm completion of the transfer.
- **Decisions:**
  - Does the picked quantity exactly match the transfer order?
  - Is any part of the stock damaged or mismatched during movement?
  - Can the destination accept the transfer as received?
- **Pain points:**
  - Transfers have two operational handoffs, increasing failure risk.
  - In-transit gaps can create anxiety if status is unclear.
  - Errors at either end affect both source and destination records.
- **Success outcome:** Stock leaves the source, arrives at the destination, and is fully traceable throughout the move.

## 24. Customer Return Authorization

- **User role:** Customer Service Representative
- **Goal:** Approve valid returns fairly while keeping control over what the warehouse should expect back.
- **Steps:**
  1. Open return authorization.
  2. Find the original order.
  3. Select the item and quantity requested for return.
  4. Validate the reason and policy eligibility.
  5. Issue the return authorization.
  6. Share return instructions with the customer.
- **Decisions:**
  - Is the return eligible under policy?
  - Is the requested quantity within allowed limits?
  - Should the authorization be issued or declined?
- **Pain points:**
  - Users often need to balance customer satisfaction with policy compliance.
  - Missing order context slows the conversation.
  - Unclear reasons can make approval harder.
- **Success outcome:** The customer gets a clear authorization path and the warehouse receives a controlled expectation of what will return.

## 25. Return Inspection and Disposition

- **User role:** Receiving Clerk
- **Goal:** Decide what to do with returned goods so good stock is recovered and bad stock is contained.
- **Steps:**
  1. Open pending return receipts.
  2. Match the incoming return to its authorization.
  3. Verify quantity and product identity.
  4. Inspect physical condition.
  5. Choose disposition: restock, quarantine, or write-off.
  6. Confirm completion of the return process.
- **Decisions:**
  - Is the return truly authorized?
  - Is the product resalable, damaged, or defective?
  - Should the stock go back into inventory, be held, or be removed?
- **Pain points:**
  - Condition assessments can be subjective.
  - Returned goods may arrive incomplete or in poor condition.
  - Users need clarity on what qualifies for restock versus quarantine.
- **Success outcome:** Returned goods are processed consistently and routed to the correct inventory state.

## 26. Reporting and Operational Review

- **User role:** Operations Director
- **Goal:** Understand operational performance and identify where intervention is needed.
- **Steps:**
  1. Open reports and analytics.
  2. Choose the relevant report or dashboard.
  3. Filter by date, location, or category.
  4. Review trends, exceptions, and outliers.
  5. Drill into problem areas if needed.
  6. Export or share findings for follow-up action.
- **Decisions:**
  - Which metric or report matters most right now?
  - Is this a one-off issue or a pattern?
  - Does the issue need operational action, policy change, or further investigation?
- **Pain points:**
  - Large data sets can slow understanding if not well focused.
  - Users may struggle to connect metrics to actionable next steps.
  - Different stakeholders may need different levels of detail.
- **Success outcome:** The user gains actionable insight and can direct operations based on evidence rather than instinct.

## 27. Inventory Valuation Reconciliation

- **User role:** Finance Manager
- **Goal:** Confirm that operational inventory records align with financial expectations for a period close.
- **Steps:**
  1. Open valuation reconciliation.
  2. Select the relevant period.
  3. Review operational valuation and comparison figures.
  4. Investigate material variances.
  5. Document reconciliation notes.
  6. Finalize the period review.
- **Decisions:**
  - Is the variance acceptable or material?
  - Does the issue stem from operations, timing, or finance treatment?
  - Can the period be closed with confidence?
- **Pain points:**
  - Finance needs confidence in data produced by operational processes.
  - Large unexplained variances can create time pressure at period end.
  - Users may need to cross-check multiple underlying events.
- **Success outcome:** Finance can complete reconciliation with a clear view of differences and documented closure confidence.

## 28. Promotional Stock Readiness

- **User role:** Marketing Manager
- **Goal:** Make sure enough inventory is secured before a campaign or launch commitment is made.
- **Steps:**
  1. Open promotional readiness.
  2. Review campaign products and required quantities.
  3. Check ring-fenced stock, ATP, and inbound supply.
  4. Identify products at risk.
  5. Confirm readiness or escalate gaps.
  6. Communicate launch confidence to stakeholders.
- **Decisions:**
  - Is current ring-fenced stock sufficient?
  - Can inbound supply close any shortfall in time?
  - Should the campaign proceed, be adjusted, or be escalated?
- **Pain points:**
  - Promotional demand creates pressure on shared inventory.
  - Users need certainty before public commitments are made.
  - Gaps discovered late can disrupt campaigns and trust.
- **Success outcome:** The campaign team has a credible readiness view and can commit with confidence.

## 29. Audit and Control Review

- **User role:** Internal Auditor
- **Goal:** Verify that inventory activity follows control rules and that the audit trail is complete.
- **Steps:**
  1. Open the audit workspace.
  2. Define the audit scope.
  3. Review transactions, approvals, and control evidence.
  4. Sample high-risk records.
  5. Note findings, breaches, or clean results.
  6. Export evidence and complete the review.
- **Decisions:**
  - Which locations, periods, or transaction types are highest risk?
  - Is a control failure isolated or systemic?
  - Does a finding require escalation or remediation tracking?
- **Pain points:**
  - Audit users need complete, reliable history without ambiguity.
  - Missing approval evidence undermines trust quickly.
  - Investigations can be time-consuming when records are fragmented.
- **Success outcome:** The auditor can confidently assess compliance and produce defensible findings.

## 30. User Account and Access Management

- **User role:** System Administrator
- **Goal:** Give each user the right access for their job while protecting control boundaries.
- **Steps:**
  1. Open user account management.
  2. Search for an existing user or create a new one.
  3. Assign role and location scope.
  4. Review any access-control conflicts.
  5. Activate, suspend, or update the account as needed.
  6. Confirm effective permissions.
- **Decisions:**
  - Does the user need a new account or an update to an existing one?
  - Which role best matches the user's responsibility?
  - Does the requested access create a segregation-of-duties issue?
- **Pain points:**
  - Over-permissioning creates control risk.
  - Under-permissioning blocks operations and frustrates users.
  - Role complexity can make correct assignment difficult.
- **Success outcome:** The user receives correct, scoped access that supports work without compromising governance.

---

## Journey Design Notes

- These journeys are intentionally written from the user's point of view rather than the system's.
- The journeys can be used as input for task flows, wireframes, usability scenarios, and acceptance criteria.
- Where multiple roles collaborate in one process, the journey is centered on the primary user who owns the outcome.

