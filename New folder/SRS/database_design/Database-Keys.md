# Database Keys Specification
## Inventory Management System — PostgreSQL

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-003 |
| **Document Title** | Database Keys — Primary, Foreign, Unique, and Candidate Keys |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Database Architect |
| **Source Documents** | SRS-DB-002 (Physical Data Model, v1.0), SRS-DB-001 (Logical Data Model, v1.0) |
| **Target Platform** | PostgreSQL 15+ |
| **Date** | July 6, 2026 |
| **Scope** | Key definitions and business justification — no DDL/SQL statements |

### Purpose

This document defines all **database keys** for the 59 tables in the Inventory Management System physical model. For each table it identifies primary keys, foreign keys, unique keys, and candidate keys, with business justification aligned to domain rules (BR-001 – BR-032) and aggregate boundaries.

### Key Design Principles

| Principle | Rationale |
|-----------|-----------|
| **Surrogate primary key** | Every table uses `id BIGINT GENERATED ALWAYS AS IDENTITY` as PK — stable, narrow, immune to business identifier format changes |
| **Business key as unique constraint** | Natural identifiers (`sku`, `po_number`, `order_number`) enforced as `UNIQUE` alternate keys for human lookup and external integration |
| **Composite uniqueness for documents** | Header + `line_number` uniqueness on all document line tables prevents duplicate lines and supports ordered business documents |
| **Dimensional uniqueness** | Product + Location composite UK on stock positions and policies enforces "one balance per SKU per site" invariant |
| **Referential integrity via FK** | Parent-child and cross-schema references use foreign keys; optional deferred FKs on cross-bounded-context links where eventual consistency applies |
| **Candidate keys documented** | All business-viable unique identifiers recorded even when not enforced as UK — guides future constraints and integration contracts |

### Key Notation

| Symbol | Meaning |
|--------|---------|
| **PK** | Primary Key — cluster identity, join anchor |
| **FK** | Foreign Key — referential integrity to parent table |
| **UK** | Unique Key — enforced uniqueness constraint |
| **CK** | Candidate Key — business identifier capable of unique identification; may or may not be enforced as UK |

---

## Domain 1: Catalog

---

### `catalog.products`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_products` | Stable internal reference for all inventory transactions; SKU format may evolve without breaking FKs across millions of movement records |
| **UK** | `sku` | `uk_products_sku` | SKU is the canonical business identity (BR-027 gatekeeper); must be globally unique — two products cannot share a stock keeping unit |
| **FK** | `created_by` → `identity.user_accounts.id` | `fk_products_created_by` | Attributes product master creation to an accountable user for audit (BO-19) |
| **CK** | `sku` | — | Primary natural key; selected as UK because it is the ubiquitous language term used in all operational documents |
| **CK** | `(sku, lifecycle_status)` | — | Not unique globally but identifies product state context; not enforced — status changes would violate UK |

---

### `catalog.product_identifiers`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_product_identifiers` | Surrogate PK for alternate identifiers that may be added/retired without affecting product PK |
| **FK** | `product_id` → `catalog.products.id` | `fk_product_identifiers_product` | Identifier belongs to exactly one product; composition within Product Catalog aggregate |
| **UK** | `(identifier_type, identifier_value)` | `uk_product_identifiers_type_value` | A barcode/GTIN must map to one product globally — duplicate scan codes cause wrong picks and receipts (BR-004) |
| **UK** | `(product_id, identifier_type, identifier_value)` | `uk_product_identifiers_product_type_value` | Prevents duplicate identifier rows on same product |
| **CK** | `identifier_value` (when `is_primary = TRUE`) | — | Primary scan code per product; enforced via partial unique index concept: one primary per product |

---

## Domain 2: Network

---

### `network.inventory_locations`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_inventory_locations` | Stable anchor for all stock balances, receipts, and fulfillments at a site |
| **UK** | `location_code` | `uk_inventory_locations_code` | Location code is the business identity used on POs, transfers, and reports; must be unique across the network |
| **FK** | `parent_location_id` → `network.inventory_locations.id` | `fk_inventory_locations_parent` | Optional hierarchy (region → site); self-reference enables roll-up reporting without duplicating location records |
| **FK** | `responsible_manager_id` → `identity.user_accounts.id` | `fk_inventory_locations_manager` | Assigns operational accountability for location performance |
| **CK** | `location_code` | — | Primary natural key; used in cross-aggregate identity references per DDD architecture |
| **CK** | `(location_code, operational_status)` | — | Identifies location in a given state; not UK because status transitions are frequent |

---

### `network.storage_positions`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_storage_positions` | Surrogate PK for bin-level addresses that may be reconfigured |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_storage_positions_location` | Position cannot exist outside parent location — composition within Inventory Location aggregate (REL-004) |
| **FK** | `dedicated_product_id` → `catalog.products.id` | `fk_storage_positions_product` | Optional dedicated-product bin assignment |
| **UK** | `(location_id, position_code)` | `uk_storage_positions_location_code` | Position code unique within location only — "A-01-03" may repeat at different warehouses |
| **CK** | `(location_id, zone, aisle, bin)` | — | Physical address composite; not enforced as UK because addressing scheme may have gaps |

---

## Domain 3: Governance

---

### `governance.governance_policies`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_governance_policies` | Supports policy versioning without recycling business codes |
| **UK** | `(policy_code, effective_from)` | `uk_governance_policies_code_effective` | One version per policy code per effective period — prevents overlapping policy versions (BR-021) |
| **CK** | `policy_code` | — | Human-readable policy reference; not alone unique due to versioning |
| **CK** | `(policy_type, applicable_scope, effective_from)` | — | Identifies active policy for a scope at a point in time; used by application lookup |

---

### `governance.reason_codes`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_reason_codes` | Stable reference for historical adjustments even after code retirement |
| **UK** | `reason_code` | `uk_reason_codes_code` | Reason code is the business taxonomy key — mandatory on adjustments (BR-020); must not duplicate |
| **FK** | `approval_threshold_id` → `governance.governance_policies.id` | `fk_reason_codes_policy` | Links reason category to approval threshold when material |
| **CK** | `reason_code` | — | Primary natural key; selected as UK |

---

## Domain 4: Inventory Balance

---

