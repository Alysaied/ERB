# -*- coding: utf-8 -*-
"""Generate implementation checklists for all IMS features F-01..F-30."""
from pathlib import Path

OUT = Path(__file__).resolve().parent

# Priority: P0 Must/MVP critical, P1 Must remaining, P2 Should, P3 Could/deferred
# Status: all Not Started (gap analysis baseline)

def T(layer, desc, priority, deps, seq):
    return {"layer": layer, "desc": desc, "priority": priority, "deps": deps, "seq": seq}

FEATURES = {}

def feat(fid, name, feat_deps, tasks):
    FEATURES[fid] = {"name": name, "feat_deps": feat_deps, "tasks": tasks}

# ---------- F-01 ----------
feat("F-01", "Product Catalog Management", ["F-27"], [
    T("Database", "Create Flyway schema `catalog` and baseline migration", "P0", ["F-27 platform DB"], 1),
    T("Database", "Create table `catalog.products` with SKU UK, lifecycle CHECK, version, audit columns", "P0", ["CHK-01-DB-01"], 2),
    T("Database", "Create table `catalog.product_identifiers` with FK to products and unique identifier", "P0", ["CHK-01-DB-02"], 3),
    T("Database", "Add indexes on products(sku), products(lifecycle_status), products(product_name)", "P1", ["CHK-01-DB-02"], 4),
    T("Database", "Grant app role DML on catalog tables; revoke DDL from app role", "P1", ["CHK-01-DB-03"], 5),
    T("Backend", "Implement Product aggregate root + ProductIdentifier entity/VO", "P0", ["CHK-01-DB-02"], 1),
    T("Backend", "Implement value objects: ProductSku, LifecycleStatus, UnitOfMeasure, Category", "P0", ["CHK-01-BE-01"], 2),
    T("Backend", "Implement ProductRepository (Spring Data JPA)", "P0", ["CHK-01-BE-01"], 3),
    T("Backend", "Implement Request/Response DTOs + MapStruct mappers for product APIs", "P0", ["CHK-01-BE-02"], 4),
    T("Backend", "Implement Bean Validation + domain validators (VR-001/007, mandatory fields)", "P0", ["CHK-01-BE-04"], 5),
    T("Backend", "Implement ProductCatalogService (create/update/search/lifecycle)", "P0", ["CHK-01-BE-03", "CHK-01-BE-05"], 6),
    T("Backend", "Implement DuplicateDetectionService + resolve API", "P1", ["CHK-01-BE-06"], 7),
    T("Backend", "Implement ProductController API-001–005, 007–009 with Problem Details errors", "P0", ["CHK-01-BE-06"], 8),
    T("Backend", "Enforce PRODUCT_MANAGE / PRODUCT_VIEW permissions on endpoints", "P0", ["F-27", "CHK-01-BE-08"], 9),
    T("Frontend", "Add child routes: catalog/new, catalog/:sku, catalog/:sku/edit", "P0", ["F-27 auth"], 1),
    T("Frontend", "Implement ProductApiService (HttpClient) replacing mocks", "P0", ["CHK-01-BE-08"], 2),
    T("Frontend", "Implement ProductFacade with signals for list/filters/selected/saveState", "P0", ["CHK-01-FE-02"], 3),
    T("Frontend", "Build Product list/create/edit pages (UI-005) with reactive forms + validation", "P0", ["CHK-01-FE-03"], 4),
    T("Frontend", "Build lifecycle change + duplicate resolution UI flows", "P1", ["CHK-01-FE-04"], 5),
    T("Frontend", "Map RFC 7807 field errors to form controls", "P1", ["CHK-01-FE-04"], 6),
    T("Testing", "API contract tests for API-001–005, 009 (happy + 400/403/409)", "P0", ["CHK-01-BE-08"], 1),
    T("Testing", "Unit tests for lifecycle transitions and duplicate SKU invariant", "P0", ["CHK-01-BE-06"], 2),
    T("Testing", "UI/E2E: create product, edit, lifecycle change (FAC-01-H1/H2/H3)", "P1", ["CHK-01-FE-04"], 3),
    T("Testing", "Permission test: non-manager denied create (FAC-01-P1)", "P0", ["CHK-01-BE-09"], 4),
    T("Documentation", "Update OpenAPI for product endpoints", "P1", ["CHK-01-BE-08"], 1),
    T("Documentation", "Mark FAC-01 checklist items with evidence links in AC file", "P2", ["CHK-01-TE-03"], 2),
])

# ---------- F-02 ----------
feat("F-02", "Location & Network Setup", ["F-27"], [
    T("Database", "Create Flyway schema `network`", "P0", ["F-27"], 1),
    T("Database", "Create `network.inventory_locations` with location_code UK, hierarchy self-FK, status", "P0", ["CHK-02-DB-01"], 2),
    T("Database", "Create `network.storage_positions` FK to location", "P0", ["CHK-02-DB-02"], 3),
    T("Database", "Add freeze/operational status columns and CHECKs", "P0", ["CHK-02-DB-02"], 4),
    T("Database", "Indexes on location_code, parent_location_id, operational_status", "P1", ["CHK-02-DB-02"], 5),
    T("Backend", "Implement InventoryLocation aggregate + StoragePosition entity", "P0", ["CHK-02-DB-03"], 1),
    T("Backend", "VOs: LocationCode, LocationType, HierarchyPath, PhysicalAddress", "P0", ["CHK-02-BE-01"], 2),
    T("Backend", "Repositories for location and storage positions", "P0", ["CHK-02-BE-01"], 3),
    T("Backend", "DTOs/mappers for location APIs", "P0", ["CHK-02-BE-02"], 4),
    T("Backend", "LocationLifecycleService (create, hierarchy, activate/deactivate/close, freeze status)", "P0", ["CHK-02-BE-03"], 5),
    T("Backend", "LocationController API-011–021 + cycle hierarchy validation", "P0", ["CHK-02-BE-05"], 6),
    T("Backend", "Enforce LOCATION_MANAGE/VIEW + location-scope filters", "P0", ["F-27", "CHK-02-BE-06"], 7),
    T("Frontend", "Child routes for location detail and storage positions", "P0", ["F-27"], 1),
    T("Frontend", "LocationApiService + LocationFacade", "P0", ["CHK-02-BE-06"], 2),
    T("Frontend", "UI-007 list/create/edit + hierarchy tree + storage grid", "P0", ["CHK-02-FE-02"], 3),
    T("Frontend", "Activation UX with opening-balance gate messaging", "P1", ["CHK-02-FE-03", "F-30"], 4),
    T("Testing", "API tests API-011–017; reject cyclic hierarchy", "P0", ["CHK-02-BE-06"], 1),
    T("Testing", "UI test create WH + add bin (FAC-02-H1/H3)", "P1", ["CHK-02-FE-03"], 2),
    T("Testing", "Permission deny without LOCATION_MANAGE (FAC-02-P1)", "P0", ["CHK-02-BE-07"], 3),
    T("Documentation", "OpenAPI location module + go-live activation notes", "P1", ["CHK-02-BE-06"], 1),
])

