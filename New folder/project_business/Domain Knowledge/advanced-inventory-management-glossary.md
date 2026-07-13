# Advanced Inventory Management Glossary

**Document Owner:** Domain Expert  
**Purpose:** Define advanced and industry-specific inventory terminology for experienced practitioners, consultants, and cross-functional specialists  
**Audience:** Inventory planners, supply chain analysts, warehouse operations leaders, finance controllers, and domain experts  
**Scope:** Business and operational terminology — excludes basic terms covered in the Business Glossary (`business domain/business-glossary.md`)

---

## How to Use This Glossary

This glossary extends the foundational Business Glossary with **advanced, specialist, and industry terminology** used in distribution, retail, manufacturing, and healthcare supply chains. Terms here assume familiarity with core concepts such as SKU, ATP, reorder level, cycle counting, and fill rate.

Each entry provides a precise definition, the business context in which the term is used, related terms, and an example of how practitioners use it in conversation or reporting.

---

## Glossary Index

| # | Term | Category |
|---|------|----------|
| 1 | Capable-to-Promise (CTP) | Availability & Allocation |
| 2 | Hard Allocation | Availability & Allocation |
| 3 | Soft Allocation | Availability & Allocation |
| 4 | Pegging | Availability & Allocation |
| 5 | Quarantine Stock | Stock Status |
| 6 | In-Transit Inventory | Stock Status |
| 7 | Pipeline Inventory | Stock Status |
| 8 | Decoupling Stock | Stock Policy |
| 9 | Anticipation Inventory | Stock Policy |
| 10 | Days of Supply (DoS) | Planning Metrics |
| 11 | Weeks of Cover | Planning Metrics |
| 12 | Economic Order Quantity (EOQ) | Replenishment |
| 13 | Min-Max Replenishment | Replenishment |
| 14 | Demand-Driven Replenishment (DDMRP) | Replenishment |
| 15 | Distribution Requirements Planning (DRP) | Planning |
| 16 | Material Requirements Planning (MRP) | Planning |
| 17 | Sales and Operations Planning (S&OP) | Planning |
| 18 | ABC-XYZ Classification Matrix | Classification |
| 19 | FSN Analysis | Classification |
| 20 | SLOB (Slow-Moving and Obsolete) | Classification |
| 21 | GMROI | Financial Metrics |
| 22 | Days Inventory Outstanding (DIO) | Financial Metrics |
| 23 | Landed Cost | Financial Metrics |
| 24 | Weighted Average Cost (WAC) | Costing |
| 25 | Lower of Cost or Market (LCM) | Costing |
| 26 | On-Shelf Availability (OSA) | Retail Metrics |
| 27 | Phantom Inventory | Retail Metrics |
| 28 | OTIF (On Time In Full) | Performance |
| 29 | Perfect Order Rate | Performance |
| 30 | Bullwhip Effect | Supply Chain Dynamics |
| 31 | Advance Shipping Notice (ASN) | Inbound |
| 32 | Three-Way Match | Inbound |
| 33 | Dock-to-Stock Time | Inbound |
| 34 | Cross-Docking | Warehouse Flow |
| 35 | Forward Pick Area | Warehouse Layout |
| 36 | Slotting | Warehouse Layout |
| 37 | Wave Picking | Fulfillment Methods |
| 38 | Batch Picking | Fulfillment Methods |
| 39 | Zone Picking | Fulfillment Methods |
| 40 | Vendor-Managed Inventory (VMI) | Supply Arrangements |
| 41 | Consignment Inventory | Supply Arrangements |
| 42 | Drop Shipment | Supply Arrangements |
| 43 | Bonded Warehouse | Trade & Compliance |
| 44 | Lot Traceability | Traceability |
| 45 | Serialization | Traceability |
| 46 | Minimum Remaining Shelf Life (MRSL) | Perishables |
| 47 | Catch Weight | Product Handling |
| 48 | Bill of Materials (BOM) | Manufacturing |
| 49 | Work-in-Progress (WIP) | Manufacturing |
| 50 | Omnichannel Inventory Pooling | Omnichannel |
| 51 | Ship-from-Store | Omnichannel |
| 52 | Endless Aisle | Omnichannel |
| 53 | Initial Allocation | Retail Distribution |
| 54 | Break Bulk | Distribution |
| 55 | Stock Keeping Unit Rationalization | Assortment |
| 56 | Supersession | Product Lifecycle |
| 57 | Excess and Obsolete (E&O) Provision | Finance |
| 58 | Inventory Reconciliation | Finance & Control |
| 59 | Blind Count | Inventory Control |
| 60 | Physical Inventory Freeze | Inventory Control |

---

## Category 1: Availability and Allocation

---

### Capable-to-Promise (CTP)

| Attribute | Description |
|-----------|-------------|
| **Term** | Capable-to-Promise (CTP) |
| **Definition** | The quantity of product a business can promise to a customer by a specific date, considering not only current available stock but also planned production, inbound supply, and capacity constraints across the fulfillment network. CTP extends beyond ATP by incorporating future supply and operational capacity. |
| **Business Context** | Used when customers request delivery on a future date rather than immediately. Common in manufacturing, configure-to-order, and B2B distribution where lead times exceed zero. Sales and customer service use CTP to quote realistic delivery dates for orders that cannot be fulfilled from current stock alone. |
| **Related Terms** | Available-to-Promise (ATP), Inbound Stock, Lead Time, Pegging, Pipeline Inventory |
| **Example Usage** | *"The customer wants five hundred units delivered in three weeks — ATP shows only two hundred, but CTP confirms we can promise the full five hundred based on the inbound PO arriving next Tuesday and production completing Thursday."* |

---

### Hard Allocation

| Attribute | Description |
|-----------|-------------|
| **Term** | Hard Allocation |
| **Definition** | A firm, non-negotiable assignment of specific inventory units to a particular order, customer, project, or location. Hard-allocated stock cannot be reallocated to another demand source without formal de-allocation and approval. |
| **Business Context** | Applied to high-priority orders, contractual commitments, government contracts, or promotional launches where stock must be ring-fenced. Operations treat hard allocations as immovable — picking and shipping must honor the assignment. |
| **Related Terms** | Soft Allocation, Reserved Stock, Committed Stock, Order Reservation, Hard Allocation |
| **Example Usage** | *"Two hundred units are hard-allocated to the government contract — do not release them for retail orders even if the store is out of stock."* |

---

### Soft Allocation

| Attribute | Description |
|-----------|-------------|
| **Term** | Soft Allocation |
| **Definition** | A provisional assignment of inventory to a demand source that can be overridden or re-prioritized based on business rules, urgency changes, or management decision. Soft allocations guide planning but are not binding until converted to hard allocation or reservation. |
| **Business Context** | Used during demand planning, order promising, and network allocation before orders are confirmed. Allows planners to model how stock would be distributed without locking it. Common in initial store allocation and draft order processing. |
| **Related Terms** | Hard Allocation, Available-to-Promise, Initial Allocation, Order Reservation |
| **Example Usage** | *"The system soft-allocated three hundred units across the eastern stores for the launch, but we can still redirect one hundred to the warehouse if online demand exceeds forecast."* |

