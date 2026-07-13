# -*- coding: utf-8 -*-
"""Generate complete per-feature implementation plans for IMS."""
from pathlib import Path

OUT = Path(__file__).resolve().parent

# Shared conventions block referenced in every plan
STACK = """
**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors
"""

ERROR_CONTRACT = """
| HTTP | Category | Typical `errorCode` prefix |
|------|----------|---------------------------|
| 400 | validation-error | `VAL_*` |
| 401 | authentication-error | `AUTH_*` |
| 403 | authorization-error | `AUTHZ_*` |
| 404 | not-found | `NOT_FOUND_*` |
| 409 | conflict | `CONFLICT_*` |
| 422 | business-rule-violation | `BIZ_*` / `BR-*` |
| 500 | internal-server-error | `SYS_*` |

Envelope: RFC 7807 `ProblemDetailResponse` (`type`, `title`, `status`, `detail`, `instance`, `errorCode`, `traceId`, `timestamp`, optional `errors[]`).
"""

FEATURES = [
  {
    "id": "F-01",
    "name": "Product Catalog Management",
    "file": "F-01-Product-Catalog-Management.md",
    "overview": "Create, update, search, and govern product master records (SKU identity, attributes, lifecycle, duplicate resolution) as the single product source of truth.",
    "goal": "Eliminate duplicate product identities and ensure every location references the same SKU, attributes, and lifecycle rules (BO-01, BO-21).",
    "stories": ["US-001", "US-002", "US-003", "US-004"],
    "ac": [
      "AC-001-H1/H2, V1/V2, E1/E2, X1/X2 — create/update product master",
      "AC-002-* — lifecycle ACTIVE/INACTIVE/DISCONTINUED with audit of prior status",
      "AC-003-* — lookup by SKU/barcode with location-scoped stock context",
      "AC-004-* — duplicate detection, merge/reject with justification",
    ],
    "prev": ["F-27"],
    "module": "M-01 Product Catalog (`ims.catalog`)",
    "schema": "catalog",
    "tables": [
      ("catalog.products", "Product master; SKU unique; lifecycle; ABC; UoM; rotation"),
      ("catalog.product_identifiers", "Alternate IDs/barcodes → product"),
    ],
    "rels": [
      "product_identifiers.product_id → products.id (FK, CASCADE delete restricted if history)",
      "Referenced by identity only from inventory, procurement, fulfillment (SKU)",
    ],
    "constraints": [
      "uk_products_sku; nn_products_sku/name/uom; chk_domain_lifecycle_status",
      "chk_domain_abc_classification (nullable until assigned); chk_domain_rotation_policy",
      "uk_product_identifiers (identifier_type, identifier_value)",
    ],
    "migrations": [
      "V1_01__catalog_schema.sql — create schema catalog",
      "V1_02__catalog_products.sql — products + identifiers + indexes on sku, name, status",
      "V1_03__catalog_seed_categories_if_needed.sql (optional reference data)",
    ],
    "entities": ["Product (AR)", "ProductIdentifier (VO or child entity)"],
    "vos": ["ProductSku", "ProductCategory", "ProductLifecycleStatus", "UnitOfMeasure", "AbcClassification", "RotationPolicy", "ShelfLifeProfile"],
    "repos": ["ProductRepository", "ProductIdentifierRepository (or embedded)"],
    "dtos_req": ["CreateProductRequest", "UpdateProductRequest", "ChangeLifecycleStatusRequest", "ResolveDuplicateRequest", "ProductSearchQuery"],
    "dtos_res": ["ProductResponse", "ProductSummaryResponse", "PagedResponse<ProductSummaryResponse>", "DuplicateResolutionResultResponse", "EligibilityResponse"],
    "validation": ["VR-001/007 SKU pattern", "mandatory name/UoM", "duplicate SKU", "lifecycle transition rules BR-027"],
    "services": ["ProductCatalogService / ProductApplicationService", "DuplicateDetectionService"],
    "controllers": ["ProductController — /api/v1/products"],
    "exceptions": ["DuplicateSkuException → 409", "ProductNotFoundException → 404", "InvalidLifecycleTransitionException → 422", "UnauthorizedProductMaintenanceException → 403"],
    "security": ["Permission: PRODUCT_MANAGE / PRODUCT_VIEW", "location scope N/A for catalog; audit createdBy"],
    "routes": [
      "products/catalog (list)",
      "products/catalog/new",
      "products/catalog/:sku",
      "products/catalog/:sku/edit",
      "products/catalog/duplicates (optional)",
    ],
    "pages": ["ProductCatalogPage (UI-005)", "ProductDetailPage", "ProductFormPage", "DuplicateResolutionDialog"],
    "components": ["ProductSearchBar", "ProductForm", "LifecycleStatusBadge", "IdentifierEditor", "DuplicateComparePanel"],
    "fe_models": ["ProductVm", "ProductIdentifierVm", "LifecycleStatus"],
    "fe_services": ["ProductApiService", "ProductFacade"],
    "forms": ["ProductCreateForm", "ProductEditForm", "LifecycleChangeForm"],
    "fe_validation": ["required sku/name/uom", "sku pattern", "async duplicate check"],
    "state": ["ProductFacade signals: list, filters, selectedSku, saveState"],
    "apis": [
      "API-001 POST /api/v1/products",
      "API-002 GET /api/v1/products",
      "API-003 GET /api/v1/products/{sku}",
      "API-004 PATCH /api/v1/products/{sku}",
      "API-005 POST /api/v1/products/{sku}/lifecycle-status",
      "API-007 GET /api/v1/products/{sku}/eligibility",
      "API-008 GET /api/v1/products/categories/{categoryCode}/products",
      "API-009 POST /api/v1/products/duplicate-resolutions",
    ],
    "qa_func": ["Create/update/search product UAT per AC-001–004", "Lifecycle blocks reservation when discontinued"],
    "qa_api": ["Contract tests for API-001–009", "400/403/409/422 cases"],
    "qa_ui": ["UI-005 CRUD happy path", "duplicate banner", "permission denied"],
  },
  {
    "id": "F-02",
    "name": "Location & Network Setup",
    "file": "F-02-Location-Network-Setup.md",
    "overview": "Configure inventory locations, hierarchy, storage positions, and location operational lifecycle (activate/deactivate/close).",
    "goal": "Enable stock assignment, tracking, and reporting at the correct warehouses, stores, and DCs (BO-01).",
    "stories": ["US-005", "US-006", "US-007", "US-010"],
    "ac": ["AC-005-* location CRUD", "AC-006-* hierarchy", "AC-007-* closure disposition (P2)", "AC-010-* opening balance gate before operational"],
    "prev": ["F-27"],
    "module": "M-02 Warehouse Network (`ims.network`)",
    "schema": "network",
    "tables": [
      ("network.inventory_locations", "Location master + hierarchy + freeze/operational status"),
      ("network.storage_positions", "Zone/aisle/bin under location"),
    ],
    "rels": [
      "storage_positions.location_id → inventory_locations.id",
      "inventory_locations.parent_location_id → inventory_locations.id (self-FK)",
    ],
    "constraints": [
      "uk_inventory_locations_location_code; no self-parent cycle (app + CHECK)",
      "nn location name/type/status; chk operational status enums",
    ],
    "migrations": [
      "V1_10__network_schema.sql",
      "V1_11__inventory_locations.sql",
      "V1_12__storage_positions.sql",
    ],
    "entities": ["InventoryLocation (AR)", "StoragePosition"],
    "vos": ["LocationCode", "LocationType", "LocationHierarchyPath", "PhysicalAddress", "EffectivePeriod"],
    "repos": ["InventoryLocationRepository", "StoragePositionRepository"],
    "dtos_req": ["CreateLocationRequest", "UpdateHierarchyRequest", "CreateStoragePositionRequest", "ActivateLocationRequest", "CloseLocationRequest"],
    "dtos_res": ["LocationResponse", "LocationSummaryResponse", "StoragePositionResponse", "FreezeStatusResponse", "OperationalStatusResponse"],
    "validation": ["VR-011 LocationCode", "hierarchy acyclic", "close blocked if stock remains unless disposition"],
    "services": ["WarehouseNetworkService", "LocationLifecycleService"],
    "controllers": ["LocationController — /api/v1/locations"],
    "exceptions": ["LocationNotFoundException", "InvalidHierarchyException", "LocationCloseBlockedException", "LocationFrozenException"],
    "security": ["LOCATION_MANAGE / LOCATION_VIEW", "Ops Director for hierarchy/closure"],
    "routes": ["locations", "locations/new", "locations/:locationCode", "locations/:locationCode/storage"],
    "pages": ["LocationWarehouseManagementPage (UI-007)", "LocationDetailPage", "StoragePositionEditor"],
    "components": ["LocationForm", "HierarchyTree", "StoragePositionGrid", "OperationalStatusChip"],
    "fe_models": ["LocationVm", "StoragePositionVm"],
    "fe_services": ["LocationApiService", "LocationFacade"],
    "forms": ["LocationForm", "StoragePositionForm", "ActivateLocationForm"],
    "fe_validation": ["required code/name/type", "parent != self"],
    "state": ["LocationFacade: tree, selected location, positions"],
    "apis": [
      "API-011 POST /api/v1/locations",
      "API-012 GET /api/v1/locations",
      "API-013 GET /api/v1/locations/{locationCode}",
      "API-014 PATCH .../hierarchy",
      "API-015/016 storage-positions",
      "API-017/018/019 activate/deactivate/close",
      "API-020 freeze-status",
      "API-021 operational-status",
    ],
    "qa_func": ["Create location + storage bins", "hierarchy rollup", "activation requires opening balance policy"],
    "qa_api": ["API-011–021 contract + freeze status"],
    "qa_ui": ["UI-007 create/edit/list", "storage position add"],
  },
  {
    "id": "F-03",
    "name": "Stock Policy & Product Classification",
    "file": "F-03-Stock-Policy-Product-Classification.md",
    "overview": "Define per product-location stock thresholds, ABC class, governance policies, reason codes, approval thresholds, and receipt tolerances.",
    "goal": "Drive proactive replenishment, differentiated counting, and consistent exception governance (BO-05).",
    "stories": ["US-008", "US-009", "US-012", "US-056"],
    "ac": ["AC-008-* thresholds", "AC-009-* ABC (P2)", "AC-012-* governance policies (P2)", "AC-056-* safety stock protection"],
    "prev": ["F-01", "F-02", "F-27"],
    "module": "M-03 Inventory Governance + M-04 Stock Policy",
    "schema": "inventory + governance",
    "tables": [
      ("inventory.stock_policies", "Reorder/min/safety per location+sku"),
      ("inventory.stock_policy_history", "Immutable threshold history"),
      ("governance.governance_policies", "Policy versions"),
      ("governance.reason_codes", "Standardized reason taxonomy"),
    ],
    "rels": [
      "stock_policies references ProductSku + LocationCode (logical FKs)",
      "reason_codes owned by governance_policies / independent with retire",
    ],
    "constraints": [
      "uk_stock_policies (location_code, sku)",
      "chk quantities >= 0; min <= reorder unless authorized invert",
      "uk_reason_codes_code; retired codes not selectable",
    ],
    "migrations": [
      "V1_20__governance_schema.sql",
      "V1_21__reason_codes_policies.sql",
      "V1_22__stock_policies.sql",
    ],
    "entities": ["StockPolicy (AR)", "GovernancePolicy (AR)", "ReasonCode"],
    "vos": ["StockThresholdSet", "ApprovalThreshold", "QuantityTolerance", "EffectivePeriod", "AbcClass"],
    "repos": ["StockPolicyRepository", "GovernancePolicyRepository", "ReasonCodeRepository"],
    "dtos_req": ["CreateStockPolicyRequest", "UpdateStockPolicyRequest", "AssignAbcRequest", "CreateReasonCodeRequest", "UpdateApprovalThresholdsRequest", "UpdateReceiptTolerancesRequest"],
    "dtos_res": ["StockPolicyResponse", "ReasonCodeResponse", "GovernancePolicyResponse", "ApprovalThresholdResponse", "ReceiptToleranceResponse"],
    "validation": ["VR thresholds", "VR-021 ABC", "VR-026/027 reason codes", "effective dating non-overlap"],
    "services": ["StockPolicyService", "GovernanceService", "SafetyStockProtectionService"],
    "controllers": ["StockPolicyController", "GovernanceController", "ProductAbc endpoint on ProductController"],
    "exceptions": ["PolicyNotFoundException", "ReasonCodeRetiredException", "InvalidThresholdException", "SafetyStockBypassRejectedException"],
    "security": ["POLICY_MANAGE", "GOVERNANCE_MANAGE", "ABC_ASSIGN"],
    "routes": ["products/stock-policies", "products/abc-classification", "governance/policies"],
    "pages": ["StockPolicyPage (UI-008)", "AbcClassificationPage (UI-009)", "GovernancePoliciesPage (UI-010)"],
    "components": ["ThresholdForm", "ReasonCodeTable", "ToleranceEditor", "AbcAssignGrid"],
    "fe_models": ["StockPolicyVm", "ReasonCodeVm", "GovernancePolicyVm"],
    "fe_services": ["StockPolicyApiService", "GovernanceApiService", "PolicyFacade"],
    "forms": ["StockPolicyForm", "ReasonCodeForm", "ThresholdForm"],
    "fe_validation": ["min/reorder/safety numeric rules", "effective date required"],
    "state": ["PolicyFacade: selected location/sku, policy draft"],
    "apis": [
      "API-038/039/040 stock-policies",
      "API-006 ABC classification",
      "API-022–030 governance reason codes, policies, thresholds, tolerances",
    ],
    "qa_func": ["Set thresholds → status/alerts consume", "retire reason code blocks new use"],
    "qa_api": ["API-006, 022–030, 038–040"],
    "qa_ui": ["UI-008/009/010 forms + list"],
  },
  {
    "id": "F-04",
    "name": "Inventory Visibility & Search",
    "file": "F-04-Inventory-Visibility-Search.md",
    "overview": "Real-time on-hand, reserved, ATP, stock status, and multi-criteria search across authorized locations.",
    "goal": "Provide a trusted single source of truth for stock questions without spreadsheets (BO-01, BO-16).",
    "stories": ["US-023", "US-024", "US-025", "US-026", "US-027", "US-028"],
    "ac": ["AC-023–027 MVP visibility", "AC-028 network/inbound views Phase 2"],
    "prev": ["F-01", "F-02", "F-27"],
    "module": "M-04 Inventory Balance + M-13 Intelligence (read)",
    "schema": "inventory (+ reads catalog/network)",
    "tables": [
      ("inventory.stock_positions", "On-hand/reserved/ATP authoritative"),
      ("inventory.lot_batches", "Lot breakdown"),
      ("inventory.quarantine_holds", "Excluded from ATP"),
      ("inventory.stock_policies", "Status derivation"),
    ],
    "rels": [
      "stock_positions unique (location_code, sku)",
      "lots/holds compose under stock_position",
    ],
    "constraints": [
      "chk on_hand/reserved/quarantine >= 0",
      "ATP invariant enforced in domain (on_hand - reserved - hold)",
    ],
    "migrations": [
      "V1_30__inventory_stock_positions.sql",
      "V1_31__lot_batches_quarantine.sql",
      "Indexes on (location_code, sku), status",
    ],
    "entities": ["StockPosition (AR)", "LotBatch", "QuarantineHold"],
    "vos": ["StockAvailabilityBreakdown", "StockStatusIndicator", "Quantity", "OwnershipClassification"],
    "repos": ["StockPositionRepository", "StockPositionQueryRepository"],
    "dtos_req": ["StockPositionSearchQuery", "AvailabilityQuery"],
    "dtos_res": ["StockPositionResponse", "AvailabilityResponse", "NetworkAvailabilityResponse", "StockStatusResponse", "StockStatusBoardResponse"],
    "validation": ["sku/location exist", "page size limits"],
    "services": ["InventoryVisibilityQueryService", "AtpCalculationService (read)"],
    "controllers": ["StockPositionController", "AvailabilityController", "IntelligenceStockStatusController"],
    "exceptions": ["StockPositionNotFoundException", "UnauthorizedLocationAccessException"],
    "security": ["INVENTORY_VIEW", "location-scope filter mandatory"],
    "routes": ["inventory/status-monitor", "inventory/availability", "home/operations (widgets)"],
    "pages": ["InventoryStatusMonitorPage (UI-020)", "AvailabilityInquiryPage (UI-021)", "OperationalDashboardPage widgets"],
    "components": ["StockStatusBoard", "AtpBadge", "LocationSkuFilter", "StockPositionTable"],
    "fe_models": ["StockPositionVm", "AvailabilityVm", "StockStatus"],
    "fe_services": ["InventoryApiService", "InventoryVisibilityFacade"],
    "forms": ["AvailabilitySearchForm", "StatusFilterForm"],
    "fe_validation": ["sku required for inquiry"],
    "state": ["filters, results, selected position signals"],
    "apis": [
      "API-033/034 stock-positions",
      "API-035/036 availability",
      "API-037 stock-status",
      "API-012 locations",
      "API-151/152/153 intelligence",
    ],
    "qa_func": ["ATP matches on_hand-reserved-hold", "location scope hides other sites"],
    "qa_api": ["API-033–037, 151–153"],
    "qa_ui": ["UI-020/021 search/filter/drill"],
  },
  {
    "id": "F-05",
    "name": "Goods Receiving & Verification",
    "file": "F-05-Goods-Receiving-Verification.md",
    "overview": "Receive and verify inbound goods, capture discrepancies, support non-PO/return intake, and emit immutable movement history.",
    "goal": "Ensure on-hand reflects physical reality from entry and protect supplier accountability (BO-03).",
    "stories": ["US-015", "US-016", "US-017", "US-019", "US-020", "US-029"],
    "ac": ["AC-015–017 receiving", "AC-019 non-PO/return", "AC-020 tolerance P2", "AC-029 movement history"],
    "prev": ["F-01", "F-02", "F-03", "F-27"],
    "module": "M-06 Inbound Receiving",
    "schema": "inbound (+ inventory, audit, procurement refs)",
    "tables": [
      ("inbound.goods_receipts", "Receipt header"),
      ("inbound.goods_receipt_lines", "Lines + lots/shelf life"),
      ("inbound.receipt_discrepancies", "Shortage/over/wrong/damage"),
      ("audit.inventory_movement_records", "Immutable movements"),
    ],
    "rels": [
      "goods_receipt_lines → goods_receipts",
      "discrepancies → goods_receipts",
      "optional FK purchase_order_id",
    ],
    "constraints": [
      "positive line qty; reason code on discrepancy",
      "PO validate-for-receipt when PO-backed (BR-007)",
    ],
    "migrations": [
      "V1_40__inbound_schema.sql",
      "V1_41__goods_receipts.sql",
      "V1_42__discrepancies.sql",
      "V1_43__movement_records.sql",
    ],
    "entities": ["GoodsReceipt (AR)", "ReceiptDiscrepancy", "GoodsReceiptLine"],
    "vos": ["PositiveQuantity", "LotIdentity", "ShelfLifeProfile", "ReasonCodeAttribution"],
    "repos": ["GoodsReceiptRepository", "InventoryMovementRecordRepository"],
    "dtos_req": ["CreateGoodsReceiptRequest", "VerifyGoodsReceiptRequest", "CreateDiscrepancyRequest", "ResolveDiscrepancyRequest", "AdHocReceiptRequest", "ReturnReceiptRequest"],
    "dtos_res": ["GoodsReceiptResponse", "DiscrepancyResponse", "MovementHistoryResponse", "PagedResponse"],
    "validation": ["PO authorization", "lot required if traceable BR-017", "tolerance BR-006/008", "reason codes"],
    "services": ["GoodsReceivingService", "DiscrepancyService", "MovementRecordingService"],
    "controllers": ["GoodsReceiptController", "AdHocReceiptController", "MovementIntelligenceController"],
    "exceptions": ["PoNotValidForReceiptException", "ReceiptVerificationFailedException", "DiscrepancyResolutionInvalidException"],
    "security": ["RECEIVE_GOODS", "RESOLVE_DISCREPANCY", "location-scoped"],
    "routes": ["inbound/goods-receipts", "inbound/goods-receipts/:id", "inbound/discrepancies", "inbound/non-po-receipts", "inventory/movement-history"],
    "pages": ["GoodsReceiptWorkbenchPage (UI-015)", "DiscrepancyResolutionPage (UI-016)", "NonPoReturnIntakePage (UI-018)", "MovementHistoryPage (UI-022)"],
    "components": ["ReceiptLineEditor", "VerifyPanel", "DiscrepancyForm", "LotCaptureFields", "MovementFilter"],
    "fe_models": ["GoodsReceiptVm", "DiscrepancyVm", "MovementVm"],
    "fe_services": ["InboundApiService", "GoodsReceiptFacade"],
    "forms": ["ReceiptCreateForm", "VerifyForm", "DiscrepancyForm", "AdHocReceiptForm"],
    "fe_validation": ["line qty > 0", "lot if required", "reason code required on discrepancy"],
    "state": ["active receipt, lines, discrepancy queue"],
    "apis": [
      "API-065 validate-for-receipt",
      "API-066–072 goods receipts + discrepancies",
      "API-075/076 ad-hoc + return receipts",
      "API-025/030 reason/tolerance",
      "API-155 movements",
    ],
    "qa_func": ["PO receipt happy path", "discrepancy resolve", "movement immutable"],
    "qa_api": ["API-065–076, 155"],
    "qa_ui": ["UI-015/016/018/022 E2E"],
  },
  {
    "id": "F-06",
    "name": "Put-Away Management",
    "file": "F-06-Put-Away-Management.md",
    "overview": "Confirm storage placement of received stock so sellable ATP reflects locatable inventory.",
    "goal": "Prevent promising stock pickers cannot find (BO-03, BO-06).",
    "stories": ["US-018"],
    "ac": ["AC-018-* pending put-away queue, confirm position, ATP update only after put-away"],
    "prev": ["F-05", "F-02", "F-27"],
    "module": "M-06 Inbound Receiving",
    "schema": "inbound + network + inventory",
    "tables": [
      ("inbound.put_aways", "Put-away confirmation records"),
      ("network.storage_positions", "Destination bins"),
      ("inventory.stock_positions", "Availability state update"),
    ],
    "rels": ["put_aways → goods_receipts; storage_position_id FK"],
    "constraints": ["put-away only when receipt verified; position belongs to receipt location"],
    "migrations": ["V1_44__put_aways.sql"],
    "entities": ["GoodsReceipt (put-away method)", "PutAway record"],
    "vos": ["StoragePositionCode", "Quantity"],
    "repos": ["PutAwayRepository", "GoodsReceiptRepository"],
    "dtos_req": ["ConfirmPutAwayRequest"],
    "dtos_res": ["PutAwayResultResponse", "PendingPutAwayResponse"],
    "validation": ["position exists at location", "qty matches pending"],
    "services": ["PutAwayService"],
    "controllers": ["PutAwayController"],
    "exceptions": ["NoPendingPutAwayException", "InvalidStoragePositionException"],
    "security": ["PUT_AWAY_EXECUTE", "location-scoped"],
    "routes": ["inbound/put-away", "inbound/put-away/:goodsReceiptId"],
    "pages": ["PutAwayWorkbenchPage (UI-017)"],
    "components": ["PendingPutAwayQueue", "PositionPicker", "PutAwayConfirmForm"],
    "fe_models": ["PendingPutAwayVm"],
    "fe_services": ["PutAwayApiService", "PutAwayFacade"],
    "forms": ["PutAwayForm"],
    "fe_validation": ["position required"],
    "state": ["pending queue, selected receipt"],
    "apis": ["API-074 GET pending-put-away", "API-073 POST put-away", "API-015/016 storage positions"],
    "qa_func": ["ATP increases only after put-away"],
    "qa_api": ["API-073/074"],
    "qa_ui": ["UI-017 complete task"],
  },
  {
    "id": "F-07",
    "name": "Purchase Order & Inbound Supply Management",
    "file": "F-07-Purchase-Order-Inbound-Supply.md",
    "overview": "Supplier master, PO lifecycle, expected deliveries, inbound tracking, and delay visibility.",
    "goal": "Give operations visibility into when shortages will be resolved (BO-05).",
    "stories": ["US-013", "US-014", "US-021", "US-022", "US-055", "US-079"],
    "ac": ["AC-013/014 PO", "AC-021 amend/cancel", "AC-055 tracking", "AC-022 supplier performance P3", "AC-079 delay notify"],
    "prev": ["F-01", "F-02", "F-27"],
    "module": "M-05 Procurement & Supplier",
    "schema": "procurement",
    "tables": [
      ("procurement.suppliers", "Supplier master"),
      ("procurement.purchase_orders / purchase_order_lines", "PO commitment"),
      ("procurement.expected_inbound_deliveries (+ lines)", "Delivery plan"),
    ],
    "rels": ["PO → supplier; expected delivery → PO; lines → sku"],
    "constraints": ["uk supplier_code; chk_domain_po_status; active supplier for new PO"],
    "migrations": ["V2_10__procurement_suppliers.sql", "V2_11__purchase_orders.sql", "V2_12__expected_deliveries.sql"],
    "entities": ["Supplier", "PurchaseOrder (AR)", "ExpectedInboundDelivery"],
    "vos": ["SupplierCode", "PaymentTerms", "LeadTimeDuration", "PurchaseOrderLine"],
    "repos": ["SupplierRepository", "PurchaseOrderRepository"],
    "dtos_req": ["CreateSupplierRequest", "CreatePurchaseOrderRequest", "AmendPurchaseOrderRequest", "CancelPurchaseOrderRequest", "ScheduleExpectedDeliveryRequest"],
    "dtos_res": ["SupplierResponse", "PurchaseOrderResponse", "OpenPoBoardResponse", "InboundCalendarResponse", "InboundDelayResponse"],
    "validation": ["product active BR-027", "supplier active", "qty > 0"],
    "services": ["SupplierService", "PurchaseOrderService", "InboundSupplyQueryService"],
    "controllers": ["SupplierController", "PurchaseOrderController", "ProcurementIntelligenceController"],
    "exceptions": ["SupplierInactiveException", "PoAmendNotAllowedException", "PoCancelBlockedException"],
    "security": ["SUPPLIER_MANAGE", "PO_MANAGE", "PO_VIEW"],
    "routes": ["procurement/suppliers", "procurement/purchase-orders", "procurement/inbound-delivery-planning", "procurement/inbound-supply-tracking"],
    "pages": ["SupplierManagementPage (UI-011)", "PurchaseOrderPage (UI-012)", "InboundDeliveryPlanningPage (UI-014)", "InboundSupplyTrackingPage (UI-019)"],
    "components": ["PoLineEditor", "SupplierForm", "DeliveryCalendar", "OpenPoTable"],
    "fe_models": ["SupplierVm", "PurchaseOrderVm", "ExpectedDeliveryVm"],
    "fe_services": ["ProcurementApiService", "PurchaseOrderFacade"],
    "forms": ["SupplierForm", "PoForm", "ExpectedDeliveryForm"],
    "fe_validation": ["supplier required", "line sku/qty"],
    "state": ["po list filters, selected PO, delivery draft"],
    "apis": ["API-049–053 suppliers", "API-059–065 POs", "API-161–163 intelligence"],
    "qa_func": ["Create PO → validate-for-receipt", "amend/cancel rules"],
    "qa_api": ["API-049–065, 161–163"],
    "qa_ui": ["UI-011/012/014/019"],
  },
  {
    "id": "F-08",
    "name": "Inter-Location Stock Transfers",
    "file": "F-08-Inter-Location-Stock-Transfers.md",
    "overview": "Request, approve, dispatch, and receive inter-location transfers with source minimum protection and in-transit tracking.",
    "goal": "Resolve local stockouts using network inventory without cascading shortages (BO-05, BR-011/012).",
    "stories": ["US-058", "US-059", "US-060", "US-061", "US-063"],
    "ac": ["AC-058 request", "AC-059 approve/reject", "AC-060 execute", "AC-061 in-transit P2", "AC-063 source minimum"],
    "prev": ["F-02", "F-03", "F-04", "F-27", "F-28"],
    "module": "M-08 Network Transfer",
    "schema": "transfer + inventory",
    "tables": [
      ("transfer.transfer_requests (+ lines)", "Request"),
      ("transfer.stock_transfers (+ lines)", "Execution"),
      ("transfer.in_transit_stock", "In-transit qty"),
    ],
    "rels": ["request → transfer on approve; lines sku/qty; source/dest location codes"],
    "constraints": ["source != dest; transfer capacity respects min threshold; SoD on approve"],
    "migrations": ["V1_50__transfer_schema.sql", "V1_51__transfer_requests.sql", "V1_52__stock_transfers_in_transit.sql"],
    "entities": ["StockTransfer (AR)", "TransferRequest state"],
    "vos": ["TransferLine", "InTransitQuantity", "UserActionAttribution"],
    "repos": ["TransferRepository", "TransferQueryRepository"],
    "dtos_req": ["CreateTransferRequest", "ApproveTransferRequest", "RejectTransferRequest", "DispatchTransferRequest", "ReceiveTransferRequest"],
    "dtos_res": ["TransferResponse", "PendingApprovalResponse", "InTransitResponse", "TransferCapacityResponse"],
    "validation": ["capacity API-042", "SoD", "location operational"],
    "services": ["TransferService", "TransferCapacityService"],
    "controllers": ["TransferController"],
    "exceptions": ["InsufficientTransferCapacityException", "SoDViolationException", "TransferStateException"],
    "security": ["TRANSFER_REQUEST", "TRANSFER_APPROVE", "TRANSFER_EXECUTE"],
    "routes": ["transfers/requests", "transfers/approvals", "transfers/execution"],
    "pages": ["TransferRequestPage (UI-038)", "TransferApprovalQueuePage (UI-039)", "TransferExecutionPage (UI-040)"],
    "components": ["TransferLineEditor", "ApprovalQueue", "DispatchReceivePanel", "InTransitBoard"],
    "fe_models": ["TransferVm", "TransferCapacityVm"],
    "fe_services": ["TransferApiService", "TransferFacade"],
    "forms": ["TransferRequestForm", "RejectReasonForm", "ReceiveForm"],
    "fe_validation": ["source != dest", "qty > 0", "justification required"],
    "state": ["request draft, approval queue, in-transit list"],
    "apis": ["API-098–107", "API-042 transfer-capacity"],
    "qa_func": ["request→approve→dispatch→receive balances both sites", "source min blocks"],
    "qa_api": ["API-098–107, 042"],
    "qa_ui": ["UI-038–040"],
  },
  {
    "id": "F-09",
    "name": "Network Stock Rebalancing",
    "file": "F-09-Network-Stock-Rebalancing.md",
    "overview": "Analyze network imbalance and recommend redistribution convertible to transfer requests.",
    "goal": "Optimize enterprise stock distribution (Phase 3 / deferred).",
    "stories": ["US-062"],
    "ac": ["AC-062-* imbalance analysis and recommendation → transfer"],
    "prev": ["F-04", "F-08", "F-20"],
    "module": "M-13 Inventory Intelligence",
    "schema": "read inventory/policies; write via transfer",
    "tables": [("Read models over inventory.stock_positions + stock_policies", "No dedicated write tables")],
    "rels": ["Recommendations create transfer.transfer_requests"],
    "constraints": ["Recommendations must respect source minimums"],
    "migrations": ["Optional V3_01__rebalance_recommendation_cache.sql"],
    "entities": ["None (query service); may use recommendation DTO aggregate"],
    "vos": ["ImbalanceScore", "RebalanceRecommendation"],
    "repos": ["NetworkImbalanceQueryRepository"],
    "dtos_req": ["RebalanceAnalysisQuery"],
    "dtos_res": ["NetworkImbalanceResponse", "RebalanceRecommendationResponse"],
    "validation": ["sku/location filters"],
    "services": ["NetworkRebalancingService"],
    "controllers": ["NetworkIntelligenceController"],
    "exceptions": ["InsufficientDataForRebalanceException"],
    "security": ["NETWORK_REBALANCE_VIEW", "TRANSFER_REQUEST to act"],
    "routes": ["transfers/network-rebalancing"],
    "pages": ["NetworkRebalancingAnalysisPage (UI-041)"],
    "components": ["ImbalanceHeatmap", "RecommendationTable", "ConvertToTransferAction"],
    "fe_models": ["ImbalanceVm", "RecommendationVm"],
    "fe_services": ["RebalanceApiService", "RebalanceFacade"],
    "forms": ["RebalanceFilterForm"],
    "fe_validation": ["date/network filters"],
    "state": ["analysis results, selected recommendations"],
    "apis": ["API-036", "API-160", "API-166"],
    "qa_func": ["Recommendation respects BR-012"],
    "qa_api": ["API-166"],
    "qa_ui": ["UI-041 convert to transfer"],
  },
  {
    "id": "F-10",
    "name": "Order Availability & Reservation",
    "file": "F-10-Order-Availability-Reservation.md",
    "overview": "Confirm ATP, reserve stock for confirmed orders, release on cancel, and support multi-location plans.",
    "goal": "Prevent overselling and double-allocation (BO-06).",
    "stories": ["US-041", "US-042", "US-043", "US-048"],
    "ac": ["AC-041 availability", "AC-042 reserve", "AC-043 release", "AC-048 multi-location P2"],
    "prev": ["F-04", "F-01", "F-27"],
    "module": "M-07 Order Fulfillment + M-04 reservations",
    "schema": "fulfillment + inventory",
    "tables": [
      ("fulfillment.customer_orders / customer_order_lines", "Orders"),
      ("fulfillment.inventory_reservations", "Reservations"),
    ],
    "rels": ["reservation → order line + stock position identity"],
    "constraints": ["reserved <= available; optimistic locking on stock_positions"],
    "migrations": ["V1_60__fulfillment_orders.sql", "V1_61__inventory_reservations.sql"],
    "entities": ["CustomerOrderFulfillment (AR)", "InventoryReservation"],
    "vos": ["OrderLine", "ReservationId", "AtpSnapshot"],
    "repos": ["CustomerOrderRepository", "ReservationRepository"],
    "dtos_req": ["CreateOrderRequest", "ConfirmAvailabilityRequest", "ConfirmOrderRequest", "CancelOrderRequest", "MultiLocationPlanRequest", "CreateReservationRequest", "ReleaseReservationRequest"],
    "dtos_res": ["OrderResponse", "AvailabilityCheckResponse", "ReservationResponse", "MultiLocationPlanResponse"],
    "validation": ["product eligibility", "ATP sufficient BR-001", "inactive product blocked"],
    "services": ["OrderAvailabilityService", "ReservationSagaService"],
    "controllers": ["FulfillmentOrderController", "ReservationController"],
    "exceptions": ["InsufficientAtpException", "ReservationConflictException", "OrderStateException"],
    "security": ["ORDER_RESERVE", "ORDER_VIEW", "location-scoped"],
    "routes": ["fulfillment/reservations", "fulfillment/split-planner", "inventory/availability"],
    "pages": ["OrderReservationWorkbenchPage (UI-030)", "MultiLocationSplitPlannerPage (UI-035)", "AvailabilityInquiryPage"],
    "components": ["AvailabilityResultPanel", "ReservationLines", "SplitPlanEditor"],
    "fe_models": ["OrderVm", "ReservationVm", "AtpVm"],
    "fe_services": ["FulfillmentApiService", "ReservationFacade"],
    "forms": ["AvailabilityCheckForm", "ConfirmOrderForm"],
    "fe_validation": ["order lines qty > 0"],
    "state": ["order draft, ATP results, reservation ids"],
    "apis": ["API-081, 084–087", "API-043/044", "API-036", "API-139"],
    "qa_func": ["confirm reduces ATP; cancel restores"],
    "qa_api": ["API-081–087, 043–044"],
    "qa_ui": ["UI-030 concurrent reservation conflict"],
  },
  {
    "id": "F-11",
    "name": "Pick, Pack & Ship Fulfillment",
    "file": "F-11-Pick-Pack-Ship-Fulfillment.md",
    "overview": "Assign pick work, verify picks, pack, and ship with inventory deduction at shipment confirmation.",
    "goal": "Execute physical fulfillment with inventory matching goods dispatched (BO-03, BO-06).",
    "stories": ["US-044", "US-049"],
    "ac": ["AC-044 pick/pack/ship", "AC-049 status visibility"],
    "prev": ["F-10", "F-27"],
    "module": "M-07 Order Fulfillment",
    "schema": "fulfillment + inventory lots",
    "tables": [
      ("fulfillment.fulfillment_executions", "Pick/pack state"),
      ("fulfillment.fulfillment_pick_lines", "Pick lines"),
      ("fulfillment.shipments / shipment_lines", "Shipments"),
    ],
    "rels": ["execution → order; shipment → execution"],
    "constraints": ["ship only after pack; lot required if traceable"],
    "migrations": ["V1_62__fulfillment_execution_shipments.sql"],
    "entities": ["CustomerOrderFulfillment", "FulfillmentExecution", "Shipment"],
    "vos": ["PickLine", "ShipmentReference", "LotIdentity"],
    "repos": ["FulfillmentExecutionRepository", "ShipmentRepository"],
    "dtos_req": ["CreatePickListRequest", "VerifyPickRequest", "PackOrderRequest", "CreateShipmentRequest"],
    "dtos_res": ["PickListResponse", "AwaitingPickResponse", "ShipmentResponse", "OrderStatusResponse"],
    "validation": ["pick qty <= reserved", "location not frozen"],
    "services": ["PickPackShipService", "OrderStatusQueryService"],
    "controllers": ["FulfillmentExecutionController"],
    "exceptions": ["PickVerificationFailedException", "LocationFrozenException", "ShipmentNotAllowedException"],
    "security": ["FULFILL_PICK", "FULFILL_SHIP"],
    "routes": ["fulfillment/pick-pack-ship", "fulfillment/order-status"],
    "pages": ["PickPackShipWorkbenchPage (UI-031)", "OrderFulfillmentStatusPage (UI-034)"],
    "components": ["PickQueue", "PickVerifyScanner", "PackPanel", "ShipConfirm"],
    "fe_models": ["PickListVm", "ShipmentVm", "OrderStatusVm"],
    "fe_services": ["FulfillmentExecutionApiService", "PickPackShipFacade"],
    "forms": ["PickVerifyForm", "ShipForm"],
    "fe_validation": ["scanned sku matches", "qty match"],
    "state": ["queue, active pick, ship draft"],
    "apis": ["API-088–092", "API-082/083/097", "API-041 lots", "API-177", "Gap C-01 location pick queue"],
    "qa_func": ["on-hand decreases only on ship"],
    "qa_api": ["API-088–092, 097"],
    "qa_ui": ["UI-031/034 full flow"],
  },
  {
    "id": "F-12",
    "name": "Partial Fulfillment & Backorder Management",
    "file": "F-12-Partial-Fulfillment-Backorder.md",
    "overview": "Partial ship available qty, create acknowledged backorders, and prioritize fulfillment when stock arrives.",
    "goal": "Maximize fill rate under shortage without silent short-ships (BO-06).",
    "stories": ["US-045", "US-046"],
    "ac": ["AC-045 partial ship MVP", "AC-046 backorder priority P2"],
    "prev": ["F-10", "F-11"],
    "module": "M-07 Order Fulfillment",
    "schema": "fulfillment",
    "tables": [("fulfillment.backorders", "Backorder queue")],
    "rels": ["backorder → order line"],
    "constraints": ["backorder qty > 0; customer ack flag for partial"],
    "migrations": ["V1_63__backorders.sql"],
    "entities": ["Backorder", "CustomerOrderFulfillment"],
    "vos": ["BackorderPriority", "PartialFulfillmentPlan"],
    "repos": ["BackorderRepository"],
    "dtos_req": ["PartialFulfillmentRequest", "CreateBackorderRequest", "FulfillBackorderRequest"],
    "dtos_res": ["PartialFulfillmentResponse", "BackorderResponse", "BackorderBoardResponse"],
    "validation": ["partial requires ack", "priority sequencing"],
    "services": ["PartialFulfillmentService", "BackorderService"],
    "controllers": ["BackorderController"],
    "exceptions": ["PartialWithoutAckException", "BackorderNotFulfillableException"],
    "security": ["BACKORDER_MANAGE", "ORDER_FULFILL"],
    "routes": ["fulfillment/partial-backorders"],
    "pages": ["PartialFulfillmentBackorderPage (UI-032)"],
    "components": ["PartialShipWizard", "BackorderQueue", "PriorityEditor"],
    "fe_models": ["BackorderVm", "PartialPlanVm"],
    "fe_services": ["BackorderApiService", "PartialFulfillmentFacade"],
    "forms": ["PartialFulfillmentForm", "CustomerAckForm"],
    "fe_validation": ["ack required", "ship qty <= available"],
    "state": ["partial draft, backorder list"],
    "apis": ["API-093–095", "API-164"],
    "qa_func": ["partial + backorder created", "auto-reserve when stock arrives P2"],
    "qa_api": ["API-093–095, 164"],
    "qa_ui": ["UI-032"],
  },
  {
    "id": "F-13",
    "name": "Fulfillment Exception Handling",
    "file": "F-13-Fulfillment-Exception-Handling.md",
    "overview": "Resolve pick failures, damage, cancellations, and optional substitutions; raise exception alerts.",
    "goal": "Minimize customer impact and correct inventory when outbound breaks (BO-06).",
    "stories": ["US-047", "US-050", "US-078"],
    "ac": ["AC-047 exceptions P2", "AC-050 substitution P3", "AC-078 alerts"],
    "prev": ["F-11", "F-27"],
    "module": "M-07 + M-04 quarantine + M-13 alerts",
    "schema": "fulfillment + inventory.quarantine_holds + audit.operational_alerts",
    "tables": [("Fulfillment exception fields / table", "Optional fulfillment.exceptions"), ("inventory.quarantine_holds", "Damage holds")],
    "rels": ["exception → order; may create quarantine hold"],
    "constraints": ["reason required; substitution requires approval"],
    "migrations": ["V2_20__fulfillment_exceptions.sql"],
    "entities": ["FulfillmentException", "CustomerOrderFulfillment"],
    "vos": ["ExceptionType", "SubstitutionApproval"],
    "repos": ["FulfillmentExceptionRepository"],
    "dtos_req": ["CreateFulfillmentExceptionRequest", "ResolveExceptionRequest", "SubstitutionRequest"],
    "dtos_res": ["ExceptionResponse", "ExceptionBoardResponse"],
    "validation": ["reason code", "SoD for substitution"],
    "services": ["FulfillmentExceptionService"],
    "controllers": ["FulfillmentExceptionController"],
    "exceptions": ["ExceptionAlreadyResolvedException", "SubstitutionNotAuthorizedException"],
    "security": ["FULFILL_EXCEPTION_MANAGE"],
    "routes": ["fulfillment/exceptions"],
    "pages": ["FulfillmentExceptionManagementPage (UI-033)"],
    "components": ["ExceptionQueue", "ResolveExceptionForm", "SubstitutionPanel"],
    "fe_models": ["FulfillmentExceptionVm"],
    "fe_services": ["ExceptionApiService", "ExceptionFacade"],
    "forms": ["ExceptionForm", "ResolveForm"],
    "fe_validation": ["reason required"],
    "state": ["exception queue"],
    "apis": ["API-096", "API-165", "API-045"],
    "qa_func": ["damage → quarantine", "alert raised"],
    "qa_api": ["API-096, 165"],
    "qa_ui": ["UI-033"],
  },
  {
    "id": "F-14",
    "name": "Cycle Counting",
    "file": "F-14-Cycle-Counting.md",
    "overview": "Schedule, assign, and capture blind cycle counts; feed accuracy metrics.",
    "goal": "Sustain inventory accuracy without full-wall disruption (BO-02).",
    "stories": ["US-030", "US-031", "US-071"],
    "ac": ["AC-030 schedule/assign", "AC-031 blind count", "AC-071 accuracy reporting"],
    "prev": ["F-01", "F-02", "F-04", "F-27"],
    "module": "M-09 Inventory Accuracy",
    "schema": "accuracy",
    "tables": [("accuracy.cycle_counts", "Cycle count headers/results")],
    "rels": ["count references location + sku; expected qty snapshotted"],
    "constraints": ["blind: system qty hidden from counter UI", "counter != approver later"],
    "migrations": ["V1_70__cycle_counts.sql"],
    "entities": ["CycleCount (AR)"],
    "vos": ["CountQuantity", "BlindCountResult", "UserActionAttribution"],
    "repos": ["CycleCountRepository"],
    "dtos_req": ["CreateCycleCountRequest", "SubmitCycleCountResultRequest", "CycleCountSearchQuery"],
    "dtos_res": ["CycleCountResponse", "CountPerformanceResponse"],
    "validation": ["assigned user", "location not conflicting freeze optionally"],
    "services": ["CycleCountService"],
    "controllers": ["CycleCountController"],
    "exceptions": ["CycleCountAlreadySubmittedException", "BlindCountViolationException"],
    "security": ["CYCLE_COUNT_MANAGE", "CYCLE_COUNT_EXECUTE"],
    "routes": ["inventory/cycle-counts", "inventory/cycle-counts/:id"],
    "pages": ["CycleCountWorkbenchPage (UI-023)"],
    "components": ["CountAssignmentList", "BlindCountEntry", "CountSubmitConfirm"],
    "fe_models": ["CycleCountVm"],
    "fe_services": ["CycleCountApiService", "CycleCountFacade"],
    "forms": ["CountResultForm"],
    "fe_validation": ["qty >= 0", "no display of system qty"],
    "state": ["assigned counts, entry draft"],
    "apis": ["API-108–111", "API-168"],
    "qa_func": ["blind enforced", "variance created when mismatch"],
    "qa_api": ["API-108–111"],
    "qa_ui": ["UI-023"],
  },
  {
    "id": "F-15",
    "name": "Full Physical Inventory Count",
    "file": "F-15-Full-Physical-Inventory-Count.md",
    "overview": "Wall-to-wall counts with location freeze, progress, and certification.",
    "goal": "Establish verified baselines and financial substantiation (BO-02, BO-07).",
    "stories": ["US-032"],
    "ac": ["AC-032-* freeze, capture, certify, variance reporting"],
    "prev": ["F-02", "F-04", "F-27"],
    "module": "M-09 Inventory Accuracy",
    "schema": "accuracy + network freeze",
    "tables": [("accuracy.physical_inventory_counts", "Physical count"), ("network.inventory_locations.freeze", "Freeze flag")],
    "rels": ["physical count → location"],
    "constraints": ["freeze blocks receive/ship/transfer/adjust except count posts"],
    "migrations": ["V1_71__physical_inventory_counts.sql"],
    "entities": ["PhysicalInventoryCount (AR)", "InventoryLocation freeze"],
    "vos": ["FreezeStatus", "CertificationRecord"],
    "repos": ["PhysicalCountRepository"],
    "dtos_req": ["CreatePhysicalCountRequest", "SubmitPhysicalCountResultsRequest", "CertifyPhysicalCountRequest"],
    "dtos_res": ["PhysicalCountResponse", "FreezeStatusResponse"],
    "validation": ["all zones complete before certify"],
    "services": ["PhysicalInventoryCountService", "LocationFreezeService"],
    "controllers": ["PhysicalCountController"],
    "exceptions": ["LocationFreezeActiveException", "PhysicalCountIncompleteException"],
    "security": ["PHYSICAL_COUNT_MANAGE", "PHYSICAL_COUNT_CERTIFY"],
    "routes": ["inventory/physical-counts", "inventory/physical-counts/:id"],
    "pages": ["PhysicalInventoryCountPage (UI-024)"],
    "components": ["FreezeBanner", "CountProgress", "CertifyPanel"],
    "fe_models": ["PhysicalCountVm"],
    "fe_services": ["PhysicalCountApiService", "PhysicalCountFacade"],
    "forms": ["PhysicalCountResultForm", "CertifyForm"],
    "fe_validation": ["completion checklist"],
    "state": ["active count, freeze flag"],
    "apis": ["API-020", "API-112–115", "API-168"],
    "qa_func": ["transactions blocked while frozen"],
    "qa_api": ["API-112–115, 020"],
    "qa_ui": ["UI-024"],
  },
  {
    "id": "F-16",
    "name": "Count Variance Investigation & Approval",
    "file": "F-16-Count-Variance-Investigation-Approval.md",
    "overview": "Investigate count variances and approve/reject adjustments with SoD and thresholds.",
    "goal": "Correct balances only through independent approval (BO-02, BO-19).",
    "stories": ["US-033", "US-034", "US-037"],
    "ac": ["AC-033 identify", "AC-034 investigate/approve", "AC-037 threshold routing"],
    "prev": ["F-14|F-15", "F-03", "F-28", "F-27"],
    "module": "M-09 Inventory Accuracy",
    "schema": "accuracy",
    "tables": [("accuracy.count_variances", "Variance lines"), ("accuracy adjustment case tables", "Investigation case")],
    "rels": ["variance → count; case → variances"],
    "constraints": ["counter cannot approve own count BR-019", "threshold → elevated approver"],
    "migrations": ["V1_72__count_variances_adjustment_cases.sql"],
    "entities": ["InventoryAdjustmentCase (AR)", "CountVariance"],
    "vos": ["VarianceQuantity", "InvestigationFinding", "ApprovalDecision"],
    "repos": ["AdjustmentCaseRepository", "VarianceRepository"],
    "dtos_req": ["CreateAdjustmentCaseRequest", "InvestigateCaseRequest", "ApproveVarianceRequest"],
    "dtos_res": ["AdjustmentCaseResponse", "PendingApprovalsResponse"],
    "validation": ["SoD API-031", "approval thresholds API-029"],
    "services": ["VarianceInvestigationService", "ApprovalRoutingService"],
    "controllers": ["AdjustmentCaseController"],
    "exceptions": ["SoDViolationException", "ApprovalThresholdNotMetException"],
    "security": ["VARIANCE_INVESTIGATE", "VARIANCE_APPROVE"],
    "routes": ["inventory/variances", "inventory/variances/:caseId"],
    "pages": ["VarianceInvestigationApprovalPage (UI-025)"],
    "components": ["VarianceTable", "InvestigationForm", "ApprovalActions"],
    "fe_models": ["VarianceCaseVm"],
    "fe_services": ["VarianceApiService", "VarianceFacade"],
    "forms": ["InvestigationForm", "ApprovalForm"],
    "fe_validation": ["findings required before approve"],
    "state": ["pending approvals queue"],
    "apis": ["API-116–119", "API-123", "API-029", "API-031"],
    "qa_func": ["self-approval blocked", "threshold routes to OD/Finance"],
    "qa_api": ["API-116–119, 123"],
    "qa_ui": ["UI-025"],
  },
  {
    "id": "F-17",
    "name": "Stock Adjustments & Write-Offs",
    "file": "F-17-Stock-Adjustments-Write-Offs.md",
    "overview": "Reason-coded stock adjustments and write-offs with approval workflow and audit trail.",
    "goal": "Correct inventory with accountability for damage, shrinkage, obsolescence, and data errors (BO-02, BO-19).",
    "stories": ["US-011", "US-035", "US-036", "US-077"],
    "ac": ["AC-011 reason codes", "AC-035 adjustments", "AC-036 write-offs", "AC-077 approval notifications"],
    "prev": ["F-03", "F-04", "F-28", "F-27"],
    "module": "M-09 + M-03",
    "schema": "accuracy + governance",
    "tables": [
      ("accuracy.stock_adjustments", "Adjustments"),
      ("accuracy.inventory_write_offs", "Write-offs"),
      ("governance.reason_codes", "Required codes"),
    ],
    "rels": ["adjustment case → stock position identity; reason_code FK"],
    "constraints": ["reason required BR-020", "approval status chk", "qty rules"],
    "migrations": ["V1_73__stock_adjustments_write_offs.sql"],
    "entities": ["InventoryAdjustmentCase", "StockAdjustment", "InventoryWriteOff"],
    "vos": ["ReasonCode", "ApprovalThreshold", "EvidenceReference"],
    "repos": ["StockAdjustmentRepository", "WriteOffRepository"],
    "dtos_req": ["SubmitAdjustmentRequest", "ApproveAdjustmentRequest", "RejectAdjustmentRequest", "CreateReasonCodeRequest"],
    "dtos_res": ["AdjustmentCaseResponse", "WriteOffResponse", "CommandResultResponse"],
    "validation": ["active reason code", "threshold", "SoD"],
    "services": ["StockAdjustmentService", "WriteOffService"],
    "controllers": ["AdjustmentController", "ReasonCodeController"],
    "exceptions": ["ReasonCodeRequiredException", "WriteOffNotAuthorizedException"],
    "security": ["ADJUST_SUBMIT", "ADJUST_APPROVE", "WRITE_OFF_AUTHORIZE"],
    "routes": ["inventory/adjustments", "inventory/write-offs", "governance/policies"],
    "pages": ["StockAdjustmentPage (UI-026)", "WriteOffAuthorizationPage (UI-027)", "GovernancePoliciesPage (UI-010)"],
    "components": ["AdjustmentForm", "ReasonCodeSelect", "EvidenceUpload", "ApprovalPanel"],
    "fe_models": ["AdjustmentVm", "WriteOffVm"],
    "fe_services": ["AdjustmentApiService", "AdjustmentFacade"],
    "forms": ["AdjustmentForm", "WriteOffForm"],
    "fe_validation": ["reason required", "qty != 0"],
    "state": ["draft adjustment, pending approvals"],
    "apis": ["API-022–025", "API-029", "API-116/117", "API-120–122"],
    "qa_func": ["adjust updates stock + movement", "write-off finance ack"],
    "qa_api": ["API-120–122"],
    "qa_ui": ["UI-026/027"],
  },
  {
    "id": "F-18",
    "name": "Quarantine & Hold Stock Management",
    "file": "F-18-Quarantine-Hold-Stock.md",
    "overview": "Apply and release quarantine/hold so non-sellable qty is excluded from ATP.",
    "goal": "Prevent shipping defective or uninspected goods (BO-06).",
    "stories": ["US-038"],
    "ac": ["AC-038-* apply/release hold; ATP exclusion; register visibility"],
    "prev": ["F-04", "F-27"],
    "module": "M-04 Inventory Balance",
    "schema": "inventory",
    "tables": [("inventory.quarantine_holds", "Holds")],
    "rels": ["hold → stock_position"],
    "constraints": ["chk_domain_hold_type; qty <= on_hand - reserved"],
    "migrations": ["Already in V1_31; add indexes for register queries"],
    "entities": ["StockPosition", "QuarantineHold"],
    "vos": ["HoldReasonClassification", "HoldType"],
    "repos": ["QuarantineHoldRepository"],
    "dtos_req": ["ApplyQuarantineHoldRequest", "ReleaseQuarantineHoldRequest"],
    "dtos_res": ["QuarantineHoldResponse", "QuarantineRegisterResponse"],
    "validation": ["reason/type required", "qty available"],
    "services": ["QuarantineHoldService"],
    "controllers": ["QuarantineController", "IntelligenceQuarantineController"],
    "exceptions": ["InsufficientQtyForHoldException", "HoldNotFoundException"],
    "security": ["QUARANTINE_MANAGE"],
    "routes": ["inventory/quarantine"],
    "pages": ["QuarantineHoldRegisterPage (UI-028)"],
    "components": ["HoldForm", "QuarantineRegisterTable", "ReleaseAction"],
    "fe_models": ["QuarantineHoldVm"],
    "fe_services": ["QuarantineApiService", "QuarantineFacade"],
    "forms": ["ApplyHoldForm", "ReleaseHoldForm"],
    "fe_validation": ["qty > 0", "reason required"],
    "state": ["register filters"],
    "apis": ["API-045", "API-046", "API-154"],
    "qa_func": ["ATP drops on hold; restores on release"],
    "qa_api": ["API-045/046/154"],
    "qa_ui": ["UI-028"],
  },
  {
    "id": "F-19",
    "name": "Shrinkage & Obsolescence Analysis",
    "file": "F-19-Shrinkage-Obsolescence-Analysis.md",
    "overview": "Analyze reason-coded loss trends and identify slow-moving/obsolete stock.",
    "goal": "Drive loss prevention and working-capital recovery (BO-02).",
    "stories": ["US-039", "US-040"],
    "ac": ["AC-039 shrinkage P2", "AC-040 obsolescence P3"],
    "prev": ["F-17", "F-04"],
    "module": "M-13 Inventory Intelligence",
    "schema": "read accuracy + audit + inventory",
    "tables": [("Read: stock_adjustments, write_offs, movements, stock_positions", "")],
    "rels": ["Aggregation by reason_code, location, sku"],
    "constraints": ["Read-only; no mutations"],
    "migrations": ["Optional materialized view V2_30__shrinkage_mv.sql"],
    "entities": ["None (query)"],
    "vos": ["ShrinkageMetric", "ObsolescenceCandidate"],
    "repos": ["ShrinkageQueryRepository"],
    "dtos_req": ["ShrinkageAnalysisQuery", "DateRangeQuery"],
    "dtos_res": ["ShrinkageAnalysisResponse"],
    "validation": ["date range VR-062"],
    "services": ["ShrinkageAnalysisService"],
    "controllers": ["AccuracyIntelligenceController"],
    "exceptions": ["InvalidDateRangeException"],
    "security": ["SHRINKAGE_VIEW"],
    "routes": ["inventory/shrinkage-obsolescence"],
    "pages": ["ShrinkageLossObsolescencePage (UI-029)"],
    "components": ["ShrinkageChart", "ReasonBreakdownTable", "ObsoleteStockList"],
    "fe_models": ["ShrinkageVm"],
    "fe_services": ["ShrinkageApiService", "ShrinkageFacade"],
    "forms": ["AnalysisFilterForm"],
    "fe_validation": ["start <= end"],
    "state": ["filters, chart data"],
    "apis": ["API-167"],
    "qa_func": ["totals match adjustments by reason"],
    "qa_api": ["API-167"],
    "qa_ui": ["UI-029"],
  },
  {
    "id": "F-20",
    "name": "Low-Stock Alerting & Replenishment",
    "file": "F-20-Low-Stock-Alerting-Replenishment.md",
    "overview": "Generate low/out-of-stock alerts, acknowledge them, suggest replenishment (transfer-before-buy), and manage purchase requisitions.",
    "goal": "Move purchasing from crisis response to threshold-driven discipline (BO-05).",
    "stories": ["US-051", "US-052", "US-053", "US-054", "US-074"],
    "ac": ["AC-051–053 MVP alerts/suggestions", "AC-054 requisitions P2", "AC-074 reporting"],
    "prev": ["F-03", "F-04", "F-27"],
    "module": "M-13 alerts + M-05 requisitions",
    "schema": "audit.operational_alerts + procurement.purchase_requisitions*",
    "tables": [
      ("audit.operational_alerts", "Alerts"),
      ("procurement.purchase_requisitions (+ lines)", "Requisitions"),
    ],
    "rels": ["alert may link sku/location; requisition from recommendation"],
    "constraints": ["acknowledge requires user; network check before approve requisition BR-011"],
    "migrations": ["V1_80__operational_alerts.sql", "V2_12__purchase_requisitions.sql"],
    "entities": ["OperationalAlert", "PurchaseRequisition (AR)"],
    "vos": ["AlertType", "ReplenishmentRecommendation", "RequisitionLine"],
    "repos": ["OperationalAlertRepository", "PurchaseRequisitionRepository"],
    "dtos_req": ["AcknowledgeAlertRequest", "CreateRequisitionRequest", "ApproveRequisitionRequest", "RejectRequisitionRequest", "ConvertRequisitionToPoRequest"],
    "dtos_res": ["AlertResponse", "ReplenishmentRecommendationResponse", "RequisitionResponse"],
    "validation": ["threshold breach detection", "network availability before buy"],
    "services": ["StockAlertService", "ReplenishmentRecommendationService", "PurchaseRequisitionService"],
    "controllers": ["AlertController", "RequisitionController", "ReplenishmentIntelligenceController"],
    "exceptions": ["AlertAlreadyAcknowledgedException", "RequisitionNetworkCheckFailedException"],
    "security": ["ALERT_REVIEW", "REQUISITION_MANAGE", "REQUISITION_APPROVE"],
    "routes": ["procurement/low-stock-alerts", "procurement/replenishment-planning", "procurement/requisitions"],
    "pages": ["LowStockAlertReviewPage (UI-036)", "ReplenishmentPlanningPage (UI-037)", "PurchaseRequisitionPage (UI-013)"],
    "components": ["AlertQueue", "AckDialog", "RecommendationCard", "RequisitionForm"],
    "fe_models": ["AlertVm", "RecommendationVm", "RequisitionVm"],
    "fe_services": ["AlertApiService", "RequisitionApiService", "ReplenishmentFacade"],
    "forms": ["AckForm", "RequisitionForm"],
    "fe_validation": ["ack rationale when dismiss"],
    "state": ["alert list, recommendations, requisition draft"],
    "apis": ["API-037/039", "API-158–160", "API-054–058", "API-166", "Gap C-03 list"],
    "qa_func": ["crossing reorder creates alert", "transfer suggested before PO"],
    "qa_api": ["API-158–160, 054–058"],
    "qa_ui": ["UI-036/037/013"],
  },
  {
    "id": "F-21",
    "name": "Returns Management",
    "file": "F-21-Returns-Management.md",
    "overview": "Return authorization, receive/inspect returned goods, and disposition to restock, quarantine, or write-off.",
    "goal": "Track returns accurately without contaminating sellable stock (BO-06, BR-26).",
    "stories": ["US-064", "US-065", "US-066", "US-067"],
    "ac": ["AC-064–067 full returns Phase 2"],
    "prev": ["F-10", "F-11", "F-05", "F-27"],
    "module": "M-10 Returns Management",
    "schema": "returns",
    "tables": [
      ("returns.return_authorizations (+ lines)", "RA"),
      ("returns.customer_returns (+ lines)", "Physical return"),
      ("returns.return_dispositions", "Disposition"),
    ],
    "rels": ["RA → original order; return → RA; disposition → return"],
    "constraints": ["chk_domain_disposition_decision; eligibility vs original order"],
    "migrations": ["V2_40__returns_schema.sql"],
    "entities": ["CustomerReturnCase (AR)", "ReturnAuthorization", "ReturnDisposition"],
    "vos": ["ReturnEligibility", "InspectionResult", "DispositionDecision"],
    "repos": ["ReturnAuthorizationRepository", "CustomerReturnRepository"],
    "dtos_req": ["CreateReturnAuthorizationRequest", "CancelReturnAuthorizationRequest", "ReceiveReturnRequest", "InspectReturnRequest", "DispositionReturnRequest"],
    "dtos_res": ["ReturnAuthorizationResponse", "ReturnResponse", "PendingReturnReceiptResponse"],
    "validation": ["order linkage", "qty <= shipped", "inspection before disposition"],
    "services": ["ReturnAuthorizationService", "ReturnInspectionService"],
    "controllers": ["ReturnsController"],
    "exceptions": ["ReturnNotEligibleException", "DispositionInvalidException"],
    "security": ["RETURN_AUTHORIZE", "RETURN_RECEIVE", "RETURN_DISPOSITION"],
    "routes": ["returns/authorizations", "returns/inspection-disposition"],
    "pages": ["ReturnAuthorizationPage (UI-042)", "ReturnInspectionDispositionPage (UI-043)"],
    "components": ["RaForm", "PendingReturnsQueue", "InspectionForm", "DispositionActions"],
    "fe_models": ["ReturnAuthorizationVm", "ReturnVm"],
    "fe_services": ["ReturnsApiService", "ReturnsFacade"],
    "forms": ["RaForm", "InspectForm", "DispositionForm"],
    "fe_validation": ["order required", "disposition reason"],
    "state": ["RA list, pending receipts"],
    "apis": ["API-124–131", "API-076 alternate; prefer API-128 C-04"],
    "qa_func": ["restock increases ATP; write-off path"],
    "qa_api": ["API-124–131"],
    "qa_ui": ["UI-042/043"],
  },
  {
    "id": "F-22",
    "name": "Inventory Reporting & Dashboards",
    "file": "F-22-Inventory-Reporting-Dashboards.md",
    "overview": "Operational dashboard and reports for stock health, movements, stockouts, accuracy, and location performance.",
    "goal": "Give leaders inventory visibility without manual compilation (BO-01, BO-04).",
    "stories": ["US-068", "US-069", "US-070", "US-072", "US-074"],
    "ac": ["AC-068–070 MVP reports", "AC-072 location P2", "AC-074 replenishment reporting"],
    "prev": ["F-04"],
    "module": "M-13 Inventory Intelligence",
    "schema": "read models over operational + audit",
    "tables": [("Projections / optional reporting views", "")],
    "rels": ["Read-only joins across modules by identity"],
    "constraints": ["Location-scope filtering on all queries"],
    "migrations": ["V1_90__intelligence_views.sql (optional)"],
    "entities": ["None (query services)"],
    "vos": ["DashboardKpi", "MovementReportRow", "StockoutRow"],
    "repos": ["DashboardQueryRepository", "MovementQueryRepository"],
    "dtos_req": ["ReportFilterQuery", "DateRangeQuery"],
    "dtos_res": ["DashboardResponse", "StockStatusSummaryResponse", "MovementReportResponse", "CountPerformanceResponse"],
    "validation": ["date range", "authorized locations"],
    "services": ["DashboardService", "OperationalReportService"],
    "controllers": ["IntelligenceDashboardController", "IntelligenceReportController"],
    "exceptions": ["UnauthorizedReportScopeException"],
    "security": ["REPORT_VIEW", "DASHBOARD_VIEW"],
    "routes": ["home/operations", "reports/operational"],
    "pages": ["OperationalDashboardPage (UI-002)", "OperationalReportsPage (UI-044)"],
    "components": ["KpiSummaryCard", "StockHealthPanel", "ReportFilterBar", "ExportButton"],
    "fe_models": ["DashboardVm", "ReportRowVm"],
    "fe_services": ["DashboardApiService", "ReportsFacade"],
    "forms": ["ReportFilterForm"],
    "fe_validation": ["date range"],
    "state": ["dashboard widgets, report results"],
    "apis": ["API-150–152", "API-154–155", "API-167–168"],
    "qa_func": ["KPI cards match underlying APIs", "export"],
    "qa_api": ["API-150–152, 155"],
    "qa_ui": ["UI-002/044"],
  },
  {
    "id": "F-23",
    "name": "Inventory Performance KPIs",
    "file": "F-23-Inventory-Performance-KPIs.md",
    "overview": "Executive KPI dashboard for fill rate, turnover, days of supply, accuracy vs targets.",
    "goal": "Track strategic inventory maturity (BO-18).",
    "stories": ["US-073"],
    "ac": ["AC-073-* KPI calc, trends, targets"],
    "prev": ["F-11", "F-04", "F-14", "F-22"],
    "module": "M-13",
    "schema": "aggregations / snapshots",
    "tables": [("Optional audit/reporting KPI snapshot tables", "")],
    "rels": ["Derived from fulfillment, inventory, accuracy"],
    "constraints": ["Read-only"],
    "migrations": ["V3_10__kpi_snapshots.sql"],
    "entities": ["None"],
    "vos": ["KpiValue", "KpiTarget", "TrendPoint"],
    "repos": ["KpiQueryRepository"],
    "dtos_req": ["KpiQuery"],
    "dtos_res": ["KpiDashboardResponse"],
    "validation": ["period required"],
    "services": ["KpiService"],
    "controllers": ["KpiController"],
    "exceptions": ["KpiDataUnavailableException"],
    "security": ["KPI_VIEW_EXEC"],
    "routes": ["reports/executive-kpis"],
    "pages": ["ExecutiveKpiDashboardPage (UI-003)"],
    "components": ["KpiTrendChart", "TargetComparison", "DrilldownLink"],
    "fe_models": ["KpiVm"],
    "fe_services": ["KpiApiService", "KpiFacade"],
    "forms": ["KpiPeriodForm"],
    "fe_validation": ["period"],
    "state": ["selected period, kpi set"],
    "apis": ["API-170"],
    "qa_func": ["fill rate matches shipped/ordered"],
    "qa_api": ["API-170"],
    "qa_ui": ["UI-003"],
  },
  {
    "id": "F-24",
    "name": "Financial Inventory Reconciliation",
    "file": "F-24-Financial-Inventory-Reconciliation.md",
    "overview": "Valuation snapshots, three-way match support, consignment ownership, and period-end reconciliation.",
    "goal": "Align operational inventory with finance needs (BO-07, BO-20).",
    "stories": ["US-075", "US-089"],
    "ac": ["AC-075 valuation", "AC-089 reconciliation"],
    "prev": ["F-05", "F-07", "F-17", "F-29"],
    "module": "M-06 finance slice + M-13 valuation",
    "schema": "finance + audit valuation",
    "tables": [
      ("finance.supplier_invoices (+ lines, match)", "3-way match"),
      ("audit.inventory_valuation_snapshots / lines", "Valuation"),
    ],
    "rels": ["invoice ↔ PO ↔ goods receipt match"],
    "constraints": ["match status; payment auth after match"],
    "migrations": ["V3_20__finance_invoices.sql", "V3_21__valuation_snapshots.sql"],
    "entities": ["SupplierInvoice (AR)", "ValuationSnapshot"],
    "vos": ["MonetaryAmount", "MatchResult", "OwnershipClassification"],
    "repos": ["SupplierInvoiceRepository", "ValuationSnapshotRepository"],
    "dtos_req": ["RegisterSupplierInvoiceRequest", "ThreeWayMatchRequest", "AuthorizePaymentRequest", "ConsignmentOwnershipRequest"],
    "dtos_res": ["SupplierInvoiceResponse", "ValuationSnapshotResponse", "ReconciliationResponse"],
    "validation": ["PO+GR+invoice quantities", "currency"],
    "services": ["ThreeWayMatchService", "ValuationService", "ReconciliationService"],
    "controllers": ["SupplierInvoiceController", "ValuationIntelligenceController"],
    "exceptions": ["ThreeWayMatchFailedException", "PaymentNotAuthorizedException"],
    "security": ["FINANCE_INVOICE", "VALUATION_VIEW", "RECONCILE"],
    "routes": ["reports/valuation-reconciliation"],
    "pages": ["InventoryValuationReconciliationPage (UI-045)"],
    "components": ["MatchPanel", "ValuationTable", "VarianceList"],
    "fe_models": ["InvoiceVm", "ValuationVm", "ReconciliationVm"],
    "fe_services": ["FinanceApiService", "ValuationFacade"],
    "forms": ["InvoiceForm", "ReconciliationSignoffForm"],
    "fe_validation": ["invoice totals"],
    "state": ["period, match results"],
    "apis": ["API-077–080", "API-047", "API-171–172"],
    "qa_func": ["match success/fail paths", "snapshot period close"],
    "qa_api": ["API-077–080, 171–172"],
    "qa_ui": ["UI-045"],
  },
  {
    "id": "F-25",
    "name": "Promotional & Launch Stock Readiness",
    "file": "F-25-Promotional-Launch-Stock-Readiness.md",
    "overview": "Allocate and ring-fence promotional stock; assess campaign readiness.",
    "goal": "Ensure campaign/launch coverage without draining general ATP (deferred Phase 3).",
    "stories": ["US-057", "US-080"],
    "ac": ["AC-057 readiness", "AC-080 campaign alerts"],
    "prev": ["F-04", "F-10", "F-27"],
    "module": "M-11 Commercial Campaign",
    "schema": "commercial",
    "tables": [
      ("commercial.promotional_stock_allocations", "Allocations"),
      ("commercial.promotional_allocation_locations", "Per-location ring-fence"),
    ],
    "rels": ["allocation → sku; locations child; may call stock segregation"],
    "constraints": ["ring-fence qty <= ATP; override auditable"],
    "migrations": ["V3_30__commercial_allocations.sql"],
    "entities": ["PromotionalStockAllocation (AR)"],
    "vos": ["CampaignId", "RingFenceQuantity", "ReadinessStatus"],
    "repos": ["PromotionalAllocationRepository"],
    "dtos_req": ["CreateAllocationRequest", "UpdateAllocationRequest", "ReadinessCheckRequest", "ReleaseAllocationRequest", "OverrideAllocationRequest"],
    "dtos_res": ["AllocationResponse", "ReadinessResponse", "RingFenceResponse"],
    "validation": ["targets", "override authority"],
    "services": ["CampaignAllocationService", "ReadinessService"],
    "controllers": ["CampaignController"],
    "exceptions": ["InsufficientAtpForRingFenceException", "OverrideNotAuthorizedException"],
    "security": ["CAMPAIGN_MANAGE", "CAMPAIGN_OVERRIDE"],
    "routes": ["reports/promotional-readiness"],
    "pages": ["PromotionalStockReadinessPage (UI-046)"],
    "components": ["AllocationForm", "ReadinessGauge", "RingFenceTable"],
    "fe_models": ["AllocationVm", "ReadinessVm"],
    "fe_services": ["CampaignApiService", "CampaignFacade"],
    "forms": ["AllocationForm", "OverrideForm"],
    "fe_validation": ["target qty > 0"],
    "state": ["allocations, readiness"],
    "apis": ["API-132–139", "API-048", "API-169", "API-178"],
    "qa_func": ["ring-fence reduces general ATP"],
    "qa_api": ["API-132–139, 169"],
    "qa_ui": ["UI-046"],
  },
  {
    "id": "F-26",
    "name": "Operational Notifications & Alerts",
    "file": "F-26-Operational-Notifications-Alerts.md",
    "overview": "Central notification center for stock, approval, transfer/fulfillment exceptions, inbound delays, and campaign alerts.",
    "goal": "Reduce decision latency by delivering actionable alerts to the right roles (BO-05, BO-06).",
    "stories": ["US-076", "US-077", "US-078", "US-079", "US-080"],
    "ac": ["AC-076/077 MVP", "AC-078/079 P2", "AC-080 deferred"],
    "prev": ["F-27"],
    "module": "M-13 + producers",
    "schema": "audit.operational_alerts",
    "tables": [("audit.operational_alerts", "Unified alert store")],
    "rels": ["alert references entity ids by type"],
    "constraints": ["acknowledge user/timestamp; unread counts"],
    "migrations": ["V1_80__operational_alerts.sql (shared with F-20)"],
    "entities": ["OperationalAlert"],
    "vos": ["AlertSeverity", "AlertChannel", "Acknowledgement"],
    "repos": ["OperationalAlertRepository"],
    "dtos_req": ["AcknowledgeAlertRequest", "AlertSearchQuery"],
    "dtos_res": ["AlertResponse", "AlertCountResponse"],
    "validation": ["ack only owner/role"],
    "services": ["NotificationService", "AlertDeliveryService"],
    "controllers": ["AlertController"],
    "exceptions": ["AlertNotFoundException", "AlertAckForbiddenException"],
    "security": ["ALERT_VIEW", "role-filtered feed"],
    "routes": ["notifications"],
    "pages": ["NotificationCenterPage (UI-004)"],
    "components": ["NotificationIconInboxTrigger", "AlertList", "AckButton", "DeepLinkAction"],
    "fe_models": ["AlertVm", "AlertCountVm"],
    "fe_services": ["NotificationApiService", "NotificationFacade (core)"],
    "forms": ["AckForm"],
    "fe_validation": ["optional rationale"],
    "state": ["core unread count signal; notification list"],
    "apis": ["API-158/159", "queues API-106/123/163/169"],
    "qa_func": ["role sees only relevant alerts", "ack clears unread"],
    "qa_api": ["API-158/159"],
    "qa_ui": ["UI-004 + header badge"],
  },
  {
    "id": "F-27",
    "name": "User Access & Role Management",
    "file": "F-27-User-Access-Role-Management.md",
    "overview": "Authenticate sessions, provision users, assign roles, and enforce location-scoped RBAC.",
    "goal": "Control who can view/transact/approve inventory operations (BO-19, BO-21).",
    "stories": ["US-081", "US-082", "US-085"],
    "ac": ["AC-081 RBAC", "AC-082 location scope", "AC-085 user provisioning"],
    "prev": [],
    "module": "M-12 Identity & Access + Platform auth",
    "schema": "identity",
    "tables": [
      ("identity.user_accounts", "Users"),
      ("identity.role_assignments", "Roles"),
      ("identity.role_assignment_locations", "Location scope"),
    ],
    "rels": ["role_assignments → user; locations → assignment"],
    "constraints": ["uk username/email; soft suspend/deactivate"],
    "migrations": ["V1_00__identity_schema.sql", "V1_01__user_accounts_roles.sql"],
    "entities": ["UserAccount (AR)", "RoleAssignment"],
    "vos": ["UserId", "RoleCode", "LocationScope"],
    "repos": ["UserAccountRepository", "RoleAssignmentRepository"],
    "dtos_req": ["CreateUserRequest", "AssignRoleRequest", "SuspendUserRequest", "DeactivateUserRequest", "SyncUsersRequest"],
    "dtos_res": ["UserResponse", "SessionResponse", "RoleAssignmentResponse", "CommandResultResponse"],
    "validation": ["unique username", "valid role codes UR-01–UR-19"],
    "services": ["UserAdminService", "SessionService", "AuthorizationService"],
    "controllers": ["UserController", "AuthController", "AuthorizationController"],
    "exceptions": ["InvalidCredentialsException", "UserSuspendedException", "RoleAssignmentConflictException"],
    "security": ["OAuth2/OIDC JWT", "ADMIN_USERS", "public only login"],
    "routes": ["auth/sign-in", "admin/users", "admin/roles-access"],
    "pages": ["SignInPage (UI-001)", "UserAccountManagementPage (UI-049)", "RoleAccessControlPage (UI-050)"],
    "components": ["SignInForm", "UserTable", "RoleAssignmentMatrix", "LocationScopePicker", "SessionContextBadge"],
    "fe_models": ["UserVm", "SessionVm", "PermissionVm"],
    "fe_services": ["AuthService", "UserApiService", "AuthorizationApiService", "SessionStore"],
    "forms": ["SignInForm", "UserForm", "RoleAssignForm"],
    "fe_validation": ["credentials required", "role/location required on assign"],
    "state": ["core session signals, permission catalog, location scope"],
    "apis": ["API-140–149", "API-173", "API-174"],
    "qa_func": ["login/logout", "suspended blocked", "location scope filters data"],
    "qa_api": ["API-140–149, 173–174"],
    "qa_ui": ["UI-001/049/050", "authGuard/guestGuard"],
  },
  {
    "id": "F-28",
    "name": "Operational Accountability & Controls",
    "file": "F-28-Operational-Accountability-Controls.md",
    "overview": "Enforce segregation of duties and record user activity for material actions.",
    "goal": "Strengthen loss prevention and individual accountability (BO-19).",
    "stories": ["US-083", "US-084"],
    "ac": ["AC-083 activity logging", "AC-084 SoD no self-approval / conflicting roles"],
    "prev": ["F-27"],
    "module": "M-12 + M-03 SoD + audit",
    "schema": "identity + governance + audit",
    "tables": [
      ("audit.audit_trail_records", "Activity/audit"),
      ("governance policies SoD rules", "Evaluated via API-031"),
    ],
    "rels": ["audit references user_id + entity"],
    "constraints": ["initiator != approver for governed actions"],
    "migrations": ["V1_02__audit_trail_records.sql", "SoD seed in governance"],
    "entities": ["AuditTrailRecord", "SoDPolicy evaluation"],
    "vos": ["UserActionAttribution", "SoDEvaluationResult"],
    "repos": ["AuditTrailRepository"],
    "dtos_req": ["EvaluateSoDRequest", "EvaluateActionRequest", "ValidateLocationScopeRequest"],
    "dtos_res": ["SoDEvaluationResponse", "AuthorizationDecisionResponse"],
    "validation": ["action + actor + subject required"],
    "services": ["SegregationOfDutiesService", "ActivityLoggingService", "ActionAuthorizationService"],
    "controllers": ["GovernanceSoDController", "AuthorizationController"],
    "exceptions": ["SoDViolationException", "LocationScopeViolationException"],
    "security": ["Called internally by all approval commands; admin configure roles"],
    "routes": ["admin/roles-access (policy)", "cross-cutting on approval UIs"],
    "pages": ["RoleAccessControlPage (UI-050) config; enforced on UI-025/026/027/039"],
    "components": ["PermissionMatrix", "SoDWarningDialog"],
    "fe_models": ["AuthorizationDecisionVm"],
    "fe_services": ["AuthorizationApiService", "used by all facades before approve"],
    "forms": ["N/A primary; approve actions call evaluate"],
    "fe_validation": ["disable approve if SoD fails"],
    "state": ["permission catalog in core"],
    "apis": ["API-031", "API-148", "API-149"],
    "qa_func": ["counter cannot approve own variance", "conflicting roles blocked"],
    "qa_api": ["API-031/148/149"],
    "qa_ui": ["approval buttons disabled + error"],
  },
  {
    "id": "F-29",
    "name": "Audit Trail & Compliance",
    "file": "F-29-Audit-Trail-Compliance.md",
    "overview": "Immutable movement/audit trail, auditor query/export, and control breach detection.",
    "goal": "Demonstrate 100% traceability for auditors (BO-19).",
    "stories": ["US-086", "US-087", "US-088"],
    "ac": ["AC-086 trail MVP", "AC-087 query P2", "AC-088 breach detection P2"],
    "prev": ["F-28"],
    "module": "M-13 audit projections + movement writer",
    "schema": "audit",
    "tables": [
      ("audit.inventory_movement_records", "Movements"),
      ("audit.audit_trail_records", "Field-level/audit events"),
    ],
    "rels": ["append-only; no update/delete grants for app role"],
    "constraints": ["immutable; chk_domain_movement_type"],
    "migrations": ["V1_03__inventory_movement_records.sql", "V1_02 audit trail", "DB REVOKE UPDATE/DELETE"],
    "entities": ["InventoryMovementRecord", "AuditTrailRecord"],
    "vos": ["MovementType", "AuditQuantitySnapshot", "BeforeAfterValues"],
    "repos": ["MovementRecordRepository", "AuditTrailQueryRepository"],
    "dtos_req": ["AuditTrailQuery", "MovementHistoryQuery", "ExportAuditRequest"],
    "dtos_res": ["AuditTrailResponse", "MovementHistoryResponse", "ExportJobResponse"],
    "validation": ["query filters required for large ranges"],
    "services": ["AuditTrailQueryService", "ControlBreachDetectionService", "MovementAppendService"],
    "controllers": ["AuditIntelligenceController"],
    "exceptions": ["AuditExportTooLargeException"],
    "security": ["AUDIT_VIEW", "AUDIT_EXPORT"],
    "routes": ["reports/audit-workspace", "reports/audit-trail", "inventory/movement-history"],
    "pages": ["AuditControlReviewPage (UI-047)", "AuditTrailQueryPage (UI-048)", "MovementHistoryPage (UI-022)"],
    "components": ["AuditFilter", "BeforeAfterViewer", "ExportDialog", "BreachList"],
    "fe_models": ["AuditEventVm", "MovementVm"],
    "fe_services": ["AuditApiService", "AuditFacade"],
    "forms": ["AuditQueryForm"],
    "fe_validation": ["date range max window"],
    "state": ["query results, export status"],
    "apis": ["API-155", "API-156", "API-157"],
    "qa_func": ["movement appears for every qty change", "no edit API"],
    "qa_api": ["API-155–157"],
    "qa_ui": ["UI-047/048"],
  },
  {
    "id": "F-30",
    "name": "System Go-Live & Initial Data Setup",
    "file": "F-30-System-Go-Live-Initial-Data-Setup.md",
    "overview": "Controlled bulk import of products and opening balances with validation and activation gates.",
    "goal": "Enable practical go-live without embedding bad opening data (BO-01, BO-21).",
    "stories": ["US-090"],
    "ac": ["AC-090-* upload, validate, review errors, approve, activate location"],
    "prev": ["F-01", "F-02", "F-27"],
    "module": "M-01 + M-04 + M-02",
    "schema": "catalog + inventory + network",
    "tables": [
      ("Staging import tables optional", "import_batches / import_errors"),
      ("catalog.products", "Bulk upsert"),
      ("inventory.stock_positions", "Opening balances"),
    ],
    "rels": ["import batch → rows; activation requires approved openings"],
    "constraints": ["opening qty >= 0; SKU must resolve; dual control approve"],
    "migrations": ["V1_95__import_batches.sql"],
    "entities": ["ImportBatch", "Product", "StockPosition opening"],
    "vos": ["ImportRowResult", "OpeningBalance"],
    "repos": ["ImportBatchRepository", "OpeningBalanceRepository"],
    "dtos_req": ["ProductImportRequest (multipart)", "OpeningBalanceRequest", "ActivateLocationRequest"],
    "dtos_res": ["ImportResultResponse", "OpeningBalanceResultResponse", "ActivationResultResponse"],
    "validation": ["file schema", "duplicate SKUs in file", "opening balance substantiation"],
    "services": ["ProductImportService", "OpeningBalanceService", "GoLiveActivationService"],
    "controllers": ["ProductImportController", "OpeningBalanceController"],
    "exceptions": ["ImportValidationException", "OpeningBalanceNotApprovedException"],
    "security": ["DATA_IMPORT", "OPENING_BALANCE_APPROVE", "LOCATION_ACTIVATE"],
    "routes": ["products/import"],
    "pages": ["ProductImportWorkspacePage (UI-006)"],
    "components": ["UploadDropzone", "ValidationErrorTable", "ImportProgress", "ActivationChecklist"],
    "fe_models": ["ImportBatchVm", "ImportErrorVm"],
    "fe_services": ["ImportApiService", "ImportFacade"],
    "forms": ["UploadForm", "ApproveImportForm"],
    "fe_validation": ["file type/size", "confirm approve"],
    "state": ["batch status, errors, approval step"],
    "apis": ["API-010", "API-032", "API-017"],
    "qa_func": ["invalid rows blocked", "activation blocked until openings approved"],
    "qa_api": ["API-010/032/017"],
    "qa_ui": ["UI-006 wizard"],
  },
]


