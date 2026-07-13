# Common Industry Rules in Inventory Management

**Document Owner:** Domain Expert  
**Purpose:** Document operational business rules that govern how organizations manage inventory in practice  
**Audience:** Operations leaders, inventory managers, business analysts, auditors, and policy authors  
**Scope:** Operational business rules only — not software validation logic, system constraints, or technical implementation

---

## How to Read This Document

Business rules are the non-negotiable policies and constraints that successful organizations enforce to maintain inventory control, protect assets, and serve customers reliably. They are expressed as what the business must, must not, or may only do under defined conditions — independent of how any system enforces them.

These rules reflect industry norms across distribution, retail, manufacturing, and healthcare. Organizations adopt them as standard operating policy, audit controls, and training requirements.

---

## Rules Index

| # | Rule | Domain |
|---|------|--------|
| 1 | Sell and promise only against available-to-promise quantity | Availability |
| 2 | Reserve stock at order confirmation | Fulfillment |
| 3 | Do not ship without confirmed pick verification | Fulfillment |
| 4 | Inbound goods must be verified before acceptance into inventory | Inbound |
| 5 | Received stock is not available until put-away is complete | Inbound |
| 6 | Receipt discrepancies must be documented before acceptance | Inbound |
| 7 | Purchase order required before receiving supplier goods | Inbound |
| 8 | Three-way match required before supplier payment | Procurement |
| 9 | Reorder action must trigger at or before reorder level | Replenishment |
| 10 | Safety stock must not be bypassed without authorized exception | Replenishment |
| 11 | Check network availability before placing new purchase | Network |
| 12 | Transfer must not deplete source below its minimum threshold | Network |
| 13 | Quarantined stock must be excluded from sellable availability | Quality |
| 14 | FEFO rotation required for shelf-life products | Rotation |
| 15 | FIFO rotation required for non-perishable standard goods | Rotation |
| 16 | Minimum remaining shelf life required at receipt | Perishables |
| 17 | Lot or batch must be captured for traceable products | Traceability |
| 18 | Cycle counts must be performed blind | Inventory Control |
| 19 | Counter must not approve adjustments from their own count | Governance |
| 20 | Every adjustment requires a reason code | Governance |
| 21 | Adjustments above threshold require independent approval | Governance |
| 22 | Investigate variance before applying adjustment | Inventory Control |
| 23 | Write-off requires documented evidence and authorization | Governance |
| 24 | Physical inventory freeze during full wall-to-wall count | Inventory Control |
| 25 | Returns require authorization before acceptance | Returns |
| 26 | Returned goods must be inspected before restocking | Returns |
| 27 | Discontinued products must not be reordered | Master Data |
| 28 | Backorder requires customer acknowledgment | Fulfillment |
| 29 | Promotional stock must be ring-fenced during campaign | Commercial |
| 30 | Bonded inventory must not be released without customs clearance | Trade |
| 31 | Consignment stock is not owned until consumption or sale event | Ownership |
| 32 | Class A products require highest count and monitoring frequency | Classification |

---

## Category 1: Availability and Customer Commitment

---

### Rule 1: Sell and Promise Only Against Available-to-Promise Quantity

**Business Reason**  
On-hand quantity includes stock already reserved or committed to other orders. Quoting or selling against total on-hand causes overselling — confirming orders the business cannot fulfill. ATP is the only honest measure of what can still be promised to new customers.

**Example**  
A distributor has 80 units on hand but 65 are reserved for standing customer orders. Sales may promise only 15 units (ATP) to a new customer — not 80.

**Consequences If Violated**  
Overselling, order cancellations, pick failures, customer complaints, expedited shipping costs, damaged sales credibility, and marketplace or contract penalties.

---

### Rule 2: Reserve Stock at Order Confirmation

**Business Reason**  
The gap between order confirmation and physical picking creates a window where the same stock can be sold to multiple customers. Reservation converts a commercial commitment into an operational hold, preventing double-allocation.

**Example**  
When a customer's order is confirmed, 10 units are immediately reserved at the fulfillment location. No other order can claim those 10 units until the reservation is released or fulfilled.

