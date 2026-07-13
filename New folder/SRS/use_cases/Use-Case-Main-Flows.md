# Use Case Main Flows
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-UC-002 |
| **Document Title** | Use Case Main Flows — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Business Analyst |
| **Source Document** | SRS-UC-001 (Use Case Catalog, v1.0) |
| **Date** | July 5, 2026 |
| **Scope** | Successful scenario only — no alternative or exception paths |

### Purpose

This document describes the main flow for each of the 48 use cases identified in the Use Case Catalog. Each flow specifies the actor action and corresponding system response for the successful completion of the business interaction.

### Flow Legend

| Column | Description |
|--------|-------------|
| **Step** | Sequential step number within the main flow |
| **Actor Action** | Action performed by the primary or supporting actor |
| **System Response** | Observable system behavior or outcome in response to the actor action |

---

## Domain 1: Master Data & Governance

### UC-001 — Manage Product Master Data

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens the product master management function. | System displays the product catalog with search and filter options. |
| 2 | Inventory Controller selects to create a new product or edit an existing product record. | System presents the product data entry form with required fields (SKU, name, description, unit of measure, category). |
| 3 | Inventory Controller enters or updates product attributes and product identifier (barcode) where applicable. | System validates required fields and checks for duplicate SKU or identifier. |
| 4 | Inventory Controller submits the product record for saving. | System saves the product master record and confirms successful creation or update. |
| 5 | Inventory Controller reviews the saved product record. | System displays the complete product profile with current status and attributes. |

---

### UC-002 — Configure Inventory Locations

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens the location management function. | System displays the inventory location network and hierarchy view. |
| 2 | Inventory Controller selects to create a new location or update an existing location. | System presents the location configuration form (name, type, parent location, status). |
| 3 | Inventory Controller defines location hierarchy and location attributes. | System validates location structure and confirms hierarchy assignment. |
| 4 | Inventory Controller establishes opening stock balances for location go-live where required. | System accepts opening balance entries by product and records initial on-hand quantities. |
| 5 | Inventory Controller activates the location for inventory operations. | System confirms location is active and available for stock assignment and transactions. |

---

### UC-003 — Define Stock Policies and Thresholds

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens stock policy configuration for a product or product group. | System displays current reorder level, minimum threshold, and safety stock settings. |
| 2 | Inventory Controller sets or updates reorder level and minimum stock threshold. | System accepts threshold values and validates against business policy limits. |
| 3 | Inventory Controller defines safety stock buffer quantity where applicable. | System records safety stock policy and associates it with the product and location scope. |
| 4 | Inventory Controller saves the stock policy configuration. | System confirms policy is saved and applies thresholds to availability monitoring. |
| 5 | Inventory Controller reviews the effective policy summary. | System displays the active policy with effective date and scope (product, location). |

---

### UC-004 — Classify Products by ABC Priority

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens ABC classification management. | System displays products with current classification status and classification criteria. |
| 2 | Inventory Controller reviews product velocity, revenue contribution, or criticality data. | System presents supporting product performance data for classification decisions. |
| 3 | Inventory Controller assigns ABC class (A, B, or C) to each product. | System accepts classification assignment per product. |
| 4 | Inventory Controller saves the classification update. | System confirms classification is saved and applies class-based monitoring and count frequency rules. |
| 5 | Inventory Controller reviews the updated ABC classification report. | System displays products grouped by class with classification effective date. |

---

### UC-005 — Maintain Governance Policies and Reason Codes

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens governance policy and reason code administration. | System displays the current reason code catalog and active governance policies. |
| 2 | Inventory Controller creates or updates a reason code category (e.g., adjustment, shrinkage, exception). | System presents reason code entry form with category and description fields. |
| 3 | Inventory Controller defines or updates inventory governance policy parameters. | System accepts policy definitions and associates them with applicable transaction types. |
| 4 | Inventory Controller activates the reason code or policy for operational use. | System validates completeness and confirms activation. |
| 5 | Inventory Controller reviews the published reason code and policy catalog. | System displays the active catalog available for use in inventory transactions. |

---

## Domain 2: Inbound & Receiving

### UC-006 — Place and Manage Purchase Orders

**Primary Actor:** Buyer

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Buyer opens purchase order management. | System displays open, pending, and historical purchase orders. |
| 2 | Buyer creates a new purchase order and selects supplier. | System presents purchase order entry form linked to supplier and authorized products. |
| 3 | Buyer enters product lines, quantities, expected delivery date, and delivery location. | System validates product eligibility (active status, not discontinued) and calculates order totals. |
| 4 | Buyer submits the purchase order for approval. | System routes the purchase order to Purchasing Manager and records pending approval status. |
| 5 | Purchasing Manager approves the purchase order. | System confirms purchase order as authorized and records expected inbound supply. |
| 6 | Buyer reviews the confirmed purchase order. | System displays approved purchase order with status, line details, and expected delivery information. |

