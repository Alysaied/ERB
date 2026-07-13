# Industry Standards in Inventory Management

**Document Owner:** Inventory Domain Expert  
**Purpose:** Document operational standards and widely adopted practices that govern how organizations manage inventory  
**Audience:** Business stakeholders, operations leaders, analysts, and inventory control teams  
**Scope:** Operational and business standards only — no software frameworks, ERP platforms, or technical implementation

---

## How to Read This Document

Across distribution, retail, manufacturing, and healthcare, organizations converge on a set of proven standards to manage inventory consistently, measurably, and at scale. Some standards are published by formal bodies (GS1, ISO, ICC). Others are operational conventions so widely adopted they function as industry norms (ABC analysis, cycle counting, FIFO).

Each entry below describes what the standard is, why organizations adopt it, the benefits it delivers, and a practical example. Standards are grouped by the operational area they primarily govern.

---

## Standards Index

| # | Standard | Area | Type |
|---|----------|------|------|
| 1 | ABC Analysis (Pareto Classification) | Classification & Prioritization | Operational convention |
| 2 | Cycle Counting by Classification | Inventory Accuracy | Operational convention |
| 3 | Reorder Point (ROP) Replenishment | Replenishment | Operational convention |
| 4 | Min-Max Replenishment | Replenishment | Operational convention |
| 5 | Economic Order Quantity (EOQ) | Replenishment | Operational convention |
| 6 | Safety Stock & Service Level Targeting | Replenishment | Operational convention |
| 7 | FIFO — First In, First Out | Stock Rotation | Operational convention |
| 8 | FEFO — First Expired, First Out | Stock Rotation | Operational convention |
| 9 | Kanban / Two-Bin Replenishment | Lean Replenishment | Operational convention |
| 10 | GS1 Product Identification Standards | Product Identification | Formal standard (GS1) |
| 11 | Perpetual Inventory Recording | Record Keeping | Operational convention |
| 12 | Segregation of Duties | Internal Controls | Formal standard (COSO / SOX-aligned) |
| 13 | Incoterms | Ownership & Inbound Logistics | Formal standard (ICC) |
| 14 | Cross-Docking | Inbound / Outbound Flow | Operational convention |
| 15 | Fill Rate & Service Level KPIs | Performance Measurement | Operational convention |
| 16 | Inventory Accuracy Benchmarks | Performance Measurement | Industry benchmark |
| 17 | Lot and Batch Traceability | Traceability & Compliance | Regulatory / operational standard |
| 18 | Velocity-Based Slotting | Warehouse Organization | Operational convention |

---

## Category 1: Classification and Prioritization

---

### 1. ABC Analysis (Pareto Classification)

#### Description

ABC analysis classifies inventory items into three groups based on business importance — typically combining sales velocity, revenue contribution, and strategic value. Class A items (roughly 15–20% of SKUs contributing 70–80% of value or volume) receive the highest attention. Class B items are moderate priority. Class C items are low priority. The method is rooted in the Pareto principle (80/20 rule) and is one of the most universal practices in inventory management.

#### Why Organizations Use It

Not all products deserve equal operational effort. Counting, monitoring, replenishment review, and stockout prevention are resource-intensive. ABC analysis directs those resources toward items with the greatest impact on revenue, customer satisfaction, and financial performance.

#### Benefits

- Concentrates management attention on high-impact products
- Sets differentiated count frequencies, safety stock levels, and review cadences
- Reduces stockout risk on priority items without over-investing in slow movers
- Provides a shared prioritization language across purchasing, operations, and finance

#### Example

A medical supplies distributor classifies 8,000 SKUs annually. Two hundred Class A items (surgical gloves, syringes, IV fluids) account for 75% of revenue. These receive weekly cycle counts, daily availability monitoring, and dedicated buyer attention. Four thousand Class C items (specialty accessories) are counted quarterly and managed with higher safety stock tolerance.

---

## Category 2: Inventory Accuracy

---

### 2. Cycle Counting by Classification

#### Description

Cycle counting is the practice of counting a subset of inventory on a rotating schedule rather than shutting down operations for a full physical count. Industry standard practice ties count frequency to ABC classification: Class A items counted weekly or monthly, Class B monthly or quarterly, Class C quarterly or semi-annually. Counts are performed during normal operations without halting receiving or shipping.

#### Why Organizations Use It

