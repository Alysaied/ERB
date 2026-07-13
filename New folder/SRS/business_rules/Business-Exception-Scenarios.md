# Business Exception Scenarios Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-EX-001 |
| **Document Title** | Business Exception Scenarios — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Business Analyst |
| **Source Documents** | BRD-IMS-001, Business Events Catalog (BE-01–BE-59), Business Workflows (WF-01–WF-32), Common Inventory Management Scenarios, Business Rules (BR-001–BR-032) |
| **Date** | July 5, 2026 |
| **Scope** | Business exception behavior only — not technical error handling, system faults, or implementation recovery |

### Purpose

This document identifies **exception scenarios** — situations that deviate from the standard happy-path inventory process and require defined business judgment, escalation, and response. Exceptions are normal operational events, not system failures. Each scenario describes what the business should do when the exception occurs.

### How to Read Each Exception

| Field | Meaning |
|-------|---------|
| **Exception ID** | Unique identifier (EX-001, EX-002, …) |
| **Business Scenario** | What is happening from a business perspective |
| **Trigger** | Event or condition that causes the exception |
| **Expected Business Response** | What the organization should do — policies and actions |
| **Responsible Actor** | Primary role accountable for resolution |
| **Business Impact** | Consequences if not handled correctly |

### Related Business Event Reference

Where applicable, exceptions map to the Business Events Catalog (BE-xx) and Business Processes (BP-xx).

---

## Domain 1: Master Data & Governance Exceptions

### EX-001 — Duplicate Product Identity Detected

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-001 |
| **Business Scenario** | A new product submission matches or closely resembles an existing SKU, barcode, or product name, risking parallel product identities for the same physical item. |
| **Trigger** | Inventory Controller or stakeholder attempts to create or update a product record (BE-02, BE-01). |
| **Expected Business Response** | Halt new record creation; compare existing and proposed records side by side; merge or correct the existing record rather than create a duplicate; document justification if a genuinely new SKU is confirmed. |
| **Responsible Actor** | Inventory Controller |
| **Business Impact** | Fragmented stock records; inaccurate ATP; duplicate purchasing; reconciliation effort; unreliable network visibility |

---

### EX-002 — Discontinued Product With Open Activity

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-002 |
| **Business Scenario** | A product marked for discontinuation still has open purchase orders, active reservations, or remaining on-hand stock requiring disposition. |
| **Trigger** | Product discontinuation requested (BE-03). |
| **Expected Business Response** | Block new replenishment per BR-027; warn stakeholders of dependent open POs and reservations; define runout timeline for remaining stock; cancel or amend open POs; fulfill or release existing reservations per policy; plan clearance or write-off for residual quantity. |
| **Responsible Actor** | Inventory Controller (with Purchasing Manager and Operations Director) |
| **Business Impact** | Obsolete inventory accumulation; customer orders for withdrawn products; trapped working capital; conflicting assortment decisions |

---

### EX-003 — Location Closure With Remaining Stock

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-003 |
| **Business Scenario** | A warehouse or store approved for closure still holds on-hand inventory that must be dispositioned before deactivation. |
| **Trigger** | Inventory location change approved for closure (BE-04). |
| **Expected Business Response** | List all remaining stock; execute disposition plan (transfer out, sell-through, write-off); block new inbound and fulfillment except authorized disposition; obtain Operations Director sign-off before location deactivation. |
| **Responsible Actor** | Operations Director |
| **Business Impact** | Stranded inventory; orphaned records; financial misstatement; lost asset value |

---

### EX-004 — Opening Balance Dispute at Go-Live

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-004 |
| **Business Scenario** | Physical opening count results for a new or cutover location are challenged by local management or finance before location activation. |
| **Trigger** | Opening stock balance submitted for approval (BP-02, BP-12). |
| **Expected Business Response** | Suspend location activation; conduct recount or independent verification for disputed SKUs; resolve catalog gaps for unknown products; require authorized approver sign-off on final baseline before operational transactions begin. |
| **Responsible Actor** | Inventory Controller |
| **Business Impact** | Go-live with embedded errors; chronic inaccuracy from day one; distrust in system data; cascading fulfillment failures |

---

## Domain 2: Inbound & Procurement Exceptions