---

### UC-007 — Plan Expected Inbound Deliveries

**Primary Actor:** Buyer

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Buyer opens inbound delivery planning for approved purchase orders. | System displays purchase orders with expected delivery dates and shipment status. |
| 2 | Buyer records or updates expected shipment date and carrier information from supplier confirmation. | System accepts delivery schedule and associates it with the purchase order. |
| 3 | Buyer communicates planned arrival to receiving location. | System updates inbound supply visibility for the destination warehouse. |
| 4 | Buyer confirms the inbound delivery plan. | System records planned inbound delivery and makes it visible to receiving and replenishment functions. |
| 5 | Buyer reviews the inbound delivery schedule. | System displays expected arrivals by date, location, and purchase order reference. |

---

### UC-008 — Receive and Verify Supplier Goods

**Primary Actor:** Receiving Clerk

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Receiving Clerk opens goods receipt for an arriving supplier shipment. | System displays expected purchase order lines and quantities for the delivery location. |
| 2 | Receiving Clerk identifies the shipment against the purchase order reference. | System retrieves matching purchase order and presents expected products and quantities. |
| 3 | Receiving Clerk scans or enters product identifier and verifies quantity and condition of each line. | System validates product identity against purchase order and records received quantities. |
| 4 | Receiving Clerk captures lot or batch number and shelf-life data for traceable products where required. | System records lot/batch attribution and validates minimum remaining shelf life. |
| 5 | Receiving Clerk confirms receipt verification is complete. | System records verified goods receipt, updates receipt status, and stages stock for put-away (not yet available for sale). |

---

### UC-009 — Document and Resolve Receipt Discrepancies

**Primary Actor:** Receiving Clerk

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Receiving Clerk identifies a discrepancy during goods verification (short, over, wrong item, or damage). | System presents discrepancy documentation form linked to the receipt line. |
| 2 | Receiving Clerk records discrepancy type, quantity variance, and supporting notes or evidence. | System captures discrepancy details with mandatory reason code and timestamp. |
| 3 | Receiving Clerk accepts verified quantities and documents unresolved variance separately. | System records accepted quantity for inventory and holds discrepancy record for resolution. |
| 4 | Warehouse Manager reviews and approves discrepancy resolution. | System confirms resolution action and updates receipt and discrepancy status. |
| 5 | Receiving Clerk completes the receipt with documented discrepancy. | System finalizes receipt record with accepted quantities and linked discrepancy documentation. |

---

### UC-010 — Perform Stock Put-Away

**Primary Actor:** Warehouse Staff

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Staff opens put-away tasks for verified received stock. | System displays received stock awaiting put-away with product, quantity, and suggested storage location. |
| 2 | Warehouse Staff retrieves stock from receiving area and moves it to designated storage location. | System records put-away in progress against the receipt reference. |
| 3 | Warehouse Staff confirms product, quantity, and destination storage location. | System validates storage location assignment and rotation rules (FIFO/FEFO) where applicable. |
| 4 | Warehouse Staff completes put-away confirmation. | System records put-away completion, updates on-hand quantity at storage location, and increases available-to-promise. |
| 5 | Warehouse Staff reviews completed put-away record. | System displays confirmed put-away with location, quantity, user, and timestamp. |

---

### UC-011 — Receive Return and Non-PO Inbound Stock

**Primary Actor:** Receiving Clerk

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Receiving Clerk opens non-PO or return receipt function. | System presents receipt type options (authorized return, ad-hoc receipt). |
| 2 | Receiving Clerk selects receipt type and enters or scans return authorization or ad-hoc receipt approval reference. | System validates authorization reference and retrieves linked order or approval details. |
| 3 | Receiving Clerk verifies product identity, quantity, and condition of inbound goods. | System records verified receipt lines against the authorization reference. |
| 4 | Receiving Clerk confirms receipt. | System records inbound receipt, stages stock for inspection or put-away per receipt type, and logs transaction with user and timestamp. |
| 5 | Receiving Clerk reviews the completed non-PO receipt record. | System displays receipt confirmation with reference, products, quantities, and next disposition status. |

---

## Domain 3: Inventory Visibility & Status

