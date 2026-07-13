# Screen Coverage Matrix

**Project:** IMS Frontend vs. Approved UI Specification  
**Specification Source:** `SRS/Inventory-Management-System-SRS.md` (UI-001–UI-050, C-001–C-060)  
**Implementation Source:** `ims-frontend/`  
**Report Date:** July 7, 2026

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total screens in specification | 50 |
| Base routes registered | 50 / 50 (100%) |
| Child/detail routes in specification | ~35 |
| Child/detail routes implemented | 0 / ~35 (0%) |
| Screens rated **Yes** (≥80% complete) | 0 |
| Screens rated **Partial** (route + scaffold or partial UI) | 50 |
| Screens rated **No** (missing route/page) | 0 |
| **Weighted average completion** | **~22%** |

### Implementation Tiers Observed

| Tier | Screens | Description |
|------|---------|-------------|
| **Tier A — Functional shell** | UI-001 | Sign-in form with demo auth; partial wireframe |
| **Tier B — Composed UI** | UI-002 | Dashboard widgets wired to mock data |
| **Tier C — Scaffold only** | UI-003–UI-050 | Route, breadcrumb, title bar, JSON mock preview only |

### Global Gaps (All Screens)

- No `HttpClient` / API service layer; all data from `MockDataService`
- No permission-based route guards or field-level authorization
- No role-filtered navigation (static `MAIN_NAVIGATION`)
- No feature child/detail routes (`:id`, `/new`, nested paths)
- 60 shared components exist as files but are **not wired** into Tier C screens
- No feature-specific child components from the SRS architecture mapping

---

## Assessment Methodology

### Status Definitions

| Status | Criteria |
|--------|----------|
| **Yes** | ≥80% of wireframe UI elements present; core workflows functional (even with mock/API) |
| **Partial** | Route and page exist; some UI or behavior present but major spec gaps remain |
| **No** | Route or page component absent |

### Completion Percentage Rubric

| Dimension | Weight |
|-----------|--------|
| Base route registered | 10% |
| Page component loads | 5% |
| Wireframe UI layout (forms, tables, panels, actions) | 40% |
| SRS child/feature components | 20% |
| Required shared component integration | 10% |
| Business functionality (CRUD, workflows, API, permissions) | 15% |

---

## Screen Coverage Matrix

| ID | Screen Name | Expected Route(s) | Impl. | Completion |
|----|-------------|-------------------|-------|------------|
| UI-001 | Sign In / Session Entry | `/auth/sign-in` | Partial | 52% |
| UI-002 | Operational Home Dashboard | `/home/operations` | Partial | 48% |
| UI-003 | Executive KPI Dashboard | `/reports/executive-kpis` | Partial | 20% |
| UI-004 | Notification Center | `/notifications` | Partial | 20% |
| UI-005 | Product Catalog Management | `/products/catalog`, `/products/catalog/new`, `/products/catalog/:sku` | Partial | 18% |
| UI-006 | Product Import Workspace | `/products/import` | Partial | 18% |
| UI-007 | Location and Warehouse Management | `/locations`, `/locations/new`, `/locations/:locationCode` | Partial | 18% |
| UI-008 | Stock Policy and Threshold Management | `/products/stock-policies`, `/products/stock-policies/:locationCode/:sku` | Partial | 18% |
| UI-009 | ABC Classification Management | `/products/abc-classification` | Partial | 18% |
| UI-010 | Governance Policies and Reason Codes | `/governance/policies`, `/governance/reason-codes` | Partial | 18% |
| UI-011 | Supplier Management | `/procurement/suppliers`, `/procurement/suppliers/new`, `/procurement/suppliers/:supplierCode` | Partial | 18% |
| UI-012 | Purchase Order Management | `/procurement/purchase-orders`, `/procurement/purchase-orders/new`, `/procurement/purchase-orders/:purchaseOrderId` | Partial | 18% |
| UI-013 | Purchase Requisition Management | `/procurement/requisitions`, `/procurement/requisitions/:requisitionId` | Partial | 18% |
| UI-014 | Inbound Delivery Planning | `/procurement/inbound-delivery-planning` | Partial | 18% |
| UI-015 | Goods Receipt Workbench | `/inbound/goods-receipts`, `/inbound/goods-receipts/:goodsReceiptId` | Partial | 18% |
| UI-016 | Receipt Discrepancy Resolution | `/inbound/discrepancies`, `/inbound/goods-receipts/:goodsReceiptId/discrepancies` | Partial | 18% |
| UI-017 | Put-Away Workbench | `/inbound/put-away`, `/inbound/put-away/:goodsReceiptId` | Partial | 18% |
| UI-018 | Non-PO and Return Receipt Intake | `/inbound/non-po-receipts` | Partial | 18% |
| UI-019 | Inbound Supply Tracking | `/procurement/inbound-supply-tracking` | Partial | 18% |
| UI-020 | Inventory Status Monitor | `/inventory/status-monitor` | Partial | 18% |
| UI-021 | Inventory Availability Inquiry | `/inventory/availability` | Partial | 18% |
| UI-022 | Inventory Movement History | `/inventory/movement-history` | Partial | 18% |
| UI-023 | Cycle Count Workbench | `/inventory/cycle-counts`, `/inventory/cycle-counts/:cycleCountId` | Partial | 18% |
| UI-024 | Physical Inventory Count Management | `/inventory/physical-counts`, `/inventory/physical-counts/:physicalCountId` | Partial | 18% |
| UI-025 | Variance Investigation and Approval | `/inventory/variances`, `/inventory/variances/:caseId` | Partial | 18% |
| UI-026 | Stock Adjustment Management | `/inventory/adjustments`, `/inventory/adjustments/:caseId` | Partial | 18% |
| UI-027 | Write-Off Authorization | `/inventory/write-offs`, `/inventory/write-offs/:caseId` | Partial | 18% |
| UI-028 | Quarantine and Hold Register | `/inventory/quarantine` | Partial | 18% |
| UI-029 | Shrinkage, Loss, and Obsolescence Analysis | `/inventory/shrinkage-obsolescence` | Partial | 18% |
| UI-030 | Order Reservation Workbench | `/fulfillment/reservations`, `/fulfillment/reservations/:orderId` | Partial | 18% |
| UI-031 | Pick, Pack, and Ship Workbench | `/fulfillment/pick-pack-ship`, `/fulfillment/pick-pack-ship/:orderId` | Partial | 18% |
| UI-032 | Partial Fulfillment and Backorder Management | `/fulfillment/partial-backorders`, `/fulfillment/partial-backorders/:orderId` | Partial | 18% |
| UI-033 | Fulfillment Exception Management | `/fulfillment/exceptions`, `/fulfillment/exceptions/:orderId` | Partial | 18% |
| UI-034 | Order Fulfillment Status | `/fulfillment/order-status`, `/fulfillment/order-status/:orderId` | Partial | 18% |
| UI-035 | Multi-Location Split Fulfillment Planner | `/fulfillment/split-planner`, `/fulfillment/split-planner/:orderId` | Partial | 18% |
| UI-036 | Low-Stock Alert Review | `/procurement/low-stock-alerts` | Partial | 18% |
| UI-037 | Replenishment Planning | `/procurement/replenishment-planning` | Partial | 18% |
| UI-038 | Transfer Request | `/transfers/requests`, `/transfers/requests/new`, `/transfers/requests/:transferId` | Partial | 18% |
| UI-039 | Transfer Approval Queue | `/transfers/approvals`, `/transfers/approvals/:transferId` | Partial | 18% |
| UI-040 | Transfer Execution and In-Transit Tracking | `/transfers/execution`, `/transfers/execution/:transferId` | Partial | 18% |
| UI-041 | Network Rebalancing Analysis | `/transfers/network-rebalancing` | Partial | 18% |
| UI-042 | Return Authorization Management | `/returns/authorizations`, `/returns/authorizations/new`, `/returns/authorizations/:returnAuthorizationId` | Partial | 18% |
| UI-043 | Return Inspection and Disposition | `/returns/inspection-disposition`, `/returns/inspection-disposition/:returnId` | Partial | 18% |
| UI-044 | Operational Reports and Analytics | `/reports/operational` | Partial | 18% |
| UI-045 | Inventory Valuation Reconciliation | `/reports/valuation-reconciliation` | Partial | 18% |
| UI-046 | Promotional Stock Readiness | `/reports/promotional-readiness` | Partial | 18% |
| UI-047 | Audit and Control Review Workspace | `/reports/audit-workspace` | Partial | 18% |
| UI-048 | Audit Trail Query | `/reports/audit-trail` | Partial | 18% |
| UI-049 | User Account Management | `/admin/users`, `/admin/users/new`, `/admin/users/:userId` | Partial | 18% |
| UI-050 | Role and Access Control Administration | `/admin/roles-access` | Partial | 18% |