**Consequences If Violated**  
Pick failures, partial shipments, competing orders for the same physical stock, customer disputes, and fulfillment chaos during high-demand periods.

---

### Rule 3: Do Not Ship Without Confirmed Pick Verification

**Business Reason**  
Inventory should not be deducted and orders should not be marked shipped until the correct items are physically retrieved, verified, packed, and handed to the carrier. Premature shipment recording creates inaccurate stock and false delivery expectations.

**Example**  
A picker retrieves 5 units of Part A-100, scans them against the pick list, and confirms the match. Only after scan confirmation is the order marked shipped and on-hand stock reduced.

**Consequences If Violated**  
Wrong items shipped to customers, inventory records deducted before goods leave, unrecorded stock still on shelves, customer returns, and compounding accuracy errors.

---

### Rule 28: Backorder Requires Customer Acknowledgment

**Business Reason**  
A backorder is a mutual agreement to wait — not an internal note that an order cannot ship. Customers must be informed of the delay, the expected fulfillment date, and their right to cancel. Silent backorders destroy trust.

**Example**  
When 20 of 50 ordered units are unavailable, customer service contacts the customer, explains 30 will ship now and 20 will follow in two weeks, and records the customer's agreement to wait.

**Consequences If Violated**  
Customer discovers delay independently, cancels orders, disputes charges, posts negative reviews, and escalates to leadership. Chargebacks and contract breaches in B2B relationships.

---

## Category 2: Inbound and Procurement

---

### Rule 4: Inbound Goods Must Be Verified Before Acceptance into Inventory

**Business Reason**  
Arrival at the dock is not receipt. Until quantity, product identity, and condition are verified against the purchase order, the business does not know what it actually received. Recording unverified quantities corrupts inventory from the point of entry.

**Example**  
A receiver compares the delivery note and PO to the physical shipment, counts cartons, inspects for damage, and records 950 accepted units — not the 1,000 ordered — as received inventory.

**Consequences If Violated**  
Phantom inventory (system shows stock that was never received), payment for goods not delivered, inability to fulfill orders, supplier disputes without evidence, and audit failures.

---

### Rule 5: Received Stock Is Not Available Until Put-Away Is Complete

**Business Reason**  
Stock sitting in the receiving area is physically in the building but not operationally available. Pickers cannot find it efficiently, it may be damaged in transit areas, and it is not in its designated storage location. Availability begins when put-away is confirmed.

**Example**  
A shipment of 200 units is received and verified at 10 AM. Put-away to aisle B-14 is completed at 1 PM. ATP increases at 1 PM — not at truck arrival.

**Consequences If Violated**  
Pickers search receiving area for "available" stock, pick times increase, dock congestion grows, counts miss receiving-area stock, and same-day fulfillment promises fail.

---

### Rule 6: Receipt Discrepancies Must Be Documented Before Acceptance

**Business Reason**  
Short shipments, over-shipments, wrong items, and damage must be recorded at the point of receipt — when evidence exists and the carrier or supplier is present. Undocumented acceptance waives the business's right to claim and hides supplier performance problems.

**Example**  
A receiver notes 50 damaged units and 30 missing units on the receipt record, photographs damage, and initiates a supplier claim — before signing the delivery acceptance.

**Consequences If Violated**  
Business pays for undelivered goods, supplier disputes become unresolvable, inventory records include unsellable or nonexistent stock, and supplier OTIF data is unreliable.

---

### Rule 7: Purchase Order Required Before Receiving Supplier Goods

**Business Reason**  
A purchase order is the authorized commercial commitment that defines what was ordered, at what price, and from whom. Receiving without a PO breaks financial controls, enables unauthorized purchases, and prevents three-way matching.

**Example**  
A supplier truck arrives with an unscheduled delivery. Receiving refuses acceptance until purchasing confirms a valid PO exists for the shipment.

**Consequences If Violated**  
Unauthorized spending, inability to verify pricing, maverick buying outside contracts, audit findings, and accounts payable cannot process payment.

---

### Rule 8: Three-Way Match Required Before Supplier Payment

