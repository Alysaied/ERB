# Domain Entity Model
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DM-001 |
| **Document Title** | Domain Entity Model — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Solution Architect / Domain Expert |
| **Source Documents** | BRD-IMS-001 (v1.0), SRS-BR-001 (Business Rules, v1.0), SRS-UC-001 (Use Case Catalog, v1.0) |
| **Date** | July 5, 2026 |
| **Scope** | Business domain model only — no database design, API design, or implementation detail |

### Purpose

This document identifies the core **domain entities** of the Inventory Management System as derived from the approved Business Requirements Document, Business Rules Catalog, and Use Case Catalog. Each entity represents a meaningful business concept with identity, responsibilities, and relationships to processes and rules that govern inventory as a strategic business asset.

### Entity Domain Map

| Domain | Entities |
|--------|----------|
| **Master Data & Reference** | Product, Inventory Location, Storage Position, Stock Policy, Reason Code, Governance Policy |
| **Inventory State & Balance** | Stock Position, Lot/Batch, Quarantine Hold, Promotional Stock Allocation |
| **Procurement & Inbound** | Supplier, Purchase Requisition, Purchase Order, Expected Inbound Delivery, Goods Receipt, Receipt Discrepancy, Put-Away, Supplier Invoice |
| **Order Fulfillment** | Customer Order, Inventory Reservation, Fulfillment Execution, Backorder, Shipment |
| **Network Balance** | Transfer Request, Stock Transfer, In-Transit Stock |
| **Inventory Control** | Cycle Count, Physical Inventory Count, Count Variance, Stock Adjustment, Inventory Write-Off |
| **Returns** | Return Authorization, Customer Return, Return Disposition |
| **Accountability & Oversight** | Inventory Movement Record, Audit Trail Record, Operational Alert, User Account, Role Assignment |
| **Financial Alignment** | Inventory Valuation Snapshot |

**Total Entities:** 40

---

## Domain 1: Master Data & Reference

---

### 1. Product

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a distinct stock-keeping unit (SKU) that the organization buys, holds, and sells. Product is the canonical identity for all inventory operations across locations, departments, and channels. |
| **Identity** | SKU (Stock Keeping Unit) |
| **Responsibilities** | Define what is being counted, stored, ordered, and fulfilled; carry commercial and operational attributes (name, description, unit of measure, category); govern lifecycle status (active, inactive, discontinued); support identifier lookup (SKU, barcode); enable ABC classification and rotation policy assignment (FIFO/FEFO, traceability requirements). |
| **Important Attributes** | SKU, product name, description, unit of measure (UOM), category, product status (active / inactive / discontinued), product identifiers (barcode, alternate codes), ABC classification, shelf-life indicator, traceability requirement (lot/batch), rotation policy (FIFO / FEFO), minimum remaining shelf life (MRSL) policy, supersession reference (if replaced) |
| **Related Business Processes** | BP-01 (Product Master Data Management), BP-04 (ABC Product Classification), BP-03 (Stock Policy & Threshold Definition), BP-07 (Goods Receipt & Verification), BP-18 (Pick, Pack & Ship), BP-22 (Replenishment Planning & Requisition) |
| **Related Business Rules** | BR-014 (FEFO Rotation for Shelf-Life Products), BR-015 (FIFO Rotation for Standard Goods), BR-016 (Minimum Remaining Shelf Life at Receipt), BR-017 (Lot or Batch Capture for Traceable Products), BR-027 (No Reorder of Discontinued Products), BR-032 (Class A Priority Monitoring) |

---

### 2. Inventory Location

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a physical place in the distribution network where stock is held, received, counted, and fulfilled — such as a warehouse, store, or distribution point. Locations form the network through which inventory is balanced and reported. |
| **Identity** | Location Code |
| **Responsibilities** | Anchor all stock balances and movements to a physical site; support location hierarchy (region, site, zone); enable location-scoped visibility, authorization, and performance reporting; define where receiving, put-away, counting, and fulfillment occur; support location go-live with opening balances and closure planning. |
| **Important Attributes** | Location code, location name, location type (warehouse / store / distribution point), parent location (hierarchy), operational status (active / planned / closing), address and region, assigned responsible manager, go-live date, closure disposition plan |
| **Related Business Processes** | BP-02 (Location & Warehouse Setup), BP-10 (Inventory Status Monitoring), BP-12 (Full Physical Inventory Count), BP-24 (Inter-Location Transfer Request), BP-25 (Inter-Location Transfer Execution), BP-29 (Inventory Performance Reporting) |
| **Related Business Rules** | BR-012 (Protect Source Location Minimum), BR-024 (Physical Inventory Freeze) |

---

### 3. Storage Position

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a designated storage area within an inventory location (aisle, zone, bin, shelf) where received goods are placed after put-away. Storage position enables efficient retrieval and rotation discipline during picking. |
| **Identity** | Storage Position Code (unique within location) |
| **Responsibilities** | Direct put-away placement after receipt; guide pick path and rotation (FIFO/FEFO); associate physical stock with a findable address within the location; support bin-level accuracy in advanced operations. |
| **Important Attributes** | Storage position code, location reference, zone/aisle/bin designation, storage type (bulk / pick face / quarantine / bonded), capacity indicator, product assignment rules (if dedicated) |
| **Related Business Processes** | BP-09 (Stock Put-Away & Storage), BP-18 (Pick, Pack & Ship), BP-11 (Cycle Counting) |
| **Related Business Rules** | BR-005 (Put-Away Before Availability), BR-014 (FEFO Rotation for Shelf-Life Products), BR-015 (FIFO Rotation for Standard Goods) |

---

