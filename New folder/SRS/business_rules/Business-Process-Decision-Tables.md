# Business Process Decision Tables
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DT-001 |
| **Document Title** | Business Process Decision Tables — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Business Analyst |
| **Source Documents** | BRD-IMS-001 (Section 10), Business Workflows (WF-01–WF-32), Business Exception Scenarios (EX-001–EX-043) |
| **Date** | July 5, 2026 |
| **Scope** | Business decision logic only — not system rules, validation logic, or technical branching |

### Purpose

This document identifies **32 business processes** that contain **multiple decision paths** and expresses key branching logic as **decision tables**. Each table maps business **conditions** to **actions** and **outcomes** so stakeholders can see how the organization should respond when situations differ.

### How to Read Decision Tables

| Column | Meaning |
|--------|---------|
| **Rule** | Rule identifier within the process (R1, R2, …). Rules are evaluated in priority order unless noted. |
| **Conditions** | Business facts that must be true for the rule to apply. "—" means any value. |
| **Actions** | What responsible actors should do when conditions are met. |
| **Outcome** | Resulting process state or next workflow triggered. |

**Notation:** Y = Yes / True · N = No / False · — = Don't care / Not applicable

### Process Index

| BP | Process | Decision Table | Complexity |
|----|---------|----------------|--------------|
| BP-01 | Product Master Data Management | DT-01 | Medium |
| BP-02 | Location & Warehouse Setup | DT-02 | Medium |
| BP-03 | Stock Policy & Threshold Definition | DT-03 | Low |
| BP-04 | ABC Product Classification | DT-04 | Low |
| BP-05 | Purchase Order Placement | DT-05 | High |
| BP-06 | Inbound Shipment Planning | DT-06 | Low |
| BP-07 | Goods Receipt & Verification | DT-07 | High |
| BP-08 | Receipt Discrepancy Resolution | DT-08 | High |
| BP-09 | Stock Put-Away & Storage | DT-09 | Low |
| BP-10 | Inventory Status Monitoring | DT-10 | Medium |
| BP-11 | Cycle Counting | DT-11 | Medium |
| BP-12 | Full Physical Inventory Count | DT-12 | Medium |
| BP-13 | Count Variance Investigation & Approval | DT-13 | High |
| BP-14 | Stock Adjustment & Write-Off | DT-14 | High |
| BP-15 | Shrinkage & Loss Management | DT-15 | Medium |
| BP-16 | Order Availability Confirmation | DT-16 | High |
| BP-17 | Inventory Reservation | DT-17 | Medium |
| BP-18 | Pick, Pack & Ship | DT-18 | High |
| BP-19 | Partial Fulfillment & Backorder | DT-19 | High |
| BP-20 | Outbound Exception Handling | DT-20 | High |
| BP-21 | Low-Stock Alert Review | DT-21 | High |
| BP-22 | Replenishment Planning & Requisition | DT-22 | Medium |
| BP-23 | Inbound Supply Tracking | DT-23 | Medium |
| BP-24 | Inter-Location Transfer Request | DT-24 | High |
| BP-25 | Inter-Location Transfer Execution | DT-25 | Medium |
| BP-26 | Network Stock Rebalancing | DT-26 | Medium |
| BP-27 | Customer Return Intake | DT-27 | Medium |
| BP-28 | Return-to-Stock or Disposal | DT-28 | High |
| BP-29 | Inventory Performance Reporting | DT-29 | Low |
| BP-30 | Inventory Valuation & Financial Reconciliation | DT-30 | Medium |
| BP-31 | Promotional & Launch Stock Readiness | DT-31 | High |
| BP-32 | Inventory Audit & Control Review | DT-32 | Medium |

---

## Domain 1: Master Data & Governance

### BP-01: Product Master Data Management (DT-01)

**Decision context:** Product create, update, or discontinuation request received.