### `inventory.stock_positions`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_stock_positions` | Hot-path join key for reservations, movements, and adjustments — narrow BIGINT for lock efficiency |
| **UK** | `(product_id, location_id)` | `uk_stock_positions_product_location` | **Core domain invariant** — exactly one balance per SKU per location; prevents split-brain ATP (BR-001, REL-019, REL-020) |
| **FK** | `product_id` → `catalog.products.id` | `fk_stock_positions_product` | Balance tracks a valid catalog product |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_stock_positions_location` | Balance anchored to a valid location |
| **CK** | `(product_id, location_id)` | — | Primary candidate key; enforced as UK |
| **CK** | `(product_id, location_id, ownership_type)` | — | Not unique — ownership is attribute not identity |

---

### `inventory.lot_batches`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_lot_batches` | Surrogate PK; lot numbers may repeat across products |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_lot_batches_stock_position` | Lot quantity belongs to parent stock position — composition (REL-023) |
| **FK** | `product_id` → `catalog.products.id` | `fk_lot_batches_product` | Denormalized for FEFO queries without joining through stock position |
| **FK** | `supplier_id` → `procurement.suppliers.id` | `fk_lot_batches_supplier` | Traceability to supplier origin for recall (BR-017, REL-134) |
| **UK** | `(product_id, lot_number, stock_position_id)` | `uk_lot_batches_product_lot_position` | Same lot may exist at one position once; supports lot-level quantity tracking |
| **CK** | `(product_id, lot_number)` | — | Lot identity within product scope per domain model; may span positions via separate rows |

---

### `inventory.quarantine_holds`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_quarantine_holds` | Surrogate PK for hold lifecycle management |
| **UK** | `hold_reference` | `uk_quarantine_holds_reference` | Business document number for hold tracking and customs clearance (BR-030) |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_quarantine_holds_stock_position` | Hold applied to specific balance — composition (REL-022) |
| **FK** | `lot_batch_id` → `inventory.lot_batches.id` | `fk_quarantine_holds_lot` | Optional lot-scoped hold for targeted recall (REL-028) |
| **FK** | `authorized_by` → `identity.user_accounts.id` | `fk_quarantine_holds_authorized_by` | Hold authorization accountability |
| **CK** | `hold_reference` | — | Primary business document key |

---

### `inventory.stock_policies`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_stock_policies` | Surrogate PK; thresholds versioned via history table |
| **UK** | `(product_id, location_id)` | `uk_stock_policies_product_location` | One replenishment policy per SKU per location — mirrors stock position identity (REL-008, REL-009) |
| **FK** | `product_id` → `catalog.products.id` | `fk_stock_policies_product` | Policy scoped to product |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_stock_policies_location` | Policy scoped to location |
| **CK** | `(product_id, location_id)` | — | Primary candidate key; same composite as stock position |

---

### `inventory.stock_policy_history`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_stock_policy_history` | Append-only history rows |
| **FK** | `stock_policy_id` → `inventory.stock_policies.id` | `fk_stock_policy_history_policy` | History belongs to parent policy |
| **FK** | `changed_by` → `identity.user_accounts.id` | `fk_stock_policy_history_changed_by` | Threshold change attribution |
| **UK** | `(stock_policy_id, effective_from)` | `uk_stock_policy_history_policy_from` | Non-overlapping history periods per policy |
| **CK** | `(stock_policy_id, effective_from, effective_to)` | — | Identifies a specific threshold version window |

---

## Domain 5: Procurement

---

### `procurement.suppliers`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_suppliers` | Stable vendor reference across PO, receipt, and invoice chains |
| **UK** | `supplier_code` | `uk_suppliers_code` | Supplier code is commercial identity — unique counterparty for procurement (BR-007, BR-008) |
| **CK** | `supplier_code` | — | Primary natural key |

---

### `procurement.purchase_requisitions`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_purchase_requisitions` | Surrogate PK for requisition lifecycle |
| **UK** | `requisition_number` | `uk_purchase_requisitions_number` | Internal document number for approval workflow traceability |
| **FK** | `requesting_location_id` → `network.inventory_locations.id` | `fk_purchase_requisitions_location` | Replenishment need anchored to destination site (REL-036) |
| **FK** | `triggering_alert_id` → `audit.operational_alerts.id` | `fk_purchase_requisitions_alert` | Links requisition to low-stock alert that triggered it (REL-038, BR-009) |
| **FK** | `approved_by` → `identity.user_accounts.id` | `fk_purchase_requisitions_approved_by` | Approval accountability |
| **FK** | `purchase_order_id` → `procurement.purchase_orders.id` | `fk_purchase_requisitions_po` | Conversion traceability — requisition to PO (REL-037) |
| **FK** | `created_by` → `identity.user_accounts.id` | `fk_purchase_requisitions_created_by` | Initiator attribution |
| **CK** | `requisition_number` | — | Primary business document key |

---

### `procurement.purchase_requisition_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_purchase_requisition_lines` | Line-level surrogate PK |
| **FK** | `requisition_id` → `procurement.purchase_requisitions.id` | `fk_purchase_requisition_lines_req` | Line belongs to parent requisition |
| **FK** | `product_id` → `catalog.products.id` | `fk_purchase_requisition_lines_product` | Line references active product — discontinued blocked (BR-027) |
| **UK** | `(requisition_id, line_number)` | `uk_purchase_requisition_lines_req_line` | Ordered line sequence unique within requisition |
| **CK** | `(requisition_id, product_id)` | — | Not UK — same product could theoretically appear on amended lines; line_number disambiguates |

---

### `procurement.purchase_orders`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_purchase_orders` | Stable PO reference for receipt and three-way match |
| **UK** | `po_number` | `uk_purchase_orders_number` | PO number is authorization document for inbound receipt (BR-007) |
| **FK** | `supplier_id` → `procurement.suppliers.id` | `fk_purchase_orders_supplier` | Commercial commitment to vendor (REL-039) |
| **FK** | `receiving_location_id` → `network.inventory_locations.id` | `fk_purchase_orders_location` | Designated receipt site (REL-040) |
| **FK** | `created_by` → `identity.user_accounts.id` | `fk_purchase_orders_created_by` | Buyer attribution |
| **CK** | `po_number` | — | Primary natural key |
| **CK** | `(supplier_id, po_number)` | — | Redundant when po_number is globally unique; supplier-scoped numbering alternative if numbering scheme changes |

---