### EX-005 — Supplier Short-Shipment

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-005 |
| **Business Scenario** | Supplier delivers fewer units than ordered on a purchase order, especially for a product already low or committed to customer orders. |
| **Trigger** | Receipt verification finds quantity below PO expected quantity (BE-15). |
| **Expected Business Response** | Record only verified received quantity; document short-shipment discrepancy; exclude disputed quantity from sellable stock; escalate with supplier for balance; recalculate ATP and customer commitments; hold payment pending three-way match resolution per BR-008. |
| **Responsible Actor** | Receiving Clerk (document) → Purchasing Manager (supplier resolution) |
| **Business Impact** | Phantom inventory if PO quantity accepted silently; stockouts on committed orders; supplier accountability lost; payment for undelivered goods |

---

### EX-006 — Damaged Goods at Receiving

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-006 |
| **Business Scenario** | Inbound shipment arrives with visible damage — crushed cartons, broken units, or temperature excursion — making some or all units unsellable. |
| **Trigger** | Receiving clerk inspects packaging and product condition (BE-14, BE-15). |
| **Expected Business Response** | Segregate damaged goods; accept only sellable units into inventory; photograph and document damage; initiate supplier or carrier claim; quarantine damaged quantity; exclude damaged stock from ATP per BR-013. |
| **Responsible Actor** | Receiving Clerk → Warehouse Manager |
| **Business Impact** | Defective goods sold to customers; returns and brand damage; unrecoverable supplier claims without dock evidence; inflated on-hand balances |

---

### EX-007 — Wrong Item Received Against Purchase Order

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-007 |
| **Business Scenario** | Physical product delivered does not match the purchase order line — different SKU, variant, or entirely wrong merchandise. |
| **Trigger** | Product identity verification fails during goods receipt (BE-15). |
| **Expected Business Response** | Reject mismatched product from inventory acceptance; document wrong-item discrepancy; notify purchasing and supplier; accept only correct items if partial shipment; do not record wrong SKU as on-hand. |
| **Responsible Actor** | Receiving Clerk → Buyer |
| **Business Impact** | Inventory records show stock that cannot be fulfilled; customer orders fail at pick; supplier dispute without documentation; payment for wrong goods |

---

### EX-008 — Receipt Without Valid Purchase Order

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-008 |
| **Business Scenario** | Supplier truck arrives with no matching open purchase order, or emergency delivery requires receipt outside standard procurement. |
| **Trigger** | Receiving initiated without PO reference (BE-14). |
| **Expected Business Response** | Hold shipment until purchasing confirms valid PO or grants authorized ad-hoc exception with documented approver and reason per BR-007; record exception for audit; do not accept standard supplier receipt without authorization. |
| **Responsible Actor** | Receiving Clerk → Purchasing Manager |
| **Business Impact** | Unauthorized spending; maverick buying; three-way match failure; audit control weakness |

---

### EX-009 — Over-Shipment Beyond Tolerance

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-009 |
| **Business Scenario** | Supplier delivers more units than ordered beyond the business-defined receipt tolerance. |
| **Trigger** | Received quantity exceeds PO open quantity plus tolerance (BE-15). |
| **Expected Business Response** | Flag over-receipt; require Warehouse Manager or Purchasing Manager approval before acceptance; document decision to accept excess, return excess, or create supplemental PO; adjust payment only for accepted quantity. |
| **Responsible Actor** | Receiving Clerk → Warehouse Manager / Purchasing Manager |
| **Business Impact** | Unplanned inventory investment; payment for unapproved goods; storage capacity strain; supplier assumes over-shipment is always accepted |

---

### EX-010 — Inbound Delivery Delayed Past Customer Promise

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-010 |
| **Business Scenario** | Purchase order or transfer shipment is delayed past the date already communicated to customers waiting on backorders or scheduled deliveries. |
| **Trigger** | Supplier or carrier reports delay; expected delivery date passes without receipt (BE-39). |
| **Expected Business Response** | Update expected arrival internally; proactively notify affected customers of revised dates; escalate with supplier; evaluate network transfer or alternate supply for critical commitments; reassess backorder queue priorities. |
| **Responsible Actor** | Buyer → Customer Service Representative |
| **Business Impact** | Silent delay destroys customer trust; backorder cancellations; contract penalties; emergency procurement at premium cost |

---

