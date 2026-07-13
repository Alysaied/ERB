# Business Glossary: Inventory Management System

**Document Owner:** Domain Expert  
**Purpose:** Define the standard business vocabulary used across inventory management operations, processes, and stakeholder communications  
**Scope:** Business terminology only — no technical, system, or implementation language  
**Based On:** Business Process Analysis, Business Actor Analysis, Business Workflows, and Business Vision

---

## How to Use This Glossary

This glossary establishes a shared language for everyone involved in inventory management — from warehouse floor staff to executive leadership. Terms are grouped by subject area for easy reference. Each entry explains what the term means in plain business language, why it matters to the organization, how it relates to other concepts, and where people commonly get it wrong.

**Audience:** Operations, warehouse, purchasing, sales, customer service, finance, marketing, and leadership teams.

---

## Glossary Index

| # | Term | Category |
|---|------|----------|
| 1 | Inventory | Core Concepts |
| 2 | Stock / On-Hand Stock | Core Concepts |
| 3 | Available-to-Promise (ATP) | Stock Status |
| 4 | Reserved Stock | Stock Status |
| 5 | Committed Stock | Stock Status |
| 6 | Inbound Stock (Expected Stock) | Stock Status |
| 7 | Stockout | Stock Status |
| 8 | Low Stock | Stock Status |
| 9 | Overstock | Stock Status |
| 10 | SKU (Stock Keeping Unit) | Master Data |
| 11 | Product Master Data | Master Data |
| 12 | Unit of Measure | Master Data |
| 13 | ABC Classification | Master Data |
| 14 | Inventory Location | Locations |
| 15 | Warehouse | Locations |
| 16 | Distribution Network | Locations |
| 17 | Reorder Level | Stock Policy |
| 18 | Minimum Stock Threshold | Stock Policy |
| 19 | Safety Stock | Stock Policy |
| 20 | Lead Time | Procurement |
| 21 | Purchase Order (PO) | Procurement |
| 22 | Purchase Requisition | Procurement |
| 23 | Supplier / Vendor | Procurement |
| 24 | Goods Receipt | Inbound |
| 25 | Receipt Discrepancy | Inbound |
| 26 | Put-Away | Inbound |
| 27 | Replenishment | Replenishment |
| 28 | Backorder | Fulfillment |
| 29 | Order Reservation | Fulfillment |
| 30 | Pick, Pack, and Ship | Fulfillment |
| 31 | Partial Fulfillment | Fulfillment |
| 32 | Fill Rate | Performance |
| 33 | Inter-Location Transfer | Network Balance |
| 34 | Stock Rebalancing | Network Balance |
| 35 | Cycle Count | Inventory Control |
| 36 | Physical Inventory Count | Inventory Control |
| 37 | Count Variance | Inventory Control |
| 38 | Stock Adjustment | Inventory Control |
| 39 | Write-Off | Inventory Control |
| 40 | Shrinkage | Inventory Control |
| 41 | Reason Code | Inventory Control |
| 42 | Inventory Accuracy | Performance |
| 43 | Inventory Valuation | Finance |
| 44 | Carrying Cost | Finance |
| 45 | Inventory Turnover | Finance |
| 46 | Customer Return | Returns |
| 47 | Return Authorization | Returns |
| 48 | Restock (Return-to-Stock) | Returns |
| 49 | Audit Trail | Governance |
| 50 | Segregation of Duties | Governance |

---

## Category 1: Core Inventory Concepts

---

### Inventory

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Inventory |
| **Definition** | The total goods and products that a business owns and holds for the purpose of sale, distribution, or operational use. Inventory includes items in warehouses, stores, and in transit between locations, valued as a business asset on the balance sheet. |
| **Why It Is Important** | Inventory is one of the largest assets for distribution and retail businesses. How well it is managed directly affects revenue, customer satisfaction, cash flow, and profitability. Poor inventory management leads to lost sales, trapped capital, and operational chaos. |
| **Related Business Terms** | Stock, On-Hand Stock, Inventory Valuation, Carrying Cost, Inventory Turnover, Shrinkage |
| **Common Misunderstandings** | People often equate inventory only with warehouse stock, ignoring store holdings and goods in transit. Inventory is not merely "what is on the shelf" — it is everything the business owns and intends to sell or use. |

---

### Stock / On-Hand Stock

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Stock / On-Hand Stock |
| **Definition** | The quantity of a specific product physically present at a given location at a point in time. On-hand stock is the starting point for understanding what the business actually has available before considering reservations, commitments, or inbound deliveries. |
| **Why It Is Important** | On-hand stock is the foundation of every inventory decision — fulfillment, replenishment, transfer, and financial reporting all depend on knowing what is physically present. Discrepancies between recorded and physical stock undermine trust in all other inventory information. |
| **Related Business Terms** | Inventory, Available-to-Promise, Reserved Stock, Cycle Count, Inventory Accuracy |
| **Common Misunderstandings** | On-hand stock is often confused with available stock. A product may show on-hand quantity but not be available for sale because portions are reserved for existing orders or damaged and unsellable. |

---

## Category 2: Stock Status & Availability

---

### Available-to-Promise (ATP)

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Available-to-Promise (ATP) |
| **Definition** | The quantity of a product that the business can confidently offer to customers right now — calculated as on-hand stock minus stock already reserved or committed to existing orders. ATP represents what can still be sold or promised without affecting current commitments. |
| **Why It Is Important** | Sales teams, customer service, and commercial planning rely on ATP to make delivery promises customers can trust. Quoting or selling against total on-hand stock without subtracting reservations leads to overselling, order cancellations, and damaged customer relationships. |
| **Related Business Terms** | On-Hand Stock, Reserved Stock, Committed Stock, Order Reservation, Stockout |
| **Common Misunderstandings** | ATP is not the same as physical stock on the shelf. Sales staff sometimes quote on-hand quantities and discover the order cannot be fulfilled because stock was already promised to another customer. ATP is the number that matters for new commitments. |