### UC-012 — Monitor Inventory Status

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens inventory status monitoring view. | System displays network-wide stock status summary by location, category, and status indicator. |
| 2 | Inventory Controller applies filters for location, product category, or status (in stock, low stock, out of stock). | System refreshes view with filtered inventory status results. |
| 3 | Inventory Controller reviews products at or below reorder level and out-of-stock conditions. | System highlights low-stock and out-of-stock items with threshold and ATP details. |
| 4 | Inventory Controller drills into a specific product or location for detail. | System displays on-hand, reserved, ATP, and quarantined quantities for the selection. |
| 5 | Inventory Controller completes status review. | System retains current monitoring view and last-reviewed timestamp for reference. |

---

### UC-013 — Inquire Inventory Availability

**Primary Actor:** Sales Representative

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Sales Representative opens inventory availability inquiry. | System presents product search by SKU, name, barcode, or category. |
| 2 | Sales Representative searches for the requested product. | System returns matching products with availability summary. |
| 3 | Sales Representative selects product and requests availability detail by location or network-wide. | System displays on-hand, reserved, and available-to-promise quantities per location and network total. |
| 4 | Sales Representative reviews stock status indicator (in stock, low stock, out of stock). | System presents current status and expected inbound quantity where applicable. |
| 5 | Sales Representative uses availability information to respond to customer inquiry. | System retains inquiry view for reference during the customer conversation. |

---

## Domain 4: Inventory Control & Accuracy

### UC-014 — Perform Cycle Count

**Primary Actor:** Warehouse Staff

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Staff opens assigned cycle count tasks. | System displays scheduled count assignments by product and location without revealing system expected quantity (blind count). |
| 2 | Warehouse Staff navigates to the assigned storage location and product. | System presents count entry form for the assigned SKU and location. |
| 3 | Warehouse Staff physically counts stock and enters the counted quantity. | System records the physical count result with counter identity and timestamp. |
| 4 | Warehouse Staff submits the completed count entry. | System saves count result, compares to system quantity internally, and flags variance if present. |
| 5 | Warehouse Staff reviews count submission confirmation. | System displays count submission status (recorded, variance pending review if applicable). |

---

### UC-015 — Conduct Full Physical Inventory Count

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller initiates a full physical inventory count for a location. | System activates physical inventory freeze for the location (suspends movements) and generates count sheets. |
| 2 | Inventory Controller assigns count teams and distributes count assignments. | System records count team assignments by zone, aisle, or product category. |
| 3 | Warehouse Staff perform wall-to-wall counts and enter physical quantities. | System records all count entries with counter identity and timestamp under freeze conditions. |
| 4 | Inventory Controller reviews count completion status across the location. | System displays count progress and identifies any uncounted locations or products. |
| 5 | Inventory Controller closes the physical count session. | System finalizes count snapshot, releases inventory freeze, and generates variance report for investigation. |

---

### UC-016 — Investigate and Approve Count Variances

**Primary Actor:** Warehouse Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Manager opens pending count variance queue. | System displays variances with product, location, system quantity, counted quantity, and variance amount. |
| 2 | Warehouse Manager selects a variance record for investigation. | System presents variance detail and investigation notes field. |
| 3 | Warehouse Manager documents investigation findings and root cause analysis. | System records investigation notes with investigator identity and timestamp. |
| 4 | Warehouse Manager approves the variance adjustment based on investigation. | System routes approval to independent approver if required by threshold; records approval decision. |
| 5 | Inventory Controller or authorized approver confirms variance approval. | System marks variance as approved and queues approved quantity adjustment for processing. |

---

### UC-017 — Process Stock Adjustments

**Primary Actor:** Warehouse Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Manager opens stock adjustment function. | System presents adjustment entry form with product, location, and current on-hand quantity. |
| 2 | Warehouse Manager selects product, location, adjustment direction (increase or decrease), and quantity. | System displays resulting quantity preview and requires reason code selection. |
| 3 | Warehouse Manager selects mandatory reason code and enters supporting notes. | System validates reason code and checks adjustment against approval threshold. |
| 4 | Warehouse Manager submits adjustment for approval where threshold requires independent authorization. | System routes to authorized approver; approver confirms adjustment. |
| 5 | Warehouse Manager confirms approved adjustment. | System applies quantity change, updates on-hand and ATP, and records adjustment in movement history with user, timestamp, and reason code. |

---

### UC-018 — Authorize and Process Inventory Write-Offs

**Primary Actor:** Operations Director

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Operations Director opens pending write-off requests. | System displays write-off requests with product, quantity, location, reason, and supporting documentation. |
| 2 | Operations Director reviews write-off evidence and business justification. | System presents complete write-off request detail and linked adjustment history. |
| 3 | Operations Director approves the write-off authorization. | System records authorization decision with approver identity and timestamp. |
| 4 | Finance Manager acknowledges financial impact where required. | System records finance acknowledgment and marks write-off as authorized. |
| 5 | Operations Director confirms write-off execution. | System removes inventory quantity from on-hand, records write-off transaction with reason code, and updates movement and audit history. |