### `procurement.purchase_order_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_purchase_order_lines` | Line surrogate PK |
| **FK** | `purchase_order_id` → `procurement.purchase_orders.id` | `fk_purchase_order_lines_po` | Line belongs to PO |
| **FK** | `product_id` → `catalog.products.id` | `fk_purchase_order_lines_product` | Ordered product — discontinued prohibited (BR-027, REL-041) |
| **UK** | `(purchase_order_id, line_number)` | `uk_purchase_order_lines_po_line` | Unique line sequence within PO |
| **CK** | `(purchase_order_id, product_id)` | — | Identifies product on PO; not UK if same SKU ordered on multiple lines intentionally |

---

### `procurement.expected_inbound_deliveries`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_expected_inbound_deliveries` | Surrogate PK |
| **UK** | `delivery_reference` | `uk_expected_inbound_deliveries_ref` | Shipment plan business identifier |
| **FK** | `purchase_order_id` → `procurement.purchase_orders.id` | `fk_expected_inbound_deliveries_po` | Delivery subordinate to PO — composition (REL-042) |
| **FK** | `receiving_location_id` → `network.inventory_locations.id` | `fk_expected_inbound_deliveries_location` | Expected arrival site |
| **CK** | `delivery_reference` | — | Primary business key |

---

### `procurement.expected_inbound_delivery_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_expected_inbound_delivery_lines` | Line surrogate PK |
| **FK** | `delivery_id` → `procurement.expected_inbound_deliveries.id` | `fk_expected_inbound_delivery_lines_delivery` | Line belongs to delivery plan |
| **FK** | `purchase_order_line_id` → `procurement.purchase_order_lines.id` | `fk_expected_inbound_delivery_lines_pol` | Links expected qty to authorized PO line (REL-045) |
| **FK** | `product_id` → `catalog.products.id` | `fk_expected_inbound_delivery_lines_product` | Product denormalized for visibility queries |
| **UK** | `(delivery_id, purchase_order_line_id)` | `uk_expected_inbound_delivery_lines` | One expected quantity entry per PO line per delivery |

---

## Domain 6: Inbound

---

### `inbound.goods_receipts`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_goods_receipts` | Receipt document anchor for put-away and three-way match |
| **UK** | `gr_number` | `uk_goods_receipts_number` | Goods receipt number is operational document identity (BR-004) |
| **FK** | `purchase_order_id` → `procurement.purchase_orders.id` | `fk_goods_receipts_po` | PO authorization for receipt (BR-007, REL-043); nullable for ad-hoc exception |
| **FK** | `supplier_id` → `procurement.suppliers.id` | `fk_goods_receipts_supplier` | Supplier accountability (REL-048) |
| **FK** | `receiving_location_id` → `network.inventory_locations.id` | `fk_goods_receipts_location` | Receipt site — blocked when frozen (BR-024, REL-049) |
| **FK** | `receiving_clerk_id` → `identity.user_accounts.id` | `fk_goods_receipts_clerk` | Receiving clerk attribution (REL-126) |
| **CK** | `gr_number` | — | Primary business document key |

---

### `inbound.goods_receipt_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_goods_receipt_lines` | Line surrogate PK |
| **FK** | `goods_receipt_id` → `inbound.goods_receipts.id` | `fk_goods_receipt_lines_gr` | Line belongs to receipt |
| **FK** | `purchase_order_line_id` → `procurement.purchase_order_lines.id` | `fk_goods_receipt_lines_pol` | Verification against PO line |
| **FK** | `product_id` → `catalog.products.id` | `fk_goods_receipt_lines_product` | Received product identity |
| **FK** | `lot_batch_id` → `inventory.lot_batches.id` | `fk_goods_receipt_lines_lot` | Lot captured at receipt (BR-017, REL-052) |
| **UK** | `(goods_receipt_id, line_number)` | `uk_goods_receipt_lines_gr_line` | Unique line sequence within receipt |

---

### `inbound.receipt_discrepancies`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_receipt_discrepancies` | Surrogate PK |
| **UK** | `discrepancy_reference` | `uk_receipt_discrepancies_ref` | Exception document for supplier claims (BR-006) |
| **FK** | `goods_receipt_id` → `inbound.goods_receipts.id` | `fk_receipt_discrepancies_gr` | Discrepancy subordinate to receipt — composition (REL-050) |
| **FK** | `goods_receipt_line_id` → `inbound.goods_receipt_lines.id` | `fk_receipt_discrepancies_gr_line` | Optional line-level discrepancy |
| **FK** | `product_id` → `catalog.products.id` | `fk_receipt_discrepancies_product` | Affected product |
| **FK** | `reason_code_id` → `governance.reason_codes.id` | `fk_receipt_discrepancies_reason` | Categorized discrepancy (REL-013) |
| **CK** | `discrepancy_reference` | — | Primary business key |

---

### `inbound.put_aways`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_put_aways` | Surrogate PK |
| **UK** | `put_away_reference` | `uk_put_aways_reference` | Put-away confirmation document (BR-005) |
| **FK** | `goods_receipt_id` → `inbound.goods_receipts.id` | `fk_put_aways_gr` | Put-away completes receipt workflow (REL-051) |
| **FK** | `goods_receipt_line_id` → `inbound.goods_receipt_lines.id` | `fk_put_aways_gr_line` | Line-level put-away |
| **FK** | `product_id` → `catalog.products.id` | `fk_put_aways_product` | Product placed |
| **FK** | `storage_position_id` → `network.storage_positions.id` | `fk_put_aways_position` | Destination bin (REL-017) |
| **FK** | `lot_batch_id` → `inventory.lot_batches.id` | `fk_put_aways_lot` | Lot placement for traceable products |
| **FK** | `performed_by` → `identity.user_accounts.id` | `fk_put_aways_performed_by` | Warehouse staff attribution |
| **CK** | `put_away_reference` | — | Primary business key |

---

## Domain 7: Finance

---

### `finance.supplier_invoices`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_supplier_invoices` | Invoice anchor for payment authorization |
| **UK** | `(supplier_id, invoice_number)` | `uk_supplier_invoices_supplier_number` | Invoice numbers unique within supplier scope — standard AP practice (REL-057) |
| **FK** | `supplier_id` → `procurement.suppliers.id` | `fk_supplier_invoices_supplier` | Billing counterparty |
| **FK** | `purchase_order_id` → `procurement.purchase_orders.id` | `fk_supplier_invoices_po` | PO leg of three-way match (BR-008, REL-055) |
| **CK** | `invoice_number` | — | Not globally unique — supplier-scoped UK enforced |