---

## Per-Screen Detail

### UI-001 — Sign In / Session Entry

| Field | Detail |
|-------|--------|
| **Expected route** | `/auth/sign-in` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `SignInPage`, `SuccessWarningErrorBannerComponent` · **Expected (SRS):** `SignInPageComponent`, `SignInFormComponent`, `SessionContextPanelComponent`, `GlobalHeader`, `ValidationMessageBlock` |
| **Missing UI elements** | Environment indicator; help link; remember-session checkbox; Forgot Password / Need Help actions; footer version and security notice; session context panel post-login |
| **Missing functionality** | `GET /api/v1/auth/session` integration; `POST /api/v1/auth/logout`; SSO/IdP auth; password recovery flow; session context service; location/role scope selection at login |
| **Completion** | **52%** |

---

### UI-002 — Operational Home Dashboard

| Field | Detail |
|-------|--------|
| **Expected route** | `/home/operations` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `OperationalDashboardPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent`, `KpiSummaryCardComponent`, `QuickActionTileComponent`, `TaskApprovalShortcutWidgetComponent` · **Expected:** `DashboardKpiGridComponent`, `StockHealthBoardComponent`, `AlertSummaryWidgetComponent`, `QuickActionsPanelComponent`, `MyTasksWidgetComponent`, `FilterBar`, `SummaryStatisticStrip`, `DataTable` |
| **Missing UI elements** | Dashboard filter bar (location, date range, role scope); recent alerts table; pending tasks table; View Alerts / Open Approvals / Refresh action buttons; last-refreshed footer timestamp |
| **Missing functionality** | `DashboardFacade` / API services (`API-150`, `151`, `152`, `158`); live refresh; role-based quick links; permission checks (`PERM-083`, `PERM-085`, `PERM-064`); alert snapshot data binding beyond static task widget |
| **Completion** | **48%** |

---

### UI-003 — Executive KPI Dashboard

| Field | Detail |
|-------|--------|
| **Expected route** | `/reports/executive-kpis` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `ExecutiveKpiDashboardPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ExecutiveKpiHeaderComponent`, `KpiCardGridComponent`, `TrendAnalysisPanelComponent`, `KpiDrilldownPanelComponent`, `KpiSummaryCard`, `TrendIndicator`, `DateRangePicker`, `ExportActionGroup`, `DrillDownLinkGroup` |
| **Missing UI elements** | Reporting period selector; export option; executive KPI cards with target comparison; trend summaries; variance indicators; drill-down panels; KPI summary table; Apply Filters / Export Dashboard actions; data-as-of footer |
| **Missing functionality** | `ExecutiveKpiFacade`, `ExecutiveKpiApiService`; `GET /api/v1/intelligence/kpis`; date-range filter state; drill-down navigation; export; `PERM-088` enforcement |
| **Completion** | **20%** |