---

### UC-019 — Manage Quarantine and Hold Stock

**Primary Actor:** Warehouse Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Manager opens quarantine and hold stock management. | System displays current quarantined and held inventory by location. |
| 2 | Warehouse Manager selects stock to place on quarantine or hold status. | System presents stock detail with current on-hand and ATP quantities. |
| 3 | Warehouse Manager assigns quarantine or hold reason and expected disposition. | System accepts hold reason and records hold initiation. |
| 4 | Warehouse Manager confirms quarantine placement. | System moves quantity from sellable ATP to quarantined status and excludes it from availability. |
| 5 | Warehouse Manager reviews updated stock status. | System displays product with quarantined quantity, hold reason, and date placed on hold. |

---

### UC-020 — Analyze Shrinkage, Loss, and Obsolete Stock

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens shrinkage and obsolescence analysis reports. | System displays shrinkage trends by reason code, location, and time period. |
| 2 | Inventory Controller reviews adjustment and write-off history grouped by loss category. | System presents summarized loss values and frequency by reason code. |
| 3 | Inventory Controller identifies slow-moving and obsolete product candidates. | System displays aging inventory report with days since last movement and excess quantity indicators. |
| 4 | Inventory Controller documents recommended actions for obsolete or slow-moving stock. | System records analysis notes and recommended disposition actions. |
| 5 | Inventory Controller shares analysis output with operations and finance stakeholders. | System generates exportable shrinkage and obsolescence analysis report. |

---

## Domain 5: Order Fulfillment

### UC-021 — Confirm Order Availability

**Primary Actor:** Sales Representative

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Sales Representative opens order availability confirmation for a customer order. | System presents order lines with requested products and quantities. |
| 2 | Sales Representative requests availability check for each order line. | System evaluates available-to-promise quantity by fulfillment location and network-wide. |
| 3 | Sales Representative reviews ATP result for each line (fully available, partially available, or unavailable). | System displays ATP quantity, fulfillment location options, and stock status per line. |
| 4 | Sales Representative confirms availability assessment with customer. | System records availability check result and timestamp against the order. |
| 5 | Sales Representative marks order as ready for confirmation or reservation. | System updates order availability status and indicates lines cleared for commitment. |

---

### UC-022 — Reserve Inventory for Confirmed Orders

**Primary Actor:** Customer Service Representative

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Customer Service Representative opens confirmed order for reservation. | System displays order lines with availability check results. |
| 2 | Customer Service Representative initiates inventory reservation for the order. | System validates ATP sufficiency for each line at selected fulfillment location. |
| 3 | Customer Service Representative confirms reservation quantities and fulfillment location per line. | System reserves on-hand quantity against the order and reduces ATP. |
| 4 | Customer Service Representative completes reservation. | System confirms reservation with reserved quantity, location, and reservation reference per line. |
| 5 | Customer Service Representative reviews reservation summary. | System displays order with reserved status and releases order to warehouse fulfillment queue. |

---

### UC-023 — Release Inventory Reservations

**Primary Actor:** Customer Service Representative

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Customer Service Representative opens order with active inventory reservation. | System displays reserved lines with reserved quantity and fulfillment location. |
| 2 | Customer Service Representative selects reservation to release (full order or specific lines). | System presents release confirmation with quantity to be returned to ATP. |
| 3 | Customer Service Representative confirms reservation release. | System removes reservation hold and restores quantity to available-to-promise. |
| 4 | Customer Service Representative records release reason where required. | System logs release reason, user, and timestamp in transaction history. |
| 5 | Customer Service Representative reviews updated order status. | System displays order with released reservation status and restored ATP. |

---

### UC-024 — Pick, Pack, and Ship Orders

**Primary Actor:** Warehouse Picker / Packer

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Picker / Packer opens fulfillment queue for assigned location. | System displays orders ready for picking with product, quantity, and storage location. |
| 2 | Warehouse Picker / Packer retrieves items from storage following rotation rules (FIFO/FEFO). | System presents pick list with location sequence and lot/batch guidance for traceable products. |
| 3 | Warehouse Picker / Packer scans or confirms each picked item and quantity. | System records pick verification per line with picker identity and timestamp. |
| 4 | Warehouse Picker / Packer packs verified items and prepares shipment with carrier documentation. | System updates order status to packed and presents shipment confirmation form. |
| 5 | Warehouse Picker / Packer confirms shipment handoff to carrier. | System deducts inventory from on-hand, clears reservation, records shipment, and updates order status to shipped. |