| Rule | Request complete & valid | Duplicate SKU exists | Dept approval | Requested status | Actions | Outcome |
|------|--------------------------|----------------------|---------------|------------------|---------|---------|
| R1 | N | — | — | — | Return to requester for missing information | Request pending — not in catalog |
| R2 | Y | Y | — | — | Compare records; merge or correct existing SKU; do not create duplicate | Single product identity maintained |
| R3 | Y | N | N | — | Revise definition; resubmit for purchasing and operations review | Request pending approval |
| R4 | Y | N | Y | Active | Finalize record; publish to all locations; enable receive, replenish, fulfill | Product active in network |
| R5 | Y | N | Y | Inactive | Set inactive; block new replenishment; allow fulfill existing stock per policy | Product inactive |
| R6 | Y | N | Y | Discontinued | Set discontinued; block new orders; flag remaining stock for clearance or write-off plan | Product discontinued — runout planning |

---

### BP-02: Location & Warehouse Setup (DT-02)

**Decision context:** Leadership approves a location change (open, close, or reorganize).

| Rule | Strategically approved | Change type | Stock disposition planned (if close) | Actions | Outcome |
|------|------------------------|-------------|-----------------------------------|---------|---------|
| R1 | N | — | — | Defer or reject; document reason | No location change |
| R2 | Y | New | — | Configure location; assign manager; set hierarchy; plan opening balance | New location setup in progress |
| R3 | Y | Reorganize | — | Update hierarchy and accountability; no stock disposition required | Network structure updated |
| R4 | Y | Close | N | Block closure; require disposition plan for all on-hand stock | Closure blocked |
| R5 | Y | Close | Y — Transfer | Execute transfers; deactivate when stock cleared | Location closed — stock redistributed |
| R6 | Y | Close | Y — Sell through | Fulfill remaining via sales; deactivate when cleared | Location closed — sell-through |
| R7 | Y | Close | Y — Write off | Authorized write-off of residual; deactivate location | Location closed — stock removed |

---

### BP-03: Stock Policy & Threshold Definition (DT-03)

**Decision context:** Stock policy review for a product at a location.

| Rule | Review trigger | Thresholds aligned with lead time & demand | ABC class | Actions | Outcome |
|------|----------------|-------------------------------------------|-----------|---------|---------|
| R1 | New product | — | — | Set conservative initial thresholds; schedule 90-day review | Interim policy active |
| R2 | Chronic stockout | N | — | Recalculate; increase reorder level or safety stock; notify purchasing | Revised policy — stockout mitigation |
| R3 | Chronic overstock | N | — | Reduce thresholds; consider rebalancing or promotion | Revised policy — overstock mitigation |
| R4 | Any | Y | A | Approve thresholds; set priority alert treatment | Policy published — Class A monitoring |
| R5 | Any | Y | B or C | Approve thresholds; standard alert treatment | Policy published — standard monitoring |
| R6 | Any | N | — | Adjust and recalculate; resubmit to Operations Director | Policy not yet effective |

---

### BP-04: ABC Product Classification (DT-04)

**Decision context:** Semi-annual or ad-hoc ABC classification review.

| Rule | Data supports classification | Assigned class | Disputed | Actions | Outcome |
|------|------------------------------|----------------|----------|---------|---------|
| R1 | Y | A | N | Approve; increase count frequency and alert priority | Class A operational priority |
| R2 | Y | B | N | Approve; standard count and alert rules | Class B standard priority |
| R3 | Y | C | N | Approve; reduced count frequency | Class C low priority |
| R4 | N | — | Y | Escalate to Operations Director with business justification | Director decides final class |
| R5 | Any | Any | N | Defer operational rule update to next cycle | Classification saved; rules unchanged until next cycle |

---

## Domain 2: Inbound & Receiving

### BP-05: Purchase Order Placement (DT-05)

**Decision context:** Replenishment need validated; buyer prepares purchase order.

| Rule | Sufficient stock or open PO | Order value vs authority | Receiving capacity | Emergency | Actions | Outcome |
|------|----------------------------|--------------------------|-------------------|-----------|---------|---------|
| R1 | Y — sufficient stock | — | — | N | Cancel or reduce requisition; reference existing supply | No new PO |
| R2 | N | Within buyer authority | Y | N | Issue standard PO; record inbound commitment | Open PO — standard lead time |
| R3 | N | Exceeds buyer authority | Y | N | Escalate to Purchasing Manager or Finance for approval; then issue PO | Open PO — approved escalation |
| R4 | N | Any | N | N | Negotiate alternate delivery date with supplier | PO delayed — capacity conflict |
| R5 | N | Approved | Y | Y | Issue expedited PO; notify Operations Director; authorize premium freight if needed | Emergency PO placed |