# ---------- F-03 ----------
feat("F-03", "Stock Policy & Product Classification", ["F-01", "F-02", "F-27"], [
    T("Database", "Create `governance` schema + `reason_codes` + `governance_policies`", "P0", ["F-27"], 1),
    T("Database", "Create `inventory.stock_policies` + `stock_policy_history`", "P0", ["F-01", "F-02"], 2),
    T("Database", "Constraints: uk(location,sku), qty>=0, reason code unique/retire flag", "P0", ["CHK-03-DB-01", "CHK-03-DB-02"], 3),
    T("Database", "ABC column/attr on catalog.products if not present", "P2", ["F-01"], 4),
    T("Backend", "StockPolicy + GovernancePolicy + ReasonCode aggregates", "P0", ["CHK-03-DB-03"], 1),
    T("Backend", "VOs: StockThresholdSet, ApprovalThreshold, QuantityTolerance, AbcClass", "P0", ["CHK-03-BE-01"], 2),
    T("Backend", "Repositories + DTOs for policies/reason codes/ABC", "P0", ["CHK-03-BE-01"], 3),
    T("Backend", "StockPolicyService + GovernanceService (effective dating)", "P0", ["CHK-03-BE-03"], 4),
    T("Backend", "API-038–040, API-022–030, API-006", "P0", ["CHK-03-BE-04"], 5),
    T("Backend", "SafetyStockProtectionService hooks for later consumers", "P2", ["CHK-03-BE-04"], 6),
    T("Backend", "Permissions POLICY_MANAGE / GOVERNANCE_MANAGE", "P0", ["F-27", "CHK-03-BE-05"], 7),
    T("Frontend", "UI-008 stock policy forms wired to API", "P0", ["CHK-03-BE-05"], 1),
    T("Frontend", "UI-010 reason codes + thresholds/tolerances", "P0", ["CHK-03-BE-05"], 2),
    T("Frontend", "UI-009 ABC classification grid (Phase 2)", "P2", ["CHK-03-BE-05"], 3),
    T("Testing", "API tests thresholds + retire reason code blocks use", "P0", ["CHK-03-BE-05"], 1),
    T("Testing", "FAC-03-H1/V1/V4/P1 automated", "P0", ["CHK-03-FE-01"], 2),
    T("Documentation", "Document effective-dating rules for ops", "P2", ["CHK-03-BE-04"], 1),
])

# ---------- F-04 ----------
feat("F-04", "Inventory Visibility & Search", ["F-01", "F-02", "F-27"], [
    T("Database", "Ensure `inventory.stock_positions` with on_hand/reserved/quarantine qty CHECKs", "P0", ["F-01", "F-02"], 1),
    T("Database", "Create `inventory.lot_batches` and `quarantine_holds` tables", "P1", ["CHK-04-DB-01"], 2),
    T("Database", "Indexes for (location_code, sku) and status queries", "P0", ["CHK-04-DB-01"], 3),
    T("Backend", "StockPosition aggregate + ATP calculation domain service", "P0", ["CHK-04-DB-01"], 1),
    T("Backend", "StockPositionRepository + query repository", "P0", ["CHK-04-BE-01"], 2),
    T("Backend", "DTOs for stock position, availability, status board", "P0", ["CHK-04-BE-02"], 3),
    T("Backend", "API-033–037 + intelligence 151–153 (MVP subset)", "P0", ["CHK-04-BE-03"], 4),
    T("Backend", "Enforce INVENTORY_VIEW + mandatory location-scope filter", "P0", ["F-27", "CHK-04-BE-04"], 5),
    T("Frontend", "InventoryApiService + InventoryVisibilityFacade", "P0", ["CHK-04-BE-04"], 1),
    T("Frontend", "UI-020 status monitor with real data + filters", "P0", ["CHK-04-FE-01"], 2),
    T("Frontend", "UI-021 availability inquiry form + results", "P0", ["CHK-04-FE-01"], 3),
    T("Frontend", "Network/inbound views (US-028 Phase 2)", "P2", ["CHK-04-FE-02", "F-07"], 4),
    T("Testing", "Unit tests ATP = on_hand - reserved - hold", "P0", ["CHK-04-BE-01"], 1),
    T("Testing", "API + scope tests FAC-04-H1/P3", "P0", ["CHK-04-BE-05"], 2),
    T("Testing", "UI smoke FAC-04-H4 search/filter", "P1", ["CHK-04-FE-02"], 3),
    T("Documentation", "ATP definition note for UAT script", "P1", ["CHK-04-BE-01"], 1),
])

# ---------- F-05 ----------
feat("F-05", "Goods Receiving & Verification", ["F-01", "F-02", "F-03", "F-27"], [
    T("Database", "Create `inbound` schema + goods_receipts / lines", "P0", ["F-02"], 1),
    T("Database", "Create `inbound.receipt_discrepancies`", "P0", ["CHK-05-DB-01"], 2),
    T("Database", "Ensure movement table available for receipt postings", "P0", ["F-29"], 3),
    T("Database", "Minimal PO seed/table support for validate-for-receipt until F-07", "P0", ["CHK-05-DB-01"], 4),
    T("Backend", "GoodsReceipt aggregate + discrepancy entity", "P0", ["CHK-05-DB-02"], 1),
    T("Backend", "VOs: PositiveQuantity, LotIdentity, ShelfLifeProfile", "P0", ["CHK-05-BE-01"], 2),
    T("Backend", "GoodsReceivingService + DiscrepancyService + movement recording", "P0", ["CHK-05-BE-01", "F-29"], 3),
    T("Backend", "API-065–072, 075–076 + reason/tolerance consult", "P0", ["CHK-05-BE-03", "F-03"], 4),
    T("Backend", "Freeze check + RECEIVE_GOODS / location scope security", "P0", ["F-27", "CHK-05-BE-04"], 5),
    T("Frontend", "InboundApiService + GoodsReceiptFacade", "P0", ["CHK-05-BE-04"], 1),
    T("Frontend", "UI-015 goods receipt workbench", "P0", ["CHK-05-FE-01"], 2),
    T("Frontend", "UI-016 discrepancy resolution", "P0", ["CHK-05-FE-01"], 3),
    T("Frontend", "UI-018 non-PO/return intake", "P1", ["CHK-05-FE-01"], 4),
    T("Frontend", "UI-022 movement history consumer", "P1", ["F-29", "CHK-05-BE-03"], 5),
    T("Testing", "API E2E receive+verify; discrepancy path FAC-05-H1/H2", "P0", ["CHK-05-FE-02"], 1),
    T("Testing", "Lot required for traceable product FAC-05-V2", "P0", ["CHK-05-BE-04"], 2),
    T("Testing", "Permission/location scope FAC-05-P1/P2", "P0", ["CHK-05-BE-05"], 3),
    T("Documentation", "Document PO-stub vs F-07 cutover for receiving", "P1", ["CHK-05-BE-04"], 1),
])