---

### Reserved Stock

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Reserved Stock |
| **Definition** | Inventory quantity that has been set aside and committed to a specific customer order, transfer, or internal purpose. Reserved stock is no longer available for other orders even though it remains physically in the warehouse until picked and shipped. |
| **Why It Is Important** | Reservations prevent the same stock from being sold twice. Without a clear reservation discipline, multiple orders compete for the same physical items, causing pick failures, partial shipments, and customer disputes. |
| **Related Business Terms** | Available-to-Promise, Order Reservation, Committed Stock, Pick Pack and Ship |
| **Common Misunderstandings** | Reserved stock is sometimes thought to have already left the building. Physically, reserved items are still on the shelf — they are simply spoken for. Only when goods are picked and shipped does on-hand stock decrease. |

---

### Committed Stock

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Committed Stock |
| **Definition** | Stock that the business has obligated to fulfill through confirmed orders, approved transfers, or other formal commitments. Committed stock overlaps with reserved stock and represents inventory the business cannot reallocate without breaking a promise. |
| **Why It Is Important** | Understanding committed stock helps operations and sales see the true picture of what remains free for new business. It supports honest availability communication and prevents overcommitment during high-demand periods. |
| **Related Business Terms** | Reserved Stock, Available-to-Promise, Backorder, Order Reservation |
| **Common Misunderstandings** | Committed stock is often used interchangeably with reserved stock. While closely related, commitment is the business obligation (the promise made), while reservation is the operational act of holding stock against that obligation. |

---

### Inbound Stock (Expected Stock)

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Inbound Stock (Expected Stock) |
| **Definition** | Inventory that has been ordered from suppliers but has not yet been received and verified at a location. Inbound stock represents a future supply that the business expects to arrive within a known or estimated timeframe. |
| **Why It Is Important** | Knowing what is inbound helps purchasing avoid duplicate orders, allows sales to quote realistic future delivery dates, and gives operations visibility into when stockouts will be resolved. Ignoring inbound stock leads to over-ordering; over-relying on it leads to broken delivery promises when shipments are delayed. |
| **Related Business Terms** | Purchase Order, Lead Time, Goods Receipt, Replenishment, Backorder |
| **Common Misunderstandings** | Inbound stock is sometimes treated as if it were already available to sell. Until goods are physically received and verified, inbound stock carries risk — suppliers may short-ship, delay, or send damaged goods. |

---

### Stockout

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Stockout |
| **Definition** | A condition where a product has zero available quantity at a location and cannot be fulfilled for new customer orders without replenishment, transfer, or backorder arrangement. A stockout means the business cannot immediately meet demand for that product. |
| **Why It Is Important** | Stockouts directly cause lost sales, customer dissatisfaction, and competitive disadvantage. Chronic stockouts on priority products signal failures in replenishment planning, demand forecasting, or network balancing. Each stockout is both a revenue event and a customer trust event. |
| **Related Business Terms** | Low Stock, Backorder, Replenishment, Fill Rate, ABC Classification |
| **Common Misunderstandings** | A stockout at one location does not always mean the product is unavailable company-wide. Another warehouse or store may have stock, but failure to transfer or visibility gaps makes the product effectively unavailable to the customer. |

---

### Low Stock

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Low Stock |
| **Definition** | A condition where a product's available quantity has fallen below the defined reorder level or minimum threshold, signaling that replenishment action should be initiated before a stockout occurs. Low stock is a warning state, not yet a failure. |
| **Why It Is Important** | Low-stock conditions are the business early-warning system. Responding while stock is low — rather than after it reaches zero — prevents stockouts, reduces emergency purchasing costs, and maintains customer service levels. Ignoring low-stock signals converts manageable situations into crises. |
| **Related Business Terms** | Reorder Level, Minimum Stock Threshold, Replenishment, Stockout, Safety Stock |
| **Common Misunderstandings** | Low stock is sometimes dismissed because "we still have some left." The reorder level is set specifically to allow time for supplier lead time — waiting until stock is nearly gone guarantees a stockout during replenishment. |

---

### Overstock

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Overstock |
| **Definition** | A condition where a location holds more of a product than is justified by current or expected demand, tying up capital, consuming storage space, and increasing the risk of obsolescence, damage, or write-off. |
| **Why It Is Important** | Overstock traps working capital that could be invested elsewhere, increases carrying costs, and often masks underlying problems such as over-purchasing, demand decline, or poor network balancing. Reducing overstock improves cash flow and warehouse efficiency. |
| **Related Business Terms** | Carrying Cost, Stock Rebalancing, Inventory Turnover, Write-Off, Replenishment |
| **Common Misunderstandings** | Overstock is sometimes viewed as "better than a stockout." Excess inventory is not free insurance — it has real financial cost and may eventually become obsolete. Balance is the goal, not maximum stock. |

---

## Category 3: Master Data & Classification

---

### SKU (Stock Keeping Unit)

| Attribute | Description |
|-----------|-------------|
| **Business Term** | SKU (Stock Keeping Unit) |
| **Definition** | A unique identifier assigned to each distinct product the business tracks in inventory. The SKU distinguishes one product from all others and is used consistently across purchasing, receiving, storage, fulfillment, and reporting. |
| **Why It Is Important** | A single, unambiguous product identity is the foundation of inventory accuracy. Duplicate or inconsistent SKUs cause the same product to be tracked under multiple codes, fragmenting stock visibility and causing fulfillment and replenishment errors. |
| **Related Business Terms** | Product Master Data, Unit of Measure, ABC Classification, On-Hand Stock |
| **Common Misunderstandings** | SKU is often confused with barcode, supplier part number, or product name. A product may have multiple barcodes or supplier references, but the business should maintain one authoritative SKU per distinct sellable product. |