### EX-011 — Supplier Lead Time Extension

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-011 |
| **Business Scenario** | Supplier communicates longer lead times due to capacity, material, or logistics disruption, invalidating current reorder points and safety stock. |
| **Trigger** | Demand or supply condition changed (BE-06); supplier notification during inbound tracking (BE-39). |
| **Expected Business Response** | Recalculate reorder levels and safety stock for affected products; place orders earlier; inform sales of longer delivery windows; evaluate alternate suppliers for critical SKUs; document policy revision effective date. |
| **Responsible Actor** | Inventory Controller → Purchasing Manager |
| **Business Impact** | Preventable stockouts despite alerts; false confidence in replenishment timing; working capital shock if reactive safety stock increase |

---

## Domain 3: Inventory Control & Accuracy Exceptions

### EX-012 — Material Cycle Count Variance

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-012 |
| **Business Scenario** | Cycle count finds physical quantity differs from recorded balance beyond defined tolerance. |
| **Trigger** | Count variance identified after blind count submission (BE-24). |
| **Expected Business Response** | Order recount if needed; investigate root cause before adjustment per BR-022; document investigation notes; route to independent approver per BR-019; apply adjustment with mandatory reason code per BR-020. |
| **Responsible Actor** | Warehouse Manager → Inventory Controller |
| **Business Impact** | Recurring variances if root cause ignored; accuracy metrics meaningless; audit findings; undetected shrinkage or process failure |

---

### EX-013 — Phantom Inventory (Record Shows Stock, Shelf Empty)

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-013 |
| **Business Scenario** | System shows positive available quantity but product cannot be found physically — empty pick location, bare shelf, or customer cannot locate item. |
| **Trigger** | Pick exception reported (BE-33); customer or sales inquiry; verification count flagged (BE-21). |
| **Expected Business Response** | Conduct physical search including overflow and mislabeled locations; if not found, adjust inventory with shrinkage or count correction reason code immediately; correct ATP to prevent further overselling; investigate root cause (theft, misplacement, unrecorded movement). |
| **Responsible Actor** | Warehouse Manager → Inventory Controller |
| **Business Impact** | Continued overselling; pick failures; customer embarrassment; lost sales despite "in stock" status; eroded data trust |

---

### EX-014 — Unexplained Shrinkage Trend at Location

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-014 |
| **Business Scenario** | A location shows rising shrinkage, write-offs, or negative adjustments exceeding its historical norm and network average without a single large incident. |
| **Trigger** | Significant loss or adjustment event; monthly shrinkage review (BE-26, BE-27). |
| **Expected Business Response** | Analyze trends by SKU, reason code, and shift; conduct process and security review; increase count frequency for affected categories; assign corrective action owner; escalate to Internal Auditor if suspected fraud. |
| **Responsible Actor** | Inventory Controller → Operations Director |
| **Business Impact** | Escalating unexplained loss; margin erosion; audit material weakness; chronic accuracy failure at location |

---

### EX-015 — Quality Hold on Received Lot

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-015 |
| **Business Scenario** | Inbound lot fails inspection, receives supplier quality alert, or is flagged for investigation before release to sellable stock. |
| **Trigger** | Quality concern at receipt or post-receipt inspection. |
| **Expected Business Response** | Move lot to quarantine; exclude from ATP immediately per BR-013; investigate with supplier; disposition as release, return, rework, or write-off with documented authorization; reassess customer orders depending on quarantined lot. |
| **Responsible Actor** | Warehouse Manager → Inventory Controller |
| **Business Impact** | Shipping defective or non-compliant product; regulatory exposure; customer safety risk; recall scope expansion |

---

### EX-016 — Full Physical Count Material Variance

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-016 |
| **Business Scenario** | Full wall-to-wall count produces location-wide variance exceeding acceptable threshold for financial substantiation. |
| **Trigger** | Full physical count completed (BE-22, BE-23). |
| **Expected Business Response** | Investigate significant line items; escalate to Operations Director and Finance; apply approved adjustments with full documentation; identify systemic causes; agree corrected baseline with finance before close. |
| **Responsible Actor** | Inventory Controller → Operations Director / Finance Manager |
| **Business Impact** | Financial misstatement; audit qualification; delayed month-end close; loss of inventory baseline credibility |

---