Annual full counts alone allow discrepancies to accumulate for months before detection. Cycle counting maintains accuracy continuously, catches errors early, and avoids the operational disruption and cost of full warehouse shutdowns.

#### Benefits

- Sustains inventory accuracy between full physical counts
- Detects root causes (receiving errors, misplacement, theft) while evidence is fresh
- Minimizes operational disruption compared to full-wall-to-wall counts
- Supports audit readiness with documented, ongoing verification

#### Example

A consumer electronics warehouse counts all Class A SKUs every Monday across rotating aisles. Fifteen to twenty SKUs are counted per day by a dedicated count team independent of the pickers who handle those items. Variances above a defined threshold trigger investigation before any adjustment is approved.

---

### 3. Perpetual Inventory Recording

#### Description

Perpetual inventory is the standard practice of updating inventory records in real time (or near real time) with every transaction — receipts, shipments, transfers, adjustments, and returns. Each movement immediately changes the recorded balance. This contrasts with periodic inventory, where balances are updated only at defined intervals (weekly, monthly, or annually).

#### Why Organizations Use It

Business decisions — sales promises, replenishment triggers, financial reporting — depend on current stock information. Delayed or batch-updated records create windows where multiple departments act on outdated quantities, causing overselling, duplicate ordering, and fulfillment failures.

#### Benefits

- Provides current stock position for sales, operations, and purchasing at all times
- Enables automated reorder triggers and ATP calculations
- Creates a transaction history for audit, investigation, and trend analysis
- Reduces reliance on emergency counts to determine actual stock levels

#### Example

A fashion retailer operates perpetual inventory across ninety stores. When a cashier scans a sold item at checkout, the store's on-hand count decreases immediately. The regional replenishment system detects when a popular dress falls below its reorder level the same day and includes it in the next automated store replenishment order.

---

## Category 3: Replenishment and Stock Policy

---

### 4. Reorder Point (ROP) Replenishment

#### Description

The reorder point standard defines the stock level at which a replenishment order must be placed. The universally applied formula accounts for demand during lead time plus safety stock:

**Reorder Point = (Average Daily Demand × Lead Time in Days) + Safety Stock**

When available stock falls to or below the reorder point, replenishment action is triggered automatically or through a defined review process.

#### Why Organizations Use It

Replenishment cannot be reactive to stockouts — by the time stock reaches zero, lead time makes immediate fulfillment impossible. The reorder point standard ensures ordering begins early enough for new supply to arrive before a stockout, based on measurable demand and supplier lead time.

#### Benefits

- Converts replenishment from gut-feel to rule-based discipline
- Accounts for supplier lead time in ordering decisions
- Scales across thousands of SKUs without individual buyer judgment on every item
- Reduces both stockouts and panic over-ordering

#### Example

A hardware store sells an average of 10 bags of concrete mix per day. Supplier lead time is 7 days. Safety stock is set at 30 bags. Reorder Point = (10 × 7) + 30 = 100 bags. When available stock hits 100, the system generates a purchase requisition for the standard order quantity.

---

### 5. Min-Max Replenishment

#### Description

Min-max is a simplified replenishment standard where each product at each location has a minimum level (trigger point) and a maximum level (target after replenishment). When stock falls to the minimum, an order is placed to bring inventory up to the maximum. The order quantity is always **Max − Current Stock**.

#### Why Organizations Use It

Min-max is easier to understand and implement than more complex models. It is widely used in retail store replenishment, distribution centers serving predictable demand, and environments where buyers need clear, consistent rules without advanced forecasting tools.

#### Benefits

- Simple, transparent rules that store managers and buyers can apply consistently
- Prevents both stockouts (minimum trigger) and uncontrolled overstock (maximum cap)
- Well-suited to high-volume, predictable consumables and fast-moving retail items
- Easy to audit — min and max levels are visible policy decisions

#### Example

A supermarket sets min = 24 units and max = 72 units for a popular cereal brand at each store. When shelf and backroom stock combined reach 24 units, the store's replenishment system orders enough to reach 72 — typically 48 units, adjusted for current on-hand quantity.

---

### 6. Economic Order Quantity (EOQ)

#### Description

EOQ is the standard formula for determining the optimal order quantity that minimizes the total cost of ordering and holding inventory. It balances the cost of placing frequent small orders (ordering cost) against the cost of holding large quantities (carrying cost). The classic formula is:

**EOQ = √(2 × Annual Demand × Ordering Cost ÷ Annual Carrying Cost per Unit)**