---

### UI-004 — Notification Center

| Field | Detail |
|-------|--------|
| **Expected route** | `/notifications` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `NotificationCenterPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `NotificationQueueComponent`, `AlertDetailDrawerComponent`, `NotificationFiltersComponent`, `PendingApprovalsSummaryComponent`, `QueueList`, `AlertDetailCard`, `BulkSelectionToolbar`, `SavedViewSelector` |
| **Missing UI elements** | Unread count header; inbox layout with filter panel; notification detail pane; filter controls (type, priority, module, status, date); notification list table; Open Related Record / Mark as Handled / Acknowledge / Refresh actions |
| **Missing functionality** | Alert acknowledge API; pending approvals aggregation; transfer/adjustment/inbound-delay/campaign readiness feeds; global unread count sync; bulk actions; saved views |
| **Completion** | **20%** |

---

### UI-005 — Product Catalog Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/products/catalog`, `/products/catalog/new`, `/products/catalog/:sku` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `ProductCatalogPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ProductSearchPanelComponent`, `ProductListComponent`, `ProductDetailPanelComponent`, `ProductEditorComponent`, `ProductLifecycleActionsComponent`, `DataTable`, `DetailPanel`, `StandardFormSection`, `StatusBadge`, `GlobalSearchBar` |
| **Missing UI elements** | Search/filter toolbar; product catalog table; product detail panel; product form (SKU, name, UOM, category, lifecycle); Create Product CTA; Edit / Save / Change Status / Resolve Duplicate actions; record metadata footer |
| **Missing functionality** | Product CRUD APIs (`API-001`–`005`, `008`, `009`); create/edit routes; lifecycle status changes; duplicate resolution; search and pagination; permissions `PERM-001`–`005` |
| **Completion** | **18%** |

---

### UI-006 — Product Import Workspace

| Field | Detail |
|-------|--------|
| **Expected route** | `/products/import` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `ProductImportWorkspacePage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ImportUploadStepComponent`, `ImportValidationResultsComponent`, `ImportReviewStepComponent`, `ImportCompletionStepComponent`, `StepProgressIndicator`, `FileUploadControl`, `ReadOnlyReviewForm` |
| **Missing UI elements** | Multi-step import wizard; template download; upload zone; validation results table; completion summary; import instructions link |
| **Missing functionality** | `POST /api/v1/products/import`; opening balances; location activation; workflow store for import state; error row review and approval |
| **Completion** | **18%** |

---

### UI-007 — Location and Warehouse Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/locations`, `/locations/new`, `/locations/:locationCode` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `LocationManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `LocationDirectoryComponent`, `LocationDetailComponent`, `LocationHierarchyEditorComponent`, `StoragePositionManagerComponent`, `LocationStatusActionsComponent`, `DataTable`, `DetailPanel`, `ToggleSwitchControl`, `ConfirmationDialog` |
| **Missing UI elements** | Location directory table; hierarchy editor; storage position manager; activate/deactivate/close actions; location detail panel; status indicators |
| **Missing functionality** | Location CRUD and hierarchy APIs (`API-011`–`019`, `021`); storage position management; operational status; detail routes |
| **Completion** | **18%** |

---

### UI-008 — Stock Policy and Threshold Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/products/stock-policies`, `/products/stock-policies/:locationCode/:sku` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `StockPolicyManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PolicySearchFormComponent`, `PolicyDetailComponent`, `ThresholdEditorComponent`, `FilterBar`, `NumberInput`, `ReadOnlyReviewForm` |
| **Missing UI elements** | Policy search form; threshold editor (reorder level, safety stock, min threshold); policy detail view; save/cancel actions |
| **Missing functionality** | Stock policy APIs (`API-038`–`040`); location/SKU parameterized routes; policy create/update |
| **Completion** | **18%** |

---

### UI-009 — ABC Classification Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/products/abc-classification` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `AbcClassificationPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ClassificationReviewGridComponent`, `ClassificationEditorComponent`, `BulkClassificationToolbarComponent`, `DataTable`, `BulkSelectionToolbar`, `StatusBadge` |
| **Missing UI elements** | Classification review grid; bulk classification toolbar; ABC assignment editor; annual value display |
| **Missing functionality** | `PUT /api/v1/products/{sku}/abc-classification`; bulk edit; product search integration |
| **Completion** | **18%** |

---

### UI-010 — Governance Policies and Reason Codes

| Field | Detail |
|-------|--------|
| **Expected route** | `/governance/policies`, `/governance/reason-codes` |
| **Implemented?** | **Partial** (policies route only; `/governance/reason-codes` missing) |
| **Related component(s)** | **Implemented:** `GovernancePoliciesPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PolicyVersionListComponent`, `PolicyEditorComponent`, `ReasonCodeListComponent`, `ReasonCodeEditorComponent`, `ThresholdsTabComponent`, `TolerancesTabComponent`, `TabsSegmentedContentSwitcher` |
| **Missing UI elements** | Tabbed policy/reason-code interface; policy version list; reason code list/editor; approval thresholds tab; receipt tolerances tab; retire reason code action |
| **Missing functionality** | Governance APIs (`API-022`–`030`); reason-code route; policy version management; threshold/tolerance editing |
| **Completion** | **18%** |

---

### UI-011 — Supplier Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/procurement/suppliers`, `/procurement/suppliers/new`, `/procurement/suppliers/:supplierCode` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `SupplierManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `SupplierListComponent`, `SupplierDetailComponent`, `SupplierEditorComponent`, `DataTable`, `DetailPanel`, `StatusBadge` |
| **Missing UI elements** | Supplier list table; supplier detail panel; create/edit form; deactivate action |
| **Missing functionality** | Supplier APIs (`API-049`–`053`); CRUD workflows; detail routes |
| **Completion** | **18%** |