def bullet(items):
    return "\n".join(f"- {i}" for i in items)


def table_rows(pairs):
    lines = ["| Object | Purpose |", "|--------|---------|"]
    for a, b in pairs:
        lines.append(f"| `{a}` | {b} |")
    return "\n".join(lines)


def render(f):
    prev = ", ".join(f"`{p}`" for p in f["prev"]) if f["prev"] else "_None (foundation)_"
    stories = ", ".join(f["stories"])
    return f"""# Implementation Plan — {f['id']}: {f['name']}

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | {f['id']} |
| **Feature Name** | {f['name']} |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | {f['module']} |
| **Required previous features** | {prev} |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

{f['overview']}

{STACK}

---

## 2. Business Goal

{f['goal']}

---

## 3. User Stories

{bullet(f['stories'])}

Primary story references: **{stories}** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

{bullet(f['ac'])}

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

{table_rows(f['tables'])}

### Relationships

{bullet(f['rels'])}

### Constraints

{bullet(f['constraints'])}

### Migration Tasks (Flyway)

{bullet(f['migrations'])}

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
{bullet(f['entities'])}

### Value Objects
{bullet(f['vos'])}

### Repositories
{bullet(f['repos'])}

### DTOs (application/API layer)
**Request:** {', '.join(f'`{x}`' for x in f['dtos_req'])}  
**Response:** {', '.join(f'`{x}`' for x in f['dtos_res'])}

### Validation
{bullet(f['validation'])}

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
{bullet(f['services'])}

### Controllers
{bullet(f['controllers'])}

### Exception Handling
{bullet(f['exceptions'])}

Global `@ControllerAdvice` maps to Problem Details.

### Security
{bullet([f['security']])}

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
{bullet(f['routes'])}

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
{bullet(f['pages'])}

### Components
{bullet(f['components'])}

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
{bullet(f['fe_models'])}

### Services
{bullet(f['fe_services'])}

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
{bullet(f['forms'])}

### Validation
{bullet(f['fe_validation'])}

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
{bullet([f['state']])}

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
{bullet(f['apis'])}

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
{bullet(f['dtos_req'])}

### Response DTOs
{bullet(f['dtos_res'])}

### Error Responses
{ERROR_CONTRACT}

---

## 9. QA Tasks

### Functional Tests
{bullet(f['qa_func'])}

### API Tests
{bullet(f['qa_api'])}

### UI Tests
{bullet(f['qa_ui'])}

---

## 10. Dependencies

### Required features
{prev}

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `{f['id']}`.

### Implementation sequence hint
Follow IMPL-DEP-001 optimal order; do not start UI polish before HTTP facade + auth for this module.

---

## 11. Definition of Done (Feature)

- [ ] Flyway migrations applied in CI
- [ ] Domain invariants covered by unit tests
- [ ] All listed APIs implemented + OpenAPI updated
- [ ] Angular routes/pages/facades wired (no mock-only)
- [ ] RBAC + location scope verified
- [ ] AC happy/validation/error/edge sampled in UAT pack
- [ ] Audit/movement side-effects verified (if mutating)
- [ ] Feature flagged or released per wave plan

---

*Generated for Technical Lead delivery planning — {f['id']}*
"""


