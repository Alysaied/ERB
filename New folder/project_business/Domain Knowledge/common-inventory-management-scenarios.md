# Common Business Scenarios in Inventory Management

**Document Owner:** Inventory Domain Expert  
**Purpose:** Describe recurring operational situations that inventory teams encounter and must resolve in daily business  
**Audience:** Operations leaders, inventory managers, business analysts, and cross-functional stakeholders  
**Scope:** Operational business scenarios only — no software behavior, system design, or automation detail

---

## How to Read This Document

Inventory management is not a single process — it is a continuous response to situations that arise across supply, demand, accuracy, and network balance. The scenarios below represent the most common situations successful organizations plan for and handle with defined discipline.

Each scenario describes what happens, who is involved, what good looks like when handled well, and the business factors that should guide decisions. These scenarios complement the Business Workflows and Business Events documents by focusing on **situations** rather than process steps or triggers.

---

## Scenario Index

| # | Scenario | Domain |
|---|----------|--------|
| 1 | Priority Product Stockout During Peak Demand | Availability Crisis |
| 2 | Customer Order Exceeds Available-to-Promise | Order Fulfillment |
| 3 | Supplier Short-Shipment on Critical Purchase Order | Inbound |
| 4 | Damaged Goods Discovered at Receiving | Inbound |
| 5 | Cycle Count Reveals Significant Variance | Inventory Control |
| 6 | Low Stock Detected Before Stockout | Replenishment |
| 7 | Network Has Stock but Local Location Is Out | Network Balance |
| 8 | Emergency Transfer Request Between Locations | Network Balance |
| 9 | Promotional Demand Exceeds Forecast | Commercial Surge |
| 10 | New Product Launch With Uncertain Demand | Commercial Launch |
| 11 | End-of-Season Excess Inventory | Lifecycle |
| 12 | Product Supersession and Old SKU Runout | Lifecycle |
| 13 | Customer Return Requiring Inspection and Disposition | Returns |
| 14 | Product Recall Requiring Lot Traceability | Compliance |
| 15 | Quality Hold on Received Inventory Lot | Quality Control |
| 16 | Concurrent Demand for Last Available Units | Allocation Conflict |
| 17 | Inbound Shipment Delayed Beyond Customer Promise | Supply Delay |
| 18 | Shelf Empty but System Shows In-Stock (Phantom Inventory) | Retail Accuracy |
| 19 | Unexplained Shrinkage Trend at a Location | Loss Prevention |
| 20 | Operations and Finance Inventory Mismatch at Month-End | Financial Alignment |
| 21 | Supplier Lead Time Extension | Supply Disruption |
| 22 | Channel Conflict Over Shared Inventory Pool | Omnichannel |
| 23 | Obsolete Stock Requiring Write-Off Decision | Financial Disposition |
| 24 | Full Physical Count With Operational Disruption | Inventory Control |
| 25 | Flash Demand Spike From External Event | Demand Shock |

---

## Category 1: Availability and Fulfillment Crises

---

### 1. Priority Product Stockout During Peak Demand

#### Description

A high-priority (Class A) product reaches zero available quantity at one or more locations during a period of elevated demand — a promotion, season, viral trend, or supply disruption. Customer orders are unfulfillable, backorders accumulate, and commercial teams face pressure to recover availability immediately.

#### Actors Involved

- Inventory / Supply Planner
- Purchasing Buyer
- Warehouse Manager
- Sales / Customer Service
- Store Manager (if retail)
- Supplier Account Manager
- Operations Leadership

#### Expected Outcome

Stock is restored at affected locations as quickly as possible through the most cost-effective combination of expedited purchase, inter-location transfer, and supplier escalation. Customers with existing commitments are prioritized. Sales is informed of realistic re-availability dates. Root cause (forecast gap, supplier delay, insufficient safety stock) is documented to prevent recurrence.

#### Business Considerations

- Prioritize by customer commitment and product class — not whoever complains loudest
- Check the full network before placing emergency purchase orders
- Communicate honestly with customers; do not promise dates that inbound supply cannot support
- Expedited freight and emergency purchasing have cost implications — authorize explicitly
- Post-incident review should examine safety stock, reorder points, and forecast accuracy