### 4. Stock Policy

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Defines replenishment and service-level thresholds for a product at a specific location (or network-wide default). Stock policy translates demand and lead-time assumptions into actionable reorder triggers and safety buffers. |
| **Identity** | Stock Policy Reference (Product + Location combination) |
| **Responsibilities** | Set reorder level, minimum threshold, and safety stock; trigger low-stock alerts and replenishment reviews; protect service levels during transfers and reservations; govern when procurement or network rebalancing should be initiated. |
| **Important Attributes** | Product reference, location reference, reorder level, minimum stock threshold, safety stock quantity, maximum stock level (overstock indicator), lead time assumption, replenishment review frequency, policy effective date, exception approval record |
| **Related Business Processes** | BP-03 (Stock Policy & Threshold Definition), BP-21 (Low-Stock Alert Review), BP-22 (Replenishment Planning & Requisition), BP-24 (Inter-Location Transfer Request), BP-26 (Network Stock Rebalancing) |
| **Related Business Rules** | BR-009 (Reorder at Reorder Level), BR-010 (Safety Stock Protection), BR-011 (Network Check Before Purchase), BR-012 (Protect Source Location Minimum) |

---

### 5. Reason Code

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Provides a standardized, categorized business explanation for inventory adjustments, exceptions, and disposition decisions. Reason codes enable shrinkage analysis, trend identification, and audit accountability. |
| **Identity** | Reason Code |
| **Responsibilities** | Categorize why inventory quantity or status changed; support mandatory attribution on adjustments, write-offs, and discrepancies; feed reporting on loss patterns and process failures; align operational actions with governance taxonomy. |
| **Important Attributes** | Reason code, description, category (adjustment / shrinkage / damage / obsolescence / receipt discrepancy / return / other), active status, approval threshold association, reporting group |
| **Related Business Processes** | BP-01 (Product Master Data Management), BP-08 (Receipt Discrepancy Resolution), BP-14 (Stock Adjustment & Write-Off), BP-15 (Shrinkage & Loss Management), BP-28 (Return-to-Stock or Disposal Decision) |
| **Related Business Rules** | BR-006 (Document Receipt Discrepancies), BR-020 (Mandatory Adjustment Reason Codes), BR-023 (Documented Write-Off Authorization) |

---

### 6. Governance Policy

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Captures organization-wide inventory control policies — approval thresholds, segregation-of-duties requirements, tolerance limits, and exception handling rules — that govern how operational entities may be changed. |
| **Identity** | Policy Identifier |
| **Responsibilities** | Define financial and quantity approval thresholds for adjustments; enforce segregation of duties (count vs. approve); set receipt quantity tolerance limits; govern ad-hoc receipt exceptions; provide the policy baseline for audit and compliance review. |
| **Important Attributes** | Policy identifier, policy name, policy type (approval threshold / tolerance / access / exception), threshold value, applicable scope (location / role / transaction type), effective date, approval authority role |
| **Related Business Processes** | BP-01 (Product Master Data Management), BP-13 (Count Variance Investigation & Approval), BP-14 (Stock Adjustment & Write-Off), BP-32 (Inventory Audit & Control Review) |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments), BR-007 (Purchase Order Required for Supplier Receipt) |

---

## Domain 2: Inventory State & Balance

---

### 7. Stock Position

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the current inventory balance of a product at a location — the authoritative answer to "what do we have, where is it, and what is available?" Stock position is the central entity connecting visibility, fulfillment, replenishment, and financial alignment. |
| **Identity** | Stock Position Reference (Product + Location [+ Lot/Batch when traceable]) |
| **Responsibilities** | Maintain on-hand, reserved, and available-to-promise (ATP) quantities; reflect stock status indicators (in stock, low stock, out of stock, overstock); exclude non-sellable holds from ATP; support network-wide and location-level availability inquiries; change only through documented movements and adjustments. |
| **Important Attributes** | Product reference, location reference, on-hand quantity, reserved quantity, available-to-promise (ATP), inbound expected quantity (network view), stock status indicator, ownership type (owned / consignment / bonded), last movement date, quarantine flag |
| **Related Business Processes** | BP-10 (Inventory Status Monitoring), BP-16 (Order Availability Confirmation), BP-17 (Inventory Reservation), BP-21 (Low-Stock Alert Review), BP-29 (Inventory Performance Reporting), BP-30 (Inventory Valuation & Financial Reconciliation) |
| **Related Business Rules** | BR-001 (ATP-Only Customer Commitment), BR-002 (Reservation at Order Confirmation), BR-013 (Quarantine Exclusion from Sellable Stock), BR-009 (Reorder at Reorder Level), BR-031 (Consignment Ownership at Consumption) |

---

### 8. Lot / Batch

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a traceable production or receipt grouping for products requiring lot-level tracking. Lot/batch identity enables targeted recall, quality investigation, regulatory compliance, and FEFO rotation. |
| **Identity** | Lot/Batch Number (within product scope) |
| **Responsibilities** | Capture lot identity at receipt and through all subsequent movements; support FEFO picking by expiration date; enable recall scope limitation; link stock position to quality and shelf-life attributes. |
| **Important Attributes** | Lot/batch number, product reference, expiration date, manufacture date, receipt date, remaining shelf life, quality status, supplier reference, associated stock quantity by location |
| **Related Business Processes** | BP-07 (Goods Receipt & Verification), BP-09 (Stock Put-Away & Storage), BP-18 (Pick, Pack & Ship), BP-25 (Inter-Location Transfer Execution), BP-14 (Stock Adjustment & Write-Off) |
| **Related Business Rules** | BR-017 (Lot or Batch Capture for Traceable Products), BR-014 (FEFO Rotation for Shelf-Life Products), BR-016 (Minimum Remaining Shelf Life at Receipt) |

---