## Domain 4: Order Fulfillment Exceptions

### EX-017 — Customer Order Exceeds Available-to-Promise

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-017 |
| **Business Scenario** | Customer order or sales quote requests quantity greater than current ATP at the fulfillment location, including cumulative effect of multiple orders against limited stock. |
| **Trigger** | Customer order or quote received (BE-28); large or strategic order submitted (BE-29). |
| **Expected Business Response** | Confirm only fulfillable quantity against ATP per BR-001; offer partial shipment, backorder with customer acknowledgment per BR-028, alternate location, or revised delivery date; do not confirm full order without documented plan; reserve only accepted quantity per BR-002. |
| **Responsible Actor** | Sales Representative / Customer Service Representative |
| **Business Impact** | Overselling; order cancellations; pick failures; customer complaints; expedited shipping costs; damaged sales credibility |

---

### EX-018 — Pick Failure — Stock Not Found at Location

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-018 |
| **Business Scenario** | Picker cannot locate reserved quantity at the designated storage location despite positive system record. |
| **Trigger** | Pick exception reported during fulfillment (BE-33). |
| **Expected Business Response** | Conduct immediate physical search; if unfound, trigger phantom inventory response (EX-013); re-pick if found elsewhere; initiate partial fulfillment or order line cancellation if unrecoverable; do not ship without verified pick per BR-003. |
| **Responsible Actor** | Warehouse Picker / Packer → Warehouse Manager |
| **Business Impact** | Shipment delay; wrong inventory record persists; customer promise missed; cascading pick queue disruption |

---

### EX-019 — Damaged Item Discovered During Pick

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-019 |
| **Business Scenario** | Product retrieved for order is damaged, expired, or otherwise unsellable at the pick point. |
| **Trigger** | Picker reports condition exception during pick verification (BE-33). |
| **Expected Business Response** | Quarantine damaged unit; process stock adjustment or write-off with reason code; attempt re-pick from alternate stock if available; substitute only with authorized approval; notify customer service if order affected. |
| **Responsible Actor** | Warehouse Picker / Packer → Warehouse Manager |
| **Business Impact** | Wrong or damaged goods shipped if ignored; customer return; brand damage; compounding record inaccuracy |

---

### EX-020 — Concurrent Demand for Last Available Units

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-020 |
| **Business Scenario** | Multiple customers, channels, or locations simultaneously require the last available units of a product — total demand exceeds remaining ATP. |
| **Trigger** | Multiple simultaneous availability confirmations or reservations against depleting ATP (BE-28, BE-30). |
| **Expected Business Response** | Apply documented allocation priority rules (contract obligation, customer tier, order date, channel priority); hard-reserve allocated quantity; communicate honestly with deprioritized parties; record allocation decision and rationale; do not award stock ad hoc under pressure. |
| **Responsible Actor** | Inventory Controller / Sales Manager |
| **Business Impact** | Arbitrary fulfillment; B2B contract breach; channel conflict; customer disputes; revenue loss on strategic accounts |

---

### EX-021 — Customer Order Cancelled After Reservation

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-021 |
| **Business Scenario** | Customer cancels order or reduces quantity after stock was reserved but before shipment. |
| **Trigger** | Customer order cancelled (BE-35). |
| **Expected Business Response** | Release reservation to restore ATP; return picked but unshipped goods to stock if applicable; record cancellation reason; notify operations if material quantity restored; update fulfillment status for customer service. |
| **Responsible Actor** | Customer Service Representative → Warehouse Manager |
| **Business Impact** | Stock artificially locked to dead orders; false stockouts; reduced sellable availability; fulfillment queue clutter |

---

### EX-022 — Partial Fulfillment Required

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-022 |
| **Business Scenario** | Full order quantity cannot be fulfilled at reservation or pick time, but customer policy allows partial delivery. |
| **Trigger** | Insufficient stock at fulfillment (BE-34). |
| **Expected Business Response** | Identify fulfillable vs. unfulfillable quantity; obtain customer acknowledgment before partial ship per BR-028; ship available portion; place remainder on backorder with ETA or cancellation option; alert purchasing for replenishment. |
| **Responsible Actor** | Customer Service Representative → Warehouse Manager |
| **Business Impact** | Complete order hold loses partial revenue; silent partial ship without acknowledgment causes disputes; backorder queue unmanaged |

