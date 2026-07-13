# Database Indexing Strategy
## Inventory Management System — PostgreSQL

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-005 |
| **Document Title** | Database Indexing Strategy |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Database Performance Specialist |
| **Source Documents** | SRS-DB-002 (Physical Data Model), SRS-DB-003 (Database Keys), SRS-DB-004 (Database Constraints) |
| **Target Platform** | PostgreSQL 15+ |
| **Date** | July 6, 2026 |
| **Scope** | Index design and justification — no DDL/SQL statements |

### Purpose

This document defines the **indexing strategy** for the Inventory Management System. Indexes are chosen only where they support real query patterns from business operations — not as a default on every column. Each index includes junior-friendly performance explanation.

---

## Part 1: Indexing Principles (Junior Guide)

### What is an index?

An index is a **sorted lookup structure** (like a book index) that helps PostgreSQL find rows quickly without scanning the entire table.

| Without index | With index |
|---------------|------------|
| Full table scan — reads every row | Index seek — jumps to matching rows |
| Fast on tiny tables | Essential on large tables (millions of rows) |
| OK for rare admin queries | Required for high-frequency operational queries |

### Why indexes matter in IMS

The hottest path is: **"How much of product X is available at location Y?"** — asked on every order confirmation, reservation, and replenishment check. That query runs thousands of times per hour. A missing index here blocks the whole warehouse.

### How PostgreSQL uses an index

1. Query arrives: `WHERE product_id = 42 AND location_id = 7`
2. Planner checks: is there an index on `(product_id, location_id)`?
3. If yes → **Index Scan** — reads only matching pages (milliseconds)
4. If no → **Seq Scan** — reads all stock position rows (seconds at scale)

**Column order matters** in composite indexes: `(product_id, location_id)` helps `WHERE product_id = ?` and `WHERE product_id = ? AND location_id = ?`, but is weaker for `WHERE location_id = ?` alone. Design indexes to match real `WHERE` clauses.

### Costs of too many indexes

| Benefit | Cost |
|---------|------|
| Faster SELECT | Slower INSERT/UPDATE/DELETE (every index must be updated) |
| Faster JOIN | More disk space |
| Faster ORDER BY | More memory during maintenance (VACUUM, REINDEX) |

**Rule:** Index for queries that run **often** and **filter/join** on the indexed columns. Do not index "just in case."

### Index types used in this system

| Type | When to use | IMS example |
|------|-------------|-------------|
| **B-tree** (default) | Equality, range, sorting, most FK lookups | `stock_positions (product_id, location_id)` |
| **Partial B-tree** | Frequent queries on a **subset** of rows | Active reservations only: `WHERE reservation_status = 'ACTIVE'` |
| **BRIN** | Very large time-ordered tables (append-only logs) | `movement_timestamp` on movement records |
| **GIN** | JSONB containment queries (rare) | `audit_trail_records.before_state` — only if JSON search needed |

**Not used:** Hash indexes (no advantage over B-tree in modern PostgreSQL), GiST (no spatial data in IMS).

---

## Part 2: Index Tiers

| Tier | Purpose | Count | Maintenance |
|------|---------|-------|-------------|
| **Tier 1 — Critical** | Hot-path operational queries; system fails SLA without these | 18 | Monitor weekly |
| **Tier 2 — Operational** | High-volume workflows; noticeable slowdown if missing | 22 | Monitor monthly |
| **Tier 3 — Reporting & audit** | Dashboards, history, compliance; tolerates slightly slower reads | 12 | Review quarterly |
| **Implicit (UNIQUE/PK)** | Created automatically by constraints — do not duplicate | ~75 | Maintained with constraints |

**Total explicit indexes defined:** 52 (excluding PK/UK implicit indexes)

---

## Part 3: Tier 1 — Critical Indexes

These support the highest-frequency queries. Deploy in the initial migration.

---

### IDX-001

| Attribute | Detail |
|-----------|--------|
| **Table** | `inventory.stock_positions` |
| **Indexed columns** | `(product_id, location_id)` |
| **Index type** | B-tree **UNIQUE** (implicit via `uk_stock_positions_product_location`) |
| **Expected query pattern** | `SELECT * FROM stock_positions WHERE product_id = ? AND location_id = ?` |
| **Business justification** | Central ATP lookup for order confirmation (BR-001), reservation (BR-002), and replenishment (BR-009). One row per SKU per site. |
| **Performance clarity (junior)** | **Why:** Every order check asks "do we have stock here?" **How:** UNIQUE constraint automatically creates this B-tree index — PostgreSQL finds the single matching row in O(log n) time instead of scanning all balances. **Do not create a duplicate non-unique index** on the same columns. |