---

### Product Master Data

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Product Master Data |
| **Definition** | The official record of each product the business tracks, including its SKU, name, description, category, unit of measure, status (active, inactive, discontinued), and attributes needed for inventory management such as reorder parameters. |
| **Why It Is Important** | Every inventory transaction — receiving, counting, reserving, shipping — depends on accurate product master data. Errors in product records propagate through the entire operation, causing wrong items shipped, incorrect counts, and unreliable replenishment. |
| **Related Business Terms** | SKU, Unit of Measure, ABC Classification, Reorder Level, Product Master Data Management |
| **Common Misunderstandings** | Product master data is sometimes treated as a one-time setup task. Products change — descriptions are updated, items are discontinued, units of measure are corrected — and without ongoing maintenance, data quality degrades and operations lose trust. |

---

### Unit of Measure

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Unit of Measure |
| **Definition** | The standard unit in which a product is counted, ordered, stored, and sold — such as each (piece), case, pallet, kilogram, or liter. The unit of measure defines what "one" of the product means for all inventory transactions. |
| **Why It Is Important** | Mismatched units of measure between purchasing (cases), storage (pallets), and sales (individual pieces) cause quantity errors that are among the most common and costly inventory mistakes. Consistent units ensure that ordering 10 cases does not accidentally become 10 individual pieces. |
| **Related Business Terms** | SKU, Product Master Data, Goods Receipt, Purchase Order |
| **Common Misunderstandings** | People assume everyone knows the unit without checking. A supplier may ship in cases while the warehouse counts in pieces — if the unit is not explicit, a receipt of "10" could mean 10 cases or 10 pieces, a tenfold error. |

---

### ABC Classification

| Attribute | Description |
|-----------|-------------|
| **Business Term** | ABC Classification |
| **Definition** | A method of grouping products by business importance, typically into three classes: A (high-value, high-velocity, or strategically critical), B (moderate importance), and C (low priority). Classification directs operational focus, count frequency, and replenishment priority. |
| **Why It Is Important** | Not all products deserve equal attention. ABC classification ensures that counting effort, stockout prevention, and management review concentrate on products that have the greatest impact on revenue, customer satisfaction, and operational cost. |
| **Related Business Terms** | SKU, Cycle Count, Reorder Level, Stockout, Inventory Accuracy |
| **Common Misunderstandings** | ABC is sometimes treated as a permanent label. Product importance changes with sales trends, seasonality, and assortment changes — classification should be reviewed regularly, not set once and forgotten. |

---

## Category 4: Locations & Network

---

### Inventory Location

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Inventory Location |
| **Definition** | Any physical place where the business holds and tracks stock — including warehouses, retail stores, distribution centers, and designated storage areas. Each location is a distinct point where on-hand quantities are recorded and managed. |
| **Why It Is Important** | Multi-location businesses must know not just what they have, but where they have it. Location-level visibility enables fulfillment from the nearest source, transfer between sites, and accountability for accuracy at each site. |
| **Related Business Terms** | Warehouse, Distribution Network, Inter-Location Transfer, On-Hand Stock, Stock Rebalancing |
| **Common Misunderstandings** | A location is sometimes assumed to mean only a warehouse. Stores that hold sellable stock are inventory locations too, and ignoring them creates blind spots in network-wide visibility. |

---

### Warehouse

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Warehouse |
| **Definition** | A dedicated facility where the business receives, stores, and dispatches inventory. Warehouses support inbound receiving, storage, order picking, packing, and outbound shipping, and are typically managed by warehouse operations teams. |
| **Why It Is Important** | Warehouses are the operational hub of inventory movement. Their efficiency, accuracy, and capacity directly determine fulfillment speed, receiving throughput, and the cost of handling goods. Poor warehouse discipline affects every downstream customer experience. |
| **Related Business Terms** | Inventory Location, Goods Receipt, Put-Away, Pick Pack and Ship, Cycle Count |
| **Common Misunderstandings** | Warehouse is often used interchangeably with "all storage." A warehouse is a specific type of location with defined operational processes — not every place stock is kept operates with the same receiving, picking, and counting discipline. |

---

### Distribution Network

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Distribution Network |
| **Definition** | The complete set of inventory-holding locations and the relationships between them — how stock flows from suppliers into warehouses and stores, and how it moves between locations to meet customer demand. The network is the organizational structure of where inventory lives and moves. |
| **Why It Is Important** | Managing inventory at a single location is straightforward; managing it across a network requires balancing stock levels, coordinating transfers, and ensuring visibility everywhere. Network thinking prevents local optimization (one site overstocked while another stockouts) from harming overall performance. |
| **Related Business Terms** | Inventory Location, Inter-Location Transfer, Stock Rebalancing, Stockout, Overstock |
| **Common Misunderstandings** | The network is sometimes managed as independent locations without coordination. A stockout at Store A may be solvable with a transfer from Warehouse B — but only if the business views inventory as a network asset, not isolated silos. |

---

## Category 5: Stock Policy & Replenishment

---

### Reorder Level

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Reorder Level |
| **Definition** | The stock quantity at which the business should initiate a replenishment action — placing a purchase order or requesting a transfer — to ensure new stock arrives before the current supply runs out. The reorder level accounts for supplier lead time and expected demand during that period. |
| **Why It Is Important** | The reorder level is the trigger that connects inventory monitoring to purchasing action. Set too high, it causes overstock; set too low, it guarantees stockouts during replenishment lead time. Correct reorder levels are essential for maintaining availability without excess capital investment. |
| **Related Business Terms** | Minimum Stock Threshold, Safety Stock, Lead Time, Low Stock, Replenishment |
| **Common Misunderstandings** | The reorder level is often confused with minimum display quantity or "how much we want on the shelf." It is specifically the point at which action must start, considering how long replenishment takes — not the target stock level after replenishment. |