---

### 2. Customer Order Exceeds Available-to-Promise

#### Description

A customer places an order (or sales confirms an order) for a quantity that exceeds what the business can fulfill from current ATP — on-hand stock minus existing reservations. This may be a single large order or the cumulative effect of multiple orders against limited stock.

#### Actors Involved

- Sales Representative / Customer Service
- Inventory Controller
- Warehouse / Fulfillment Team
- Customer
- Sales Manager

#### Expected Outcome

The business confirms what can be fulfilled immediately, what must be backordered, and realistic delivery dates for the remainder — with customer agreement. Stock is reserved for the accepted portion. The unfulfillable portion is either backordered with a committed date, partially cancelled, or redirected to an alternate product. No order is confirmed beyond ATP without a documented plan.

#### Business Considerations

- Never confirm full order quantity against on-hand without checking ATP
- Large or strategic customers may warrant allocation negotiation — but not silent overcommitment
- Partial fulfillment increases shipping cost and customer friction — use deliberately
- Backorders require inbound supply or transfer plan, not indefinite holding
- Pattern of ATP breaches signals policy or forecasting problems

---

### 3. Concurrent Demand for Last Available Units

#### Description

Multiple customers, stores, or channels simultaneously need the last available units of a product. Total demand exceeds remaining ATP and competing requests must be prioritized — a government contract vs. retail orders, online vs. in-store, standing customer vs. new order.

#### Actors Involved

- Inventory Controller
- Sales Manager
- Operations Manager
- Customer Service
- Commercial / Leadership (for strategic decisions)

#### Expected Outcome

A clear allocation decision is made based on documented priority rules (contractual obligation, customer tier, order date, channel priority). Allocated stock is hard-reserved for the winning demand. Deprioritized requests receive honest communication and alternatives (backorder, substitute, transfer timeline). Decision and rationale are recorded.

#### Business Considerations

- Allocation rules should exist before the conflict arises, not invented under pressure
- Hard allocation prevents reallocation disputes during picking
- Deprioritized customers deserve proactive communication, not discovery at shipment
- Recurring allocation conflicts indicate insufficient safety stock or network imbalance
- Revenue impact of allocation decisions should be visible to leadership

---

## Category 2: Inbound and Supply Scenarios

---

### 4. Supplier Short-Shipment on Critical Purchase Order

#### Description

A supplier delivers fewer units than ordered on a purchase order for a product that is already low, committed to customer orders, or needed for an upcoming promotion. The receipt is physically short and the business must decide how to accept, document, and respond.

#### Actors Involved

- Receiving Clerk / Warehouse Team
- Purchasing Buyer
- Supplier Account Manager
- Inventory Controller
- Accounts Payable

#### Expected Outcome

The short shipment is documented at receipt with quantity actually received — not the PO quantity. A receipt discrepancy is raised with the supplier. Inventory records reflect only verified units. Purchasing escalates with the supplier for the balance. Affected customer orders and replenishment plans are reassessed. Payment is held or adjusted pending resolution per three-way match rules.

#### Business Considerations

- Accepting short shipment without documentation loses supplier accountability
- ATP and customer commitments must be recalculated immediately on short receipt
- Chronic short-shipment from a supplier is a sourcing and safety stock issue
- Do not record ordered quantity as received — this creates phantom inventory
- Balance urgency (need the stock) against control (document the gap)

---

### 5. Damaged Goods Discovered at Receiving

#### Description

Inbound goods arrive with visible damage — crushed cartons, broken units, water damage, or temperature excursion for cold-chain products. Some or all of the shipment may be unsellable. The receiver must decide what to accept, reject, quarantine, or claim.

#### Actors Involved

- Receiving Clerk
- Warehouse Supervisor
- Quality Control (if applicable)
- Purchasing Buyer
- Carrier / Supplier
- Inventory Controller

#### Expected Outcome