Organizations use EOQ as a baseline order quantity, often adjusted for supplier minimums, case packs, and practical constraints.

#### Why Organizations Use It

Ordering too frequently wastes purchasing and receiving labor. Ordering too much ties up capital and increases carrying costs, obsolescence risk, and storage expense. EOQ provides a mathematically grounded starting point for order sizing.

#### Benefits

- Reduces total inventory cost by balancing ordering and carrying expenses
- Provides a defensible, repeatable order quantity for each product
- Supports negotiation with suppliers on order frequency and volume
- Serves as a benchmark when evaluating whether current order practices are efficient

#### Example

An industrial parts distributor calculates EOQ for a bearing that sells 12,000 units per year. Ordering cost is $50 per PO; carrying cost is $2 per unit per year. EOQ = √(2 × 12,000 × 50 ÷ 2) = approximately 775 units. The buyer rounds to the supplier's case pack of 800 units and places orders roughly fifteen times per year.

---

### 7. Safety Stock and Service Level Targeting

#### Description

Safety stock is the standard practice of holding buffer inventory above expected demand to protect against uncertainty — demand spikes, forecast errors, and supplier delays. Organizations typically set safety stock based on a target service level (e.g., 95% or 98% probability of not stocking out during lead time). Higher service levels require more safety stock; the relationship is defined through demand variability and lead time variability analysis.

#### Why Organizations Use It

Demand and supply are never perfectly predictable. Without deliberate buffer stock, any deviation from plan — a late shipment, an unexpected bulk order, a promotional surge — causes an immediate stockout. Safety stock is the standard mechanism for converting service level commitments into inventory policy.

#### Benefits

- Translates customer service targets into concrete inventory holdings
- Differentiates buffer levels by product priority (high for Class A, lower for Class C)
- Reduces stockout frequency without requiring perfect forecasting
- Provides a documented rationale for why extra stock is held

#### Example

A pharmaceutical wholesaler targets a 99% service level for life-critical medications (Class A). Based on demand variability and a 14-day supplier lead time, safety stock for one cardiac drug is set at 450 units above expected lead-time demand. For a low-priority supplement (Class C) with a 95% target, safety stock is only 80 units.

---

## Category 4: Stock Rotation and Product Handling

---

### 8. FIFO — First In, First Out

#### Description

FIFO is the standard stock rotation method requiring that the oldest received inventory is picked, sold, or used first. In practice, this means newer stock is placed behind or beneath older stock, and pickers are directed to retrieve from the oldest available lot or location. FIFO is the default rotation standard for non-perishable goods across retail, distribution, and manufacturing.

#### Why Organizations Use It

Inventory that sits too long risks obsolescence, packaging degradation, model-year expiration, and warranty issues. FIFO ensures stock moves through the supply chain in the order it arrived, minimizing age-related loss and ensuring customers receive current product versions.

#### Benefits

- Reduces obsolescence and write-offs from aged stock
- Ensures customers receive fresh, current product
- Simplifies stock rotation with a clear, easy-to-communicate rule
- Supports accurate costing when older (often lower) costs flow through first

#### Example

A paint retailer receives a shipment of 500 cans of white paint in January and another 300 in March. FIFO rules require pickers to draw from the January pallet positions first. Store staff are trained to place new deliveries behind existing stock on the shelf, never in front.

---

### 9. FEFO — First Expired, First Out

#### Description

FEFO is the rotation standard used for products with defined expiry dates — food, pharmaceuticals, cosmetics, and chemicals. Stock with the earliest expiration date is picked and shipped first, regardless of which lot was physically received first. FEFO is a regulatory expectation in many industries and a core operational standard in grocery, pharmacy, and healthcare supply chains.

#### Why Organizations Use It

Expired products cannot be sold, must be written off, and in regulated industries may create legal liability. FEFO minimizes waste by ensuring the shortest remaining shelf life moves out first, protecting both revenue and consumer safety.

#### Benefits

- Minimizes expired product write-offs and waste
- Meets regulatory and food safety compliance requirements
- Protects consumer safety in pharmaceutical and food supply chains
- Reduces financial loss from products that pass their sell-by date in storage

#### Example

A hospital pharmacy stores insulin from three delivery lots with expiration dates of August, October, and December. FEFO picking rules direct nurses and automated dispensing systems to use August-lot vials first, even though the December lot was received most recently. Monthly reports flag products within 60 days of expiry for priority use or return to supplier.

---