---

### Pegging

| Attribute | Description |
|-----------|-------------|
| **Term** | Pegging |
| **Definition** | The practice of linking supply (purchase orders, production orders, transfers) to specific demand (customer orders, forecast, safety stock requirements) to show which inbound supply is intended to fulfill which outbound need. |
| **Business Context** | Essential in MRP, DRP, and complex B2B environments where customers ask "which PO is covering my order?" Pegging provides traceability between supply and demand, supporting prioritization when supply is short. |
| **Related Terms** | Capable-to-Promise, Material Requirements Planning, Inbound Stock, Backorder |
| **Example Usage** | *"Pegging shows that PO 44821 is directly tied to Customer Order 99012 — if that PO is delayed, we need to notify the customer immediately."* |

---

## Category 2: Stock Types and Status

---

### Quarantine Stock

| Attribute | Description |
|-----------|-------------|
| **Term** | Quarantine Stock |
| **Definition** | Inventory that is physically present but isolated from sellable or usable stock pending quality inspection, regulatory clearance, investigation, or disposition decision. Quarantined stock is excluded from ATP and cannot be picked, shipped, or sold. |
| **Business Context** | Standard practice in pharmaceuticals, food, medical devices, and any industry with quality hold requirements. Triggered by receipt inspection failures, customer complaints, recall investigations, or regulatory holds. |
| **Related Terms** | Quality Hold, Lot Traceability, Goods Receipt, Write-Off, Available-to-Promise |
| **Example Usage** | *"Move all units from Lot 2026-0412 to quarantine — quality flagged a contamination risk and nothing ships until lab results are back."* |

---

### In-Transit Inventory

| Attribute | Description |
|-----------|-------------|
| **Term** | In-Transit Inventory |
| **Definition** | Stock that has left the sending location but has not yet been received and verified at the destination. In-transit inventory is in a legal and operational limbo — ownership and risk depend on Incoterms or contractual terms. |
| **Business Context** | Critical in multi-location networks, international trade, and inter-company transfers. Finance, operations, and purchasing must agree on when in-transit stock appears on whose books. Discrepancies between sent and received quantities are common at this stage. |
| **Related Terms** | Incoterms, Inter-Location Transfer, Goods Receipt, Pipeline Inventory, Bonded Warehouse |
| **Example Usage** | *"We have four hundred units in transit from the Dallas DC to the Chicago store — they won't be available for sale until receipt is confirmed tomorrow morning."* |

---

### Pipeline Inventory

| Attribute | Description |
|-----------|-------------|
| **Term** | Pipeline Inventory |
| **Definition** | The total inventory investment tied up across the entire supply chain — including stock at suppliers, in transit, at distribution centers, at stores, and in the production pipeline. Pipeline inventory represents the full end-to-end stock holding, not just what is in the warehouse. |
| **Business Context** | Used by supply chain strategists and finance to assess total working capital committed to inventory across the network. Reducing pipeline inventory without harming service levels is a primary supply chain optimization goal. |
| **Related Terms** | In-Transit Inventory, Inbound Stock, Carrying Cost, Days Inventory Outstanding, Distribution Network |
| **Example Usage** | *"Our warehouse on-hand is $2 million, but total pipeline inventory including in-transit and supplier-held stock is $3.8 million — that's the number finance cares about."* |

---

## Category 3: Stock Policy and Planning

---

### Decoupling Stock

| Attribute | Description |
|-----------|-------------|
| **Term** | Decoupling Stock |
| **Definition** | Inventory held deliberately between dependent stages of the supply chain to insulate one stage from disruptions or variability in an adjacent stage. Decoupling stock breaks the direct dependency between supplier output and customer demand or between production stages. |
| **Business Context** | Found between manufacturing and distribution, between supplier and buyer, or between production line stages. Allows downstream operations to continue when upstream supply is interrupted. Distinct from safety stock, which buffers against demand uncertainty. |
| **Related Terms** | Safety Stock, Buffer Stock, Lead Time, Pipeline Inventory |
| **Example Usage** | *"We hold two weeks of decoupling stock at the DC so store replenishment continues even if the factory has a planned maintenance shutdown."* |

---

### Anticipation Inventory

| Attribute | Description |
|-----------|-------------|
| **Term** | Anticipation Inventory |
| **Definition** | Stock built up in advance of a known future event — seasonal peak, planned price increase, promotional campaign, plant shutdown, or product launch — when current production or purchasing capacity cannot meet demand at the time it will occur. |
| **Business Context** | Common in seasonal retail (holiday builds), agriculture, and manufacturing with capacity constraints. Requires coordinated planning between commercial, operations, and finance to avoid post-event excess. |
| **Related Terms** | Safety Stock, Replenishment, Sales and Operations Planning, SLOB, Promotional Inventory |
| **Example Usage** | *"Anticipation inventory for the back-to-school season starts building in June — we need six weeks of cover in stores by August first."* |

---

### Economic Order Quantity (EOQ)

| Attribute | Description |
|-----------|-------------|
| **Term** | Economic Order Quantity (EOQ) |
| **Definition** | The calculated order quantity that minimizes the total combined cost of placing orders (ordering cost) and holding inventory (carrying cost). EOQ balances the expense of frequent small orders against the expense of holding large quantities. |
| **Business Context** | Used by inventory planners and buyers as a baseline for order sizing, often adjusted for supplier minimums, case packs, truckload optimization, and practical constraints. A foundational concept in inventory theory applied pragmatically in industry. |
| **Related Terms** | Carrying Cost, Reorder Level, Min-Max Replenishment, Replenishment |
| **Example Usage** | *"EOQ for this bearing is seven hundred and seventy-five units — we're ordering eight hundred to match the supplier's case pack."* |

---

### Min-Max Replenishment

| Attribute | Description |
|-----------|-------------|
| **Term** | Min-Max Replenishment |
| **Definition** | A replenishment method where each product at each location has a defined minimum level (trigger) and maximum level (target). When stock falls to the minimum, an order is placed to bring inventory up to the maximum. |
| **Business Context** | Widely used in retail store replenishment, MRO supplies, and environments requiring simple, transparent rules. Easier to implement and audit than EOQ-based models. Store managers and buyers understand min-max intuitively. |
| **Related Terms** | Reorder Level, Replenishment, Economic Order Quantity, Safety Stock |
| **Example Usage** | *"Store 1042 hit min on the cereal SKU — the replenishment order will top us up to the max of seventy-two units."* |

---

### Demand-Driven Replenishment (DDMRP)