Damaged goods are segregated and not entered as sellable inventory. Acceptable units are received normally. Damaged units are documented with photos, reason codes, and carrier or supplier claim initiation. Quarantined stock is excluded from ATP until disposition. Supplier or carrier credit, replacement, or rejection is pursued per agreement terms.

#### Business Considerations

- Damaged goods accepted into sellable stock become future customer complaints and returns
- Cold-chain damage may affect entire shipment even without visible signs
- Carrier vs. supplier liability depends on Incoterms and freight terms
- Photo evidence at the dock is essential for claims — delay loses evidence
- Receiving tolerance policies should define when partial acceptance is allowed

---

### 6. Inbound Shipment Delayed Beyond Customer Promise

#### Description

A purchase order or transfer shipment is delayed — supplier production issue, carrier delay, customs hold, weather — and the delay pushes past the date already promised to customers who are waiting on backorders or scheduled deliveries.

#### Actors Involved

- Purchasing Buyer
- Supplier Account Manager
- Inventory / Supply Planner
- Customer Service
- Customer
- Logistics / Transportation

#### Expected Outcome

Affected customers are proactively notified of the revised delivery date before they discover the delay themselves. Revised ATP and CTP dates are communicated internally. Escalation with supplier or carrier is initiated. Alternative supply (alternate supplier, network transfer) is evaluated for critical commitments. Customer compensation or priority handling is decided for strategic accounts.

#### Business Considerations

- Proactive communication preserves trust; silence converts delay into cancellation
- Every customer promise tied to inbound supply carries supplier risk — track dependency
- Chronic supplier delays require safety stock and dual-sourcing review
- Do not auto-extend promise dates without verifying new arrival confidence
- Cost of expedited alternatives should be weighed against customer and revenue risk

---

### 7. Supplier Lead Time Extension

#### Description

A supplier formally or informally communicates that lead times are increasing — due to raw material shortages, capacity constraints, logistics disruption, or geographic events. Existing reorder points and safety stock levels may no longer provide adequate cover.

#### Actors Involved

- Purchasing Buyer
- Inventory / Supply Planner
- Supplier Account Manager
- Operations Leadership
- Finance (for working capital impact)

#### Expected Outcome

Reorder points, safety stock levels, and order quantities are recalculated for affected products using the new lead time. Purchasing adjusts order timing to place orders earlier. Sales and customer service are informed of potentially longer delivery windows. Alternate suppliers are evaluated for critical items. Inventory investment may increase temporarily to bridge the gap.

#### Business Considerations

- Lead time changes invalidate existing replenishment policy — recalculate, don't guess
- True operational lead time includes receiving and put-away, not just supplier quote
- Working capital impact of higher safety stock should be visible to finance
- Dual sourcing may be justified for single-source critical items
- Communicate externally only after internal policy is updated

---

## Category 3: Inventory Control and Accuracy

---

### 8. Cycle Count Reveals Significant Variance

#### Description

A scheduled cycle count finds a material difference between the physical quantity and the recorded quantity for a product at a location. The variance exceeds the defined tolerance threshold and requires investigation before adjustment.

#### Actors Involved

- Cycle Count Team
- Warehouse Supervisor
- Inventory Controller
- Inventory Manager (for approval)
- Operations Leadership (for large variances)

#### Expected Outcome

Count is repeated to confirm the variance (blind recount). Root cause is investigated — receiving error, pick error, misplacement, unrecorded damage, theft, or data entry mistake. Adjustment is applied with mandatory reason code and manager approval. Corrective action addresses the process failure, not just the number. Trend is monitored for recurring variances on the same SKU or location.

#### Business Considerations

- Investigate before adjusting — adjustments without root cause analysis guarantee recurrence
- Large variances on high-value items may trigger loss prevention involvement
- Counter must be independent of the person who handles that stock daily
- Recurring variances on the same SKU signal a systemic process failure
- Small variances across many SKUs aggregate into significant financial loss

---

### 9. Shelf Empty but System Shows In-Stock (Phantom Inventory)

#### Description

