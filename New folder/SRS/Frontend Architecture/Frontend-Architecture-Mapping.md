# Inventory Management System Frontend Architecture Mapping

## Purpose
This document maps the approved UI design, API design, domain model, and system architecture into a clean Angular frontend architecture. It focuses on feature decomposition, module boundaries, routing, services, DTO usage, and state ownership. It intentionally does not generate Angular code.

## Frontend Architecture Principles
- Organize the Angular app by business capability, not by technical artifact type.
- Mirror the approved bounded contexts and system modules in the frontend feature structure.
- Keep route-level pages thin; move orchestration into facades and application services.
- Prefer standalone routed features or lazy-loaded feature areas with clear public entry points.
- Separate `core`, `shared`, and `features` concerns:
  - `core`: app shell, auth/session, guards, interceptors, global layout, permission evaluation.
  - `shared`: reusable UI components, pipes, directives, presentational widgets, common DTO mappers.
  - `features`: business workflows aligned to modules such as inventory, procurement, inbound, fulfillment, and administration.
- Use a facade-first UI architecture:
  - components handle rendering and user interaction
  - facades coordinate page state and commands
  - API services encapsulate HTTP contracts
  - mappers adapt DTOs into frontend view models
- Keep state ownership explicit:
  - global state only for session, navigation context, notification counts, and app-wide preferences
  - feature state for work queues, filters, selected records, wizard progress, and long-running workflows
  - transient form state stays local to the page or child form components

## Recommended State Management Strategy
- Use Angular Signals for simple shared UI state and session context.
- Use `ComponentStore` or a feature-scoped signal store for page/workbench state.
- Reserve NgRx-style global state only for truly cross-application concerns:
  - authenticated session and user context
  - permission catalog and location scope
  - notification/task counts
  - shell navigation state
- Treat server data as query-driven state behind facades with caching per feature.
- Avoid a single monolithic global store for all CRUD screens.

## Recommended Angular Project Structure
```text
src/app/
  core/
    application/
      auth/
      authorization/
      session/
      navigation/
      notifications/
    guards/
    http/
    layout/
    shell/
    config/
  shared/
    ui/
      layout/
      tables/
      filters/
      forms/
      feedback/
      workflow/
      audit/
    directives/
    pipes/
    utils/
    models/
      common/
      view-models/
  features/
    home/
    products/
      catalog/
      import/
      abc-classification/
      stock-policies/
    locations/
    governance/
    procurement/
      suppliers/
      requisitions/
      purchase-orders/
      delivery-planning/
      supply-tracking/
      low-stock-alerts/
      replenishment/
    inbound/
      goods-receipts/
      discrepancies/
      put-away/
      ad-hoc-receipts/
    inventory/
      status-monitor/
      availability/
      movement-history/
      cycle-counts/
      physical-counts/
      variances/
      adjustments/
      write-offs/
      quarantine/
      shrinkage/
    fulfillment/
      reservations/
      pick-pack-ship/
      partial-fulfillment/
      exceptions/
      order-status/
      split-fulfillment/
    transfers/
      requests/
      approvals/
      execution/
      rebalancing/
    returns/
      authorizations/
      inspection/
    reports/
      operational/
      executive-kpis/
      valuation/
      promotional-readiness/
      audit/
    administration/
      users/
      roles-access/
  app.routes.ts
```

## Cross-Cutting Shared Components
Use these shared components consistently across the application:
- App shell and navigation: `GlobalHeader`, `MainNavigationBar`, `SecondaryNavigationPanel`, `BreadcrumbTrail`, `PageTitleBar`, `SessionContextBadge`
- Querying and list management: `FilterBar`, `DateRangePicker`, `SavedViewSelector`, `DataTable`, `RowActionMenu`, `DetailPanel`, `QueueList`
- Workflow and feedback: `StepProgressIndicator`, `ApprovalDecisionPanel`, `StatusTimeline`, `ConfirmationDialog`, `SuccessWarningErrorBanner`, `EmptyStatePanel`, `LoadingSkeleton`
- Forms and auditability: `StandardFormSection`, `LineItemEditor`, `ValidationMessageBlock`, `RecordMetadataBlock`, `EvidenceAttachmentPanel`, `AuditRecordViewer`, `PermissionMatrix`

## Feature Module Map
- `home`
- `notifications`
- `products`
- `locations`
- `governance`
- `procurement`
- `inbound`
- `inventory`
- `fulfillment`
- `transfers`
- `returns`
- `reports`
- `administration`

## Screen-to-Architecture Mapping

### UI-001 Sign In / Session Entry
- Angular feature module: `core/auth`
- Main page component: `SignInPageComponent`
- Child components: `SignInFormComponent`, `SessionContextPanelComponent`
- Shared components: `GlobalHeader`, `ValidationMessageBlock`, `SuccessWarningErrorBanner`
- Required Angular services: `AuthFacade`, `SessionService`, `SessionContextService`
- Required DTOs: `SessionResponse`, `LogoutCommandResultResponse`
- Related API endpoints: `GET /api/v1/auth/session`, `POST /api/v1/auth/logout`
- Required permissions: authenticated session bootstrap only
- Application routes: `/auth/sign-in`
- State management responsibility: local form state plus global session state in `core/session`

### UI-002 Operational Home Dashboard
- Angular feature module: `home`
- Main page component: `OperationalDashboardPageComponent`
- Child components: `DashboardKpiGridComponent`, `StockHealthBoardComponent`, `AlertSummaryWidgetComponent`, `QuickActionsPanelComponent`, `MyTasksWidgetComponent`
- Shared components: `GlobalHeader`, `MainNavigationBar`, `KpiSummaryCard`, `SummaryStatisticStrip`, `QuickActionTile`, `TaskApprovalShortcutWidget`, `FilterBar`
- Required Angular services: `DashboardFacade`, `DashboardApiService`, `AlertApiService`, `TaskInboxService`
- Required DTOs: dashboard and stock-status summary responses from APIs `150`, `151`, `152`, `158`
- Related API endpoints: `GET /api/v1/intelligence/dashboard`, `GET /api/v1/intelligence/stock-status/summary`, `GET /api/v1/intelligence/stock-status/board`, `GET /api/v1/intelligence/alerts`
- Required permissions: `PERM-083`, `PERM-085`, `PERM-064`
- Application routes: `/home/operations`
- State management responsibility: feature dashboard state for filters, selected widgets, and refresh cadence

### UI-003 Executive KPI Dashboard
- Angular feature module: `reports`
- Main page component: `ExecutiveKpiDashboardPageComponent`
- Child components: `ExecutiveKpiHeaderComponent`, `KpiCardGridComponent`, `TrendAnalysisPanelComponent`, `KpiDrilldownPanelComponent`
- Shared components: `KpiSummaryCard`, `TrendIndicator`, `DateRangePicker`, `ExportActionGroup`, `DrillDownLinkGroup`
- Required Angular services: `ExecutiveKpiFacade`, `ExecutiveKpiApiService`
- Required DTOs: KPI dashboard query DTOs and `KpiReportResponse`
- Related API endpoints: `GET /api/v1/intelligence/kpis`
- Required permissions: `PERM-088`
- Application routes: `/reports/executive-kpis`
- State management responsibility: feature state for date range, KPI comparisons, and drill-down selection

### UI-004 Notification Center
- Angular feature module: `notifications`
- Main page component: `NotificationCenterPageComponent`
- Child components: `NotificationQueueComponent`, `AlertDetailDrawerComponent`, `NotificationFiltersComponent`, `PendingApprovalsSummaryComponent`
- Shared components: `NotificationIconInboxTrigger`, `QueueList`, `AlertDetailCard`, `BulkSelectionToolbar`, `SavedViewSelector`
- Required Angular services: `NotificationFacade`, `AlertApiService`, `TransferApprovalApiService`, `AdjustmentApprovalApiService`
- Required DTOs: alert list response, `CommandResultResponse`, pending approvals list responses
- Related API endpoints: `GET /api/v1/intelligence/alerts`, `POST /api/v1/intelligence/alerts/{alertId}/acknowledge`, `GET /api/v1/transfers/pending-approvals`, `GET /api/v1/accuracy/pending-approvals`, `GET /api/v1/intelligence/procurement/inbound-delays`, `GET /api/v1/intelligence/campaigns/readiness`
- Required permissions: `PERM-064`, `PERM-065`, plus queue permissions `PERM-072`, `PERM-044`, `PERM-046`, `PERM-036`, `PERM-092`
- Application routes: `/notifications`
- State management responsibility: global unread count in shell; feature queue/filter state in module store