---

### BP-06: Inbound Shipment Planning (DT-06)

**Decision context:** Supplier confirms shipment; inbound date approaching.

| Rule | Dock capacity available | Shipment aligns with PO | Priority SKU or stockout | Actions | Outcome |
|------|-------------------------|-------------------------|--------------------------|---------|---------|
| R1 | Y | Y | N | Schedule receiving resources; standard processing | Receiving prepared |
| R2 | Y | Y | Y | Schedule receiving; notify sales and operations of inbound ETA | Stakeholders informed — priority inbound |
| R3 | Y | N | — | Flag discrepancy for receiving; alert buyer | Receiving on alert — content mismatch expected |
| R4 | N | — | — | Request delivery reschedule from supplier | Inbound rescheduled |

---

### BP-07: Goods Receipt & Verification (DT-07)

**Decision context:** Supplier shipment arrives at receiving dock. *High-path process — full verification matrix.*

| Rule | Valid PO reference | Quantity matches PO | Product identity correct | Condition acceptable | Actions | Outcome |
|------|-------------------|---------------------|------------------------|---------------------|---------|---------|
| R1 | Y | Y | Y | Y | Record accepted quantity; create receipt; route to put-away | Clean receipt → BP-09 |
| R2 | N | — | — | — | Hold shipment; contact purchasing for PO or ad-hoc authorization | Receipt blocked — no PO |
| R3 | Y | N | Y | Y | Document quantity variance; accept verified quantity only | Partial receipt → BP-08 |
| R4 | Y | — | N | — | Reject wrong item; document discrepancy; do not add to inventory | Wrong item → BP-08 |
| R5 | Y | — | Y | N | Segregate damaged units; accept sound units if any; document damage | Damage discrepancy → BP-08 |
| R6 | Y | N | N | N | Document all variances; hold disputed quantity from sellable stock | Multi-issue receipt → BP-08 |

---

### BP-08: Receipt Discrepancy Resolution (DT-08)

**Decision context:** Discrepancy identified during goods receipt.

| Rule | Discrepancy type | Accept partial now | Supplier accepts claim | Actions | Outcome |
|------|------------------|-------------------|------------------------|---------|---------|
| R1 | Short shipment | Y | Y | Record partial receipt; pursue balance shipment or credit | Inventory updated — short resolved |
| R2 | Short shipment | N | — | Hold entire line; negotiate with supplier before acceptance | Receipt pending — full resolution |
| R3 | Over-shipment | Y | Y | Accept within tolerance or per approval; adjust PO/payment | Excess accepted or returned per agreement |
| R4 | Damage | Y | Y | Accept good units; reject damaged; initiate claim | Partial inventory — damage excluded |
| R5 | Wrong item | N | — | Reject wrong merchandise; return to supplier | No inventory impact — wrong item returned |
| R6 | Any | — | N (disputed) | Escalate to Purchasing Manager; withhold payment pending resolution | Dispute open — supplier negotiation |

---

### BP-09: Stock Put-Away & Storage (DT-09)

**Decision context:** Verified goods await placement in storage.

| Rule | Designated location available | Special handling required | Same-day put-away feasible | Actions | Outcome |
|------|------------------------------|---------------------------|------------------------------|---------|---------|
| R1 | Y | N | Y | Confirm put-away; increase ATP for quantity put away | Stock available for fulfillment |
| R2 | Y | Y | Y | Place in designated special-handling area; confirm put-away | Stock available — special location |
| R3 | N | — | Y | Assign alternate overflow location; plan rebalancing | Stock available — overflow location |
| R4 | Y | — | N | Leave in receiving status; queue for next shift put-away | Received but not yet available (BR-005) |

---

## Domain 3: Inventory Control

### BP-10: Inventory Status Monitoring (DT-10)

**Decision context:** Daily or event-driven inventory status review.