**Business Reason**  
Payment must be authorized only when the purchase order (what was ordered), goods receipt (what was received), and supplier invoice (what is billed) agree within defined tolerance. This prevents paying for unordered, unreceived, or mispriced goods.

**Example**  
Accounts payable matches PO line for 1,000 units at $5.00, receipt record for 950 units, and invoice for 1,000 units at $5.00. Payment is held until the 50-unit short shipment is resolved with the supplier.

**Consequences If Violated**  
Overpayment to suppliers, payment for phantom goods, financial loss, audit material weaknesses, and eroded procurement controls.

---

## Category 3: Replenishment and Stock Policy

---

### Rule 9: Reorder Action Must Trigger at or Before Reorder Level

**Business Reason**  
The reorder level is calculated to allow enough time for replenishment to arrive before stock reaches zero, accounting for lead time and demand during that period. Delaying action past the reorder level guarantees a stockout during lead time.

**Example**  
A product's reorder level is 200 units with 10-day lead time. When available stock hits 200, a purchase requisition is generated the same business day — not when stock reaches 50.

**Consequences If Violated**  
Preventable stockouts, emergency purchasing at premium cost, customer backorders, lost sales, and erosion of fill rate on affected products.

---

### Rule 10: Safety Stock Must Not Be Bypassed Without Authorized Exception

**Business Reason**  
Safety stock is a deliberate buffer protecting against demand and supply uncertainty. Consuming safety stock to fulfill routine orders or reallocating it without replenishment plan removes the organization's protection against the next disruption.

**Example**  
A warehouse manager wants to send safety stock to fulfill a non-priority order. The request is denied unless operations leadership approves an exception with a documented replenishment plan.

**Consequences If Violated**  
Next demand spike or supplier delay causes immediate stockout. Safety stock investment is wasted. Organization operates with no buffer and chronic crisis mode.

---

## Category 4: Network and Transfers

---

### Rule 11: Check Network Availability Before Placing New Purchase

**Business Reason**  
A local stockout may be solvable with a transfer from another location that holds excess. Purchasing new stock when the network already owns sufficient quantity wastes capital, increases carrying cost, and worsens network imbalance.

**Example**  
Store 15 is out of a popular jacket. Before placing a PO, the planner checks the network and finds 200 units at the regional DC. A transfer request is initiated instead of a purchase order.

**Consequences If Violated**  
Duplicate inventory investment, excess at one location while another stockouts, wasted freight on unnecessary purchases, and higher total carrying cost across the network.

---

### Rule 12: Transfer Must Not Deplete Source Below Its Minimum Threshold

**Business Reason**  
Sending stock to fix one location's shortage must not create a shortage at the source. Transfers require verification that the sending location can spare the quantity while maintaining its own service level.

**Example**  
A store requests 50 units from the DC. The DC has 60 available (ATP) with a minimum threshold of 40. Only 20 units may be transferred — not 50.

**Consequences If Violated**  
Source location stockouts, cascading transfers across the network, emergency replenishment at the source, and net worsening of network availability.

---

## Category 5: Quality, Rotation, and Traceability

---

### Rule 13: Quarantined Stock Must Be Excluded from Sellable Availability

**Business Reason**  
Quarantined inventory is held pending quality investigation, regulatory clearance, or recall response. Including quarantined stock in sellable availability risks shipping defective, contaminated, or non-compliant products to customers.

**Example**  
A lot of 500 units fails incoming inspection and is moved to the quarantine zone. ATP is reduced by 500 immediately. No orders are fulfilled from that lot until quality releases or rejects it.

**Consequences If Violated**  
Defective products shipped to customers, regulatory non-compliance, product recalls, legal liability, customer safety risk, and reputational damage.

---

### Rule 14: FEFO Rotation Required for Shelf-Life Products

**Business Reason**  
Products with expiration dates must ship in order of earliest expiry first. Shipping newer stock while older stock expires in the warehouse causes write-offs, customer safety issues, and regulatory violations.

**Example**  
A pharmacy warehouse picks insulin vials with the nearest expiration date first, even if a newer lot arrived more recently.