---

### IDX-002

| Attribute | Detail |
|-----------|--------|
| **Table** | `catalog.products` |
| **Indexed columns** | `sku` |
| **Index type** | B-tree **UNIQUE** (implicit via `uk_products_sku`) |
| **Expected query pattern** | `SELECT id FROM products WHERE sku = ?` |
| **Business justification** | SKU is the ubiquitous lookup key at receipt, pick, and catalog integration. |
| **Performance clarity (junior)** | **Why:** External systems and scanners send SKU strings, not internal `id`. **How:** UNIQUE index on `sku` converts string lookup to fast seek before any stock operation. |

---

### IDX-003

| Attribute | Detail |
|-----------|--------|
| **Table** | `catalog.product_identifiers` |
| **Indexed columns** | `(identifier_type, identifier_value)` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT product_id FROM product_identifiers WHERE identifier_type = 'BARCODE' AND identifier_value = ?` |
| **Business justification** | Barcode scan at receiving dock and pick face (BR-004). Wrong index = slow scan response. |
| **Performance clarity (junior)** | **Why:** Warehouse staff scan barcodes, not SKUs. **How:** Composite UK lets PostgreSQL resolve barcode → product_id in one index lookup. |

---

### IDX-004

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.inventory_reservations` |
| **Indexed columns** | `(stock_position_id)` WHERE `reservation_status = 'ACTIVE'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM inventory_reservations WHERE stock_position_id = ? AND reservation_status = 'ACTIVE'` |
| **Business justification** | Only active reservations affect ATP; released/fulfilled rows are historical noise (BR-002). |
| **Performance clarity (junior)** | **Why:** Table grows with all historical reservations but queries care about ACTIVE rows only. **How:** Partial index stores only active rows — smaller, faster, cheaper to maintain than a full composite index on `(stock_position_id, reservation_status)`. **Note:** Do not also create a non-partial index on the same columns — one index only. |

---

### IDX-005

| Attribute | Detail |
|-----------|--------|
| **Table** | `inventory.lot_batches` |
| **Indexed columns** | `(stock_position_id, expiration_date)` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM lot_batches WHERE stock_position_id = ? ORDER BY expiration_date ASC LIMIT 1` |
| **Business justification** | FEFO pick — earliest expiring lot first at a specific bin (BR-014). |
| **Performance clarity (junior)** | **Why:** Picker needs "which lot expires first at this bin?" **How:** Index sorted by `expiration_date` within each `stock_position_id` avoids sorting thousands of lots at pick time. |

---

### IDX-006

| Attribute | Detail |
|-----------|--------|
| **Table** | `inventory.lot_batches` |
| **Indexed columns** | `(product_id, expiration_date)` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM lot_batches WHERE product_id = ? AND expiration_date > CURRENT_DATE ORDER BY expiration_date` |
| **Business justification** | Network-wide FEFO and recall scope queries across locations. |
| **Performance clarity (junior)** | **Why:** Quality team asks "all lots of product X expiring soon network-wide." **How:** Product_id narrows scope; expiration_date supports range scan and ORDER BY. |

---

### IDX-008

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.customer_orders` |
| **Indexed columns** | `(order_status, order_date DESC)` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM customer_orders WHERE order_status IN ('CONFIRMED','PARTIAL') ORDER BY order_date DESC LIMIT 50` |
| **Business justification** | Open order queue for warehouse dashboard and fulfillment planning. |
| **Performance clarity (junior)** | **Why:** Warehouse managers view "orders needing action today." **How:** `order_status` filters open orders; `order_date DESC` returns newest first without separate sort step. |

---

### IDX-009

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.customer_orders` |
| **Indexed columns** | `order_number` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT * FROM customer_orders WHERE order_number = ?` |
| **Business justification** | Customer service and integration lookup by order number. |
| **Performance clarity (junior)** | **Why:** Call center searches by order number constantly. **How:** UK provides index automatically — no extra index needed. |

---

### IDX-010