A retail store or warehouse situation where the inventory record shows positive available quantity, but the product cannot be found physically — the shelf is empty, the pick location is bare, or the customer cannot locate the item. Sales are lost and customer trust erodes despite "in stock" system status.

#### Actors Involved

- Store Associate / Picker
- Store Manager / Warehouse Supervisor
- Customer Service
- Inventory Controller
- Customer

#### Expected Outcome

Physical search is conducted including backroom, overstock, and mislabeled locations. If stock cannot be found, an adjustment is made with appropriate reason code (likely shrinkage or count correction). ATP is corrected immediately. Customer is offered alternative fulfillment (ship from another location, substitute, rain check). Root cause is investigated — unrecorded theft, unprocessed returns, receiving error, or failure to record shelf replenishment.

#### Business Considerations

- Phantom inventory is a symptom — shrinkage, process failure, or poor shelf discipline is the cause
- Online "in stock" with empty shelves is an omnichannel trust failure
- Immediate ATP correction prevents additional overselling
- Store-level accuracy accountability drives prevention
- OSA (on-shelf availability) metrics catch what warehouse fill rate misses

---

### 10. Unexplained Shrinkage Trend at a Location

#### Description

A specific warehouse or store shows a rising pattern of inventory loss — adjustments for shrinkage, count variances, or write-offs — that exceeds the location's historical norm and the network average. No single large incident explains the trend.

#### Actors Involved

- Inventory Controller
- Location Manager
- Loss Prevention / Security
- Operations Leadership
- Human Resources (if internal theft suspected)

#### Expected Outcome

Shrinkage data is analyzed by product category, reason code, shift, and time period to identify patterns. Physical security and process audits are conducted. Receiving, picking, and adjustment controls are reviewed. Training gaps or process shortcuts are corrected. If internal theft is suspected, loss prevention investigates within policy. Accuracy improves and shrinkage rate returns to benchmark within an agreed timeline.

#### Business Considerations

- Shrinkage is not always theft — administrative errors and process failures are equally common
- Public accusation without evidence creates legal and morale risk
- Trend analysis by reason code directs investigation more effectively than total shrinkage number
- Segregation of duties review is standard when shrinkage trends are unexplained
- Location manager accountability should be supportive, not purely punitive

---

### 11. Full Physical Count With Operational Disruption

#### Description

The organization conducts a comprehensive wall-to-wall inventory count at a location, requiring a temporary freeze on receiving, shipping, transfers, and adjustments to produce a reliable snapshot. Operations must balance count accuracy against business disruption.

#### Actors Involved

- Inventory Controller
- Warehouse / Store Manager
- Count Team (often external or cross-trained staff)
- Finance
- Operations Leadership
- Receiving and Shipping Teams (paused during freeze)

#### Expected Outcome

All inventory at the location is counted within the planned window. Variances are investigated, approved, and adjusted. Location accuracy is established at a verified baseline. Finance receives substantiated inventory value for reporting. Operations resume normal activity immediately after freeze lifts. Cycle counting program maintains accuracy going forward so the next full count is a validation, not a crisis.

#### Business Considerations

- Minimize freeze duration — strong cycle counting reduces full count scope and time
- Blind counting is essential for audit credibility
- Pre-count cleanup (complete put-away, clear receiving dock) improves count quality
- External or cross-location counters reduce bias
- Full count is a point-in-time snapshot — without ongoing cycle counting, accuracy degrades within weeks

---

## Category 4: Replenishment and Network Balance

---

### 12. Low Stock Detected Before Stockout

#### Description

A product's available quantity falls below its defined reorder level or minimum threshold at a location — triggering a low-stock alert. Stock is not yet at zero, but replenishment action is required now to avoid a stockout given supplier lead time.

#### Actors Involved

- Inventory / Supply Planner
- Purchasing Buyer
- Warehouse Manager
- Store Manager (if retail)

#### Expected Outcome

Replenishment action is initiated within the defined response time — purchase requisition, purchase order, or transfer request. Inbound supply is tracked. If lead time risk exists, sales and customer service are warned of potential availability constraints. Stock is monitored daily until replenishment arrives and is received. Stockout is prevented.