---

### `finance.supplier_invoice_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_supplier_invoice_lines` | Line surrogate PK |
| **FK** | `supplier_invoice_id` → `finance.supplier_invoices.id` | `fk_supplier_invoice_lines_invoice` | Line belongs to invoice |
| **FK** | `purchase_order_line_id` → `procurement.purchase_order_lines.id` | `fk_supplier_invoice_lines_pol` | Match to authorized PO line |
| **FK** | `product_id` → `catalog.products.id` | `fk_supplier_invoice_lines_product` | Billed product |
| **UK** | `(supplier_invoice_id, line_number)` | `uk_supplier_invoice_lines_inv_line` | Unique line sequence |

---

### `finance.invoice_goods_receipt_match`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_invoice_goods_receipt_match` | Associative table surrogate PK |
| **FK** | `supplier_invoice_id` → `finance.supplier_invoices.id` | `fk_inv_gr_match_invoice` | Invoice in match set |
| **FK** | `goods_receipt_id` → `inbound.goods_receipts.id` | `fk_inv_gr_match_gr` | Receipt in match set (BR-008, REL-056) |
| **UK** | `(supplier_invoice_id, goods_receipt_id)` | `uk_inv_gr_match_pair` | One match record per invoice-receipt pair |

---

## Domain 8: Fulfillment

---

### `fulfillment.customer_orders`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_customer_orders` | Order anchor for reservations, picks, and shipments |
| **UK** | `order_number` | `uk_customer_orders_number` | Order number is customer-facing and integration identity |
| **CK** | `order_number` | — | Primary natural key |
| **CK** | `(customer_reference, order_number)` | — | External CRM correlation when order numbers are channel-scoped |

---

### `fulfillment.customer_order_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_customer_order_lines` | Line surrogate PK |
| **FK** | `customer_order_id` → `fulfillment.customer_orders.id` | `fk_customer_order_lines_order` | Line belongs to order — composition |
| **FK** | `product_id` → `catalog.products.id` | `fk_customer_order_lines_product` | Ordered SKU |
| **FK** | `fulfillment_location_id` → `network.inventory_locations.id` | `fk_customer_order_lines_location` | Ship-from site for line |
| **UK** | `(customer_order_id, line_number)` | `uk_customer_order_lines_order_line` | Unique ordered line sequence |

---

### `fulfillment.inventory_reservations`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_inventory_reservations` | Reservation surrogate PK |
| **UK** | `reservation_reference` | `uk_inventory_reservations_ref` | Operational hold document (BR-002) |
| **FK** | `customer_order_id` → `fulfillment.customer_orders.id` | `fk_inventory_reservations_order` | Reservation serves order (REL-065) |
| **FK** | `order_line_id` → `fulfillment.customer_order_lines.id` | `fk_inventory_reservations_line` | Line-level reservation |
| **FK** | `product_id` → `catalog.products.id` | `fk_inventory_reservations_product` | Reserved SKU (REL-066) |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_inventory_reservations_location` | Reservation location |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_inventory_reservations_position` | Modifies specific balance — ATP reduction (REL-024) |
| **CK** | `reservation_reference` | — | Primary business key |

---

### `fulfillment.fulfillment_executions`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_fulfillment_executions` | Pick/pack work unit PK |
| **UK** | `fulfillment_reference` | `uk_fulfillment_executions_ref` | Warehouse work document |
| **FK** | `customer_order_id` → `fulfillment.customer_orders.id` | `fk_fulfillment_executions_order` | Execution fulfills order (REL-067) |
| **FK** | `fulfillment_location_id` → `network.inventory_locations.id` | `fk_fulfillment_executions_location` | Pick site (REL-068) |
| **FK** | `assigned_picker_id` → `identity.user_accounts.id` | `fk_fulfillment_executions_picker` | Picker attribution |
| **CK** | `fulfillment_reference` | — | Primary business key |

---

### `fulfillment.fulfillment_pick_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_fulfillment_pick_lines` | Pick line surrogate PK |
| **FK** | `fulfillment_execution_id` → `fulfillment.fulfillment_executions.id` | `fk_fulfillment_pick_lines_fe` | Pick belongs to execution |
| **FK** | `order_line_id` → `fulfillment.customer_order_lines.id` | `fk_fulfillment_pick_lines_ol` | Fulfills order line |
| **FK** | `product_id` → `catalog.products.id` | `fk_fulfillment_pick_lines_product` | Picked product |
| **FK** | `storage_position_id` → `network.storage_positions.id` | `fk_fulfillment_pick_lines_position` | Source bin (REL-018) |
| **FK** | `lot_batch_id` → `inventory.lot_batches.id` | `fk_fulfillment_pick_lines_lot` | Lot on pick (BR-017, REL-069) |
| **UK** | `(fulfillment_execution_id, order_line_id)` | `uk_fulfillment_pick_lines_fe_ol` | One pick line per order line per execution |

---

### `fulfillment.backorders`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_backorders` | Backorder surrogate PK |
| **UK** | `backorder_reference` | `uk_backorders_ref` | Customer-agreed delay document (BR-028) |
| **FK** | `customer_order_id` → `fulfillment.customer_orders.id` | `fk_backorders_order` | Backorder on order (REL-071) |
| **FK** | `order_line_id` → `fulfillment.customer_order_lines.id` | `fk_backorders_line` | Line-level backorder |
| **FK** | `product_id` → `catalog.products.id` | `fk_backorders_product` | Awaiting SKU (REL-072) |
| **CK** | `backorder_reference` | — | Primary business key |

---

### `fulfillment.shipments`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_shipments` | Shipment surrogate PK |
| **UK** | `shipment_number` | `uk_shipments_number` | Dispatch document identity (BR-003) |
| **FK** | `customer_order_id` → `fulfillment.customer_orders.id` | `fk_shipments_order` | Shipment fulfills order (REL-063) |
| **FK** | `fulfillment_execution_id` → `fulfillment.fulfillment_executions.id` | `fk_shipments_fe` | Verified pick required (BR-003, REL-073) |
| **FK** | `ship_from_location_id` → `network.inventory_locations.id` | `fk_shipments_location` | Ship-from site |
| **CK** | `shipment_number` | — | Primary business key |
| **CK** | `tracking_identifier` | — | Carrier tracking when assigned; not UK — carriers may reuse formats |

---