| Attribute | Detail |
|-----------|--------|
| **Table** | `network.inventory_locations` |
| **Indexed columns** | `location_code` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT id FROM inventory_locations WHERE location_code = ?` |
| **Business justification** | Location code used in UI, reports, and cross-system references. |
| **Performance clarity (junior)** | **Why:** Users think in "WH-01" not internal id 7. **How:** UK on location_code — implicit index, do not duplicate. |

---

### IDX-011

| Attribute | Detail |
|-----------|--------|
| **Table** | `inventory.stock_positions` |
| **Indexed columns** | `(location_id, stock_status)` WHERE `stock_status IN ('LOW_STOCK','OUT_OF_STOCK')` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM stock_positions WHERE location_id = ? AND stock_status IN ('LOW_STOCK','OUT_OF_STOCK')` |
| **Business justification** | Low-stock alert generation and replenishment review (BR-009, BR-032). |
| **Performance clarity (junior)** | **Why:** Replenishment team monitors exceptions, not every IN_STOCK row. **How:** Partial index includes only alert-worthy rows — tiny index, fast scan per location. Most rows are IN_STOCK and excluded. |

---

### IDX-012

| Attribute | Detail |
|-----------|--------|
| **Table** | `procurement.purchase_orders` |
| **Indexed columns** | `po_number` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT * FROM purchase_orders WHERE po_number = ?` |
| **Business justification** | PO lookup at receiving dock and three-way match (BR-007, BR-008). |
| **Performance clarity (junior)** | **Why:** Receiver scans/types PO number on every inbound shipment. **How:** UK provides index — no duplicate needed. |

---

### IDX-013

| Attribute | Detail |
|-----------|--------|
| **Table** | `inbound.goods_receipts` |
| **Indexed columns** | `purchase_order_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM goods_receipts WHERE purchase_order_id = ?` |
| **Business justification** | "What has been received against this PO?" — receiving and match workflows. |
| **Performance clarity (junior)** | **Why:** Three-way match joins invoice → PO → all receipts for that PO. **How:** FK column is not auto-indexed in PostgreSQL — explicit index required for JOIN performance. |

---

### IDX-014

| Attribute | Detail |
|-----------|--------|
| **Table** | `procurement.purchase_order_lines` |
| **Indexed columns** | `(purchase_order_id, product_id)` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM purchase_order_lines WHERE purchase_order_id = ? AND product_id = ?` |
| **Business justification** | Receipt verification against specific PO line (BR-004, BR-007). |
| **Performance clarity (junior)** | **Why:** Receiver confirms "PO line for SKU X." **How:** Composite index matches both filter columns — one seek instead of fetching all PO lines. |

---

### IDX-015

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.customer_order_lines` |
| **Indexed columns** | `customer_order_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM customer_order_lines WHERE customer_order_id = ?` |
| **Business justification** | Load all lines when opening an order for reservation and fulfillment. |
| **Performance clarity (junior)** | **Why:** Every order detail screen loads header + lines. **How:** Index on FK parent id — classic parent-child pattern. Without it, full scan of all order lines in the system. |

---

### IDX-016

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.inventory_reservations` |
| **Indexed columns** | `order_line_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM inventory_reservations WHERE order_line_id = ?` |
| **Business justification** | Find reservation for order line during ship and cancellation. |
| **Performance clarity (junior)** | **Why:** Shipment consumes reservation per order line. **How:** Direct lookup by line id when processing fulfillment. |

---

### IDX-017

| Attribute | Detail |
|-----------|--------|
| **Table** | `inventory.stock_policies` |
| **Indexed columns** | `(product_id, location_id)` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT * FROM stock_policies WHERE product_id = ? AND location_id = ?` |
| **Business justification** | Threshold lookup paired with stock position for reorder alerts (BR-009). |
| **Performance clarity (junior)** | **Why:** ATP status compared to reorder level on same product+location key. **How:** UK mirrors stock_positions key — often joined together; both have implicit indexes. |

---

### IDX-018

| Attribute | Detail |
|-----------|--------|
| **Table** | `identity.user_accounts` |
| **Indexed columns** | `user_identifier` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT * FROM user_accounts WHERE user_identifier = ?` |
| **Business justification** | Login and attribution on every transactional row. |
| **Performance clarity (junior)** | **Why:** Every operation records "who did it." **How:** UK on login id — implicit index at authentication time. |

---

## Part 4: Tier 2 — Operational Indexes

High-volume workflows beyond the absolute hot path.

---

### IDX-019

| Attribute | Detail |
|-----------|--------|
| **Table** | `inbound.goods_receipt_lines` |
| **Indexed columns** | `goods_receipt_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM goods_receipt_lines WHERE goods_receipt_id = ?` |
| **Business justification** | Load receipt lines for verification and put-away. |
| **Performance clarity (junior)** | **Why:** Parent-child document pattern. **How:** Index on receipt header FK — same pattern as order lines. |

---

### IDX-020