---

### EX-023 — Authorized Product Substitution Required

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-023 |
| **Business Scenario** | Primary ordered SKU is unavailable at pick, but an approved alternate product could satisfy the customer need. |
| **Trigger** | Pick exception or availability shortfall with defined substitute relationship (BE-33). |
| **Expected Business Response** | Present only pre-approved substitute options; obtain customer acceptance and authorized approval; reserve and ship substitute SKU; record substitution on order with original and fulfilled product reference; adjust inventory for actual product shipped. |
| **Responsible Actor** | Warehouse Manager → Sales Manager / Customer Service Representative |
| **Business Impact** | Unauthorized substitute causes margin loss, warranty issues, or customer rejection; order remains unfulfilled if substitution declined without plan |

---

## Domain 5: Replenishment Exceptions

### EX-024 — False Positive Low-Stock Alert

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-024 |
| **Business Scenario** | Low-stock alert fires but investigation shows adequate stock, inbound supply en route, or data timing issue — no genuine replenishment need. |
| **Trigger** | Low-stock alert issued (BE-36); purchasing daily review. |
| **Expected Business Response** | Validate against ATP, open POs, and in-transit transfers; dismiss alert with documented reason; review threshold configuration if recurring false positives; do not place duplicate purchase order. |
| **Responsible Actor** | Buyer / Purchasing Manager |
| **Business Impact** | Duplicate procurement; excess inventory; alert fatigue; ignored genuine alerts later |

---

### EX-025 — Emergency Stockout on Priority SKU

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-025 |
| **Business Scenario** | Class A or priority product reaches zero ATP with active customer demand or open commitments. |
| **Trigger** | Emergency stockout declared (BE-10); stock threshold breached at zero (BE-19). |
| **Expected Business Response** | Escalate urgently to purchasing and operations leadership; check network for transfer before new purchase per BR-011; initiate expedited PO or emergency transfer; communicate realistic re-availability to sales and customer service; document root cause for post-incident review. |
| **Responsible Actor** | Purchasing Manager → Operations Director |
| **Business Impact** | Lost sales; customer cancellations; premium freight costs; revenue at risk on priority products; reputational damage |

---

### EX-026 — Safety Stock Override Requested

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-026 |
| **Business Scenario** | Reservation, transfer, or fulfillment request would consume safety stock below policy buffer without a replenishment plan. |
| **Trigger** | Reservation or transfer evaluation against safety stock (BE-30, BE-41). |
| **Expected Business Response** | Block routine consumption of safety stock per BR-010; require authorized exception with approver, documented reason, and replenishment plan; record exception for governance review; deny if no recovery plan exists. |
| **Responsible Actor** | Operations Director / Inventory Controller |
| **Business Impact** | Next demand or supply shock causes immediate stockout; safety investment wasted; chronic crisis replenishment |

---

## Domain 6: Network Balance & Transfer Exceptions

### EX-027 — Local Stockout With Network Excess Elsewhere

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-027 |
| **Business Scenario** | One location is out of stock on a product while other network locations hold available excess quantity. |
| **Trigger** | Network imbalance identified (BE-42); low-stock at one site with surplus elsewhere. |
| **Expected Business Response** | Verify network ATP; initiate inter-location transfer request before new purchase per BR-011; approve transfer if source can spare stock per BR-012; communicate revised availability to sales. |
| **Responsible Actor** | Regional / Store Manager → Operations Director |
| **Business Impact** | Duplicate purchasing; excess at one site while another stockouts; trapped capital; lost local sales |

---

### EX-028 — Transfer Would Breach Source Minimum

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-028 |
| **Business Scenario** | Approved or requested transfer quantity would deplete the source location below its minimum threshold or safety stock. |
| **Trigger** | Inter-location transfer requested or approved (BE-41, BE-43). |
| **Expected Business Response** | Reduce transfer to maximum spareable quantity per BR-012; reject or modify request with documented reason; suggest alternate source location if available; do not approve transfer that creates source stockout. |
| **Responsible Actor** | Operations Director / Warehouse Manager (source) |
| **Business Impact** | Cascading stockouts across network; emergency replenishment at source; net worsening of network availability |

---