#### Business Considerations

- Low stock is a warning, not a crisis — response time determines whether it becomes a stockout
- Reorder level must account for full operational lead time including receiving
- Check network for transfer options before defaulting to purchase
- Ignoring low-stock alerts because "we still have some" guarantees future stockouts
- Alert fatigue from poorly tuned thresholds erodes discipline — review policy regularly

---

### 13. Network Has Stock but Local Location Is Out

#### Description

A specific store or warehouse is out of stock on a product, but other locations in the distribution network hold available quantity. The local stockout is solvable without new purchasing — if the organization detects the imbalance and acts on it.

#### Actors Involved

- Store Manager / Warehouse Manager
- Network Planner / Inventory Controller
- Transportation / Logistics
- Sales / Customer Service

#### Expected Outcome

Network inventory visibility identifies available stock at other locations. An inter-location transfer is initiated to resolve the local stockout faster than supplier replenishment would. Customer orders are fulfilled from the transfer or redirected to a location with stock. Local stockout duration is minimized without incremental purchase cost.

#### Business Considerations

- Local stockouts are often network problems, not supply problems
- Transfer cost and time must be less than the cost of lost sale or emergency purchase
- Source location must be checked — transferring from another low site creates a new stockout
- Omnichannel pooling makes this scenario visible; siloed location management hides it
- Transfer decision should be systematic, not dependent on a store manager making phone calls

---

### 14. Emergency Transfer Request Between Locations

#### Description

A location urgently needs stock — a key customer order, a promotional event, or an unexpected demand spike — and standard replenishment lead time is too slow. An expedited inter-location transfer is requested from another site in the network.

#### Actors Involved

- Requesting Location Manager
- Source Location Manager
- Network Planner
- Transportation / Logistics
- Inventory Controller

#### Expected Outcome

Source location availability is verified (not just on-hand — ATP at source). Transfer is approved, picked, shipped, and received with expedited handling. Requesting location receives stock in time to meet the urgent need. Both locations' inventory records are updated. Cost of expedited transfer is documented for performance review.

#### Business Considerations

- Verify source ATP — emergency transfer that creates a stockout at source is a net failure
- Expedited freight cost should be authorized explicitly, not absorbed silently
- Emergency transfers should trigger review of why standard replenishment failed
- Priority rules needed when multiple locations request the same source stock
- Transfer is faster than purchase but not instant — factor transit time into promises

---

## Category 5: Commercial and Lifecycle Scenarios

---

### 15. Promotional Demand Exceeds Forecast

#### Description

A marketing promotion, price reduction, or media event drives customer demand significantly above the forecasted level. Stock depletes faster than planned and availability may not last through the promotional period.

#### Actors Involved

- Marketing / Merchandising
- Inventory / Supply Planner
- Purchasing Buyer
- Store Manager
- Sales / Customer Service
- Operations Leadership

#### Expected Outcome

Remaining stock is allocated to maximize promotional ROI — prioritized to promoted channels and locations. Expedited replenishment or network transfers are initiated if additional supply can arrive during the promotion. Marketing is informed of stock status to adjust campaign intensity. Customers are managed honestly if stock will not last. Post-promotion analysis captures forecast error for future planning.

#### Business Considerations

- Commercial and operations must align before the promotion — not during the crisis
- Pulling forward demand from future weeks creates a post-promotion demand valley
- Overselling a promotion damages brand trust more than a stockout on a regular item
- Emergency supply has premium cost — weigh against incremental promotional revenue
- "Available while supplies last" is a legitimate and honest commercial position

---

### 16. New Product Launch With Uncertain Demand

#### Description

The business introduces a new product with no sales history. Initial stock must be positioned across the network without reliable demand data. Risk of both stockout (under-allocate) and excess (over-allocate) is high.

#### Actors Involved

- Merchandising / Product Manager
- Inventory / Supply Planner
- Purchasing Buyer
- Marketing
- Store Manager
- Sales

#### Expected Outcome