| Attribute | Detail |
|-----------|--------|
| **Table** | `inbound.put_aways` |
| **Indexed columns** | `goods_receipt_line_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM put_aways WHERE goods_receipt_line_id = ?` |
| **Business justification** | Check put-away completion before ATP increase (BR-005). |
| **Performance clarity (junior)** | **Why:** System asks "is this receipt line put away yet?" **How:** Direct lookup on receipt line FK. |

---

### IDX-021

| Attribute | Detail |
|-----------|--------|
| **Table** | `procurement.purchase_orders` |
| **Indexed columns** | `(supplier_id, po_status)` WHERE `po_status IN ('OPEN','PARTIAL')` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM purchase_orders WHERE supplier_id = ? AND po_status IN ('OPEN','PARTIAL')` |
| **Business justification** | Open PO list per supplier for receiving and AP. |
| **Performance clarity (junior)** | **Why:** Buyers care about open POs, not 5 years of closed history. **How:** Partial index shrinks size by excluding CLOSED/CANCELLED rows. |

---

### IDX-022

| Attribute | Detail |
|-----------|--------|
| **Table** | `finance.supplier_invoices` |
| **Indexed columns** | `purchase_order_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM supplier_invoices WHERE purchase_order_id = ?` |
| **Business justification** | Three-way match PO leg (BR-008). |
| **Performance clarity (junior)** | **Why:** AP clerk finds invoices for a PO. **How:** FK index for JOIN in match workflow. |

---

### IDX-023

| Attribute | Detail |
|-----------|--------|
| **Table** | `finance.supplier_invoices` |
| **Indexed columns** | `(supplier_id, invoice_number)` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT * FROM supplier_invoices WHERE supplier_id = ? AND invoice_number = ?` |
| **Business justification** | Duplicate invoice detection. |
| **Performance clarity (junior)** | **Why:** UK enforces uniqueness and serves lookup — no extra index. |

---

### IDX-024

| Attribute | Detail |
|-----------|--------|
| **Table** | `finance.invoice_goods_receipt_match` |
| **Indexed columns** | `goods_receipt_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM invoice_goods_receipt_match WHERE goods_receipt_id = ?` |
| **Business justification** | Reverse lookup: which invoices matched this receipt. |
| **Performance clarity (junior)** | **Why:** UK covers `(supplier_invoice_id, goods_receipt_id)` but queries from receipt side need `goods_receipt_id` leading column. **How:** Second index justified — different access path than UK. |

---

### IDX-025

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.fulfillment_executions` |
| **Indexed columns** | `customer_order_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM fulfillment_executions WHERE customer_order_id = ?` |
| **Business justification** | Pick queue per order. |
| **Performance clarity (junior)** | **Why:** Warehouse loads pick work for one order. **How:** Standard FK parent index. |

---

### IDX-026

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.fulfillment_executions` |
| **Indexed columns** | `(fulfillment_location_id, pick_verification_status)` WHERE `pick_verification_status = 'PENDING'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM fulfillment_executions WHERE fulfillment_location_id = ? AND pick_verification_status = 'PENDING'` |
| **Business justification** | Warehouse pick queue by location. |
| **Performance clarity (junior)** | **Why:** Pickers see only pending work at their site. **How:** Partial index on PENDING rows only — verified picks are dead for queue purposes. |

---

### IDX-027

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.shipments` |
| **Indexed columns** | `customer_order_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM shipments WHERE customer_order_id = ?` |
| **Business justification** | Order tracking and shipment history. |
| **Performance clarity (junior)** | **Why:** Customer service views shipments for an order. **How:** FK index on order. |

---

### IDX-028

| Attribute | Detail |
|-----------|--------|
| **Table** | `fulfillment.backorders` |
| **Indexed columns** | `(resolution_status, product_id)` WHERE `resolution_status = 'OPEN'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM backorders WHERE resolution_status = 'OPEN' AND product_id = ?` |
| **Business justification** | Replenishment priority for open backorders (BR-028). |
| **Performance clarity (junior)** | **Why:** Planners ask "what SKUs have open backorders?" **How:** Partial index on OPEN only — fulfilled backorders excluded. |

---

### IDX-029

| Attribute | Detail |
|-----------|--------|
| **Table** | `transfer.stock_transfers` |
| **Indexed columns** | `(destination_location_id, transfer_status)` WHERE `transfer_status = 'IN_TRANSIT'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM stock_transfers WHERE destination_location_id = ? AND transfer_status = 'IN_TRANSIT'` |
| **Business justification** | Expected inbound transfers at destination (BR-012). |
| **Performance clarity (junior)** | **Why:** Destination warehouse prepares for incoming transfers. **How:** Small partial index — few IN_TRANSIT rows at any time. |

---

### IDX-030

| Attribute | Detail |
|-----------|--------|
| **Table** | `transfer.in_transit_stock` |
| **Indexed columns** | `stock_transfer_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM in_transit_stock WHERE stock_transfer_id = ?` |
| **Business justification** | Pipeline detail for active transfer. |
| **Performance clarity (junior)** | **Why:** Child rows of transfer header. **How:** FK index — composition pattern. |

---

### IDX-031

| Attribute | Detail |
|-----------|--------|
| **Table** | `inventory.quarantine_holds` |
| **Indexed columns** | `(stock_position_id)` WHERE `hold_status = 'ACTIVE'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT SUM(held_qty) FROM quarantine_holds WHERE stock_position_id = ? AND hold_status = 'ACTIVE'` |
| **Business justification** | ATP calculation excludes active holds (BR-013). |
| **Performance clarity (junior)** | **Why:** Same pattern as reservations — only ACTIVE holds reduce ATP. **How:** Partial index for sum aggregation per stock position. |

---

### IDX-032

| Attribute | Detail |
|-----------|--------|
| **Table** | `network.storage_positions` |
| **Indexed columns** | `(location_id, position_code)` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT id FROM storage_positions WHERE location_id = ? AND position_code = ?` |
| **Business justification** | Put-away and pick bin lookup. |
| **Performance clarity (junior)** | **Why:** "Put this in bin A-01-03 at WH-01." **How:** UK provides composite index — no duplicate. |