### UI-005 Product Catalog Management
- Angular feature module: `products`
- Main page component: `ProductCatalogPageComponent`
- Child components: `ProductSearchPanelComponent`, `ProductListComponent`, `ProductDetailPanelComponent`, `ProductEditorComponent`, `ProductLifecycleActionsComponent`
- Shared components: `GlobalSearchBar`, `DataTable`, `DetailPanel`, `StandardFormSection`, `StatusBadge`, `RecordMetadataBlock`
- Required Angular services: `ProductCatalogFacade`, `ProductApiService`, `ProductFormService`
- Required DTOs: `SearchProductsQuery`, `GetProductBySkuRequest`, `CreateProductRequest`, `UpdateProductAttributesRequest`, `ChangeProductLifecycleStatusRequest`, `ProductSummaryResponse`, `ProductDetailResponse`, `ProductStatusChangeResponse`
- Related API endpoints: `POST /api/v1/products`, `GET /api/v1/products`, `GET /api/v1/products/{sku}`, `PATCH /api/v1/products/{sku}`, `POST /api/v1/products/{sku}/lifecycle-status`, `GET /api/v1/products/categories/{categoryCode}/products`, `POST /api/v1/products/duplicate-resolutions`
- Required permissions: `PERM-001`, `PERM-002`, `PERM-003`, `PERM-004`, `PERM-005`
- Application routes: `/products/catalog`, `/products/catalog/new`, `/products/catalog/:sku`
- State management responsibility: feature state for search filters, selected SKU, and edit/view mode; form state remains local

### UI-006 Product Import Workspace
- Angular feature module: `products`
- Main page component: `ProductImportWorkspacePageComponent`
- Child components: `ImportUploadStepComponent`, `ImportValidationResultsComponent`, `ImportReviewStepComponent`, `ImportCompletionStepComponent`
- Shared components: `StepProgressIndicator`, `FileUploadControl`, `ReadOnlyReviewForm`, `ValidationMessageBlock`, `SuccessWarningErrorBanner`
- Required Angular services: `ProductImportFacade`, `ProductImportApiService`, `OpeningBalanceApiService`, `LocationActivationApiService`
- Required DTOs: `BulkProductImportRequest`, opening-balance request DTOs, import result responses
- Related API endpoints: `POST /api/v1/products/import`, `POST /api/v1/inventory/opening-balances`, `POST /api/v1/locations/{locationCode}/activate`
- Required permissions: `PERM-015`, `PERM-010`, `PERM-007`
- Application routes: `/products/import`
- State management responsibility: workflow store for file, validation issues, approved rows, and completion outcome

### UI-007 Location and Warehouse Management
- Angular feature module: `locations`
- Main page component: `LocationManagementPageComponent`
- Child components: `LocationDirectoryComponent`, `LocationDetailComponent`, `LocationHierarchyEditorComponent`, `StoragePositionManagerComponent`, `LocationStatusActionsComponent`
- Shared components: `DataTable`, `DetailPanel`, `StandardFormSection`, `ConfirmationDialog`, `ToggleSwitchControl`, `RecordMetadataBlock`
- Required Angular services: `LocationFacade`, `LocationApiService`, `StoragePositionApiService`
- Required DTOs: location create/update requests, storage-position requests, `LocationSummaryResponse`, location detail responses
- Related API endpoints: `POST /api/v1/locations`, `GET /api/v1/locations`, `GET /api/v1/locations/{locationCode}`, `PATCH /api/v1/locations/{locationCode}/hierarchy`, `POST /api/v1/locations/{locationCode}/storage-positions`, `GET /api/v1/locations/{locationCode}/storage-positions`, `POST /api/v1/locations/{locationCode}/activate`, `POST /api/v1/locations/{locationCode}/deactivate`, `POST /api/v1/locations/{locationCode}/close`, `GET /api/v1/locations/{locationCode}/operational-status`
- Required permissions: `PERM-006`, `PERM-007`, `PERM-008`, `PERM-009`, `PERM-004`
- Application routes: `/locations`, `/locations/new`, `/locations/:locationCode`
- State management responsibility: feature state for selected location, hierarchy mode, storage-position tab, and status transition dialogs

### UI-008 Stock Policy and Threshold Management
- Angular feature module: `products`
- Main page component: `StockPolicyManagementPageComponent`
- Child components: `PolicySearchFormComponent`, `PolicyDetailComponent`, `ThresholdEditorComponent`
- Shared components: `FilterBar`, `NumberInput`, `DateField`, `ValidationMessageBlock`, `ReadOnlyReviewForm`
- Required Angular services: `StockPolicyFacade`, `StockPolicyApiService`
- Required DTOs: stock-policy create/get/update DTOs and stock-policy response DTOs
- Related API endpoints: `POST /api/v1/inventory/stock-policies`, `GET /api/v1/inventory/stock-policies/{locationCode}/{sku}`, `PATCH /api/v1/inventory/stock-policies/{locationCode}/{sku}`
- Required permissions: `PERM-011`
- Application routes: `/products/stock-policies`, `/products/stock-policies/:locationCode/:sku`
- State management responsibility: local form state plus feature filter state

### UI-009 ABC Classification Management
- Angular feature module: `products`
- Main page component: `AbcClassificationPageComponent`
- Child components: `ClassificationReviewGridComponent`, `ClassificationEditorComponent`, `BulkClassificationToolbarComponent`
- Shared components: `DataTable`, `BulkSelectionToolbar`, `StatusBadge`, `SuccessWarningErrorBanner`
- Required Angular services: `AbcClassificationFacade`, `ProductApiService`
- Required DTOs: `SearchProductsQuery`, `AssignAbcClassificationRequest`, `PagedResponse<ProductSummaryResponse>`
- Related API endpoints: `PUT /api/v1/products/{sku}/abc-classification`, `GET /api/v1/products`
- Required permissions: `PERM-012`, `PERM-004`
- Application routes: `/products/abc-classification`
- State management responsibility: feature table selection and batch-edit state

### UI-010 Governance Policies and Reason Codes
- Angular feature module: `governance`
- Main page component: `GovernancePoliciesPageComponent`
- Child components: `PolicyVersionListComponent`, `PolicyEditorComponent`, `ReasonCodeListComponent`, `ReasonCodeEditorComponent`, `ThresholdsTabComponent`, `TolerancesTabComponent`
- Shared components: `TabsSegmentedContentSwitcher`, `StandardFormSection`, `TextAreaNotesField`, `ToggleSwitchControl`, `ReadOnlyReviewForm`
- Required Angular services: `GovernanceFacade`, `GovernancePolicyApiService`, `ReasonCodeApiService`
- Required DTOs: governance policy request/response DTOs, reason-code request/response DTOs, threshold and tolerance response DTOs
- Related API endpoints: `POST /api/v1/governance/reason-codes`, `GET /api/v1/governance/reason-codes`, `POST /api/v1/governance/reason-codes/{code}/retire`, `GET /api/v1/governance/reason-codes/{code}/validate`, `POST /api/v1/governance/policies`, `PATCH /api/v1/governance/policies/{policyId}/approval-thresholds`, `PATCH /api/v1/governance/policies/{policyId}/receipt-tolerances`, `GET /api/v1/governance/approval-thresholds`, `GET /api/v1/governance/receipt-tolerances`
- Required permissions: `PERM-013`, `PERM-014`, `PERM-032`
- Application routes: `/governance/policies`, `/governance/reason-codes`
- State management responsibility: feature state for active tab, draft policy version, and selected reason code

### UI-011 Supplier Management
- Angular feature module: `procurement`
- Main page component: `SupplierManagementPageComponent`
- Child components: `SupplierListComponent`, `SupplierDetailComponent`, `SupplierEditorComponent`
- Shared components: `DataTable`, `DetailPanel`, `StandardFormSection`, `StatusBadge`
- Required Angular services: `SupplierFacade`, `SupplierApiService`
- Required DTOs: supplier create/get/update DTOs and supplier summary/detail responses
- Related API endpoints: `POST /api/v1/suppliers`, `GET /api/v1/suppliers`, `GET /api/v1/suppliers/{supplierCode}`, `PATCH /api/v1/suppliers/{supplierCode}`, `POST /api/v1/suppliers/{supplierCode}/deactivate`
- Required permissions: `PERM-024`, `PERM-025`, `PERM-026`, `PERM-035`
- Application routes: `/procurement/suppliers`, `/procurement/suppliers/new`, `/procurement/suppliers/:supplierCode`
- State management responsibility: feature list/detail state; edit form local

