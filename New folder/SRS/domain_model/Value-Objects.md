# Domain Value Objects
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DM-002 |
| **Document Title** | Domain Value Objects — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | BRD-IMS-001 (v1.0), SRS-DM-001 (Domain Entity Model, v1.0), SRS-BR-001 (Business Rules, v1.0), SRS-UC-001 (Use Case Catalog, v1.0) |
| **Date** | July 5, 2026 |
| **Scope** | Immutable business concepts only — no database columns, API payloads, or implementation detail |

### Purpose

This document identifies **Value Objects** in the Inventory Management System domain. A value object is a business concept defined entirely by its attribute values, with no independent identity or lifecycle. Two instances with the same values are interchangeable. When business meaning changes, the value object is replaced — not mutated.

This catalog complements **SRS-DM-001 (Domain Entity Model)**, which documents entities that carry identity and lifecycle.

### Value Object vs. Entity — Quick Reference

| Characteristic | Entity | Value Object |
|----------------|--------|--------------|
| Identity | Has a unique business identifier | No identity — equality by value |
| Mutability | Lifecycle with state changes | Immutable — replace when values change |
| Example | Purchase Order (PO-2026-0042) | Monetary Amount ($12.50 USD) |

### Value Object Domain Map

| Domain | Value Objects |
|--------|---------------|
| **Measurement & Quantity** | Quantity, Unit of Measure, Monetary Amount, Lead Time Duration |
| **Product & Classification** | Product Identifier, Product Category, Product Lifecycle Status, ABC Classification, Rotation Policy, Shelf Life Profile |
| **Stock & Availability** | Stock Availability Breakdown, Stock Status Indicator, Ownership Classification, Stock Threshold Set |
| **Location & Address** | Physical Address, Storage Position Address, Location Type |
| **Time & Period** | Effective Period, Campaign Period |
| **Transaction Lines** | Purchase Order Line, Order Line Quantity, Receipt Line Detail, Transfer Line Detail, Invoice Line Detail, Shipment Line Detail, Pick Line Detail, Requisition Line Detail |
| **Variance & Inspection** | Quantity Variance, Condition Grade, Discrepancy Classification, Disposition Decision |
| **Governance & Control** | Reason Code Attribution, Approval Threshold, Quantity Tolerance, Three-Way Match Result, User Action Attribution, Audit Quantity Snapshot |
| **Fulfillment & Commercial** | Fulfillment Quantity Breakdown, Customer Acknowledgment, Channel Designation, Payment Terms |
| **Movement & Status** | Movement Classification, Hold Reason Classification, Alert Priority |
| **Financial & Traceability** | Valuation Line Amount, Lot Identity |

**Total Value Objects:** 46

---

## Domain 1: Measurement & Quantity

---

### 1. Quantity

| Aspect | Detail |
|--------|--------|
| **Definition** | A non-negative numeric amount of a product expressed in a specific unit of measure. Quantity is the fundamental measure for all inventory balances, movements, orders, and counts. |
| **Why It Is a Value Object** | A quantity of "50 Each" has no identity of its own — only meaning through its numeric amount and unit. Two quantities with the same amount and unit are identical. When count changes, a new quantity replaces the old one rather than mutating it in place. |
| **Attributes** | Amount (non-negative number), unit of measure |
| **Related Entities** | Stock Position, Goods Receipt, Shipment, Stock Adjustment, Inventory Reservation, Cycle Count, Count Variance, Purchase Order, Customer Order |
| **Example** | `Quantity(50, Each)` — fifty units of a product counted, ordered, or moved |

---

### 2. Unit of Measure

