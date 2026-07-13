# Ubiquitous Language
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DM-008 |
| **Document Title** | Ubiquitous Language — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | BRD-IMS-001 (Section 21), SRS-DM-001 through SRS-DM-007, SRS-BR-001 (Business Rules) |
| **Date** | July 5, 2026 |
| **Scope** | Business terminology only — aligned with Domain Model; no technical or implementation terms |

### Purpose

This document defines the **Ubiquitous Language** of the Inventory Management System — the shared, precise vocabulary used by business stakeholders and reflected in the domain model. Every term maps to a concept in the Domain Entity Model (SRS-DM-001), a Bounded Context (SRS-DM-007), or an industry business rule (SRS-BR-001).

When business and technology teams use these terms consistently, requirements, use cases, and domain model artifacts remain aligned.

### How to Read This Document

| Field | Meaning |
|-------|---------|
| **Term** | The canonical business word or phrase |
| **Definition** | What the term means in this organization |
| **Context** | The Bounded Context where the term is primarily defined and used |
| **Related Terms** | Other ubiquitous language terms with direct business relationship |
| **Terms That Should Never Be Confused** | Commonly misused or similar terms with different meanings |

### Context Reference

| Context Code | Bounded Context |
|--------------|-----------------|
| **PC** | Product Catalog |
| **WN** | Warehouse Network |
| **IG** | Inventory Governance |
| **IB** | Inventory Balance |
| **PS** | Procurement & Supplier |
| **IR** | Inbound Receiving |
| **OF** | Order Fulfillment |
| **NT** | Network Transfer |
| **IA** | Inventory Accuracy |
| **RM** | Returns Management |
| **CC** | Commercial Campaign |
| **IAc** | Identity & Access |
| **II** | Inventory Intelligence |
| **ALL** | Used across multiple contexts |

---

## Section 1: Product Catalog (PC)

---

### SKU (Stock Keeping Unit)

| Field | Detail |
|-------|--------|
| **Definition** | The unique business identifier for a distinct product tracked in inventory. SKU is the primary identity key for all stock operations across locations. |
| **Context** | Product Catalog |
| **Related Terms** | Product, Unit of Measure, Barcode, Stock Position |
| **Terms That Should Never Be Confused** | **Lot/Batch Number** — identifies a production or receipt grouping within a SKU, not the product itself; **Product Name** — descriptive label, not unique identifier |

---

### Product

| Field | Detail |
|-------|--------|
| **Definition** | The master record for a SKU including name, description, unit of measure, category, lifecycle status, ABC classification, and rotation/traceability attributes. |
| **Context** | Product Catalog |
| **Related Terms** | SKU, Product Lifecycle Status, ABC Classification, Rotation Policy |
| **Terms That Should Never Be Confused** | **Stock Position** — quantity of a product at a location, not the product definition; **Product Line** — informal commercial grouping, not an IMS entity |

---

### Product Lifecycle Status

| Field | Detail |
|-------|--------|
| **Definition** | The commercial availability state of a product: **Active** (orderable and fulfillable), **Inactive** (not sold but may hold stock), or **Discontinued** (exit from assortment; no reorder permitted). |
| **Context** | Product Catalog |
| **Related Terms** | Product, Purchase Order, Inventory Reservation |
| **Terms That Should Never Be Confused** | **Stock Status Indicator** — describes quantity health (in stock, low stock) at a location, not product commercial status; **Product Category** — classification for reporting, not lifecycle |

---

### ABC Classification

| Field | Detail |
|-------|--------|
| **Definition** | Product segmentation by business importance — Class **A** (highest revenue/velocity/criticality), **B** (moderate), or **C** (lower) — used to prioritize count frequency, monitoring intensity, and alert priority. |
| **Context** | Product Catalog |
| **Related Terms** | Product, Cycle Count, Operational Alert |
| **Terms That Should Never Be Confused** | **Product Category** — merchandise grouping (e.g., Electronics), not operational priority; **Stock Status Indicator** — current quantity state, not importance classification |

---

### Rotation Policy

| Field | Detail |
|-------|--------|
| **Definition** | The required stock rotation discipline for a product: **FIFO** (First-In, First-Out) for standard goods, or **FEFO** (First-Expired, First-Out) for shelf-life products. |
| **Context** | Product Catalog |
| **Related Terms** | Product, Lot/Batch, Put-Away, Fulfillment Execution |
| **Terms That Should Never Be Confused** | **Put-Away** — the act of placing stock in storage, not the rotation rule; **Pick Path** — warehouse navigation, not rotation policy |

---

### Unit of Measure (UOM)

| Field | Detail |
|-------|--------|
| **Definition** | The standard unit in which a product is counted, ordered, stored, and sold — such as Each, Case, Pallet, Kilogram, or Liter. |
| **Context** | Product Catalog |
| **Related Terms** | Product, SKU, Quantity |
| **Terms That Should Never Be Confused** | **Quantity** — numeric amount, which always includes a UOM; bare numbers without UOM are incomplete in inventory context |

---

## Section 2: Warehouse Network (WN)

---

### Inventory Location

| Field | Detail |
|-------|--------|
| **Definition** | A physical place where stock is held, received, counted, and fulfilled — such as a warehouse, store, or distribution point. Identified by a unique Location Code. |
| **Context** | Warehouse Network |
| **Related Terms** | Storage Position, Stock Position, Location Freeze |
| **Terms That Should Never Be Confused** | **Storage Position** — subdivision within a location (bin/shelf), not the location itself; **Supplier Location** — external vendor site, not an owned inventory location |

---

### Storage Position

| Field | Detail |
|-------|--------|
| **Definition** | A designated storage area within an inventory location — zone, aisle, bin, or shelf — where received goods are placed after put-away and from which picks are retrieved. |
| **Context** | Warehouse Network |
| **Related Terms** | Inventory Location, Put-Away, Fulfillment Execution |
| **Terms That Should Never Be Confused** | **Inventory Location** — the warehouse or site as a whole; **Dock** — receiving area before put-away, not a storage position |

---

### Location Freeze

| Field | Detail |
|-------|--------|
| **Definition** | A temporary suspension of all receiving, shipping, transfers, and adjustments at a location during a wall-to-wall physical inventory count, ensuring a stable quantity snapshot. |
| **Context** | Warehouse Network |
| **Related Terms** | Physical Inventory Count, Inventory Location |
| **Terms That Should Never Be Confused** | **Quarantine Hold** — excludes specific stock from sellable availability, not a location-wide operational suspension; **Location Deactivation** — permanent or semi-permanent closure, not temporary count freeze |

