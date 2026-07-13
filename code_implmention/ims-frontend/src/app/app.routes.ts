import { Routes } from '@angular/router';
import { authGuard, guestGuard } from './core/guards/auth.guard';
import { AppShellComponent } from './core/layout/app-shell/app-shell.component';

export const routes: Routes = [
  { path: '', redirectTo: 'home/operations', pathMatch: 'full' },
  {
    path: 'auth/sign-in',
    canActivate: [guestGuard],
    loadComponent: () =>
      import('./features/auth/sign-in-page/sign-in-page.page').then((m) => m.SignInPage),
  },
  {
    path: '',
    component: AppShellComponent,
    canActivate: [authGuard],
    children: [
      {
        path: 'home/operations',
        loadComponent: () =>
          import('./features/home/operational-dashboard-page/operational-dashboard-page.page').then(
            (m) => m.OperationalDashboardPage
          ),
      },
      {
        path: 'notifications',
        loadComponent: () =>
          import('./features/notifications/notification-center-page/notification-center-page.page').then(
            (m) => m.NotificationCenterPage
          ),
      },
      {
        path: 'products/catalog',
        loadComponent: () =>
          import('./features/products/product-catalog-page/product-catalog-page.page').then(
            (m) => m.ProductCatalogPage
          ),
      },
      {
        path: 'products/import',
        loadComponent: () =>
          import('./features/products/product-import-workspace-page/product-import-workspace-page.page').then(
            (m) => m.ProductImportWorkspacePage
          ),
      },
      {
        path: 'products/stock-policies',
        loadComponent: () =>
          import('./features/products/stock-policy-management-page/stock-policy-management-page.page').then(
            (m) => m.StockPolicyManagementPage
          ),
      },
      {
        path: 'products/abc-classification',
        loadComponent: () =>
          import('./features/products/abc-classification-page/abc-classification-page.page').then(
            (m) => m.AbcClassificationPage
          ),
      },
      {
        path: 'locations',
        loadComponent: () =>
          import('./features/locations/location-management-page/location-management-page.page').then(
            (m) => m.LocationManagementPage
          ),
      },
      {
        path: 'governance/policies',
        loadComponent: () =>
          import('./features/governance/governance-policies-page/governance-policies-page.page').then(
            (m) => m.GovernancePoliciesPage
          ),
      },
      {
        path: 'procurement/suppliers',
        loadComponent: () =>
          import('./features/procurement/supplier-management-page/supplier-management-page.page').then(
            (m) => m.SupplierManagementPage
          ),
      },
      {
        path: 'procurement/purchase-orders',
        loadComponent: () =>
          import('./features/procurement/purchase-order-management-page/purchase-order-management-page.page').then(
            (m) => m.PurchaseOrderManagementPage
          ),
      },
      {
        path: 'procurement/requisitions',
        loadComponent: () =>
          import('./features/procurement/purchase-requisition-management-page/purchase-requisition-management-page.page').then(
            (m) => m.PurchaseRequisitionManagementPage
          ),
      },
      {
        path: 'procurement/inbound-delivery-planning',
        loadComponent: () =>
          import('./features/procurement/inbound-delivery-planning-page/inbound-delivery-planning-page.page').then(
            (m) => m.InboundDeliveryPlanningPage
          ),
      },
      {
        path: 'procurement/inbound-supply-tracking',
        loadComponent: () =>
          import('./features/procurement/inbound-supply-tracking-page/inbound-supply-tracking-page.page').then(
            (m) => m.InboundSupplyTrackingPage
          ),
      },
      {
        path: 'procurement/low-stock-alerts',
        loadComponent: () =>
          import('./features/procurement/low-stock-alert-review-page/low-stock-alert-review-page.page').then(
            (m) => m.LowStockAlertReviewPage
          ),
      },
      {
        path: 'procurement/replenishment-planning',
        loadComponent: () =>
          import('./features/procurement/replenishment-planning-page/replenishment-planning-page.page').then(
            (m) => m.ReplenishmentPlanningPage
          ),
      },
      {
        path: 'inbound/goods-receipts',
        loadComponent: () =>
          import('./features/inbound/goods-receipt-workbench-page/goods-receipt-workbench-page.page').then(
            (m) => m.GoodsReceiptWorkbenchPage
          ),
      },
      {
        path: 'inbound/discrepancies',
        loadComponent: () =>
          import('./features/inbound/receipt-discrepancy-resolution-page/receipt-discrepancy-resolution-page.page').then(
            (m) => m.ReceiptDiscrepancyResolutionPage
          ),
      },
      {
        path: 'inbound/put-away',
        loadComponent: () =>
          import('./features/inbound/put-away-workbench-page/put-away-workbench-page.page').then(
            (m) => m.PutAwayWorkbenchPage
          ),
      },
      {
        path: 'inbound/non-po-receipts',
        loadComponent: () =>
          import('./features/inbound/non-po-return-receipt-intake-page/non-po-return-receipt-intake-page.page').then(
            (m) => m.NonPoReturnReceiptIntakePage
          ),
      },
      {
        path: 'inventory/status-monitor',
        loadComponent: () =>
          import('./features/inventory/inventory-status-monitor-page/inventory-status-monitor-page.page').then(
            (m) => m.InventoryStatusMonitorPage
          ),
      },
      {
        path: 'inventory/availability',
        loadComponent: () =>
          import('./features/inventory/inventory-availability-inquiry-page/inventory-availability-inquiry-page.page').then(
            (m) => m.InventoryAvailabilityInquiryPage
          ),
      },
      {
        path: 'inventory/movement-history',
        loadComponent: () =>
          import('./features/inventory/inventory-movement-history-page/inventory-movement-history-page.page').then(
            (m) => m.InventoryMovementHistoryPage
          ),
      },
      {
        path: 'inventory/cycle-counts',
        loadComponent: () =>
          import('./features/inventory/cycle-count-workbench-page/cycle-count-workbench-page.page').then(
            (m) => m.CycleCountWorkbenchPage
          ),
      },
      {
        path: 'inventory/physical-counts',
        loadComponent: () =>
          import('./features/inventory/physical-inventory-count-management-page/physical-inventory-count-management-page.page').then(
            (m) => m.PhysicalInventoryCountManagementPage
          ),
      },
      {
        path: 'inventory/variances',
        loadComponent: () =>
          import('./features/inventory/variance-investigation-approval-page/variance-investigation-approval-page.page').then(
            (m) => m.VarianceInvestigationApprovalPage
          ),
      },
      {
        path: 'inventory/adjustments',
        loadComponent: () =>
          import('./features/inventory/stock-adjustment-management-page/stock-adjustment-management-page.page').then(
            (m) => m.StockAdjustmentManagementPage
          ),
      },
      {
        path: 'inventory/write-offs',
        loadComponent: () =>
          import('./features/inventory/write-off-authorization-page/write-off-authorization-page.page').then(
            (m) => m.WriteOffAuthorizationPage
          ),
      },
      {
        path: 'inventory/quarantine',
        loadComponent: () =>
          import('./features/inventory/quarantine-hold-register-page/quarantine-hold-register-page.page').then(
            (m) => m.QuarantineHoldRegisterPage
          ),
      },
      {
        path: 'inventory/shrinkage-obsolescence',
        loadComponent: () =>
          import('./features/inventory/shrinkage-analysis-page/shrinkage-analysis-page.page').then(
            (m) => m.ShrinkageAnalysisPage
          ),
      },
      {
        path: 'fulfillment/reservations',
        loadComponent: () =>
          import('./features/fulfillment/order-reservation-workbench-page/order-reservation-workbench-page.page').then(
            (m) => m.OrderReservationWorkbenchPage
          ),
      },
      {
        path: 'fulfillment/pick-pack-ship',
        loadComponent: () =>
          import('./features/fulfillment/pick-pack-ship-workbench-page/pick-pack-ship-workbench-page.page').then(
            (m) => m.PickPackShipWorkbenchPage
          ),
      },
      {
        path: 'fulfillment/partial-backorders',
        loadComponent: () =>
          import('./features/fulfillment/partial-fulfillment-backorder-page/partial-fulfillment-backorder-page.page').then(
            (m) => m.PartialFulfillmentBackorderPage
          ),
      },
      {
        path: 'fulfillment/exceptions',
        loadComponent: () =>
          import('./features/fulfillment/fulfillment-exception-management-page/fulfillment-exception-management-page.page').then(
            (m) => m.FulfillmentExceptionManagementPage
          ),
      },
      {
        path: 'fulfillment/order-status',
        loadComponent: () =>
          import('./features/fulfillment/order-fulfillment-status-page/order-fulfillment-status-page.page').then(
            (m) => m.OrderFulfillmentStatusPage
          ),
      },
      {
        path: 'fulfillment/split-planner',
        loadComponent: () =>
          import('./features/fulfillment/multi-location-split-fulfillment-planner-page/multi-location-split-fulfillment-planner-page.page').then(
            (m) => m.MultiLocationSplitFulfillmentPlannerPage
          ),
      },
      {
        path: 'transfers/requests',
        loadComponent: () =>
          import('./features/transfers/transfer-request-page/transfer-request-page.page').then(
            (m) => m.TransferRequestPage
          ),
      },
      {
        path: 'transfers/approvals',
        loadComponent: () =>
          import('./features/transfers/transfer-approval-queue-page/transfer-approval-queue-page.page').then(
            (m) => m.TransferApprovalQueuePage
          ),
      },
      {
        path: 'transfers/execution',
        loadComponent: () =>
          import('./features/transfers/transfer-execution-tracking-page/transfer-execution-tracking-page.page').then(
            (m) => m.TransferExecutionTrackingPage
          ),
      },
      {
        path: 'transfers/network-rebalancing',
        loadComponent: () =>
          import('./features/transfers/network-rebalancing-analysis-page/network-rebalancing-analysis-page.page').then(
            (m) => m.NetworkRebalancingAnalysisPage
          ),
      },
      {
        path: 'returns/authorizations',
        loadComponent: () =>
          import('./features/returns/return-authorization-management-page/return-authorization-management-page.page').then(
            (m) => m.ReturnAuthorizationManagementPage
          ),
      },
      {
        path: 'returns/inspection-disposition',
        loadComponent: () =>
          import('./features/returns/return-inspection-disposition-page/return-inspection-disposition-page.page').then(
            (m) => m.ReturnInspectionDispositionPage
          ),
      },
      {
        path: 'reports/executive-kpis',
        loadComponent: () =>
          import('./features/reports/executive-kpi-dashboard-page/executive-kpi-dashboard-page.page').then(
            (m) => m.ExecutiveKpiDashboardPage
          ),
      },
      {
        path: 'reports/operational',
        loadComponent: () =>
          import('./features/reports/operational-reports-analytics-page/operational-reports-analytics-page.page').then(
            (m) => m.OperationalReportsAnalyticsPage
          ),
      },
      {
        path: 'reports/valuation-reconciliation',
        loadComponent: () =>
          import('./features/reports/inventory-valuation-reconciliation-page/inventory-valuation-reconciliation-page.page').then(
            (m) => m.InventoryValuationReconciliationPage
          ),
      },
      {
        path: 'reports/promotional-readiness',
        loadComponent: () =>
          import('./features/reports/promotional-stock-readiness-page/promotional-stock-readiness-page.page').then(
            (m) => m.PromotionalStockReadinessPage
          ),
      },
      {
        path: 'reports/audit-workspace',
        loadComponent: () =>
          import('./features/reports/audit-control-review-workspace-page/audit-control-review-workspace-page.page').then(
            (m) => m.AuditControlReviewWorkspacePage
          ),
      },
      {
        path: 'reports/audit-trail',
        loadComponent: () =>
          import('./features/reports/audit-trail-query-page/audit-trail-query-page.page').then(
            (m) => m.AuditTrailQueryPage
          ),
      },
      {
        path: 'admin/users',
        loadComponent: () =>
          import('./features/administration/user-account-management-page/user-account-management-page.page').then(
            (m) => m.UserAccountManagementPage
          ),
      },
      {
        path: 'admin/roles-access',
        loadComponent: () =>
          import('./features/administration/role-access-control-administration-page/role-access-control-administration-page.page').then(
            (m) => m.RoleAccessControlAdministrationPage
          ),
      },
    ],
  },
  { path: '**', redirectTo: 'home/operations' },
];