| Attribute | Description |
|-----------|-------------|
| **Term** | Demand-Driven Material Requirements Planning (DDMRP) |
| **Definition** | A planning methodology that positions strategic inventory buffers at key decoupling points in the supply chain and replenishes based on actual demand consumption rather than forecast-driven push. Buffers are sized dynamically using lead time, variability, and priority factors. |
| **Business Context** | Adopted by manufacturers and distributors seeking to reduce bullwhip effect and improve flow without heavy reliance on forecast accuracy. Positions inventory where variability is highest and protects downstream flow. |
| **Related Terms** | Decoupling Stock, Safety Stock, Material Requirements Planning, Bullwhip Effect |
| **Example Usage** | *"We've implemented DDMRP buffers at the regional DCs — replenishment now triggers on buffer penetration, not on the old MRP forecast explosion."* |

---

### Distribution Requirements Planning (DRP)

| Attribute | Description |
|-----------|-------------|
| **Term** | Distribution Requirements Planning (DRP) |
| **Definition** | A time-phased planning process that determines what inventory is needed at each distribution location, when it is needed, and how much to ship or replenish — based on forecasted demand, current stock, lead times, and network constraints. |
| **Business Context** | Used by multi-echelon distribution networks to coordinate replenishment from central warehouses to regional DCs and stores. Bridges demand planning and physical distribution. The distribution equivalent of MRP for manufacturing. |
| **Related Terms** | Material Requirements Planning, Replenishment, Distribution Network, Sales and Operations Planning |
| **Example Usage** | *"DRP shows the southeast region needs a bulk transfer of two thousand units next week — the central DC has the stock and the transit time fits."* |

---

### Material Requirements Planning (MRP)

| Attribute | Description |
|-----------|-------------|
| **Term** | Material Requirements Planning (MRP) |
| **Definition** | A time-phased planning process that calculates component and raw material requirements based on master production schedules, bill of materials explosions, current inventory, and lead times. MRP answers: what to buy or make, how much, and when. |
| **Business Context** | Core planning method in manufacturing environments. Drives purchase orders for raw materials and production orders for sub-assemblies. Accuracy depends on reliable BOMs, lead times, and inventory records. |
| **Related Terms** | Bill of Materials, Work-in-Progress, Distribution Requirements Planning, Pegging |
| **Example Usage** | *"MRP exploded the production schedule and generated purchase requisitions for twelve components — three are short and need expediting."* |

---

### Sales and Operations Planning (S&OP)

| Attribute | Description |
|-----------|-------------|
| **Term** | Sales and Operations Planning (S&OP) |
| **Definition** | A cross-functional monthly (or weekly) management process that aligns demand forecasts, supply plans, inventory targets, and financial goals. S&OP reconciles what sales expects to sell with what operations can supply and what finance will fund. |
| **Business Context** | Executive-level discipline connecting commercial ambition to operational reality. Prevents inventory crises from forecast-supply misalignment. Mature organizations treat S&OP as the primary forum for inventory investment decisions. |
| **Related Terms** | Anticipation Inventory, Replenishment, Distribution Requirements Planning, Fill Rate |
| **Example Usage** | *"S&OP agreed on a two percent inventory increase for Q4 to support the holiday promotion — purchasing is authorized to build anticipation stock starting in September."* |

---

## Category 4: Classification and Analysis

---

### ABC-XYZ Classification Matrix

| Attribute | Description |
|-----------|-------------|
| **Term** | ABC-XYZ Classification Matrix |
| **Definition** | A two-dimensional classification combining ABC analysis (value/importance on the Y-axis) with XYZ analysis (demand variability on the X-axis). AX items are high-value with stable demand; CZ items are low-value with highly erratic demand. Each cell receives differentiated management policies. |
| **Business Context** | Used by advanced inventory planners to set safety stock, count frequency, and replenishment methods with more precision than ABC alone. AX items need tight control but predictable planning; CZ items need minimal investment and high tolerance for stockouts. |
| **Related Terms** | ABC Classification, FSN Analysis, Safety Stock, Cycle Count |
| **Example Usage** | *"This SKU is AZ — high revenue but wildly unpredictable demand — we need higher safety stock and weekly review despite it being Class A."* |

---

### FSN Analysis

| Attribute | Description |
|-----------|-------------|
| **Term** | FSN Analysis (Fast, Slow, Non-moving) |
| **Definition** | A classification method grouping products by movement velocity: Fast-moving (regular turnover), Slow-moving (infrequent sales), and Non-moving (no sales in a defined period). FSN complements ABC by focusing purely on movement rate rather than value. |
| **Business Context** | Used to identify dead stock candidates, set count priorities, and drive SKU rationalization. Non-moving items are prime candidates for write-off, clearance, or discontinuation. Often combined with ABC for comprehensive classification. |
| **Related Terms** | ABC Classification, SLOB, Stock Keeping Unit Rationalization, Inventory Turnover |
| **Example Usage** | *"FSN analysis flagged four hundred non-moving SKUs that haven't sold in twelve months — that's $800K in dead stock we need to disposition."* |

---

### SLOB (Slow-Moving and Obsolete)

| Attribute | Description |
|-----------|-------------|
| **Term** | SLOB (Slow-Moving and Obsolete) |
| **Definition** | Inventory that is either selling significantly below expected velocity (slow-moving) or no longer sellable due to product discontinuation, model changes, expiry, or market irrelevance (obsolete). SLOB is a primary source of inventory write-downs and carrying cost waste. |
| **Business Context** | Finance and operations track SLOB as a health indicator. Regular SLOB reviews are a best practice to prevent capital entrapment. Common metric in earnings calls and working capital improvement programs. |
| **Related Terms** | Excess and Obsolete Provision, FSN Analysis, Write-Off, Inventory Turnover, Aged Inventory |
| **Example Usage** | *"Q3 SLOB increased to $1.4 million — we need a clearance plan for the obsolete phone cases before year-end close."* |

---

## Category 5: Financial and Performance Metrics

---

### GMROI (Gross Margin Return on Investment)

| Attribute | Description |
|-----------|-------------|
| **Term** | GMROI (Gross Margin Return on Investment) |
| **Definition** | A retail and distribution profitability metric calculated as gross margin dollars divided by average inventory cost. GMROI measures how many gross margin dollars are generated for every dollar invested in inventory. Higher GMROI indicates more profitable use of inventory investment. |
| **Business Context** | Used by retail merchants, category managers, and finance to evaluate whether a product category earns enough margin to justify its inventory investment. Complements turnover by adding profitability dimension. A fast-turning item with low margin may have worse GMROI than a slower item with high margin. |
| **Related Terms** | Inventory Turnover, Carrying Cost, ABC Classification, Inventory Valuation |
| **Example Usage** | *"Category GMROI is 2.8 — we're earning $2.80 in gross margin for every dollar of inventory, which is above the chain target of 2.5."* |

---

### Days Inventory Outstanding (DIO)