---

## Section 3: Inventory Governance (IG)

---

### Reason Code

| Field | Detail |
|-------|--------|
| **Definition** | A standardized, categorized business explanation required for every inventory adjustment, write-off, and receipt discrepancy — enabling shrinkage analysis and audit accountability. |
| **Context** | Inventory Governance |
| **Related Terms** | Stock Adjustment, Inventory Write-Off, Receipt Discrepancy, Governance Policy |
| **Terms That Should Never Be Confused** | **Disposition Decision** — outcome for returned goods (restock/quarantine/write-off), not a general adjustment taxonomy; **Notes/Comments** — free text, not a governed categorized code |

---

### Governance Policy

| Field | Detail |
|-------|--------|
| **Definition** | An organization-wide inventory control rule defining approval thresholds, tolerance limits, segregation-of-duties requirements, or exception handling — effective for a defined period. |
| **Context** | Inventory Governance |
| **Related Terms** | Reason Code, Approval Threshold, Segregation of Duties |
| **Terms That Should Never Be Confused** | **Stock Policy** — replenishment thresholds per product-location, not enterprise control rules; **Business Rule (BR-xxx)** — documented policy statement in SRS-BR-001, of which governance policy is the operational parameterization |

---

### Segregation of Duties (SoD)

| Field | Detail |
|-------|--------|
| **Definition** | The separation of conflicting responsibilities — such as counting vs. approving, or initiating vs. authorizing adjustments — to prevent fraud and undetected error. |
| **Context** | Inventory Governance, Identity & Access |
| **Related Terms** | Governance Policy, Count Variance, Role Assignment |
| **Terms That Should Never Be Confused** | **Role-Based Access** — what a user may do by role, not the conflict prevention rule itself; **Dual Approval** — one instance of SoD, not the full concept |

---

### Approval Threshold

| Field | Detail |
|-------|--------|
| **Definition** | A governance limit — expressed as quantity, monetary value, or both — above which an inventory action requires independent approval by an authorized person who did not initiate the underlying transaction. |
| **Context** | Inventory Governance |
| **Related Terms** | Governance Policy, Stock Adjustment, Count Variance |
| **Terms That Should Never Be Confused** | **Reorder Level** — triggers replenishment, not approval; **Safety Stock** — buffer quantity, not an approval trigger |

---

## Section 4: Inventory Balance (IB)

---

### Stock Position

| Field | Detail |
|-------|--------|
| **Definition** | The authoritative inventory balance for one product at one location — maintaining on-hand, reserved, and available-to-promise quantities, ownership classification, and optional lot/batch breakdown. |
| **Context** | Inventory Balance |
| **Related Terms** | On-Hand Stock, Available-to-Promise, Reserved Stock, Stock Policy |
| **Terms That Should Never Be Confused** | **Product** — what is being tracked; **Stock Policy** — replenishment rules, not current quantities; **Storage Position** — where physically placed within location |

---

### On-Hand Stock

| Field | Detail |
|-------|--------|
| **Definition** | The physical quantity of a product present at a location at a point in time, regardless of reservation or hold status. |
| **Context** | Inventory Balance |
| **Related Terms** | Stock Position, Available-to-Promise, Reserved Stock |
| **Terms That Should Never Be Confused** | **Available-to-Promise (ATP)** — portion of on-hand available for new commitments; **On-Order** — inbound expected, not physically present; **In-Transit Stock** — left source but not yet at destination |

---

### Available-to-Promise (ATP)

| Field | Detail |
|-------|--------|
| **Definition** | The quantity that may be quoted or committed to new customers — calculated as on-hand minus reserved minus quarantined/hold quantities. The only honest measure for sales promises. |
| **Context** | Inventory Balance |
| **Related Terms** | On-Hand Stock, Reserved Stock, Quarantine Hold, Inventory Reservation |
| **Terms That Should Never Be Confused** | **On-Hand Stock** — total physical quantity including reserved and quarantined; **Inbound Expected** — pipeline supply not yet available; **Committed Stock** — colloquial term often meaning reserved, but ATP is the precise quotable measure |

---

### Reserved Stock

| Field | Detail |
|-------|--------|
| **Definition** | On-hand quantity operationally committed to confirmed customer orders, removed from ATP until fulfilled or released. |
| **Context** | Inventory Balance, Order Fulfillment |
| **Related Terms** | Inventory Reservation, Available-to-Promise, On-Hand Stock |
| **Terms That Should Never Be Confused** | **Backorder** — customer-agreed delay for quantity not yet reserved because stock is unavailable; **Promotional Allocation** — ring-fenced for campaign, not customer order reservation; **Safety Stock** — buffer not for customer commitment |

---

### Stock Policy

| Field | Detail |
|-------|--------|
| **Definition** | Replenishment thresholds defined for a specific product at a specific location: reorder level, minimum threshold, safety stock buffer, and maximum (overstock) level. |
| **Context** | Inventory Balance |
| **Related Terms** | Reorder Level, Safety Stock, Stock Position, Operational Alert |
| **Terms That Should Never Be Confused** | **Governance Policy** — enterprise approval and control rules, not replenishment thresholds; **Stock Position** — current quantities, not policy limits |

---

### Reorder Level

| Field | Detail |
|-------|--------|
| **Definition** | The ATP threshold that triggers replenishment review or action, calculated to allow sufficient lead time for supply to arrive before stockout. |
| **Context** | Inventory Balance |
| **Related Terms** | Stock Policy, Safety Stock, Low Stock, Replenishment |
| **Terms That Should Never Be Confused** | **Minimum Threshold** — lowest acceptable level before critical action, may differ from reorder trigger; **Maximum Level** — overstock indicator, not reorder trigger; **Zero ATP** — stockout condition, not the proactive trigger point |

---

### Safety Stock

| Field | Detail |
|-------|--------|
| **Definition** | A deliberate buffer quantity above the reorder level protecting against demand and supply uncertainty. Must not be consumed for routine fulfillment without authorized exception and replenishment plan. |
| **Context** | Inventory Balance |
| **Related Terms** | Stock Policy, Reorder Level, Inventory Reservation |
| **Terms That Should Never Be Confused** | **Reserved Stock** — committed to specific orders, not a general buffer; **Minimum Threshold** — policy floor, not the uncertainty buffer; **Reorder Level** — trigger point, which is typically above safety stock |