### EX-029 — In-Transit Transfer Receipt Variance

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-029 |
| **Business Scenario** | Destination receives fewer units than dispatched, or goods arrive damaged in transit between locations. |
| **Trigger** | Transfer shipment received with variance (BE-46). |
| **Expected Business Response** | Document receipt variance; investigate loss or damage in transit; adjust source and destination records accordingly; process write-off or claim if applicable; close transfer only when quantities reconciled. |
| **Responsible Actor** | Receiving Clerk (destination) → Warehouse Manager |
| **Business Impact** | Stock lost between locations; both sites show incorrect balances; accountability gap; unresolved in-transit aging |

---

### EX-030 — Emergency Transfer Request

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-030 |
| **Business Scenario** | Location urgently needs stock — key customer order, promotional event, or unexpected spike — faster than supplier replenishment allows. |
| **Trigger** | Inter-location transfer requested with urgency flag (BE-41). |
| **Expected Business Response** | Verify source ATP and minimum threshold; obtain expedited approval; execute pick and ship with documented freight authorization; track in-transit until receipt confirmed; review why standard replenishment failed. |
| **Responsible Actor** | Regional / Store Manager → Operations Director |
| **Business Impact** | Customer promise missed if transfer delayed; premium freight unbudgeted; source location risk if minimum not protected |

---

## Domain 7: Returns Exceptions

### EX-031 — Return Received Without Authorization

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-031 |
| **Business Scenario** | Warehouse receives returned goods without a valid return authorization linked to an original order. |
| **Trigger** | Returned goods arrive at dock (BE-48) without matching authorization. |
| **Expected Business Response** | Hold goods; contact customer service to validate or issue retroactive authorization per policy; refuse acceptance if policy violation or fraud suspected; do not add to sellable stock without valid linkage per BR-025. |
| **Responsible Actor** | Receiving Clerk → Customer Service Representative |
| **Business Impact** | Returns cannot match orders; fraudulent returns accepted; refund without receipt; inventory records incorrect |

---

### EX-032 — Returned Product Fails Inspection

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-032 |
| **Business Scenario** | Returned item is used, damaged, or defective and does not meet resale quality standards. |
| **Trigger** | Return inspection completed with fail outcome (BE-49). |
| **Expected Business Response** | Write off or liquidate non-resalable quantity with reason code per BR-026; do not restock to sellable inventory; process customer refund or credit per original resolution agreement; capture return reason for trend analysis. |
| **Responsible Actor** | Warehouse Manager → Inventory Controller |
| **Business Impact** | Damaged goods resold as new; repeat returns; customer complaints; inflated sellable ATP |

---

### EX-033 — Return Quantity or Product Mismatch

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-033 |
| **Business Scenario** | Physical return does not match authorization — wrong product, partial quantity, or excess units. |
| **Trigger** | Return receipt verification against authorization (BE-48). |
| **Expected Business Response** | Document mismatch; contact customer; hold mismatched items; accept only authorized product and quantity; adjust refund or credit proportionally per policy. |
| **Responsible Actor** | Receiving Clerk → Customer Service Representative |
| **Business Impact** | Over-refund; inventory credited for wrong items; unresolved return status; customer dispute |

---

## Domain 8: Commercial & Promotional Exceptions

### EX-034 — Promotional Demand Exceeds Forecast

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-034 |
| **Business Scenario** | Marketing promotion drives demand above planned levels and promotional stock depletes faster than campaign duration. |
| **Trigger** | Marketing campaign scheduled with accelerating sell-through (BE-55); stock threshold breached on promoted SKUs. |
| **Expected Business Response** | Ring-fence remaining promotional stock per BR-029; allocate to promoted channels; expedite replenishment or network transfer if feasible; inform marketing to adjust campaign intensity; communicate "while supplies last" if stock will not last. |
| **Responsible Actor** | Marketing Manager → Purchasing Manager / Operations Director |
| **Business Impact** | Campaign stockout during peak visibility; promotional ROI lost; customer disappointment at worst moment; channel conflict |

---