| Attribute | Description |
|-----------|-------------|
| **Term** | Days Inventory Outstanding (DIO) |
| **Definition** | A financial metric measuring the average number of days inventory is held before being sold, calculated as (Average Inventory ÷ Cost of Goods Sold) × 365. DIO indicates how quickly inventory converts to revenue. |
| **Business Context** | Used by finance, investors, and supply chain leadership to benchmark inventory efficiency across periods, business units, and competitors. Declining DIO generally indicates improving efficiency; rising DIO signals slowing movement or overstock. |
| **Related Terms** | Inventory Turnover, Days of Supply, Carrying Cost, Cash-to-Cash Cycle |
| **Example Usage** | *"DIO improved from fifty-two to forty-six days this quarter — we're freeing working capital without hurting fill rate."* |

---

### Days of Supply (DoS)

| Attribute | Description |
|-----------|-------------|
| **Term** | Days of Supply (DoS) |
| **Definition** | An operational metric showing how many days current inventory will last at the current or forecasted rate of consumption or sales. Calculated as On-Hand Quantity ÷ Average Daily Demand. |
| **Business Context** | Used by planners, buyers, and operations for day-to-day replenishment decisions. More intuitive than absolute unit quantities for comparing products with different velocities. DoS triggers action when it falls below lead time coverage. |
| **Related Terms** | Weeks of Cover, Reorder Level, Safety Stock, Low Stock |
| **Example Usage** | *"We're at four days of supply on this SKU and lead time is ten days — we're already in the danger zone."* |

---

### Weeks of Cover

| Attribute | Description |
|-----------|-------------|
| **Term** | Weeks of Cover |
| **Definition** | The number of weeks current inventory will sustain at projected weekly demand. Functionally equivalent to Days of Supply but expressed in weekly units, commonly used in retail and consumer goods for seasonal planning. |
| **Business Context** | Retail buyers and merchandisers think in weeks when planning seasonal builds and promotional inventory. "Eight weeks of cover going into the holiday season" is a standard planning conversation. |
| **Related Terms** | Days of Supply, Anticipation Inventory, Replenishment, Overstock |
| **Example Usage** | *"We have fourteen weeks of cover on the winter jacket — that's four weeks too many; start the markdown plan."* |

---

### Landed Cost

| Attribute | Description |
|-----------|-------------|
| **Term** | Landed Cost |
| **Definition** | The total cost of a product when it arrives at the buyer's location, including purchase price plus all associated costs: freight, insurance, duties, tariffs, handling, and inbound logistics. Landed cost is the true cost basis for inventory valuation on imported goods. |
| **Business Context** | Essential for international sourcing decisions, margin analysis, and accurate inventory valuation. Comparing supplier quotes on purchase price alone without landed cost leads to poor sourcing decisions and margin erosion. |
| **Related Terms** | Inventory Valuation, Incoterms, Bonded Warehouse, Weighted Average Cost |
| **Example Usage** | *"The unit price from the Asian supplier is lower, but landed cost is eight percent higher once we add freight and duties — the domestic supplier is actually cheaper."* |

---

### Weighted Average Cost (WAC)

| Attribute | Description |
|-----------|-------------|
| **Term** | Weighted Average Cost (WAC) |
| **Definition** | An inventory costing method that recalculates the average unit cost after each receipt by blending the cost of existing stock with the cost of newly received stock. All units are valued at the same average cost regardless of when they were purchased. |
| **Business Context** | Common costing method in distribution and retail where FIFO/LIFO physical rotation is practiced but financial costing uses a blended average. Simplifies valuation when purchase prices fluctuate frequently. |
| **Related Terms** | Inventory Valuation, FIFO, Landed Cost, Cost of Goods Sold |
| **Example Usage** | *"After this receipt, the weighted average cost moved from $4.20 to $4.35 per unit — margin reports need to reflect the new cost."* |

---

### Lower of Cost or Market (LCM)

| Attribute | Description |
|-----------|-------------|
| **Term** | Lower of Cost or Market (LCM) |
| **Definition** | An accounting principle requiring inventory to be valued at the lower of its original cost or its current market value (net realizable value). When market value drops below cost — due to obsolescence, damage, or price decline — inventory must be written down. |
| **Business Context** | Drives inventory write-downs during financial close, especially for seasonal, fashion, and technology products subject to rapid devaluation. Finance and operations must collaborate to identify items requiring LCM adjustment. |
| **Related Terms** | Write-Off, Excess and Obsolete Provision, Inventory Valuation, SLOB |
| **Example Usage** | *"Year-end LCM review requires a $200K write-down on last season's apparel — market value is below carrying cost."* |

---

### OTIF (On Time In Full)

| Attribute | Description |
|-----------|-------------|
| **Term** | OTIF (On Time In Full) |
| **Definition** | A supply chain performance metric measuring the percentage of deliveries that arrive on the committed date and in the complete ordered quantity. OTIF combines timeliness and completeness into a single service measure. |
| **Business Context** | Widely used in retail-supplier relationships, B2B contracts, and third-party logistics scorecards. Retailers increasingly impose OTIF penalties on suppliers. Internally, measures both inbound supplier performance and outbound customer delivery performance. |
| **Related Terms** | Fill Rate, Perfect Order Rate, Lead Time, Supplier Performance |
| **Example Usage** | *"Supplier OTIF dropped to eighty-eight percent this quarter — we're missing promotional launch dates and incurring penalties."* |

---

### Perfect Order Rate

| Attribute | Description |
|-----------|-------------|
| **Term** | Perfect Order Rate |
| **Definition** | The percentage of orders delivered with no defects across all dimensions: complete quantity, on time, undamaged, with accurate documentation, and to the correct location. A perfect order meets every criterion simultaneously. |
| **Business Context** | The gold standard customer service metric in distribution and e-commerce. Decomposing imperfect orders by failure type (late, incomplete, damaged, wrong item) reveals whether inventory, warehouse, or carrier is the root cause. |
| **Related Terms** | OTIF, Fill Rate, Pick Pack and Ship, Partial Fulfillment |
| **Example Usage** | *"Perfect order rate is ninety-one percent — the biggest failure mode is incomplete shipments, which points to inventory accuracy or pick errors."* |

---

### On-Shelf Availability (OSA)

| Attribute | Description |
|-----------|-------------|
| **Term** | On-Shelf Availability (OSA) |
| **Definition** | The percentage of time a product is physically present on the retail shelf (or in the customer-accessible location) when a customer would want to buy it. OSA measures the last step of the inventory chain — from warehouse to shelf — not just warehouse stock. |
| **Business Context** | Critical retail metric distinct from warehouse fill rate. A store may have stock in the backroom but zero OSA if shelves are empty. OSA losses from poor shelf replenishment are often invisible in warehouse-centric reporting. |
| **Related Terms** | Phantom Inventory, Fill Rate, Stockout, Shelf Replenishment |
| **Example Usage** | *"Warehouse fill rate is ninety-eight percent but OSA on the promoted SKU is only eighty-two percent — the problem is shelf restocking, not supply."* |

---

### Phantom Inventory