---

### Stock Status Indicator

| Field | Detail |
|-------|--------|
| **Definition** | A derived classification of inventory health for a product at a location: **In Stock**, **Low Stock**, **Out of Stock**, or **Overstock** — based on comparison of ATP against Stock Policy thresholds. |
| **Context** | Inventory Balance |
| **Related Terms** | Stock Position, Stock Policy, Operational Alert |
| **Terms That Should Never Be Confused** | **Product Lifecycle Status** — active/inactive/discontinued, not quantity health; **Quarantine Hold** — specific hold status, not overall stock health |

---

### Lot/Batch

| Field | Detail |
|-------|--------|
| **Definition** | A traceable production or receipt grouping for products requiring lot-level tracking, carrying expiration date, manufacture date, and quality attributes for FEFO rotation and recall scope. |
| **Context** | Inventory Balance |
| **Related Terms** | Product, Rotation Policy, Goods Receipt, Fulfillment Execution |
| **Terms That Should Never Be Confused** | **SKU** — product identity, not production grouping; **Serial Number** — individual item tracking, finer granularity than lot (out of MVP scope) |

---

### Quarantine Hold

| Field | Detail |
|-------|--------|
| **Definition** | A business hold excluding physically present stock from sellable ATP due to quality investigation, regulatory restriction, product recall, or pending customs clearance. |
| **Context** | Inventory Balance |
| **Related Terms** | Available-to-Promise, Stock Position, Bonded Inventory |
| **Terms That Should Never Be Confused** | **Location Freeze** — suspends all location activity, not specific stock; **Reserved Stock** — committed to orders, not under investigation; **Inactive Product** — commercial status, not physical hold |

---

### Bonded Inventory

| Field | Detail |
|-------|--------|
| **Definition** | Stock physically present but under customs control — duties unpaid — that must not be released to domestic sellable availability until customs clearance is confirmed. |
| **Context** | Inventory Balance, Inbound Receiving |
| **Related Terms** | Quarantine Hold, Put-Away, Ownership Classification |
| **Terms That Should Never Be Confused** | **Quarantine Hold** — broader hold category including quality and recall, not specifically customs; **Consignment Stock** — supplier-owned until consumption, not customs-controlled |

---

### Consignment Stock

| Field | Detail |
|-------|--------|
| **Definition** | Inventory physically at the organization's location but owned by the supplier until a defined consumption or sale event per supplier agreement. Not treated as owned stock for valuation until ownership transfers. |
| **Context** | Inventory Balance, Procurement & Supplier |
| **Related Terms** | Supplier, Ownership Classification, Inventory Valuation Snapshot |
| **Terms That Should Never Be Confused** | **On-Hand Stock (Owned)** — organization balance-sheet asset; **Bonded Inventory** — customs-controlled, not supplier-owned; **In-Transit Stock** — in movement, not ownership question |

---

### Ownership Classification

| Field | Detail |
|-------|--------|
| **Definition** | The legal and financial ownership state of held inventory: **Owned**, **Consignment**, or **Bonded** — governing valuation treatment and availability rules. |
| **Context** | Inventory Balance |
| **Related Terms** | Consignment Stock, Bonded Inventory, Inventory Valuation Snapshot |
| **Terms That Should Never Be Confused** | **Product Lifecycle Status** — commercial availability, not legal ownership; **Stock Status Indicator** — quantity health, not ownership type |

---

## Section 5: Procurement & Supplier (PS)

---

### Supplier

| Field | Detail |
|-------|--------|
| **Definition** | An external vendor from whom the organization procures goods, identified by Supplier Code, carrying commercial terms including payment terms, lead time, and consignment agreement indicator. |
| **Context** | Procurement & Supplier |
| **Related Terms** | Purchase Order, Supplier Invoice, Goods Receipt |
| **Terms That Should Never Be Confused** | **Carrier/Logistics Partner** — transports goods, does not supply them; **Customer** — receives outbound goods, not inbound supplier |

---

### Purchase Requisition

| Field | Detail |
|-------|--------|
| **Definition** | An internal request to procure stock — specifying product, quantity, and target location — submitted for approval before commercial Purchase Order creation. |
| **Context** | Procurement & Supplier |
| **Related Terms** | Purchase Order, Replenishment, Operational Alert |
| **Terms That Should Never Be Confused** | **Purchase Order** — authorized external commercial commitment to supplier, not internal request; **Transfer Request** — internal network redistribution, not external procurement |

---

### Purchase Order (PO)

| Field | Detail |
|-------|--------|
| **Definition** | An authorized commercial commitment to a supplier specifying products, quantities, prices, delivery terms, and receiving location. Required before supplier goods receipt except approved ad-hoc exceptions. |
| **Context** | Procurement & Supplier |
| **Related Terms** | Supplier, Purchase Requisition, Goods Receipt, Expected Inbound Delivery |
| **Terms That Should Never Be Confused** | **Purchase Requisition** — internal pre-approval request, not supplier-facing commitment; **Customer Order** — outbound demand, not inbound supply; **Goods Receipt** — physical arrival event, not commercial authorization |

---

### Expected Inbound Delivery

| Field | Detail |
|-------|--------|
| **Definition** | A planned or confirmed supplier shipment tied to a Purchase Order, communicating anticipated arrival date and quantity for receiving preparation and pipeline visibility. |
| **Context** | Procurement & Supplier |
| **Related Terms** | Purchase Order, Goods Receipt, Inbound Expected |
| **Terms That Should Never Be Confused** | **Goods Receipt** — actual verified arrival, not plan; **In-Transit Stock** — inter-location movement within network, not supplier inbound; **Inbound Expected (ATP view)** — informational pipeline quantity, does not increase ATP |

---

### Lead Time

| Field | Detail |
|-------|--------|
| **Definition** | The elapsed business time from purchase order placement until goods are available for sale or use at the receiving location, accounting for supplier processing, transit, receipt, and put-away. |
| **Context** | Procurement & Supplier, Inventory Balance |
| **Related Terms** | Purchase Order, Stock Policy, Reorder Level |
| **Terms That Should Never Be Confused** | **Transit Time** — shipping duration only, subset of lead time; **Fulfillment Cycle Time** — order-to-ship for customers, not supplier inbound |