### EX-035 — Campaign Stock Gap Before Launch

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-035 |
| **Business Scenario** | Pre-launch readiness review finds current plus inbound stock insufficient for campaign targets within lead time. |
| **Trigger** | Marketing campaign scheduled or new product launch date set (BE-55, BE-56). |
| **Expected Business Response** | Quantify gap by SKU and location; escalate go/no-go decision to commercial and operations leadership; expedite purchasing if recoverable; delay or reduce campaign scope if not; document risk acceptance if proceeding. |
| **Responsible Actor** | Marketing Manager → Operations Director |
| **Business Impact** | Public launch without stock; brand embarrassment; wasted marketing spend; BO-24 promotional readiness failure |

---

### EX-036 — Channel Conflict Over Shared Inventory

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-036 |
| **Business Scenario** | Online, retail, wholesale, or marketplace channels compete for the same limited ATP — conflicting allocation requests for last units. |
| **Trigger** | Concurrent orders from multiple channels against shared pool (BE-28). |
| **Expected Business Response** | Apply leadership-defined channel priority rules; hard-allocate per EX-020; update channel-facing availability manually until integration available; escalate recurring conflicts to commercial leadership for policy review. |
| **Responsible Actor** | Inventory Controller / Sales Manager |
| **Business Impact** | Double-selling across channels; store associates vs. e-commerce conflict; wholesale contract breach; inconsistent customer experience |

---

## Domain 9: Financial, Governance & Compliance Exceptions

### EX-037 — Operations and Finance Inventory Mismatch at Month-End

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-037 |
| **Business Scenario** | Operational inventory quantities or valuation do not reconcile with general ledger balance at month-end close. |
| **Trigger** | Month-end financial close initiated (BE-53). |
| **Expected Business Response** | Categorize variances (timing, quantity, valuation); investigate unexplained gaps; correct operational records or agree financial adjustment; complete reconciliation within close calendar; escalate material gaps to CFO. |
| **Responsible Actor** | Finance Manager → Inventory Controller |
| **Business Impact** | Financial misstatement; audit findings; delayed close; BO-18 and BO-20 objectives fail; operations-finance distrust persists |

---

### EX-038 — Adjustment or Write-Off Exceeds Approval Threshold

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-038 |
| **Business Scenario** | Proposed inventory adjustment or write-off exceeds the approver's financial or quantity authority. |
| **Trigger** | Stock correction required (BE-25); significant write-off recorded (BE-54). |
| **Expected Business Response** | Route to independent higher-authority approver per BR-021; require documented evidence for write-offs per BR-023; block application until approved; notify finance for material write-offs. |
| **Responsible Actor** | Warehouse Manager (initiator) → Operations Director / CFO |
| **Business Impact** | Unauthorized large adjustments; fraud opportunity; financial misstatement; audit material weakness |

---

### EX-039 — Segregation of Duties Violation Attempted

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-039 |
| **Business Scenario** | Same person attempts to perform and approve a conflicting action — count and approve own variance, receive and approve own PO variance, or self-approve material adjustment. |
| **Trigger** | Control incident or policy breach identified (BE-59). |
| **Expected Business Response** | Block self-approval; route to independent approver per BR-019; log policy breach or authorized exception; review role assignment for systemic conflicts; inform Internal Auditor if material or recurring. |
| **Responsible Actor** | Warehouse Manager / Inventory Controller → Operations Director |
| **Business Impact** | Fraud and error undetected; SOX or audit failure; invalid accuracy and adjustment records |

---

### EX-040 — Product Recall Requiring Lot Quarantine

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-040 |
| **Business Scenario** | Quality defect, contamination, or regulatory notice requires recall of specific lot or batch — stock may be in warehouse, in transit, or already shipped. |
| **Trigger** | Supplier quality alert; regulatory notice; internal quality failure discovery. |
| **Expected Business Response** | Identify all affected lot quantity through traceability records; quarantine immediately and exclude from ATP per BR-013; trace shipped units to customers; notify regulatory authorities within mandated timelines; disposition quarantined stock after investigation. |
| **Responsible Actor** | Inventory Controller → Quality / Regulatory (with Operations Director) |
| **Business Impact** | Consumer harm; regulatory penalties; full product-line recall if lot data missing; legal liability; brand catastrophe |

---