| Attribute | Description |
|-----------|-------------|
| **Term** | Phantom Inventory |
| **Definition** | A condition where the inventory system shows stock as available, but no physical product exists on the shelf or in the warehouse. The "ghost" quantity cannot be sold, picked, or seen by customers despite positive system records. |
| **Business Context** | A major retail and e-commerce problem causing lost sales, false ATP, and customer frustration. Caused by unrecorded shrinkage, unprocessed returns, receiving errors, and failure to record damages. Often discovered when a customer or picker cannot find system-indicated stock. |
| **Related Terms** | On-Shelf Availability, Inventory Accuracy, Shrinkage, Stock Adjustment |
| **Example Usage** | *"The system says twelve units in Store 205, but the shelf is empty — this is phantom inventory from unrecorded theft over the past two weeks."* |

---

## Category 6: Supply Chain Dynamics

---

### Bullwhip Effect

| Attribute | Description |
|-----------|-------------|
| **Term** | Bullwhip Effect |
| **Definition** | The phenomenon where small fluctuations in end-customer demand amplify into progressively larger swings in orders placed upstream through the supply chain — from retailer to distributor to manufacturer to raw material supplier. Each stage overreacts to the previous stage's orders. |
| **Business Context** | Explains why supply chains experience excess inventory followed by severe shortages despite relatively stable consumer demand. Mitigated through information sharing, VMI, reduced order batching, and demand-driven replenishment. A core concept in supply chain management education and consulting. |
| **Related Terms** | Safety Stock, Demand-Driven Replenishment, Sales and Operations Planning, Pipeline Inventory |
| **Example Usage** | *"The bullwhip effect hit us after the promotion — stores ordered conservatively, the DC panicked and tripled its PO, and now we have six months of excess at the supplier."* |

---

## Category 7: Inbound and Warehouse Operations

---

### Advance Shipping Notice (ASN)

| Attribute | Description |
|-----------|-------------|
| **Term** | Advance Shipping Notice (ASN) |
| **Definition** | An electronic notification sent by the supplier or carrier to the buyer before goods arrive, detailing shipment contents: products, quantities, lot numbers, packaging, and expected arrival time. ASNs enable pre-receiving preparation and automated receipt verification. |
| **Business Context** | Standard in retail and distribution EDI relationships. Receiving teams use ASNs to plan dock labor, pre-allocate storage locations, and scan-verify deliveries upon arrival. Reduces receiving time and improves receipt accuracy. |
| **Related Terms** | Goods Receipt, Purchase Order, Three-Way Match, Dock-to-Stock Time |
| **Example Usage** | *"ASN for PO 55219 arrived this morning — receiving is pre-staging dock space for twelve pallets expected at 2 PM."* |

---

### Three-Way Match

| Attribute | Description |
|-----------|-------------|
| **Term** | Three-Way Match |
| **Definition** | The control process of verifying that three documents agree before approving supplier payment: the purchase order (what was ordered), the goods receipt (what was received), and the supplier invoice (what is being billed). Payment is authorized only when all three match within tolerance. |
| **Business Context** | A fundamental accounts payable control in procurement. Prevents paying for goods not ordered, not received, or billed at wrong prices. Receiving accuracy directly affects the ability to three-way match and pay suppliers on time. |
| **Related Terms** | Purchase Order, Goods Receipt, Receipt Discrepancy, Landed Cost |
| **Example Usage** | *"Invoice 8834 failed three-way match — the supplier billed for one thousand units but we only received nine hundred and fifty. Payment is on hold."* |

---

### Dock-to-Stock Time

| Attribute | Description |
|-----------|-------------|
| **Term** | Dock-to-Stock Time |
| **Definition** | The elapsed time from when goods arrive at the receiving dock to when they are verified, put away, and recorded as available sellable or pickable stock. Measures inbound operational efficiency. |
| **Business Context** | A key warehouse KPI. Long dock-to-stock times delay product availability, congest receiving areas, and extend lead times. Best-in-class operations target hours, not days. Directly impacts CTP and replenishment responsiveness. |
| **Related Terms** | Put-Away, Goods Receipt, Cross-Docking, Advance Shipping Notice |
| **Example Usage** | *"Dock-to-stock time averaged eighteen hours last month — we need to hit the four-hour SLA to support same-day fulfillment."* |

---

### Cross-Docking

| Attribute | Description |
|-----------|-------------|
| **Term** | Cross-Docking |
| **Definition** | A logistics practice where inbound goods are transferred directly from receiving to outbound shipping with minimal or no storage. Products are sorted at the dock by destination and loaded onto outbound vehicles, bypassing put-away and long-term storage. |
| **Business Context** | Standard for high-velocity retail replenishment, perishable goods, and pre-allocated store deliveries. Reduces handling cost, storage requirements, and lead time. Requires precise inbound scheduling and outbound routing coordination. |
| **Related Terms** | Put-Away, Dock-to-Stock Time, Distribution Requirements Planning, Break Bulk |
| **Example Usage** | *"Tonight's inbound pallets are cross-docked straight to the outbound route trucks — nothing goes to storage."* |

---

### Forward Pick Area

| Attribute | Description |
|-----------|-------------|
| **Term** | Forward Pick Area |
| **Definition** | A warehouse zone positioned close to packing and shipping stations where fast-moving products are stored in pick-ready quantities. The forward pick area (or pick face) is replenished from bulk storage in the main warehouse. |
| **Business Context** | Core warehouse design concept for reducing picker travel time. High-velocity SKUs are concentrated in the forward pick area; slow movers remain in remote bulk storage. Replenishment of the pick face is a continuous intraday activity. |
| **Related Terms** | Slotting, Bulk Storage, Velocity-Based Slotting, Pick Pack and Ship |
| **Example Usage** | *"The forward pick area for aisle three is running low on the top-twenty SKUs — schedule a bulk replenishment from deep storage before the afternoon wave."* |

---

### Slotting

| Attribute | Description |
|-----------|-------------|
| **Term** | Slotting |
| **Definition** | The practice of assigning products to optimal storage locations within a warehouse based on velocity, size, weight, compatibility, and pick frequency. Slotting determines which bin, shelf, or rack position each SKU occupies. |
| **Business Context** | Ongoing warehouse optimization activity. Poor slotting wastes picker labor; good slotting can improve productivity by fifteen to thirty percent without adding staff. Slotting reviews are conducted quarterly or when demand patterns shift significantly. |
| **Related Terms** | Forward Pick Area, Velocity-Based Slotting, Warehouse, Pick Pack and Ship |
| **Example Usage** | *"The slotting review moved our top fifty SKUs to the forward pick zone — average pick path dropped by twenty-two percent."* |

---

### Wave Picking

| Attribute | Description |
|-----------|-------------|
| **Term** | Wave Picking |
| **Definition** | A fulfillment method where orders are grouped into batches (waves) released for picking at scheduled intervals throughout the day. Each wave may be sorted by carrier cutoff, priority, route, or product zone. |
| **Business Context** | Standard in high-volume warehouses and e-commerce fulfillment centers. Balances picking efficiency (batching similar orders) with shipping deadlines (carrier cutoff times). Wave planning is a daily operations scheduling activity. |
| **Related Terms** | Batch Picking, Zone Picking, Pick Pack and Ship, Order Fulfillment |
| **Example Usage** | *"Release Wave 3 at 1 PM — it covers four hundred and fifty orders for the FedEx cutoff at 5 PM."* |