# ---------- F-06 ----------
feat("F-06", "Put-Away Management", ["F-05", "F-02", "F-27"], [
    T("Database", "Create `inbound.put_aways` with FK to goods_receipt and storage_position", "P0", ["F-05", "F-02"], 1),
    T("Database", "Constraints: position belongs to receipt location", "P0", ["CHK-06-DB-01"], 2),
    T("Backend", "PutAwayService confirming storage and updating availability", "P0", ["CHK-06-DB-02", "F-04"], 1),
    T("Backend", "API-073, API-074 (+ storage position APIs)", "P0", ["CHK-06-BE-01"], 2),
    T("Backend", "Permission PUT_AWAY_EXECUTE + location scope", "P0", ["F-27", "CHK-06-BE-02"], 3),
    T("Frontend", "PutAwayApiService + facade", "P0", ["CHK-06-BE-02"], 1),
    T("Frontend", "UI-017 pending queue + position picker + confirm", "P0", ["CHK-06-FE-01"], 2),
    T("Testing", "FAC-06-H2/X1 ATP only after put-away", "P0", ["CHK-06-FE-02"], 1),
    T("Testing", "Invalid position / already put away errors", "P1", ["CHK-06-BE-02"], 2),
    T("Documentation", "Received vs available state diagram for UAT", "P2", ["CHK-06-BE-01"], 1),
])

# ---------- F-07 ----------
feat("F-07", "Purchase Order & Inbound Supply Management", ["F-01", "F-02", "F-27"], [
    T("Database", "Create `procurement` schema: suppliers, POs, lines, expected deliveries", "P2", ["F-01", "F-02"], 1),
    T("Database", "PO status CHECKs; supplier_code UK; FKs for lines/deliveries", "P2", ["CHK-07-DB-01"], 2),
    T("Backend", "Supplier + PurchaseOrder aggregates", "P2", ["CHK-07-DB-02"], 1),
    T("Backend", "PurchaseOrderService (create/amend/cancel/schedule delivery)", "P2", ["CHK-07-BE-01"], 2),
    T("Backend", "API-049–053, 059–065, 161–163", "P2", ["CHK-07-BE-02"], 3),
    T("Backend", "Permissions SUPPLIER_MANAGE / PO_MANAGE / PO_VIEW", "P2", ["F-27", "CHK-07-BE-03"], 4),
    T("Frontend", "ProcurementApiService + PurchaseOrderFacade", "P2", ["CHK-07-BE-03"], 1),
    T("Frontend", "UI-011 suppliers, UI-012 POs", "P2", ["CHK-07-FE-01"], 2),
    T("Frontend", "UI-014 delivery planning, UI-019 inbound tracking", "P2", ["CHK-07-FE-01"], 3),
    T("Testing", "FAC-07-H1/H3/V1/V2 API+UI", "P2", ["CHK-07-FE-02"], 1),
    T("Testing", "Receiving integration uses live validate-for-receipt", "P2", ["CHK-07-BE-03", "F-05"], 2),
    T("Documentation", "Replace PO-stub runbook with F-07 cutover notes", "P2", ["CHK-07-BE-03"], 1),
])

# ---------- F-08 ----------
feat("F-08", "Inter-Location Stock Transfers", ["F-02", "F-03", "F-04", "F-27", "F-28"], [
    T("Database", "Create `transfer` schema: requests, transfers, lines, in_transit_stock", "P0", ["F-02"], 1),
    T("Database", "Constraints source!=dest; status CHECKs; optimistic locking", "P0", ["CHK-08-DB-01"], 2),
    T("Backend", "StockTransfer aggregate + capacity evaluation vs stock policy", "P0", ["CHK-08-DB-02", "F-03", "F-04"], 1),
    T("Backend", "TransferService request/approve/reject/dispatch/receive", "P0", ["CHK-08-BE-01", "F-28"], 2),
    T("Backend", "API-098–107, API-042", "P0", ["CHK-08-BE-02"], 3),
    T("Backend", "SoD on approve; TRANSFER_* permissions", "P0", ["F-28", "CHK-08-BE-03"], 4),
    T("Frontend", "TransferApiService + TransferFacade", "P0", ["CHK-08-BE-03"], 1),
    T("Frontend", "UI-038 request, UI-039 approval, UI-040 execution", "P0", ["CHK-08-FE-01"], 2),
    T("Frontend", "In-transit monitor polish (US-061 Phase 2)", "P2", ["CHK-08-FE-02"], 3),
    T("Testing", "FAC-08-H1–H3/V2/E2 golden path + SoD", "P0", ["CHK-08-FE-02"], 1),
    T("Testing", "Source minimum blocks over-transfer", "P0", ["CHK-08-BE-03"], 2),
    T("Documentation", "Transfer state machine for UAT", "P1", ["CHK-08-BE-02"], 1),
])

# ---------- F-09 ----------
feat("F-09", "Network Stock Rebalancing", ["F-04", "F-08", "F-20"], [
    T("Database", "Optional recommendation cache table (or pure query)", "P3", ["F-04"], 1),
    T("Backend", "NetworkRebalancingService + API-166/160/036", "P3", ["F-04", "F-08"], 1),
    T("Backend", "Convert recommendation → transfer request command", "P3", ["CHK-09-BE-01", "F-08"], 2),
    T("Frontend", "UI-041 imbalance analysis + convert action", "P3", ["CHK-09-BE-01"], 1),
    T("Testing", "FAC-09-H1/H2/V2", "P3", ["CHK-09-FE-01"], 1),
    T("Documentation", "Phase 3 scope note / MoSCoW Won't waiver if deferred", "P3", [], 1),
])