| Rule | ATP below reorder | ATP zero (stockout) | Overstock detected | Inbound expected soon | Actions | Outcome |
|------|-------------------|---------------------|--------------------|-----------------------|---------|---------|
| R1 | Y | N | N | — | Generate low-stock alert; route to BP-21 | Low-stock review triggered |
| R2 | — | Y | N | N | Urgent escalation; emergency replenishment or transfer | Stockout response — BP-21 / BP-24 |
| R3 | — | Y | N | Y | Monitor inbound; notify sales of ETA; defer emergency PO if inbound covers gap | Stockout mitigated by inbound |
| R4 | N | N | Y | — | Flag for network rebalancing review — BP-26 | Overstock flagged |
| R5 | N | N | N | — | Continue routine monitoring | Normal status |

---

### BP-11: Cycle Counting (DT-11)

**Decision context:** Scheduled or ad-hoc cycle count performed.

| Rule | Physical vs system within tolerance | Recount needed | Fulfillment active during count | Actions | Outcome |
|------|-------------------------------------|----------------|--------------------------------|---------|---------|
| R1 | Y | N | — | Close count task; no adjustment | Count confirmed — accurate |
| R2 | N | Y | — | Perform blind recount before submission | Recount in progress |
| R3 | N | N | Y | Record variance; continue operations; route material variance to BP-13 | Variance investigation triggered |
| R4 | N | N | N | Count during low-activity window; record variance | Variance recorded — minimal disruption |

---

### BP-12: Full Physical Inventory Count (DT-12)

**Decision context:** Full wall-to-wall count at a location.

| Rule | Location prepared | All SKUs counted | Total variance within range | Financial adjustment needed | Actions | Outcome |
|------|-------------------|------------------|---------------------------|------------------------------|---------|---------|
| R1 | N | — | — | — | Reschedule count; complete preparation | Count deferred |
| R2 | Y | N | — | — | Identify gaps; recount missing areas | Count incomplete |
| R3 | Y | Y | Y | N | Certify baseline; lift movement freeze | Location accuracy certified |
| R4 | Y | Y | N | Y | Investigate material variances; approve adjustments — BP-13/BP-14 | Baseline corrected — financial impact |
| R5 | Y | Y | N | N | Full investigation before close | Investigation required — BP-13 |

---

### BP-13: Count Variance Investigation & Approval (DT-13)

**Decision context:** Material count variance identified.

| Rule | Recount confirms variance | Root cause identified | Within approver authority | Segregation OK (counter ≠ approver) | Actions | Outcome |
|------|---------------------------|----------------------|---------------------------|-------------------------------------|---------|---------|
| R1 | N | — | — | — | Dispute variance; order additional recount | Investigation continues |
| R2 | Y | Y | Y | Y | Approve adjustment with reason code and documentation | Inventory corrected — explained |
| R3 | Y | Y | N | Y | Escalate to Operations Director for approval | Pending executive approval |
| R4 | Y | N | — | Y | Escalate unexplained variance; loss prevention review if warranted | Unexplained variance — BP-15 |
| R5 | Y | Y | Y | N | Reassign to independent approver per BR-019 | Independent approval required |
| R6 | Y | Any | — | — | Reject adjustment; continue investigation | No inventory change |

---

### BP-14: Stock Adjustment & Write-Off (DT-14)

**Decision context:** Inventory balance change required (correction, damage, shrinkage, obsolescence).

| Rule | Reason code & evidence sufficient | Value within approver authority | Write-off required | Segregation of duties satisfied | Actions | Outcome |
|------|-----------------------------------|--------------------------------|------------------|-----------------------------------|---------|---------|
| R1 | N | — | — | — | Return to initiator for documentation | Adjustment not applied |
| R2 | Y | Y | N | Y | Approve correction; update on-hand and ATP | Routine adjustment applied |
| R3 | Y | N | N | Y | Escalate to Operations Director or COO | Pending high-value approval |
| R4 | Y | Y | Y | Y | Approve write-off; notify finance; remove from sellable stock | Write-off applied — financial treatment |
| R5 | Y | — | — | N | Reassign to independent approver | SOD block — rerouted approval |
| R6 | Y | N | Y | Y | Executive and finance approval for material write-off | Material write-off pending |

---

### BP-15: Shrinkage & Loss Management (DT-15)

**Decision context:** Periodic shrinkage review identifies abnormal loss pattern.