---

### Batch Picking

| Attribute | Description |
|-----------|-------------|
| **Term** | Batch Picking |
| **Definition** | A picking method where a single picker collects the same SKU for multiple orders in one trip through the warehouse, then sorts items into individual orders at a staging area. Reduces repeated travel to the same location for different orders. |
| **Business Context** | Efficient when many orders contain the same popular SKUs. Common in e-commerce and catalog fulfillment. Requires a sortation step after picking. Most effective combined with wave or zone picking strategies. |
| **Related Terms** | Wave Picking, Zone Picking, Pick Pack and Ship, Forward Pick Area |
| **Example Usage** | *"Batch-pick all orders needing the bestseller SKU — there are eighty orders, so one trip to bin A-14 covers them all."* |

---

### Zone Picking

| Attribute | Description |
|-----------|-------------|
| **Term** | Zone Picking |
| **Definition** | A picking method where the warehouse is divided into zones, and each picker is responsible only for picking items within their assigned zone. Orders pass through multiple zones, with each zone adding its items before moving to the next. |
| **Business Context** | Used in large warehouses where full-facility travel per order is inefficient. Pickers become experts in their zone. Requires order routing between zones and a consolidation point. Often combined with wave picking for scheduling. |
| **Related Terms** | Wave Picking, Batch Picking, Slotting, Forward Pick Area |
| **Example Usage** | *"Zone C picker handles all frozen items — the order tote moves to Zone D for ambient goods after C is complete."* |

---

## Category 8: Supply Arrangements

---

### Vendor-Managed Inventory (VMI)

| Attribute | Description |
|-----------|-------------|
| **Term** | Vendor-Managed Inventory (VMI) |
| **Definition** | A supply arrangement where the supplier monitors the buyer's inventory levels and initiates replenishment shipments based on agreed rules, targets, or consumption data — rather than the buyer placing individual purchase orders. |
| **Business Context** | Common in retail (supplier manages shelf stock), automotive, and industrial MRO. Reduces buyer administrative burden and improves supplier visibility to actual demand. Requires trust, data sharing, and clear performance agreements. |
| **Related Terms** | Consignment Inventory, Replenishment, Bullwhip Effect, Supplier |
| **Example Usage** | *"Under the VMI agreement, the supplier monitors our daily consumption and maintains two weeks of cover — we don't place POs unless there's an exception."* |

---

### Consignment Inventory

| Attribute | Description |
|-----------|-------------|
| **Term** | Consignment Inventory |
| **Definition** | Stock physically held at the buyer's location but owned by the supplier until the buyer consumes, sells, or issues it. The buyer does not pay for or record consignment stock as owned inventory until ownership transfers per agreement terms. |
| **Business Context** | Reduces buyer working capital risk while ensuring product availability. Common in automotive parts, industrial supplies, and retail display stock. Requires clear tracking of consigned vs. owned stock and periodic reconciliation with the supplier. |
| **Related Terms** | Vendor-Managed Inventory, Inventory Valuation, Pipeline Inventory |
| **Example Usage** | *"The consignment stock in Bay 7 is still owned by the supplier — we only take ownership when a work order issues the part."* |

---

### Drop Shipment

| Attribute | Description |
|-----------|-------------|
| **Term** | Drop Shipment |
| **Definition** | A fulfillment method where the seller accepts a customer order but the supplier or manufacturer ships the product directly to the customer. The seller never physically handles the inventory — it ships from the supplier's warehouse to the end customer. |
| **Business Context** | Enables catalog and e-commerce expansion without inventory investment. Common for bulky, low-velocity, or specialty items. The seller manages the customer relationship; the supplier manages fulfillment. Inventory risk and carrying cost remain with the supplier. |
| **Related Terms** | Pipeline Inventory, Vendor-Managed Inventory, Order Fulfillment, Omnichannel Inventory Pooling |
| **Example Usage** | *"The custom furniture line is drop-ship only — we take the order, the manufacturer ships direct to the customer, and we never hold it in our warehouse."* |

---

## Category 9: Trade, Compliance, and Traceability

---

### Bonded Warehouse

| Attribute | Description |
|-----------|-------------|
| **Term** | Bonded Warehouse |
| **Definition** | A secured facility licensed by customs authorities where imported goods are stored without payment of duties and taxes until the goods are released for domestic sale, re-exported, or otherwise dispositioned. Inventory in bonded storage is under customs control. |
| **Business Context** | Used by importers to defer duty payments until goods are sold, manage re-export operations, and comply with customs regulations. Inventory in bonded warehouses is tracked separately from domestic stock and subject to customs audit. |
| **Related Terms** | Landed Cost, In-Transit Inventory, Incoterms, Inventory Valuation |
| **Example Usage** | *"Hold the imported electronics in the bonded warehouse until we confirm domestic demand — we don't want to pay duties on units we might re-export."* |

---

### Lot Traceability

| Attribute | Description |
|-----------|-------------|
| **Term** | Lot Traceability |
| **Definition** | The ability to track a product lot or batch from its origin through every movement, transformation, and transaction — receipt, storage, pick, ship, and return — enabling targeted recall, quality investigation, and regulatory compliance. |
| **Business Context** | Legally required in pharmaceuticals (DSCSA), food (FSMA), medical devices, and aerospace. Operationally valuable in any industry where defect isolation prevents full-product-line recalls. Lot traceability depends on disciplined lot capture at every transaction point. |
| **Related Terms** | Serialization, Quarantine Stock, Minimum Remaining Shelf Life, Recall |
| **Example Usage** | *"Lot traceability shows that defective batch 2026-0412 was shipped to forty-three customers — initiate targeted recall, not a full product withdrawal."* |

---

### Serialization

| Attribute | Description |
|-----------|-------------|
| **Term** | Serialization |
| **Definition** | Assigning a unique serial number to each individual unit of a product (not just each lot) and tracking that unit through every transaction in the supply chain. Serialization provides unit-level traceability beyond lot-level tracking. |
| **Business Context** | Mandated for prescription pharmaceuticals in the US (DSCSA) and EU (FMD). Growing in luxury goods (anti-counterfeiting), electronics (warranty), and high-value industrial components. Requires scanning and recording at unit level for every movement. |
| **Related Terms** | Lot Traceability, GS1 Standards, Quarantine Stock, Recall |
| **Example Usage** | *"Every unit must be scanned at ship and receive for serialization compliance — we need to report the serial number chain to the FDA."* |

---

### Minimum Remaining Shelf Life (MRSL)