**Consequences If Violated**  
Expired product write-offs, customer receipt of near-expiry goods, regulatory penalties in pharmaceuticals and food, and potential consumer harm.

---

### Rule 15: FIFO Rotation Required for Non-Perishable Standard Goods

**Business Reason**  
Oldest stock should move first to minimize obsolescence, packaging degradation, and model-year expiration. Consistent FIFO prevents aged inventory from sitting indefinitely while new stock cycles normally.

**Example**  
A warehouse picker is directed to pick from the oldest pallet position for SKU W-200, even though a newer shipment arrived yesterday.

**Consequences If Violated**  
Obsolescence write-offs, customers receive outdated product versions, warranty complications, and warehouse congestion from aged stock accumulation.

---

### Rule 16: Minimum Remaining Shelf Life Required at Receipt

**Business Reason**  
Receiving product too close to expiration guarantees write-off before sale. Minimum remaining shelf life (MRSL) requirements protect the business from accepting stock with insufficient selling window.

**Example**  
A grocery distributor's MRSL policy requires 90 days remaining shelf life at receipt. A delivery with 60 days remaining is rejected and returned to the supplier.

**Consequences If Violated**  
Product expires before sale, write-off costs increase, customers receive near-expiry goods, and supplier quality agreements are unenforced.

---

### Rule 17: Lot or Batch Must Be Captured for Traceable Products

**Business Reason**  
Lot capture at every transaction point enables targeted recall, quality investigation, and regulatory compliance. Without lot data, the only option in a defect scenario is a full product-line recall.

**Example**  
A food distributor records lot number 2026-0412 at goods receipt, transfer, pick, and ship. When a contamination is found in that lot, only affected units are recalled.

**Consequences If Violated**  
Full product-line recall instead of targeted lot recall, regulatory non-compliance, inability to identify affected customers, extended investigation time, and greater financial and reputational damage.

---

## Category 6: Inventory Control and Governance

---

### Rule 18: Cycle Counts Must Be Performed Blind

**Business Reason**  
Counters who see the system's expected quantity before counting may consciously or unconsciously match it, defeating the purpose of verification. Blind counting produces unbiased accuracy measurement.

**Example**  
A cycle counter is given the SKU and bin location only — not the system's quantity of 47. The counter records 42 physically found. The 5-unit variance is calculated after submission.

**Consequences If Violated**  
Inaccurate counts validate bad data instead of detecting errors. Inventory accuracy metrics become meaningless. Audit credibility is destroyed. Root causes remain undetected.

---

### Rule 19: Counter Must Not Approve Adjustments from Their Own Count

**Business Reason**  
Segregation of duties prevents fraud and undetected error. When the same person counts, investigates, and approves, there is no independent verification of the variance or its cause.

**Example**  
A cycle counter finds a 15-unit variance. The count is submitted for review. A warehouse supervisor who did not perform the count investigates and approves the adjustment.

**Consequences If Violated**  
Fraud opportunity (inflate or deflate stock for personal gain), undetected counting errors, audit control failures, and SOX compliance violations for public companies.

---

### Rule 20: Every Adjustment Requires a Reason Code

**Business Reason**  
Adjustments without categorized reasons are analytically useless. The business knows quantity changed but not why — preventing shrinkage analysis, trend identification, and targeted corrective action.

**Example**  
A 10-unit decrease is recorded with reason code "damage — water intrusion" rather than a generic "correction." Monthly shrinkage analysis shows a spike in water damage at one location.

**Consequences If Violated**  
Shrinkage trends invisible, audit trail insufficient, root causes unaddressed, loss prevention cannot prioritize, and recurring problems continue indefinitely.

---

### Rule 21: Adjustments Above Threshold Require Independent Approval

**Business Reason**  
High-value or high-quantity adjustments carry greater financial and fraud risk. Independent approval by an authorized person who did not perform the underlying transaction provides oversight proportional to the impact.

**Example**  
Adjustments of more than 10 units or $500 require inventory manager approval. A 50-unit write-down is submitted with evidence and approved by the manager, not the warehouse associate who reported it.