---

### IDX-033

| Attribute | Detail |
|-----------|--------|
| **Table** | `network.inventory_locations` |
| **Indexed columns** | `parent_location_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM inventory_locations WHERE parent_location_id = ?` |
| **Business justification** | Hierarchy roll-up — list child sites under region. |
| **Performance clarity (junior)** | **Why:** Reports aggregate by region. **How:** Index on self-referencing FK — tree traversal from parent to children. |

---

### IDX-034

| Attribute | Detail |
|-----------|--------|
| **Table** | `accuracy.cycle_counts` |
| **Indexed columns** | `(location_id, count_status, schedule_date)` WHERE `count_status IN ('SCHEDULED','IN_PROGRESS')` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM cycle_counts WHERE location_id = ? AND count_status IN ('SCHEDULED','IN_PROGRESS') ORDER BY schedule_date` |
| **Business justification** | Counter work queue (BR-018). |
| **Performance clarity (junior)** | **Why:** Counters see today's assignments at their warehouse. **How:** Partial index excludes completed historical counts. |

---

### IDX-035

| Attribute | Detail |
|-----------|--------|
| **Table** | `accuracy.count_variances` |
| **Indexed columns** | `(approval_status, investigation_status)` WHERE `approval_status = 'PENDING'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM count_variances WHERE approval_status = 'PENDING' ORDER BY created_at` |
| **Business justification** | Approver work queue (BR-019, BR-021). |
| **Performance clarity (junior)** | **Why:** Managers approve pending variances — not thousands of old approved rows. **How:** Partial index on PENDING only. |

---

### IDX-036

| Attribute | Detail |
|-----------|--------|
| **Table** | `accuracy.stock_adjustments` |
| **Indexed columns** | `(approval_status)` WHERE `approval_status = 'PENDING'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM stock_adjustments WHERE approval_status = 'PENDING'` |
| **Business justification** | Adjustment approval queue (BR-021). |
| **Performance clarity (junior)** | **Why:** Same approval-queue pattern as variances. **How:** Tiny partial index of pending items. |

---

### IDX-037

| Attribute | Detail |
|-----------|--------|
| **Table** | `returns.return_authorizations` |
| **Indexed columns** | `customer_order_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM return_authorizations WHERE customer_order_id = ?` |
| **Business justification** | RMA history per order (BR-025). |
| **Performance clarity (junior)** | **Why:** Customer service checks return eligibility on original order. **How:** FK index. |

---

### IDX-038

| Attribute | Detail |
|-----------|--------|
| **Table** | `returns.return_authorizations` |
| **Indexed columns** | `rma_number` |
| **Index type** | B-tree **UNIQUE** (implicit via UK) |
| **Expected query pattern** | `SELECT * FROM return_authorizations WHERE rma_number = ?` |
| **Business justification** | Warehouse scans RMA at return dock. |
| **Performance clarity (junior)** | **Why:** UK on rma_number — implicit index, no duplicate. |

---

### IDX-039

| Attribute | Detail |
|-----------|--------|
| **Table** | `procurement.purchase_requisitions` |
| **Indexed columns** | `(approval_status)` WHERE `approval_status IN ('SUBMITTED','APPROVED')` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM purchase_requisitions WHERE approval_status = 'SUBMITTED'` |
| **Business justification** | Buyer approval queue. |
| **Performance clarity (junior)** | **Why:** Buyers approve submitted requisitions — not drafts or converted. **How:** Partial index on workflow-active states. |