| Aspect | Detail |
|--------|--------|
| **Definition** | The standard unit in which a product is counted, ordered, stored, and sold — such as Each, Case, Pallet, Kilogram, or Liter. |
| **Why It Is a Value Object** | UOM is a classification label with no lifecycle. "Case" means the same regardless of where it appears. It is defined by its code and description, not by a unique identifier. |
| **Attributes** | UOM code, display name, base-unit indicator (whether this is the product's primary counting unit) |
| **Related Entities** | Product, Quantity (embedded), Purchase Order Line, Order Line Quantity |
| **Example** | `UnitOfMeasure(CS, Case, baseUnit=false)` — one case as a ordering unit distinct from the each-level base unit |

---

### 3. Monetary Amount

| Aspect | Detail |
|--------|--------|
| **Definition** | A monetary value expressed as an amount in a specific currency, used for purchase pricing, invoice matching, adjustment valuation, and write-off financial impact. |
| **Why It Is a Value Object** | "$1,250.00 USD" has no independent identity — it is fully defined by amount and currency. Arithmetic and comparison operate on values; changing amount creates a new monetary amount. |
| **Attributes** | Amount (decimal), currency code (e.g., USD, EUR) |
| **Related Entities** | Purchase Order, Supplier Invoice, Inventory Write-Off, Stock Adjustment, Inventory Valuation Snapshot, Approval Threshold |
| **Example** | `MonetaryAmount(1250.00, USD)` — extended line value on a purchase order |

---

### 4. Lead Time Duration

| Aspect | Detail |
|--------|--------|
| **Definition** | The elapsed business time assumed between placing a replenishment order and having goods available for sale or use at a location. |
| **Why It Is a Value Object** | Lead time is a planning assumption defined by its duration value and unit — not tracked as a separate business object. Replacing "14 days" with "21 days" means replacing the whole value. |
| **Attributes** | Duration value (positive integer), duration unit (business days / calendar days), source (supplier default / product-specific / location override) |
| **Related Entities** | Stock Policy, Supplier, Purchase Order, Expected Inbound Delivery |
| **Example** | `LeadTimeDuration(14, businessDays, supplierDefault)` — two-week supplier lead time for replenishment planning |

---

## Domain 2: Product & Classification

---

### 5. Product Identifier

| Aspect | Detail |
|--------|--------|
| **Definition** | A typed product lookup code — SKU, barcode, or alternate identifier — used to reference a product in operational transactions without carrying full product master data. |
| **Why It Is a Value Object** | The identifier string "SKU-8842" paired with type "SKU" is a value tuple. It identifies a product concept but has no lifecycle separate from the Product entity it references. |
| **Attributes** | Identifier type (SKU / barcode / alternate), identifier value (non-empty string) |
| **Related Entities** | Product, Goods Receipt, Fulfillment Execution, Cycle Count, Customer Return |
| **Example** | `ProductIdentifier(SKU, SKU-8842)` — scanned or entered at receiving dock to match purchase order line |

---

### 6. Product Category

| Aspect | Detail |
|--------|--------|
| **Definition** | A business grouping label that classifies products for reporting, filtering, and operational segmentation. |
| **Why It Is a Value Object** | Category is defined by its code and name. "Electronics" is the same category wherever referenced; renaming creates a new category value applied going forward. |
| **Attributes** | Category code, category name, parent category code (optional, for hierarchy) |
| **Related Entities** | Product, Inventory Valuation Snapshot, Operational Alert (filtering scope) |
| **Example** | `ProductCategory(ELEC, Electronics)` — classifies a product for dashboard filtering |

---

### 7. Product Lifecycle Status

| Aspect | Detail |
|--------|--------|
| **Definition** | The current commercial availability state of a product: active (orderable and fulfillable), inactive (not sold but may hold stock), or discontinued (exit from assortment, no reorder). |
| **Why It Is a Value Object** | Status is an enumerated business state without its own identity. `Active` equals `Active` everywhere. Transition from active to discontinued replaces the status value on the Product entity. |
| **Attributes** | Status value (active / inactive / discontinued) |
| **Related Entities** | Product, Purchase Order, Purchase Requisition, Inventory Reservation, Customer Order |
| **Example** | `ProductLifecycleStatus(discontinued)` — blocks new purchase requisitions per BR-027 |

---

### 8. ABC Classification

| Aspect | Detail |
|--------|--------|
| **Definition** | A priority segment (A, B, or C) assigned to a product based on business importance — revenue contribution, velocity, or criticality — to prioritize operational effort. |
| **Why It Is a Value Object** | Class "A" is a label with fixed meaning across the catalog. It has no identity beyond its letter value and the classification criteria snapshot may accompany it. |
| **Attributes** | Class value (A / B / C), classification basis note (optional: revenue / velocity / criticality) |
| **Related Entities** | Product, Cycle Count, Operational Alert, Stock Policy |
| **Example** | `ABCClassification(A, revenue)` — triggers highest cycle count frequency per BR-032 |

---

### 9. Rotation Policy

| Aspect | Detail |
|--------|--------|
| **Definition** | The required stock rotation discipline for a product: FIFO (first-in, first-out) for standard goods or FEFO (first-expired, first-out) for shelf-life products. |
| **Why It Is a Value Object** | Rotation policy is a rule classification with no independent existence. Two products both assigned `FEFO` share the same policy value. |
| **Attributes** | Policy type (FIFO / FEFO), shelf-life applicability indicator |
| **Related Entities** | Product, Put-Away, Fulfillment Execution, Storage Position |
| **Example** | `RotationPolicy(FEFO, shelfLifeApplicable=true)` — pick instructions prioritize earliest expiration per BR-014 |

---

### 10. Shelf Life Profile

| Aspect | Detail |
|--------|--------|
| **Definition** | A point-in-time capture of shelf-life attributes for a received or held lot — expiration date, manufacture date, and remaining shelf life at receipt — used to enforce MRSL and FEFO decisions. |
| **Why It Is a Value Object** | The tuple of dates and remaining days at a specific moment is immutable fact. When re-measured, a new profile replaces the prior snapshot. It describes condition, not a tracked object. |
| **Attributes** | Expiration date, manufacture date (optional), remaining shelf life in days (at capture point), MRSL policy threshold in days |
| **Related Entities** | Lot/Batch, Goods Receipt, Receipt Line Detail, Receipt Discrepancy, Fulfillment Execution |
| **Example** | `ShelfLifeProfile(expiration=2026-12-01, remainingDays=180, mrslThreshold=90)` — passes MRSL check at receipt per BR-016 |

---

## Domain 3: Stock & Availability

---

### 11. Stock Availability Breakdown

| Aspect | Detail |
|--------|--------|
| **Definition** | The decomposed view of inventory quantity at a point in time showing on-hand, reserved, available-to-promise (ATP), and optionally inbound expected — each as distinct quantity components. |
| **Why It Is a Value Object** | The breakdown is a computed snapshot defined entirely by its component quantities. Two breakdowns with identical components represent the same availability state. ATP is derived, not independently identified. |
| **Attributes** | On-hand quantity, reserved quantity, ATP quantity, inbound expected quantity (optional), quarantined quantity (optional) |
| **Related Entities** | Stock Position, Customer Order, Inventory Reservation, Operational Alert |
| **Example** | `StockAvailabilityBreakdown(onHand=100, reserved=30, atp=65, quarantined=5)` — 65 units quotable to new customers per BR-001 |

---

### 12. Stock Status Indicator

| Aspect | Detail |
|--------|--------|
| **Definition** | A derived classification of inventory health for a product at a location: in stock, low stock, out of stock, or overstock — based on comparison against stock policy thresholds. |
| **Why It Is a Value Object** | The indicator is a computed label with no identity. `Low Stock` at one moment is replaced by `Out of Stock` when thresholds are crossed — a new value, not a mutation. |
| **Attributes** | Status value (inStock / lowStock / outOfStock / overstock), evaluated against threshold reference (optional) |
| **Related Entities** | Stock Position, Stock Policy, Operational Alert |
| **Example** | `StockStatusIndicator(lowStock, reorderLevel)` — triggers replenishment alert per BR-009 |

---

### 13. Ownership Classification

| Aspect | Detail |
|--------|--------|
| **Definition** | The legal and financial ownership state of held inventory: owned (organization asset), consignment (supplier-owned until consumption), or bonded (customs-controlled until clearance). |
| **Why It Is a Value Object** | Ownership type is an enumerated classification without lifecycle. It determines valuation and availability rules but is not itself a trackable business object. |
| **Attributes** | Ownership type (owned / consignment / bonded), ownership transfer trigger (for consignment: consumption / sale / issue) |
| **Related Entities** | Stock Position, Quarantine Hold, Goods Receipt, Inventory Valuation Snapshot |
| **Example** | `OwnershipClassification(consignment, transferOnConsumption)` — excluded from owned valuation until consumption per BR-031 |

---

### 14. Stock Threshold Set

| Aspect | Detail |
|--------|--------|
| **Definition** | The replenishment policy limits for a product at a location: reorder level, minimum threshold, safety stock buffer, and maximum (overstock) level. |
| **Why It Is a Value Object** | Thresholds are a coherent set of numeric limits that define policy at a point in time. When recalibrated, the entire set is replaced with a new effective threshold set — preserving history as immutable snapshots. |
| **Attributes** | Reorder level (quantity), minimum threshold (quantity), safety stock (quantity), maximum level (quantity) |
| **Related Entities** | Stock Policy, Stock Position, Transfer Request, Operational Alert |
| **Example** | `StockThresholdSet(reorder=50, minimum=20, safety=15, maximum=200)` — reorder action triggers when ATP reaches 50 |

---

## Domain 4: Location & Address

---

### 15. Physical Address

| Aspect | Detail |
|--------|--------|
| **Definition** | The geographic address of an inventory location used for logistics, regional reporting, and network hierarchy grouping. |
| **Why It Is a Value Object** | An address is defined by its component lines and region. Correcting a postal code replaces the address value — it has no independent business identity. |
| **Attributes** | Street lines, city, state or region, postal code, country |
| **Related Entities** | Inventory Location, Supplier |
| **Example** | `PhysicalAddress(100 Warehouse Blvd, Dallas, TX, 75201, US)` — regional grouping for network reporting |

---

### 16. Storage Position Address

| Aspect | Detail |
|--------|--------|
| **Definition** | The within-location address of a storage area — zone, aisle, bin, or shelf — where stock is physically placed after put-away. |
| **Why It Is a Value Object** | "Zone A / Aisle 3 / Bin 12" is a composite location value with no lifecycle. Two pickers directed to the same address are going to the same place. |
| **Attributes** | Zone, aisle, bin/shelf, storage type (bulk / pickFace / quarantine / bonded) |
| **Related Entities** | Storage Position, Put-Away, Fulfillment Execution, Cycle Count |
| **Example** | `StoragePositionAddress(zone=A, aisle=3, bin=12, type=pickFace)` — pick path destination for order line |

---

### 17. Location Type

| Aspect | Detail |
|--------|--------|
| **Definition** | The operational classification of an inventory location: warehouse, store, or distribution point — determining its role in the network. |
| **Why It Is a Value Object** | Location type is a fixed enumeration. "Warehouse" carries the same business meaning across all locations of that type. |
| **Attributes** | Type value (warehouse / store / distributionPoint) |
| **Related Entities** | Inventory Location |
| **Example** | `LocationType(warehouse)` — central fulfillment site in the distribution network |

---

## Domain 5: Time & Period

---

### 18. Effective Period

| Aspect | Detail |
|--------|--------|
| **Definition** | A bounded date range during which a business policy, threshold set, or governance rule is in force. |
| **Why It Is a Value Object** | A period from July 1 to September 30 is defined by its start and end dates. Changing the end date creates a new period value; historical periods remain immutable records. |
| **Attributes** | Start date, end date (optional — open-ended if null), period label (optional) |
| **Related Entities** | Stock Policy, Governance Policy, Promotional Stock Allocation, Role Assignment |
| **Example** | `EffectivePeriod(2026-07-01, 2026-09-30, Q3-2026 Policy)` — stock threshold set valid for one quarter |

---

### 19. Campaign Period

| Aspect | Detail |
|--------|--------|
| **Definition** | The bounded date range and commercial scope of a promotional campaign or product launch during which ring-fenced inventory is protected. |
| **Why It Is a Value Object** | Campaign timing is a commercial fact defined by dates and name. It has no identity separate from the promotional allocation entity that references it. |
| **Attributes** | Campaign name, start date, end date, channel scope reference |
| **Related Entities** | Promotional Stock Allocation, Operational Alert, Customer Order |
| **Example** | `CampaignPeriod(Summer Sale 2026, 2026-06-01, 2026-08-31, eCommerce)` — ring-fenced stock protected per BR-029 |

---

## Domain 6: Transaction Lines

Transaction line value objects represent immutable product-quantity-price tuples embedded within document entities. They carry no independent identity — line sequence provides ordering context only.

---

### 20. Purchase Order Line

| Aspect | Detail |
|--------|--------|
| **Definition** | A single product line on a purchase order specifying ordered quantity, unit price, and expected receipt quantity tracking. |
| **Why It Is a Value Object** | PO line meaning is fully defined by product, quantity, and price. Amending a line replaces it with a new line value; the tuple "Product X, 100 units, $5.00" has no identity beyond its content. |
| **Attributes** | Product identifier, ordered quantity, unit price (monetary amount), received quantity to date, line status (open / partial / closed) |
| **Related Entities** | Purchase Order, Goods Receipt, Supplier Invoice, Expected Inbound Delivery |
| **Example** | `PurchaseOrderLine(SKU-4420, Quantity(100, Each), $5.00 USD, received=60, partial)` — open PO line awaiting balance receipt |

---

### 21. Requisition Line Detail

| Aspect | Detail |
|--------|--------|
| **Definition** | A product and requested quantity on an internal purchase requisition before commercial PO creation. |
| **Why It Is a Value Object** | The requisition line is a need statement — product plus quantity — with no independent lifecycle. Approval converts it to a PO line value. |
| **Attributes** | Product identifier, requested quantity, target location, requested delivery date |
| **Related Entities** | Purchase Requisition, Purchase Order, Operational Alert |
| **Example** | `RequisitionLineDetail(SKU-4420, Quantity(200, Each), WH-DALLAS, 2026-07-15)` — replenishment need from low-stock alert |

---

### 22. Receipt Line Detail

| Aspect | Detail |
|--------|--------|
| **Definition** | A verified inbound line recording product, received quantity, condition assessment, and optional lot identity captured at goods receipt. |
| **Why It Is a Value Object** | What was received is an immutable fact at receipt time. Correcting a receipt creates a new receipt line value or adjustment — the original received tuple remains historical truth. |
| **Attributes** | Product identifier, received quantity, condition grade, lot identity (optional), shelf life profile (optional), verification outcome (accepted / rejected / hold) |
| **Related Entities** | Goods Receipt, Receipt Discrepancy, Put-Away, Lot/Batch |
| **Example** | `ReceiptLineDetail(SKU-4420, Quantity(98, Each), good, LotIdentity(L20260701), accepted)` — two units short triggers discrepancy |

---

### 23. Order Line Quantity

| Aspect | Detail |
|--------|--------|
| **Definition** | The quantity breakdown for a customer order line showing requested, reserved, fulfilled, and backordered amounts. |
| **Why It Is a Value Object** | Line quantities at a snapshot moment are a value decomposition. As fulfillment progresses, new quantity breakdown values replace prior ones. |
| **Attributes** | Product identifier, requested quantity, reserved quantity, fulfilled quantity, backordered quantity |
| **Related Entities** | Customer Order, Inventory Reservation, Fulfillment Execution, Backorder |
| **Example** | `OrderLineQuantity(SKU-4420, requested=50, reserved=50, fulfilled=30, backordered=20)` — partial fulfillment state |

---

### 24. Transfer Line Detail

| Aspect | Detail |
|--------|--------|
| **Definition** | A product and quantity tuple on an inter-location transfer, optionally specifying lot identity for traceable products. |
| **Why It Is a Value Object** | Transfer line content defines what moves. The tuple has no identity beyond product, quantity, and lot — embedded in the Stock Transfer entity. |
| **Attributes** | Product identifier, transfer quantity, lot identity (optional), source storage position address (optional) |
| **Related Entities** | Transfer Request, Stock Transfer, In-Transit Stock |
| **Example** | `TransferLineDetail(SKU-4420, Quantity(25, Each), LotIdentity(L20260701))` — traceable transfer between locations per BR-017 |

---

### 25. Invoice Line Detail

| Aspect | Detail |
|--------|--------|
| **Definition** | A billed product line on a supplier invoice specifying billed quantity and unit price for three-way match evaluation. |
| **Why It Is a Value Object** | Invoice line is a financial fact tuple. Matching compares values across PO line and receipt line — the invoice line itself has no independent identity. |
| **Attributes** | Product identifier, billed quantity, unit price (monetary amount), extended amount (monetary amount) |
| **Related Entities** | Supplier Invoice, Purchase Order, Goods Receipt, Three-Way Match Result |
| **Example** | `InvoiceLineDetail(SKU-4420, Quantity(98, Each), $5.00 USD, $490.00 USD)` — matched against PO and receipt for payment per BR-008 |

---

### 26. Pick Line Detail

| Aspect | Detail |
|--------|--------|
| **Definition** | The pick execution record for an order line showing requested versus picked quantity, storage source, and lot applied during fulfillment. |
| **Why It Is a Value Object** | Pick result is an immutable operational fact at verification time. Failed picks generate new pick line values or exceptions — the verified pick tuple does not mutate. |
| **Attributes** | Product identifier, requested quantity, picked quantity, lot identity (optional), source storage position address, pick verification status (pending / verified / short) |
| **Related Entities** | Fulfillment Execution, Shipment, Lot/Batch, Storage Position |
| **Example** | `PickLineDetail(SKU-4420, requested=10, picked=10, LotIdentity(L20260701), verified)` — verified pick enables shipment per BR-003 |

---

### 27. Shipment Line Detail

| Aspect | Detail |
|--------|--------|
| **Definition** | A dispatched product line on a shipment recording shipped quantity and lot attribution at carrier handoff. |
| **Why It Is a Value Object** | What left the building is an immutable dispatch fact. The shipped tuple defines the outbound movement — no separate identity required. |
| **Attributes** | Product identifier, shipped quantity, lot identity (optional), order line reference |
| **Related Entities** | Shipment, Fulfillment Execution, Inventory Movement Record |
| **Example** | `ShipmentLineDetail(SKU-4420, Quantity(10, Each), LotIdentity(L20260701))` — inventory deduction at dispatch |

---

## Domain 7: Variance & Inspection

---

### 28. Quantity Variance

| Aspect | Detail |
|--------|--------|
| **Definition** | The calculated difference between system-recorded quantity and physically counted or expected quantity, expressed as absolute and signed variance. |
| **Why It Is a Value Object** | Variance is a mathematical result defined by two input quantities. System=100, Physical=95 yields Variance=−5 regardless of when or where calculated. |
| **Attributes** | System quantity, physical or expected quantity, variance quantity (signed), variance direction (short / over / match) |
| **Related Entities** | Count Variance, Cycle Count, Physical Inventory Count, Receipt Discrepancy, Stock Adjustment |
| **Example** | `QuantityVariance(system=100, physical=95, variance=-5, short)` — triggers count variance investigation per BR-022 |

---

### 29. Condition Grade

| Aspect | Detail |
|--------|--------|
| **Definition** | The assessed physical and resale condition of received or returned goods at inspection time. |
| **Why It Is a Value Object** | Condition is an evaluated classification at a moment in time. "Damaged — not resalable" is a value judgment captured once; reassessment produces a new grade value. |
| **Attributes** | Grade value (new / good / acceptable / damaged / defective / expired), inspection notes (optional), resalable indicator (yes / no) |
| **Related Entities** | Receipt Line Detail, Customer Return, Return Disposition, Goods Receipt |
| **Example** | `ConditionGrade(damaged, resalable=false)` — returned goods routed to write-off per BR-026 |

---

### 30. Discrepancy Classification

| Aspect | Detail |
|--------|--------|
| **Definition** | The categorized type of receipt variance: short shipment, over-shipment, wrong item, damage, or shelf-life non-compliance. |
| **Why It Is a Value Object** | Discrepancy type is an enumerated classification of a variance event. It carries business meaning for resolution workflow but has no independent identity. |
| **Attributes** | Discrepancy type (short / over / wrongItem / damage / shelfLifeNonCompliance), severity indicator (optional) |
| **Related Entities** | Receipt Discrepancy, Goods Receipt, Receipt Line Detail |
| **Example** | `DiscrepancyClassification(shortShipment)` — documented at receipt before acceptance per BR-006 |

---

### 31. Disposition Decision

| Aspect | Detail |
|--------|--------|
| **Definition** | The outcome decision for returned or non-conforming goods: restock to sellable inventory, place in quarantine, or write off. |
| **Why It Is a Value Object** | A disposition is a final classification applied at decision time. Changing decision replaces the value — the decision moment and outcome form an immutable tuple with condition grade. |
| **Attributes** | Decision value (restock / quarantine / writeOff), decision basis (condition grade reference), decision date |
| **Related Entities** | Return Disposition, Customer Return, Quarantine Hold, Inventory Write-Off |
| **Example** | `DispositionDecision(restock, ConditionGrade(good), 2026-07-05)` — returned item returns to sellable ATP |

---

## Domain 8: Governance & Control

---

### 32. Reason Code Attribution

| Aspect | Detail |
|--------|--------|
| **Definition** | An immutable snapshot of the reason code and description applied to an inventory adjustment, write-off, or exception at the time of the transaction — preserving meaning even if the master reason code is later retired. |
| **Why It Is a Value Object** | Historical transactions must retain why they occurred. Capturing `{code: SHRINK, description: "Unexplained loss"}` at transaction time creates an immutable attribution value independent of the Reason Code entity lifecycle. |
| **Attributes** | Reason code, reason description, reason category (adjustment / shrinkage / damage / obsolescence / receipt / return) |
| **Related Entities** | Stock Adjustment, Inventory Write-Off, Receipt Discrepancy, Inventory Movement Record, Reason Code (master reference entity) |
| **Example** | `ReasonCodeAttribution(SHRINK, Unexplained loss, shrinkage)` — mandatory on every adjustment per BR-020 |

---

### 33. Approval Threshold

| Aspect | Detail |
|--------|--------|
| **Definition** | A governance limit — expressed as quantity, monetary amount, or both — above which independent approval is required before an inventory action takes effect. |
| **Why It Is a Value Object** | Threshold limits are policy numbers without identity. "$5,000 adjustment requires director approval" is a rule value applied at evaluation time. |
| **Attributes** | Threshold type (quantity / monetary / both), quantity limit (optional), monetary limit (optional), required approver role |
| **Related Entities** | Governance Policy, Stock Adjustment, Count Variance, Inventory Write-Off |
| **Example** | `ApprovalThreshold(monetary, limit=$5000, approver=OperationsDirector)` — independent approval per BR-021 |

---

### 34. Quantity Tolerance

| Aspect | Detail |
|--------|--------|
| **Definition** | The acceptable variance range between ordered, received, and billed quantities or amounts within which automatic match approval is permitted. |
| **Why It Is a Value Object** | Tolerance of "±2% or ±5 units" is a policy parameter value. It defines acceptable bounds — not a tracked business object. |
| **Attributes** | Tolerance type (percentage / absolute quantity / absolute monetary), tolerance value, evaluation basis (quantity / amount) |
| **Related Entities** | Governance Policy, Receipt Discrepancy, Three-Way Match Result, Supplier Invoice |
| **Example** | `QuantityTolerance(percentage, 2%, quantity)` — receipt within 2% auto-accepted; beyond triggers discrepancy |

---

### 35. Three-Way Match Result

| Aspect | Detail |
|--------|--------|
| **Definition** | The outcome of comparing purchase order, goods receipt, and supplier invoice lines — indicating matched within tolerance or exception requiring resolution. |
| **Why It Is a Value Object** | Match result is a computed evaluation at a point in time: matched, quantity exception, price exception, or unmatched. Same inputs yield same result — no independent identity. |
| **Attributes** | Match status (matched / quantityException / priceException / unmatched), variance quantity (optional), variance amount (optional), tolerance applied |
| **Related Entities** | Supplier Invoice, Purchase Order, Goods Receipt, Supplier |
| **Example** | `ThreeWayMatchResult(matched, tolerance=QuantityTolerance(2%))` — payment authorized per BR-008 |

---

### 36. User Action Attribution

| Aspect | Detail |
|--------|--------|
| **Definition** | An immutable record of who performed or approved a business action, including user identity and role at the time of action — supporting accountability and segregation of duties. |
| **Why It Is a Value Object** | The tuple `{user: J.Smith, role: WarehouseManager, timestamp: 2026-07-05T14:30}` at action time is historical fact. Role changes later do not alter the captured attribution value. |
| **Attributes** | User identifier, user display name, role at time of action, action timestamp |
| **Related Entities** | Inventory Movement Record, Audit Trail Record, Stock Adjustment, Count Variance, Inventory Write-Off, User Account |
| **Example** | `UserActionAttribution(WH-MGR-007, Jane Smith, WarehouseManager, 2026-07-05T14:30)` — approver distinct from counter per BR-019 |

---

### 37. Audit Quantity Snapshot

| Aspect | Detail |
|--------|--------|
| **Definition** | A before-and-after capture of inventory quantity or status at the moment of a material change, forming the evidential basis of audit trail records. |
| **Why It Is a Value Object** | Snapshot `{before: 100, after: 95}` is immutable historical fact. It describes state transition — not an entity with its own lifecycle. |
| **Attributes** | Before quantity, after quantity, before status (optional), after status (optional), snapshot timestamp |
| **Related Entities** | Audit Trail Record, Stock Adjustment, Inventory Movement Record, Count Variance |
| **Example** | `AuditQuantitySnapshot(before=100, after=95, timestamp=2026-07-05T14:30)` — records adjustment impact for audit |

---

## Domain 9: Fulfillment & Commercial

---

### 38. Fulfillment Quantity Breakdown

| Aspect | Detail |
|--------|--------|
| **Definition** | The decomposition of an order line's quantity into fulfilled, backordered, and cancelled portions after availability confirmation or pick execution. |
| **Why It Is a Value Object** | Breakdown `{requested: 50, fulfilled: 30, backordered: 20}` is a state summary defined by its components. Progress replaces the breakdown value — it does not mutate in place. |
| **Attributes** | Requested quantity, fulfilled quantity, backordered quantity, cancelled quantity |
| **Related Entities** | Customer Order, Backorder, Fulfillment Execution, Shipment |
| **Example** | `FulfillmentQuantityBreakdown(requested=50, fulfilled=30, backordered=20, cancelled=0)` — partial fulfillment with customer acknowledgment per BR-028 |

---

### 39. Customer Acknowledgment

| Aspect | Detail |
|--------|--------|
| **Definition** | Explicit customer consent to accept a backorder or partial delivery, including acknowledgment method and timestamp — elevating backorder from internal note to mutual agreement. |
| **Why It Is a Value Object** | Acknowledgment is a captured fact: who agreed, when, and how. It has no lifecycle — either the acknowledgment value exists or it does not. |
| **Attributes** | Acknowledgment status (pending / acknowledged / declined), acknowledgment method (phone / email / portal), acknowledgment timestamp, acknowledged by (customer contact reference) |
| **Related Entities** | Backorder, Customer Order, Fulfillment Quantity Breakdown |
| **Example** | `CustomerAcknowledgment(acknowledged, email, 2026-07-05T10:15, customerContact=ORD-Acct-442)` — required before backorder recorded per BR-028 |

---

### 40. Channel Designation

| Aspect | Detail |
|--------|--------|
| **Definition** | The sales or fulfillment channel to which promotional stock or an order is attributed — such as eCommerce, retail store, B2B, or promotional campaign. |
| **Why It Is a Value Object** | Channel label is a commercial classification without identity. "eCommerce" means the same across all orders and allocations referencing it. |
| **Attributes** | Channel code, channel name, channel type (direct / partner / promotional) |
| **Related Entities** | Customer Order, Promotional Stock Allocation, Campaign Period |
| **Example** | `ChannelDesignation(B2B, Business Direct, direct)` — order fulfilled from B2B allocation pool |

---

### 41. Payment Terms

| Aspect | Detail |
|--------|--------|
| **Definition** | The agreed commercial payment conditions between the organization and a supplier, governing invoice due dates and payment authorization timing. |
| **Why It Is a Value Object** | "Net 30" is a terms classification defined by its code and due-day count. It has no lifecycle independent of the supplier relationship context. |
| **Attributes** | Terms code (e.g., NET30, NET60, COD), due days, discount terms (optional: percentage and days) |
| **Related Entities** | Supplier, Purchase Order, Supplier Invoice |
| **Example** | `PaymentTerms(NET30, dueDays=30)` — invoice due 30 days from receipt on supplier agreement |

---

## Domain 10: Movement & Status Classification

---

### 42. Movement Classification

| Aspect | Detail |
|--------|--------|
| **Definition** | The categorized type of inventory movement event: receipt, shipment, transfer, adjustment, write-off, reservation, return, or put-away. |
| **Why It Is a Value Object** | Movement type is an enumerated label classifying what happened. Two receipt movements share the same classification value — identity belongs to the movement record entity. |
| **Attributes** | Movement type (receipt / shipment / transfer / adjustment / writeOff / reservation / return / putAway), direction (inbound / outbound / neutral) |
| **Related Entities** | Inventory Movement Record, Goods Receipt, Shipment, Stock Transfer, Stock Adjustment |
| **Example** | `MovementClassification(transfer, neutral)` — inter-location stock movement between source and destination |

---

### 43. Hold Reason Classification

| Aspect | Detail |
|--------|--------|
| **Definition** | The categorized reason inventory is placed under quarantine or hold: quality investigation, regulatory restriction, product recall, or customs/bonded clearance pending. |
| **Why It Is a Value Object** | Hold reason is a classification enum determining exclusion from ATP. The reason value defines business treatment — not a separately tracked object. |
| **Attributes** | Hold type (quality / regulatory / recall / customs / investigation), sellable exclusion indicator (always true for holds) |
| **Related Entities** | Quarantine Hold, Stock Position, Goods Receipt |
| **Example** | `HoldReasonClassification(customs, sellableExcluded=true)` — bonded stock excluded from ATP per BR-030 |

---

### 44. Alert Priority

| Aspect | Detail |
|--------|--------|
| **Definition** | The urgency classification assigned to an operational alert based on severity of the underlying condition — such as Class A stockout versus routine low-stock warning. |
| **Why It Is a Value Object** | Priority is a severity label (critical / high / medium / low) with no identity. Same condition severity always maps to the same priority value. |
| **Attributes** | Priority level (critical / high / medium / low), escalation indicator, response time expectation (optional) |
| **Related Entities** | Operational Alert, Stock Status Indicator, ABC Classification |
| **Example** | `AlertPriority(critical, escalation=true, responseTime=sameDay)` — Class A stockout alert per BR-032 |

---

## Domain 11: Financial & Traceability

---

### 45. Valuation Line Amount

| Aspect | Detail |
|--------|--------|
| **Definition** | The financial value of an inventory quantity calculated as unit cost multiplied by quantity — used in valuation snapshots and write-off impact assessment. |
| **Why It Is a Value Object** | Extended value is a computed financial tuple (quantity × unit cost). Same inputs always produce the same value — no independent business identity. |
| **Attributes** | Product identifier, quantity, unit cost (monetary amount), extended value (monetary amount), ownership classification |
| **Related Entities** | Inventory Valuation Snapshot, Inventory Write-Off, Stock Adjustment |
| **Example** | `ValuationLineAmount(SKU-4420, Quantity(100, Each), $5.00 USD, $500.00 USD, owned)` — month-end valuation line |

---

### 46. Lot Identity

| Aspect | Detail |
|--------|--------|
| **Definition** | The identifying tuple for a traceable production or receipt batch — lot number combined with key dates — captured on movements without referencing the full Lot/Batch entity state. |
| **Why It Is a Value Object** | Lot identity `{number: L20260701, expiration: 2026-12-01}` on a pick line is an immutable identifier tuple embedded in transactions. It describes which batch was touched — the Lot/Batch entity carries ongoing stock state. |
| **Attributes** | Lot/batch number, expiration date (optional), manufacture date (optional) |
| **Related Entities** | Lot/Batch, Receipt Line Detail, Pick Line Detail, Transfer Line Detail, Shipment Line Detail, Inventory Movement Record |
| **Example** | `LotIdentity(L20260701, expiration=2026-12-01)` — captured on pick for traceability per BR-017 |

---

## Value Object Composition Patterns

Several domain entities are composed of multiple value objects rather than primitive attributes:

| Entity | Composed Value Objects |
|--------|------------------------|
| **Stock Position** | Stock Availability Breakdown, Stock Status Indicator, Ownership Classification, Quantity |
| **Stock Policy** | Stock Threshold Set, Lead Time Duration, Effective Period |
| **Product** | Product Identifier, Product Category, Product Lifecycle Status, ABC Classification, Rotation Policy, Unit of Measure |
| **Inventory Location** | Physical Address, Location Type |
| **Storage Position** | Storage Position Address |
| **Purchase Order** | Purchase Order Line (collection), Payment Terms, Lead Time Duration |
| **Goods Receipt** | Receipt Line Detail (collection), User Action Attribution |
| **Customer Order** | Order Line Quantity (collection), Fulfillment Quantity Breakdown, Channel Designation |
| **Count Variance** | Quantity Variance, Reason Code Attribution, User Action Attribution |
| **Stock Adjustment** | Quantity, Reason Code Attribution, Audit Quantity Snapshot, Approval Threshold (evaluated) |
| **Supplier Invoice** | Invoice Line Detail (collection), Three-Way Match Result |
| **Promotional Stock Allocation** | Campaign Period, Channel Designation, Quantity |
| **Inventory Movement Record** | Movement Classification, Quantity, Lot Identity, Reason Code Attribution, User Action Attribution, Audit Quantity Snapshot |
| **Return Disposition** | Condition Grade, Disposition Decision |

---

## Value Object-to-Business-Rule Traceability

| Business Rule | Primary Value Objects |
|---------------|----------------------|
| BR-001 | Stock Availability Breakdown (ATP component) |
| BR-002 | Order Line Quantity (reserved component) |
| BR-003 | Pick Line Detail (verification status) |
| BR-004 | Receipt Line Detail (verification outcome) |
| BR-005 | Stock Availability Breakdown (ATP effective after put-away) |
| BR-006 | Discrepancy Classification, Quantity Variance |
| BR-008 | Three-Way Match Result, Invoice Line Detail, Purchase Order Line |
| BR-009 | Stock Threshold Set, Stock Status Indicator |
| BR-010 | Stock Threshold Set (safety stock component) |
| BR-011 | Stock Availability Breakdown (network ATP view) |
| BR-012 | Stock Threshold Set (minimum at source) |
| BR-013 | Hold Reason Classification, Stock Availability Breakdown |
| BR-014 | Rotation Policy, Shelf Life Profile, Lot Identity |
| BR-015 | Rotation Policy |
| BR-016 | Shelf Life Profile (MRSL evaluation) |
| BR-017 | Lot Identity |
| BR-018 | Quantity (blind count — no system quantity in count value) |
| BR-019 | User Action Attribution (counter vs. approver) |
| BR-020 | Reason Code Attribution |
| BR-021 | Approval Threshold, User Action Attribution |
| BR-022 | Quantity Variance |
| BR-023 | Reason Code Attribution, Valuation Line Amount |
| BR-024 | Effective Period (count freeze window) |
| BR-025 | Customer Acknowledgment (return eligibility context) |
| BR-026 | Condition Grade, Disposition Decision |
| BR-027 | Product Lifecycle Status |
| BR-028 | Customer Acknowledgment, Fulfillment Quantity Breakdown |
| BR-029 | Campaign Period, Channel Designation |
| BR-030 | Hold Reason Classification, Ownership Classification |
| BR-031 | Ownership Classification, Valuation Line Amount |
| BR-032 | ABC Classification, Alert Priority |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| Solution Architect | | | |
| Senior Business Analyst | | | |
| Inventory Controller | | | |

---

*End of Domain Value Objects*

*Document ID: SRS-DM-002 | Version 1.0 | July 5, 2026*