---

## Section 6: Inbound Receiving (IR)

---

### Goods Receipt

| Field | Detail |
|-------|--------|
| **Definition** | The business event of verifying and accepting inbound goods — confirming quantity, product identity, and condition against Purchase Order or authorized exception — before stock enters inventory control. |
| **Context** | Inbound Receiving |
| **Related Terms** | Purchase Order, Receipt Discrepancy, Put-Away, Supplier |
| **Terms That Should Never Be Confused** | **Put-Away** — placement in storage after receipt, separate step; **Stock Received** — balance increase after put-away complete, not dock verification; **Customer Return** — inbound from customer, not supplier |

---

### Receipt Discrepancy

| Field | Detail |
|-------|--------|
| **Definition** | A documented difference between expected and actual receipt — short shipment, over-shipment, wrong item, damage, or shelf-life non-compliance — captured with evidence at the point of receipt. |
| **Context** | Inbound Receiving |
| **Related Terms** | Goods Receipt, Reason Code, Three-Way Match |
| **Terms That Should Never Be Confused** | **Count Variance** — system vs. physical count during cycle/physical count, not receipt vs. PO; **Stock Adjustment** — correction after investigation, not receipt-time exception |

---

### Put-Away

| Field | Detail |
|-------|--------|
| **Definition** | The confirmation that verified received goods have been moved from the receiving dock to a designated storage position. Stock is not available for sale or fulfillment until put-away is complete. |
| **Context** | Inbound Receiving |
| **Related Terms** | Goods Receipt, Storage Position, Stock Received, Rotation Policy |
| **Terms That Should Never Be Confused** | **Goods Receipt** — verification at dock, not storage placement; **Pick** — retrieval for outbound order, opposite direction; **Stock Received** — domain outcome after put-away increases on-hand |

---

### Minimum Remaining Shelf Life (MRSL)

| Field | Detail |
|-------|--------|
| **Definition** | The minimum acceptable remaining shelf life at receipt for shelf-life products — deliveries not meeting MRSL must be rejected or dispositioned before acceptance into sellable inventory. |
| **Context** | Inbound Receiving, Product Catalog |
| **Related Terms** | Rotation Policy (FEFO), Lot/Batch, Receipt Discrepancy |
| **Terms That Should Never Be Confused** | **Expiration Date** — absolute date on lot, not the policy threshold; **FEFO** — pick rotation rule at fulfillment, not receipt acceptance criterion |

---

### Supplier Invoice

| Field | Detail |
|-------|--------|
| **Definition** | The supplier's billing document for goods supplied, matched against Purchase Order and Goods Receipt in three-way match before payment authorization. |
| **Context** | Inbound Receiving |
| **Related Terms** | Three-Way Match, Purchase Order, Goods Receipt |
| **Terms That Should Never Be Confused** | **Purchase Order** — authorization to buy, not bill; **Goods Receipt** — operational receipt record, not financial document; **Inventory Valuation Snapshot** — period-end value summary, not supplier bill |

---

### Three-Way Match

| Field | Detail |
|-------|--------|
| **Definition** | Financial control confirming agreement among Purchase Order (what was ordered), Goods Receipt (what was received), and Supplier Invoice (what was billed) within defined tolerance before payment is authorized. |
| **Context** | Inbound Receiving |
| **Related Terms** | Supplier Invoice, Purchase Order, Goods Receipt, Governance Policy |
| **Terms That Should Never Be Confused** | **Inventory Valuation Reconciliation** — operational stock value vs. general ledger, not PO-receipt-invoice match; **Receipt Discrepancy** — operational variance at dock, not financial match outcome |

---

## Section 7: Order Fulfillment (OF)

---

### Customer Order

| Field | Detail |
|-------|--------|
| **Definition** | A customer demand for products triggering availability confirmation, reservation, and fulfillment execution. IMS holds fulfillment-relevant order context; authoritative order data may reside in external sales systems. |
| **Context** | Order Fulfillment |
| **Related Terms** | Inventory Reservation, Fulfillment Execution, Shipment, Backorder |
| **Terms That Should Never Be Confused** | **Purchase Order** — inbound supplier commitment, not customer demand; **Shipment** — dispatch event, not the order itself; **Transfer Request** — internal stock movement, not customer sale |

---

### Inventory Reservation

| Field | Detail |
|-------|--------|
| **Definition** | An operational hold on stock for a confirmed customer order line, increasing reserved quantity and decreasing ATP from the moment of order confirmation until fulfillment or release. |
| **Context** | Order Fulfillment, Inventory Balance |
| **Related Terms** | Reserved Stock, Customer Order, Available-to-Promise |
| **Terms That Should Never Be Confused** | **Backorder** — agreement to wait for unavailable quantity, not a hold on existing stock; **Promotional Allocation** — campaign ring-fence, not order-specific hold; **Quarantine Hold** — quality/regulatory exclusion, not customer commitment |

---

### Fulfillment Execution

| Field | Detail |
|-------|--------|
| **Definition** | The warehouse work of picking, verifying, packing, and preparing order lines for dispatch — applying FIFO/FEFO rotation and capturing lot/batch for traceable products. |
| **Context** | Order Fulfillment |
| **Related Terms** | Pick Verification, Shipment, Customer Order, Storage Position |
| **Terms That Should Never Be Confused** | **Shipment** — carrier handoff and dispatch, after pick verification; **Goods Receipt** — inbound operation, not outbound; **Inventory Reservation** — quantity hold, not physical warehouse work |

---

### Pick Verification

| Field | Detail |
|-------|--------|
| **Definition** | Confirmation that physically retrieved items match the order line in product, quantity, and lot/batch — required before shipment recording. |
| **Context** | Order Fulfillment |
| **Related Terms** | Fulfillment Execution, Shipment, Rotation Policy |
| **Terms That Should Never Be Confused** | **Goods Receipt Verification** — inbound dock check, not outbound pick check; **Cycle Count** — accuracy audit, not order fulfillment step |

---

### Shipment