---

### UC-025 — Handle Partial Fulfillment and Backorders

**Primary Actor:** Customer Service Representative

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Customer Service Representative identifies order line with insufficient ATP for full quantity. | System displays available quantity versus ordered quantity per affected line. |
| 2 | Customer Service Representative presents partial fulfillment and backorder options to customer. | System presents fulfill-now quantity and backorder quantity with expected availability date if known. |
| 3 | Customer Service Representative records customer acceptance of partial shipment and backorder terms. | System captures customer acknowledgment for backordered quantity. |
| 4 | Customer Service Representative confirms partial fulfillment plan. | System reserves available quantity for immediate fulfillment and creates backorder record for remainder. |
| 5 | Customer Service Representative reviews updated order with split fulfillment status. | System displays order with shipped/pick-ready lines and backorder lines with expected fulfillment priority. |

---

### UC-026 — Handle Outbound Fulfillment Exceptions

**Primary Actor:** Warehouse Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Manager opens outbound exception queue. | System displays fulfillment exceptions (pick failure, quantity mismatch, damaged pick) with order and product detail. |
| 2 | Warehouse Manager reviews exception detail and physical investigation findings. | System presents pick record, system quantity, and reported exception reason. |
| 3 | Warehouse Manager determines resolution action (re-pick, substitute, partial ship, or quarantine). | System presents resolution options based on exception type. |
| 4 | Warehouse Manager authorizes resolution and documents reason. | System records resolution decision with manager authorization. |
| 5 | Warehouse Manager confirms exception resolution. | System updates order fulfillment status, adjusts inventory or quarantine as needed, and returns order to fulfillment flow or customer service. |

---

### UC-027 — View Order Fulfillment Status

**Primary Actor:** Customer Service Representative

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Customer Service Representative opens order fulfillment status inquiry. | System presents order search by order number, customer reference, or date. |
| 2 | Customer Service Representative selects the customer order. | System displays order header with current fulfillment status. |
| 3 | Customer Service Representative reviews line-level status (reserved, picking, packed, shipped, backordered). | System shows status, quantity, and fulfillment location per order line. |
| 4 | Customer Service Representative views shipment and carrier information for shipped lines. | System displays shipment date, carrier, and tracking reference where recorded. |
| 5 | Customer Service Representative uses status information to respond to customer inquiry. | System retains inquiry view with current real-time fulfillment status. |

---

## Domain 6: Replenishment & Inbound Supply

### UC-028 — Review Low-Stock and Out-of-Stock Alerts

**Primary Actor:** Purchasing Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Purchasing Manager opens low-stock and out-of-stock alert dashboard. | System displays active alerts by product, location, current ATP, and reorder threshold. |
| 2 | Purchasing Manager reviews alert priority based on ABC classification and severity. | System sorts and highlights priority alerts (Class A, out-of-stock conditions). |
| 3 | Purchasing Manager selects an alert for review. | System presents alert detail with stock history, open purchase orders, and network availability. |
| 4 | Purchasing Manager acknowledges the alert and assigns follow-up action. | System records alert acknowledgment with user and timestamp. |
| 5 | Purchasing Manager reviews remaining unacknowledged alerts. | System updates alert queue to reflect acknowledged items and pending actions. |

---

### UC-029 — Plan Replenishment and Create Purchase Requisitions

**Primary Actor:** Buyer

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Buyer opens replenishment planning from acknowledged low-stock alerts or suggestions. | System displays replenishment suggestions with recommended quantity, supplier, and network availability check results. |
| 2 | Buyer reviews network stock and confirms transfer is not preferred before purchase. | System shows excess stock at other locations and transfer alternatives. |
| 3 | Buyer creates purchase requisition with product, quantity, required date, and delivery location. | System validates product reorder eligibility and safety stock rules. |
| 4 | Buyer submits requisition for Purchasing Manager approval. | System routes requisition for approval and records pending status. |
| 5 | Purchasing Manager approves requisition. | System confirms approved requisition and makes it available for purchase order creation. |

---

### UC-030 — Track Inbound Supply Status

**Primary Actor:** Buyer

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Buyer opens inbound supply tracking view. | System displays open purchase orders with expected delivery dates and receipt status. |
| 2 | Buyer selects a purchase order to review supply status. | System presents PO lines with ordered, received, and outstanding quantities. |
| 3 | Buyer updates delivery status based on supplier communication. | System records revised expected delivery date and status. |
| 4 | Buyer reviews inbound supply position for replenishment planning. | System displays expected inbound quantity by product and arrival date. |
| 5 | Buyer confirms supply tracking review is complete. | System retains current inbound supply status for purchasing and receiving visibility. |