### `fulfillment.shipment_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_shipment_lines` | Shipment line surrogate PK |
| **FK** | `shipment_id` → `fulfillment.shipments.id` | `fk_shipment_lines_shipment` | Line belongs to shipment |
| **FK** | `order_line_id` → `fulfillment.customer_order_lines.id` | `fk_shipment_lines_ol` | Shipped order line |
| **FK** | `product_id` → `catalog.products.id` | `fk_shipment_lines_product` | Shipped product |
| **FK** | `lot_batch_id` → `inventory.lot_batches.id` | `fk_shipment_lines_lot` | Lot traceability on dispatch |
| **FK** | `reservation_id` → `fulfillment.inventory_reservations.id` | `fk_shipment_lines_reservation` | Consumes reservation (REL-074) |
| **UK** | `(shipment_id, order_line_id)` | `uk_shipment_lines_shipment_ol` | One shipment line per order line per shipment |

---

## Domain 9: Network Transfer

---

### `transfer.transfer_requests`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_transfer_requests` | Request surrogate PK |
| **UK** | `request_number` | `uk_transfer_requests_number` | Transfer request document |
| **FK** | `source_location_id` → `network.inventory_locations.id` | `fk_transfer_requests_source` | Source site (REL-075, BR-012) |
| **FK** | `destination_location_id` → `network.inventory_locations.id` | `fk_transfer_requests_dest` | Destination site (REL-076) |
| **FK** | `requested_by` → `identity.user_accounts.id` | `fk_transfer_requests_requester` | Requestor attribution |
| **FK** | `approved_by` → `identity.user_accounts.id` | `fk_transfer_requests_approver` | Approver attribution |
| **FK** | `stock_transfer_id` → `transfer.stock_transfers.id` | `fk_transfer_requests_transfer` | Request-to-execution link (REL-078) |
| **CK** | `request_number` | — | Primary business key |

---

### `transfer.transfer_request_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_transfer_request_lines` | Line surrogate PK |
| **FK** | `transfer_request_id` → `transfer.transfer_requests.id` | `fk_transfer_request_lines_req` | Line belongs to request |
| **FK** | `product_id` → `catalog.products.id` | `fk_transfer_request_lines_product` | Product to transfer (REL-077) |
| **UK** | `(transfer_request_id, line_number)` | `uk_transfer_request_lines_req_line` | Unique line sequence |

---

### `transfer.stock_transfers`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_stock_transfers` | Transfer execution PK |
| **UK** | `transfer_number` | `uk_stock_transfers_number` | Transfer document identity |
| **FK** | `transfer_request_id` → `transfer.transfer_requests.id` | `fk_stock_transfers_request` | Optional request origin (REL-080) |
| **FK** | `source_location_id` → `network.inventory_locations.id` | `fk_stock_transfers_source` | Source deduction site |
| **FK** | `destination_location_id` → `network.inventory_locations.id` | `fk_stock_transfers_dest` | Destination receipt site |
| **CK** | `transfer_number` | — | Primary business key |

---

### `transfer.stock_transfer_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_stock_transfer_lines` | Line surrogate PK |
| **FK** | `stock_transfer_id` → `transfer.stock_transfers.id` | `fk_stock_transfer_lines_transfer` | Line belongs to transfer |
| **FK** | `product_id` → `catalog.products.id` | `fk_stock_transfer_lines_product` | Transferred SKU |
| **FK** | `lot_batch_id` → `inventory.lot_batches.id` | `fk_stock_transfer_lines_lot` | Lot on transfer (BR-017, REL-083) |
| **UK** | `(stock_transfer_id, line_number)` | `uk_stock_transfer_lines_transfer_line` | Unique line sequence |

---

### `transfer.in_transit_stock`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_in_transit_stock` | In-transit surrogate PK |
| **UK** | `in_transit_reference` | `uk_in_transit_stock_ref` | Pipeline stock document |
| **FK** | `stock_transfer_id` → `transfer.stock_transfers.id` | `fk_in_transit_stock_transfer` | Subordinate to transfer — composition (REL-081) |
| **FK** | `stock_transfer_line_id` → `transfer.stock_transfer_lines.id` | `fk_in_transit_stock_line` | Line-level in-transit |
| **FK** | `product_id` → `catalog.products.id` | `fk_in_transit_stock_product` | Product in pipeline |
| **FK** | `source_location_id` → `network.inventory_locations.id` | `fk_in_transit_stock_source` | Origin site |
| **FK** | `destination_location_id` → `network.inventory_locations.id` | `fk_in_transit_stock_dest` | Destination site |
| **CK** | `in_transit_reference` | — | Primary business key |

---

## Domain 10: Inventory Accuracy

---

### `accuracy.cycle_counts`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_cycle_counts` | Count assignment PK |
| **UK** | `count_assignment_number` | `uk_cycle_counts_number` | Count work document (BR-018) |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_cycle_counts_location` | Count site (REL-086) |
| **FK** | `product_id` → `catalog.products.id` | `fk_cycle_counts_product` | Counted SKU (REL-085) |
| **FK** | `storage_position_id` → `network.storage_positions.id` | `fk_cycle_counts_position` | Optional bin scope (REL-087) |
| **FK** | `counter_id` → `identity.user_accounts.id` | `fk_cycle_counts_counter` | Counter for SoD — must differ from approver (BR-019, REL-089) |
| **CK** | `count_assignment_number` | — | Primary business key |

---

### `accuracy.physical_inventory_counts`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_physical_inventory_counts` | Wall-to-wall count event PK |
| **UK** | `count_event_number` | `uk_physical_inventory_counts_number` | Count event document (BR-024) |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_physical_inventory_counts_location` | Frozen location (REL-007, REL-090) |
| **CK** | `count_event_number` | — | Primary business key |

---

### `accuracy.count_variances`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_count_variances` | Variance surrogate PK |
| **UK** | `variance_reference` | `uk_count_variances_ref` | Variance investigation document |
| **FK** | `cycle_count_id` → `accuracy.cycle_counts.id` | `fk_count_variances_cycle` | Cycle count origin (REL-092) — mutually exclusive with physical count |
| **FK** | `physical_count_id` → `accuracy.physical_inventory_counts.id` | `fk_count_variances_physical` | Physical count origin (REL-092) |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_count_variances_position` | Affected balance (REL-093) |
| **FK** | `product_id` → `catalog.products.id` | `fk_count_variances_product` | Denormalized product |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_count_variances_location` | Denormalized location |
| **FK** | `approver_id` → `identity.user_accounts.id` | `fk_count_variances_approver` | Independent approver ≠ counter (BR-019, REL-095) |
| **CK** | `variance_reference` | — | Primary business key |
| **CK** | `(cycle_count_id)` or `(physical_count_id)` | — | Exactly one count origin per variance — application CHECK, not UK |