### 9. Quarantine Hold

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents inventory physically present but excluded from sellable availability due to quality investigation, regulatory restriction, recall, customs hold (bonded), or other business hold. |
| **Identity** | Hold Reference |
| **Responsibilities** | Remove affected quantity from ATP; track hold reason and expected resolution; govern release back to sellable stock or disposition to write-off; support customs clearance workflow for bonded inventory. |
| **Important Attributes** | Hold reference, product reference, location reference, lot/batch reference (if applicable), held quantity, hold type (quality / regulatory / recall / customs / investigation), hold reason, hold start date, expected resolution date, release or disposition outcome, authorizing party |
| **Related Business Processes** | BP-14 (Stock Adjustment & Write-Off), BP-20 (Outbound Exception Handling), BP-07 (Goods Receipt & Verification), BP-09 (Stock Put-Away & Storage) |
| **Related Business Rules** | BR-013 (Quarantine Exclusion from Sellable Stock), BR-030 (Bonded Inventory Customs Clearance) |

---

### 10. Promotional Stock Allocation

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents inventory ring-fenced for a specific promotional campaign, product launch, or channel commitment. Promotional allocation protects campaign supply from consumption by non-promotional demand. |
| **Identity** | Allocation Reference |
| **Responsibilities** | Reserve defined quantity for campaign period and channel; exclude allocated stock from general ATP for non-approved orders; support readiness review before campaign commitment; release un consumed allocation after campaign end. |
| **Important Attributes** | Allocation reference, product reference, location(s), allocated quantity, campaign or launch name, effective start date, effective end date, channel scope, readiness status, commercial approval reference |
| **Related Business Processes** | BP-31 (Promotional & Launch Stock Readiness), BP-17 (Inventory Reservation), BP-22 (Replenishment Planning & Requisition) |
| **Related Business Rules** | BR-029 (Promotional Stock Ring-Fencing) |

---

## Domain 3: Procurement & Inbound Supply

---

### 11. Supplier

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents an external vendor from whom the organization procures goods. Supplier is the commercial counterparty in the inbound supply chain and accountability chain for receipt and payment. |
| **Identity** | Supplier Code |
| **Responsibilities** | Anchor purchase orders and goods receipts; support supplier delivery performance tracking; enable three-way match for payment authorization; associate inbound supply with commercial terms. |
| **Important Attributes** | Supplier code, supplier name, contact information, payment terms, lead time profile, active status, consignment agreement indicator, delivery performance rating |
| **Related Business Processes** | BP-05 (Purchase Order Placement), BP-07 (Goods Receipt & Verification), BP-08 (Receipt Discrepancy Resolution), BP-23 (Inbound Supply Tracking), BP-30 (Inventory Valuation & Financial Reconciliation) |
| **Related Business Rules** | BR-007 (Purchase Order Required for Supplier Receipt), BR-008 (Three-Way Match Before Payment), BR-031 (Consignment Ownership at Consumption) |

---

### 12. Purchase Requisition

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents an internal request to procure stock, created when replenishment planning identifies a need. Requisition precedes formal purchase order creation and carries approval workflow. |
| **Identity** | Requisition Number |
| **Responsibilities** | Capture replenishment need with product, quantity, and target location; route for internal approval before PO creation; link to triggering low-stock alert or replenishment suggestion; prevent requisition for discontinued products. |
| **Important Attributes** | Requisition number, requesting location, product lines (product, quantity), requested delivery date, triggering alert reference, approval status, approver, creation date, linked purchase order reference |
| **Related Business Processes** | BP-22 (Replenishment Planning & Requisition), BP-21 (Low-Stock Alert Review), BP-05 (Purchase Order Placement) |
| **Related Business Rules** | BR-009 (Reorder at Reorder Level), BR-011 (Network Check Before Purchase), BR-027 (No Reorder of Discontinued Products), BR-010 (Safety Stock Protection) |

---

### 13. Purchase Order

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the authorized commercial commitment to a supplier specifying products, quantities, prices, and delivery terms. The purchase order is the control document for inbound receipt and financial three-way match. |
| **Identity** | Purchase Order Number |
| **Responsibilities** | Authorize what may be received from a supplier; define expected inbound supply; enable PO-receipt-invoice matching; track open, partially received, and closed status; govern receipt without PO exceptions. |
| **Important Attributes** | Purchase order number, supplier reference, order date, expected delivery date, line items (product, ordered quantity, unit price), received quantity (per line), PO status (open / partial / closed / cancelled), delivery location, total commitment value, amendment history |
| **Related Business Processes** | BP-05 (Purchase Order Placement), BP-06 (Inbound Shipment Planning), BP-07 (Goods Receipt & Verification), BP-23 (Inbound Supply Tracking), BP-30 (Inventory Valuation & Financial Reconciliation) |
| **Related Business Rules** | BR-007 (Purchase Order Required for Supplier Receipt), BR-008 (Three-Way Match Before Payment), BR-027 (No Reorder of Discontinued Products) |

---

### 14. Expected Inbound Delivery

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a planned or confirmed supplier shipment tied to a purchase order, communicating when and what quantity is expected to arrive. Supports receiving preparation and inbound supply visibility. |
| **Identity** | Delivery Plan Reference |
| **Responsibilities** | Communicate anticipated arrival date and quantity to receiving and replenishment teams; update when supplier changes schedule; feed inbound expected quantity into network availability views; trigger delay notifications. |
| **Important Attributes** | Delivery plan reference, purchase order reference, expected arrival date, expected quantity by product, carrier reference, shipment status (planned / in transit / arrived / delayed), receiving location |
| **Related Business Processes** | BP-06 (Inbound Shipment Planning), BP-23 (Inbound Supply Tracking), BP-10 (Inventory Status Monitoring) |
| **Related Business Rules** | — |

---