---

## Domain 7: Network Balance & Transfers

### UC-031 — Request Inter-Location Stock Transfer

**Primary Actor:** Regional / Store Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Regional / Store Manager opens inter-location transfer request. | System presents transfer request form with source and destination location options. |
| 2 | Regional / Store Manager selects source location, destination location, product, and requested quantity. | System validates source location ATP and checks source minimum threshold compliance. |
| 3 | Regional / Store Manager enters business justification for transfer. | System accepts justification and presents transfer impact preview. |
| 4 | Regional / Store Manager submits transfer request. | System records transfer request with pending approval status and notifies approver. |
| 5 | Regional / Store Manager reviews submitted transfer request. | System displays transfer request reference, status, and estimated source and destination impact. |

---

### UC-032 — Approve or Reject Transfer Requests

**Primary Actor:** Operations Director

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Operations Director opens pending transfer approval queue. | System displays transfer requests with source, destination, product, quantity, and requester. |
| 2 | Operations Director reviews transfer impact on source and destination service levels. | System presents source ATP after transfer, minimum threshold check, and destination need. |
| 3 | Operations Director approves the transfer request. | System records approval decision with approver identity and timestamp. |
| 4 | Operations Director confirms approval notification to source and destination locations. | System notifies Warehouse Manager at source and destination and updates transfer status to approved. |
| 5 | Operations Director reviews updated transfer pipeline. | System displays approved transfer ready for execution at source location. |

---

### UC-033 — Execute and Record Inter-Location Transfer

**Primary Actor:** Warehouse Staff

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Staff opens approved transfer dispatch at source location. | System displays approved transfer with product, quantity, and destination. |
| 2 | Warehouse Staff picks and verifies transfer quantity from source storage. | System records dispatch verification with lot/batch attribution where required. |
| 3 | Warehouse Staff confirms dispatch from source location. | System deducts quantity from source on-hand and records in-transit transfer status. |
| 4 | Warehouse Staff at destination receives and verifies transferred quantity. | System presents expected in-transit receipt for confirmation. |
| 5 | Warehouse Staff confirms receipt at destination. | System adds quantity to destination on-hand, clears in-transit status, and records complete transfer in movement history. |

---

### UC-034 — Analyze and Recommend Network Rebalancing

**Primary Actor:** Operations Director

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Operations Director opens network rebalancing analysis. | System displays location-level stock imbalances (stockout vs. excess) across the network. |
| 2 | Operations Director reviews rebalancing recommendations by product and location pair. | System presents suggested transfer quantities based on demand and excess positions. |
| 3 | Operations Director evaluates recommendations against service-level and transfer cost considerations. | System shows projected ATP impact at source and destination for each recommendation. |
| 4 | Operations Director approves selected rebalancing recommendations for transfer initiation. | System generates transfer requests from approved recommendations. |
| 5 | Operations Director reviews initiated rebalancing transfer pipeline. | System displays created transfer requests with status and network balance improvement summary. |

---

## Domain 8: Returns Management

### UC-035 — Authorize and Record Customer Returns

**Primary Actor:** Customer Service Representative

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Customer Service Representative opens customer return authorization. | System presents return request form with customer and order lookup. |
| 2 | Customer Service Representative locates original order and selects lines for return. | System displays original order lines with eligible return quantities per return policy. |
| 3 | Customer Service Representative validates return reason and return eligibility. | System confirms return policy compliance and calculates authorized return quantity. |
| 4 | Customer Service Representative issues return authorization to customer. | System generates return authorization reference with authorized products, quantities, and return destination. |
| 5 | Customer Service Representative reviews issued return authorization. | System displays active return authorization with status pending receipt. |

---

### UC-036 — Receive, Inspect, and Disposition Returned Goods

**Primary Actor:** Receiving Clerk

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Receiving Clerk opens return receipt against return authorization. | System retrieves return authorization with expected products and quantities. |
| 2 | Receiving Clerk receives returned goods and verifies quantity against authorization. | System records received return quantity per line. |
| 3 | Receiving Clerk inspects returned product condition. | System presents inspection form with condition assessment options (resalable, damaged, defective). |
| 4 | Receiving Clerk records inspection outcome and disposition decision (restock, quarantine, or write-off). | System accepts disposition with reason code and routes to appropriate next action. |
| 5 | Receiving Clerk confirms return processing completion. | System updates return status, applies restock to on-hand or routes to quarantine/write-off, and closes return authorization. |