| Attribute | Description |
|-----------|-------------|
| **Term** | Minimum Remaining Shelf Life (MRSL) |
| **Definition** | The minimum acceptable remaining shelf life (expressed in days or percentage) that a product must have at the time of receipt, shipment, or sale. Products below MRSL are rejected at receipt or cannot be shipped to customers. |
| **Business Context** | Standard requirement in grocery, pharmaceutical, and cosmetic supply chains. Buyers set MRSL in supplier agreements (e.g., "minimum seventy percent remaining shelf life at receipt"). Enforces FEFO and prevents receiving product too close to expiry. |
| **Related Terms** | FEFO, Lot Traceability, Quarantine Stock, Write-Off |
| **Example Usage** | *"Reject the delivery — remaining shelf life is forty-five days and our MRSL requires ninety days minimum at receipt."* |

---

## Category 10: Product Handling and Manufacturing

---

### Catch Weight

| Attribute | Description |
|-----------|-------------|
| **Term** | Catch Weight |
| **Definition** | A product management approach for items where the unit of sale has variable physical weight — such as meat, cheese, produce, or bulk commodities. The product is ordered by unit (each, case) but priced and costed by actual weight, which is captured at receipt or sale. |
| **Business Context** | Standard in food distribution, protein processing, and commodity trading. Requires weighing at transaction points and maintaining both unit quantity and weight in inventory records. Mismanaging catch weight causes significant margin and inventory valuation errors. |
| **Related Terms** | Unit of Measure, Goods Receipt, Inventory Valuation, Weighted Average Cost |
| **Example Usage** | *"Receive the beef cases by catch weight — scan the case, weigh it, and record both one case and forty-two point three kilograms."* |

---

### Bill of Materials (BOM)

| Attribute | Description |
|-----------|-------------|
| **Term** | Bill of Materials (BOM) |
| **Definition** | A structured list of all components, raw materials, and sub-assemblies required to manufacture a finished product, including quantities per unit of output. The BOM is the recipe that drives material requirements planning and production costing. |
| **Business Context** | Foundational master data in manufacturing. MRP explodes BOMs to calculate component requirements. Errors in BOMs propagate through purchasing, production, and costing. BOM management is a governance process, not a one-time setup. |
| **Related Terms** | Material Requirements Planning, Work-in-Progress, Finished Goods, Raw Materials |
| **Example Usage** | *"The engineering change updated the BOM — we now need four screws instead of three per unit, which changes our component demand."* |

---

### Work-in-Progress (WIP)

| Attribute | Description |
|-----------|-------------|
| **Term** | Work-in-Progress (WIP) |
| **Definition** | Inventory that has entered the production process but is not yet a finished good — partially assembled products, items on the production line, and sub-assemblies awaiting the next manufacturing stage. WIP is an inventory category distinct from raw materials and finished goods. |
| **Business Context** | Tracked in manufacturing environments to value partially completed production, manage shop floor flow, and calculate production lead times. Excessive WIP indicates production bottlenecks; insufficient WIP indicates line starvation. |
| **Related Terms** | Bill of Materials, Raw Materials, Finished Goods, Material Requirements Planning |
| **Example Usage** | *"WIP on the assembly line is valued at $340K — we can't ship those units until final quality inspection and packaging are complete."* |

---

## Category 11: Omnichannel and Retail Distribution

---

### Omnichannel Inventory Pooling

| Attribute | Description |
|-----------|-------------|
| **Term** | Omnichannel Inventory Pooling |
| **Definition** | A strategy where inventory across stores, warehouses, and fulfillment centers is managed as a shared network pool rather than isolated location silos. Any stock in the pool can fulfill demand from any channel — online, in-store, or marketplace. |
| **Business Context** | Enables ship-from-store, buy-online-pick-up-in-store, and endless aisle capabilities. Requires real-time network visibility and intelligent order routing. The defining inventory strategy for modern retail competing on convenience and availability. |
| **Related Terms** | Ship-from-Store, Endless Aisle, Available-to-Promise, Distribution Network |
| **Example Usage** | *"With inventory pooling live, the online order routes to Store 205 for fulfillment because it has ATP and is closest to the customer."* |

---

### Ship-from-Store

| Attribute | Description |
|-----------|-------------|
| **Term** | Ship-from-Store |
| **Definition** | A fulfillment model where retail stores act as mini-fulfillment centers, picking and shipping online orders from store stock to customers. Extends the fulfillment network without building additional warehouse capacity. |
| **Business Context** | Reduces delivery time and shipping cost by fulfilling from the nearest location with stock. Also helps move slow store inventory. Requires store staff training, inventory accuracy at store level, and clear rules on which store stock is available for online orders. |
| **Related Terms** | Omnichannel Inventory Pooling, Endless Aisle, On-Shelf Availability, Pick Pack and Ship |
| **Example Usage** | *"Ship-from-store fulfilled thirty percent of online orders this week — average delivery time dropped from three days to one."* |

---

### Endless Aisle

| Attribute | Description |
|-----------|-------------|
| **Term** | Endless Aisle |
| **Definition** | A retail capability allowing store associates to sell products not physically present in the store by ordering them from the network inventory pool or supplier for direct delivery to the customer. The store's "aisle" extends to the entire network assortment. |
| **Business Context** | Prevents lost sales when a customer wants a size, color, or product the store does not carry. Combines the tactile in-store experience with the assortment breadth of e-commerce. Requires real-time network ATP visibility at the point of sale. |
| **Related Terms** | Omnichannel Inventory Pooling, Available-to-Promise, Ship-from-Store, Drop Shipment |
| **Example Usage** | *"We don't have your size in the store, but endless aisle shows twelve units at the downtown location — I can have it shipped to your home in two days."* |

---

### Initial Allocation

| Attribute | Description |
|-----------|-------------|
| **Term** | Initial Allocation |
| **Definition** | The planned distribution of a new product or seasonal assortment from a central source to individual stores or channels based on forecasted demand, store profile, size curves, and strategic priority — before actual sales data is available. |
| **Business Context** | Critical for new product launches and seasonal transitions in retail. Poor initial allocation creates stockouts at high-potential stores and excess at others. Often uses soft allocation first, converted to hard allocation or transfer orders for execution. |
| **Related Terms** | Soft Allocation, Distribution Requirements Planning, Anticipation Inventory, Stock Rebalancing |
| **Example Usage** | *"Initial allocation for the spring collection goes out next week — flagship stores get the full size curve, smaller stores get a capped assortment."* |

---

### Break Bulk

| Attribute | Description |
|-----------|-------------|
| **Term** | Break Bulk |
| **Definition** | The process of opening master cartons, cases, or pallets and sorting individual units or smaller packs for distribution to stores, customers, or pick locations. Break bulk converts bulk-received goods into fulfillable units. |
| **Business Context** | Standard in distribution centers serving retail stores that cannot receive full-pallet quantities. Break bulk operations add handling cost and time but are necessary when store orders are in eaches or inner packs rather than full cases. |
| **Related Terms** | Cross-Docking, Unit of Measure, Put-Away, Case Pack |
| **Example Usage** | *"Receive the shipment as full pallets but break bulk overnight — stores need individual cases by morning."* |