### 15. Goods Receipt

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the business event of accepting verified inbound goods into inventory control. Goods receipt confirms that quantity, product identity, and condition have been validated before stock is recorded. |
| **Identity** | Goods Receipt Number |
| **Responsibilities** | Match inbound shipment to purchase order (or authorized exception); verify quantity, product, and condition; capture lot/batch and shelf-life data for traceable products; initiate put-away; create the receipt leg of three-way match; reject or hold non-conforming deliveries. |
| **Important Attributes** | Goods receipt number, purchase order reference (or exception authorization), supplier reference, receiving location, receipt date, received lines (product, quantity, condition), lot/batch assignments, verification status, receiving clerk, linked discrepancies |
| **Related Business Processes** | BP-07 (Goods Receipt & Verification), BP-08 (Receipt Discrepancy Resolution), BP-09 (Stock Put-Away & Storage), BP-27 (Customer Return Intake) |
| **Related Business Rules** | BR-004 (Verify Before Inventory Acceptance), BR-005 (Put-Away Before Availability), BR-006 (Document Receipt Discrepancies), BR-007 (Purchase Order Required for Supplier Receipt), BR-016 (Minimum Remaining Shelf Life at Receipt), BR-017 (Lot or Batch Capture for Traceable Products), BR-030 (Bonded Inventory Customs Clearance) |

---

### 16. Receipt Discrepancy

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a documented difference between expected and actual receipt — short shipment, over-shipment, wrong item, damage, or shelf-life non-compliance — captured at the point of receipt with supporting evidence. |
| **Identity** | Discrepancy Reference |
| **Responsibilities** | Record variance before acceptance; preserve evidence for supplier claims; drive resolution workflow (accept partial, reject, claim); affect three-way match outcome; prevent silent acceptance of incorrect supply. |
| **Important Attributes** | Discrepancy reference, goods receipt reference, discrepancy type (short / over / wrong item / damage / shelf-life), expected vs. received quantity, product affected, evidence documentation, resolution status, resolution outcome, supplier claim reference |
| **Related Business Processes** | BP-08 (Receipt Discrepancy Resolution), BP-07 (Goods Receipt & Verification) |
| **Related Business Rules** | BR-006 (Document Receipt Discrepancies), BR-008 (Three-Way Match Before Payment), BR-016 (Minimum Remaining Shelf Life at Receipt) |

---

### 17. Put-Away

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the business confirmation that received goods have been moved from the receiving area to their designated storage position and are now operationally available for sale and fulfillment. |
| **Identity** | Put-Away Reference |
| **Responsibilities** | Transition stock from "received but unavailable" to sellable ATP; assign storage position; apply rotation placement (FIFO/FEFO); release bonded inventory only after customs clearance; complete the inbound-to-available lifecycle. |
| **Important Attributes** | Put-away reference, goods receipt reference, product reference, quantity, from area (receiving dock), to storage position, put-away date, performing staff, availability effective timestamp |
| **Related Business Processes** | BP-09 (Stock Put-Away & Storage) |
| **Related Business Rules** | BR-005 (Put-Away Before Availability), BR-014 (FEFO Rotation for Shelf-Life Products), BR-015 (FIFO Rotation for Standard Goods), BR-030 (Bonded Inventory Customs Clearance) |

---

### 18. Supplier Invoice

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the supplier's billing document for goods supplied. Supplier invoice is the financial leg of the three-way match against purchase order and goods receipt before payment authorization. |
| **Identity** | Supplier Invoice Number (within supplier scope) |
| **Responsibilities** | Record billed quantity and price; support three-way match evaluation against PO and receipt; flag mismatches for resolution; gate payment authorization; align operational receipt with financial obligation. |
| **Important Attributes** | Invoice number, supplier reference, invoice date, purchase order reference, line items (product, billed quantity, unit price), total amount, match status (pending / matched / exception), tolerance variance, payment authorization status |
| **Related Business Processes** | BP-30 (Inventory Valuation & Financial Reconciliation), BP-08 (Receipt Discrepancy Resolution), BP-05 (Purchase Order Placement) |
| **Related Business Rules** | BR-008 (Three-Way Match Before Payment) |

---

## Domain 4: Order Fulfillment

---

### 19. Customer Order

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a customer demand for products that the organization commits to fulfill. Customer order is the commercial trigger for availability confirmation, reservation, picking, and shipment. *(Authoritative order data may reside in external sales/CRM systems; IMS holds fulfillment-relevant order context.)* |
| **Identity** | Order Number |
| **Responsibilities** | Carry order lines (product, requested quantity); trigger availability confirmation against ATP; drive reservation, pick, pack, and ship; support partial fulfillment and backorder handling; link to returns via original order reference. |
| **Important Attributes** | Order number, customer reference, order date, requested delivery date, order lines (product, quantity, fulfilled quantity, backordered quantity), order status (draft / confirmed / partially fulfilled / fulfilled / cancelled), fulfillment location(s), channel |
| **Related Business Processes** | BP-16 (Order Availability Confirmation), BP-17 (Inventory Reservation), BP-18 (Pick, Pack & Ship), BP-19 (Partial Fulfillment & Backorder Management), BP-27 (Customer Return Intake) |
| **Related Business Rules** | BR-001 (ATP-Only Customer Commitment), BR-002 (Reservation at Order Confirmation), BR-028 (Backorder Customer Acknowledgment) |

---

### 20. Inventory Reservation

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents an operational hold on stock for a confirmed customer order line, reducing ATP to prevent double-allocation between confirmation and physical fulfillment. |
| **Identity** | Reservation Reference |
| **Responsibilities** | Commit on-hand stock to a specific order line; reduce ATP immediately upon order confirmation; release when order is cancelled, amended, or fulfilled; respect safety stock and promotional ring-fence rules; support multi-location split reservations. |
| **Important Attributes** | Reservation reference, order reference, order line reference, product reference, location reference, reserved quantity, reservation date, reservation status (active / released / fulfilled), expiry or priority indicator |
| **Related Business Processes** | BP-17 (Inventory Reservation), BP-16 (Order Availability Confirmation), BP-18 (Pick, Pack & Ship), BP-31 (Promotional & Launch Stock Readiness) |
| **Related Business Rules** | BR-002 (Reservation at Order Confirmation), BR-010 (Safety Stock Protection), BR-029 (Promotional Stock Ring-Fencing), BR-001 (ATP-Only Customer Commitment) |