### EX-041 — Control Policy Breach With Authorized Exception

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-041 |
| **Business Scenario** | Business situation requires deviation from standard policy — ad-hoc receipt without PO, safety stock override, or emergency approval outside normal authority — with legitimate operational justification. |
| **Trigger** | Control incident identified with exception path (BE-59). |
| **Expected Business Response** | Document approver, policy reference, business reason, and replenishment or recovery plan; apply exception only within granted authority; log for governance review; do not normalize exception into standard practice. |
| **Responsible Actor** | Operations Director / Purchasing Manager |
| **Business Impact** | If undocumented: audit finding and control erosion; if denied when needed: operational paralysis during genuine emergency |

---

## Domain 10: Demand Shock & Lifecycle Exceptions

### EX-042 — Flash Demand Spike From External Event

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-042 |
| **Business Scenario** | Unplanned external event — viral trend, competitor stockout redirect, weather — causes sudden demand depleting stock in hours or days. |
| **Trigger** | Rapid ATP depletion; multiple urgent availability inquiries; stock threshold breached on unaffected forecast SKUs. |
| **Expected Business Response** | Apply allocation rules immediately; assess fastest replenishment path; communicate realistic availability internally and externally; avoid overcommitment; conduct post-event review for safety stock and supplier capacity. |
| **Responsible Actor** | Operations Director → Inventory Controller / Purchasing Manager |
| **Business Impact** | Overselling during spike; reputational damage outlasting revenue gain; unfilled strategic customer orders; supplier also caught short |

---

### EX-043 — End-of-Season or Obsolete Stock Requiring Write-Off

| Attribute | Detail |
|-----------|--------|
| **Exception ID** | EX-043 |
| **Business Scenario** | Seasonal, discontinued, or slow-moving product has no remaining commercial value and must be removed from active inventory. |
| **Trigger** | Scheduled aging review; product discontinued with residual stock (BE-03); overstock report review. |
| **Expected Business Response** | Segregate physically; execute planned exit (markdown, outlet, donation, destroy); process authorized write-off with evidence per BR-023; update financial records; do not delay write-off inflating reported inventory. |
| **Responsible Actor** | Inventory Controller → Finance Manager |
| **Business Impact** | Trapped working capital; inflated operational and financial inventory; recurring carrying cost; misleading availability if stock remains "active" |

---

## Exception Response Pattern Summary

| Pattern | Exception IDs | Core Business Discipline |
|---------|---------------|--------------------------|
| **Verify before recording** | EX-005 – EX-009, EX-031 – EX-033 | Document at point of occurrence; never accept silent variance |
| **Investigate before adjusting** | EX-012, EX-013, EX-014, EX-016 | Root cause before number correction |
| **Check network first** | EX-025, EX-027, EX-030 | Transfer before purchase |
| **ATP-only commitment** | EX-017, EX-020, EX-022, EX-036 | Promise only fulfillable quantity |
| **Independent approval** | EX-038, EX-039 | Segregation of duties on material actions |
| **Proactive communication** | EX-010, EX-017, EX-022, EX-025 | Customer and internal honesty on delays |
| **Quarantine and exclude** | EX-006, EX-015, EX-040 | Non-sellable stock never in ATP |
| **Governed exception only** | EX-008, EX-026, EX-041 | Documented override — not normalized bypass |

---

## Exception-to-Process Traceability

| Business Process | Related Exceptions |
|------------------|-------------------|
| BP-01 Product Master | EX-001, EX-002 |
| BP-02 Location Setup | EX-003, EX-004 |
| BP-05 – BP-09 Inbound | EX-005 – EX-011 |
| BP-10 – BP-15 Inventory Control | EX-012 – EX-016 |
| BP-16 – BP-20 Fulfillment | EX-017 – EX-023 |
| BP-21 – BP-23 Replenishment | EX-024 – EX-026 |
| BP-24 – BP-26 Network Balance | EX-027 – EX-030 |
| BP-27 – BP-28 Returns | EX-031 – EX-033 |
| BP-31 Promotional Readiness | EX-034, EX-035 |
| BP-30 Financial Reconciliation | EX-037 |
| BP-14 Adjustments & Write-Offs | EX-038, EX-043 |
| BP-32 Audit & Governance | EX-039, EX-041 |
| Cross-cutting | EX-020, EX-036, EX-040, EX-042 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Business Analyst | | | |
| Product Owner | | | |
| Operations Director | | | |
| Inventory Controller | | | |

---

*End of Business Exception Scenarios Specification*

*Document ID: SRS-EX-001 | Version 1.0 | July 5, 2026*