---

### UI-012 — Purchase Order Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/procurement/purchase-orders`, `/procurement/purchase-orders/new`, `/procurement/purchase-orders/:purchaseOrderId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `PurchaseOrderManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PurchaseOrderListComponent`, `PurchaseOrderEditorComponent`, `PurchaseOrderDetailComponent`, `ExpectedDeliveriesPanelComponent`, `LineItemEditor`, `StatusTimeline` |
| **Missing UI elements** | PO list table; multi-line PO editor; expected deliveries panel; amend/cancel actions; approval status timeline |
| **Missing functionality** | PO APIs (`API-059`–`063`, `065`, `161`); create/amend/cancel; receipt validation link |
| **Completion** | **18%** |

---

### UI-013 — Purchase Requisition Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/procurement/requisitions`, `/procurement/requisitions/:requisitionId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `PurchaseRequisitionManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `RequisitionQueueComponent`, `RequisitionDetailComponent`, `RequisitionApprovalPanelComponent`, `ConvertToPoPanelComponent`, `QueueList`, `ApprovalDecisionPanel` |
| **Missing UI elements** | Requisition queue; detail view; approval panel; convert-to-PO panel |
| **Missing functionality** | Requisition APIs (`API-054`–`058`); approve/reject/convert workflows; list endpoint gap (SRS C-03) |
| **Completion** | **18%** |

---

### UI-014 — Inbound Delivery Planning

| Field | Detail |
|-------|--------|
| **Expected route** | `/procurement/inbound-delivery-planning` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `InboundDeliveryPlanningPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `InboundCalendarComponent`, `DeliveryScheduleEditorComponent`, `InboundDelayPanelComponent`, `DateField`, `FilterBar`, `AlertDetailCard` |
| **Missing UI elements** | Inbound calendar view; delivery schedule editor; inbound delay panel |
| **Missing functionality** | Expected delivery APIs (`API-064`, `162`, `163`); calendar filter state |
| **Completion** | **18%** |

---

### UI-015 — Goods Receipt Workbench

| Field | Detail |
|-------|--------|
| **Expected route** | `/inbound/goods-receipts`, `/inbound/goods-receipts/:goodsReceiptId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `GoodsReceiptWorkbenchPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ReceiptQueueComponent`, `ReceiptLineVerificationComponent`, `ReceiptLotCaptureComponent`, `QueueList`, `LineItemEditor`, `StepProgressIndicator` |
| **Missing UI elements** | Receipt queue; line verification grid; lot/shelf-life capture; verify/complete actions |
| **Missing functionality** | Goods receipt APIs (`API-065`–`069`); PO validation; receipt workflow store |
| **Completion** | **18%** |

---

### UI-016 — Receipt Discrepancy Resolution

| Field | Detail |
|-------|--------|
| **Expected route** | `/inbound/discrepancies`, `/inbound/goods-receipts/:goodsReceiptId/discrepancies` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `ReceiptDiscrepancyResolutionPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `DiscrepancyListComponent`, `DiscrepancyEditorComponent`, `DiscrepancyResolutionPanelComponent`, `ComparisonPanel`, `VarianceHighlightBlock`, `EvidenceAttachmentPanel`, `ApprovalDecisionPanel` |
| **Missing UI elements** | Discrepancy list; expected vs. received comparison; resolution panel; evidence attachment |
| **Missing functionality** | Discrepancy APIs (`API-070`–`072`); tolerance validation; reason code lookup |
| **Completion** | **18%** |

---

### UI-017 — Put-Away Workbench

| Field | Detail |
|-------|--------|
| **Expected route** | `/inbound/put-away`, `/inbound/put-away/:goodsReceiptId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `PutAwayWorkbenchPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PendingPutAwayQueueComponent`, `StoragePositionSelectorComponent`, `PutAwayConfirmationPanelComponent`, `QueueList`, `DropdownSelectControl`, `ConfirmationDialog` |
| **Missing UI elements** | Pending put-away queue; storage position selector; confirmation panel |
| **Missing functionality** | Put-away APIs (`API-074`, `073`); storage position lookup; task completion |
| **Completion** | **18%** |

---

### UI-018 — Non-PO and Return Receipt Intake

| Field | Detail |
|-------|--------|
| **Expected route** | `/inbound/non-po-receipts` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `NonPoReturnReceiptIntakePage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ReceiptTypeSelectorComponent`, `AdHocReceiptFormComponent`, `ReturnReceiptFormComponent`, `RadioGroupSegmentedChoice`, `StandardFormSection` |
| **Missing UI elements** | Receipt type selector (ad-hoc vs. return); ad-hoc receipt form; return receipt form with RMA reference |
| **Missing functionality** | `POST /api/v1/inbound/ad-hoc-receipts`; `POST /api/v1/inbound/return-receipts` |
| **Completion** | **18%** |

---

### UI-019 — Inbound Supply Tracking