---

### `accuracy.stock_adjustments`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_stock_adjustments` | Adjustment surrogate PK |
| **UK** | `adjustment_reference` | `uk_stock_adjustments_ref` | Adjustment document (BR-020) |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_stock_adjustments_position` | Modified balance (REL-031) |
| **FK** | `product_id` → `catalog.products.id` | `fk_stock_adjustments_product` | Denormalized product |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_stock_adjustments_location` | Denormalized location |
| **FK** | `reason_code_id` → `governance.reason_codes.id` | `fk_stock_adjustments_reason` | Mandatory reason (BR-020, REL-097) |
| **FK** | `count_variance_id` → `accuracy.count_variances.id` | `fk_stock_adjustments_variance` | Count-to-correction traceability (REL-096, BR-022) |
| **FK** | `initiated_by` → `identity.user_accounts.id` | `fk_stock_adjustments_initiator` | Initiator (REL-098) |
| **FK** | `approved_by` → `identity.user_accounts.id` | `fk_stock_adjustments_approver` | Independent approver (BR-021) |
| **CK** | `adjustment_reference` | — | Primary business key |

---

### `accuracy.inventory_write_offs`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_inventory_write_offs` | Write-off surrogate PK |
| **UK** | `write_off_reference` | `uk_inventory_write_offs_ref` | Write-off document (BR-023) |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_inventory_write_offs_position` | Permanent quantity removal (REL-032) |
| **FK** | `product_id` → `catalog.products.id` | `fk_inventory_write_offs_product` | Denormalized product |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_inventory_write_offs_location` | Denormalized location |
| **FK** | `reason_code_id` → `governance.reason_codes.id` | `fk_inventory_write_offs_reason` | Mandatory reason (BR-020) |
| **FK** | `return_disposition_id` → `returns.return_dispositions.id` | `fk_inventory_write_offs_disposition` | Return-originated write-off (REL-099) |
| **FK** | `initiated_by` → `identity.user_accounts.id` | `fk_inventory_write_offs_initiator` | Initiator |
| **FK** | `authorized_by` → `identity.user_accounts.id` | `fk_inventory_write_offs_authorizer` | Authorizer (BR-023, REL-101) |
| **CK** | `write_off_reference` | — | Primary business key |

---

## Domain 11: Returns

---

### `returns.return_authorizations`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_return_authorizations` | RMA surrogate PK |
| **UK** | `rma_number` | `uk_return_authorizations_rma` | RMA is gate document for returns (BR-025) |
| **FK** | `customer_order_id` → `fulfillment.customer_orders.id` | `fk_return_authorizations_order` | Validates against original order (REL-105) |
| **CK** | `rma_number` | — | Primary business key |

---

### `returns.return_authorization_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_return_authorization_lines` | Line surrogate PK |
| **FK** | `return_authorization_id` → `returns.return_authorizations.id` | `fk_return_authorization_lines_rma` | Line belongs to RMA |
| **FK** | `product_id` → `catalog.products.id` | `fk_return_authorization_lines_product` | Authorized return SKU (REL-107) |
| **UK** | `(return_authorization_id, line_number)` | `uk_return_authorization_lines_rma_line` | Unique line sequence |

---

### `returns.customer_returns`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_customer_returns` | Return receipt surrogate PK |
| **UK** | `return_number` | `uk_customer_returns_number` | Return receipt document |
| **FK** | `return_authorization_id` → `returns.return_authorizations.id` | `fk_customer_returns_rma` | Valid RMA required (BR-025, REL-108) |
| **FK** | `customer_order_id` → `fulfillment.customer_orders.id` | `fk_customer_returns_order` | Original order reference |
| **FK** | `receiving_location_id` → `network.inventory_locations.id` | `fk_customer_returns_location` | Receipt site (REL-109) |
| **FK** | `receiving_clerk_id` → `identity.user_accounts.id` | `fk_customer_returns_clerk` | Clerk attribution |
| **CK** | `return_number` | — | Primary business key |

---

### `returns.customer_return_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_customer_return_lines` | Line surrogate PK |
| **FK** | `customer_return_id` → `returns.customer_returns.id` | `fk_customer_return_lines_return` | Line belongs to return |
| **FK** | `product_id` → `catalog.products.id` | `fk_customer_return_lines_product` | Returned product |
| **UK** | `(customer_return_id, line_number)` | `uk_customer_return_lines_return_line` | Unique line sequence |

---

### `returns.return_dispositions`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_return_dispositions` | Disposition surrogate PK |
| **UK** | `disposition_reference` | `uk_return_dispositions_ref` | Disposition document (BR-026) |
| **FK** | `customer_return_id` → `returns.customer_returns.id` | `fk_return_dispositions_return` | Disposition of return (REL-112) |
| **FK** | `return_line_id` → `returns.customer_return_lines.id` | `fk_return_dispositions_line` | Line-level disposition |
| **FK** | `product_id` → `catalog.products.id` | `fk_return_dispositions_product` | Dispositioned product |
| **FK** | `restock_location_id` → `network.inventory_locations.id` | `fk_return_dispositions_location` | Restock target |
| **FK** | `quarantine_hold_id` → `inventory.quarantine_holds.id` | `fk_return_dispositions_hold` | Quarantine path (REL-114) |
| **FK** | `write_off_id` → `accuracy.inventory_write_offs.id` | `fk_return_dispositions_writeoff` | Write-off path (REL-113) |
| **FK** | `inspector_id` → `identity.user_accounts.id` | `fk_return_dispositions_inspector` | Inspector attribution |
| **CK** | `disposition_reference` | — | Primary business key |

---

## Domain 12: Commercial

---

### `commercial.promotional_stock_allocations`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_promotional_stock_allocations` | Allocation surrogate PK |
| **UK** | `allocation_reference` | `uk_promotional_allocations_ref` | Campaign ring-fence document (BR-029) |
| **FK** | `product_id` → `catalog.products.id` | `fk_promotional_allocations_product` | Ring-fenced SKU (REL-026) |
| **CK** | `allocation_reference` | — | Primary business key |
| **CK** | `(product_id, campaign_name, effective_start_date)` | — | Identifies campaign allocation window; not UK if campaigns rerun annually |