**Consequences If Violated**  
Large-scale fraud or error goes undetected, financial misstatement, audit findings, and unauthorized manipulation of inventory values.

---

### Rule 22: Investigate Variance Before Applying Adjustment

**Business Reason**  
Adjustments fix the record; investigation fixes the process. Applying adjustments without understanding why the variance occurred guarantees the same discrepancy will reappear on the next count.

**Example**  
A 8-unit variance on a SKU is found during cycle count. Investigation reveals items stored in an unlabeled overflow bin. Stock is adjusted, and overflow bin labeling is corrected — not just the number.

**Consequences If Violated**  
Recurring variances on the same SKUs, chronic accuracy problems, process failures continue, and adjustment volume grows without improvement.

---

### Rule 23: Write-Off Requires Documented Evidence and Authorization

**Business Reason**  
Write-offs permanently remove inventory value from the business. Unauthorized or undocumented write-offs enable fraud, inflate remaining inventory inaccurately, and create audit exposure.

**Example**  
A write-off of 100 expired units requires photographs, lot numbers, expiration dates, and manager approval before inventory and financial records are reduced.

**Consequences If Violated**  
Ghost stock (written off physically but still in system, or vice versa), fraudulent disposal of sellable goods, financial misstatement, audit material weaknesses, and margin distortion.

---

### Rule 24: Physical Inventory Freeze During Full Wall-to-Wall Count

**Business Reason**  
Movements during a full count change the quantity being counted, making the snapshot unreliable. A freeze ensures the counted quantity is stable and auditable.

**Example**  
A warehouse begins a full count Friday at 6 PM. No receiving, shipping, transfers, or adjustments occur until the count is completed and verified Sunday evening.

**Consequences If Violated**  
Count results unreliable, variances impossible to interpret, financial inventory substantiation fails, and the entire count must be repeated — doubling disruption and cost.

---

## Category 7: Returns and Product Lifecycle

---

### Rule 25: Returns Require Authorization Before Acceptance

**Business Reason**  
Unauthorized returns cannot be linked to original orders, may violate return policy, and give the warehouse no advance notice. Authorization connects the physical return to the commercial transaction and expected resolution.

**Example**  
A customer contacts support for a return. Support issues a return authorization (RA) number linked to the original order. The warehouse accepts the package only when a valid RA is presented.

**Consequences If Violated**  
Returns cannot be matched to orders, refunds issued without receipt, policy violations, fraudulent returns accepted, and inventory records updated incorrectly.

---

### Rule 26: Returned Goods Must Be Inspected Before Restocking

**Business Reason**  
Not all returns are resalable. Used, damaged, or defective products placed back in sellable inventory will be shipped to the next customer as new — generating repeat returns, complaints, and brand damage.

**Example**  
A returned blender is inspected at the returns station. The motor fails the function test. It is written off — not restocked. A returned blender in resalable condition is cleaned, resealed, and returned to stock.

**Consequences If Violated**  
Damaged goods sold as new, increased return rates, customer complaints, brand reputation damage, and inventory records showing sellable stock that is actually unsellable.

---

### Rule 27: Discontinued Products Must Not Be Reordered

**Business Reason**  
Discontinued status means the business has decided to exit the product. Reordering discontinued SKUs creates obsolete inventory that must eventually be written off, and conflicts with supersession plans.

**Example**  
A buyer attempts to reorder SKU A-100, which was discontinued last month and superseded by A-200. The requisition is blocked. Remaining A-100 stock is sold through on a defined runout timeline.

**Consequences If Violated**  
Obsolete inventory accumulation, capital trapped in unsellable goods, customer confusion between old and new versions, and write-off costs at year-end.

---

## Category 8: Commercial, Trade, and Classification

---

### Rule 29: Promotional Stock Must Be Ring-Fenced During Campaign

**Business Reason**  
Promotional inventory is positioned for a specific campaign period and channel. Allowing non-promotional orders to consume promotional stock defeats the campaign plan and leaves promoted channels without supply.

**Example**  
Five hundred units are hard-allocated to the holiday promotion at flagship stores. Wholesale and online channels cannot draw from this allocation during the campaign period without commercial leadership approval.