# ---------- F-10 ----------
feat("F-10", "Order Availability & Reservation", ["F-04", "F-01", "F-27"], [
    T("Database", "Create fulfillment.customer_orders, order_lines, inventory_reservations", "P0", ["F-04"], 1),
    T("Database", "Optimistic locking on stock_positions for reservation races", "P0", ["CHK-10-DB-01"], 2),
    T("Backend", "CustomerOrderFulfillment aggregate + reservation saga", "P0", ["CHK-10-DB-02"], 1),
    T("Backend", "API-081, 084–086, 043–044 (087 multi-location P2)", "P0", ["CHK-10-BE-01"], 2),
    T("Backend", "ORDER_RESERVE permission + location scope", "P0", ["F-27", "CHK-10-BE-02"], 3),
    T("Frontend", "FulfillmentApiService + ReservationFacade", "P0", ["CHK-10-BE-02"], 1),
    T("Frontend", "UI-030 reservation workbench", "P0", ["CHK-10-FE-01"], 2),
    T("Frontend", "UI-035 multi-location planner (Phase 2)", "P2", ["CHK-10-BE-02"], 3),
    T("Testing", "FAC-10-H1–H3, E1 concurrency, V3 insufficient ATP", "P0", ["CHK-10-FE-02"], 1),
    T("Testing", "Cancel releases reservation restores ATP", "P0", ["CHK-10-BE-02"], 2),
    T("Documentation", "Reservation saga notes + idempotency keys", "P1", ["CHK-10-BE-01"], 1),
])

# ---------- F-11 ----------
feat("F-11", "Pick, Pack & Ship Fulfillment", ["F-10", "F-27"], [
    T("Database", "Create fulfillment_executions, pick_lines, shipments, shipment_lines", "P0", ["F-10"], 1),
    T("Backend", "PickPackShipService + lot selection helpers", "P0", ["CHK-11-DB-01"], 1),
    T("Backend", "API-088–092, 082–083, 097 (+ C-01 location queue)", "P0", ["CHK-11-BE-01"], 2),
    T("Backend", "Deduct on-hand only on ship; FULFILL_PICK/SHIP permissions", "P0", ["CHK-11-BE-02", "F-27"], 3),
    T("Frontend", "PickPackShipFacade + UI-031 workbench", "P0", ["CHK-11-BE-02"], 1),
    T("Frontend", "UI-034 order status", "P0", ["CHK-11-BE-02"], 2),
    T("Testing", "FAC-11-H1–H3; ship-before-pack blocked", "P0", ["CHK-11-FE-01"], 1),
    T("Testing", "Golden path reserve→ship balances", "P0", ["CHK-11-FE-01", "F-10"], 2),
    T("Documentation", "Document C-01 workaround until queue API exists", "P1", ["CHK-11-BE-02"], 1),
])

# ---------- F-12 ----------
feat("F-12", "Partial Fulfillment & Backorder Management", ["F-10", "F-11"], [
    T("Database", "Create `fulfillment.backorders` with priority/status", "P0", ["F-11"], 1),
    T("Backend", "PartialFulfillmentService + BackorderService", "P0", ["CHK-12-DB-01"], 1),
    T("Backend", "API-093–095, 164 (priority Phase 2)", "P0", ["CHK-12-BE-01"], 2),
    T("Backend", "Require customer ack for partial ship", "P0", ["CHK-12-BE-02"], 3),
    T("Frontend", "UI-032 partial ship wizard + backorder board", "P0", ["CHK-12-BE-02"], 1),
    T("Frontend", "Backorder priority UI (Phase 2)", "P2", ["CHK-12-FE-01"], 2),
    T("Testing", "FAC-12-H1/V1; priority sequencing Phase 2", "P0", ["CHK-12-FE-01"], 1),
    T("Documentation", "Partial/backorder customer comms notes", "P2", ["CHK-12-BE-02"], 1),
])

# ---------- F-13 ----------
feat("F-13", "Fulfillment Exception Handling", ["F-11", "F-27"], [
    T("Database", "Create fulfillment exceptions table/fields", "P2", ["F-11"], 1),
    T("Backend", "FulfillmentExceptionService + optional quarantine create", "P2", ["CHK-13-DB-01", "F-18"], 1),
    T("Backend", "API-096, 165, 045; substitution Phase 3", "P2", ["CHK-13-BE-01"], 2),
    T("Frontend", "UI-033 exception queue + resolve forms", "P2", ["CHK-13-BE-02"], 1),
    T("Testing", "FAC-13-H1/H2/V1/P1", "P2", ["CHK-13-FE-01"], 1),
    T("Documentation", "Exception type catalog for WH training", "P2", ["CHK-13-BE-02"], 1),
])

# ---------- F-14 ----------
feat("F-14", "Cycle Counting", ["F-01", "F-02", "F-04", "F-27"], [
    T("Database", "Create `accuracy.cycle_counts`", "P0", ["F-04"], 1),
    T("Backend", "CycleCount aggregate + blind count rules", "P0", ["CHK-14-DB-01"], 1),
    T("Backend", "API-108–111, 168", "P0", ["CHK-14-BE-01"], 2),
    T("Backend", "Permissions CYCLE_COUNT_MANAGE/EXECUTE", "P0", ["F-27", "CHK-14-BE-02"], 3),
    T("Frontend", "UI-023 assignment list + blind entry (hide system qty)", "P0", ["CHK-14-BE-02"], 1),
    T("Testing", "FAC-14-H2/V3 blind enforced; API tests", "P0", ["CHK-14-FE-01"], 1),
    T("Documentation", "Blind count SOP for warehouse staff", "P1", ["CHK-14-FE-01"], 1),
])

# ---------- F-15 ----------
feat("F-15", "Full Physical Inventory Count", ["F-02", "F-04", "F-27"], [
    T("Database", "Create `accuracy.physical_inventory_counts`; freeze flag on locations", "P0", ["F-02"], 1),
    T("Backend", "PhysicalInventoryCountService + LocationFreezeService", "P0", ["CHK-15-DB-01"], 1),
    T("Backend", "API-020, 112–115; block mutators when frozen", "P0", ["CHK-15-BE-01"], 2),
    T("Frontend", "UI-024 initiate/progress/certify + freeze banner", "P0", ["CHK-15-BE-02"], 1),
    T("Testing", "FAC-15-H1/E1 receive blocked while frozen", "P0", ["CHK-15-FE-01", "F-05"], 1),
    T("Documentation", "Physical count freeze checklist", "P1", ["CHK-15-BE-02"], 1),
])