---

### 21. Fulfillment Execution

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the warehouse work of picking, verifying, packing, and preparing order lines for dispatch. Fulfillment execution is the operational bridge between reservation and shipment. |
| **Identity** | Fulfillment Reference |
| **Responsibilities** | Retrieve correct products from storage applying FIFO/FEFO; verify picked quantity against order; record pick confirmation before shipment; capture lot/batch on pick for traceable products; escalate exceptions (short pick, damage, shelf mismatch). |
| **Important Attributes** | Fulfillment reference, order reference, fulfillment location, pick lines (product, requested quantity, picked quantity, lot/batch), pick verification status, pack confirmation, assigned picker/packer, exception flags, pick completion timestamp |
| **Related Business Processes** | BP-18 (Pick, Pack & Ship), BP-20 (Outbound Exception Handling), BP-19 (Partial Fulfillment & Backorder Management) |
| **Related Business Rules** | BR-003 (Verified Pick Before Shipment), BR-014 (FEFO Rotation for Shelf-Life Products), BR-015 (FIFO Rotation for Standard Goods), BR-017 (Lot or Batch Capture for Traceable Products) |

---

### 22. Backorder

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a customer-agreed delay to fulfill remaining order quantity when full quantity is unavailable at confirmation or pick. Backorder is a mutual commercial commitment, not an internal note. |
| **Identity** | Backorder Reference |
| **Responsibilities** | Record unfulfilled quantity with customer acknowledgment; communicate expected fulfillment timing; offer cancel or partial delivery options; prioritize replenishment allocation; convert to reservation when stock becomes available. |
| **Important Attributes** | Backorder reference, order reference, order line reference, product reference, backordered quantity, customer acknowledgment status, expected fulfillment date, backorder reason, priority for replenishment, resolution status |
| **Related Business Processes** | BP-19 (Partial Fulfillment & Backorder Management), BP-22 (Replenishment Planning & Requisition) |
| **Related Business Rules** | BR-028 (Backorder Customer Acknowledgment), BR-001 (ATP-Only Customer Commitment) |

---

### 23. Shipment

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the confirmed dispatch of fulfilled goods to the customer or carrier. Shipment is the point at which inventory is deducted and the delivery promise is activated. |
| **Identity** | Shipment Number |
| **Responsibilities** | Confirm verified pick completion before dispatch; deduct on-hand and release reservation; record carrier handoff; provide shipment status for customer service; create outbound movement record. |
| **Important Attributes** | Shipment number, order reference, fulfillment reference, ship-from location, ship date, carrier reference, tracking identifier, shipped lines (product, quantity, lot/batch), shipment status (dispatched / in transit / delivered) |
| **Related Business Processes** | BP-18 (Pick, Pack & Ship) |
| **Related Business Rules** | BR-003 (Verified Pick Before Shipment) |

---

## Domain 5: Network Balance

---

### 24. Transfer Request

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a formal request to move stock from one location to another to resolve local shortage, rebalance network inventory, or respond to operational need — evaluated before new procurement. |
| **Identity** | Transfer Request Number |
| **Responsibilities** | Specify source location, destination location, product, and quantity; validate source can spare stock above minimum threshold; route for approval; prevent unnecessary procurement when network stock exists. |
| **Important Attributes** | Transfer request number, source location, destination location, product lines (product, requested quantity), request reason, request date, requestor, approval status, approver, rejection reason |
| **Related Business Processes** | BP-24 (Inter-Location Transfer Request), BP-26 (Network Stock Rebalancing), BP-21 (Low-Stock Alert Review) |
| **Related Business Rules** | BR-011 (Network Check Before Purchase), BR-012 (Protect Source Location Minimum), BR-010 (Safety Stock Protection) |

---

### 25. Stock Transfer

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the executed movement of stock between inventory locations, with full transaction history from dispatch through receipt at destination. |
| **Identity** | Transfer Number |
| **Responsibilities** | Deduct stock at source upon dispatch; track in-transit state; receive and verify at destination; capture lot/batch through transfer for traceable products; update stock positions at both locations; maintain audit trail. |
| **Important Attributes** | Transfer number, transfer request reference, source location, destination location, transfer lines (product, quantity, lot/batch), dispatch date, receipt date, transfer status (requested / approved / in transit / received / cancelled), in-transit quantity |
| **Related Business Processes** | BP-25 (Inter-Location Transfer Execution), BP-24 (Inter-Location Transfer Request) |
| **Related Business Rules** | BR-012 (Protect Source Location Minimum), BR-017 (Lot or Batch Capture for Traceable Products) |

---

### 26. In-Transit Stock

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents inventory that has left the source location but has not yet been received at the destination — a distinct network availability state during inter-location transfer. |
| **Identity** | In-Transit Reference (linked to Stock Transfer) |
| **Responsibilities** | Track quantity in movement between locations; exclude from source ATP and destination ATP until receipt confirmed; support network visibility of pipeline stock; enable exception handling for delayed or lost transfers. |
| **Important Attributes** | In-transit reference, stock transfer reference, product reference, quantity, source location, destination location, dispatch date, expected receipt date, in-transit status, carrier reference (if applicable) |
| **Related Business Processes** | BP-25 (Inter-Location Transfer Execution), BP-26 (Network Stock Rebalancing), BP-10 (Inventory Status Monitoring) |
| **Related Business Rules** | BR-012 (Protect Source Location Minimum) |

---

## Domain 6: Inventory Control & Accuracy

---