---

### IDX-040

| Attribute | Detail |
|-----------|--------|
| **Table** | `transfer.transfer_requests` |
| **Indexed columns** | `(request_status)` WHERE `request_status = 'SUBMITTED'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM transfer_requests WHERE request_status = 'SUBMITTED'` |
| **Business justification** | Transfer approval queue (BR-012). |
| **Performance clarity (junior)** | **Why:** Operations director approves pending transfers. **How:** Partial index — small pending set. |

---

## Part 5: Tier 3 — Reporting & Audit Indexes

---

### IDX-041

| Attribute | Detail |
|-----------|--------|
| **Table** | `audit.inventory_movement_records` |
| **Indexed columns** | `(stock_position_id, movement_timestamp DESC)` |
| **Index type** | B-tree (per monthly partition) |
| **Expected query pattern** | `SELECT * FROM inventory_movement_records WHERE stock_position_id = ? ORDER BY movement_timestamp DESC LIMIT 100` |
| **Business justification** | Stock position history for investigation and audit (BO-19). |
| **Performance clarity (junior)** | **Why:** "Show me last 100 movements for this SKU at this site." **How:** Composite index with DESC timestamp — PostgreSQL reads index backward for recent-first without sort. **Partition note:** Create this index on each monthly partition, not only parent table. |

---

### IDX-042

| Attribute | Detail |
|-----------|--------|
| **Table** | `audit.inventory_movement_records` |
| **Indexed columns** | `movement_timestamp` |
| **Index type** | **BRIN** |
| **Expected query pattern** | `SELECT COUNT(*) FROM inventory_movement_records WHERE movement_timestamp BETWEEN ? AND ?` |
| **Business justification** | Time-range reporting on very large append-only log (10M+ rows/year). |
| **Performance clarity (junior)** | **Why:** BRIN is tiny compared to B-tree on timestamp — stores min/max per block range. **How:** Perfect for append-only data inserted in time order. **When NOT to use:** Point lookups by stock_position_id — use IDX-041 instead. BRIN complements, does not replace IDX-041. |

---

### IDX-043

| Attribute | Detail |
|-----------|--------|
| **Table** | `audit.audit_trail_records` |
| **Indexed columns** | `(affected_entity_type, affected_entity_id, event_timestamp DESC)` |
| **Index type** | B-tree (per monthly partition) |
| **Expected query pattern** | `SELECT * FROM audit_trail_records WHERE affected_entity_type = 'stock_adjustments' AND affected_entity_id = ? ORDER BY event_timestamp DESC` |
| **Business justification** | Compliance audit trail per entity (BR-019, BO-19). |
| **Performance clarity (junior)** | **Why:** Auditor asks "full history of changes to adjustment #12345." **How:** Polymorphic lookup by type + id, sorted by time. |

---

### IDX-044

| Attribute | Detail |
|-----------|--------|
| **Table** | `audit.operational_alerts` |
| **Indexed columns** | `(acknowledgment_status, alert_type, severity)` WHERE `acknowledgment_status = 'OPEN'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM operational_alerts WHERE acknowledgment_status = 'OPEN' ORDER BY severity DESC, alert_date` |
| **Business justification** | Alert dashboard and replenishment review (BR-009, BR-032). |
| **Performance clarity (junior)** | **Why:** Users see open alerts only — resolved alerts purged after 90 days. **How:** Partial index keeps dashboard query fast as alert table grows. |

---

### IDX-045

| Attribute | Detail |
|-----------|--------|
| **Table** | `audit.inventory_valuation_snapshots` |
| **Indexed columns** | `(valuation_date DESC, location_scope)` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM inventory_valuation_snapshots WHERE location_scope = 'NETWORK' ORDER BY valuation_date DESC LIMIT 12` |
| **Business justification** | Month-end valuation history (BR-031, BP-30). |
| **Performance clarity (junior)** | **Why:** Finance views last 12 monthly snapshots — low volume table, simple index sufficient. |

---

### IDX-046

| Attribute | Detail |
|-----------|--------|
| **Table** | `audit.inventory_valuation_lines` |
| **Indexed columns** | `snapshot_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM inventory_valuation_lines WHERE snapshot_id = ?` |
| **Business justification** | Load snapshot detail lines for reconciliation report. |
| **Performance clarity (junior)** | **Why:** Parent-child report pattern. **How:** FK index on snapshot header. |

---

### IDX-047

| Attribute | Detail |
|-----------|--------|
| **Table** | `inventory.stock_policy_history` |
| **Indexed columns** | `(stock_policy_id, effective_from DESC)` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM stock_policy_history WHERE stock_policy_id = ? ORDER BY effective_from DESC` |
| **Business justification** | Threshold change audit for replenishment analysis. |
| **Performance clarity (junior)** | **Why:** Planner reviews "when did reorder level change?" **How:** History lookup by policy id, recent first. |