---

### `commercial.promotional_allocation_locations`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_promotional_allocation_locations` | Junction surrogate PK |
| **FK** | `allocation_id` → `commercial.promotional_stock_allocations.id` | `fk_promo_alloc_locations_allocation` | Location scope of allocation (REL-027) |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_promo_alloc_locations_location` | Supplying location |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_promo_alloc_locations_position` | Specific balance ring-fenced (REL-025) |
| **UK** | `(allocation_id, location_id)` | `uk_promo_alloc_locations_alloc_loc` | One allocation entry per location per campaign |

---

## Domain 13: Identity & Access

---

### `identity.user_accounts`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_user_accounts` | User surrogate PK — referenced across all transactional tables for attribution |
| **UK** | `user_identifier` | `uk_user_accounts_identifier` | Login/employee ID must be unique — accountability anchor (BO-19) |
| **UK** | `email` | `uk_user_accounts_email` | Optional; unique when present for authentication and notification |
| **CK** | `user_identifier` | — | Primary natural key |
| **CK** | `email` | — | Alternate login identifier when used |

---

### `identity.role_assignments`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_role_assignments` | Assignment surrogate PK |
| **FK** | `user_account_id` → `identity.user_accounts.id` | `fk_role_assignments_user` | Assignment belongs to user — composition (REL-123) |
| **UK** | `(user_account_id, role_name, effective_from)` | `uk_role_assignments_user_role_from` | Same role not double-assigned at same effective date; supports history |
| **CK** | `(user_account_id, role_name)` | — | Active role lookup; not UK due to effective dating |

---

### `identity.role_assignment_locations`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_role_assignment_locations` | Junction surrogate PK |
| **FK** | `role_assignment_id` → `identity.role_assignments.id` | `fk_role_assignment_locations_assignment` | Scope belongs to assignment |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_role_assignment_locations_location` | Authorized site (REL-124) |
| **UK** | `(role_assignment_id, location_id)` | `uk_role_assignment_locations` | One scope entry per location per assignment |

---

## Domain 14: Audit & Reporting

---

### `audit.inventory_movement_records`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_inventory_movement_records` | Partition-local surrogate PK; append-only |
| **UK** | `(movement_reference, movement_timestamp)` | `uk_movement_records_ref_ts` | Reference unique within partition window; supports idempotent event ingestion |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_movement_records_position` | Affected balance (REL-115) |
| **FK** | `product_id` → `catalog.products.id` | `fk_movement_records_product` | Denormalized for partition-local queries |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_movement_records_location` | Denormalized for reporting |
| **FK** | `lot_batch_id` → `inventory.lot_batches.id` | `fk_movement_records_lot` | Lot on movement (BR-017) |
| **FK** | `reason_code_id` → `governance.reason_codes.id` | `fk_movement_records_reason` | Reason on adjustment movements (BR-020) |
| **FK** | `performed_by` → `identity.user_accounts.id` | `fk_movement_records_user` | User attribution (REL-117) |
| **CK** | `movement_reference` | — | Business transaction reference |
| **CK** | `(source_document_type, source_document_id)` | — | Polymorphic origin link (REL-116) — not FK due to multiple source tables |

---

### `audit.audit_trail_records`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_audit_trail_records` | Partition-local surrogate PK; immutable |
| **UK** | `(audit_event_reference, event_timestamp)` | `uk_audit_trail_ref_ts` | Unique event within partition |
| **FK** | `user_id` → `identity.user_accounts.id` | `fk_audit_trail_user` | Actor identity (REL-119) |
| **FK** | `movement_record_id` → `audit.inventory_movement_records.id` | `fk_audit_trail_movement` | Links governance snapshot to operational movement (REL-127) |
| **CK** | `(affected_entity_type, affected_entity_id)` | — | Polymorphic governed entity (REL-118) |
| **CK** | `audit_event_reference` | — | Primary business event key |

---

### `audit.operational_alerts`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_operational_alerts` | Alert surrogate PK |
| **UK** | `alert_reference` | `uk_operational_alerts_ref` | Alert document for workflow routing |
| **FK** | `product_id` → `catalog.products.id` | `fk_operational_alerts_product` | Alert context SKU |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_operational_alerts_location` | Alert context site |
| **FK** | `stock_position_id` → `inventory.stock_positions.id` | `fk_operational_alerts_position` | Threshold breach source (REL-120) |
| **CK** | `(source_entity_type, source_entity_id)` | — | Polymorphic trigger (transfer, delivery, allocation) |
| **CK** | `alert_reference` | — | Primary business key |

---

### `audit.inventory_valuation_snapshots`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_inventory_valuation_snapshots` | Snapshot surrogate PK |
| **UK** | `snapshot_reference` | `uk_valuation_snapshots_ref` | Finance reconciliation document |
| **UK** | `(valuation_date, location_scope)` | `uk_valuation_snapshots_date_scope` | One network/regional snapshot per period — prevents duplicate month-end close |
| **FK** | `prepared_by` → `identity.user_accounts.id` | `fk_valuation_snapshots_prepared_by` | Preparer attribution |
| **CK** | `snapshot_reference` | — | Primary business key |

---

### `audit.inventory_valuation_lines`

| Key Type | Column(s) | Constraint Name (logical) | Business Justification |
|----------|-----------|---------------------------|------------------------|
| **PK** | `id` | `pk_inventory_valuation_lines` | Line surrogate PK |
| **FK** | `snapshot_id` → `audit.inventory_valuation_snapshots.id` | `fk_valuation_lines_snapshot` | Line belongs to snapshot |
| **FK** | `product_id` → `catalog.products.id` | `fk_valuation_lines_product` | Valued SKU (REL-130) |
| **FK** | `location_id` → `network.inventory_locations.id` | `fk_valuation_lines_location` | Valued site (REL-131) |
| **UK** | `(snapshot_id, product_id, location_id)` | `uk_valuation_lines_snapshot_prod_loc` | One valuation line per SKU per location per snapshot |

---

## Appendix A: Primary Key Summary

All 59 tables use **`id BIGINT GENERATED ALWAYS AS IDENTITY`** as the sole primary key column.