| Rule | Shrinkage within threshold | Root cause type | Corrective action defined | Actions | Outcome |
|------|---------------------------|-----------------|---------------------------|---------|---------|
| R1 | Y | — | — | Monitor; document in review cycle | Normal shrinkage — no action |
| R2 | N | Operational | Y | Implement process fix or training; follow up next cycle | Corrective plan active |
| R3 | N | Criminal suspected | — | Escalate to loss prevention and Internal Auditor | Security investigation |
| R4 | N | Supplier-related | — | Initiate supplier quality or receipt review with purchasing | Supplier corrective action |
| R5 | N | — | N | Continue monitoring; escalate to Operations Director | Extended review period |

---

## Domain 4: Order Fulfillment

### BP-16: Order Availability Confirmation (DT-16)

**Decision context:** Customer order or quote requires availability check before commitment.

| Rule | ATP sufficient at primary location | Network ATP sufficient | Inbound arrives in time | Customer accepts partial/delay | Actions | Outcome |
|------|-----------------------------------|------------------------|-------------------------|-------------------------------|---------|---------|
| R1 | Y | — | — | — | Confirm full order; commit delivery date; proceed to BP-17 | Full availability confirmed |
| R2 | N | Y | — | — | Evaluate alternate location or split fulfillment — BP-24 / BP-17 | Multi-location fulfillment path |
| R3 | N | N | Y | — | Commit with inbound-backed date; disclose timing to customer | Delayed commitment — inbound dependent |
| R4 | N | N | N | Y | Offer partial ship and/or backorder with acknowledgment — BP-19 | Partial or backorder path |
| R5 | N | N | N | N | Decline or revise order; alert replenishment — BP-21 | Order not confirmed as requested |

---

### BP-17: Inventory Reservation (DT-17)

**Decision context:** Confirmed order requires stock reservation.

| Rule | Full ATP available | Partial ATP only | Priority order | Safety stock impact | Actions | Outcome |
|------|-------------------|------------------|----------------|---------------------|---------|---------|
| R1 | Y | N | N | N | Reserve full quantity at selected location; queue for pick | Full reservation — BP-18 |
| R2 | Y | N | Y | N | Reserve full quantity; place in priority pick queue | Priority reservation |
| R3 | N | Y | — | N | Reserve available portion; route remainder to BP-19 | Partial reservation |
| R4 | N | N | — | Y | Block unless authorized safety stock exception with replenishment plan | Reservation blocked — BR-010 |
| R5 | N | N | — | N | Release confirmation; return to BP-16 for renegotiation | Reservation failed — availability changed |

---

### BP-18: Pick, Pack & Ship (DT-18)

**Decision context:** Reserved order released to warehouse for physical fulfillment.

| Rule | Full quantity locatable | Product condition OK | Order packed complete | Expedited shipment | Actions | Outcome |
|------|-------------------------|---------------------|----------------------|-------------------|---------|---------|
| R1 | Y | Y | Y | N | Verify pick; pack; ship; deduct inventory; confirm shipment | Order shipped — complete |
| R2 | Y | Y | Y | Y | Expedited carrier handoff; document premium freight authorization | Priority shipment complete |
| R3 | Y | Y | N | — | Hold shipment; wait for remaining lines or partial ship per BP-19 | Shipment held — partial |
| R4 | N | — | — | — | Report pick exception — BP-20 | Pick failure path |
| R5 | Y | N | — | — | Quarantine damaged unit; re-pick or exception — BP-20 | Damage exception path |

---

### BP-19: Partial Fulfillment & Backorder Management (DT-19)

**Decision context:** Full order quantity cannot be fulfilled immediately.

| Rule | Customer accepts partial | Replenishment ETA known | Network transfer faster than PO | Actions | Outcome |
|------|-------------------------|-------------------------|--------------------------------|---------|---------|
| R1 | Y | Y | — | Ship available now; backorder remainder with communicated ETA; alert purchasing | Partial shipped — backorder tracked |
| R2 | Y | N | — | Ship partial; provide ETA range or cancel option for remainder | Partial shipped — uncertain backorder |
| R3 | N | — | — | Hold full order or cancel per customer preference; release reservation if cancelled | Order held or cancelled |
| R4 | Y | — | Y | Initiate emergency transfer — BP-24; ship when transfer received | Backorder resolved by transfer |
| R5 | Y | Y | N | Place replenishment priority; auto-reserve inbound to backorder queue — BP-17 | Backorder awaiting supplier stock |