## Category 5: Lean and Visual Replenishment

---

### 10. Kanban / Two-Bin Replenishment

#### Description

Kanban (Japanese for "signboard") is a lean replenishment standard using visual signals to trigger restocking. The two-bin variant is the most common form: each item has a primary bin in active use and a secondary bin in reserve. When the primary bin is emptied, it becomes the signal to reorder; the secondary bin supplies operations during replenishment. No complex forecasting is needed — physical consumption triggers the supply action.

#### Why Organizations Use It

For predictable, high-usage consumables (MRO supplies, production components, medical disposables), traditional forecasting adds complexity without proportional benefit. Kanban replaces forecast-driven ordering with consumption-driven signals, reducing administrative overhead and stockouts on routine items.

#### Benefits

- Eliminates forecast dependency for stable, repetitive demand items
- Creates an unmistakable visual trigger that any worker can act on
- Reduces overstock by sizing bins to cover only lead-time demand
- Lowers purchasing administration — orders are triggered by actual use, not schedules

#### Example

A manufacturing plant uses two-bin Kanban for machine lubricant. Each bin holds two days of usage. When the shop floor worker opens the second bin, they place the empty first bin on a designated reorder rack. The material handler collects empty bins daily and places a replenishment order. The second bin sustains production until the new delivery arrives.

---

## Category 6: Product Identification and Traceability

---

### 11. GS1 Product Identification Standards

#### Description

GS1 is the global standards body that defines how products, locations, and logistics units are identified and barcoded. Key standards include GTIN (Global Trade Item Number) for product identification, GLN (Global Location Number) for facility identification, and SSCC (Serial Shipping Container Code) for logistics units. GS1 barcodes (EAN-13, UPC-A, GS1-128) are the universal language of product scanning across retail, healthcare, and logistics worldwide.

#### Why Organizations Use It

Without a common identification standard, every trading partner uses different product codes, barcodes, and labeling conventions. GS1 provides a single, interoperable system so manufacturers, distributors, retailers, and regulators can scan, track, and exchange product data consistently across the supply chain.

#### Benefits

- Enables accurate scanning at receiving, picking, point-of-sale, and shipping
- Eliminates manual data entry and the errors that accompany it
- Supports end-to-end traceability from manufacturer to consumer
- Required for doing business with major retailers, healthcare systems, and government buyers

#### Example

A food manufacturer assigns a GTIN-13 barcode to each product variant. The distributor scans barcodes during goods receipt to verify PO line items automatically. Retail stores scan the same barcode at checkout to deduct sold quantity from inventory. During a product recall, the GTIN enables rapid identification of affected lots across every location in the supply chain.

---

### 12. Lot and Batch Traceability

#### Description

Lot and batch traceability is the operational standard of recording which production or receipt batch each inventory unit belongs to, and tracking that batch through every movement — receipt, storage, transfer, pick, ship, and return. In regulated industries (pharmaceuticals, food, aerospace, chemicals), traceability is a legal requirement. In all industries, it is the standard practice for managing recalls, quality investigations, and warranty claims.

#### Why Organizations Use It

When a defect is discovered, the business must identify every unit from the affected batch and every customer who received it — quickly and completely. Without lot traceability, the only safe option is a full product-line recall, which is vastly more expensive and damaging than a targeted batch recall.

#### Benefits

- Enables targeted recalls instead of blanket product withdrawals
- Supports quality investigations by linking defects to specific production runs
- Meets regulatory compliance in pharmaceuticals (GMP), food (HACCP), and medical devices
- Reduces liability exposure by demonstrating controlled traceability

#### Example

A dairy processor assigns lot number 2026-0412 to a production run of yogurt. Each case label carries the lot number. When a quality test reveals contamination in that lot, the company queries its inventory system, identifies 3,200 cases still in warehouses and 1,800 already shipped to forty-three stores, and initiates a targeted recall within four hours — without affecting other production lots of the same product.

---

## Category 7: Internal Controls and Trade Standards

---

### 13. Segregation of Duties

#### Description

Segregation of duties is the internal control standard requiring that no single individual can complete an inventory transaction from initiation through approval without independent review. Standard applications in inventory include: the person who counts stock should not approve the adjustment; the person who requests a write-off should not authorize it; the person who receives goods should not also approve supplier payments for those goods.

#### Why Organizations Use It

Inventory is a high-value, movable asset — creating inherent fraud and error risk. Segregation of duties is the primary control recommended by the COSO framework and required under Sarbanes-Oxley (SOX) for publicly traded companies. Auditors specifically test this control during inventory audits.