def main():
    index_rows = []
    for f in FEATURES:
        path = OUT / f["file"]
        path.write_text(render(f), encoding="utf-8")
        index_rows.append(f"| {f['id']} | {f['name']} | [{f['file']}](./{f['file']}) | {', '.join(f['stories'])} |")
        print("wrote", path.name)

    index = f"""# IMS Feature Implementation Plans — Index

| Attribute | Detail |
|-----------|--------|
| **Document ID** | IMPL-PLAN-000 |
| **Perspective** | Technical Lead |
| **Date** | July 11, 2026 |
| **Companion docs** | [IMS-Implementation-Features.md](../IMS-Implementation-Features.md), [IMS-Feature-Dependency-Map.md](../IMS-Feature-Dependency-Map.md) |

## Shared engineering conventions

- **Backend:** Java 21, Spring Boot 3.x, Spring Modulith modules M-01–M-13, Spring Data JPA, MapStruct, Flyway, PostgreSQL schema-per-module
- **Frontend:** Angular 19 standalone, feature folders, ApiService + Facade + Signals, RFC 7807 error mapping
- **Security:** OAuth2/OIDC JWT; permission + location-scope on every endpoint
- **Errors:** `SRS/API_Design/Error-Response-Specification.md`
- **AC source:** `project_businsse/acceptance-criteria-reviewed.md`
- **Order:** implement per `IMS-Feature-Dependency-Map.md` (F-27 first)

## Plans ({len(FEATURES)})

| ID | Feature | Plan | User Stories |
|----|---------|------|--------------|
{chr(10).join(index_rows)}

## Suggested squad ownership

| Squad | Features |
|-------|----------|
| Platform | F-27, F-28, F-29, F-26 |
| Master & Balance | F-01, F-02, F-03, F-04, F-30 |
| Inbound | F-05, F-06, F-07 |
| Accuracy | F-14, F-15, F-16, F-17, F-18, F-19 |
| Fulfillment | F-10, F-11, F-12, F-13, F-21 |
| Network & Intel | F-08, F-09, F-20, F-22, F-23, F-24, F-25 |
"""
    (OUT / "README.md").write_text(index, encoding="utf-8")
    print("wrote README.md", len(FEATURES), "plans")


if __name__ == "__main__":
    main()