Initial allocation is placed based on analogous product data, market research, and commercial judgment — with explicit acknowledgment of uncertainty. Soft allocation allows redirection before hard commitments. Sell-through is monitored daily in the first weeks. Stock is rebalanced quickly based on early demand signals. Exit plan exists for slow-performing locations if demand underperforms.

#### Business Considerations

- Perfect forecast is impossible for new products — plan for adjustment, not precision
- Initial allocation is a hypothesis — fast rebalancing is more valuable than perfect first guess
- Marketing commitments should be tied to confirmed stock positioning, not aspirations
- Supplier minimum order quantities may force more stock than demand justifies
- Launch excess is cheaper if identified early — delay in rebalancing compounds cost

---

### 17. End-of-Season Excess Inventory

#### Description

A seasonal product — apparel, holiday goods, garden supplies — has not sold through at the projected rate as the season ends. Remaining stock risks becoming obsolete, requiring markdown, transfer, or write-off.

#### Actors Involved

- Merchandising / Category Manager
- Inventory / Supply Planner
- Store Manager
- Marketing
- Finance
- Outlet / Clearance Channel Manager

#### Expected Outcome

Remaining stock is dispositioned through a planned exit strategy — in-season markdown, outlet channel transfer, return to supplier (if contract allows), donation, or write-off. Decision is made before obsolescence, not after. Working capital is freed. Carrying cost stops accumulating. Financial impact is recorded through appropriate channels (markdown, E&O provision, write-off).

#### Business Considerations

- Earlier markdown retains more value than delayed clearance
- Holding seasonal stock "until next year" often costs more than exit now
- Transfer to outlet channels recovers partial value vs. full write-off
- Finance needs advance notice of planned markdowns for margin forecasting
- Post-season analysis improves next year's buy quantity and allocation

---

### 18. Product Supersession and Old SKU Runout

#### Description

A manufacturer or the business replaces an existing product with a new version. The old SKU must be sold through, redirected, or written off while the new SKU is introduced — without customer confusion, duplicate stocking, or excess obsolete inventory.

#### Actors Involved

- Product Manager
- Purchasing Buyer
- Inventory Controller
- Sales / Customer Service
- Warehouse Manager
- Marketing

#### Expected Outcome

Supersession rules are published: old SKU is closed to new orders, existing stock is sold through on a defined timeline, new orders are directed to the replacement SKU. Remaining old stock is dispositioned (markdown, return, write-off) by the runout deadline. Customer-facing teams know which SKU to sell and how to handle existing orders for the old version.

#### Business Considerations

- Without supersession rules, customers order obsolete SKUs and old/new stock compete
- Sell-through timeline must be realistic — forced write-off is the alternative
- Service and warranty obligations may require old SKU parts availability for a defined period
- Sales teams need clear guidance on substitution — not ad hoc decisions per customer
- Supplier return or credit for unsold old stock should be negotiated at supersession time

---

## Category 6: Returns, Compliance, and Quality

---

### 19. Customer Return Requiring Inspection and Disposition

#### Description

A customer returns a product — due to defect, wrong item, dissatisfaction, or warranty claim. The returned item must be received, linked to the original order, inspected, and dispositioned as restock, refurbish, liquidate, or write-off.

#### Actors Involved

- Customer Service
- Warehouse Receiving / Returns Team
- Quality Control
- Inventory Controller
- Customer
- Finance (for refund processing)

#### Expected Outcome

Return is received against a valid return authorization linked to the original order. Item is inspected against restock criteria. Resalable goods re-enter sellable inventory. Defective or used goods are written off or liquidated. Customer refund or replacement is processed per policy. Return reason data is captured for trend analysis.

#### Business Considerations

- Auto-restocking without inspection sends damaged goods to the next customer
- Return reason trends reveal product quality and fulfillment accuracy issues
- Return volume spikes after holidays require planned capacity, not ad hoc scrambling
- Refund should not be processed until return is physically received (policy dependent)
- Restocked returns must be indistinguishable in quality from new stock — or labeled accordingly

---

### 20. Product Recall Requiring Lot Traceability

#### Description