### UI-012 Purchase Order Management
- Angular feature module: `procurement`
- Main page component: `PurchaseOrderManagementPageComponent`
- Child components: `PurchaseOrderListComponent`, `PurchaseOrderEditorComponent`, `PurchaseOrderDetailComponent`, `ExpectedDeliveriesPanelComponent`
- Shared components: `LineItemEditor`, `DataTable`, `RecordMetadataBlock`, `ConfirmationDialog`, `StatusTimeline`
- Required Angular services: `PurchaseOrderFacade`, `PurchaseOrderApiService`, `OpenPurchaseOrdersApiService`
- Required DTOs: PO create/get/update/cancel DTOs, PO summary/detail responses, open-PO board responses
- Related API endpoints: `POST /api/v1/procurement/purchase-orders`, `GET /api/v1/procurement/purchase-orders`, `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}`, `PATCH /api/v1/procurement/purchase-orders/{purchaseOrderId}`, `POST /api/v1/procurement/purchase-orders/{purchaseOrderId}/cancel`, `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}/validate-for-receipt`, `GET /api/v1/intelligence/procurement/open-pos`
- Required permissions: `PERM-024`, `PERM-025`, `PERM-026`, `PERM-027`, `PERM-035`
- Application routes: `/procurement/purchase-orders`, `/procurement/purchase-orders/new`, `/procurement/purchase-orders/:purchaseOrderId`
- State management responsibility: feature list/detail state, draft PO state for multi-line editing

### UI-013 Purchase Requisition Management
- Angular feature module: `procurement`
- Main page component: `PurchaseRequisitionManagementPageComponent`
- Child components: `RequisitionQueueComponent`, `RequisitionDetailComponent`, `RequisitionApprovalPanelComponent`, `ConvertToPoPanelComponent`
- Shared components: `QueueList`, `ApprovalDecisionPanel`, `ReadOnlyReviewForm`, `StatusTimeline`
- Required Angular services: `PurchaseRequisitionFacade`, `PurchaseRequisitionApiService`, `PurchaseOrderApiService`
- Required DTOs: requisition create/get/approve/reject/convert DTOs and requisition detail response
- Related API endpoints: `POST /api/v1/procurement/requisitions`, `GET /api/v1/procurement/requisitions/{requisitionId}`, `POST /api/v1/procurement/requisitions/{requisitionId}/approve`, `POST /api/v1/procurement/requisitions/{requisitionId}/reject`, `POST /api/v1/procurement/requisitions/{requisitionId}/convert-to-po`
- Required permissions: `PERM-067`, `PERM-068`, `PERM-024`
- Application routes: `/procurement/requisitions`, `/procurement/requisitions/:requisitionId`
- State management responsibility: feature queue and approval state; note missing list endpoint requires a temporary query-model workaround or deferred browse capability

### UI-014 Inbound Delivery Planning
- Angular feature module: `procurement`
- Main page component: `InboundDeliveryPlanningPageComponent`
- Child components: `InboundCalendarComponent`, `DeliveryScheduleEditorComponent`, `InboundDelayPanelComponent`
- Shared components: `DateField`, `FilterBar`, `AlertDetailCard`, `StatusBadge`
- Required Angular services: `InboundDeliveryPlanningFacade`, `PurchaseOrderApiService`, `InboundCalendarApiService`, `InboundDelayApiService`
- Required DTOs: expected-delivery request DTOs, inbound calendar response, inbound delay response
- Related API endpoints: `POST /api/v1/procurement/purchase-orders/{purchaseOrderId}/expected-deliveries`, `GET /api/v1/intelligence/procurement/inbound-calendar`, `GET /api/v1/intelligence/procurement/inbound-delays`
- Required permissions: `PERM-027`, `PERM-036`
- Application routes: `/procurement/inbound-delivery-planning`
- State management responsibility: feature calendar/filter state

### UI-015 Goods Receipt Workbench
- Angular feature module: `inbound`
- Main page component: `GoodsReceiptWorkbenchPageComponent`
- Child components: `ReceiptQueueComponent`, `ReceiptHeaderComponent`, `ReceiptLineVerificationComponent`, `ReceiptLotCaptureComponent`, `ReceiptVerificationActionsComponent`
- Shared components: `QueueList`, `LineItemEditor`, `StepProgressIndicator`, `SummaryStatisticStrip`, `SessionContextBadge`
- Required Angular services: `GoodsReceiptFacade`, `GoodsReceiptApiService`, `PurchaseOrderValidationApiService`
- Required DTOs: receipt create/get/list/verify DTOs, goods receipt detail/list responses, lot identity DTOs
- Related API endpoints: `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}/validate-for-receipt`, `POST /api/v1/inbound/goods-receipts`, `GET /api/v1/inbound/goods-receipts`, `GET /api/v1/inbound/goods-receipts/{goodsReceiptId}`, `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/verify`
- Required permissions: `PERM-028`
- Application routes: `/inbound/goods-receipts`, `/inbound/goods-receipts/:goodsReceiptId`
- State management responsibility: workflow store for current receipt, verified lines, captured lots, and verification progress

### UI-016 Receipt Discrepancy Resolution
- Angular feature module: `inbound`
- Main page component: `ReceiptDiscrepancyResolutionPageComponent`
- Child components: `DiscrepancyListComponent`, `DiscrepancyEditorComponent`, `DiscrepancyResolutionPanelComponent`, `ReceiptVsExpectedComparisonComponent`
- Shared components: `ComparisonPanel`, `VarianceHighlightBlock`, `EvidenceAttachmentPanel`, `ApprovalDecisionPanel`, `AlertDetailCard`
- Required Angular services: `ReceiptDiscrepancyFacade`, `ReceiptDiscrepancyApiService`, `ReasonCodeLookupService`, `ReceiptToleranceApiService`
- Required DTOs: discrepancy create/list/resolve DTOs, reason-code validation DTOs, receipt tolerance responses
- Related API endpoints: `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies`, `GET /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies`, `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/discrepancies/{discrepancyId}/resolve`, `GET /api/v1/governance/reason-codes/{code}/validate`, `GET /api/v1/governance/receipt-tolerances`
- Required permissions: `PERM-029`, `PERM-030`, `PERM-014`, `PERM-032`
- Application routes: `/inbound/discrepancies`, `/inbound/goods-receipts/:goodsReceiptId/discrepancies`
- State management responsibility: feature case state with selected discrepancy and attached evidence metadata

### UI-017 Put-Away Workbench
- Angular feature module: `inbound`
- Main page component: `PutAwayWorkbenchPageComponent`
- Child components: `PendingPutAwayQueueComponent`, `StoragePositionSelectorComponent`, `PutAwayConfirmationPanelComponent`
- Shared components: `QueueList`, `DropdownSelectControl`, `ConfirmationDialog`, `SessionContextBadge`
- Required Angular services: `PutAwayFacade`, `PutAwayApiService`, `StoragePositionApiService`
- Required DTOs: pending-put-away list responses, put-away command DTOs, storage-position list responses
- Related API endpoints: `GET /api/v1/inbound/pending-put-away`, `POST /api/v1/inbound/goods-receipts/{goodsReceiptId}/put-away`, `POST /api/v1/locations/{locationCode}/storage-positions`, `GET /api/v1/locations/{locationCode}/storage-positions`
- Required permissions: `PERM-033`, `PERM-004`
- Application routes: `/inbound/put-away`, `/inbound/put-away/:goodsReceiptId`
- State management responsibility: feature work queue and current put-away task state

### UI-018 Non-PO and Return Receipt Intake
- Angular feature module: `inbound`
- Main page component: `NonPoReturnReceiptIntakePageComponent`
- Child components: `ReceiptTypeSelectorComponent`, `AdHocReceiptFormComponent`, `ReturnReceiptFormComponent`
- Shared components: `RadioGroupSegmentedChoice`, `StandardFormSection`, `ValidationMessageBlock`
- Required Angular services: `AdHocReceiptFacade`, `AdHocReceiptApiService`, `ReturnReceiptApiService`
- Required DTOs: ad-hoc receipt request DTOs, return-receipt request DTOs, command result responses
- Related API endpoints: `POST /api/v1/inbound/ad-hoc-receipts`, `POST /api/v1/inbound/return-receipts`
- Required permissions: `PERM-031`, `PERM-034`
- Application routes: `/inbound/non-po-receipts`
- State management responsibility: local form state only; no durable feature store needed