#### Benefits

- Reduces fraud risk by requiring collusion for manipulation
- Catches honest errors through independent verification
- Satisfies audit and regulatory compliance requirements
- Builds organizational trust in inventory data integrity

#### Example

A warehouse cycle counter finds a 20-unit variance on a high-value electronic component. The counter submits the variance report with photographic evidence. A warehouse supervisor (who did not perform the count) reviews the evidence and investigates. An inventory control manager (who did not count or supervise the count) approves the adjustment. Three distinct roles, each documented in the audit trail.

---

### 14. Incoterms (International Commercial Terms)

#### Description

Incoterms are standardized trade terms published by the International Chamber of Commerce (ICC) that define when ownership, risk, and cost transfer between buyer and seller during international shipments. Terms such as EXW (Ex Works), FOB (Free on Board), CIF (Cost, Insurance, and Freight), and DDP (Delivered Duty Paid) determine at which point in the shipping journey inventory becomes the buyer's asset and who bears transit risk.

#### Why Organizations Use It

International shipments cross multiple legal jurisdictions, carriers, and customs boundaries. Without agreed Incoterms, disputes arise over who owns goods in transit, who pays freight and insurance, and when inventory should appear on the buyer's books. Incoterms provide a globally recognized vocabulary for these responsibilities.

#### Benefits

- Clarifies the exact point when inventory ownership transfers to the buyer
- Defines who bears risk of loss or damage during transit
- Standardizes commercial negotiations across international trading partners
- Determines when inbound stock should be recorded in the buyer's inventory

#### Example

A European retailer purchases goods from an Asian supplier under FOB Shanghai terms. The supplier delivers goods to the port and loads them onto the vessel. From that moment, risk transfers to the retailer. The retailer records the goods as inbound inventory when the vessel departs, even though physical receipt at the European warehouse occurs three weeks later.

---

## Category 8: Warehouse and Logistics Flow

---

### 15. Cross-Docking

#### Description

Cross-docking is the operational standard of transferring inbound goods directly from receiving to outbound shipping with minimal or no storage time. Products are sorted at the dock by destination and loaded onto outbound trucks, bypassing put-away and long-term storage. Cross-docking is standard practice for high-velocity, predictable-flow distribution — especially retail store replenishment and perishable goods.

#### Why Organizations Use It

Traditional receive-store-pick-ship flow adds handling time, storage cost, and delay. For products with known downstream demand, cross-docking eliminates the storage step entirely, reducing lead time from supplier to store and lowering warehouse labor and space requirements.

#### Benefits

- Reduces lead time from supplier to customer or store
- Lowers warehouse storage and handling costs
- Minimizes inventory holding for fast-moving, predictable products
- Improves freshness for perishable and time-sensitive goods

#### Example

A grocery distribution center receives palletized shipments of bottled water from three suppliers overnight. By 6 AM, receiving teams break down pallets and sort cases directly onto outbound route trucks labeled for each of forty stores. No cases enter long-term storage. Store delivery trucks depart by 8 AM — the same day the supplier goods arrived.

---

### 16. Velocity-Based Slotting

#### Description

Velocity-based slotting is the warehouse organization standard of positioning products based on how frequently they are picked. Fast-moving items (high velocity) are placed in the most accessible locations — near packing stations, at ergonomic height, in forward pick areas. Slow-moving items are stored in remote or upper rack positions. Slotting is reviewed and rebalanced periodically as demand patterns change.

#### Why Organizations Use It

Picker travel time is the largest labor cost in warehouse fulfillment. Placing the most-picked items closest to shipping points minimizes walking distance, increases picks per hour, and reduces order fulfillment time. Random or static slotting without velocity consideration wastes labor on every order.

#### Benefits

- Reduces order picking time and labor cost
- Increases warehouse throughput without adding staff
- Improves order fulfillment speed for high-demand products
- Optimizes use of prime warehouse real estate (forward pick zones)

#### Example

A fulfillment center analyzes twelve weeks of pick data and identifies its top 200 SKUs (5% of products accounting for 60% of picks). These are moved to a forward pick zone within thirty feet of the packing stations. Medium-velocity items occupy standard rack positions. Slow movers are relocated to upper rack levels at the rear of the warehouse. Average pick time per order drops by 22%.

---

## Category 9: Performance Measurement

---