---

## Domain 9: Reporting, Performance & Financial Alignment

### UC-037 — Review Inventory Dashboards and Operational Reports

**Primary Actor:** Operations Director

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Operations Director opens inventory management dashboard. | System displays inventory summary with on-hand value, stock status distribution, and alert counts. |
| 2 | Operations Director selects operational report (movement, stockout, overstock, accuracy, or location performance). | System generates report for selected type and default period. |
| 3 | Operations Director applies filters for location, category, or date range. | System refreshes report with filtered data. |
| 4 | Operations Director reviews report findings and identifies areas requiring action. | System presents report with drill-down capability to product and location detail. |
| 5 | Operations Director exports or saves report for management review. | System produces exportable report output with generation timestamp. |

---

### UC-038 — Review Inventory Performance KPIs

**Primary Actor:** Chief Executive Officer

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Chief Executive Officer opens executive inventory KPI dashboard. | System displays Tier 1 KPIs (accuracy, fill rate, turnover, stockout risk, on-time delivery). |
| 2 | Chief Executive Officer selects reporting period for KPI review. | System refreshes KPI values with period comparison to target and prior period. |
| 3 | Chief Executive Officer reviews KPI trend indicators and RAG status. | System presents KPI trends, targets, and red/amber/green status per metric. |
| 4 | Chief Executive Officer drills into underperforming KPI for contributing factors. | System displays breakdown by location, category, or product segment. |
| 5 | Chief Executive Officer completes executive KPI review. | System retains dashboard state and supports export for steering committee reporting. |

---

### UC-039 — Reconcile Inventory Valuation with Finance

**Primary Actor:** Finance Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Finance Manager opens inventory valuation reconciliation view. | System displays operational inventory valuation summary by location and category. |
| 2 | Finance Manager selects reconciliation period (e.g., month-end close). | System generates valuation report for the selected period with movement and adjustment detail. |
| 3 | Finance Manager compares operational valuation to general ledger inventory balance. | System presents side-by-side comparison with variance amount and percentage. |
| 4 | Finance Manager documents reconciliation adjustments or confirms alignment within tolerance. | System records reconciliation status and finance notes. |
| 5 | Finance Manager finalizes period reconciliation. | System marks reconciliation as complete and archives reconciliation record for audit. |

---

## Domain 10: Commercial Alignment & Governance

### UC-040 — Confirm Promotional and Launch Stock Readiness

**Primary Actor:** Marketing Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Marketing Manager opens promotional stock readiness review for upcoming campaign. | System displays campaign or launch definition with required products and quantities. |
| 2 | Marketing Manager reviews ring-fenced promotional stock allocation. | System shows allocated promotional quantity, consumed quantity, and remaining ring-fenced stock. |
| 3 | Marketing Manager verifies ATP and inbound supply against campaign requirement. | System presents readiness status per product (confirmed, at risk, short) against campaign start date. |
| 4 | Marketing Manager confirms stock readiness for campaign launch. | System records readiness confirmation with manager identity and confirmation date. |
| 5 | Marketing Manager reviews campaign readiness summary. | System displays overall launch readiness status and any remaining gaps. |

---

### UC-041 — Conduct Inventory Audit and Control Review

**Primary Actor:** Internal Auditor

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Internal Auditor opens inventory audit and control review workspace. | System presents audit query tools for transactions, approvals, and policy compliance. |
| 2 | Internal Auditor defines audit scope (period, location, transaction type). | System retrieves scoped transaction population for review. |
| 3 | Internal Auditor samples transactions and verifies segregation of duties compliance. | System displays transaction detail with initiator, approver, timestamp, and reason codes. |
| 4 | Internal Auditor tests control policy adherence (reason codes, approvals, blind counts). | System presents compliance indicators and flags potential control breaches. |
| 5 | Internal Auditor documents audit findings and completes control review. | System records audit review session and exports audit workpaper summary. |

---

## Domain 11: Cross-Cutting System Interactions

### UC-042 — View Inventory Movement and Transaction History

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens inventory movement history inquiry. | System presents search criteria (product, location, date range, transaction type, user). |
| 2 | Inventory Controller enters search criteria for the investigation scope. | System retrieves matching movement transactions. |
| 3 | Inventory Controller reviews transaction list summary. | System displays chronologically sorted movements with type, quantity, user, and timestamp. |
| 4 | Inventory Controller selects a transaction for detail. | System presents full transaction detail including before/after quantities, reason code, and reference document. |
| 5 | Inventory Controller exports movement history for analysis. | System generates exportable movement history report for the search scope. |

---

### UC-043 — Query and Review Audit Trail