---

### Minimum Stock Threshold

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Minimum Stock Threshold |
| **Definition** | The lowest acceptable stock level for a product at a location before the business considers the situation critical. Falling below this threshold triggers urgent review and may generate priority alerts distinct from standard reorder notifications. |
| **Why It Is Important** | While the reorder level initiates routine replenishment, the minimum threshold signals that stock is critically low and may require emergency action — expedited orders, inter-location transfers, or sales communication to manage customer expectations. |
| **Related Business Terms** | Reorder Level, Low Stock, Safety Stock, Stockout, ABC Classification |
| **Common Misunderstandings** | Minimum threshold and reorder level are often treated as the same number. They serve different purposes — reorder level starts the replenishment clock; minimum threshold warns that time may have run out. |

---

### Safety Stock

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Safety Stock |
| **Definition** | Extra inventory held deliberately above expected demand to protect against uncertainty — such as supplier delays, demand spikes, or forecast errors. Safety stock is a buffer that reduces stockout risk at the cost of additional carrying investment. |
| **Why It Is Important** | Without safety stock, any deviation from plan — a late shipment, an unexpected order surge — immediately causes a stockout. The right amount of safety stock balances service level against carrying cost, especially for priority products with unreliable supply or volatile demand. |
| **Related Business Terms** | Reorder Level, Lead Time, Stockout, Carrying Cost, ABC Classification |
| **Common Misunderstandings** | Safety stock is sometimes viewed as waste or inefficiency. It is a deliberate business investment in reliability — the question is not whether to hold buffer stock, but how much is justified for each product. |

---

### Lead Time

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Lead Time |
| **Definition** | The elapsed time between placing a replenishment order and receiving the goods at the location. Lead time includes supplier processing, manufacturing (if applicable), transit, and receiving verification — and determines how early the business must reorder. |
| **Why It Is Important** | Lead time is the critical variable in replenishment planning. If lead time is 14 days and the reorder level only covers 7 days of demand, stockouts are inevitable. Accurate lead time understanding prevents both stockouts and panic over-ordering. |
| **Related Business Terms** | Reorder Level, Purchase Order, Inbound Stock, Replenishment, Supplier |
| **Common Misunderstandings** | Lead time is often quoted as the supplier's stated delivery time without including receiving and put-away at the warehouse. True operational lead time extends until stock is available for sale or fulfillment, not just until the truck arrives. |

---

### Replenishment

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Replenishment |
| **Definition** | The end-to-end business activity of restoring inventory to appropriate levels — including detecting low stock, planning order quantities, placing purchase orders or initiating transfers, tracking inbound supply, and receiving goods. Replenishment ensures continuity of supply. |
| **Why It Is Important** | Replenishment is the lifeblood of inventory availability. Reactive, gut-feel replenishment leads to stockouts on popular items and overstock on slow movers. Disciplined replenishment aligned with demand, lead times, and policy protects revenue and working capital. |
| **Related Business Terms** | Reorder Level, Purchase Order, Purchase Requisition, Low Stock, Inbound Stock |
| **Common Misunderstandings** | Replenishment is sometimes equated only with "ordering more." It includes validating the need, choosing the right quantity and source (purchase vs. transfer), tracking delivery, and confirming receipt — a full cycle, not just placing an order. |

---

## Category 6: Procurement & Inbound

---