| Field | Detail |
|-------|--------|
| **Expected route** | `/procurement/inbound-supply-tracking` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `InboundSupplyTrackingPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `OpenPurchaseOrdersBoardComponent`, `InboundCalendarPanelComponent`, `InboundDelaysPanelComponent`, `InTransitStockPanelComponent`, `FilterBar`, `DateRangePicker`, `DataTable` |
| **Missing UI elements** | Open PO board; inbound calendar; delays panel; in-transit stock panel |
| **Missing functionality** | PO list/detail; inbound calendar/delay APIs; in-transit transfer visibility |
| **Completion** | **18%** |

---

### UI-020 — Inventory Status Monitor

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/status-monitor` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `InventoryStatusMonitorPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `StockStatusSummaryComponent`, `StockStatusBoardComponent`, `InventoryFiltersComponent`, `StockPositionDetailDrawerComponent`, `FilterBar`, `SavedViewSelector`, `DataTable`, `KpiSummaryCard`, `DrillDownLinkGroup` |
| **Missing UI elements** | Stock status summary KPIs; status board (on-hand, ATP, low-stock, quarantine); filter bar; saved views; stock position detail drawer |
| **Missing functionality** | Stock position/status APIs (`API-033`, `034`, `037`, `151`, `152`); drill-down; location filtering |
| **Completion** | **18%** |

---

### UI-021 — Inventory Availability Inquiry

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/availability` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `InventoryAvailabilityInquiryPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `AvailabilitySearchFormComponent`, `AvailabilityResultComponent`, `NetworkAvailabilityPanelComponent`, `InquiryHistoryPanelComponent`, `GlobalSearchBar`, `SearchResultsList`, `DetailPanel` |
| **Missing UI elements** | Product search form; ATP result display; network availability panel; inquiry history |
| **Missing functionality** | Availability APIs (`API-035`, `036`, `153`); order availability check; inquiry logging |
| **Completion** | **18%** |

---

### UI-022 — Inventory Movement History

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/movement-history` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `InventoryMovementHistoryPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `MovementFiltersComponent`, `MovementResultsTableComponent`, `MovementDetailDrawerComponent`, `FilterBar`, `DateRangePicker`, `DataTable`, `ExportActionGroup`, `AuditRecordViewer` |
| **Missing UI elements** | Movement filter bar; results table; detail drawer; export actions |
| **Missing functionality** | `GET /api/v1/intelligence/movements`; query/export; audit record drill-down |
| **Completion** | **18%** |

---

### UI-023 — Cycle Count Workbench

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/cycle-counts`, `/inventory/cycle-counts/:cycleCountId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `CycleCountWorkbenchPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `CycleCountQueueComponent`, `CycleCountTaskComponent`, `CycleCountSubmissionComponent`, `QueueList`, `NumberInput`, `SessionContextBadge` |
| **Missing UI elements** | Assigned count queue; blind count entry form; submission confirmation |
| **Missing functionality** | Cycle count APIs (`API-108`–`111`, `168`); count result submission |
| **Completion** | **18%** |

---

### UI-024 — Physical Inventory Count Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/physical-counts`, `/inventory/physical-counts/:physicalCountId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `PhysicalInventoryCountManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PhysicalCountSessionComponent`, `FreezeStatusBannerComponent`, `CountProgressBoardComponent`, `CertificationPanelComponent`, `SummaryStatisticStrip`, `StatusTimeline`, `ConfirmationDialog` |
| **Missing UI elements** | Count session manager; location freeze banner; team progress board; certification checklist |
| **Missing functionality** | Physical count APIs (`API-112`–`115`); freeze status (`API-020`); certify workflow |
| **Completion** | **18%** |

---

### UI-025 — Variance Investigation and Approval

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/variances`, `/inventory/variances/:caseId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `VarianceInvestigationApprovalPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `VarianceCaseQueueComponent`, `VarianceInvestigationFormComponent`, `VarianceComparisonPanelComponent`, `VarianceApprovalPanelComponent`, `QueueList`, `ComparisonPanel`, `ApprovalDecisionPanel`, `EvidenceAttachmentPanel` |
| **Missing UI elements** | Variance case queue; investigation notes form; system vs. physical comparison; independent approval panel |
| **Missing functionality** | Adjustment case APIs (`API-116`–`119`, `123`); SoD enforcement; evidence attachment |
| **Completion** | **18%** |

---

### UI-026 — Stock Adjustment Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/adjustments`, `/inventory/adjustments/:caseId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `StockAdjustmentManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `AdjustmentRequestFormComponent`, `AdjustmentCaseDetailComponent`, `AdjustmentSubmissionPanelComponent`, `StandardFormSection`, `LineItemEditor`, `TextAreaNotesField` |
| **Missing UI elements** | Adjustment request form with mandatory reason code; case detail; submission/approval panel |
| **Missing functionality** | Adjustment case APIs (`API-116`–`122`); reason code lookup; approval threshold routing |
| **Completion** | **18%** |

---