### UI-019 Inbound Supply Tracking
- Angular feature module: `procurement`
- Main page component: `InboundSupplyTrackingPageComponent`
- Child components: `OpenPurchaseOrdersBoardComponent`, `InboundCalendarPanelComponent`, `InboundDelaysPanelComponent`, `InTransitStockPanelComponent`
- Shared components: `FilterBar`, `DateRangePicker`, `DataTable`, `StatusBadge`
- Required Angular services: `InboundSupplyTrackingFacade`, `PurchaseOrderApiService`, `InboundCalendarApiService`, `InboundDelayApiService`, `TransferInTransitApiService`
- Required DTOs: PO list/detail responses, expected-delivery DTOs, in-transit transfer responses
- Related API endpoints: `GET /api/v1/procurement/purchase-orders`, `GET /api/v1/procurement/purchase-orders/{purchaseOrderId}`, `POST /api/v1/procurement/purchase-orders/{purchaseOrderId}/expected-deliveries`, `GET /api/v1/transfers/in-transit`, `GET /api/v1/intelligence/procurement/open-pos`, `GET /api/v1/intelligence/procurement/inbound-calendar`, `GET /api/v1/intelligence/procurement/inbound-delays`
- Required permissions: `PERM-027`, `PERM-035`, `PERM-036`, `PERM-075`
- Application routes: `/procurement/inbound-supply-tracking`
- State management responsibility: feature dashboard/query state

### UI-020 Inventory Status Monitor
- Angular feature module: `inventory`
- Main page component: `InventoryStatusMonitorPageComponent`
- Child components: `StockStatusSummaryComponent`, `StockStatusBoardComponent`, `InventoryFiltersComponent`, `StockPositionDetailDrawerComponent`
- Shared components: `FilterBar`, `SavedViewSelector`, `DataTable`, `KpiSummaryCard`, `DrillDownLinkGroup`
- Required Angular services: `InventoryStatusFacade`, `StockPositionApiService`, `StockStatusApiService`, `LocationLookupService`
- Required DTOs: stock-position list/detail responses, stock-status indicator responses, summary/board responses
- Related API endpoints: `GET /api/v1/locations`, `GET /api/v1/inventory/stock-positions`, `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}`, `GET /api/v1/inventory/stock-status/{locationCode}/{sku}`, `GET /api/v1/intelligence/stock-status/summary`, `GET /api/v1/intelligence/stock-status/board`
- Required permissions: `PERM-017`, `PERM-020`, `PERM-083`, `PERM-085`, `PERM-004`
- Application routes: `/inventory/status-monitor`
- State management responsibility: feature filter, saved-view, and selected stock-position state

### UI-021 Inventory Availability Inquiry
- Angular feature module: `inventory`
- Main page component: `InventoryAvailabilityInquiryPageComponent`
- Child components: `AvailabilitySearchFormComponent`, `AvailabilityResultComponent`, `NetworkAvailabilityPanelComponent`, `InquiryHistoryPanelComponent`
- Shared components: `GlobalSearchBar`, `SearchResultsList`, `DetailPanel`, `StatusBadge`
- Required Angular services: `AvailabilityFacade`, `ProductApiService`, `AvailabilityApiService`, `AvailabilityInquiryLogApiService`
- Required DTOs: `SearchProductsQuery`, `GetProductBySkuRequest`, availability query/request DTOs, availability response DTOs
- Related API endpoints: `GET /api/v1/products`, `GET /api/v1/products/{sku}`, `GET /api/v1/inventory/availability/{sku}`, `GET /api/v1/inventory/availability/{sku}/network`, `POST /api/v1/fulfillment/orders/{orderId}/availability`, `GET /api/v1/intelligence/availability/inquiries`
- Required permissions: `PERM-004`, `PERM-018`, `PERM-022`, `PERM-051`
- Application routes: `/inventory/availability`
- State management responsibility: feature query/result state; search form local

### UI-022 Inventory Movement History
- Angular feature module: `inventory`
- Main page component: `InventoryMovementHistoryPageComponent`
- Child components: `MovementFiltersComponent`, `MovementResultsTableComponent`, `MovementDetailDrawerComponent`
- Shared components: `FilterBar`, `DateRangePicker`, `DataTable`, `ExportActionGroup`, `AuditRecordViewer`
- Required Angular services: `MovementHistoryFacade`, `MovementHistoryApiService`
- Required DTOs: movement-history query DTOs and movement record response DTOs
- Related API endpoints: `GET /api/v1/intelligence/movements`
- Required permissions: `PERM-023`, `PERM-084`
- Application routes: `/inventory/movement-history`
- State management responsibility: feature query and export state

### UI-023 Cycle Count Workbench
- Angular feature module: `inventory`
- Main page component: `CycleCountWorkbenchPageComponent`
- Child components: `CycleCountQueueComponent`, `CycleCountTaskComponent`, `CycleCountSubmissionComponent`
- Shared components: `QueueList`, `NumberInput`, `SessionContextBadge`, `SuccessWarningErrorBanner`
- Required Angular services: `CycleCountFacade`, `CycleCountApiService`, `CountPerformanceApiService`
- Required DTOs: cycle-count create/list/get/result DTOs, count performance responses
- Related API endpoints: `POST /api/v1/accuracy/cycle-counts`, `GET /api/v1/accuracy/cycle-counts`, `GET /api/v1/accuracy/cycle-counts/{cycleCountId}`, `POST /api/v1/accuracy/cycle-counts/{cycleCountId}/result`, `GET /api/v1/intelligence/accuracy/count-performance`
- Required permissions: `PERM-037`, `PERM-038`, `PERM-086`
- Application routes: `/inventory/cycle-counts`, `/inventory/cycle-counts/:cycleCountId`
- State management responsibility: feature queue and active count task state

### UI-024 Physical Inventory Count Management
- Angular feature module: `inventory`
- Main page component: `PhysicalInventoryCountManagementPageComponent`
- Child components: `PhysicalCountSessionComponent`, `FreezeStatusBannerComponent`, `CountProgressBoardComponent`, `CertificationPanelComponent`
- Shared components: `SummaryStatisticStrip`, `KpiSummaryCard`, `CheckboxGroup`, `ConfirmationDialog`, `StatusTimeline`
- Required Angular services: `PhysicalCountFacade`, `PhysicalCountApiService`, `LocationFreezeApiService`, `CountPerformanceApiService`
- Required DTOs: physical-count create/get/results/certify DTOs, freeze-status response, count-performance response
- Related API endpoints: `GET /api/v1/locations/{locationCode}/freeze-status`, `POST /api/v1/accuracy/physical-counts`, `GET /api/v1/accuracy/physical-counts/{physicalCountId}`, `POST /api/v1/accuracy/physical-counts/{physicalCountId}/results`, `POST /api/v1/accuracy/physical-counts/{physicalCountId}/certify`, `GET /api/v1/intelligence/accuracy/count-performance`
- Required permissions: `PERM-039`, `PERM-040`, `PERM-086`
- Application routes: `/inventory/physical-counts`, `/inventory/physical-counts/:physicalCountId`
- State management responsibility: workflow store for count session, freeze status, progress, and certification checklist

### UI-025 Variance Investigation and Approval
- Angular feature module: `inventory`
- Main page component: `VarianceInvestigationApprovalPageComponent`
- Child components: `VarianceCaseQueueComponent`, `VarianceInvestigationFormComponent`, `VarianceComparisonPanelComponent`, `VarianceApprovalPanelComponent`
- Shared components: `QueueList`, `ComparisonPanel`, `ApprovalDecisionPanel`, `EvidenceAttachmentPanel`, `AuditRecordViewer`
- Required Angular services: `VarianceCaseFacade`, `AdjustmentCaseApiService`, `PendingApprovalsApiService`
- Required DTOs: adjustment-case create/get/investigate/variance-approve DTOs, pending-approvals responses
- Related API endpoints: `POST /api/v1/accuracy/adjustment-cases`, `GET /api/v1/accuracy/adjustment-cases/{caseId}`, `POST /api/v1/accuracy/adjustment-cases/{caseId}/investigate`, `POST /api/v1/accuracy/adjustment-cases/{caseId}/variances/{varianceId}/approve`, `GET /api/v1/accuracy/pending-approvals`
- Required permissions: `PERM-043`, `PERM-041`, `PERM-042`, `PERM-044`, `PERM-046`
- Application routes: `/inventory/variances`, `/inventory/variances/:caseId`
- State management responsibility: feature case-state and approval queue state