---

### BP-20: Outbound Exception Handling (DT-20)

**Decision context:** Fulfillment disruption during pick, pack, or ship.

| Rule | Exception type | Order still fulfillable | Record inaccurate | Customer accepts substitute | Actions | Outcome |
|------|----------------|------------------------|-------------------|----------------------------|---------|---------|
| R1 | Stock not found | Y (re-pick) | Y | — | Search location; adjust inventory; re-queue pick | Inventory corrected — order continues |
| R2 | Stock not found | N | Y | — | Adjust inventory; cancel or partial per customer | Order revised — record fixed |
| R3 | Damage at pick | Y | — | — | Quarantine; re-pick from alternate stock | Order continues |
| R4 | Damage at pick | N | — | Y | Ship approved substitute with documentation | Substitute shipped |
| R5 | Customer cancellation | — | — | — | Release reservation; return picked goods to stock if applicable | Order cancelled |
| R6 | Carrier failure | Y | — | — | Rebook carrier; maintain shipment ready state | Shipment delayed — rebooked |

---

## Domain 5: Replenishment

### BP-21: Low-Stock Alert Review (DT-21)

**Decision context:** Low-stock or out-of-stock alert requires purchasing response.

| Rule | Alert valid (not false positive) | Open PO covers need | Network transfer faster | Priority SKU | Actions | Outcome |
|------|----------------------------------|--------------------|-------------------------|--------------|---------|---------|
| R1 | N | — | — | — | Dismiss with documented reason; review thresholds if recurring | Alert closed — no action |
| R2 | Y | Y | — | — | Monitor open PO; track inbound — BP-23 | Awaiting inbound supply |
| R3 | Y | N | Y | — | Initiate transfer request — BP-24 | Transfer path |
| R4 | Y | N | N | Y | Emergency escalation; expedited PO or transfer | Emergency replenishment |
| R5 | Y | N | N | N | Forward to replenishment planning — BP-22 | Standard replenishment path |

---

### BP-22: Replenishment Planning & Requisition (DT-22)

**Decision context:** Validated replenishment need converted to purchase requisition.

| Rule | Budget available | Requisition within PM authority | Multiple SKUs same supplier | Promotional pre-build | Actions | Outcome |
|------|------------------|--------------------------------|----------------------------|----------------------|---------|---------|
| R1 | N | — | — | — | Defer or reduce quantity; inform sales and operations | Replenishment deferred |
| R2 | Y | Y | N | N | Approve requisition; hand to BP-05 for PO | Requisition approved — PO path |
| R3 | Y | N | — | — | Escalate to Finance or COO per value | Pending executive approval |
| R4 | Y | Y | Y | — | Consolidate into single supplier order | Combined PO requisition |
| R5 | Y | Y | — | Y | Approve larger pre-build per campaign plan — BP-31 | Promotional replenishment |

---

### BP-23: Inbound Supply Tracking (DT-23)

**Decision context:** Open purchase order monitored for delivery performance.

| Rule | Delivery on schedule | Delay material to stockout | Alternative supply viable | Actions | Outcome |
|------|---------------------|---------------------------|--------------------------|---------|---------|
| R1 | Y | — | — | Continue routine monitoring until receipt | On track |
| R2 | N | N | — | Follow up with supplier; update ETA | Minor delay — tracked |
| R3 | N | Y | Y | Expedite, alternate supplier, or network transfer; notify sales | Critical delay — mitigation active |
| R4 | N | Y | N | Notify operations and customer service; revise customer commitments | Delay communicated — wait |
| R5 | Received | — | — | Close PO line; trigger backorder fulfillment — BP-17 if applicable | Supply arrived |

---

## Domain 6: Network Balance

### BP-24: Inter-Location Transfer Request (DT-24)

**Decision context:** Stock movement requested between locations.