### 17. Fill Rate and Service Level KPIs

#### Description

Fill rate is the standard KPI measuring the percentage of customer demand fulfilled completely from available stock on the first attempt, without backorder or cancellation. Industry benchmarks vary by sector: retail distribution typically targets 95–98% line fill rate; healthcare and industrial MRO often target 98–99.5% for critical items. Service level agreements (SLAs) between supply chain functions and commercial teams formalize these targets.

#### Why Organizations Use It

Inventory management exists to serve customer demand. Fill rate connects inventory decisions directly to commercial outcomes — lost sales, customer complaints, and competitive positioning. Without a standard KPI, organizations cannot assess whether their inventory investment is actually delivering the availability customers expect.

#### Benefits

- Links inventory performance to revenue and customer satisfaction
- Enables target-setting by product class (higher for A items, lower tolerance for C items)
- Drives root-cause analysis when fill rate drops (supplier, forecast, policy, or execution failure)
- Provides a common metric for operations, sales, and leadership

#### Example

A building materials distributor commits to a 97% fill rate for its top 500 products (Class A). Monthly reporting shows fill rate dropped to 93% in the southwest region. Investigation reveals a supplier consolidation that increased lead time from 5 to 12 days without updating reorder points. Reorder points are recalibrated, and fill rate recovers to 96.5% within six weeks.

---

### 18. Inventory Accuracy Benchmarks

#### Description

Inventory accuracy is measured as the percentage of SKUs or items counted where the physical quantity matches the recorded quantity within an acceptable tolerance (e.g., ±1 unit or ±2%). Industry benchmarks established by ASCM (Association for Supply Chain Management) and observed across sectors set expectations: best-in-class operations achieve 99%+ accuracy for Class A items and 97%+ overall. Accuracy below 95% is widely considered a sign of systemic control failure.

#### Why Organizations Use It

Accuracy benchmarks provide an objective standard for whether inventory records can be trusted. Operations, finance, and auditors all depend on a shared definition of "accurate enough." Benchmarks create accountability and a target for continuous improvement programs.

#### Benefits

- Establishes an objective standard for data trustworthiness
- Supports audit substantiation of balance sheet inventory values
- Identifies locations, product categories, or processes with systemic accuracy problems
- Drives investment in counting discipline, process improvement, and training

#### Example

A national retailer targets 98% unit-level accuracy across all stores, measured through monthly cycle counts. Stores below 95% are flagged for intensive count programs and process review. One store consistently scores 91% on apparel — investigation reveals inconsistent receiving practices during high-volume promotional deliveries. Standardized receiving checklists are introduced, and accuracy rises to 97% within two months.

---

## Standards by Operational Area — Quick Reference

| Operational Area | Standards to Apply |
|------------------|-------------------|
| Product prioritization | ABC Analysis |
| Replenishment triggers | Reorder Point, Min-Max, EOQ, Safety Stock |
| Lean / high-frequency items | Kanban / Two-Bin |
| Stock rotation | FIFO (general), FEFO (perishables) |
| Inventory accuracy | Cycle Counting, Perpetual Recording, Accuracy Benchmarks |
| Product identification | GS1 Standards |
| Traceability & recalls | Lot and Batch Traceability |
| Internal controls | Segregation of Duties |
| International trade | Incoterms |
| Warehouse efficiency | Velocity-Based Slotting, Cross-Docking |
| Performance management | Fill Rate KPIs, Inventory Accuracy Benchmarks |

---

## How Standards Work Together

Operational standards are not applied in isolation. A typical distribution organization combines them into a coherent operating model:

1. **Classify** products using ABC analysis
2. **Identify** products with GS1 barcodes and assign lot numbers where required
3. **Set policy** using reorder points, safety stock, and EOQ-based order quantities
4. **Record** all movements through perpetual inventory
5. **Rotate** stock using FIFO or FEFO
6. **Count** using ABC-based cycle counting frequencies
7. **Control** through segregation of duties and documented adjustments
8. **Organize** the warehouse with velocity-based slotting
9. **Measure** fill rate and inventory accuracy against industry benchmarks
10. **Improve** by investigating failures and recalibrating policy

---

## Related Documents

- Core Inventory Management Concepts (`Domain Knowledge/core-inventory-management-concepts.md`)
- Business Glossary (`business domain/business-glossary.md`)
- Business Process Analysis (`business domain/business-processes.md`)

---

*End of Inventory Management Industry Standards Document*