### UI-026 Stock Adjustment Management
- Angular feature module: `inventory`
- Main page component: `StockAdjustmentManagementPageComponent`
- Child components: `AdjustmentRequestFormComponent`, `AdjustmentCaseDetailComponent`, `AdjustmentSubmissionPanelComponent`
- Shared components: `StandardFormSection`, `LineItemEditor`, `TextAreaNotesField`, `ConfirmationDialog`, `RecordMetadataBlock`
- Required Angular services: `StockAdjustmentFacade`, `AdjustmentCaseApiService`, `ReasonCodeLookupService`, `ApprovalThresholdApiService`
- Required DTOs: adjustment-case create/get/submit/approve/reject DTOs, reason-code responses, threshold responses
- Related API endpoints: `GET /api/v1/governance/reason-codes`, `GET /api/v1/governance/approval-thresholds`, `POST /api/v1/accuracy/adjustment-cases`, `GET /api/v1/accuracy/adjustment-cases/{caseId}`, `POST /api/v1/accuracy/adjustment-cases/{caseId}/submit`, `POST /api/v1/accuracy/adjustment-cases/{caseId}/approve`, `POST /api/v1/accuracy/adjustment-cases/{caseId}/reject`
- Required permissions: `PERM-014`, `PERM-013`, `PERM-043`, `PERM-045`, `PERM-044`
- Application routes: `/inventory/adjustments`, `/inventory/adjustments/:caseId`
- State management responsibility: draft adjustment form local; feature case workflow state for submission and approval path

### UI-027 Write-Off Authorization
- Angular feature module: `inventory`
- Main page component: `WriteOffAuthorizationPageComponent`
- Child components: `WriteOffCaseQueueComponent`, `WriteOffReviewComponent`, `FinanceAcknowledgementPanelComponent`, `WriteOffDecisionPanelComponent`
- Shared components: `ReadOnlyReviewForm`, `ApprovalDecisionPanel`, `EvidenceAttachmentPanel`, `ConfirmationDialog`
- Required Angular services: `WriteOffFacade`, `AdjustmentCaseApiService`
- Required DTOs: adjustment-case detail, submit, approve, reject DTOs and command results
- Related API endpoints: `GET /api/v1/accuracy/adjustment-cases/{caseId}`, `POST /api/v1/accuracy/adjustment-cases/{caseId}/submit`, `POST /api/v1/accuracy/adjustment-cases/{caseId}/approve`, `POST /api/v1/accuracy/adjustment-cases/{caseId}/reject`
- Required permissions: `PERM-045`, `PERM-046`, `PERM-044`
- Application routes: `/inventory/write-offs`, `/inventory/write-offs/:caseId`
- State management responsibility: feature approval queue and case decision state

### UI-028 Quarantine and Hold Register
- Angular feature module: `inventory`
- Main page component: `QuarantineHoldRegisterPageComponent`
- Child components: `QuarantineRegisterTableComponent`, `HoldActionPanelComponent`, `ReleaseHoldDialogComponent`
- Shared components: `DataTable`, `RadioGroupSegmentedChoice`, `StatusBadge`, `ConfirmationDialog`
- Required Angular services: `QuarantineHoldFacade`, `QuarantineHoldApiService`, `QuarantineRegisterApiService`
- Required DTOs: quarantine-hold apply/release DTOs, quarantine register response DTOs
- Related API endpoints: `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds`, `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds/{holdId}/release`, `GET /api/v1/intelligence/quarantine-register`
- Required permissions: `PERM-047`, `PERM-048`
- Application routes: `/inventory/quarantine`
- State management responsibility: feature filter and selected-hold state

### UI-029 Shrinkage, Loss, and Obsolescence Analysis
- Angular feature module: `inventory`
- Main page component: `ShrinkageAnalysisPageComponent`
- Child components: `ShrinkageKpiPanelComponent`, `TrendAnalysisTableComponent`, `ObsolescenceBreakdownComponent`
- Shared components: `KpiSummaryCard`, `DateRangePicker`, `ReportViewer`, `TrendIndicator`, `ExportActionGroup`
- Required Angular services: `ShrinkageAnalysisFacade`, `ShrinkageAnalysisApiService`
- Required DTOs: shrinkage analysis query/response DTOs
- Related API endpoints: `GET /api/v1/intelligence/accuracy/shrinkage`
- Required permissions: `PERM-049`
- Application routes: `/inventory/shrinkage-obsolescence`
- State management responsibility: feature analytical filter state

### UI-030 Order Reservation Workbench
- Angular feature module: `fulfillment`
- Main page component: `OrderReservationWorkbenchPageComponent`
- Child components: `OrderSearchQueueComponent`, `OrderReservationDetailComponent`, `AvailabilityCheckPanelComponent`, `ReservationActionsPanelComponent`
- Shared components: `QueueList`, `LineItemEditor`, `SummaryStatisticStrip`, `StatusTimeline`
- Required Angular services: `OrderReservationFacade`, `OrderApiService`, `AvailabilityApiService`, `ReservationApiService`, `CampaignRingFenceApiService`
- Required DTOs: order create/detail responses, order-availability request/response DTOs, reservation create/release DTOs, ring-fence responses
- Related API endpoints: `POST /api/v1/fulfillment/orders`, `POST /api/v1/fulfillment/orders/{orderId}/availability`, `POST /api/v1/fulfillment/orders/{orderId}/confirm`, `POST /api/v1/fulfillment/orders/{orderId}/cancel`, `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations`, `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/reservations/{reservationId}/release`, `GET /api/v1/campaigns/ring-fence/{locationCode}/{sku}`
- Required permissions: `PERM-054`, `PERM-051`, `PERM-052`, `PERM-053`, `PERM-092`
- Application routes: `/fulfillment/reservations`, `/fulfillment/reservations/:orderId`
- State management responsibility: workflow store for availability result, reservation status, and order confirmation saga state

### UI-031 Pick, Pack, and Ship Workbench
- Angular feature module: `fulfillment`
- Main page component: `PickPackShipWorkbenchPageComponent`
- Child components: `PickQueueComponent`, `PickVerificationComponent`, `PackingPanelComponent`, `ShipmentConfirmationPanelComponent`
- Shared components: `QueueList`, `StepProgressIndicator`, `ConfirmationDialog`, `SessionContextBadge`
- Required Angular services: `PickPackShipFacade`, `PickListApiService`, `PickVerificationApiService`, `ShipmentApiService`, `LotBreakdownApiService`
- Required DTOs: pick-list create/awaiting DTOs, pick verification DTOs, pack command DTOs, shipment command DTOs, lot-breakdown responses
- Related API endpoints: `POST /api/v1/fulfillment/orders/{orderId}/pick-lists`, `GET /api/v1/fulfillment/orders/{orderId}/pick-lists/awaiting`, `POST /api/v1/fulfillment/orders/{orderId}/picks/{pickId}/verify`, `POST /api/v1/fulfillment/orders/{orderId}/pack`, `POST /api/v1/fulfillment/orders/{orderId}/shipments`, `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/lots`
- Required permissions: `PERM-055`, `PERM-056`, `PERM-017`
- Application routes: `/fulfillment/pick-pack-ship`, `/fulfillment/pick-pack-ship/:orderId`
- State management responsibility: feature workbench state for active pick, pack completion, and shipment confirmation; note location-level pick queue API gap should be reflected as a backend dependency