---

### Stock Keeping Unit Rationalization

| Attribute | Description |
|-----------|-------------|
| **Term** | Stock Keeping Unit Rationalization |
| **Definition** | The deliberate process of reducing product assortment by discontinuing, consolidating, or merging SKUs that add complexity without proportional revenue or margin contribution. Rationalization reduces inventory spread and operational cost. |
| **Business Context** | Periodic exercise in retail, manufacturing, and distribution to combat SKU proliferation. Each active SKU carries carrying cost, count burden, and replenishment overhead. Rationalization frees working capital and simplifies operations. |
| **Related Terms** | FSN Analysis, SLOB, ABC Classification, Product Master Data |
| **Example Usage** | *"This year's SKU rationalization eliminates three hundred low-velocity variants — we expect to free $1.2 million in working capital."* |

---

### Supersession

| Attribute | Description |
|-----------|-------------|
| **Term** | Supersession |
| **Definition** | The planned replacement of an existing product (old SKU) by a new version (new SKU), with defined rules for selling through remaining old stock, redirecting orders, and eventually discontinuing the predecessor. |
| **Business Context** | Standard in technology, automotive parts, and any industry with product model changes. Without supersession rules, customers order obsolete SKUs, old and new stock compete, and excess obsolete inventory accumulates. |
| **Related Terms** | Product Master Data, SLOB, Write-Off, Stock Keeping Unit Rationalization |
| **Example Usage** | *"SKU A-100 is superseded by A-200 — sell through remaining A-100 stock, redirect all new orders to A-200, and write off whatever's left after sixty days."* |

---

## Category 12: Finance and Control

---

### Excess and Obsolete (E&O) Provision

| Attribute | Description |
|-----------|-------------|
| **Term** | Excess and Obsolete (E&O) Provision |
| **Definition** | A financial reserve set aside on the balance sheet to account for the expected loss in value of inventory that is overstocked, slow-moving, or likely to become unsellable. The E&O provision reduces reported inventory asset value to reflect realistic recoverable value. |
| **Business Context** | Required by accounting standards and audited annually. Finance and operations collaborate to assess E&O risk by category. Growing E&O provisions signal assortment, forecasting, or lifecycle management problems. Common line item in earnings reports for retail and manufacturing. |
| **Related Terms** | SLOB, Lower of Cost or Market, Write-Off, Inventory Valuation |
| **Example Usage** | *"We increased the E&O provision by $500K this quarter to cover slow-moving seasonal inventory that didn't sell through."* |

---

### Inventory Reconciliation

| Attribute | Description |
|-----------|-------------|
| **Term** | Inventory Reconciliation |
| **Definition** | The periodic process of comparing operational inventory records (quantities managed by warehouse and inventory teams) with financial inventory records (values managed by accounting) to identify and resolve discrepancies in quantity, value, timing, or classification. |
| **Business Context** | Standard month-end and quarter-end discipline. Differences arise from timing (in-transit), unrecorded adjustments, costing method changes, and ownership transfers. Unreconciled inventory undermines financial statement accuracy and audit confidence. |
| **Related Terms** | Inventory Valuation, Physical Inventory Count, Stock Adjustment, Inventory Accuracy |
| **Example Usage** | *"Month-end inventory reconciliation shows a $45K gap between operations and finance — most of it is in-transit ownership timing, but $8K needs investigation."* |

---

### Blind Count

| Attribute | Description |
|-----------|-------------|
| **Term** | Blind Count |
| **Definition** | A physical inventory counting method where the person performing the count does not see the system's expected quantity before or during the count. The counter records only what they physically find, and variances are calculated afterward by comparing the count to system records. |
| **Business Context** | Standard best practice for cycle counting and full physical counts. Prevents counters from unconsciously or deliberately matching the system quantity. Essential for unbiased accuracy measurement and audit credibility. |
| **Related Terms** | Cycle Count, Physical Inventory Count, Count Variance, Inventory Accuracy |
| **Example Usage** | *"All cycle counts are blind — the counter gets the SKU and location but not the system quantity. Variances are revealed only after submission."* |

---

### Physical Inventory Freeze

| Attribute | Description |
|-----------|-------------|
| **Term** | Physical Inventory Freeze |
| **Definition** | A temporary halt on inventory movements — receiving, shipping, transfers, and adjustments — during a full physical count to ensure the counted quantity is not changed while counting is in progress. Also called an inventory blackout period. |
| **Business Context** | Required for annual full physical counts to produce a reliable snapshot. Duration is minimized to reduce operational disruption. Modern operations with strong cycle counting programs require shorter freezes because accuracy is maintained continuously. |
| **Related Terms** | Physical Inventory Count, Cycle Count, Inventory Accuracy, Blind Count |
| **Example Usage** | *"The inventory freeze starts Friday at 6 PM — no receiving or shipping until the wall-to-wall count is complete Sunday night."* |

---

## Commonly Confused Advanced Term Pairs

| Term A | Term B | Key Difference |
|--------|--------|----------------|
| ATP | CTP | ATP is what can be sold now; CTP includes future supply and capacity by a date |
| Hard Allocation | Soft Allocation | Hard is binding; soft is provisional and can be overridden |
| Days of Supply | Days Inventory Outstanding | DoS is operational (how long stock lasts); DIO is financial (inventory efficiency) |
| Fill Rate | OTIF | Fill rate measures quantity completeness; OTIF adds on-time delivery |
| Fill Rate | On-Shelf Availability | Fill rate is warehouse-centric; OSA measures shelf presence for customers |
| Phantom Inventory | Shrinkage | Phantom is the symptom (system shows stock that isn't there); shrinkage is often the cause |
| Lot Traceability | Serialization | Lot tracks batches; serialization tracks individual units |
| Consignment | VMI | Consignment is about ownership; VMI is about who manages replenishment |
| Cross-Docking | Break Bulk | Cross-dock bypasses storage; break bulk opens bulk into smaller units |
| SLOB | E&O Provision | SLOB describes the inventory condition; E&O is the financial reserve for expected loss |
| Decoupling Stock | Safety Stock | Decoupling insulates supply chain stages; safety stock buffers demand uncertainty |
| MRP | DRP | MRP plans manufacturing components; DRP plans distribution network replenishment |

---

## Document Summary

This advanced glossary defines **60 industry terms** beyond the foundational Business Glossary. Terms span availability and allocation, planning methodologies, financial metrics, warehouse operations, omnichannel fulfillment, traceability, supply arrangements, and financial controls.

Use this glossary alongside:
- Business Glossary (`business domain/business-glossary.md`) — foundational terms
- Core Inventory Management Concepts (`Domain Knowledge/core-inventory-management-concepts.md`)
- Inventory Management Industry Standards (`Domain Knowledge/inventory-management-industry-standards.md`)
- Inventory Management Best Practices (`Domain Knowledge/inventory-management-best-practices.md`)

---

*End of Advanced Inventory Management Glossary*