# ---------- F-16 ----------
feat("F-16", "Count Variance Investigation & Approval", ["F-14", "F-15", "F-03", "F-28"], [
    T("Database", "Create count_variances + adjustment case tables", "P0", ["F-14", "F-15"], 1),
    T("Backend", "VarianceInvestigationService + approval routing/thresholds", "P0", ["CHK-16-DB-01", "F-03", "F-28"], 1),
    T("Backend", "API-116–119, 123, 029, 031", "P0", ["CHK-16-BE-01"], 2),
    T("Frontend", "UI-025 investigation + approve/reject", "P0", ["CHK-16-BE-02"], 1),
    T("Testing", "FAC-16-E1 SoD self-approve blocked; H2 approve posts adjust", "P0", ["CHK-16-FE-01"], 1),
    T("Documentation", "Variance approval matrix by threshold", "P1", ["CHK-16-BE-01"], 1),
])

# ---------- F-17 ----------
feat("F-17", "Stock Adjustments & Write-Offs", ["F-03", "F-04", "F-28", "F-27"], [
    T("Database", "Create accuracy.stock_adjustments + inventory_write_offs", "P0", ["F-03"], 1),
    T("Backend", "StockAdjustmentService + WriteOffService + reason validation", "P0", ["CHK-17-DB-01", "F-28"], 1),
    T("Backend", "API-120–122 (+ reason APIs); movement on post", "P0", ["CHK-17-BE-01", "F-29"], 2),
    T("Backend", "Permissions ADJUST_SUBMIT/APPROVE, WRITE_OFF_AUTHORIZE", "P0", ["F-27", "CHK-17-BE-02"], 3),
    T("Frontend", "UI-026 adjustments, UI-027 write-offs", "P0", ["CHK-17-BE-02"], 1),
    T("Testing", "FAC-17-H2/V1/E1/P2", "P0", ["CHK-17-FE-01"], 1),
    T("Documentation", "Reason code usage guide", "P1", ["F-03"], 1),
])

# ---------- F-18 ----------
feat("F-18", "Quarantine & Hold Stock Management", ["F-04", "F-27"], [
    T("Database", "Ensure quarantine_holds table + hold type CHECK", "P2", ["F-04"], 1),
    T("Backend", "QuarantineHoldService apply/release updating ATP", "P2", ["CHK-18-DB-01"], 1),
    T("Backend", "API-045, 046, 154", "P2", ["CHK-18-BE-01"], 2),
    T("Frontend", "UI-028 quarantine register", "P2", ["CHK-18-BE-02"], 1),
    T("Testing", "FAC-18-H1/H2 ATP exclusion", "P2", ["CHK-18-FE-01"], 1),
    T("Documentation", "Hold type definitions for WH", "P2", ["CHK-18-BE-02"], 1),
])

# ---------- F-19 ----------
feat("F-19", "Shrinkage & Obsolescence Analysis", ["F-17", "F-04"], [
    T("Database", "Optional materialized view for shrinkage aggregates", "P2", ["F-17"], 1),
    T("Backend", "ShrinkageAnalysisService + API-167", "P2", ["CHK-19-DB-01"], 1),
    T("Frontend", "UI-029 analysis charts/tables", "P2", ["CHK-19-BE-01"], 1),
    T("Testing", "FAC-19-H1/V1/P1", "P2", ["CHK-19-FE-01"], 1),
    T("Documentation", "Monthly loss review SOP", "P2", ["CHK-19-FE-01"], 1),
])

# ---------- F-20 ----------
feat("F-20", "Low-Stock Alerting & Replenishment", ["F-03", "F-04", "F-27"], [
    T("Database", "Create audit.operational_alerts; purchase_requisitions (Phase 2)", "P0", ["F-03"], 1),
    T("Backend", "StockAlertService threshold breach detection + dedupe", "P0", ["CHK-20-DB-01", "F-04"], 1),
    T("Backend", "API-158–160 alerts/recommendations (MVP)", "P0", ["CHK-20-BE-01"], 2),
    T("Backend", "Requisition APIs 054–058 + list gap C-03 (Phase 2)", "P2", ["CHK-20-DB-01", "F-07"], 3),
    T("Frontend", "UI-036 alert review + ack", "P0", ["CHK-20-BE-02"], 1),
    T("Frontend", "UI-037 / UI-013 requisition flows (Phase 2)", "P2", ["CHK-20-BE-03"], 2),
    T("Testing", "FAC-20-H1/H2/H3; requisition FAC-20-H4 Phase 2", "P0", ["CHK-20-FE-01"], 1),
    T("Documentation", "Alert severity & ack policy", "P1", ["CHK-20-BE-01"], 1),
])

# ---------- F-21 ----------
feat("F-21", "Returns Management", ["F-10", "F-11", "F-05", "F-27"], [
    T("Database", "Create returns schema: RAs, customer_returns, dispositions", "P2", ["F-10"], 1),
    T("Backend", "CustomerReturnCase aggregate + services", "P2", ["CHK-21-DB-01"], 1),
    T("Backend", "API-124–131 (prefer 128 over 076 — C-04)", "P2", ["CHK-21-BE-01"], 2),
    T("Frontend", "UI-042 RA management, UI-043 inspection/disposition", "P2", ["CHK-21-BE-02"], 1),
    T("Testing", "FAC-21-H1–H5/V2/P1", "P2", ["CHK-21-FE-01"], 1),
    T("Documentation", "Returns disposition decision tree", "P2", ["CHK-21-BE-02"], 1),
])

# ---------- F-22 ----------
feat("F-22", "Inventory Reporting & Dashboards", ["F-04"], [
    T("Database", "Reporting views/indexes for dashboard & movements", "P0", ["F-04", "F-05"], 1),
    T("Backend", "DashboardService + OperationalReportService", "P0", ["CHK-22-DB-01"], 1),
    T("Backend", "API-150–152, 155 (+ 167/168 as available)", "P0", ["CHK-22-BE-01"], 2),
    T("Frontend", "Replace UI-002 mocks with live widgets", "P0", ["CHK-22-BE-02"], 1),
    T("Frontend", "UI-044 operational reports + filters/export", "P0", ["CHK-22-BE-02"], 2),
    T("Testing", "FAC-22-H1–H4/P2", "P0", ["CHK-22-FE-01"], 1),
    T("Documentation", "Dashboard widget catalog for roles", "P1", ["CHK-22-FE-01"], 1),
])