### UI-032 Partial Fulfillment and Backorder Management
- Angular feature module: `fulfillment`
- Main page component: `PartialFulfillmentBackorderPageComponent`
- Child components: `PartialFulfillmentEditorComponent`, `BackorderDecisionPanelComponent`, `BackorderListComponent`
- Shared components: `ComparisonPanel`, `LineItemEditor`, `StatusTimeline`, `ValidationMessageBlock`
- Required Angular services: `BackorderFacade`, `PartialFulfillmentApiService`, `BackorderApiService`
- Required DTOs: partial-fulfillment command DTOs, backorder create/fulfill DTOs, backorder pipeline responses
- Related API endpoints: `POST /api/v1/fulfillment/orders/{orderId}/partial-fulfillment`, `POST /api/v1/fulfillment/orders/{orderId}/backorders`, `POST /api/v1/fulfillment/backorders/{backorderId}/fulfill`, `GET /api/v1/intelligence/fulfillment/backorders`
- Required permissions: `PERM-057`, `PERM-058`
- Application routes: `/fulfillment/partial-backorders`, `/fulfillment/partial-backorders/:orderId`
- State management responsibility: workflow store for fulfillment split decision and backorder lifecycle

### UI-033 Fulfillment Exception Management
- Angular feature module: `fulfillment`
- Main page component: `FulfillmentExceptionManagementPageComponent`
- Child components: `ExceptionQueueComponent`, `ExceptionDetailComponent`, `ExceptionResolutionFormComponent`
- Shared components: `QueueList`, `AlertDetailCard`, `TextAreaNotesField`, `SuccessWarningErrorBanner`
- Required Angular services: `FulfillmentExceptionFacade`, `FulfillmentExceptionApiService`, `QuarantineHoldApiService`
- Required DTOs: fulfillment exception create DTOs, exception log responses, quarantine-hold command DTOs
- Related API endpoints: `POST /api/v1/fulfillment/orders/{orderId}/exceptions`, `GET /api/v1/intelligence/fulfillment/exceptions`, `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/quarantine-holds`
- Required permissions: `PERM-059`, `PERM-047`
- Application routes: `/fulfillment/exceptions`, `/fulfillment/exceptions/:orderId`
- State management responsibility: feature exception queue state

### UI-034 Order Fulfillment Status
- Angular feature module: `fulfillment`
- Main page component: `OrderFulfillmentStatusPageComponent`
- Child components: `OrderStatusSearchComponent`, `OrderStatusDetailComponent`, `ReservationShipmentTimelineComponent`, `BackorderSummaryTabComponent`
- Shared components: `SearchResultsList`, `RecordMetadataBlock`, `StatusTimeline`, `TabsSegmentedContentSwitcher`
- Required Angular services: `OrderStatusFacade`, `OrderStatusApiService`, `FulfillmentStatusFeedService`
- Required DTOs: order list/detail/status DTOs and fulfillment status feed responses
- Related API endpoints: `GET /api/v1/fulfillment/orders`, `GET /api/v1/fulfillment/orders/{orderId}`, `GET /api/v1/fulfillment/orders/{orderId}/status`, `GET /api/v1/integrations/sales/fulfillment-status`
- Required permissions: `PERM-062`
- Application routes: `/fulfillment/order-status`, `/fulfillment/order-status/:orderId`
- State management responsibility: feature search and selected order status state

### UI-035 Multi-Location Split Fulfillment Planner
- Angular feature module: `fulfillment`
- Main page component: `MultiLocationSplitFulfillmentPlannerPageComponent`
- Child components: `NetworkAvailabilityPanelComponent`, `SplitPlanEditorComponent`, `SourceLocationAllocationGridComponent`
- Shared components: `RadioGroupSegmentedChoice`, `ComparisonPanel`, `ReadOnlyReviewForm`
- Required Angular services: `SplitFulfillmentFacade`, `NetworkAvailabilityApiService`, `MultiLocationPlanApiService`
- Required DTOs: network availability responses, multi-location plan request/response DTOs
- Related API endpoints: `GET /api/v1/inventory/availability/{sku}/network`, `POST /api/v1/fulfillment/orders/{orderId}/multi-location-plan`
- Required permissions: `PERM-022`, `PERM-061`
- Application routes: `/fulfillment/split-planner`, `/fulfillment/split-planner/:orderId`
- State management responsibility: workflow store for multi-source allocation plan

### UI-036 Low-Stock Alert Review
- Angular feature module: `procurement`
- Main page component: `LowStockAlertReviewPageComponent`
- Child components: `AlertQueueComponent`, `AlertDetailPanelComponent`, `RecommendationPanelComponent`
- Shared components: `QueueList`, `AlertDetailCard`, `SavedViewSelector`, `BulkSelectionToolbar`
- Required Angular services: `LowStockAlertFacade`, `AlertApiService`, `StockStatusApiService`, `StockPolicyApiService`, `ReplenishmentRecommendationApiService`
- Required DTOs: alert responses, stock-status responses, stock-policy responses, replenishment recommendation responses
- Related API endpoints: `GET /api/v1/inventory/stock-status/{locationCode}/{sku}`, `GET /api/v1/inventory/stock-policies/{locationCode}/{sku}`, `GET /api/v1/intelligence/alerts`, `POST /api/v1/intelligence/alerts/{alertId}/acknowledge`, `GET /api/v1/intelligence/replenishment/recommendations`
- Required permissions: `PERM-020`, `PERM-011`, `PERM-064`, `PERM-065`, `PERM-066`
- Application routes: `/procurement/low-stock-alerts`
- State management responsibility: feature alert queue and acknowledgement state

### UI-037 Replenishment Planning
- Angular feature module: `procurement`
- Main page component: `ReplenishmentPlanningPageComponent`
- Child components: `RecommendationListComponent`, `TransferBeforeBuyPanelComponent`, `RequisitionDraftPanelComponent`
- Shared components: `RecommendationCard`, `AlertDetailCard`, `ReadOnlyReviewForm`, `DateField`
- Required Angular services: `ReplenishmentPlanningFacade`, `ReplenishmentRecommendationApiService`, `NetworkImbalanceApiService`, `PurchaseRequisitionApiService`
- Required DTOs: replenishment recommendation responses, requisition create/detail DTOs, network imbalance responses
- Related API endpoints: `POST /api/v1/procurement/requisitions`, `GET /api/v1/procurement/requisitions/{requisitionId}`, `POST /api/v1/procurement/requisitions/{requisitionId}/approve`, `POST /api/v1/procurement/requisitions/{requisitionId}/reject`, `POST /api/v1/procurement/requisitions/{requisitionId}/convert-to-po`, `GET /api/v1/intelligence/replenishment/recommendations`, `GET /api/v1/intelligence/network/imbalance`
- Required permissions: `PERM-067`, `PERM-068`, `PERM-066`, `PERM-076`
- Application routes: `/procurement/replenishment-planning`
- State management responsibility: feature planning state; note list-browsing remains constrained by missing requisition list endpoint

### UI-038 Transfer Request
- Angular feature module: `transfers`
- Main page component: `TransferRequestPageComponent`
- Child components: `TransferRequestFormComponent`, `TransferCapacityPanelComponent`, `TransferRequestDetailComponent`
- Shared components: `LineItemEditor`, `NumberInput`, `ReadOnlyReviewForm`, `StatusTimeline`
- Required Angular services: `TransferRequestFacade`, `TransferApiService`, `TransferCapacityApiService`
- Required DTOs: transfer create/list/detail DTOs, transfer-capacity responses
- Related API endpoints: `POST /api/v1/transfers`, `GET /api/v1/transfers`, `GET /api/v1/transfers/{transferId}`, `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity`
- Required permissions: `PERM-071`, `PERM-075`, `PERM-076`
- Application routes: `/transfers/requests`, `/transfers/requests/new`, `/transfers/requests/:transferId`
- State management responsibility: feature draft transfer and detail state

### UI-039 Transfer Approval Queue
- Angular feature module: `transfers`
- Main page component: `TransferApprovalQueuePageComponent`
- Child components: `PendingTransferQueueComponent`, `TransferApprovalDetailComponent`, `TransferDecisionPanelComponent`
- Shared components: `QueueList`, `ApprovalDecisionPanel`, `ComparisonPanel`, `SavedViewSelector`
- Required Angular services: `TransferApprovalFacade`, `TransferApprovalApiService`, `PendingTransferApprovalApiService`, `TransferCapacityApiService`
- Required DTOs: approve/reject transfer DTOs, pending approval responses, transfer-capacity responses
- Related API endpoints: `POST /api/v1/transfers/{transferId}/approve`, `POST /api/v1/transfers/{transferId}/reject`, `GET /api/v1/transfers/pending-approvals`, `GET /api/v1/inventory/stock-positions/{locationCode}/{sku}/transfer-capacity`
- Required permissions: `PERM-072`, `PERM-076`
- Application routes: `/transfers/approvals`, `/transfers/approvals/:transferId`
- State management responsibility: feature approval queue and selected transfer decision state