### UI-027 — Write-Off Authorization

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/write-offs`, `/inventory/write-offs/:caseId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `WriteOffAuthorizationPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `WriteOffCaseQueueComponent`, `WriteOffReviewComponent`, `FinanceAcknowledgementPanelComponent`, `WriteOffDecisionPanelComponent`, `ReadOnlyReviewForm`, `ApprovalDecisionPanel`, `EvidenceAttachmentPanel` |
| **Missing UI elements** | Write-off case queue; evidence review; finance acknowledgement; approve/reject decision panel |
| **Missing functionality** | Write-off approval workflow via adjustment case APIs; multi-level authorization |
| **Completion** | **18%** |

---

### UI-028 — Quarantine and Hold Register

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/quarantine` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `QuarantineHoldRegisterPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `QuarantineRegisterTableComponent`, `HoldActionPanelComponent`, `ReleaseHoldDialogComponent`, `DataTable`, `RadioGroupSegmentedChoice`, `ConfirmationDialog` |
| **Missing UI elements** | Quarantine register table; apply/release hold actions; non-sellable quantity display |
| **Missing functionality** | Quarantine hold APIs (`API-045`, `046`, `154`); hold lifecycle management |
| **Completion** | **18%** |

---

### UI-029 — Shrinkage, Loss, and Obsolescence Analysis

| Field | Detail |
|-------|--------|
| **Expected route** | `/inventory/shrinkage-obsolescence` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `ShrinkageAnalysisPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ShrinkageKpiPanelComponent`, `TrendAnalysisTableComponent`, `ObsolescenceBreakdownComponent`, `KpiSummaryCard`, `DateRangePicker`, `ReportViewer`, `TrendIndicator`, `ExportActionGroup` |
| **Missing UI elements** | Shrinkage KPI panel; trend analysis table; obsolescence breakdown; report viewer |
| **Missing functionality** | `GET /api/v1/intelligence/accuracy/shrinkage`; analytical filters; export |
| **Completion** | **18%** |

---

### UI-030 — Order Reservation Workbench

| Field | Detail |
|-------|--------|
| **Expected route** | `/fulfillment/reservations`, `/fulfillment/reservations/:orderId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `OrderReservationWorkbenchPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `OrderSearchQueueComponent`, `OrderReservationDetailComponent`, `AvailabilityCheckPanelComponent`, `ReservationActionsPanelComponent`, `QueueList`, `LineItemEditor`, `StatusTimeline` |
| **Missing UI elements** | Order search queue; availability check panel; reserve/release/confirm actions |
| **Missing functionality** | Order and reservation APIs (`API-081`, `084`–`086`, `043`, `044`); ring-fence check |
| **Completion** | **18%** |

---

### UI-031 — Pick, Pack, and Ship Workbench

| Field | Detail |
|-------|--------|
| **Expected route** | `/fulfillment/pick-pack-ship`, `/fulfillment/pick-pack-ship/:orderId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `PickPackShipWorkbenchPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PickQueueComponent`, `PickVerificationComponent`, `PackingPanelComponent`, `ShipmentConfirmationPanelComponent`, `QueueList`, `StepProgressIndicator` |
| **Missing UI elements** | Location pick queue; pick verification; packing panel; shipment confirmation |
| **Missing functionality** | Pick/pack/ship APIs (`API-088`–`092`); lot breakdown; location-level queue (SRS API gap C-01) |
| **Completion** | **18%** |

---

### UI-032 — Partial Fulfillment and Backorder Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/fulfillment/partial-backorders`, `/fulfillment/partial-backorders/:orderId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `PartialFulfillmentBackorderPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PartialFulfillmentEditorComponent`, `BackorderDecisionPanelComponent`, `BackorderListComponent`, `ComparisonPanel`, `LineItemEditor`, `StatusTimeline` |
| **Missing UI elements** | Partial fulfillment quantity editor; backorder decision panel; backorder list |
| **Missing functionality** | Partial fulfillment/backorder APIs (`API-093`–`095`, `164`); customer acknowledgment workflow |
| **Completion** | **18%** |

---

### UI-033 — Fulfillment Exception Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/fulfillment/exceptions`, `/fulfillment/exceptions/:orderId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `FulfillmentExceptionManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ExceptionQueueComponent`, `ExceptionDetailComponent`, `ExceptionResolutionFormComponent`, `QueueList`, `AlertDetailCard` |
| **Missing UI elements** | Exception queue; detail view; resolution form with routing options |
| **Missing functionality** | Exception APIs (`API-096`, `165`); quarantine routing on resolution |
| **Completion** | **18%** |

---

### UI-034 — Order Fulfillment Status

| Field | Detail |
|-------|--------|
| **Expected route** | `/fulfillment/order-status`, `/fulfillment/order-status/:orderId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `OrderFulfillmentStatusPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `OrderStatusSearchComponent`, `OrderStatusDetailComponent`, `ReservationShipmentTimelineComponent`, `BackorderSummaryTabComponent`, `SearchResultsList`, `StatusTimeline`, `TabsSegmentedContentSwitcher` |
| **Missing UI elements** | Order status search; detail with reservation/pick/pack/ship timeline; backorder summary tab |
| **Missing functionality** | Order status APIs (`API-082`, `083`, `097`, `177`); sales integration feed |
| **Completion** | **18%** |

---

### UI-035 — Multi-Location Split Fulfillment Planner

| Field | Detail |
|-------|--------|
| **Expected route** | `/fulfillment/split-planner`, `/fulfillment/split-planner/:orderId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `MultiLocationSplitFulfillmentPlannerPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `NetworkAvailabilityPanelComponent`, `SplitPlanEditorComponent`, `SourceLocationAllocationGridComponent`, `ComparisonPanel`, `ReadOnlyReviewForm` |
| **Missing UI elements** | Network availability panel; split plan editor; source location allocation grid |
| **Missing functionality** | Multi-location plan API (`API-087`); network availability (`API-036`); plan submission |
| **Completion** | **18%** |

---

### UI-036 — Low-Stock Alert Review

| Field | Detail |
|-------|--------|
| **Expected route** | `/procurement/low-stock-alerts` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `LowStockAlertReviewPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `AlertQueueComponent`, `AlertDetailPanelComponent`, `RecommendationPanelComponent`, `QueueList`, `AlertDetailCard`, `SavedViewSelector`, `BulkSelectionToolbar` |
| **Missing UI elements** | Alert queue with priority; alert detail panel; replenishment recommendation panel; acknowledge action |
| **Missing functionality** | Alert APIs (`API-158`, `159`, `160`); stock status/policy context; bulk acknowledgement |
| **Completion** | **18%** |

---

### UI-037 — Replenishment Planning

| Field | Detail |
|-------|--------|
| **Expected route** | `/procurement/replenishment-planning` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `ReplenishmentPlanningPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `RecommendationListComponent`, `TransferBeforeBuyPanelComponent`, `RequisitionDraftPanelComponent`, `RecommendationCard`, `AlertDetailCard` |
| **Missing UI elements** | Replenishment recommendation list; transfer-before-buy comparison; requisition draft panel |
| **Missing functionality** | Replenishment recommendation API (`API-160`); requisition creation; network imbalance review |
| **Completion** | **18%** |

---

