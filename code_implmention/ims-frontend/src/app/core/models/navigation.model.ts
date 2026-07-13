export interface NavItem {
  label: string;
  route: string;
  icon?: string;
  children?: NavItem[];
}

export const MAIN_NAVIGATION: NavItem[] = [
  {
    label: 'Home',
    route: '/home/operations',
    icon: 'home',
    children: [
      { label: 'Operational Dashboard', route: '/home/operations' },
      { label: 'Executive KPI Dashboard', route: '/reports/executive-kpis' },
      { label: 'Notifications', route: '/notifications' },
    ],
  },
  {
    label: 'Inventory',
    route: '/inventory/status-monitor',
    icon: 'inventory',
    children: [
      { label: 'Status Monitor', route: '/inventory/status-monitor' },
      { label: 'Availability Inquiry', route: '/inventory/availability' },
      { label: 'Movement History', route: '/inventory/movement-history' },
      { label: 'Cycle Counts', route: '/inventory/cycle-counts' },
      { label: 'Physical Counts', route: '/inventory/physical-counts' },
      { label: 'Variance Approvals', route: '/inventory/variances' },
      { label: 'Stock Adjustments', route: '/inventory/adjustments' },
      { label: 'Write-Offs', route: '/inventory/write-offs' },
      { label: 'Quarantine & Holds', route: '/inventory/quarantine' },
      { label: 'Shrinkage & Obsolescence', route: '/inventory/shrinkage-obsolescence' },
    ],
  },
  {
    label: 'Products',
    route: '/products/catalog',
    icon: 'products',
    children: [
      { label: 'Product Catalog', route: '/products/catalog' },
      { label: 'Product Import', route: '/products/import' },
      { label: 'ABC Classification', route: '/products/abc-classification' },
      { label: 'Stock Policies', route: '/products/stock-policies' },
    ],
  },
  {
    label: 'Locations',
    route: '/locations',
    icon: 'locations',
    children: [{ label: 'Location Directory', route: '/locations' }],
  },
  {
    label: 'Procurement',
    route: '/procurement/suppliers',
    icon: 'procurement',
    children: [
      { label: 'Suppliers', route: '/procurement/suppliers' },
      { label: 'Purchase Requisitions', route: '/procurement/requisitions' },
      { label: 'Purchase Orders', route: '/procurement/purchase-orders' },
      { label: 'Inbound Delivery Planning', route: '/procurement/inbound-delivery-planning' },
      { label: 'Inbound Supply Tracking', route: '/procurement/inbound-supply-tracking' },
      { label: 'Low-Stock Alerts', route: '/procurement/low-stock-alerts' },
      { label: 'Replenishment Planning', route: '/procurement/replenishment-planning' },
    ],
  },
  {
    label: 'Inbound',
    route: '/inbound/goods-receipts',
    icon: 'inbound',
    children: [
      { label: 'Goods Receipt Workbench', route: '/inbound/goods-receipts' },
      { label: 'Receipt Discrepancies', route: '/inbound/discrepancies' },
      { label: 'Put-Away Workbench', route: '/inbound/put-away' },
      { label: 'Non-PO Receipt Intake', route: '/inbound/non-po-receipts' },
    ],
  },
  {
    label: 'Fulfillment',
    route: '/fulfillment/reservations',
    icon: 'fulfillment',
    children: [
      { label: 'Order Reservation', route: '/fulfillment/reservations' },
      { label: 'Pick / Pack / Ship', route: '/fulfillment/pick-pack-ship' },
      { label: 'Partial Fulfillment & Backorders', route: '/fulfillment/partial-backorders' },
      { label: 'Fulfillment Exceptions', route: '/fulfillment/exceptions' },
      { label: 'Order Status', route: '/fulfillment/order-status' },
      { label: 'Multi-Location Fulfillment', route: '/fulfillment/split-planner' },
    ],
  },
  {
    label: 'Transfers',
    route: '/transfers/requests',
    icon: 'transfers',
    children: [
      { label: 'Transfer Requests', route: '/transfers/requests' },
      { label: 'Transfer Approvals', route: '/transfers/approvals' },
      { label: 'Transfer Execution', route: '/transfers/execution' },
      { label: 'Network Rebalancing', route: '/transfers/network-rebalancing' },
    ],
  },
  {
    label: 'Returns',
    route: '/returns/authorizations',
    icon: 'returns',
    children: [
      { label: 'Return Authorizations', route: '/returns/authorizations' },
      { label: 'Return Inspection & Disposition', route: '/returns/inspection-disposition' },
    ],
  },
  {
    label: 'Reports & Analytics',
    route: '/reports/operational',
    icon: 'reports',
    children: [
      { label: 'Operational Reports', route: '/reports/operational' },
      { label: 'Executive KPI Dashboard', route: '/reports/executive-kpis' },
      { label: 'Valuation Reconciliation', route: '/reports/valuation-reconciliation' },
      { label: 'Promotional Readiness', route: '/reports/promotional-readiness' },
      { label: 'Audit Workspace', route: '/reports/audit-workspace' },
      { label: 'Audit Trail Query', route: '/reports/audit-trail' },
    ],
  },
  {
    label: 'Governance & Audit',
    route: '/governance/policies',
    icon: 'governance',
    children: [{ label: 'Governance Policies', route: '/governance/policies' }],
  },
  {
    label: 'Administration',
    route: '/admin/users',
    icon: 'admin',
    children: [
      { label: 'User Accounts', route: '/admin/users' },
      { label: 'Roles & Access Control', route: '/admin/roles-access' },
    ],
  },
];
