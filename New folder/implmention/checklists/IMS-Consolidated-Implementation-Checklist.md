# IMS Consolidated Implementation Checklist

**Total tasks:** 288 · **Status baseline:** Not Started

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-01-DB-01` | F-01 | Create Flyway schema `catalog` and baseline migration | Database | P0 | Not Started | F-27 platform DB |
| `CHK-01-DB-02` | F-01 | Create table `catalog.products` with SKU UK, lifecycle CHECK, version, audit columns | Database | P0 | Not Started | CHK-01-DB-01 |
| `CHK-01-DB-03` | F-01 | Create table `catalog.product_identifiers` with FK to products and unique identifier | Database | P0 | Not Started | CHK-01-DB-02 |
| `CHK-01-DB-04` | F-01 | Add indexes on products(sku), products(lifecycle_status), products(product_name) | Database | P1 | Not Started | CHK-01-DB-02 |
| `CHK-01-DB-05` | F-01 | Grant app role DML on catalog tables; revoke DDL from app role | Database | P1 | Not Started | CHK-01-DB-03 |
| `CHK-01-BE-01` | F-01 | Implement Product aggregate root + ProductIdentifier entity/VO | Backend | P0 | Not Started | CHK-01-DB-02 |
| `CHK-01-BE-02` | F-01 | Implement value objects: ProductSku, LifecycleStatus, UnitOfMeasure, Category | Backend | P0 | Not Started | CHK-01-BE-01 |
| `CHK-01-BE-03` | F-01 | Implement ProductRepository (Spring Data JPA) | Backend | P0 | Not Started | CHK-01-BE-01 |
| `CHK-01-BE-04` | F-01 | Implement Request/Response DTOs + MapStruct mappers for product APIs | Backend | P0 | Not Started | CHK-01-BE-02 |
| `CHK-01-BE-05` | F-01 | Implement Bean Validation + domain validators (VR-001/007, mandatory fields) | Backend | P0 | Not Started | CHK-01-BE-04 |
| `CHK-01-BE-06` | F-01 | Implement ProductCatalogService (create/update/search/lifecycle) | Backend | P0 | Not Started | CHK-01-BE-03, CHK-01-BE-05 |
| `CHK-01-BE-07` | F-01 | Implement DuplicateDetectionService + resolve API | Backend | P1 | Not Started | CHK-01-BE-06 |
| `CHK-01-BE-08` | F-01 | Implement ProductController API-001–005, 007–009 with Problem Details errors | Backend | P0 | Not Started | CHK-01-BE-06 |
| `CHK-01-BE-09` | F-01 | Enforce PRODUCT_MANAGE / PRODUCT_VIEW permissions on endpoints | Backend | P0 | Not Started | F-27, CHK-01-BE-08 |
| `CHK-01-FE-01` | F-01 | Add child routes: catalog/new, catalog/:sku, catalog/:sku/edit | Frontend | P0 | Not Started | F-27 auth |
| `CHK-01-FE-02` | F-01 | Implement ProductApiService (HttpClient) replacing mocks | Frontend | P0 | Not Started | CHK-01-BE-08 |
| `CHK-01-FE-03` | F-01 | Implement ProductFacade with signals for list/filters/selected/saveState | Frontend | P0 | Not Started | CHK-01-FE-02 |
| `CHK-01-FE-04` | F-01 | Build Product list/create/edit pages (UI-005) with reactive forms + validation | Frontend | P0 | Not Started | CHK-01-FE-03 |
| `CHK-01-FE-05` | F-01 | Build lifecycle change + duplicate resolution UI flows | Frontend | P1 | Not Started | CHK-01-FE-04 |
| `CHK-01-FE-06` | F-01 | Map RFC 7807 field errors to form controls | Frontend | P1 | Not Started | CHK-01-FE-04 |
| `CHK-01-TE-01` | F-01 | API contract tests for API-001–005, 009 (happy + 400/403/409) | Testing | P0 | Not Started | CHK-01-BE-08 |
| `CHK-01-TE-02` | F-01 | Unit tests for lifecycle transitions and duplicate SKU invariant | Testing | P0 | Not Started | CHK-01-BE-06 |
| `CHK-01-TE-03` | F-01 | UI/E2E: create product, edit, lifecycle change (FAC-01-H1/H2/H3) | Testing | P1 | Not Started | CHK-01-FE-04 |
| `CHK-01-TE-04` | F-01 | Permission test: non-manager denied create (FAC-01-P1) | Testing | P0 | Not Started | CHK-01-BE-09 |
| `CHK-01-DO-01` | F-01 | Update OpenAPI for product endpoints | Documentation | P1 | Not Started | CHK-01-BE-08 |
| `CHK-01-DO-02` | F-01 | Mark FAC-01 checklist items with evidence links in AC file | Documentation | P2 | Not Started | CHK-01-TE-03 |
| `CHK-02-DB-01` | F-02 | Create Flyway schema `network` | Database | P0 | Not Started | F-27 |
| `CHK-02-DB-02` | F-02 | Create `network.inventory_locations` with location_code UK, hierarchy self-FK, status | Database | P0 | Not Started | CHK-02-DB-01 |
| `CHK-02-DB-03` | F-02 | Create `network.storage_positions` FK to location | Database | P0 | Not Started | CHK-02-DB-02 |
| `CHK-02-DB-04` | F-02 | Add freeze/operational status columns and CHECKs | Database | P0 | Not Started | CHK-02-DB-02 |
| `CHK-02-DB-05` | F-02 | Indexes on location_code, parent_location_id, operational_status | Database | P1 | Not Started | CHK-02-DB-02 |
| `CHK-02-BE-01` | F-02 | Implement InventoryLocation aggregate + StoragePosition entity | Backend | P0 | Not Started | CHK-02-DB-03 |
| `CHK-02-BE-02` | F-02 | VOs: LocationCode, LocationType, HierarchyPath, PhysicalAddress | Backend | P0 | Not Started | CHK-02-BE-01 |
| `CHK-02-BE-03` | F-02 | Repositories for location and storage positions | Backend | P0 | Not Started | CHK-02-BE-01 |
| `CHK-02-BE-04` | F-02 | DTOs/mappers for location APIs | Backend | P0 | Not Started | CHK-02-BE-02 |
| `CHK-02-BE-05` | F-02 | LocationLifecycleService (create, hierarchy, activate/deactivate/close, freeze status) | Backend | P0 | Not Started | CHK-02-BE-03 |
| `CHK-02-BE-06` | F-02 | LocationController API-011–021 + cycle hierarchy validation | Backend | P0 | Not Started | CHK-02-BE-05 |
| `CHK-02-BE-07` | F-02 | Enforce LOCATION_MANAGE/VIEW + location-scope filters | Backend | P0 | Not Started | F-27, CHK-02-BE-06 |
| `CHK-02-FE-01` | F-02 | Child routes for location detail and storage positions | Frontend | P0 | Not Started | F-27 |
| `CHK-02-FE-02` | F-02 | LocationApiService + LocationFacade | Frontend | P0 | Not Started | CHK-02-BE-06 |
| `CHK-02-FE-03` | F-02 | UI-007 list/create/edit + hierarchy tree + storage grid | Frontend | P0 | Not Started | CHK-02-FE-02 |
| `CHK-02-FE-04` | F-02 | Activation UX with opening-balance gate messaging | Frontend | P1 | Not Started | CHK-02-FE-03, F-30 |
| `CHK-02-TE-01` | F-02 | API tests API-011–017; reject cyclic hierarchy | Testing | P0 | Not Started | CHK-02-BE-06 |
| `CHK-02-TE-02` | F-02 | UI test create WH + add bin (FAC-02-H1/H3) | Testing | P1 | Not Started | CHK-02-FE-03 |
| `CHK-02-TE-03` | F-02 | Permission deny without LOCATION_MANAGE (FAC-02-P1) | Testing | P0 | Not Started | CHK-02-BE-07 |
| `CHK-02-DO-01` | F-02 | OpenAPI location module + go-live activation notes | Documentation | P1 | Not Started | CHK-02-BE-06 |
| `CHK-03-DB-01` | F-03 | Create `governance` schema + `reason_codes` + `governance_policies` | Database | P0 | Not Started | F-27 |
| `CHK-03-DB-02` | F-03 | Create `inventory.stock_policies` + `stock_policy_history` | Database | P0 | Not Started | F-01, F-02 |
| `CHK-03-DB-03` | F-03 | Constraints: uk(location,sku), qty>=0, reason code unique/retire flag | Database | P0 | Not Started | CHK-03-DB-01, CHK-03-DB-02 |
| `CHK-03-DB-04` | F-03 | ABC column/attr on catalog.products if not present | Database | P2 | Not Started | F-01 |
| `CHK-03-BE-01` | F-03 | StockPolicy + GovernancePolicy + ReasonCode aggregates | Backend | P0 | Not Started | CHK-03-DB-03 |
| `CHK-03-BE-02` | F-03 | VOs: StockThresholdSet, ApprovalThreshold, QuantityTolerance, AbcClass | Backend | P0 | Not Started | CHK-03-BE-01 |
| `CHK-03-BE-03` | F-03 | Repositories + DTOs for policies/reason codes/ABC | Backend | P0 | Not Started | CHK-03-BE-01 |
| `CHK-03-BE-04` | F-03 | StockPolicyService + GovernanceService (effective dating) | Backend | P0 | Not Started | CHK-03-BE-03 |
| `CHK-03-BE-05` | F-03 | API-038–040, API-022–030, API-006 | Backend | P0 | Not Started | CHK-03-BE-04 |
| `CHK-03-BE-06` | F-03 | SafetyStockProtectionService hooks for later consumers | Backend | P2 | Not Started | CHK-03-BE-04 |
| `CHK-03-BE-07` | F-03 | Permissions POLICY_MANAGE / GOVERNANCE_MANAGE | Backend | P0 | Not Started | F-27, CHK-03-BE-05 |
| `CHK-03-FE-01` | F-03 | UI-008 stock policy forms wired to API | Frontend | P0 | Not Started | CHK-03-BE-05 |
| `CHK-03-FE-02` | F-03 | UI-010 reason codes + thresholds/tolerances | Frontend | P0 | Not Started | CHK-03-BE-05 |
| `CHK-03-FE-03` | F-03 | UI-009 ABC classification grid (Phase 2) | Frontend | P2 | Not Started | CHK-03-BE-05 |
| `CHK-03-TE-01` | F-03 | API tests thresholds + retire reason code blocks use | Testing | P0 | Not Started | CHK-03-BE-05 |
| `CHK-03-TE-02` | F-03 | FAC-03-H1/V1/V4/P1 automated | Testing | P0 | Not Started | CHK-03-FE-01 |
| `CHK-03-DO-01` | F-03 | Document effective-dating rules for ops | Documentation | P2 | Not Started | CHK-03-BE-04 |
| `CHK-04-DB-01` | F-04 | Ensure `inventory.stock_positions` with on_hand/reserved/quarantine qty CHECKs | Database | P0 | Not Started | F-01, F-02 |
| `CHK-04-DB-02` | F-04 | Create `inventory.lot_batches` and `quarantine_holds` tables | Database | P1 | Not Started | CHK-04-DB-01 |
| `CHK-04-DB-03` | F-04 | Indexes for (location_code, sku) and status queries | Database | P0 | Not Started | CHK-04-DB-01 |
| `CHK-04-BE-01` | F-04 | StockPosition aggregate + ATP calculation domain service | Backend | P0 | Not Started | CHK-04-DB-01 |
| `CHK-04-BE-02` | F-04 | StockPositionRepository + query repository | Backend | P0 | Not Started | CHK-04-BE-01 |
| `CHK-04-BE-03` | F-04 | DTOs for stock position, availability, status board | Backend | P0 | Not Started | CHK-04-BE-02 |
| `CHK-04-BE-04` | F-04 | API-033–037 + intelligence 151–153 (MVP subset) | Backend | P0 | Not Started | CHK-04-BE-03 |
| `CHK-04-BE-05` | F-04 | Enforce INVENTORY_VIEW + mandatory location-scope filter | Backend | P0 | Not Started | F-27, CHK-04-BE-04 |
| `CHK-04-FE-01` | F-04 | InventoryApiService + InventoryVisibilityFacade | Frontend | P0 | Not Started | CHK-04-BE-04 |
| `CHK-04-FE-02` | F-04 | UI-020 status monitor with real data + filters | Frontend | P0 | Not Started | CHK-04-FE-01 |
| `CHK-04-FE-03` | F-04 | UI-021 availability inquiry form + results | Frontend | P0 | Not Started | CHK-04-FE-01 |
| `CHK-04-FE-04` | F-04 | Network/inbound views (US-028 Phase 2) | Frontend | P2 | Not Started | CHK-04-FE-02, F-07 |
| `CHK-04-TE-01` | F-04 | Unit tests ATP = on_hand - reserved - hold | Testing | P0 | Not Started | CHK-04-BE-01 |
| `CHK-04-TE-02` | F-04 | API + scope tests FAC-04-H1/P3 | Testing | P0 | Not Started | CHK-04-BE-05 |
| `CHK-04-TE-03` | F-04 | UI smoke FAC-04-H4 search/filter | Testing | P1 | Not Started | CHK-04-FE-02 |
| `CHK-04-DO-01` | F-04 | ATP definition note for UAT script | Documentation | P1 | Not Started | CHK-04-BE-01 |
| `CHK-05-DB-01` | F-05 | Create `inbound` schema + goods_receipts / lines | Database | P0 | Not Started | F-02 |
| `CHK-05-DB-02` | F-05 | Create `inbound.receipt_discrepancies` | Database | P0 | Not Started | CHK-05-DB-01 |
| `CHK-05-DB-03` | F-05 | Ensure movement table available for receipt postings | Database | P0 | Not Started | F-29 |
| `CHK-05-DB-04` | F-05 | Minimal PO seed/table support for validate-for-receipt until F-07 | Database | P0 | Not Started | CHK-05-DB-01 |
| `CHK-05-BE-01` | F-05 | GoodsReceipt aggregate + discrepancy entity | Backend | P0 | Not Started | CHK-05-DB-02 |
| `CHK-05-BE-02` | F-05 | VOs: PositiveQuantity, LotIdentity, ShelfLifeProfile | Backend | P0 | Not Started | CHK-05-BE-01 |
| `CHK-05-BE-03` | F-05 | GoodsReceivingService + DiscrepancyService + movement recording | Backend | P0 | Not Started | CHK-05-BE-01, F-29 |
| `CHK-05-BE-04` | F-05 | API-065–072, 075–076 + reason/tolerance consult | Backend | P0 | Not Started | CHK-05-BE-03, F-03 |
| `CHK-05-BE-05` | F-05 | Freeze check + RECEIVE_GOODS / location scope security | Backend | P0 | Not Started | F-27, CHK-05-BE-04 |
| `CHK-05-FE-01` | F-05 | InboundApiService + GoodsReceiptFacade | Frontend | P0 | Not Started | CHK-05-BE-04 |
| `CHK-05-FE-02` | F-05 | UI-015 goods receipt workbench | Frontend | P0 | Not Started | CHK-05-FE-01 |
| `CHK-05-FE-03` | F-05 | UI-016 discrepancy resolution | Frontend | P0 | Not Started | CHK-05-FE-01 |
| `CHK-05-FE-04` | F-05 | UI-018 non-PO/return intake | Frontend | P1 | Not Started | CHK-05-FE-01 |
| `CHK-05-FE-05` | F-05 | UI-022 movement history consumer | Frontend | P1 | Not Started | F-29, CHK-05-BE-03 |
| `CHK-05-TE-01` | F-05 | API E2E receive+verify; discrepancy path FAC-05-H1/H2 | Testing | P0 | Not Started | CHK-05-FE-02 |
| `CHK-05-TE-02` | F-05 | Lot required for traceable product FAC-05-V2 | Testing | P0 | Not Started | CHK-05-BE-04 |
| `CHK-05-TE-03` | F-05 | Permission/location scope FAC-05-P1/P2 | Testing | P0 | Not Started | CHK-05-BE-05 |
| `CHK-05-DO-01` | F-05 | Document PO-stub vs F-07 cutover for receiving | Documentation | P1 | Not Started | CHK-05-BE-04 |
| `CHK-06-DB-01` | F-06 | Create `inbound.put_aways` with FK to goods_receipt and storage_position | Database | P0 | Not Started | F-05, F-02 |
| `CHK-06-DB-02` | F-06 | Constraints: position belongs to receipt location | Database | P0 | Not Started | CHK-06-DB-01 |
| `CHK-06-BE-01` | F-06 | PutAwayService confirming storage and updating availability | Backend | P0 | Not Started | CHK-06-DB-02, F-04 |
| `CHK-06-BE-02` | F-06 | API-073, API-074 (+ storage position APIs) | Backend | P0 | Not Started | CHK-06-BE-01 |
| `CHK-06-BE-03` | F-06 | Permission PUT_AWAY_EXECUTE + location scope | Backend | P0 | Not Started | F-27, CHK-06-BE-02 |
| `CHK-06-FE-01` | F-06 | PutAwayApiService + facade | Frontend | P0 | Not Started | CHK-06-BE-02 |
| `CHK-06-FE-02` | F-06 | UI-017 pending queue + position picker + confirm | Frontend | P0 | Not Started | CHK-06-FE-01 |
| `CHK-06-TE-01` | F-06 | FAC-06-H2/X1 ATP only after put-away | Testing | P0 | Not Started | CHK-06-FE-02 |
| `CHK-06-TE-02` | F-06 | Invalid position / already put away errors | Testing | P1 | Not Started | CHK-06-BE-02 |
| `CHK-06-DO-01` | F-06 | Received vs available state diagram for UAT | Documentation | P2 | Not Started | CHK-06-BE-01 |
| `CHK-07-DB-01` | F-07 | Create `procurement` schema: suppliers, POs, lines, expected deliveries | Database | P2 | Not Started | F-01, F-02 |
| `CHK-07-DB-02` | F-07 | PO status CHECKs; supplier_code UK; FKs for lines/deliveries | Database | P2 | Not Started | CHK-07-DB-01 |
| `CHK-07-BE-01` | F-07 | Supplier + PurchaseOrder aggregates | Backend | P2 | Not Started | CHK-07-DB-02 |
| `CHK-07-BE-02` | F-07 | PurchaseOrderService (create/amend/cancel/schedule delivery) | Backend | P2 | Not Started | CHK-07-BE-01 |
| `CHK-07-BE-03` | F-07 | API-049–053, 059–065, 161–163 | Backend | P2 | Not Started | CHK-07-BE-02 |
| `CHK-07-BE-04` | F-07 | Permissions SUPPLIER_MANAGE / PO_MANAGE / PO_VIEW | Backend | P2 | Not Started | F-27, CHK-07-BE-03 |
| `CHK-07-FE-01` | F-07 | ProcurementApiService + PurchaseOrderFacade | Frontend | P2 | Not Started | CHK-07-BE-03 |
| `CHK-07-FE-02` | F-07 | UI-011 suppliers, UI-012 POs | Frontend | P2 | Not Started | CHK-07-FE-01 |
| `CHK-07-FE-03` | F-07 | UI-014 delivery planning, UI-019 inbound tracking | Frontend | P2 | Not Started | CHK-07-FE-01 |
| `CHK-07-TE-01` | F-07 | FAC-07-H1/H3/V1/V2 API+UI | Testing | P2 | Not Started | CHK-07-FE-02 |
| `CHK-07-TE-02` | F-07 | Receiving integration uses live validate-for-receipt | Testing | P2 | Not Started | CHK-07-BE-03, F-05 |
| `CHK-07-DO-01` | F-07 | Replace PO-stub runbook with F-07 cutover notes | Documentation | P2 | Not Started | CHK-07-BE-03 |
| `CHK-08-DB-01` | F-08 | Create `transfer` schema: requests, transfers, lines, in_transit_stock | Database | P0 | Not Started | F-02 |
| `CHK-08-DB-02` | F-08 | Constraints source!=dest; status CHECKs; optimistic locking | Database | P0 | Not Started | CHK-08-DB-01 |
| `CHK-08-BE-01` | F-08 | StockTransfer aggregate + capacity evaluation vs stock policy | Backend | P0 | Not Started | CHK-08-DB-02, F-03, F-04 |
| `CHK-08-BE-02` | F-08 | TransferService request/approve/reject/dispatch/receive | Backend | P0 | Not Started | CHK-08-BE-01, F-28 |
| `CHK-08-BE-03` | F-08 | API-098–107, API-042 | Backend | P0 | Not Started | CHK-08-BE-02 |
| `CHK-08-BE-04` | F-08 | SoD on approve; TRANSFER_* permissions | Backend | P0 | Not Started | F-28, CHK-08-BE-03 |
| `CHK-08-FE-01` | F-08 | TransferApiService + TransferFacade | Frontend | P0 | Not Started | CHK-08-BE-03 |
| `CHK-08-FE-02` | F-08 | UI-038 request, UI-039 approval, UI-040 execution | Frontend | P0 | Not Started | CHK-08-FE-01 |
| `CHK-08-FE-03` | F-08 | In-transit monitor polish (US-061 Phase 2) | Frontend | P2 | Not Started | CHK-08-FE-02 |
| `CHK-08-TE-01` | F-08 | FAC-08-H1–H3/V2/E2 golden path + SoD | Testing | P0 | Not Started | CHK-08-FE-02 |
| `CHK-08-TE-02` | F-08 | Source minimum blocks over-transfer | Testing | P0 | Not Started | CHK-08-BE-03 |
| `CHK-08-DO-01` | F-08 | Transfer state machine for UAT | Documentation | P1 | Not Started | CHK-08-BE-02 |
| `CHK-09-DB-01` | F-09 | Optional recommendation cache table (or pure query) | Database | P3 | Not Started | F-04 |
| `CHK-09-BE-01` | F-09 | NetworkRebalancingService + API-166/160/036 | Backend | P3 | Not Started | F-04, F-08 |
| `CHK-09-BE-02` | F-09 | Convert recommendation → transfer request command | Backend | P3 | Not Started | CHK-09-BE-01, F-08 |
| `CHK-09-FE-01` | F-09 | UI-041 imbalance analysis + convert action | Frontend | P3 | Not Started | CHK-09-BE-01 |
| `CHK-09-TE-01` | F-09 | FAC-09-H1/H2/V2 | Testing | P3 | Not Started | CHK-09-FE-01 |
| `CHK-09-DO-01` | F-09 | Phase 3 scope note / MoSCoW Won't waiver if deferred | Documentation | P3 | Not Started | — |
| `CHK-10-DB-01` | F-10 | Create fulfillment.customer_orders, order_lines, inventory_reservations | Database | P0 | Not Started | F-04 |
| `CHK-10-DB-02` | F-10 | Optimistic locking on stock_positions for reservation races | Database | P0 | Not Started | CHK-10-DB-01 |
| `CHK-10-BE-01` | F-10 | CustomerOrderFulfillment aggregate + reservation saga | Backend | P0 | Not Started | CHK-10-DB-02 |
| `CHK-10-BE-02` | F-10 | API-081, 084–086, 043–044 (087 multi-location P2) | Backend | P0 | Not Started | CHK-10-BE-01 |
| `CHK-10-BE-03` | F-10 | ORDER_RESERVE permission + location scope | Backend | P0 | Not Started | F-27, CHK-10-BE-02 |
| `CHK-10-FE-01` | F-10 | FulfillmentApiService + ReservationFacade | Frontend | P0 | Not Started | CHK-10-BE-02 |
| `CHK-10-FE-02` | F-10 | UI-030 reservation workbench | Frontend | P0 | Not Started | CHK-10-FE-01 |
| `CHK-10-FE-03` | F-10 | UI-035 multi-location planner (Phase 2) | Frontend | P2 | Not Started | CHK-10-BE-02 |
| `CHK-10-TE-01` | F-10 | FAC-10-H1–H3, E1 concurrency, V3 insufficient ATP | Testing | P0 | Not Started | CHK-10-FE-02 |
| `CHK-10-TE-02` | F-10 | Cancel releases reservation restores ATP | Testing | P0 | Not Started | CHK-10-BE-02 |
| `CHK-10-DO-01` | F-10 | Reservation saga notes + idempotency keys | Documentation | P1 | Not Started | CHK-10-BE-01 |
| `CHK-11-DB-01` | F-11 | Create fulfillment_executions, pick_lines, shipments, shipment_lines | Database | P0 | Not Started | F-10 |
| `CHK-11-BE-01` | F-11 | PickPackShipService + lot selection helpers | Backend | P0 | Not Started | CHK-11-DB-01 |
| `CHK-11-BE-02` | F-11 | API-088–092, 082–083, 097 (+ C-01 location queue) | Backend | P0 | Not Started | CHK-11-BE-01 |
| `CHK-11-BE-03` | F-11 | Deduct on-hand only on ship; FULFILL_PICK/SHIP permissions | Backend | P0 | Not Started | CHK-11-BE-02, F-27 |
| `CHK-11-FE-01` | F-11 | PickPackShipFacade + UI-031 workbench | Frontend | P0 | Not Started | CHK-11-BE-02 |
| `CHK-11-FE-02` | F-11 | UI-034 order status | Frontend | P0 | Not Started | CHK-11-BE-02 |
| `CHK-11-TE-01` | F-11 | FAC-11-H1–H3; ship-before-pack blocked | Testing | P0 | Not Started | CHK-11-FE-01 |
| `CHK-11-TE-02` | F-11 | Golden path reserve→ship balances | Testing | P0 | Not Started | CHK-11-FE-01, F-10 |
| `CHK-11-DO-01` | F-11 | Document C-01 workaround until queue API exists | Documentation | P1 | Not Started | CHK-11-BE-02 |
| `CHK-12-DB-01` | F-12 | Create `fulfillment.backorders` with priority/status | Database | P0 | Not Started | F-11 |
| `CHK-12-BE-01` | F-12 | PartialFulfillmentService + BackorderService | Backend | P0 | Not Started | CHK-12-DB-01 |
| `CHK-12-BE-02` | F-12 | API-093–095, 164 (priority Phase 2) | Backend | P0 | Not Started | CHK-12-BE-01 |
| `CHK-12-BE-03` | F-12 | Require customer ack for partial ship | Backend | P0 | Not Started | CHK-12-BE-02 |
| `CHK-12-FE-01` | F-12 | UI-032 partial ship wizard + backorder board | Frontend | P0 | Not Started | CHK-12-BE-02 |
| `CHK-12-FE-02` | F-12 | Backorder priority UI (Phase 2) | Frontend | P2 | Not Started | CHK-12-FE-01 |
| `CHK-12-TE-01` | F-12 | FAC-12-H1/V1; priority sequencing Phase 2 | Testing | P0 | Not Started | CHK-12-FE-01 |
| `CHK-12-DO-01` | F-12 | Partial/backorder customer comms notes | Documentation | P2 | Not Started | CHK-12-BE-02 |
| `CHK-13-DB-01` | F-13 | Create fulfillment exceptions table/fields | Database | P2 | Not Started | F-11 |
| `CHK-13-BE-01` | F-13 | FulfillmentExceptionService + optional quarantine create | Backend | P2 | Not Started | CHK-13-DB-01, F-18 |
| `CHK-13-BE-02` | F-13 | API-096, 165, 045; substitution Phase 3 | Backend | P2 | Not Started | CHK-13-BE-01 |
| `CHK-13-FE-01` | F-13 | UI-033 exception queue + resolve forms | Frontend | P2 | Not Started | CHK-13-BE-02 |
| `CHK-13-TE-01` | F-13 | FAC-13-H1/H2/V1/P1 | Testing | P2 | Not Started | CHK-13-FE-01 |
| `CHK-13-DO-01` | F-13 | Exception type catalog for WH training | Documentation | P2 | Not Started | CHK-13-BE-02 |
| `CHK-14-DB-01` | F-14 | Create `accuracy.cycle_counts` | Database | P0 | Not Started | F-04 |
| `CHK-14-BE-01` | F-14 | CycleCount aggregate + blind count rules | Backend | P0 | Not Started | CHK-14-DB-01 |
| `CHK-14-BE-02` | F-14 | API-108–111, 168 | Backend | P0 | Not Started | CHK-14-BE-01 |
| `CHK-14-BE-03` | F-14 | Permissions CYCLE_COUNT_MANAGE/EXECUTE | Backend | P0 | Not Started | F-27, CHK-14-BE-02 |
| `CHK-14-FE-01` | F-14 | UI-023 assignment list + blind entry (hide system qty) | Frontend | P0 | Not Started | CHK-14-BE-02 |
| `CHK-14-TE-01` | F-14 | FAC-14-H2/V3 blind enforced; API tests | Testing | P0 | Not Started | CHK-14-FE-01 |
| `CHK-14-DO-01` | F-14 | Blind count SOP for warehouse staff | Documentation | P1 | Not Started | CHK-14-FE-01 |
| `CHK-15-DB-01` | F-15 | Create `accuracy.physical_inventory_counts`; freeze flag on locations | Database | P0 | Not Started | F-02 |
| `CHK-15-BE-01` | F-15 | PhysicalInventoryCountService + LocationFreezeService | Backend | P0 | Not Started | CHK-15-DB-01 |
| `CHK-15-BE-02` | F-15 | API-020, 112–115; block mutators when frozen | Backend | P0 | Not Started | CHK-15-BE-01 |
| `CHK-15-FE-01` | F-15 | UI-024 initiate/progress/certify + freeze banner | Frontend | P0 | Not Started | CHK-15-BE-02 |
| `CHK-15-TE-01` | F-15 | FAC-15-H1/E1 receive blocked while frozen | Testing | P0 | Not Started | CHK-15-FE-01, F-05 |
| `CHK-15-DO-01` | F-15 | Physical count freeze checklist | Documentation | P1 | Not Started | CHK-15-BE-02 |
| `CHK-16-DB-01` | F-16 | Create count_variances + adjustment case tables | Database | P0 | Not Started | F-14, F-15 |
| `CHK-16-BE-01` | F-16 | VarianceInvestigationService + approval routing/thresholds | Backend | P0 | Not Started | CHK-16-DB-01, F-03, F-28 |
| `CHK-16-BE-02` | F-16 | API-116–119, 123, 029, 031 | Backend | P0 | Not Started | CHK-16-BE-01 |
| `CHK-16-FE-01` | F-16 | UI-025 investigation + approve/reject | Frontend | P0 | Not Started | CHK-16-BE-02 |
| `CHK-16-TE-01` | F-16 | FAC-16-E1 SoD self-approve blocked; H2 approve posts adjust | Testing | P0 | Not Started | CHK-16-FE-01 |
| `CHK-16-DO-01` | F-16 | Variance approval matrix by threshold | Documentation | P1 | Not Started | CHK-16-BE-01 |
| `CHK-17-DB-01` | F-17 | Create accuracy.stock_adjustments + inventory_write_offs | Database | P0 | Not Started | F-03 |
| `CHK-17-BE-01` | F-17 | StockAdjustmentService + WriteOffService + reason validation | Backend | P0 | Not Started | CHK-17-DB-01, F-28 |
| `CHK-17-BE-02` | F-17 | API-120–122 (+ reason APIs); movement on post | Backend | P0 | Not Started | CHK-17-BE-01, F-29 |
| `CHK-17-BE-03` | F-17 | Permissions ADJUST_SUBMIT/APPROVE, WRITE_OFF_AUTHORIZE | Backend | P0 | Not Started | F-27, CHK-17-BE-02 |
| `CHK-17-FE-01` | F-17 | UI-026 adjustments, UI-027 write-offs | Frontend | P0 | Not Started | CHK-17-BE-02 |
| `CHK-17-TE-01` | F-17 | FAC-17-H2/V1/E1/P2 | Testing | P0 | Not Started | CHK-17-FE-01 |
| `CHK-17-DO-01` | F-17 | Reason code usage guide | Documentation | P1 | Not Started | F-03 |
| `CHK-18-DB-01` | F-18 | Ensure quarantine_holds table + hold type CHECK | Database | P2 | Not Started | F-04 |
| `CHK-18-BE-01` | F-18 | QuarantineHoldService apply/release updating ATP | Backend | P2 | Not Started | CHK-18-DB-01 |
| `CHK-18-BE-02` | F-18 | API-045, 046, 154 | Backend | P2 | Not Started | CHK-18-BE-01 |
| `CHK-18-FE-01` | F-18 | UI-028 quarantine register | Frontend | P2 | Not Started | CHK-18-BE-02 |
| `CHK-18-TE-01` | F-18 | FAC-18-H1/H2 ATP exclusion | Testing | P2 | Not Started | CHK-18-FE-01 |
| `CHK-18-DO-01` | F-18 | Hold type definitions for WH | Documentation | P2 | Not Started | CHK-18-BE-02 |
| `CHK-19-DB-01` | F-19 | Optional materialized view for shrinkage aggregates | Database | P2 | Not Started | F-17 |
| `CHK-19-BE-01` | F-19 | ShrinkageAnalysisService + API-167 | Backend | P2 | Not Started | CHK-19-DB-01 |
| `CHK-19-FE-01` | F-19 | UI-029 analysis charts/tables | Frontend | P2 | Not Started | CHK-19-BE-01 |
| `CHK-19-TE-01` | F-19 | FAC-19-H1/V1/P1 | Testing | P2 | Not Started | CHK-19-FE-01 |
| `CHK-19-DO-01` | F-19 | Monthly loss review SOP | Documentation | P2 | Not Started | CHK-19-FE-01 |
| `CHK-20-DB-01` | F-20 | Create audit.operational_alerts; purchase_requisitions (Phase 2) | Database | P0 | Not Started | F-03 |
| `CHK-20-BE-01` | F-20 | StockAlertService threshold breach detection + dedupe | Backend | P0 | Not Started | CHK-20-DB-01, F-04 |
| `CHK-20-BE-02` | F-20 | API-158–160 alerts/recommendations (MVP) | Backend | P0 | Not Started | CHK-20-BE-01 |
| `CHK-20-BE-03` | F-20 | Requisition APIs 054–058 + list gap C-03 (Phase 2) | Backend | P2 | Not Started | CHK-20-DB-01, F-07 |
| `CHK-20-FE-01` | F-20 | UI-036 alert review + ack | Frontend | P0 | Not Started | CHK-20-BE-02 |
| `CHK-20-FE-02` | F-20 | UI-037 / UI-013 requisition flows (Phase 2) | Frontend | P2 | Not Started | CHK-20-BE-03 |
| `CHK-20-TE-01` | F-20 | FAC-20-H1/H2/H3; requisition FAC-20-H4 Phase 2 | Testing | P0 | Not Started | CHK-20-FE-01 |
| `CHK-20-DO-01` | F-20 | Alert severity & ack policy | Documentation | P1 | Not Started | CHK-20-BE-01 |
| `CHK-21-DB-01` | F-21 | Create returns schema: RAs, customer_returns, dispositions | Database | P2 | Not Started | F-10 |
| `CHK-21-BE-01` | F-21 | CustomerReturnCase aggregate + services | Backend | P2 | Not Started | CHK-21-DB-01 |
| `CHK-21-BE-02` | F-21 | API-124–131 (prefer 128 over 076 — C-04) | Backend | P2 | Not Started | CHK-21-BE-01 |
| `CHK-21-FE-01` | F-21 | UI-042 RA management, UI-043 inspection/disposition | Frontend | P2 | Not Started | CHK-21-BE-02 |
| `CHK-21-TE-01` | F-21 | FAC-21-H1–H5/V2/P1 | Testing | P2 | Not Started | CHK-21-FE-01 |
| `CHK-21-DO-01` | F-21 | Returns disposition decision tree | Documentation | P2 | Not Started | CHK-21-BE-02 |
| `CHK-22-DB-01` | F-22 | Reporting views/indexes for dashboard & movements | Database | P0 | Not Started | F-04, F-05 |
| `CHK-22-BE-01` | F-22 | DashboardService + OperationalReportService | Backend | P0 | Not Started | CHK-22-DB-01 |
| `CHK-22-BE-02` | F-22 | API-150–152, 155 (+ 167/168 as available) | Backend | P0 | Not Started | CHK-22-BE-01 |
| `CHK-22-FE-01` | F-22 | Replace UI-002 mocks with live widgets | Frontend | P0 | Not Started | CHK-22-BE-02 |
| `CHK-22-FE-02` | F-22 | UI-044 operational reports + filters/export | Frontend | P0 | Not Started | CHK-22-BE-02 |
| `CHK-22-TE-01` | F-22 | FAC-22-H1–H4/P2 | Testing | P0 | Not Started | CHK-22-FE-01 |
| `CHK-22-DO-01` | F-22 | Dashboard widget catalog for roles | Documentation | P1 | Not Started | CHK-22-FE-01 |
| `CHK-23-DB-01` | F-23 | KPI snapshot tables/views | Database | P3 | Not Started | F-22 |
| `CHK-23-BE-01` | F-23 | KpiService + API-170 | Backend | P3 | Not Started | CHK-23-DB-01 |
| `CHK-23-FE-01` | F-23 | UI-003 executive KPI dashboard | Frontend | P3 | Not Started | CHK-23-BE-01 |
| `CHK-23-TE-01` | F-23 | FAC-23-H1/P1 | Testing | P3 | Not Started | CHK-23-FE-01 |
| `CHK-23-DO-01` | F-23 | KPI definitions & targets | Documentation | P3 | Not Started | CHK-23-BE-01 |
| `CHK-24-DB-01` | F-24 | finance.supplier_invoices* + valuation snapshot tables | Database | P3 | Not Started | F-07, F-05 |
| `CHK-24-BE-01` | F-24 | ThreeWayMatchService + ValuationService + API-077–080, 171–172 | Backend | P3 | Not Started | CHK-24-DB-01 |
| `CHK-24-FE-01` | F-24 | UI-045 valuation reconciliation | Frontend | P3 | Not Started | CHK-24-BE-01 |
| `CHK-24-TE-01` | F-24 | FAC-24-H1–H4/V2 | Testing | P3 | Not Started | CHK-24-FE-01 |
| `CHK-24-DO-01` | F-24 | Month-end recon runbook | Documentation | P3 | Not Started | CHK-24-FE-01 |
| `CHK-25-DB-01` | F-25 | commercial.promotional_stock_allocations* | Database | P3 | Not Started | F-04 |
| `CHK-25-BE-01` | F-25 | CampaignAllocationService + API-132–139, 048, 169 | Backend | P3 | Not Started | CHK-25-DB-01 |
| `CHK-25-FE-01` | F-25 | UI-046 promotional readiness | Frontend | P3 | Not Started | CHK-25-BE-01 |
| `CHK-25-TE-01` | F-25 | FAC-25-H1/H2/E2 ring-fence isolation | Testing | P3 | Not Started | CHK-25-FE-01 |
| `CHK-25-DO-01` | F-25 | Campaign readiness checklist | Documentation | P3 | Not Started | CHK-25-FE-01 |
| `CHK-26-DB-01` | F-26 | Ensure `audit.operational_alerts` with ack columns/indexes | Database | P0 | Not Started | F-27 |
| `CHK-26-BE-01` | F-26 | NotificationService + role-filtered feed + API-158/159 | Backend | P0 | Not Started | CHK-26-DB-01 |
| `CHK-26-BE-02` | F-26 | Wire producers: stock, approval, transfer, fulfillment, inbound, campaign | Backend | P1 | Not Started | CHK-26-BE-01, F-20, F-17 |
| `CHK-26-FE-01` | F-26 | Core NotificationFacade + header badge | Frontend | P0 | Not Started | CHK-26-BE-01 |
| `CHK-26-FE-02` | F-26 | UI-004 notification center list/ack/deep links | Frontend | P0 | Not Started | CHK-26-FE-01 |
| `CHK-26-TE-01` | F-26 | FAC-26-H1–H3/P1 role filtering | Testing | P0 | Not Started | CHK-26-FE-02 |
| `CHK-26-DO-01` | F-26 | Alert taxonomy & recipient matrix | Documentation | P1 | Not Started | CHK-26-BE-02 |
| `CHK-27-DB-01` | F-27 | Create `identity` schema: user_accounts, role_assignments, role_assignment_locations | Database | P0 | Not Started | — |
| `CHK-27-DB-02` | F-27 | Seed admin user + baseline roles (UR subset) | Database | P0 | Not Started | CHK-27-DB-01 |
| `CHK-27-BE-01` | F-27 | Spring Security OAuth2/JWT resource server + session endpoints | Backend | P0 | Not Started | CHK-27-DB-02 |
| `CHK-27-BE-02` | F-27 | UserAccount aggregate + UserAdminService | Backend | P0 | Not Started | CHK-27-DB-01 |
| `CHK-27-BE-03` | F-27 | API-140–149, 173, 174 | Backend | P0 | Not Started | CHK-27-BE-01, CHK-27-BE-02 |
| `CHK-27-BE-04` | F-27 | Authorization evaluate + location-scope validate services | Backend | P0 | Not Started | CHK-27-BE-03 |
| `CHK-27-FE-01` | F-27 | HttpClient, interceptors, environments, auth/guest guards | Frontend | P0 | Not Started | CHK-27-BE-01 |
| `CHK-27-FE-02` | F-27 | UI-001 real sign-in; AuthService/SessionStore signals | Frontend | P0 | Not Started | CHK-27-FE-01 |
| `CHK-27-FE-03` | F-27 | UI-049 user admin, UI-050 roles/access | Frontend | P0 | Not Started | CHK-27-BE-03 |
| `CHK-27-FE-04` | F-27 | Permission-aware navigation filtering | Frontend | P1 | Not Started | CHK-27-FE-03 |
| `CHK-27-TE-01` | F-27 | FAC-27-H1/H3/E1/E2/P1 API+UI | Testing | P0 | Not Started | CHK-27-FE-02 |
| `CHK-27-TE-02` | F-27 | Protected route returns 401 without token | Testing | P0 | Not Started | CHK-27-FE-01 |
| `CHK-27-DO-01` | F-27 | Auth setup, seed users, role matrix quick ref | Documentation | P0 | Not Started | CHK-27-BE-03 |
| `CHK-28-DB-01` | F-28 | Ensure audit_trail_records; SoD rule seed in governance | Database | P0 | Not Started | F-27 |
| `CHK-28-BE-01` | F-28 | SegregationOfDutiesService + ActivityLogging aspect/interceptor | Backend | P0 | Not Started | CHK-28-DB-01 |
| `CHK-28-BE-02` | F-28 | API-031, 148, 149 wired into approval commands | Backend | P0 | Not Started | CHK-28-BE-01 |
| `CHK-28-FE-01` | F-28 | Disable approve actions when SoD evaluate fails; show dialog | Frontend | P0 | Not Started | CHK-28-BE-02 |
| `CHK-28-FE-02` | F-28 | UI-050 SoD/policy configuration surfaces | Frontend | P1 | Not Started | CHK-28-BE-02 |
| `CHK-28-TE-01` | F-28 | FAC-28-H2/E1 self-approve blocked on adjustment/variance/transfer | Testing | P0 | Not Started | CHK-28-FE-01, F-17 |
| `CHK-28-DO-01` | F-28 | SoD matrix (initiator vs approver) for auditors | Documentation | P1 | Not Started | CHK-28-BE-01 |
| `CHK-29-DB-01` | F-29 | inventory_movement_records + audit_trail_records; REVOKE UPDATE/DELETE | Database | P0 | Not Started | F-28 |
| `CHK-29-DB-02` | F-29 | Indexes on entity/date/user for query performance | Database | P1 | Not Started | CHK-29-DB-01 |
| `CHK-29-BE-01` | F-29 | MovementAppendService used by all stock mutators | Backend | P0 | Not Started | CHK-29-DB-01 |
| `CHK-29-BE-02` | F-29 | AuditTrailQueryService + API-155–157 | Backend | P0 | Not Started | CHK-29-BE-01 |
| `CHK-29-BE-03` | F-29 | Control breach detection (Phase 2) | Backend | P2 | Not Started | CHK-29-BE-02 |
| `CHK-29-FE-01` | F-29 | UI-022 movement history; UI-048 audit query | Frontend | P0 | Not Started | CHK-29-BE-02 |
| `CHK-29-FE-02` | F-29 | UI-047 audit workspace (Phase 2) | Frontend | P2 | Not Started | CHK-29-BE-03 |
| `CHK-29-TE-01` | F-29 | FAC-29-H1/E1 mutate audit forbidden; P1 AUDIT_VIEW | Testing | P0 | Not Started | CHK-29-FE-01 |
| `CHK-29-DO-01` | F-29 | Audit retention & export policy | Documentation | P1 | Not Started | CHK-29-BE-02 |
| `CHK-30-DB-01` | F-30 | Optional import_batches / import_errors staging tables | Database | P0 | Not Started | F-01 |
| `CHK-30-BE-01` | F-30 | ProductImportService validate/upsert + OpeningBalanceService | Backend | P0 | Not Started | CHK-30-DB-01, F-01, F-04 |
| `CHK-30-BE-02` | F-30 | API-010, 032, 017 activation gate | Backend | P0 | Not Started | CHK-30-BE-01, F-02 |
| `CHK-30-BE-03` | F-30 | SoD: importer ≠ opening approver when required | Backend | P0 | Not Started | F-28, CHK-30-BE-02 |
| `CHK-30-FE-01` | F-30 | UI-006 import wizard: upload/validate/review/approve/activate | Frontend | P0 | Not Started | CHK-30-BE-02 |
| `CHK-30-TE-01` | F-30 | FAC-30-H1–H3/V1/V4/P3 | Testing | P0 | Not Started | CHK-30-FE-01 |
| `CHK-30-TE-02` | F-30 | Production cutover dry-run checklist execution | Testing | P0 | Not Started | CHK-30-FE-01 |
| `CHK-30-DO-01` | F-30 | Go-live runbook + rollback plan | Documentation | P0 | Not Started | CHK-30-BE-02 |