---

### IDX-048

| Attribute | Detail |
|-----------|--------|
| **Table** | `identity.role_assignments` |
| **Indexed columns** | `(user_account_id)` WHERE `assignment_status = 'ACTIVE'` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM role_assignments WHERE user_account_id = ? AND assignment_status = 'ACTIVE'` |
| **Business justification** | Authorization check on every API request. |
| **Performance clarity (junior)** | **Why:** Login loads active roles only — not historical inactive assignments. **How:** Partial index for permission resolution. |

---

### IDX-049

| Attribute | Detail |
|-----------|--------|
| **Table** | `identity.role_assignment_locations` |
| **Indexed columns** | `role_assignment_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT location_id FROM role_assignment_locations WHERE role_assignment_id = ?` |
| **Business justification** | Location scope check for warehouse operations. |
| **Performance clarity (junior)** | **Why:** After loading roles, load scoped locations. **How:** FK child index. |

---

### IDX-050

| Attribute | Detail |
|-----------|--------|
| **Table** | `commercial.promotional_stock_allocations` |
| **Indexed columns** | `(product_id, readiness_status)` WHERE `readiness_status IN ('PLANNED','READY','ACTIVE')` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM promotional_stock_allocations WHERE product_id = ? AND readiness_status = 'ACTIVE'` |
| **Business justification** | Campaign readiness review (BR-029). |
| **Performance clarity (junior)** | **Why:** Small table, few active campaigns — partial index for active/planned only. |

---

### IDX-051

| Attribute | Detail |
|-----------|--------|
| **Table** | `commercial.promotional_allocation_locations` |
| **Indexed columns** | `stock_position_id` |
| **Index type** | B-tree |
| **Expected query pattern** | `SELECT * FROM promotional_allocation_locations WHERE stock_position_id = ?` |
| **Business justification** | Check ring-fence when reserving stock (BR-029). |
| **Performance clarity (junior)** | **Why:** Reservation service asks "is this balance ring-fenced for a campaign?" **How:** Reverse lookup from stock position to active allocation. |

---

### IDX-052

| Attribute | Detail |
|-----------|--------|
| **Table** | `governance.governance_policies` |
| **Indexed columns** | `(policy_type, effective_from DESC)` WHERE `is_active = TRUE AND effective_to IS NULL` |
| **Index type** | **Partial B-tree** |
| **Expected query pattern** | `SELECT * FROM governance_policies WHERE policy_type = 'APPROVAL_THRESHOLD' AND is_active = TRUE AND effective_to IS NULL` |
| **Business justification** | Load current effective policy for approval threshold check (BR-021). |
| **Performance clarity (junior)** | **Why:** Only current active policies matter at runtime — not retired versions. **How:** Partial index on "currently effective" rows. |

---

## Part 6: Indexes Explicitly NOT Created

Avoiding unnecessary indexes is as important as creating the right ones.

| Table / Column | Why NOT indexed | Junior explanation |
|----------------|-----------------|-------------------|
| `products.description` | Never in WHERE/JOIN; TEXT search not required in IMS | Full table scan on description search would need full-text (GIN) only if search feature added later |
| `products.category_code` | Low-selectivity filter alone; network reports use stock_positions join | Index on low-cardinality column alone rarely helps unless combined in composite with high-selectivity column |
| Every FK automatically | PostgreSQL does **not** auto-index FKs | Only index FKs that appear in JOIN/WHERE on the **child** side of frequent queries |
| `stock_positions.product_id` alone | Covered by UK `(product_id, location_id)` leftmost prefix | Composite UK already helps `WHERE product_id = ?` — separate single-column index is redundant |
| `customer_orders.customer_reference` | Optional, low-cardinality, rare lookup | Add only if CRM integration requires frequent search by customer_reference |
| `shipments.tracking_identifier` | Lookup only after ship; nullable; not hot path | Index when carrier tracking portal integration is confirmed |
| `goods_receipts.supplier_id` | Receipts usually found by PO or GR number, not supplier | Supplier performance reports are batch — acceptable sequential scan with date filter |
| `audit_trail_records.before_state` (JSONB) | No JSON containment queries in scope | GIN index is large — add only if "search audit JSON" feature is built |
| Duplicate index on `reservation_status` alone | Low cardinality (3 values) without leading selective column | Always combine with `stock_position_id` in partial index |
| `inventory_write_offs`, `stock_adjustments` by `stock_position_id` | Low volume; approval queues use status partial indexes | Historical adjustment lookup is rare — add if investigation tool requires it |
| All `created_at` columns | Rarely filtered alone; use composite with status | `WHERE created_at > ?` alone causes large index — prefer `(status, created_at)` if date filtering needed |