# ---------- F-23 ----------
feat("F-23", "Inventory Performance KPIs", ["F-11", "F-04", "F-14", "F-22"], [
    T("Database", "KPI snapshot tables/views", "P3", ["F-22"], 1),
    T("Backend", "KpiService + API-170", "P3", ["CHK-23-DB-01"], 1),
    T("Frontend", "UI-003 executive KPI dashboard", "P3", ["CHK-23-BE-01"], 1),
    T("Testing", "FAC-23-H1/P1", "P3", ["CHK-23-FE-01"], 1),
    T("Documentation", "KPI definitions & targets", "P3", ["CHK-23-BE-01"], 1),
])

# ---------- F-24 ----------
feat("F-24", "Financial Inventory Reconciliation", ["F-05", "F-07", "F-17", "F-29"], [
    T("Database", "finance.supplier_invoices* + valuation snapshot tables", "P3", ["F-07", "F-05"], 1),
    T("Backend", "ThreeWayMatchService + ValuationService + API-077–080, 171–172", "P3", ["CHK-24-DB-01"], 1),
    T("Frontend", "UI-045 valuation reconciliation", "P3", ["CHK-24-BE-01"], 1),
    T("Testing", "FAC-24-H1–H4/V2", "P3", ["CHK-24-FE-01"], 1),
    T("Documentation", "Month-end recon runbook", "P3", ["CHK-24-FE-01"], 1),
])

# ---------- F-25 ----------
feat("F-25", "Promotional & Launch Stock Readiness", ["F-04", "F-10", "F-27"], [
    T("Database", "commercial.promotional_stock_allocations*", "P3", ["F-04"], 1),
    T("Backend", "CampaignAllocationService + API-132–139, 048, 169", "P3", ["CHK-25-DB-01"], 1),
    T("Frontend", "UI-046 promotional readiness", "P3", ["CHK-25-BE-01"], 1),
    T("Testing", "FAC-25-H1/H2/E2 ring-fence isolation", "P3", ["CHK-25-FE-01"], 1),
    T("Documentation", "Campaign readiness checklist", "P3", ["CHK-25-FE-01"], 1),
])

# ---------- F-26 ----------
feat("F-26", "Operational Notifications & Alerts", ["F-27"], [
    T("Database", "Ensure `audit.operational_alerts` with ack columns/indexes", "P0", ["F-27"], 1),
    T("Backend", "NotificationService + role-filtered feed + API-158/159", "P0", ["CHK-26-DB-01"], 1),
    T("Backend", "Wire producers: stock, approval, transfer, fulfillment, inbound, campaign", "P1", ["CHK-26-BE-01", "F-20", "F-17"], 2),
    T("Frontend", "Core NotificationFacade + header badge", "P0", ["CHK-26-BE-01"], 1),
    T("Frontend", "UI-004 notification center list/ack/deep links", "P0", ["CHK-26-FE-01"], 2),
    T("Testing", "FAC-26-H1–H3/P1 role filtering", "P0", ["CHK-26-FE-02"], 1),
    T("Documentation", "Alert taxonomy & recipient matrix", "P1", ["CHK-26-BE-02"], 1),
])

# ---------- F-27 ----------
feat("F-27", "User Access & Role Management", [], [
    T("Database", "Create `identity` schema: user_accounts, role_assignments, role_assignment_locations", "P0", [], 1),
    T("Database", "Seed admin user + baseline roles (UR subset)", "P0", ["CHK-27-DB-01"], 2),
    T("Backend", "Spring Security OAuth2/JWT resource server + session endpoints", "P0", ["CHK-27-DB-02"], 1),
    T("Backend", "UserAccount aggregate + UserAdminService", "P0", ["CHK-27-DB-01"], 2),
    T("Backend", "API-140–149, 173, 174", "P0", ["CHK-27-BE-01", "CHK-27-BE-02"], 3),
    T("Backend", "Authorization evaluate + location-scope validate services", "P0", ["CHK-27-BE-03"], 4),
    T("Frontend", "HttpClient, interceptors, environments, auth/guest guards", "P0", ["CHK-27-BE-01"], 1),
    T("Frontend", "UI-001 real sign-in; AuthService/SessionStore signals", "P0", ["CHK-27-FE-01"], 2),
    T("Frontend", "UI-049 user admin, UI-050 roles/access", "P0", ["CHK-27-BE-03"], 3),
    T("Frontend", "Permission-aware navigation filtering", "P1", ["CHK-27-FE-03"], 4),
    T("Testing", "FAC-27-H1/H3/E1/E2/P1 API+UI", "P0", ["CHK-27-FE-02"], 1),
    T("Testing", "Protected route returns 401 without token", "P0", ["CHK-27-FE-01"], 2),
    T("Documentation", "Auth setup, seed users, role matrix quick ref", "P0", ["CHK-27-BE-03"], 1),
])

# ---------- F-28 ----------
feat("F-28", "Operational Accountability & Controls", ["F-27"], [
    T("Database", "Ensure audit_trail_records; SoD rule seed in governance", "P0", ["F-27"], 1),
    T("Backend", "SegregationOfDutiesService + ActivityLogging aspect/interceptor", "P0", ["CHK-28-DB-01"], 1),
    T("Backend", "API-031, 148, 149 wired into approval commands", "P0", ["CHK-28-BE-01"], 2),
    T("Frontend", "Disable approve actions when SoD evaluate fails; show dialog", "P0", ["CHK-28-BE-02"], 1),
    T("Frontend", "UI-050 SoD/policy configuration surfaces", "P1", ["CHK-28-BE-02"], 2),
    T("Testing", "FAC-28-H2/E1 self-approve blocked on adjustment/variance/transfer", "P0", ["CHK-28-FE-01", "F-17"], 1),
    T("Documentation", "SoD matrix (initiator vs approver) for auditors", "P1", ["CHK-28-BE-01"], 1),
])