### UI-040 Transfer Execution and In-Transit Tracking
- Angular feature module: `transfers`
- Main page component: `TransferExecutionTrackingPageComponent`
- Child components: `TransferExecutionQueueComponent`, `DispatchPanelComponent`, `ReceivePanelComponent`, `InTransitBoardComponent`
- Shared components: `QueueList`, `SummaryStatisticStrip`, `ConfirmationDialog`, `SessionContextBadge`
- Required Angular services: `TransferExecutionFacade`, `TransferDispatchApiService`, `TransferReceiveApiService`, `TransferInTransitApiService`
- Required DTOs: transfer list/detail responses, dispatch/receive/cancel command DTOs, in-transit responses
- Related API endpoints: `GET /api/v1/transfers`, `GET /api/v1/transfers/{transferId}`, `POST /api/v1/transfers/{transferId}/dispatch`, `POST /api/v1/transfers/{transferId}/receive`, `POST /api/v1/transfers/{transferId}/cancel`, `GET /api/v1/transfers/in-transit`
- Required permissions: `PERM-073`, `PERM-074`, `PERM-075`
- Application routes: `/transfers/execution`, `/transfers/execution/:transferId`
- State management responsibility: feature queue and execution-step state

### UI-041 Network Rebalancing Analysis
- Angular feature module: `transfers`
- Main page component: `NetworkRebalancingAnalysisPageComponent`
- Child components: `ImbalanceHeatmapComponent`, `RecommendationListComponent`, `RebalanceActionPanelComponent`
- Shared components: `RecommendationCard`, `FilterBar`, `DrillDownLinkGroup`
- Required Angular services: `NetworkRebalancingFacade`, `NetworkAvailabilityApiService`, `ReplenishmentRecommendationApiService`, `NetworkImbalanceApiService`
- Required DTOs: network availability responses, replenishment recommendation responses, network imbalance responses
- Related API endpoints: `GET /api/v1/inventory/availability/{sku}/network`, `GET /api/v1/intelligence/replenishment/recommendations`, `GET /api/v1/intelligence/network/imbalance`
- Required permissions: `PERM-022`, `PERM-066`, `PERM-076`
- Application routes: `/transfers/network-rebalancing`
- State management responsibility: feature analytics state

### UI-042 Return Authorization Management
- Angular feature module: `returns`
- Main page component: `ReturnAuthorizationManagementPageComponent`
- Child components: `ReturnAuthorizationSearchComponent`, `ReturnAuthorizationFormComponent`, `ReturnAuthorizationDetailComponent`
- Shared components: `SearchResultsList`, `LineItemEditor`, `ReadOnlyReviewForm`, `StatusTimeline`
- Required Angular services: `ReturnAuthorizationFacade`, `ReturnAuthorizationApiService`
- Required DTOs: return authorization create/list/get/cancel DTOs and return authorization response DTOs
- Related API endpoints: `POST /api/v1/returns/authorizations`, `GET /api/v1/returns/authorizations`, `GET /api/v1/returns/authorizations/{returnAuthorizationId}`, `POST /api/v1/returns/authorizations/{returnAuthorizationId}/cancel`
- Required permissions: `PERM-077`, `PERM-082`
- Application routes: `/returns/authorizations`, `/returns/authorizations/new`, `/returns/authorizations/:returnAuthorizationId`
- State management responsibility: feature list/detail state; authorization form local

### UI-043 Return Inspection and Disposition
- Angular feature module: `returns`
- Main page component: `ReturnInspectionDispositionPageComponent`
- Child components: `PendingReturnReceiptsQueueComponent`, `ReturnInspectionFormComponent`, `DispositionDecisionPanelComponent`, `ReturnDispositionSummaryComponent`
- Shared components: `QueueList`, `StepProgressIndicator`, `RadioGroupSegmentedChoice`, `FieldGroupHeader`, `StatusTimeline`
- Required Angular services: `ReturnProcessingFacade`, `ReturnReceiptApiService`, `ReturnInspectionApiService`, `ReturnDispositionApiService`
- Required DTOs: return receive/inspect/disposition DTOs, pending-return list responses, return-receipt command results
- Related API endpoints: `POST /api/v1/returns/{returnId}/receive`, `POST /api/v1/returns/{returnId}/inspect`, `POST /api/v1/returns/{returnId}/disposition`, `GET /api/v1/returns/pending-receipts`, `POST /api/v1/inbound/return-receipts`
- Required permissions: `PERM-078`, `PERM-079`, `PERM-080`, `PERM-081`, `PERM-034`
- Application routes: `/returns/inspection-disposition`, `/returns/inspection-disposition/:returnId`
- State management responsibility: workflow store for receive -> inspect -> disposition progression

### UI-044 Operational Reports and Analytics
- Angular feature module: `reports`
- Main page component: `OperationalReportsAnalyticsPageComponent`
- Child components: `ReportsCatalogComponent`, `ReportFiltersComponent`, `ReportViewerPanelComponent`, `DrilldownResultsPanelComponent`
- Shared components: `ReportViewer`, `FilterBar`, `DateRangePicker`, `ExportActionGroup`, `TrendIndicator`
- Required Angular services: `OperationalReportsFacade`, `DashboardApiService`, `StockStatusApiService`, `QuarantineRegisterApiService`, `MovementHistoryApiService`, `ShrinkageAnalysisApiService`, `CountPerformanceApiService`
- Required DTOs: dashboard responses, stock-status responses, quarantine register responses, movement history responses, shrinkage responses, count-performance responses
- Related API endpoints: `GET /api/v1/intelligence/dashboard`, `GET /api/v1/intelligence/stock-status/summary`, `GET /api/v1/intelligence/stock-status/board`, `GET /api/v1/intelligence/quarantine-register`, `GET /api/v1/intelligence/movements`, `GET /api/v1/intelligence/accuracy/shrinkage`, `GET /api/v1/intelligence/accuracy/count-performance`
- Required permissions: `PERM-083`, `PERM-085`, `PERM-047`, `PERM-023`, `PERM-084`, `PERM-049`, `PERM-086`
- Application routes: `/reports/operational`
- State management responsibility: feature report catalog, active report definition, filters, and export state

### UI-045 Inventory Valuation Reconciliation
- Angular feature module: `reports`
- Main page component: `InventoryValuationReconciliationPageComponent`
- Child components: `ValuationSnapshotPanelComponent`, `ReconciliationComparisonPanelComponent`, `ThreeWayMatchStatusPanelComponent`, `InvoiceAuthorizationPanelComponent`
- Shared components: `ComparisonPanel`, `VarianceHighlightBlock`, `DateRangePicker`, `ReportViewer`, `ExportActionGroup`
- Required Angular services: `ValuationReconciliationFacade`, `SupplierInvoiceApiService`, `ValuationSnapshotApiService`, `ValuationReconciliationApiService`, `ConsignmentOwnershipApiService`
- Required DTOs: supplier invoice register/get/match/pay DTOs, valuation snapshot responses, reconciliation responses, consignment-ownership command DTOs
- Related API endpoints: `POST /api/v1/inbound/supplier-invoices`, `GET /api/v1/inbound/supplier-invoices/{invoiceId}`, `POST /api/v1/inbound/supplier-invoices/{invoiceId}/three-way-match`, `POST /api/v1/inbound/supplier-invoices/{invoiceId}/authorize-payment`, `POST /api/v1/inventory/stock-positions/{locationCode}/{sku}/consignment-ownership`, `GET /api/v1/intelligence/valuation/snapshots`, `GET /api/v1/intelligence/valuation/reconciliation`
- Required permissions: `PERM-094`, `PERM-017`, `PERM-090`
- Application routes: `/reports/valuation-reconciliation`
- State management responsibility: feature reconciliation workspace state