### 27. Cycle Count

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a scheduled partial physical count of selected products or locations on a rotating basis, performed without full warehouse shutdown, to measure and maintain inventory accuracy. |
| **Identity** | Cycle Count Assignment Number |
| **Responsibilities** | Assign count scope (product, location, storage position); enforce blind counting (counter not shown system quantity); schedule by ABC priority (Class A highest frequency); record physical count result; trigger variance investigation when needed. |
| **Important Attributes** | Count assignment number, count schedule date, location reference, product scope, storage position scope, assigned counter, count status (scheduled / in progress / completed), physical count quantity, count completion date |
| **Related Business Processes** | BP-11 (Cycle Counting), BP-13 (Count Variance Investigation & Approval) |
| **Related Business Rules** | BR-018 (Blind Cycle Counting), BR-032 (Class A Priority Monitoring) |

---

### 28. Physical Inventory Count

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a comprehensive wall-to-wall physical count at a location to establish an authoritative inventory accuracy baseline, typically on annual or audit-mandated cycle. |
| **Identity** | Physical Count Event Number |
| **Responsibilities** | Enforce location freeze (no receiving, shipping, transfers, or adjustments during count); capture full location snapshot; identify variances against system records; support audit and finance baseline reconciliation. |
| **Important Attributes** | Count event number, location reference, count start date, count completion date, freeze status, count scope (full location), assigned teams, total variances identified, count certification status |
| **Related Business Processes** | BP-12 (Full Physical Inventory Count), BP-13 (Count Variance Investigation & Approval) |
| **Related Business Rules** | BR-024 (Physical Inventory Freeze) |

---

### 29. Count Variance

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a identified difference between system-recorded quantity and physically counted quantity, requiring investigation before any adjustment is applied. |
| **Identity** | Variance Reference |
| **Responsibilities** | Quantify discrepancy (system vs. physical); trigger root cause investigation; route for independent approval (counter cannot approve own count); gate stock adjustment creation; feed accuracy metrics. |
| **Important Attributes** | Variance reference, count reference (cycle or physical), product reference, location reference, system quantity, physical quantity, variance quantity, variance value, investigation status, investigation findings, approval status, approver (independent of counter) |
| **Related Business Processes** | BP-13 (Count Variance Investigation & Approval), BP-14 (Stock Adjustment & Write-Off) |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments), BR-022 (Investigate Before Adjusting) |

---

### 30. Stock Adjustment

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a correction to recorded inventory quantity when physical reality differs from system records, applied with mandatory reason code and appropriate authorization. |
| **Identity** | Adjustment Reference |
| **Responsibilities** | Increase or decrease stock position with documented reason; enforce reason code and user attribution; require independent approval above threshold; update stock position and create movement record; distinguish from write-off (recoverable correction vs. permanent removal). |
| **Important Attributes** | Adjustment reference, product reference, location reference, adjustment quantity (+/−), reason code, initiating user, approval status, approver, linked variance reference (if from count), adjustment date, before/after quantities |
| **Related Business Processes** | BP-14 (Stock Adjustment & Write-Off), BP-13 (Count Variance Investigation & Approval), BP-15 (Shrinkage & Loss Management) |
| **Related Business Rules** | BR-020 (Mandatory Adjustment Reason Codes), BR-021 (Independent Approval for Material Adjustments), BR-022 (Investigate Before Adjusting) |

---

### 31. Inventory Write-Off

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the formal, authorized removal of inventory value for goods that are damaged beyond resale, obsolete, expired, or confirmed lost — a permanent reduction distinct from reversible adjustment. |
| **Identity** | Write-Off Reference |
| **Responsibilities** | Permanently remove quantity and value from inventory; require documented evidence and authorized approval; apply mandatory reason code; reduce stock position; support shrinkage and financial reconciliation reporting. |
| **Important Attributes** | Write-off reference, product reference, location reference, write-off quantity, reason code, supporting evidence reference, initiating user, authorizing approver, write-off date, financial value impact, disposition method (destroy / donate / scrap) |
| **Related Business Processes** | BP-14 (Stock Adjustment & Write-Off), BP-15 (Shrinkage & Loss Management), BP-28 (Return-to-Stock or Disposal Decision) |
| **Related Business Rules** | BR-023 (Documented Write-Off Authorization), BR-020 (Mandatory Adjustment Reason Codes) |

---

## Domain 7: Returns Management

---

### 32. Return Authorization

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents approved permission for a customer to return goods, linked to the original order and return policy, before the warehouse accepts physical return. |
| **Identity** | Return Authorization Number (RMA) |
| **Responsibilities** | Validate return eligibility against original order and policy; specify expected return products and quantities; communicate return instructions to customer; provide warehouse advance notice; gate receipt of returned goods. |
| **Important Attributes** | RMA number, original order reference, customer reference, authorized return lines (product, quantity), return reason, authorization date, expiration date, return disposition expectation, authorization status |
| **Related Business Processes** | BP-27 (Customer Return Intake), BP-28 (Return-to-Stock or Disposal Decision) |
| **Related Business Rules** | BR-025 (Return Authorization Required) |

---

### 33. Customer Return

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the physical receipt of customer-returned goods at the warehouse, linked to a valid return authorization, initiating inspection and disposition workflow. |
| **Identity** | Customer Return Number |
| **Responsibilities** | Receive returned goods only with valid RMA; verify quantity and product against authorization; initiate condition inspection; route to restock, quarantine, or write-off disposition; update return processing status. |
| **Important Attributes** | Return number, RMA reference, original order reference, receiving location, receipt date, returned lines (product, quantity, condition at receipt), inspection status, receiving clerk |
| **Related Business Processes** | BP-27 (Customer Return Intake), BP-28 (Return-to-Stock or Disposal Decision), BP-07 (Goods Receipt & Verification) |
| **Related Business Rules** | BR-025 (Return Authorization Required), BR-004 (Verify Before Inventory Acceptance) |

---