| Rule | Source has unreserved excess | Transfer vs purchase justified | Within WM authority | Urgent stockout at destination | Source minimum protected | Actions | Outcome |
|------|---------------------------|-------------------------------|---------------------|-------------------------------|-------------------------|---------|---------|
| R1 | N | — | — | — | — | Reject; document reason; pursue purchase — BP-22 | Transfer rejected |
| R2 | Y | N | — | — | — | Reject; wait for supplier replenishment | Purchase preferred |
| R3 | Y | Y | Y | N | Y | Approve standard transfer — BP-25 | Transfer approved |
| R4 | Y | Y | N | — | Y | Escalate to Operations Director for approval | Pending executive approval |
| R5 | Y | Y | — | Y | Y | Expedite approval and execution | Emergency transfer |
| R6 | Y | Y | — | — | N | Reduce quantity to maximum spareable; approve modified transfer | Partial transfer approved (BR-012) |

---

### BP-25: Inter-Location Transfer Execution (DT-25)

**Decision context:** Approved transfer physically executed.

| Rule | Source can ship full qty | Receipt matches dispatch | Condition at receipt | Actions | Outcome |
|------|-------------------------|--------------------------|---------------------|---------|---------|
| R1 | Y | Y | Acceptable | Dispatch; receive; update both locations; close transfer | Transfer complete — balances correct |
| R2 | Y | N | — | Investigate variance; adjust records; possible write-off | Transfer variance — investigation |
| R3 | N | — | — | Ship partial; notify destination; cancel or re-request remainder | Partial transfer executed |
| R4 | Y | Y | Damaged | Accept sound units; write off damaged; document transit loss | Partial receipt — damage adjustment |

---

### BP-26: Network Stock Rebalancing (DT-26)

**Decision context:** Network review identifies persistent imbalance.

| Rule | Imbalance warrants transfer cost | Inbound PO resolves soon | Plan size | Actions | Outcome |
|------|----------------------------------|-------------------------|-----------|---------|---------|
| R1 | N | Y | — | Monitor; adjust PO destination allocation | No transfer — inbound fix |
| R2 | N | N | — | Continue monitoring; review next cycle | Defer rebalancing |
| R3 | Y | — | Standard | Operations Director approves; initiate BP-24/BP-25 transfers | Rebalancing executed |
| R4 | Y | — | Large network move | COO approves; coordinated multi-location transfers | Executive-approved rebalancing |
| R5 | Y | — | Any | Update location-specific replenishment to prevent recurrence | Policy adjusted — transfer executed |

---

## Domain 7: Returns

### BP-27: Customer Return Intake (DT-27)

**Decision context:** Customer requests return.

| Rule | Eligible per policy | Resolution type | Replacement ATP available | Return channel | Actions | Outcome |
|------|---------------------|-----------------|---------------------------|----------------|---------|---------|
| R1 | N | — | — | — | Deny with explanation; document decision | Return denied |
| R2 | Y | Refund | — | Ship | Issue RA; notify warehouse and finance | Return authorized — refund path |
| R3 | Y | Replacement | Y | — | Issue RA; place replacement order — BP-16 | Return authorized — replacement shipped |
| R4 | Y | Replacement | N | — | Issue RA; backorder replacement | Return authorized — replacement backordered |
| R5 | Y | Store credit | — | Store drop-off | Issue RA; route to store then warehouse | Store return path |

---

### BP-28: Return-to-Stock or Disposal (DT-28)

**Decision context:** Returned goods received and inspected.

| Rule | Matches authorization | Condition for resale | Quarantine required | Actions | Outcome |
|------|----------------------|---------------------|---------------------|---------|---------|
| R1 | N | — | — | Contact customer; hold goods; resolve mismatch | Return mismatch — CS intervention |
| R2 | Y | Resalable | N | Restock to sellable inventory; process refund/credit | Return complete — stock recovered |
| R3 | Y | Not resalable | N | Write off with return reason code; process refund per policy | Return complete — stock written off |
| R4 | Y | Pending | Y | Hold in quarantine; inspect; disposition after outcome | Inspection pending — quarantined |
| R5 | Y | Rework possible | — | Route to rework; restock if passes secondary inspection | Rework path |

---

## Domain 8: Performance, Financial & Governance

### BP-29: Inventory Performance Reporting (DT-29)

**Decision context:** Scheduled or ad-hoc reporting cycle.