---

## Part 7: Index Maintenance Guide (Junior)

### Monitoring

| Check | Tool | Frequency |
|-------|------|-----------|
| Unused indexes | `pg_stat_user_indexes` where `idx_scan = 0` | Monthly |
| Bloated indexes | `pgstatindex` or pg_repack | Quarterly |
| Slow queries missing indexes | `pg_stat_statements`, EXPLAIN ANALYZE | Weekly on Tier 1 |

### When INSERT/UPDATE feels slow

Ask: **did we add an index we don't use?** Each extra index adds write cost. Check `idx_scan` — if zero after 30 days in production, drop the index.

### Partial index reminder

```text
-- Conceptual example (not DDL for deployment)
Index: reservations WHERE status = 'ACTIVE'
Stores: only active rows
Query must include: reservation_status = 'ACTIVE' (or equivalent) for index to be used
```

If the query omits the `WHERE status = 'ACTIVE'` predicate, PostgreSQL cannot use the partial index.

### Partitioned tables

`inventory_movement_records` and `audit_trail_records` are partitioned by month. **Indexes must exist on each partition** (PostgreSQL 11+ can create on parent and propagate). BRIN on `movement_timestamp` works well **inside** each partition.

---

## Part 8: Index Summary Matrix

| Schema | Tier 1 | Tier 2 | Tier 3 | Implicit UK/PK |
|--------|--------|--------|--------|----------------|
| `catalog` | 3 | 0 | 0 | 3 |
| `network` | 1 | 2 | 0 | 2 |
| `inventory` | 4 | 1 | 1 | 3 |
| `procurement` | 2 | 2 | 0 | 4 |
| `inbound` | 1 | 2 | 0 | 1 |
| `finance` | 0 | 3 | 0 | 1 |
| `fulfillment` | 4 | 5 | 0 | 1 |
| `transfer` | 0 | 2 | 0 | 1 |
| `accuracy` | 0 | 3 | 0 | 4 |
| `returns` | 0 | 1 | 0 | 1 |
| `commercial` | 0 | 0 | 2 | 1 |
| `identity` | 1 | 0 | 2 | 2 |
| `governance` | 0 | 0 | 1 | 2 |
| `audit` | 0 | 0 | 6 | 2 |
| **Total explicit** | **16** | **21** | **12** | **~28 used** |

*Note: Several Tier 1 entries document implicit UK/PK indexes only. Total explicit indexes to CREATE: **49**.*

---

## Part 9: Query Pattern → Index Quick Reference

| Business operation | Query pattern | Index |
|------------------|---------------|-------|
| Confirm order availability | `stock_positions BY product_id + location_id` | UK implicit (IDX-001) |
| Scan barcode at receipt | `product_identifiers BY type + value` | UK implicit (IDX-003) |
| Reserve stock | `reservations ACTIVE BY stock_position_id` | IDX-004 partial |
| FEFO pick | `lot_batches BY stock_position_id ORDER BY expiration` | IDX-005 |
| Open order dashboard | `customer_orders BY status + date` | IDX-008 |
| Low stock alert | `stock_positions LOW/OUT at location` | IDX-011 partial |
| Receive against PO | `goods_receipts BY purchase_order_id` | IDX-013 |
| Three-way match | `invoices + receipts BY purchase_order_id` | IDX-013, IDX-022 |
| Pick queue | `fulfillment_executions PENDING at location` | IDX-026 partial |
| Approval queues | `* WHERE approval_status = 'PENDING'` | IDX-035, IDX-036 partial |
| Movement history | `movement_records BY position + timestamp` | IDX-041 |
| Open alerts | `operational_alerts OPEN` | IDX-044 partial |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Database Performance Specialist | | | |
| Database Architect | | | |
| DDD Solution Architect | | | |

---

*End of Database Indexing Strategy*

*Document ID: SRS-DB-005 | Version 1.0 | July 6, 2026*