| Field | Detail |
|-------|--------|
| **Definition** | The confirmed dispatch of verified goods to a carrier for customer delivery, triggering on-hand deduction and reservation consumption at the ship-from location. |
| **Context** | Order Fulfillment |
| **Related Terms** | Fulfillment Execution, Pick Verification, Customer Order, Stock Shipped |
| **Terms That Should Never Be Confused** | **Expected Inbound Delivery** — supplier shipment inbound, not customer outbound; **Transfer Dispatch** — inter-location movement, not customer delivery; **Fulfillment Execution** — warehouse work including pick and pack, not carrier handoff |

---

### Backorder

| Field | Detail |
|-------|--------|
| **Definition** | A customer-agreed delay to fulfill remaining order quantity when full quantity is unavailable at confirmation — requiring explicit customer acknowledgment before recording. A mutual commercial commitment, not an internal note. |
| **Context** | Order Fulfillment |
| **Related Terms** | Partial Fulfillment, Customer Order, Inventory Reservation |
| **Terms That Should Never Be Confused** | **Inventory Reservation** — hold on existing available stock; **Purchase Order** — inbound supply order to replenish, not customer-facing delay; **Out of Stock** — condition, not customer agreement |

---

### Partial Fulfillment

| Field | Detail |
|-------|--------|
| **Definition** | Shipping the available portion of an order line when full quantity cannot be met, with remaining quantity handled via backorder or separate fulfillment. |
| **Context** | Order Fulfillment |
| **Related Terms** | Backorder, Shipment, Customer Order |
| **Terms That Should Never Be Confused** | **Split Fulfillment** — shipping from multiple locations, not partial quantity; **Backorder** — the unfulfilled remainder agreement, not the act of shipping partial quantity |

---

### Multi-Location Split Fulfillment

| Field | Detail |
|-------|--------|
| **Definition** | Fulfilling a single customer order from multiple inventory locations when no single location holds sufficient ATP for the full order quantity. |
| **Context** | Order Fulfillment |
| **Related Terms** | Customer Order, Inventory Reservation, Stock Transfer |
| **Terms That Should Never Be Confused** | **Partial Fulfillment** — less than full quantity from one location, not multiple locations; **Stock Transfer** — internal redistribution, not customer-directed fulfillment |

---

## Section 8: Network Transfer (NT)

---

### Transfer Request

| Field | Detail |
|-------|--------|
| **Definition** | A formal request to move stock from a source location to a destination location, specifying product and quantity, evaluated against network availability and source minimum thresholds before approval. |
| **Context** | Network Transfer |
| **Related Terms** | Stock Transfer, Network Rebalancing, Purchase Requisition |
| **Terms That Should Never Be Confused** | **Purchase Requisition** — request to buy from supplier, not move existing stock; **Customer Order** — outbound customer demand, not internal redistribution; **Stock Transfer** — approved and executing movement, not the request |

---

### Stock Transfer

| Field | Detail |
|-------|--------|
| **Definition** | The executed movement of stock between inventory locations — from dispatch at source through in-transit tracking to receipt at destination — with full transaction history. |
| **Context** | Network Transfer |
| **Related Terms** | In-Transit Stock, Transfer Request, Stock Position |
| **Terms That Should Never Be Confused** | **Shipment** — outbound to customer, not inter-location; **Goods Receipt** — inbound from supplier, not from another owned location; **Transfer Request** — pre-approval intent, not executed movement |

---

### In-Transit Stock

| Field | Detail |
|-------|--------|
| **Definition** | Inventory that has left the source location but has not yet been received at the destination — excluded from both source and destination ATP until receipt is confirmed. |
| **Context** | Network Transfer |
| **Related Terms** | Stock Transfer, Expected Inbound Delivery |
| **Terms That Should Never Be Confused** | **Expected Inbound Delivery** — supplier pipeline inbound, not inter-location; **On-Hand Stock** — at a location, not in movement; **Inbound Expected (ATP view)** — informational only for supplier supply |

---

### Network Rebalancing

| Field | Detail |
|-------|--------|
| **Definition** | Proactive redistribution of stock across the location network to resolve simultaneous stockout risk at one site and excess at another — preferring transfer before new procurement. |
| **Context** | Network Transfer, Inventory Balance |
| **Related Terms** | Transfer Request, Stock Transfer, Network Availability |
| **Terms That Should Never Be Confused** | **Replenishment** — restocking from external supplier, not internal redistribution; **Stock Adjustment** — quantity correction, not planned movement |

---

## Section 9: Inventory Accuracy (IA)

---

### Cycle Count

| Field | Detail |
|-------|--------|
| **Definition** | A scheduled partial physical count of selected products or locations on a rotating basis, performed blind (counter not shown system quantity) without full warehouse shutdown. |
| **Context** | Inventory Accuracy |
| **Related Terms** | Count Variance, Physical Inventory Count, ABC Classification |
| **Terms That Should Never Be Confused** | **Physical Inventory Count** — full wall-to-wall count with location freeze, not partial rotation; **Goods Receipt** — inbound verification, not accuracy audit |

---

### Physical Inventory Count

| Field | Detail |
|-------|--------|
| **Definition** | A comprehensive wall-to-wall count of all products at a location, imposing location freeze until certified complete — establishing an authoritative accuracy baseline. |
| **Context** | Inventory Accuracy, Warehouse Network |
| **Related Terms** | Location Freeze, Count Variance, Cycle Count |
| **Terms That Should Never Be Confused** | **Cycle Count** — partial rotating count without full shutdown; **Opening Balance** — initial stock at go-live, not periodic audit |

---

### Count Variance

| Field | Detail |
|-------|--------|
| **Definition** | An identified difference between system-recorded quantity and physically counted quantity, requiring investigation and independent approval before any Stock Adjustment is applied. |
| **Context** | Inventory Accuracy |
| **Related Terms** | Cycle Count, Physical Inventory Count, Stock Adjustment, Segregation of Duties |
| **Terms That Should Never Be Confused** | **Receipt Discrepancy** — expected vs. received at supplier inbound, not system vs. physical during count; **Stock Adjustment** — authorized correction, not the discovered discrepancy |

---

### Stock Adjustment

| Field | Detail |
|-------|--------|
| **Definition** | An authorized correction to recorded inventory quantity with mandatory reason code — increasing or decreasing on-hand to align record with physical reality after investigation. |
| **Context** | Inventory Accuracy, Inventory Balance |
| **Related Terms** | Reason Code, Count Variance, Inventory Write-Off |
| **Terms That Should Never Be Confused** | **Inventory Write-Off** — permanent value removal, not reversible correction; **Stock Transfer** — movement between locations, not quantity correction; **Reservation** — customer hold, not record correction |