### Purchase Order (PO)

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Purchase Order (PO) |
| **Definition** | A formal commercial document issued by the buyer to a supplier specifying the products, quantities, agreed prices, delivery terms, and expected delivery date. The purchase order represents a binding commitment to purchase and the supplier's obligation to deliver. |
| **Why It Is Important** | The purchase order is the authoritative record of what was ordered, enabling receiving verification, supplier accountability, financial commitment tracking, and inbound supply visibility. Without PO discipline, receiving cannot verify shipments and finance cannot control spending. |
| **Related Business Terms** | Purchase Requisition, Supplier, Goods Receipt, Inbound Stock, Receipt Discrepancy |
| **Common Misunderstandings** | A purchase order is not the same as a purchase requisition (internal request) or a delivery note (supplier's shipment document). Each document serves a different purpose in the procurement cycle. |

---

### Purchase Requisition

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Purchase Requisition |
| **Definition** | An internal request to purchase specific products in defined quantities, submitted for review and approval before a formal purchase order is issued to the supplier. The requisition documents the business need and proposed order details. |
| **Why It Is Important** | Requisitions create an approval checkpoint between detecting a replenishment need and committing company funds. They ensure purchasing decisions are reviewed, budget-aligned, and documented before supplier orders are placed. |
| **Related Business Terms** | Purchase Order, Replenishment, Low Stock, Reorder Level |
| **Common Misunderstandings** | A requisition is sometimes treated as an order. Until approved and converted into a purchase order sent to the supplier, no external commitment exists and no goods are expected. |

---

### Supplier / Vendor

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Supplier / Vendor |
| **Definition** | An external business partner that provides products to the organization under agreed commercial terms — including pricing, lead times, minimum order quantities, delivery standards, and payment terms. Suppliers are the source of inbound inventory. |
| **Why It Is Important** | Supplier reliability directly affects stock availability. Lead time consistency, delivery accuracy, and product quality from suppliers determine how much safety stock is needed and how often receipt discrepancies occur. Supplier performance is an inventory management variable, not just a purchasing concern. |
| **Related Business Terms** | Purchase Order, Lead Time, Goods Receipt, Receipt Discrepancy, Inbound Stock |
| **Common Misunderstandings** | All suppliers are sometimes treated as interchangeable. Different suppliers have different lead times, reliability, and terms — replenishment planning must account for supplier-specific behavior, not generic averages. |

---

### Goods Receipt

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Goods Receipt |
| **Definition** | The business act of accepting inbound delivery, verifying that received products match the purchase order and delivery documentation in quantity and condition, and formally recording the accepted stock into inventory at the receiving location. |
| **Why It Is Important** | Goods receipt is the moment inventory officially increases. Until receipt is verified and recorded, ordered stock does not exist for fulfillment or sales purposes. Accurate and timely receiving is essential for inventory record integrity and supplier accountability. |
| **Related Business Terms** | Purchase Order, Receipt Discrepancy, Put-Away, On-Hand Stock, Inbound Stock |
| **Common Misunderstandings** | Goods receipt is sometimes confused with the physical arrival of a truck. Arrival is not receipt — verification, acceptance, and recording must occur before stock is considered on hand. |

---

### Receipt Discrepancy

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Receipt Discrepancy |
| **Definition** | Any difference between what was expected on a purchase order and what was actually received — including short shipments, over-shipments, damaged goods, or wrong items. Discrepancies require investigation, documentation, and resolution with the supplier. |
| **Why It Is Important** | Unresolved receipt discrepancies corrupt inventory records and create financial disputes. Accepting short shipments without documentation means the business pays for or expects stock it never received; accepting damage without rejection means unsellable goods enter inventory. |
| **Related Business Terms** | Goods Receipt, Purchase Order, Supplier, Stock Adjustment, Write-Off |
| **Common Misunderstandings** | Discrepancies are sometimes "fixed" by adjusting records to match what arrived without supplier follow-up. This hides supplier performance problems and may result in paying for goods never delivered. |

---

### Put-Away

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Put-Away |
| **Definition** | The movement of received and verified goods from the receiving area to their designated storage location within the warehouse, making them organized, protected, and locatable for future picking and fulfillment. |
| **Why It Is Important** | Stock sitting in the receiving area is not truly available for operations — pickers cannot find it efficiently, it may be damaged in transit areas, and it creates dock congestion. Timely put-away completes the inbound process and enables fulfillment. |
| **Related Business Terms** | Goods Receipt, Warehouse, On-Hand Stock, Pick Pack and Ship |
| **Common Misunderstandings** | Put-away is sometimes skipped or delayed because "the stock is in the building." Until goods are in their storage location, fulfillment is slower, counts are inaccurate, and the receiving area becomes a bottleneck. |

---

## Category 7: Fulfillment & Orders

---

### Order Reservation

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Order Reservation |
| **Definition** | The act of setting aside a specific quantity of stock for a confirmed customer order so it cannot be allocated to other orders. Reservation converts a sales commitment into an operational hold on physical inventory. |
| **Why It Is Important** | Reservation is the bridge between sales commitment and warehouse execution. Without it, the gap between order confirmation and picking creates a window where the same stock can be sold twice — the most common cause of pick failures and customer disappointment. |
| **Related Business Terms** | Reserved Stock, Available-to-Promise, Pick Pack and Ship, Backorder |
| **Common Misunderstandings** | Some organizations confirm orders without reserving stock, assuming the warehouse will "figure it out." By the time picking begins, stock may already be committed elsewhere. Reservation should occur at or immediately after order confirmation. |

---

### Pick, Pack, and Ship

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Pick, Pack, and Ship |
| **Definition** | The three-step warehouse fulfillment process: retrieving ordered items from storage (pick), preparing them for delivery with appropriate packaging and documentation (pack), and handing the completed shipment to the carrier for delivery to the customer (ship). |
| **Why It Is Important** | This is the physical execution of the customer promise. Speed, accuracy, and care during pick, pack, and ship determine whether customers receive the right products on time and in good condition. Errors at this stage are immediately visible to customers. |
| **Related Business Terms** | Order Reservation, Reserved Stock, Partial Fulfillment, Fill Rate, Outbound Exception |
| **Common Misunderstandings** | Shipping is sometimes considered complete when the pick list is printed. Until items are physically picked, verified, packed, and handed to the carrier, the order has not shipped and inventory should not be deducted. |

---

### Backorder

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Backorder |
| **Definition** | A customer order line that cannot be fulfilled immediately due to insufficient stock, held pending replenishment or transfer, with the customer informed of the delay and the business committed to fulfilling when stock becomes available. |
| **Why It Is Important** | Backorders preserve customer relationships when stock is temporarily unavailable — but only if managed well. Uncommunicated backorders, indefinite delays, and forgotten backorder lines destroy trust. Disciplined backorder management converts a stockout from a cancellation into a delayed sale. |
| **Related Business Terms** | Stockout, Partial Fulfillment, Replenishment, Inbound Stock, Order Reservation |
| **Common Misunderstandings** | Backorders are sometimes created without customer consent or communication. A backorder is a mutual agreement to wait — not simply an internal note that the order cannot ship. Customers must be informed and agree to wait. |

---

### Partial Fulfillment

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Partial Fulfillment |
| **Definition** | Shipping only the portion of a customer order that is currently available while placing the remaining quantity on backorder or canceling unfulfillable lines. Partial fulfillment is used when full order delivery is not possible but some customer value can still be delivered. |
| **Why It Is Important** | Partial fulfillment preserves partial revenue and maintains customer relationships during supply constraints. However, it increases shipping costs, complicates order tracking, and frustrates customers who did not expect split deliveries — so it must be used deliberately with customer agreement. |
| **Related Business Terms** | Backorder, Fill Rate, Order Reservation, Stockout, Pick Pack and Ship |
| **Common Misunderstandings** | Partial fulfillment is sometimes used without informing the customer. Shipping half an order without prior agreement often causes more dissatisfaction than waiting for the full order or canceling cleanly. |

---

### Fill Rate

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Fill Rate |
| **Definition** | A measure of how completely the business fulfills customer demand from available stock — typically expressed as the percentage of order lines or order quantity shipped in full on the first attempt, without backorder or cancellation. |
| **Why It Is Important** | Fill rate is a direct indicator of how well inventory management serves customers. Low fill rates mean lost revenue, increased customer service cost, and reputational damage. It connects inventory decisions to commercial outcomes in a single metric. |
| **Related Business Terms** | Stockout, Backorder, Partial Fulfillment, Inventory Accuracy, Available-to-Promise |
| **Common Misunderstandings** | Fill rate is sometimes calculated only on shipped orders, excluding cancelled or backordered lines. True fill rate measures whether demand was met at the point of commitment — not just whether shipped orders were complete. |

---

## Category 8: Network Balance & Transfers

---

### Inter-Location Transfer

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Inter-Location Transfer |
| **Definition** | The movement of stock from one inventory location to another within the business network — such as from a central warehouse to a retail store, or between warehouses — to address local stock imbalances without waiting for supplier replenishment. |
| **Why It Is Important** | Transfers are often faster than new purchasing and can immediately resolve local stockouts when another location has excess. They optimize the use of inventory already owned by the business rather than buying more or losing sales. |
| **Related Business Terms** | Distribution Network, Stock Rebalancing, Stockout, Overstock, Inventory Location |
| **Common Misunderstandings** | Transfers are sometimes initiated without checking whether the source location can spare the stock. Removing stock from a location that also needs it creates a new stockout at the source — network balance requires checking both ends. |

---

### Stock Rebalancing

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Stock Rebalancing |
| **Definition** | A planned review and redistribution of inventory across the location network to reduce simultaneous overstock at some sites and stockouts at others. Rebalancing is proactive network optimization rather than reactive emergency transfers. |
| **Why It Is Important** | Without rebalancing, the business buys more stock to fix local stockouts while excess sits elsewhere — wasting capital and freight. Periodic rebalancing aligns network inventory with network demand and improves overall fill rate and turnover. |
| **Related Business Terms** | Inter-Location Transfer, Distribution Network, Overstock, Stockout, Inventory Turnover |
| **Common Misunderstandings** | Rebalancing is sometimes confused with routine store replenishment. Replenishment fills predictable demand from a central source; rebalancing corrects distribution imbalances that arise from uneven sales, returns, or initial allocation errors. |

---

## Category 9: Inventory Control & Accuracy

---

### Cycle Count

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Cycle Count |
| **Definition** | A physical count of a subset of products at a location on a rotating schedule — for example, specific categories, ABC classes, or aisles each day or week — rather than counting the entire location at once. Cycle counting maintains accuracy through continuous verification. |
| **Why It Is Important** | Cycle counting detects and corrects discrepancies early, before they compound. It avoids the operational disruption of shutting down an entire warehouse for a full count while sustaining the accuracy levels needed for reliable fulfillment and financial reporting. |
| **Related Business Terms** | Physical Inventory Count, Count Variance, Inventory Accuracy, ABC Classification, Stock Adjustment |
| **Common Misunderstandings** | Cycle counting is sometimes treated as optional or low priority. Without regular counts, discrepancies accumulate silently until a full count or a major fulfillment failure reveals the problem — by which time root cause is hard to trace. |

---

### Physical Inventory Count

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Physical Inventory Count |
| **Definition** | A comprehensive count of all inventory at a location — every product, every storage area — typically conducted annually or semi-annually to establish a verified baseline, support financial reporting, and correct accumulated discrepancies. |
| **Why It Is Important** | Full counts provide the definitive inventory position for financial statements and audit substantiation. They reset accuracy when cycle counting alone has not kept pace and validate that the organization's inventory asset is real and correctly valued. |
| **Related Business Terms** | Cycle Count, Count Variance, Inventory Accuracy, Inventory Valuation, Stock Adjustment |
| **Common Misunderstandings** | A full count is sometimes viewed as a replacement for cycle counting. Full counts are point-in-time snapshots; without ongoing cycle counting, accuracy degrades again within weeks of the count. |

---

### Count Variance

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Count Variance |
| **Definition** | The difference between the quantity recorded in inventory records and the quantity found during a physical count. A variance indicates that records and physical reality do not agree and requires investigation before correction. |
| **Why It Is Important** | Variances are the visible symptom of inventory control failures — process errors, theft, damage, misplacement, or recording mistakes. Tracking variance trends by location, product, and reason reveals where the business is losing stock and where controls are weak. |
| **Related Business Terms** | Cycle Count, Physical Inventory Count, Stock Adjustment, Shrinkage, Inventory Accuracy |
| **Common Misunderstandings** | Small variances are sometimes ignored as "not worth investigating." Chronic small variances across many SKUs aggregate into significant financial loss and mask systemic problems that grow over time. |

---

### Stock Adjustment

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Stock Adjustment |
| **Definition** | A formal correction to recorded inventory quantity — increasing or decreasing the balance — with a mandatory reason code, supporting evidence, and approval from an authorized person. Adjustments align records with physical reality or correct data errors. |
| **Why It Is Important** | Adjustments are necessary whenever reality and records diverge, but uncontrolled adjustments are a primary source of inventory fraud and inaccuracy. Mandatory reasons, evidence, and approval ensure every change is justified, traceable, and reviewable. |
| **Related Business Terms** | Count Variance, Write-Off, Reason Code, Shrinkage, Audit Trail |
| **Common Misunderstandings** | Adjustments are sometimes used as a quick fix to make records match without investigating why the discrepancy occurred. This treats the symptom while the underlying problem — theft, process failure, training gap — continues. |

---

### Write-Off

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Write-Off |
| **Definition** | The formal removal of inventory from active stock because it has no remaining business value — due to damage, obsolescence, expiry, theft, or unsellable condition. A write-off reduces both physical and financial inventory and is recorded as a business loss. |
| **Why It Is Important** | Write-offs directly impact margin and must be controlled, documented, and approved. Unrecorded write-offs leave "ghost stock" in the system that cannot be sold but appears available, while unapproved write-offs create fraud risk and audit exposure. |
| **Related Business Terms** | Stock Adjustment, Shrinkage, Reason Code, Inventory Valuation, Restock |
| **Common Misunderstandings** | Write-offs are sometimes delayed or avoided to keep inventory numbers looking healthy. Delayed write-offs inflate both operational and financial inventory, misleading sales, management, and auditors about what the business actually owns. |

---

### Shrinkage

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Shrinkage |
| **Definition** | Inventory loss that cannot be fully explained by known sales or documented adjustments — resulting from theft, unrecorded damage, administrative errors, supplier fraud, or process failures. Shrinkage represents stock that has disappeared without proper accountability. |
| **Why It Is Important** | Shrinkage is a direct hit to margin with no offsetting revenue. Tracking shrinkage trends by location, category, and reason code is essential for loss prevention, control improvement, and understanding the true cost of inventory operations. |
| **Related Business Terms** | Write-Off, Count Variance, Stock Adjustment, Inventory Accuracy, Reason Code |
| **Common Misunderstandings** | Shrinkage is sometimes attributed entirely to theft. While theft is a factor, administrative errors, receiving mistakes, unrecorded damage, and process failures are equally common causes — and are fixable through operational improvement. |

---

### Reason Code

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Reason Code |
| **Definition** | A standardized category assigned to every stock adjustment or write-off explaining why the change occurred — such as damage, shrinkage, count correction, obsolescence, or data error. Reason codes create a consistent vocabulary for inventory exceptions. |
| **Why It Is Important** | Without reason codes, adjustment data is meaningless — the business knows quantities changed but not why. Reason codes enable shrinkage analysis, audit review, trend identification, and targeted corrective action. |
| **Related Business Terms** | Stock Adjustment, Write-Off, Shrinkage, Audit Trail, Segregation of Duties |
| **Common Misunderstandings** | Reason codes are sometimes treated as optional or filled with generic labels like "other." Vague codes defeat their purpose — the business cannot analyze or prevent losses it has not categorized. |

---

### Inventory Accuracy

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Inventory Accuracy |
| **Definition** | The degree to which recorded inventory quantities match physical stock across products and locations, typically measured as the percentage of items or SKUs counted without a material variance. High accuracy means the business can trust its inventory records. |
| **Why It Is Important** | Inventory accuracy is the foundation of every other inventory capability. Inaccurate records cause stockouts despite apparent availability, excess purchasing, pick failures, unreliable financial reporting, and loss of organizational trust in inventory data. |
| **Related Business Terms** | Cycle Count, Count Variance, Stock Adjustment, Fill Rate, Inventory Valuation |
| **Common Misunderstandings** | Accuracy is sometimes measured only at annual full count time. True accuracy is a continuous operational standard — if records drift between counts, day-to-day decisions are made on unreliable data even if the annual snapshot looks acceptable. |

---

## Category 10: Finance & Valuation

---

### Inventory Valuation

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Inventory Valuation |
| **Definition** | The process of determining the total monetary value of inventory held by the business — by applying unit costs or valuation rates to physical quantities — for financial reporting, balance sheet presentation, and reconciliation with accounting records. |
| **Why It Is Important** | Inventory is a major balance sheet asset. Accurate valuation ensures financial statements are truthful, supports working capital management, enables margin analysis, and satisfies audit requirements. Valuation disconnects between operations and finance undermine executive confidence in all inventory data. |
| **Related Business Terms** | On-Hand Stock, Write-Off, Carrying Cost, Inventory Turnover, Stock Adjustment |
| **Common Misunderstandings** | Operational stock quantities and financial inventory value are sometimes assumed to always match. Timing differences, unrecorded adjustments, in-transit stock, and costing method choices can create variances that require reconciliation — quantity accuracy does not automatically guarantee valuation accuracy. |

---

### Carrying Cost

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Carrying Cost |
| **Definition** | The total cost of holding inventory over time — including capital tied up in stock, storage space, handling labor, insurance, obsolescence risk, and shrinkage. Carrying cost represents what the business pays to keep goods on hand rather than converting them to cash. |
| **Why It Is Important** | Carrying cost explains why overstock is not harmless. Every unit held beyond what demand requires consumes capital and incurs ongoing expense. Understanding carrying cost helps the business make informed trade-offs between availability (avoiding stockouts) and efficiency (minimizing excess). |
| **Related Business Terms** | Overstock, Inventory Turnover, Safety Stock, Replenishment, Inventory Valuation |
| **Common Misunderstandings** | Carrying cost is often ignored because it is not a visible line item on invoices. It is a real economic cost — typically estimated at 15–30% of inventory value annually — that makes excess stock far more expensive than it appears. |

---

### Inventory Turnover

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Inventory Turnover |
| **Definition** | A measure of how many times the business sells and replaces its inventory over a period, typically calculated as cost of goods sold divided by average inventory value. Higher turnover indicates stock is moving efficiently; lower turnover suggests slow-moving or excess inventory. |
| **Why It Is Important** | Turnover connects inventory investment to sales performance. Low turnover signals capital trapped in slow movers, increasing obsolescence and carrying cost risk. Improving turnover frees working capital and indicates healthier alignment between supply and demand. |
| **Related Business Terms** | Carrying Cost, Overstock, Inventory Valuation, Replenishment, ABC Classification |
| **Common Misunderstandings** | High turnover is sometimes pursued without regard to stockouts. Extremely high turnover may mean the business is under-stocked and losing sales. The goal is optimal turnover — fast enough to minimize carrying cost, slow enough to maintain service levels. |

---

## Category 11: Returns

---

### Customer Return

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Customer Return |
| **Definition** | Goods sent back by a customer after purchase — due to defect, wrong item, dissatisfaction, or warranty claim — requiring intake, inspection, resolution (refund, replacement, or credit), and inventory disposition. |
| **Why It Is Important** | Returns affect customer satisfaction, inventory accuracy, and financial results. Mishandled returns — not recorded, not inspected, or not resolved — create ghost stock, revenue leakage, and repeat customer complaints. Return volume also signals product quality and fulfillment accuracy issues. |
| **Related Business Terms** | Return Authorization, Restock, Write-Off, Customer Service, Partial Fulfillment |
| **Common Misunderstandings** | Returns are sometimes treated as a customer service issue only. Every return has an inventory consequence — goods re-enter stock, are written off, or are lost — and must be processed through inventory discipline, not just refunded and forgotten. |

---

### Return Authorization

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Return Authorization |
| **Definition** | Formal approval for a customer to return specified products, documenting the return reason, eligible resolution, and instructions for shipping or drop-off. The authorization links the physical return to the original order and expected outcome. |
| **Why It Is Important** | Return authorization prevents unauthorized returns, ensures policy compliance, and gives the warehouse advance notice to expect incoming goods. Without authorization, receiving cannot match returns to orders and resolution becomes ad hoc. |
| **Related Business Terms** | Customer Return, Restock, Write-Off, Customer Service |
| **Common Misunderstandings** | Authorization is sometimes skipped for "simple" returns. Even straightforward returns need documentation to connect the physical goods to the order, trigger the correct refund or replacement, and update inventory. |

---

### Restock (Return-to-Stock)

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Restock (Return-to-Stock) |
| **Definition** | Returning a received customer return to sellable inventory after inspection confirms the product meets resale quality standards. Restocking increases on-hand quantity and makes the product available for future orders. |
| **Why It Is Important** | Restocking recovers inventory value from returns — a returned item in resalable condition is an asset, not a loss. Proper inspection before restocking prevents damaged or used goods from being sold as new, protecting customer trust and reducing future returns. |
| **Related Business Terms** | Customer Return, Write-Off, Goods Receipt, Inventory Accuracy |
| **Common Misunderstandings** | All returns are sometimes restocked automatically. Only inspected, resalable goods should re-enter inventory — defective, used, or damaged returns must be written off or disposed of, not placed back on the shelf. |

---

## Category 12: Governance & Compliance

---

### Audit Trail

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Audit Trail |
| **Definition** | The complete, chronological record of inventory-related activities — who did what, when, where, and why — including receipts, shipments, adjustments, count results, and approvals. The audit trail provides evidence for investigation, accountability, and audit. |
| **Why It Is Important** | When discrepancies, fraud, or customer disputes arise, the audit trail is the only way to reconstruct what happened. Without it, the business cannot hold people accountable, satisfy auditors, or learn from mistakes. A strong audit trail is both a control and a diagnostic tool. |
| **Related Business Terms** | Stock Adjustment, Reason Code, Segregation of Duties, Inventory Audit, Write-Off |
| **Common Misunderstandings** | The audit trail is sometimes thought to exist only for finance or IT. Every person who touches inventory — receivers, pickers, counters, approvers — creates audit trail entries through their documented actions. Informal or undocumented changes leave gaps. |

---

### Segregation of Duties

| Attribute | Description |
|-----------|-------------|
| **Business Term** | Segregation of Duties |
| **Definition** | A control principle requiring that no single person can complete an inventory transaction from start to finish without independent review — for example, the person who counts stock should not be the same person who approves the adjustment based on that count. |
| **Why It Is Important** | Segregation of duties is the primary defense against fraud and undetected error. When one person can record, approve, and adjust inventory without oversight, the opportunity and incentive for manipulation increase dramatically. Auditors specifically test this control. |
| **Related Business Terms** | Audit Trail, Stock Adjustment, Count Variance, Inventory Audit, Reason Code |
| **Common Misunderstandings** | Segregation is sometimes waived in small teams as "impractical." While perfect separation is harder with fewer people, minimum standards — such as independent approval of adjustments — must still be maintained or control risk is accepted explicitly. |

---

## Quick Reference: Commonly Confused Term Pairs

| Term A | Term B | Key Difference |
|--------|--------|----------------|
| On-Hand Stock | Available-to-Promise | On-hand is physical total; ATP subtracts reservations |
| Purchase Requisition | Purchase Order | Requisition is internal request; PO is external supplier commitment |
| Goods Receipt | Physical Arrival | Arrival is truck at dock; receipt is verified and recorded acceptance |
| Cycle Count | Physical Inventory Count | Cycle counts a rotating subset; full count covers everything at once |
| Stock Adjustment | Write-Off | Adjustment corrects quantity; write-off removes valueless stock permanently |
| Backorder | Stockout | Stockout is zero stock; backorder is a customer order waiting for supply |
| Replenishment | Rebalancing | Replenishment buys or sources new stock; rebalancing redistributes existing stock |
| Reserved Stock | Shipped Stock | Reserved is still on shelf; shipped has left and reduced on-hand |
| Inbound Stock | On-Hand Stock | Inbound is ordered but not received; on-hand is physically present |
| Reorder Level | Minimum Threshold | Reorder level starts routine action; minimum threshold signals critical urgency |

---

## Document Summary

This glossary defines **50 business terms** essential to inventory management operations across a multi-location distribution and retail organization. Terms are defined in plain business language with importance rationale, related concepts, and common misunderstandings to support consistent communication across departments.

This glossary should be used alongside the Business Process Analysis, Business Actor Analysis, and Business Workflow documents as the shared vocabulary for requirements, training, and operational policy development.

---

*End of Business Glossary Document*