### UI-038 — Transfer Request

| Field | Detail |
|-------|--------|
| **Expected route** | `/transfers/requests`, `/transfers/requests/new`, `/transfers/requests/:transferId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `TransferRequestPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `TransferRequestFormComponent`, `TransferCapacityPanelComponent`, `TransferRequestDetailComponent`, `LineItemEditor`, `NumberInput`, `StatusTimeline` |
| **Missing UI elements** | Transfer request form (source, destination, SKU, qty); capacity panel; justification notes |
| **Missing functionality** | Transfer APIs (`API-098`–`100`, `042`); capacity validation; create/detail routes |
| **Completion** | **18%** |

---

### UI-039 — Transfer Approval Queue

| Field | Detail |
|-------|--------|
| **Expected route** | `/transfers/approvals`, `/transfers/approvals/:transferId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `TransferApprovalQueuePage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PendingTransferQueueComponent`, `TransferApprovalDetailComponent`, `TransferDecisionPanelComponent`, `QueueList`, `ApprovalDecisionPanel`, `ComparisonPanel` |
| **Missing UI elements** | Pending transfer queue; approval detail with capacity impact; approve/reject panel |
| **Missing functionality** | Transfer approval APIs (`API-101`, `102`, `106`); SoD and capacity checks |
| **Completion** | **18%** |

---

### UI-040 — Transfer Execution and In-Transit Tracking

| Field | Detail |
|-------|--------|
| **Expected route** | `/transfers/execution`, `/transfers/execution/:transferId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `TransferExecutionTrackingPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `TransferExecutionQueueComponent`, `DispatchPanelComponent`, `ReceivePanelComponent`, `InTransitBoardComponent`, `QueueList`, `SummaryStatisticStrip` |
| **Missing UI elements** | Execution queue; dispatch panel; receive panel; in-transit board |
| **Missing functionality** | Dispatch/receive/cancel APIs (`API-103`–`105`, `107`); in-transit monitoring |
| **Completion** | **18%** |

---

### UI-041 — Network Rebalancing Analysis

| Field | Detail |
|-------|--------|
| **Expected route** | `/transfers/network-rebalancing` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `NetworkRebalancingAnalysisPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ImbalanceHeatmapComponent`, `RecommendationListComponent`, `RebalanceActionPanelComponent`, `RecommendationCard`, `FilterBar`, `DrillDownLinkGroup` |
| **Missing UI elements** | Network imbalance heatmap/visualization; recommendation list; rebalance action panel |
| **Missing functionality** | Network imbalance API (`API-166`); recommendation-to-transfer workflow |
| **Completion** | **18%** |

---

### UI-042 — Return Authorization Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/returns/authorizations`, `/returns/authorizations/new`, `/returns/authorizations/:returnAuthorizationId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `ReturnAuthorizationManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ReturnAuthorizationSearchComponent`, `ReturnAuthorizationFormComponent`, `ReturnAuthorizationDetailComponent`, `SearchResultsList`, `LineItemEditor`, `StatusTimeline` |
| **Missing UI elements** | Order lookup search; RA creation form; RA detail with eligibility validation |
| **Missing functionality** | Return authorization APIs (`API-124`–`127`); order eligibility check; cancel RA |
| **Completion** | **18%** |

---

### UI-043 — Return Inspection and Disposition

| Field | Detail |
|-------|--------|
| **Expected route** | `/returns/inspection-disposition`, `/returns/inspection-disposition/:returnId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `ReturnInspectionDispositionPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PendingReturnReceiptsQueueComponent`, `ReturnInspectionFormComponent`, `DispositionDecisionPanelComponent`, `QueueList`, `StepProgressIndicator`, `RadioGroupSegmentedChoice` |
| **Missing UI elements** | Pending return receipts queue; condition inspection form; restock/quarantine/write-off disposition panel |
| **Missing functionality** | Return receive/inspect/disposition APIs (`API-128`–`131`); receive→inspect→disposition workflow |
| **Completion** | **18%** |

---

### UI-044 — Operational Reports and Analytics

| Field | Detail |
|-------|--------|
| **Expected route** | `/reports/operational` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `OperationalReportsAnalyticsPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ReportsCatalogComponent`, `ReportFiltersComponent`, `ReportViewerPanelComponent`, `DrilldownResultsPanelComponent`, `ReportViewer`, `FilterBar`, `DateRangePicker`, `ExportActionGroup` |
| **Missing UI elements** | Reports catalog; report filter panel; report viewer; drill-down results |
| **Missing functionality** | Multiple intelligence APIs (`API-150`–`155`, `167`, `168`); report selection; export |
| **Completion** | **18%** |

---

### UI-045 — Inventory Valuation Reconciliation

| Field | Detail |
|-------|--------|
| **Expected route** | `/reports/valuation-reconciliation` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `InventoryValuationReconciliationPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `ValuationSnapshotPanelComponent`, `ReconciliationComparisonPanelComponent`, `ThreeWayMatchStatusPanelComponent`, `InvoiceAuthorizationPanelComponent`, `ComparisonPanel`, `VarianceHighlightBlock`, `ReportViewer` |
| **Missing UI elements** | Valuation snapshot panel; operational vs. finance comparison; three-way match status; invoice authorization |
| **Missing functionality** | Valuation APIs (`API-171`, `172`); supplier invoice match (`API-077`–`080`); reconciliation workflow |
| **Completion** | **18%** |

---

### UI-046 — Promotional Stock Readiness

| Field | Detail |
|-------|--------|
| **Expected route** | `/reports/promotional-readiness` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `PromotionalStockReadinessPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `CampaignAllocationListComponent`, `CampaignAllocationEditorComponent`, `ReadinessAssessmentPanelComponent`, `RingFenceStatusPanelComponent`, `KpiSummaryCard`, `AlertDetailCard` |
| **Missing UI elements** | Campaign allocation list/editor; readiness assessment; ring-fence status panel |
| **Missing functionality** | Campaign APIs (`API-132`–`139`, `169`, `178`); readiness/release/override workflows |
| **Completion** | **18%** |