### UI-046 Promotional Stock Readiness
- Angular feature module: `reports`
- Main page component: `PromotionalStockReadinessPageComponent`
- Child components: `CampaignAllocationListComponent`, `CampaignAllocationEditorComponent`, `ReadinessAssessmentPanelComponent`, `RingFenceStatusPanelComponent`
- Shared components: `KpiSummaryCard`, `TrendIndicator`, `AlertDetailCard`, `SummaryStatisticStrip`
- Required Angular services: `PromotionalReadinessFacade`, `CampaignAllocationApiService`, `CampaignReadinessApiService`, `CampaignPlanIntegrationService`
- Required DTOs: campaign allocation create/list/get/update/readiness/release/override DTOs, ring-fence responses, readiness responses
- Related API endpoints: `POST /api/v1/campaigns/allocations`, `GET /api/v1/campaigns/allocations`, `GET /api/v1/campaigns/allocations/{allocationId}`, `PATCH /api/v1/campaigns/allocations/{allocationId}`, `POST /api/v1/campaigns/allocations/{allocationId}/readiness`, `POST /api/v1/campaigns/allocations/{allocationId}/release`, `POST /api/v1/campaigns/allocations/{allocationId}/override`, `GET /api/v1/campaigns/ring-fence/{locationCode}/{sku}`, `GET /api/v1/intelligence/campaigns/readiness`, `POST /api/v1/integrations/marketing/campaign-plans`
- Required permissions: `PERM-092`, `PERM-093`
- Application routes: `/reports/promotional-readiness`
- State management responsibility: feature campaign-allocation state and readiness workflow state

### UI-047 Audit and Control Review Workspace
- Angular feature module: `reports`
- Main page component: `AuditControlReviewWorkspacePageComponent`
- Child components: `AuditScopeFormComponent`, `AuditPopulationResultsComponent`, `ControlTestChecklistComponent`, `AuditFindingsEditorComponent`
- Shared components: `StepProgressIndicator`, `ReportViewer`, `EvidenceAttachmentPanel`, `AuditRecordViewer`
- Required Angular services: `AuditWorkspaceFacade`, `AuditTrailApiService`, `AuditEvidenceExportService`
- Required DTOs: audit-trail query responses and audit export responses
- Related API endpoints: `GET /api/v1/intelligence/audit-trail`, `GET /api/v1/intelligence/audit-trail/export`
- Required permissions: `PERM-098`, `PERM-099`
- Application routes: `/reports/audit-workspace`
- State management responsibility: workflow store for audit scope, selected evidence set, and findings draft

### UI-048 Audit Trail Query
- Angular feature module: `reports`
- Main page component: `AuditTrailQueryPageComponent`
- Child components: `AuditQueryFiltersComponent`, `AuditResultsTableComponent`, `AuditRecordDetailDrawerComponent`
- Shared components: `DateRangePicker`, `DataTable`, `AuditRecordViewer`, `ExportActionGroup`
- Required Angular services: `AuditTrailQueryFacade`, `AuditTrailApiService`
- Required DTOs: audit-trail query DTOs, audit record responses, export responses
- Related API endpoints: `GET /api/v1/intelligence/audit-trail`, `GET /api/v1/intelligence/audit-trail/export`
- Required permissions: `PERM-098`, `PERM-099`
- Application routes: `/reports/audit-trail`
- State management responsibility: feature query, selected audit record, and export state

### UI-049 User Account Management
- Angular feature module: `administration`
- Main page component: `UserAccountManagementPageComponent`
- Child components: `UserAccountListComponent`, `UserAccountDetailComponent`, `UserProvisioningFormComponent`, `RoleAssignmentPanelComponent`
- Shared components: `GlobalSearchBar`, `DataTable`, `RoleAssignmentWidget`, `AccessScopeSelector`, `ConfirmationDialog`
- Required Angular services: `UserAccountFacade`, `UserAccountApiService`, `RoleAssignmentApiService`, `UserDirectorySyncService`
- Required DTOs: user create/list/get/suspend/deactivate/sync DTOs, `RoleAssignmentDto`, user account responses
- Related API endpoints: `POST /api/v1/users`, `GET /api/v1/users`, `GET /api/v1/users/{userId}`, `POST /api/v1/users/{userId}/roles`, `DELETE /api/v1/users/{userId}/roles/{roleAssignmentId}`, `POST /api/v1/users/{userId}/suspend`, `POST /api/v1/users/{userId}/deactivate`, `POST /api/v1/users/sync`
- Required permissions: `PERM-095`, `PERM-096`
- Application routes: `/admin/users`, `/admin/users/new`, `/admin/users/:userId`
- State management responsibility: feature list/detail state; provisioning form local

### UI-050 Role and Access Control Administration
- Angular feature module: `administration`
- Main page component: `RoleAccessControlAdministrationPageComponent`
- Child components: `PermissionMatrixViewComponent`, `RoleScopeRulesPanelComponent`, `AuthorizationEvaluationPanelComponent`, `LocationScopeValidationPanelComponent`
- Shared components: `PermissionMatrix`, `AccessScopeSelector`, `TabsSegmentedContentSwitcher`, `ReadOnlyReviewForm`
- Required Angular services: `AuthorizationAdminFacade`, `AuthorizationEvaluationApiService`, `LocationScopeValidationApiService`, `SessionService`
- Required DTOs: segregation-of-duties evaluation DTOs, action-evaluate DTOs, location-scope validation DTOs, session response DTO
- Related API endpoints: `POST /api/v1/governance/segregation-of-duties/evaluate`, `POST /api/v1/authorization/actions/evaluate`, `POST /api/v1/authorization/location-scope/validate`, `GET /api/v1/auth/session`
- Required permissions: `PERM-013`, `PERM-062`, authenticated session context
- Application routes: `/admin/roles-access`
- State management responsibility: feature policy-evaluation state, no long-lived workflow state required

## Routing Recommendation
- Top-level route groups should mirror business navigation:
  - `/home`
  - `/inventory`
  - `/products`
  - `/locations`
  - `/procurement`
  - `/inbound`
  - `/fulfillment`
  - `/transfers`
  - `/returns`
  - `/reports`
  - `/governance`
  - `/admin`
- All route groups except `/auth` should be lazy loaded.
- Use route guards for:
  - authenticated session
  - permission-based access
  - location-scope validation where a route carries `locationCode`
- Prefer route resolvers only for lightweight reference data; main business data should load through facades to preserve retry, skeleton, and refresh behavior.

## Service Layer Recommendation
- `ApiService` per business sub-domain for HTTP communication.
- `Facade` per screen or tightly related screen cluster for orchestration and view-model assembly.
- `LookupService` for reusable lists such as locations, reason codes, suppliers, and users.
- `Mapper` layer to convert backend DTOs into:
  - list row models
  - detail view models
  - command payloads
  - workflow step summaries

## Shared DTO Organization Recommendation
Organize frontend DTO contracts under feature folders, not a single giant shared folder:
```text
features/
  inventory/
    data-access/
      dto/
      mappers/
      services/
  procurement/
    data-access/
      dto/
      mappers/
      services/
```
Use `shared/models/common` only for:
- pagination wrappers
- command result wrappers
- audit metadata
- quantity and monetary primitives
- session and permission primitives

## Clean Architecture Alignment for Angular
- `feature/ui`: page components and presentational components
- `feature/application`: facades, workflow coordinators, permission orchestration
- `feature/domain`: business-oriented frontend models, enums, policy helpers, display rules
- `feature/data-access`: HTTP services, DTOs, mappers, repository-style adapters

This keeps Angular aligned with the approved backend architecture while remaining idiomatic for a SPA.

## Frontend Risks and Notes
- Requisition browsing depends on the missing requisition list endpoint identified in API review item `C-03`. Screens `UI-013` and `UI-037` should be planned with an API dependency note.
- Pick/pack/ship workbench completeness depends on the missing location-level pick queue endpoint identified in API review item `C-01`.
- Returns receipt should standardize on `POST /api/v1/returns/{returnId}/receive` as the canonical user-facing path, with `POST /api/v1/inbound/return-receipts` treated as infrastructure or transitional support.
- Permission checks should be enforced both at route entry and action level. A visible screen does not imply all commands on that screen are available.

## Recommendation Summary
- Build the Angular app as a capability-aligned modular SPA.
- Use lazy-loaded feature areas that mirror the 13 approved backend modules, consolidated into practical frontend feature groups.
- Keep components focused on rendering, facades focused on orchestration, and API services focused on contracts.
- Use local and feature-scoped state by default, with small global state reserved for session, permissions, shell, and notifications.
- Standardize shared workflow components for queues, approvals, timelines, filters, and auditability to reduce duplication across the 50 screens.