**Consequences If Violated**  
Promoted stores stockout during campaign, promotional ROI lost, marketing commitments unfulfilled, and customer disappointment at the worst possible moment.

---

### Rule 30: Bonded Inventory Must Not Be Released Without Customs Clearance

**Business Reason**  
Bonded warehouse stock is under customs control. Duties and taxes have not been paid. Releasing bonded goods into domestic commerce without customs authorization is illegal and creates financial and regulatory liability.

**Example**  
Imported electronics are stored in a bonded warehouse. When domestic demand is confirmed, customs release is processed and duties paid before stock is moved to sellable domestic inventory.

**Consequences If Violated**  
Customs penalties, seizure of goods, legal prosecution, financial liability for unpaid duties, and supply chain disruption.

---

### Rule 31: Consignment Stock Is Not Owned Until Consumption or Sale Event

**Business Reason**  
Consignment inventory is physically at the buyer's location but owned by the supplier until the buyer consumes, sells, or issues it per agreement. Treating consignment as owned inventory overstates assets and triggers incorrect financial recording.

**Example**  
A machine shop holds 200 consignment fasteners from Supplier X. Ownership transfers when a work order issues fasteners to production — not when they arrive at the shop.

**Consequences If Violated**  
Balance sheet overstates inventory assets, financial reconciliation errors, incorrect COGS timing, and supplier consignment reconciliation disputes.

---

### Rule 32: Class A Products Require Highest Count and Monitoring Frequency

**Business Reason**  
Not all products warrant equal operational effort. Class A items drive the majority of revenue and customer impact. Higher count frequency and monitoring intensity on A items prevents stockouts and accuracy failures where they matter most.

**Example**  
Class A SKUs are cycle-counted weekly and monitored daily for availability. Class C SKUs are cycle-counted quarterly with automated min-max replenishment.

**Consequences If Violated**  
High-revenue products stockout due to undetected discrepancies. Counting effort wasted on low-impact items while priority items drift. Fill rate failures on the products customers care about most.

---

## Rules by Control Objective

| Control Objective | Rules |
|-------------------|-------|
| **Prevent overselling** | 1, 2, 3, 28 |
| **Protect inbound integrity** | 4, 5, 6, 7, 8 |
| **Maintain replenishment discipline** | 9, 10, 11 |
| **Protect network balance** | 11, 12 |
| **Ensure product safety and compliance** | 13, 14, 15, 16, 17 |
| **Sustain inventory accuracy** | 18, 19, 20, 21, 22, 24 |
| **Control financial exposure** | 8, 21, 23, 30, 31 |
| **Manage returns and lifecycle** | 25, 26, 27 |
| **Align commercial and operations** | 29 |
| **Prioritize by business impact** | 32 |

---

## Rules That Must Work Together

Some rules are ineffective in isolation. These combinations are industry-standard:

| Combination | Why Both Are Needed |
|-------------|---------------------|
| Rule 1 (ATP) + Rule 2 (Reserve) | ATP tells you what is available; reservation locks it against commitments |
| Rule 4 (Verify receipt) + Rule 6 (Document discrepancies) | Verification without documentation loses supplier accountability |
| Rule 18 (Blind count) + Rule 19 (Independent approval) | Blind count detects variance; independent approval prevents fraud |
| Rule 20 (Reason code) + Rule 22 (Investigate first) | Investigation finds cause; reason code captures it for analysis |
| Rule 14 (FEFO) + Rule 16 (MRSL at receipt) | FEFO manages rotation; MRSL prevents accepting stock too close to expiry |
| Rule 11 (Check network) + Rule 12 (Protect source) | Network check enables transfer; source protection prevents new shortages |

---

## Related Documents

- Inventory Management Industry Standards (`Domain Knowledge/inventory-management-industry-standards.md`)
- Inventory Management Best Practices (`Domain Knowledge/inventory-management-best-practices.md`)
- Common Inventory Management Challenges (`Domain Knowledge/common-inventory-management-challenges.md`)
- Business Glossary (`business domain/business-glossary.md`)

---

*End of Inventory Management Business Rules Document*