A product defect, contamination, or regulatory issue requires recalling specific lots or batches from the supply chain. The business must identify every affected unit's location — warehouse, store, in-transit, or already shipped to customers — and remove it from circulation.

#### Actors Involved

- Quality Assurance / Regulatory
- Inventory Controller
- Warehouse Manager
- Store Manager
- Customer Service
- Legal / Compliance
- Supplier
- Logistics

#### Expected Outcome

All affected lot inventory is identified through lot traceability records and quarantined immediately. Shipped units are traced to customers for notification and return. Regulatory reporting requirements are met within mandated timelines. Unaffected lots continue to be sold. Recall scope is precise (lot-level), not blanket (entire product line). Root cause investigation begins in parallel.

#### Business Considerations

- Lot traceability is only as good as lot capture discipline at every transaction point
- Speed of quarantine limits consumer exposure and legal liability
- Customer communication must be clear, honest, and actionable
- Quarantined stock is excluded from ATP immediately — do not wait for investigation
- Post-recall review examines whether traceability gaps delayed response

---

### 21. Quality Hold on Received Inventory Lot

#### Description

Inbound inventory fails quality inspection, receives a supplier quality alert, or is flagged by an internal concern. The lot must be quarantined pending investigation — excluded from sellable stock until cleared or dispositioned.

#### Actors Involved

- Quality Control
- Receiving Team
- Inventory Controller
- Purchasing Buyer
- Supplier Quality Representative
- Warehouse Manager

#### Expected Outcome

Affected lot is moved to quarantine and excluded from ATP. Investigation determines whether the lot can be released, reworked, returned to supplier, or must be written off. Decision is documented with supporting evidence. Released stock re-enters sellable inventory. Rejected stock is dispositioned per supplier agreement. Customer orders depending on the quarantined lot are reassessed.

#### Business Considerations

- Quarantine must be physical and systemic — quarantined stock in pick locations is a compliance failure
- Customer orders pegged to the quarantined lot need immediate reassessment
- Supplier chargeback or replacement depends on documented evidence at receipt
- Release from quarantine requires authorized sign-off, not informal assumption
- Pattern of quality holds from a supplier is a sourcing decision, not just a QC event

---

## Category 7: Financial, Omnichannel, and Demand Shock

---

### 22. Operations and Finance Inventory Mismatch at Month-End

#### Description

At month-end close, operational inventory quantities and financial inventory valuation do not reconcile. Differences arise from timing (in-transit ownership), unrecorded adjustments, costing changes, or quantity discrepancies between systems of record.

#### Actors Involved

- Inventory Controller
- Finance / Accounting
- Warehouse Manager
- Operations Leadership
- External Auditor (if material)

#### Expected Outcome

Differences are categorized (timing, quantity, valuation) and investigated. Legitimate timing differences are documented with agreed cut-off rules. Quantity gaps trigger investigation and correction. Financial records are adjusted to reflect substantiated inventory position. Reconciliation is completed within the close calendar. Recurring gaps trigger process improvement.

#### Business Considerations

- Some timing difference is normal (in-transit) — agree on cut-off rules in advance
- Unexplained quantity gaps are control failures, not just reconciliation nuisances
- Operations and finance must use the same product, location, and unit definitions
- Material unreconciled gaps are audit findings
- Monthly reconciliation prevents year-end surprises

---

### 23. Channel Conflict Over Shared Inventory Pool

#### Description

In an omnichannel environment, the same network inventory pool serves multiple channels — online, retail stores, wholesale, marketplaces. Competing channel demand creates conflict over who gets limited stock: an online order vs. a walk-in customer, a marketplace order vs. a store display requirement.

#### Actors Involved

- E-commerce / Digital Team
- Store Manager
- Inventory Controller
- Commercial / Leadership
- Customer Service
- Wholesale Account Manager

#### Expected Outcome

Allocation follows documented channel priority rules. Conflicts are resolved consistently, not case-by-case under pressure. ATP is updated in real time across channels to prevent double-selling. Channel-specific safety buffers are considered for strategic positions (e.g., store display minimum). Performance is measured by channel without one channel consistently losing.