---

### Inventory Write-Off

| Field | Detail |
|-------|--------|
| **Definition** | The formal, authorized permanent removal of inventory quantity and value for damaged, obsolete, expired, or lost goods — distinct from reversible adjustment. |
| **Context** | Inventory Accuracy, Inventory Balance |
| **Related Terms** | Reason Code, Stock Adjustment, Shrinkage, Return Disposition |
| **Terms That Should Never Be Confused** | **Stock Adjustment** — record correction that may increase or decrease, not terminal removal; **Return Disposition (Write-Off)** — write-off of returned goods specifically; **Product Discontinued** — commercial exit, not physical removal |

---

### Shrinkage

| Field | Detail |
|-------|--------|
| **Definition** | Unexplained or unaccounted inventory loss from theft, damage, misplacement, or process error — analyzed through reason-coded adjustments and write-offs over time. |
| **Context** | Inventory Accuracy, Inventory Intelligence |
| **Related Terms** | Stock Adjustment, Inventory Write-Off, Reason Code, Inventory Accuracy |
| **Terms That Should Never Be Confused** | **Count Variance** — specific discovered discrepancy at count time, not ongoing loss trend; **Write-Off** — individual removal event, not the aggregate loss pattern |

---

### Inventory Accuracy

| Field | Detail |
|-------|--------|
| **Definition** | The degree of agreement between system-recorded quantities and physically counted stock, measured through cycle counts and physical inventory counts — expressed as a percentage or variance rate. |
| **Context** | Inventory Accuracy, Inventory Intelligence |
| **Related Terms** | Cycle Count, Count Variance, Physical Inventory Count |
| **Terms That Should Never Be Confused** | **Fill Rate** — order fulfillment performance, not record-vs-physical agreement; **Inventory Turnover** — velocity of stock movement, not accuracy |

---

## Section 10: Returns Management (RM)

---

### Return Authorization (RMA)

| Field | Detail |
|-------|--------|
| **Definition** | Approved permission for a customer to return specified products, linked to the original customer order and return policy, before the warehouse accepts physical return. |
| **Context** | Returns Management |
| **Related Terms** | Customer Return, Customer Order, Return Disposition |
| **Terms That Should Never Be Confused** | **Customer Return** — physical receipt of goods, after RMA issued; **Purchase Order** — inbound from supplier, not customer return; **Backorder** — fulfillment delay, not return permission |

---

### Customer Return

| Field | Detail |
|-------|--------|
| **Definition** | The physical receipt of customer-returned goods at a warehouse, verified against a valid Return Authorization, initiating inspection and disposition workflow. |
| **Context** | Returns Management |
| **Related Terms** | Return Authorization, Return Disposition, Goods Receipt |
| **Terms That Should Never Be Confused** | **Goods Receipt** — supplier inbound, not customer return; **Return Authorization** — permission to return, not physical arrival; **Shipment** — outbound to customer, opposite direction |

---

### Return Disposition

| Field | Detail |
|-------|--------|
| **Definition** | The business outcome decision for returned goods after condition inspection: **Restock** (return to sellable inventory), **Quarantine** (further investigation), or **Write-Off** (permanent removal). |
| **Context** | Returns Management |
| **Related Terms** | Customer Return, Condition Grade, Quarantine Hold, Inventory Write-Off |
| **Terms That Should Never Be Confused** | **Reason Code** — categorized explanation for adjustments generally, not return-specific outcome; **Stock Adjustment** — quantity correction mechanism, not inspection decision |

---

### Condition Grade

| Field | Detail |
|-------|--------|
| **Definition** | The assessed physical and resale condition of received or returned goods at inspection — determining whether restock, quarantine, or write-off disposition applies. |
| **Context** | Returns Management, Inbound Receiving |
| **Related Terms** | Return Disposition, Goods Receipt, Receipt Discrepancy |
| **Terms That Should Never Be Confused** | **Reason Code** — why an adjustment occurred, not product condition assessment; **Product Lifecycle Status** — active/discontinued, not physical condition |

---

## Section 11: Commercial Campaign (CC)

---

### Promotional Stock Allocation

| Field | Detail |
|-------|--------|
| **Definition** | A defined quantity of inventory ring-fenced for a specific promotional campaign or product launch, excluded from general ATP for non-approved orders during the campaign period. |
| **Context** | Commercial Campaign |
| **Related Terms** | Campaign Period, Channel Designation, Inventory Reservation |
| **Terms That Should Never Be Confused** | **Inventory Reservation** — hold for specific customer order, not campaign pool; **Safety Stock** — uncertainty buffer, not commercial ring-fence; **Stock Policy Maximum** — overstock limit, not campaign allocation |

---

### Campaign Period

| Field | Detail |
|-------|--------|
| **Definition** | The bounded date range during which promotional stock allocation is active and protected from non-promotional consumption. |
| **Context** | Commercial Campaign |
| **Related Terms** | Promotional Stock Allocation, Promotional Readiness |
| **Terms That Should Never Be Confused** | **Lead Time** — supply timing, not marketing campaign window; **Effective Period (Governance Policy)** — policy validity dates, not campaign dates |

---

### Promotional Readiness

| Field | Detail |
|-------|--------|
| **Definition** | Confirmation that ring-fenced promotional inventory is sufficient and available at fulfillment locations before campaign or launch commitment deadline. |
| **Context** | Commercial Campaign, Inventory Intelligence |
| **Related Terms** | Promotional Stock Allocation, Operational Alert |
| **Terms That Should Never Be Confused** | **Available-to-Promise** — general sellable quantity, not campaign-specific readiness; **Inbound Expected** — supplier pipeline, not campaign stock confirmation |

---

## Section 12: Identity & Access (IAc)

---

### User Account

| Field | Detail |
|-------|--------|
| **Definition** | An identified individual authorized to perform inventory operations, carrying role assignments and location scope for accountability on all transactions. |
| **Context** | Identity & Access |
| **Related Terms** | Role Assignment, Segregation of Duties, Audit Trail |
| **Terms That Should Never Be Confused** | **Supplier** — external vendor, not system user; **Customer** — external buyer, not internal operator; **Actor (BRD)** — business role concept, User Account is the system identity |

---

### Role Assignment