| Rule | KPI breach | Audience | Data anomaly found | Actions | Outcome |
|------|-----------|----------|-------------------|---------|---------|
| R1 | Y | Executive | N | Escalate; assign corrective action owner | Management intervention triggered |
| R2 | N | Operational | N | Distribute operational detail report | Routine reporting |
| R3 | N | Management | N | Distribute management summary | Standard management review |
| R4 | — | Executive | N | Distribute executive dashboard | Executive visibility |
| R5 | — | — | Y | Investigate before distribution; or distribute with data caveat | Qualified report issued |

---

### BP-30: Inventory Valuation & Financial Reconciliation (DT-30)

**Decision context:** Month-end operational vs finance inventory reconciliation.

| Rule | Variance within tolerance | Timing difference explains gap | Operational correction needed | Actions | Outcome |
|------|---------------------------|-------------------------------|------------------------------|---------|---------|
| R1 | Y | — | — | Accept reconciliation; support financial posting | Clean close |
| R2 | N | Y | N | Document timing explanation; reconcile without ops change | Explained timing variance |
| R3 | N | N | Y | Initiate BP-14 adjustments; re-reconcile | Ops correction before close |
| R4 | N | N | N | Hold financial posting; escalate to CFO and Operations Director | Close blocked — investigation |
| R5 | Y | — | — | CFO approves; archive substantiation for audit | Reconciliation approved |

---

### BP-31: Promotional & Launch Stock Readiness (DT-31)

**Decision context:** Campaign or launch approaching; stock readiness assessed.

| Rule | Current + inbound sufficient | Gap closable before launch | Ops capacity for surge | Actions | Outcome |
|------|------------------------------|---------------------------|------------------------|---------|---------|
| R1 | Y | — | Y | Go decision; ring-fence promotional stock — BR-029 | Launch ready — go |
| R2 | N | Y | Y | Expedite pre-build PO; proceed with risk note | Launch proceed — mitigated gap |
| R3 | N | N | — | Delay campaign or reduce scope | Launch delayed or reduced |
| R4 | — | — | N | Limit promotion intensity or add fulfillment capacity | Launch conditional — capacity constraint |
| R5 | N | Y | N | Go with fulfillment risk acceptance documented | Launch proceed — ops risk accepted |

---

### BP-32: Inventory Audit & Control Review (DT-32)

**Decision context:** Internal or external audit of inventory controls.

| Rule | Controls effective | Finding material | Corrective action needed | External audit risk | Actions | Outcome |
|------|-------------------|------------------|--------------------------|---------------------|---------|---------|
| R1 | Y | — | — | — | Document clean audit; no action | Controls effective |
| R2 | N | N | Process improvement | N | Assign improvement actions; follow up next cycle | Minor remediation |
| R3 | N | Y | Immediate | Y | Escalate to COO and CFO; accelerated remediation | Material finding — executive escalation |
| R4 | N | Y | Policy update | N | Update governance policies — BP-03/BP-12; retrain | Policy remediation |
| R5 | — | — | — | Y | Prepare evidence package; support external auditor | External audit support |

---

## Cross-Process Decision Flow Summary

High-frequency decision chains across processes:

```text
Goods Receipt (BP-07)
  ├─ Clean → Put-Away (BP-09) → Available
  └─ Variance → Discrepancy (BP-08) → Resolved receipt

Order Intake (BP-16)
  ├─ Full ATP → Reserve (BP-17) → Pick/Ship (BP-18)
  ├─ Partial ATP → Partial/Backorder (BP-19)
  └─ No ATP → Replenish (BP-21) or Transfer (BP-24)

Low Stock (BP-21)
  ├─ False alert → Dismiss
  ├─ Open PO → Track (BP-23)
  ├─ Network stock → Transfer (BP-24)
  └─ No network stock → Requisition (BP-22) → PO (BP-05)

Count Variance (BP-11/12)
  └─ Material variance → Investigate (BP-13)
        ├─ Approved → Adjust (BP-14)
        └─ Rejected → Continue investigation
```

---

## Traceability Reference

| Source | Identifier |
|--------|------------|
| Business Processes | BP-01 – BP-32 |
| Business Workflows | WF-01 – WF-32 |
| Business Rules | BR-001 – BR-032 |
| Business Exception Scenarios | EX-001 – EX-043 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Business Analyst | | | |
| Product Owner | | | |
| Operations Director | | | |

---

*End of Business Process Decision Tables*

*Document ID: SRS-DT-001 | Version 1.0 | July 5, 2026*