# ---------- F-29 ----------
feat("F-29", "Audit Trail & Compliance", ["F-28"], [
    T("Database", "inventory_movement_records + audit_trail_records; REVOKE UPDATE/DELETE", "P0", ["F-28"], 1),
    T("Database", "Indexes on entity/date/user for query performance", "P1", ["CHK-29-DB-01"], 2),
    T("Backend", "MovementAppendService used by all stock mutators", "P0", ["CHK-29-DB-01"], 1),
    T("Backend", "AuditTrailQueryService + API-155–157", "P0", ["CHK-29-BE-01"], 2),
    T("Backend", "Control breach detection (Phase 2)", "P2", ["CHK-29-BE-02"], 3),
    T("Frontend", "UI-022 movement history; UI-048 audit query", "P0", ["CHK-29-BE-02"], 1),
    T("Frontend", "UI-047 audit workspace (Phase 2)", "P2", ["CHK-29-BE-03"], 2),
    T("Testing", "FAC-29-H1/E1 mutate audit forbidden; P1 AUDIT_VIEW", "P0", ["CHK-29-FE-01"], 1),
    T("Documentation", "Audit retention & export policy", "P1", ["CHK-29-BE-02"], 1),
])

# ---------- F-30 ----------
feat("F-30", "System Go-Live & Initial Data Setup", ["F-01", "F-02", "F-27"], [
    T("Database", "Optional import_batches / import_errors staging tables", "P0", ["F-01"], 1),
    T("Backend", "ProductImportService validate/upsert + OpeningBalanceService", "P0", ["CHK-30-DB-01", "F-01", "F-04"], 1),
    T("Backend", "API-010, 032, 017 activation gate", "P0", ["CHK-30-BE-01", "F-02"], 2),
    T("Backend", "SoD: importer ≠ opening approver when required", "P0", ["F-28", "CHK-30-BE-02"], 3),
    T("Frontend", "UI-006 import wizard: upload/validate/review/approve/activate", "P0", ["CHK-30-BE-02"], 1),
    T("Testing", "FAC-30-H1–H3/V1/V4/P3", "P0", ["CHK-30-FE-01"], 1),
    T("Testing", "Production cutover dry-run checklist execution", "P0", ["CHK-30-FE-01"], 2),
    T("Documentation", "Go-live runbook + rollback plan", "P0", ["CHK-30-BE-02"], 1),
])


LAYER_ABBR = {
    "Database": "DB",
    "Backend": "BE",
    "Frontend": "FE",
    "Testing": "TE",
    "Documentation": "DO",
}

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
LAYER_ORDER = ["Database", "Backend", "Frontend", "Testing", "Documentation"]


def task_id(fid, layer, seq):
    n = fid.split("-")[1]
    return f"CHK-{n}-{LAYER_ABBR[layer]}-{seq:02d}"


def resolve_deps(raw_deps, fid):
    """Leave feature deps and cross refs as-is; local CHK refs already correct if seq known."""
    out = []
    for d in raw_deps:
        if d.startswith("CHK-"):
            out.append(d)
        elif d.startswith("F-"):
            out.append(d)
        else:
            out.append(d)
    return out if out else ["—"]


def render_feature(fid, meta):
    name = meta["name"]
    feat_deps = ", ".join(meta["feat_deps"]) if meta["feat_deps"] else "None"
    lines = [
        f"# Implementation Checklist — {fid}: {name}",
        "",
        "| Attribute | Detail |",
        "|-----------|--------|",
        f"| **Feature ID** | {fid} |",
        f"| **Feature Name** | {name} |",
        f"| **Document Type** | Technical Lead Implementation Checklist |",
        f"| **Feature dependencies** | {feat_deps} |",
        f"| **Default status** | Not Started |",
        f"| **Task count** | {len(meta['tasks'])} |",
        "",
        "---",
        "",
        "## Checklist",
        "",
        "| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |",
        "|---------|---------|------------------|-------|----------|--------|--------------|",
    ]
    # renumber seq per layer for stable IDs
    layer_seq = {l: 0 for l in LAYER_ORDER}
    rows = []
    for t in meta["tasks"]:
        layer_seq[t["layer"]] += 1
        tid = task_id(fid, t["layer"], layer_seq[t["layer"]])
        # Fix deps that used provisional CHK-xx-LY-n from generator input
        deps = []
        for d in t["deps"]:
            if d.startswith("CHK-") and d.count("-") >= 3:
                deps.append(d)
            else:
                deps.append(d)
        dep_s = ", ".join(deps) if deps else "—"
        rows.append((tid, fid, t["desc"], t["layer"], t["priority"], "Not Started", dep_s, t["layer"], PRIORITY_ORDER[t["priority"]]))

    # sort by layer then priority then id for readability in file - keep generation order actually
    for r in rows:
        lines.append(f"| `{r[0]}` | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")

    lines += [
        "",
        "## Layer summary",
        "",
        "| Layer | Count |",
        "|-------|-------|",
    ]
    from collections import Counter
    c = Counter(t["layer"] for t in meta["tasks"])
    for l in LAYER_ORDER:
        lines.append(f"| {l} | {c.get(l, 0)} |")

    lines += [
        "",
        "## Priority summary",
        "",
        "| Priority | Meaning | Count |",
        "|----------|---------|-------|",
    ]
    pc = Counter(t["priority"] for t in meta["tasks"])
    meanings = {"P0": "MVP critical / blocking", "P1": "MVP important", "P2": "Phase 2 Should Have", "P3": "Phase 3 / deferred"}
    for p in ["P0", "P1", "P2", "P3"]:
        lines.append(f"| {p} | {meanings[p]} | {pc.get(p, 0)} |")

    lines += [
        "",
        "## Status legend",
        "",
        "| Status | Meaning |",
        "|--------|---------|",
        "| Not Started | Not begun |",
        "| In Progress | Actively being worked |",
        "| Blocked | Waiting on dependency |",
        "| Done | Complete and verified |",
        "| Won't Do | Explicitly waived by PO |",
        "",
        "## Related artifacts",
        "",
        f"- Implementation plan: `implmention/plans/{fid}-*.md`",
        f"- Acceptance criteria: `implmention/acceptance-criteria/{fid}-Acceptance-Criteria.md`",
        "- Sprint plan: `implmention/IMS-Sprint-Plan.md`",
        "",
        f"*Technical Lead checklist — {fid}*",
        "",
    ]
    return "\n".join(lines), rows