| Field | Detail |
|-------|--------|
| **Definition** | The delegation of business permissions to a user account — specifying role (e.g., Receiving Clerk, Warehouse Manager) and authorized location scope. |
| **Context** | Identity & Access |
| **Related Terms** | User Account, Segregation of Duties, Inventory Location |
| **Terms That Should Never Be Confused** | **Job Title** — HR designation, not system permission set; **Actor** — business process participant, not access control record |

---

## Section 13: Inventory Intelligence (II)

---

### Inventory Movement Record

| Field | Detail |
|-------|--------|
| **Definition** | An immutable operational record of a single inventory quantity or status change — capturing product, location, quantity, direction, movement type, reason, user, and timestamp. |
| **Context** | Inventory Intelligence |
| **Related Terms** | Audit Trail, Stock Position, Shipment, Goods Receipt |
| **Terms That Should Never Be Confused** | **Audit Trail Record** — governance-grade before/after with approval chain, richer than operational movement; **Stock Transfer** — specific movement type, not the log concept; **Transaction** — technical term, avoid in business conversation |

---

### Audit Trail Record

| Field | Detail |
|-------|--------|
| **Definition** | A governance-grade immutable record of a material inventory change including user identity, role at time of action, before/after state, and approval chain — supporting compliance and control testing. |
| **Context** | Inventory Intelligence |
| **Related Terms** | Inventory Movement Record, Segregation of Duties, Governance Policy |
| **Terms That Should Never Be Confused** | **Inventory Movement Record** — operational history of quantity changes, not necessarily full governance metadata; **System Log** — technical diagnostic output, not business audit evidence |

---

### Operational Alert

| Field | Detail |
|-------|--------|
| **Definition** | A proactive notification of a business condition requiring human review — such as low stock, pending approval, transfer exception, inbound delay, or campaign readiness gap. |
| **Context** | Inventory Intelligence |
| **Related Terms** | Stock Status Indicator, Replenishment, Transfer Request |
| **Terms That Should Never Be Confused** | **Stock Status Indicator** — classification (low stock), not the notification itself; **Business Rule** — policy definition, not triggered alert instance |

---

### Inventory Valuation Snapshot

| Field | Detail |
|-------|--------|
| **Definition** | A point-in-time summary of owned inventory value by product and location for finance reconciliation against the general ledger — excluding consignment, quarantined, and in-transit stock per policy. |
| **Context** | Inventory Intelligence |
| **Related Terms** | Three-Way Match, Consignment Stock, Inventory Write-Off |
| **Terms That Should Never Be Confused** | **On-Hand Stock** — operational quantity, not financial value; **Supplier Invoice** — supplier bill for specific receipt, not period-end valuation; **Inventory Turnover** — velocity metric, not point-in-time value |

---

### Replenishment

| Field | Detail |
|-------|--------|
| **Definition** | The business process of restocking products to maintain target inventory levels — triggered at reorder level through purchase requisition, transfer request, or network rebalancing. |
| **Context** | Inventory Balance, Procurement & Supplier, Network Transfer |
| **Related Terms** | Reorder Level, Purchase Requisition, Transfer Request, Low Stock |
| **Terms That Should Never Be Confused** | **Purchase Order** — one replenishment mechanism (external buy), not the entire process; **Put-Away** — inbound storage step, not replenishment planning |

---

### Fill Rate

| Field | Detail |
|-------|--------|
| **Definition** | The percentage of customer order lines fulfilled in full on the first shipment — a fulfillment performance KPI, not an inventory quantity measure. |
| **Context** | Inventory Intelligence, Order Fulfillment |
| **Related Terms** | Partial Fulfillment, Shipment, Customer Order |
| **Terms That Should Never Be Confused** | **Inventory Accuracy** — record vs. physical agreement, not order fulfillment performance; **Available-to-Promise** — current quotable quantity, not historical performance metric |

---

### Inventory Turnover

| Field | Detail |
|-------|--------|
| **Definition** | A financial performance metric expressing how quickly inventory is sold and replaced — cost of goods sold divided by average inventory value over a period. |
| **Context** | Inventory Intelligence |
| **Related Terms** | Inventory Valuation Snapshot, Carrying Cost |
| **Terms That Should Never Be Confused** | **Inventory Movement Record** — transaction history, not velocity metric; **Fill Rate** — order fulfillment completeness, not stock rotation speed |

---

## Section 14: Cross-Context Published Language (ALL)

These identifiers are shared across all bounded contexts as the **Published Language** for cross-context references.

---

### Location Code

| Field | Detail |
|-------|--------|
| **Definition** | The unique business identifier for an Inventory Location, used by all contexts to anchor stock, transactions, and authorization scope to a physical site. |
| **Context** | All contexts |
| **Related Terms** | Inventory Location, Storage Position, Stock Position |
| **Terms That Should Never Be Confused** | **Storage Position Code** — identifier within a location, not the location itself; **Supplier Code** — external vendor identifier |

---

### Product SKU Reference

| Field | Detail |
|-------|--------|
| **Definition** | The cross-context reference to a Product by SKU — the standard way all contexts identify *what* product is involved without embedding full product master data. |
| **Context** | All contexts |
| **Related Terms** | SKU, Product, Stock Position |
| **Terms That Should Never Be Confused** | **Barcode** — lookup identifier that resolves to SKU, not the canonical key itself; **Lot/Batch Number** — traceability sub-identity within a SKU |

---

## Critical Distinction Reference

High-risk confusions that cause operational and financial errors if terminology is mixed:

| Never Confuse | With | Key Difference |
|---------------|------|----------------|
| **Available-to-Promise (ATP)** | On-Hand Stock | ATP excludes reserved and quarantined; on-hand is total physical |
| **Available-to-Promise (ATP)** | Inbound Expected | Inbound is pipeline information; ATP is physically available now |
| **Goods Receipt** | Put-Away | Receipt verifies at dock; put-away confirms storage placement |
| **Put-Away** | Stock Received | Put-away is the action; stock received is the balance outcome |
| **Inventory Reservation** | Backorder | Reservation holds existing stock; backorder agrees to wait for unavailable quantity |
| **Inventory Reservation** | Promotional Allocation | Reservation is order-specific; allocation is campaign ring-fence |
| **Stock Adjustment** | Inventory Write-Off | Adjustment corrects record; write-off permanently removes value |
| **Stock Adjustment** | Stock Transfer | Adjustment changes quantity in place; transfer moves between locations |
| **Count Variance** | Receipt Discrepancy | Variance is system vs. physical at count; discrepancy is expected vs. received at inbound |
| **Purchase Requisition** | Purchase Order | Requisition is internal approval request; PO is supplier commitment |
| **Purchase Order** | Customer Order | PO is inbound from supplier; customer order is outbound demand |
| **Transfer Request** | Stock Transfer | Request is intent pending approval; transfer is executing movement |
| **Shipment** | Stock Transfer | Shipment goes to customer; transfer goes between owned locations |
| **Cycle Count** | Physical Inventory Count | Cycle count is partial rotation; physical count is full wall-to-wall with freeze |
| **Quarantine Hold** | Location Freeze | Hold excludes specific stock from ATP; freeze suspends all location activity |
| **Quarantine Hold** | Reserved Stock | Hold is quality/regulatory exclusion; reserved is customer commitment |
| **Bonded Inventory** | Consignment Stock | Bonded is customs-controlled; consignment is supplier-owned until consumption |
| **Reason Code** | Disposition Decision | Reason code categorizes why; disposition decides return outcome |
| **Stock Policy** | Governance Policy | Stock policy is replenishment thresholds; governance is enterprise control rules |
| **Product Lifecycle Status** | Stock Status Indicator | Lifecycle is active/discontinued; status indicator is in/low/out of stock |
| **Return Authorization** | Customer Return | RMA is permission; customer return is physical receipt |
| **Three-Way Match** | Valuation Reconciliation | Three-way match is PO-receipt-invoice; valuation is operational stock vs. GL |
| **Inventory Movement Record** | Audit Trail Record | Movement is operational log; audit trail adds governance before/after and approval |
| **Fill Rate** | Inventory Accuracy | Fill rate is order fulfillment KPI; accuracy is record vs. physical agreement |

---

## Term Index (Alphabetical)

| Term | Context | Section |
|------|---------|---------|
| ABC Classification | Product Catalog | 1 |
| Approval Threshold | Inventory Governance | 3 |
| Audit Trail Record | Inventory Intelligence | 13 |
| Available-to-Promise (ATP) | Inventory Balance | 4 |
| Backorder | Order Fulfillment | 7 |
| Bonded Inventory | Inventory Balance | 4 |
| Campaign Period | Commercial Campaign | 11 |
| Condition Grade | Returns Management | 10 |
| Consignment Stock | Inventory Balance | 4 |
| Count Variance | Inventory Accuracy | 9 |
| Customer Order | Order Fulfillment | 7 |
| Customer Return | Returns Management | 10 |
| Cycle Count | Inventory Accuracy | 9 |
| Expected Inbound Delivery | Procurement & Supplier | 5 |
| Fill Rate | Inventory Intelligence | 13 |
| Fulfillment Execution | Order Fulfillment | 7 |
| Goods Receipt | Inbound Receiving | 6 |
| Governance Policy | Inventory Governance | 3 |
| In-Transit Stock | Network Transfer | 8 |
| Inventory Accuracy | Inventory Accuracy | 9 |
| Inventory Location | Warehouse Network | 2 |
| Inventory Movement Record | Inventory Intelligence | 13 |
| Inventory Reservation | Order Fulfillment | 7 |
| Inventory Turnover | Inventory Intelligence | 13 |
| Inventory Valuation Snapshot | Inventory Intelligence | 13 |
| Inventory Write-Off | Inventory Accuracy | 9 |
| Lead Time | Procurement & Supplier | 5 |
| Location Code | All contexts | 14 |
| Location Freeze | Warehouse Network | 2 |
| Lot/Batch | Inventory Balance | 4 |
| Minimum Remaining Shelf Life (MRSL) | Inbound Receiving | 6 |
| Multi-Location Split Fulfillment | Order Fulfillment | 7 |
| Network Rebalancing | Network Transfer | 8 |
| On-Hand Stock | Inventory Balance | 4 |
| Operational Alert | Inventory Intelligence | 13 |
| Ownership Classification | Inventory Balance | 4 |
| Partial Fulfillment | Order Fulfillment | 7 |
| Physical Inventory Count | Inventory Accuracy | 9 |
| Pick Verification | Order Fulfillment | 7 |
| Product | Product Catalog | 1 |
| Product Lifecycle Status | Product Catalog | 1 |
| Promotional Readiness | Commercial Campaign | 11 |
| Promotional Stock Allocation | Commercial Campaign | 11 |
| Purchase Order (PO) | Procurement & Supplier | 5 |
| Purchase Requisition | Procurement & Supplier | 5 |
| Put-Away | Inbound Receiving | 6 |
| Quarantine Hold | Inventory Balance | 4 |
| Reason Code | Inventory Governance | 3 |
| Receipt Discrepancy | Inbound Receiving | 6 |
| Replenishment | Multiple | 13 |
| Reorder Level | Inventory Balance | 4 |
| Reserved Stock | Inventory Balance | 4 |
| Return Authorization (RMA) | Returns Management | 10 |
| Return Disposition | Returns Management | 10 |
| Role Assignment | Identity & Access | 12 |
| Rotation Policy | Product Catalog | 1 |
| Safety Stock | Inventory Balance | 4 |
| Segregation of Duties (SoD) | Inventory Governance | 3 |
| Shipment | Order Fulfillment | 7 |
| Shrinkage | Inventory Accuracy | 9 |
| SKU | Product Catalog | 1 |
| Stock Adjustment | Inventory Accuracy | 9 |
| Stock Policy | Inventory Balance | 4 |
| Stock Position | Inventory Balance | 4 |
| Stock Status Indicator | Inventory Balance | 4 |
| Stock Transfer | Network Transfer | 8 |
| Storage Position | Warehouse Network | 2 |
| Supplier | Procurement & Supplier | 5 |
| Supplier Invoice | Inbound Receiving | 6 |
| Three-Way Match | Inbound Receiving | 6 |
| Transfer Request | Network Transfer | 8 |
| Unit of Measure (UOM) | Product Catalog | 1 |
| User Account | Identity & Access | 12 |

**Total Terms:** 72

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| Senior Business Analyst | | | |
| Product Owner | | | |
| Inventory Controller | | | |

---

*End of Ubiquitous Language*

*Document ID: SRS-DM-008 | Version 1.0 | July 5, 2026*