---

### UI-047 — Audit and Control Review Workspace

| Field | Detail |
|-------|--------|
| **Expected route** | `/reports/audit-workspace` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `AuditControlReviewWorkspacePage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `AuditScopeFormComponent`, `AuditPopulationResultsComponent`, `ControlTestChecklistComponent`, `AuditFindingsEditorComponent`, `StepProgressIndicator`, `ReportViewer`, `EvidenceAttachmentPanel` |
| **Missing UI elements** | Audit scope definition form; population results; control test checklist; findings editor |
| **Missing functionality** | Audit trail query/export (`API-156`, `157`); audit workflow store; findings documentation |
| **Completion** | **18%** |

---

### UI-048 — Audit Trail Query

| Field | Detail |
|-------|--------|
| **Expected route** | `/reports/audit-trail` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `AuditTrailQueryPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `AuditQueryFiltersComponent`, `AuditResultsTableComponent`, `AuditRecordDetailDrawerComponent`, `DateRangePicker`, `DataTable`, `AuditRecordViewer`, `ExportActionGroup` |
| **Missing UI elements** | Audit query filters (entity, date, user, action); results table; before/after detail drawer; export |
| **Missing functionality** | Audit trail APIs (`API-156`, `157`); immutable record inspection |
| **Completion** | **18%** |

---

### UI-049 — User Account Management

| Field | Detail |
|-------|--------|
| **Expected route** | `/admin/users`, `/admin/users/new`, `/admin/users/:userId` |
| **Implemented?** | **Partial** (base route only) |
| **Related component(s)** | **Implemented:** `UserAccountManagementPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `UserAccountListComponent`, `UserAccountDetailComponent`, `UserProvisioningFormComponent`, `RoleAssignmentPanelComponent`, `DataTable`, `RoleAssignmentWidget`, `AccessScopeSelector`, `GlobalSearchBar` |
| **Missing UI elements** | User account list table; provisioning form; role assignment panel; suspend/deactivate actions |
| **Missing functionality** | User APIs (`API-140`–`147`); role assignment; directory sync |
| **Completion** | **18%** |

---

### UI-050 — Role and Access Control Administration

| Field | Detail |
|-------|--------|
| **Expected route** | `/admin/roles-access` |
| **Implemented?** | **Partial** |
| **Related component(s)** | **Implemented:** `RoleAccessControlAdministrationPage`, `PageTitleBarComponent`, `BreadcrumbTrailComponent` · **Expected:** `PermissionMatrixViewComponent`, `RoleScopeRulesPanelComponent`, `AuthorizationEvaluationPanelComponent`, `LocationScopeValidationPanelComponent`, `PermissionMatrix`, `AccessScopeSelector`, `TabsSegmentedContentSwitcher` |
| **Missing UI elements** | Permission matrix view; role scope rules panel; authorization evaluation tester; location scope validation panel |
| **Missing functionality** | SoD evaluation (`API-031`); action authorization (`API-148`); location scope validation (`API-149`); session context |
| **Completion** | **18%** |

---

## Shared Component Coverage (C-001–C-060)

The specification defines 60 reusable components. The project **scaffolds all 60** as standalone files under `shared/ui/`, but most are **shell stubs** (minimal template, not integrated into feature pages).

| Integration Status | Count | Notes |
|--------------------|-------|-------|
| Wired into app shell (global) | 8 | C-001–C-003, C-006–C-009 (header, nav, footer, search, notifications, user menu, session badge) |
| Wired into UI-002 dashboard | 3 | C-010, C-011 (partial), C-016 |
| Wired into UI-001 | 1 | C-037 SuccessWarningErrorBanner (partial) |
| Scaffolded but not used in feature pages | ~48 | Present as files; `ng-content` placeholders or minimal markup |
| Not implemented at all | 0 | All C-001–C-060 files exist |

---

## Route Coverage Gap Summary

| Gap Type | Spec Count | Implemented | Gap |
|----------|------------|-------------|-----|
| Base list/index routes | 50 | 50 | 0 |
| `/new` create routes | 8 | 0 | 8 |
| `/:id` detail routes | ~27 | 0 | ~27 |
| Nested child routes | 2 | 0 | 2 |
| Alternate governance route | 1 (`/governance/reason-codes`) | 0 | 1 |

---

## Recommended Priority Order

Based on coverage gaps and business criticality from the SRS:

1. **UI-001, UI-002** — Complete authentication shell and operational landing (highest partial completion)
2. **UI-005, UI-007, UI-020** — Master data and inventory visibility foundations
3. **UI-015, UI-017, UI-030, UI-031** — Core inbound and fulfillment workbenches
4. **UI-025, UI-026, UI-039** — Approval queues with SoD controls
5. **UI-049, UI-050** — Administration and access control
6. Remaining Tier C screens in domain priority order

---

## Document References

| Document | Path |
|----------|------|
| UI Screen Catalog | `SRS/Inventory-Management-System-SRS.md` § UI-001–UI-050 |
| Wireframe Specifications | `SRS/Inventory-Management-System-SRS.md` § UI wireframes |
| Screen-to-Architecture Mapping | `SRS/Inventory-Management-System-SRS.md` § Screen-to-Architecture Mapping |
| Component Inventory | `SRS/Inventory-Management-System-SRS.md` § C-001–C-060 |
| Implemented routes | `ims-frontend/src/app/app.routes.ts` |
| Architecture report | `gap_frontend/Project-Architecture-Report.md` |

---

*End of matrix.*