def main():
    all_rows = []
    index_rows = []
    total = 0
    for fid in sorted(FEATURES.keys(), key=lambda x: int(x.split("-")[1])):
        meta = FEATURES[fid]
        # Fix task IDs in dependency strings: regenerate tasks with correct sequential IDs per layer
        layer_seq = {l: 0 for l in LAYER_ORDER}
        fixed_tasks = []
        id_map = {}  # provisional -> final not needed if we rewrite deps after
        for i, t in enumerate(meta["tasks"]):
            layer_seq[t["layer"]] += 1
            tid = task_id(fid, t["layer"], layer_seq[t["layer"]])
            # map old style CHK-01-DB-01 from description of provisional seq in source
            old = task_id(fid, t["layer"], t["seq"])
            id_map[old] = tid
            fixed_tasks.append({**t, "_tid": tid, "_old": old})

        # second pass deps
        for t in fixed_tasks:
            new_deps = []
            for d in t["deps"]:
                new_deps.append(id_map.get(d, d))
            t["deps"] = new_deps

        meta["tasks"] = [{k: v for k, v in t.items() if not k.startswith("_") } | {"_tid": t["_tid"]} for t in fixed_tasks]

        # render with explicit tids
        name = meta["name"]
        feat_deps = ", ".join(meta["feat_deps"]) if meta["feat_deps"] else "None"
        lines = [
            f"# Implementation Checklist — {fid}: {name}",
            "",
            "| Attribute | Detail |",
            "|-----------|--------|",
            f"| **Feature ID** | {fid} |",
            f"| **Feature Name** | {name} |",
            f"| **Document Type** | Technical Lead Implementation Checklist |",
            f"| **Feature dependencies** | {feat_deps} |",
            f"| **Default status** | Not Started |",
            f"| **Task count** | {len(meta['tasks'])} |",
            "",
            "---",
            "",
            "## Checklist",
            "",
            "| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |",
            "|---------|---------|------------------|-------|----------|--------|--------------|",
        ]
        for t in meta["tasks"]:
            dep_s = ", ".join(t["deps"]) if t["deps"] else "—"
            lines.append(
                f"| `{t['_tid']}` | {fid} | {t['desc']} | {t['layer']} | {t['priority']} | Not Started | {dep_s} |"
            )
            all_rows.append({
                "id": t["_tid"], "feature": fid, "name": name, "desc": t["desc"],
                "layer": t["layer"], "priority": t["priority"], "status": "Not Started",
                "deps": dep_s,
            })
        from collections import Counter
        c = Counter(t["layer"] for t in meta["tasks"])
        pc = Counter(t["priority"] for t in meta["tasks"])
        lines += ["", "## Layer summary", "", "| Layer | Count |", "|-------|-------|"]
        for l in LAYER_ORDER:
            lines.append(f"| {l} | {c.get(l, 0)} |")
        meanings = {"P0": "MVP critical / blocking", "P1": "MVP important", "P2": "Phase 2 Should Have", "P3": "Phase 3 / deferred"}
        lines += ["", "## Priority summary", "", "| Priority | Meaning | Count |", "|----------|---------|-------|"]
        for p in ["P0", "P1", "P2", "P3"]:
            lines.append(f"| {p} | {meanings[p]} | {pc.get(p, 0)} |")
        lines += [
            "", "## Status legend", "",
            "| Status | Meaning |", "|--------|---------|",
            "| Not Started | Not begun |",
            "| In Progress | Actively being worked |",
            "| Blocked | Waiting on dependency |",
            "| Done | Complete and verified |",
            "| Won't Do | Explicitly waived by PO |",
            "", "## Related artifacts", "",
            f"- Implementation plan: `implmention/plans/` ({fid})",
            f"- Acceptance criteria: `implmention/acceptance-criteria/{fid}-Acceptance-Criteria.md`",
            "- Sprint plan: `implmention/IMS-Sprint-Plan.md`",
            "", f"*Technical Lead checklist — {fid}*", "",
        ]
        fname = f"{fid}-Implementation-Checklist.md"
        (OUT / fname).write_text("\n".join(lines), encoding="utf-8")
        n = len(meta["tasks"])
        total += n
        index_rows.append(f"| {fid} | {name} | {n} | [{fname}](./{fname}) |")
        print("wrote", fname, n)

    # Master consolidated CSV-like markdown table (may be large)
    master_lines = [
        "# IMS Implementation Checklists — Master Index",
        "",
        "| Attribute | Detail |",
        "|-----------|--------|",
        "| **Document ID** | IMPL-CHK-000 |",
        "| **Perspective** | Technical Lead |",
        "| **Date** | July 11, 2026 |",
        f"| **Features** | {len(FEATURES)} |",
        f"| **Total tasks** | {total} |",
        "| **Default status** | Not Started |",
        "",
        "## Layers",
        "",
        "| Layer | Description |",
        "|-------|-------------|",
        "| Database | Schemas, tables, constraints, Flyway migrations |",
        "| Backend | Domain, repos, DTOs, services, controllers, security |",
        "| Frontend | Routes, pages, components, services, forms, state |",
        "| Testing | Unit, API, UI/E2E, permission tests |",
        "| Documentation | OpenAPI, runbooks, UAT notes |",
        "",
        "## Priority",
        "",
        "| Code | Meaning |",
        "|------|---------|",
        "| P0 | MVP critical / blocking |",
        "| P1 | MVP important |",
        "| P2 | Phase 2 Should Have |",
        "| P3 | Phase 3 / deferred |",
        "",
        "## Checklists by feature",
        "",
        "| Feature | Name | Tasks | File |",
        "|---------|------|-------|------|",
    ] + index_rows + [
        "",
        "## How to use",
        "",
        "1. Open the feature checklist for the current sprint feature.",
        "2. Work **Database → Backend → Frontend → Testing → Documentation** unless blocked.",
        "3. Update **Status** in the feature file as work progresses.",
        "4. Do not mark Done until related FAC-* acceptance criteria pass.",
        "",
        "## Related",
        "",
        "- [IMS-Sprint-Plan.md](../IMS-Sprint-Plan.md)",
        "- [IMS-Feature-Dependency-Map.md](../IMS-Feature-Dependency-Map.md)",
        "- [plans/README.md](../plans/README.md)",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(master_lines), encoding="utf-8")

    # Full consolidated checklist
    consol = [
        "# IMS Consolidated Implementation Checklist",
        "",
        f"**Total tasks:** {total} · **Status baseline:** Not Started",
        "",
        "| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |",
        "|---------|---------|------------------|-------|----------|--------|--------------|",
    ]
    for r in all_rows:
        consol.append(
            f"| `{r['id']}` | {r['feature']} | {r['desc']} | {r['layer']} | {r['priority']} | {r['status']} | {r['deps']} |"
        )
    consol.append("")
    (OUT / "IMS-Consolidated-Implementation-Checklist.md").write_text("\n".join(consol), encoding="utf-8")
    print("TOTAL", total, "tasks across", len(FEATURES), "features")


if __name__ == "__main__":
    main()