| Design Decision | Business Justification |
|-----------------|------------------------|
| Surrogate over natural PK | Business identifiers (SKU, PO number) can change format, merge, or require soft-retirement without cascading PK updates across high-volume child tables |
| Single-column PK | Simplifies ORM mapping, partition management, and FK definitions |
| BIGINT not INT | Supports very high-volume tables (movement records, order lines) without ID exhaustion |
| No composite PKs | Composite business uniqueness enforced via UK constraints — separates physical row identity from business identity |

---

## Appendix B: Foreign Key Relationship Map

| Child Table | Parent Table | Cardinality | ON DELETE Policy (recommended) | Business Rule |
|-------------|--------------|-------------|-------------------------------|---------------|
| `inventory.stock_positions` | `catalog.products` | N:1 | RESTRICT | Cannot delete product with balances |
| `inventory.stock_positions` | `network.inventory_locations` | N:1 | RESTRICT | Cannot delete location with stock |
| `fulfillment.inventory_reservations` | `inventory.stock_positions` | N:1 | RESTRICT | Reservation requires valid balance |
| `inbound.goods_receipts` | `procurement.purchase_orders` | N:1 | RESTRICT | PO required for receipt (BR-007) |
| `inbound.put_aways` | `inbound.goods_receipts` | N:1 | RESTRICT | Put-away requires receipt |
| `accuracy.stock_adjustments` | `governance.reason_codes` | N:1 | RESTRICT | Reason mandatory (BR-020) |
| `accuracy.count_variances` | `accuracy.cycle_counts` | N:1 | RESTRICT | Variance traceable to count |
| `returns.customer_returns` | `returns.return_authorizations` | N:1 | RESTRICT | RMA required (BR-025) |
| `finance.invoice_goods_receipt_match` | `finance.supplier_invoices` | N:1 | CASCADE | Match rows die with invoice draft |
| `identity.role_assignments` | `identity.user_accounts` | N:1 | CASCADE | Assignments removed with user deprovisioning |
| `audit.inventory_movement_records` | `inventory.stock_positions` | N:1 | RESTRICT | Movement history preserved |

**Cross-schema FK note:** Foreign keys spanning bounded contexts (e.g., `fulfillment` → `inventory`) enforce referential integrity at persistence time. Cross-aggregate coordination still uses domain events per architecture — FKs prevent orphan rows, not distributed transactions.

---

## Appendix C: Unique Key Catalog

| Table | Unique Key Column(s) | Enforces Business Rule |
|-------|---------------------|------------------------|
| `catalog.products` | `sku` | Global SKU uniqueness |
| `catalog.product_identifiers` | `(identifier_type, identifier_value)` | No duplicate scan codes |
| `network.inventory_locations` | `location_code` | Network location identity |
| `network.storage_positions` | `(location_id, position_code)` | Bin unique within site |
| `inventory.stock_positions` | `(product_id, location_id)` | One balance per SKU per site |
| `inventory.stock_policies` | `(product_id, location_id)` | One policy per SKU per site |
| `inventory.lot_batches` | `(product_id, lot_number, stock_position_id)` | Lot quantity uniqueness at position |
| `procurement.suppliers` | `supplier_code` | Vendor identity |
| `procurement.purchase_orders` | `po_number` | PO document identity |
| `finance.supplier_invoices` | `(supplier_id, invoice_number)` | AP invoice uniqueness |
| `fulfillment.customer_orders` | `order_number` | Order identity |
| `governance.reason_codes` | `reason_code` | Taxonomy uniqueness |
| `identity.user_accounts` | `user_identifier` | Login uniqueness |
| `governance.governance_policies` | `(policy_code, effective_from)` | Policy version uniqueness |
| `finance.invoice_goods_receipt_match` | `(supplier_invoice_id, goods_receipt_id)` | Single match pair |
| `commercial.promotional_allocation_locations` | `(allocation_id, location_id)` | One location entry per campaign |
| `audit.inventory_valuation_lines` | `(snapshot_id, product_id, location_id)` | Snapshot line uniqueness |
| All `*_lines` tables | `(parent_id, line_number)` | Document line ordering |

---

## Appendix D: Candidate Key Reference

Candidate keys not enforced as UK are retained for integration contracts and future constraint hardening.

| Table | Candidate Key | Why Not Enforced as UK |
|-------|---------------|------------------------|
| `fulfillment.shipments` | `tracking_identifier` | Carrier may assign tracking late or reuse across carriers |
| `procurement.purchase_order_lines` | `(purchase_order_id, product_id)` | Same SKU may appear on multiple lines (different prices/dates) |
| `audit.inventory_movement_records` | `(source_document_type, source_document_id, stock_position_id)` | Multiple movements per source document (partial shipments) |
| `accuracy.count_variances` | `(cycle_count_id)` XOR `(physical_count_id)` | Enforced via CHECK constraint, not UK |
| `commercial.promotional_stock_allocations` | `(product_id, campaign_name, effective_start_date)` | Campaign names may repeat across years |

---

## Appendix E: Keys Enforcing Critical Business Rules

| Business Rule | Key Enforcement |
|---------------|-----------------|
| **BR-001** ATP-only commitment | `uk_stock_positions_product_location` ensures single authoritative balance per SKU/site |
| **BR-002** Reservation at confirmation | FK `inventory_reservations.stock_position_id` binds hold to specific balance |
| **BR-005** Put-away before availability | FK chain `put_aways` → `goods_receipts` → `purchase_orders` enforces receipt workflow |
| **BR-007** PO required for receipt | FK `goods_receipts.purchase_order_id` (nullable only for documented exception) |
| **BR-008** Three-way match | UK `invoice_goods_receipt_match (supplier_invoice_id, goods_receipt_id)` |
| **BR-019** Independent count approval | FK `count_variances.approver_id` ≠ `cycle_counts.counter_id` — application-enforced SoD |
| **BR-020** Mandatory reason code | FK `stock_adjustments.reason_code_id` NOT NULL + RESTRICT |
| **BR-025** RMA required | FK `customer_returns.return_authorization_id` NOT NULL |
| **BR-027** No discontinued reorder | FK to `products` + application lifecycle check on insert |
| **BR-029** Promotional ring-fence | UK `promotional_allocation_locations (allocation_id, location_id)` |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Database Architect | | | |
| DDD Solution Architect | | | |
| Solution Architect | | | |
| Inventory Controller | | | |

---

*End of Database Keys Specification*

*Document ID: SRS-DB-003 | Version 1.0 | July 6, 2026*