### 34. Return Disposition

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the business decision on returned goods outcome — restock to sellable inventory, quarantine for further inspection, or write-off — based on condition assessment. |
| **Identity** | Disposition Reference |
| **Responsibilities** | Assess returned product condition against resale standards; authorize restock only for qualifying goods; route damaged goods to write-off or quarantine; update stock position upon restock; prevent used/damaged goods entering sellable inventory. |
| **Important Attributes** | Disposition reference, customer return reference, product reference, quantity, condition grade, disposition decision (restock / quarantine / write-off), inspection date, inspector, restock location (if applicable), linked write-off or hold reference |
| **Related Business Processes** | BP-28 (Return-to-Stock or Disposal Decision) |
| **Related Business Rules** | BR-026 (Inspect Returns Before Restocking), BR-013 (Quarantine Exclusion from Sellable Stock), BR-023 (Documented Write-Off Authorization) |

---

## Domain 8: Accountability & Oversight

---

### 35. Inventory Movement Record

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a single documented change in inventory position — the immutable business fact that stock moved, was adjusted, or changed status. Movement records form the operational history of all stock activity. |
| **Identity** | Movement Transaction Reference |
| **Responsibilities** | Record every inventory change with product, location, quantity, direction, and business event type; capture user identity and timestamp; carry reason code where applicable; support traceability by lot/batch; enable operational investigation and reporting. |
| **Important Attributes** | Movement reference, movement type (receipt / shipment / transfer / adjustment / write-off / reservation / return / put-away), product reference, location reference, quantity change, lot/batch reference, reason code, originating business document reference, user identity, movement timestamp, before/after balances |
| **Related Business Processes** | BP-10 (Inventory Status Monitoring), BP-29 (Inventory Performance Reporting), all transaction processes (BP-07 through BP-09, BP-14, BP-18, BP-25, BP-28) |
| **Related Business Rules** | BR-017 (Lot or Batch Capture for Traceable Products), BR-020 (Mandatory Adjustment Reason Codes) |

---

### 36. Audit Trail Record

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the governance-grade record of material inventory changes including user identity, timestamp, and before/after state — supporting compliance, fraud prevention, and control testing. |
| **Identity** | Audit Event Reference |
| **Responsibilities** | Provide immutable evidence of who changed what and when; support segregation-of-duties verification; enable internal and external audit queries; complement movement records with authorization and approval context. |
| **Important Attributes** | Audit event reference, affected entity type, affected entity reference, action performed, user identity, role at time of action, timestamp, before state snapshot, after state snapshot, approval chain reference, IP or session context (business accountability) |
| **Related Business Processes** | BP-32 (Inventory Audit & Control Review), BP-14 (Stock Adjustment & Write-Off), BP-13 (Count Variance Investigation & Approval) |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments), BR-020 (Mandatory Adjustment Reason Codes) |

---

### 37. Operational Alert

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a proactive notification of a business condition requiring human review or action — such as low stock, pending approval, fulfillment exception, or campaign readiness gap. |
| **Identity** | Alert Reference |
| **Responsibilities** | Signal threshold breaches and exception conditions; route to responsible actor; track acknowledgment and resolution; prevent silent degradation of service levels; support replenishment and governance timeliness. |
| **Important Attributes** | Alert reference, alert type (low stock / out of stock / pending approval / transfer exception / inbound delay / campaign readiness), severity, affected product/location, triggering condition, alert date, assigned recipient role, acknowledgment status, resolution status |
| **Related Business Processes** | BP-21 (Low-Stock Alert Review), BP-24 (Inter-Location Transfer Request), BP-31 (Promotional & Launch Stock Readiness), BP-20 (Outbound Exception Handling) |
| **Related Business Rules** | BR-009 (Reorder at Reorder Level), BR-032 (Class A Priority Monitoring) |

---

### 38. User Account

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents an identified individual authorized to perform inventory operations within defined role and location scope. User account is the accountability anchor for all inventory actions. |
| **Identity** | User Identifier |
| **Responsibilities** | Authenticate identity for system access; carry role assignments and location scope; enforce segregation of duties; attribute movements, adjustments, and approvals to a named individual; support provisioning and deactivation lifecycle. |
| **Important Attributes** | User identifier, display name, assigned roles, authorized locations, account status (active / suspended / deactivated), effective date, last activity date, conflicting duty flags |
| **Related Business Processes** | All operational processes; BP-32 (Inventory Audit & Control Review) |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments) |

---

### 39. Role Assignment

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents the delegation of business permissions to a user account — defining what functions a person may perform and within which locations, implementing segregation of duties. |
| **Identity** | Role Assignment Reference (User + Role [+ Location Scope]) |
| **Responsibilities** | Grant view, transact, approve, or configure authority by role; scope permissions to assigned locations; prevent conflicting duty combinations; enable role changes on employee lifecycle events. |
| **Important Attributes** | Assignment reference, user reference, role name (e.g., Warehouse Manager, Receiving Clerk, Buyer), location scope, permission set, assignment effective date, assignment status, segregation-of-duties compliance flag |
| **Related Business Processes** | BP-32 (Inventory Audit & Control Review); cross-cutting across all processes |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments), BR-023 (Documented Write-Off Authorization) |

---

## Domain 9: Financial Alignment

---

### 40. Inventory Valuation Snapshot

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Represents a point-in-time summary of inventory value by product, location, and category for alignment with financial records and month-end close — bridging operational stock records to finance. |
| **Identity** | Valuation Snapshot Reference (Period + Scope) |
| **Responsibilities** | Summarize owned inventory value excluding consignment not yet consumed; support reconciliation against general ledger; identify valuation variances; inform working capital and carrying cost analysis; exclude quarantined and in-transit stock per policy. |
| **Important Attributes** | Snapshot reference, valuation date, location scope, product lines (product, quantity, unit cost, extended value), total inventory value, ownership breakdown (owned / consignment), variance vs. general ledger, reconciliation status, prepared by |
| **Related Business Processes** | BP-30 (Inventory Valuation & Financial Reconciliation), BP-29 (Inventory Performance Reporting) |
| **Related Business Rules** | BR-008 (Three-Way Match Before Payment), BR-031 (Consignment Ownership at Consumption) |