**Primary Actor:** Internal Auditor

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Internal Auditor opens audit trail query function. | System presents audit search criteria (entity type, date range, user, action type). |
| 2 | Internal Auditor defines audit query parameters. | System retrieves immutable audit log entries matching criteria. |
| 3 | Internal Auditor reviews audit log summary results. | System displays audit entries with user, timestamp, action, and entity reference. |
| 4 | Internal Auditor selects entry to view before-and-after state detail. | System presents complete audit record with prior value, new value, and reason where applicable. |
| 5 | Internal Auditor exports audit trail results. | System generates exportable audit report suitable for external audit evidence. |

---

### UC-044 — Manage User Accounts and Role Assignments

**Primary Actor:** System Administrator

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | System Administrator opens user account management. | System displays user directory with account status and assigned roles. |
| 2 | System Administrator creates a new user account or selects existing account to modify. | System presents user profile form with identity, contact, and role assignment fields. |
| 3 | System Administrator assigns business role(s) and location scope to the user. | System validates role assignment against available roles and location definitions. |
| 4 | System Administrator activates the user account. | System creates or updates account, applies role permissions, and confirms activation. |
| 5 | System Administrator reviews user account summary. | System displays active account with assigned roles, location scope, and effective permissions summary. |

---

### UC-045 — Enforce Role-Based and Location-Scoped Access

**Primary Actor:** System Administrator

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | System Administrator configures role permission matrix and location scoping rules. | System displays role-to-permission mapping and location scope assignments. |
| 2 | System Administrator defines or updates permissions for a business role. | System accepts permission changes and validates against segregation of duties rules. |
| 3 | System Administrator saves access control configuration. | System applies updated permissions to all users assigned the affected role. |
| 4 | Authorized user signs in and accesses a permitted function within assigned location. | System authenticates user, evaluates role and location scope, and grants access to the function. |
| 5 | System Administrator reviews access enforcement log. | System displays successful access grants with user, function, location, and timestamp. |

---

### UC-046 — Import Initial Product and Stock Master Data

**Primary Actor:** Inventory Controller

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Inventory Controller opens initial data import function. | System presents import templates for product master and opening stock balances. |
| 2 | Inventory Controller prepares and uploads import file with product and stock data. | System validates file format and required field completeness. |
| 3 | Inventory Controller reviews import validation results. | System displays validation summary with record counts, errors, and warnings. |
| 4 | Inventory Controller confirms import execution for validated records. | System loads product master records and opening stock balances into the system. |
| 5 | Inventory Controller reviews import completion report. | System displays import results with created/updated record counts and confirms data availability for operations. |

---

### UC-047 — Receive and Respond to Operational Notifications

**Primary Actor:** Warehouse Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Manager opens notification inbox. | System displays pending notifications (low stock, approvals, exceptions, inbound delays, campaign alerts). |
| 2 | Warehouse Manager selects a notification to review. | System presents notification detail with linked business context (product, order, transfer, or campaign). |
| 3 | Warehouse Manager navigates to the related function to take action. | System opens the linked use case context (alert review, approval queue, exception record). |
| 4 | Warehouse Manager completes required action for the notification. | System records action completion against the notification. |
| 5 | Warehouse Manager marks notification as handled. | System archives notification and removes it from active pending queue. |

---

### UC-048 — Support Multi-Location Split Fulfillment

**Primary Actor:** Warehouse Manager

| Step | Actor Action | System Response |
|------|--------------|-----------------|
| 1 | Warehouse Manager opens order requiring split fulfillment across locations. | System displays order lines with single-location ATP shortfall and network-wide availability. |
| 2 | Warehouse Manager requests multi-location fulfillment plan. | System proposes fulfillment split by location with quantity per source location. |
| 3 | Warehouse Manager reviews and confirms split fulfillment allocation. | System creates location-specific reservations for each contributing location. |
| 4 | Warehouse Manager releases split fulfillment to respective warehouse queues. | System routes pick tasks to each source location with linked parent order reference. |
| 5 | Warehouse Manager monitors completion of all split shipment components. | System displays consolidated order status showing shipped/pending lines across all fulfillment locations. |

---

## Traceability

| Source Document | Reference |
|-----------------|-----------|
| Use Case Catalog | SRS-UC-001 (UC-001 through UC-048) |
| Business Requirements Document | BRD-IMS-001 |
| Business Rule Catalog | SRS-BR-001 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Business Analyst | | | |
| Product Owner | | | |
| Operations Director | | | |

---

*End of Use Case Main Flows*

*Document ID: SRS-UC-002 | Version 1.0 | July 5, 2026*