#### Business Considerations

- Channel priority rules must be set by leadership, not decided ad hoc by warehouse staff
- Real-time ATP across channels is prerequisite for omnichannel pooling
- Store associates resent online orders "taking their stock" without clear policy
- Wholesale contracts may have hard allocation that overrides retail needs
- Channel conflict is a sign of insufficient total stock or unclear governance

---

### 24. Obsolete Stock Requiring Write-Off Decision

#### Description

Inventory has no remaining commercial value — discontinued product, expired goods, irreparably damaged stock, or technology made irrelevant by supersession. It must be formally removed from active inventory and written off as a financial loss.

#### Actors Involved

- Inventory Controller
- Category Manager / Product Manager
- Finance
- Warehouse Manager
- Operations Leadership (for approval)
- Loss Prevention (if theft-related)

#### Expected Outcome

Obsolete stock is physically identified, segregated, and removed from sellable locations. Write-off is documented with reason code, evidence, and authorized approval. Financial records reflect the reduced inventory value. Physical disposal (scrap, donate, destroy) is completed per policy and regulatory requirements. Ghost stock is eliminated from the system.

#### Business Considerations

- Delayed write-offs inflate both operational and financial inventory misleadingly
- Write-off approval must be independent of the person who managed the stock
- Tax and regulatory implications vary by disposal method and product type
- Pattern of write-offs in a category signals buying, lifecycle, or forecasting problems
- Destroyed pharmaceutical or hazmat products require documented compliance

---

### 25. Flash Demand Spike From External Event

#### Description

An unplanned external event — viral social media mention, competitor stockout redirecting demand, weather event, news coverage — causes sudden, unexpected demand for a product the business did not forecast. Stock depletes in hours or days rather than weeks.

#### Actors Involved

- Sales / Customer Service
- Inventory / Supply Planner
- Purchasing Buyer
- Marketing
- Operations Leadership
- Supplier

#### Expected Outcome

Remaining stock is managed to maximize value — allocation rules applied, channels prioritized. Supply chain is assessed for fastest replenishment path. Marketing and sales communicate realistic availability. Price gouging or overcommitment is avoided. Post-event analysis captures the spike for future safety stock and supplier capacity consideration.

#### Business Considerations

- Flash spikes cannot be perfectly forecast — response speed matters more than prediction
- Overselling during a spike creates reputational damage that outlasts the revenue gain
- Supplier may also be caught short — verify replenishment feasibility before promising
- Opportunistic pricing may conflict with brand values and customer relationships
- Decide in advance whether flash-demand products get reserved for existing customers

---

## Scenario Response Patterns

Successful organizations recognize that most scenarios fall into a few response patterns:

| Pattern | Scenarios | Core Discipline |
|---------|-----------|-----------------|
| **Detect early, act before crisis** | Low stock, lead time extension, shrinkage trend | Monitoring, thresholds, trend analysis |
| **Verify before recording** | Short shipment, damaged goods, returns, receiving | Receipt discipline, inspection, documentation |
| **Check the network first** | Local stockout, emergency transfer, channel conflict | Network visibility, transfer before purchase |
| **Investigate before adjusting** | Count variance, phantom inventory, shrinkage | Root cause analysis, reason codes, independence |
| **Communicate proactively** | Supply delay, stockout, allocation conflict, recall | Customer and internal honesty, revised dates |
| **Plan exit before obsolescence** | End-of-season, supersession, obsolete write-off | Lifecycle management, markdown timing |
| **Align commercial and operations** | Promotion surge, launch, flash demand | S&OP, pre-event planning, sell-through monitoring |

---

## Related Documents

- Business Events Catalog (`business domain/business-events.md`)
- Business Workflow Descriptions (`business domain/business-workflows.md`)
- Business Process Analysis (`business domain/business-processes.md`)
- Inventory Management Best Practices (`Domain Knowledge/inventory-management-best-practices.md`)
- Core Inventory Management Concepts (`Domain Knowledge/core-inventory-management-concepts.md`)

---

*End of Common Business Scenarios Document*