---

## Entity Relationship Overview

The following diagram summarizes primary business relationships between core entities ( cardinality simplified for readability):

```
Supplier ──< Purchase Order ──< Expected Inbound Delivery
                    │
                    └──< Goods Receipt ──< Receipt Discrepancy
                              │
                              └── Put-Away ──> Stock Position <── Product
                                    │              │
Inventory Location ─────────────────┘              ├── Stock Policy
      │                                            ├── Inventory Reservation ── Customer Order
      └── Storage Position                         ├── Quarantine Hold
      │                                            ├── Promotional Stock Allocation
      └── Cycle Count / Physical Count ──> Count Variance ──> Stock Adjustment
      │                                                              │
      └── Transfer Request ──> Stock Transfer ──> In-Transit Stock   └── Inventory Write-Off
                                                                    │
Return Authorization ──> Customer Return ──> Return Disposition ────┘
                                                                    │
Customer Order ──> Fulfillment Execution ──> Shipment              │
                    └── Backorder                                   │
                                                                    ▼
                                              Inventory Movement Record ──> Audit Trail Record
```

---

## Entity-to-Process Traceability Matrix

| Entity | Primary Processes |
|--------|-------------------|
| Product | BP-01, BP-04, BP-07, BP-18, BP-22 |
| Inventory Location | BP-02, BP-10, BP-12, BP-24, BP-25 |
| Storage Position | BP-09, BP-18 |
| Stock Policy | BP-03, BP-21, BP-22 |
| Reason Code | BP-08, BP-14, BP-15 |
| Governance Policy | BP-13, BP-14, BP-32 |
| Stock Position | BP-10, BP-16, BP-17, BP-21 |
| Lot/Batch | BP-07, BP-09, BP-18, BP-25 |
| Quarantine Hold | BP-14, BP-20 |
| Promotional Stock Allocation | BP-31, BP-17 |
| Supplier | BP-05, BP-07, BP-30 |
| Purchase Requisition | BP-22 |
| Purchase Order | BP-05, BP-06, BP-07, BP-23 |
| Expected Inbound Delivery | BP-06, BP-23 |
| Goods Receipt | BP-07, BP-09 |
| Receipt Discrepancy | BP-08 |
| Put-Away | BP-09 |
| Supplier Invoice | BP-30 |
| Customer Order | BP-16, BP-17, BP-18, BP-19 |
| Inventory Reservation | BP-17 |
| Fulfillment Execution | BP-18, BP-20 |
| Backorder | BP-19 |
| Shipment | BP-18 |
| Transfer Request | BP-24 |
| Stock Transfer | BP-25 |
| In-Transit Stock | BP-25, BP-26 |
| Cycle Count | BP-11 |
| Physical Inventory Count | BP-12 |
| Count Variance | BP-13 |
| Stock Adjustment | BP-14 |
| Inventory Write-Off | BP-14, BP-15 |
| Return Authorization | BP-27 |
| Customer Return | BP-27, BP-28 |
| Return Disposition | BP-28 |
| Inventory Movement Record | BP-10, BP-29 (all transaction processes) |
| Audit Trail Record | BP-32 |
| Operational Alert | BP-21, BP-31 |
| User Account | Cross-cutting |
| Role Assignment | Cross-cutting |
| Inventory Valuation Snapshot | BP-30 |

---

## Entity-to-Business-Rule Traceability Matrix

| Business Rule | Primary Entities Governed |
|---------------|---------------------------|
| BR-001 | Stock Position, Customer Order, Inventory Reservation |
| BR-002 | Inventory Reservation, Stock Position |
| BR-003 | Fulfillment Execution, Shipment |
| BR-004 | Goods Receipt, Customer Return |
| BR-005 | Put-Away, Stock Position |
| BR-006 | Receipt Discrepancy, Goods Receipt |
| BR-007 | Purchase Order, Goods Receipt |
| BR-008 | Purchase Order, Goods Receipt, Supplier Invoice |
| BR-009 | Stock Policy, Stock Position, Operational Alert |
| BR-010 | Stock Policy, Inventory Reservation, Transfer Request |
| BR-011 | Transfer Request, Purchase Requisition, Stock Position |
| BR-012 | Transfer Request, Stock Transfer, Stock Policy |
| BR-013 | Quarantine Hold, Stock Position |
| BR-014 | Lot/Batch, Put-Away, Fulfillment Execution |
| BR-015 | Stock Position, Put-Away, Fulfillment Execution |
| BR-016 | Goods Receipt, Receipt Discrepancy, Lot/Batch |
| BR-017 | Lot/Batch, Goods Receipt, Inventory Movement Record |
| BR-018 | Cycle Count |
| BR-019 | Count Variance, Cycle Count, User Account |
| BR-020 | Stock Adjustment, Reason Code, Inventory Movement Record |
| BR-021 | Stock Adjustment, Count Variance, Governance Policy |
| BR-022 | Count Variance, Stock Adjustment |
| BR-023 | Inventory Write-Off, User Account |
| BR-024 | Physical Inventory Count, Inventory Location |
| BR-025 | Return Authorization, Customer Return |
| BR-026 | Return Disposition, Customer Return |
| BR-027 | Product, Purchase Order, Purchase Requisition |
| BR-028 | Backorder, Customer Order |
| BR-029 | Promotional Stock Allocation, Inventory Reservation |
| BR-030 | Quarantine Hold, Put-Away, Goods Receipt |
| BR-031 | Stock Position, Inventory Valuation Snapshot, Supplier |
| BR-032 | Product, Cycle Count, Operational Alert |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Solution Architect | | | |
| Senior Business Analyst | | | |
| Product Owner | | | |
| Inventory Controller | | | |

---

*End of Domain Entity Model*

*Document ID: SRS-DM-001 | Version 1.0 | July 5, 2026*
