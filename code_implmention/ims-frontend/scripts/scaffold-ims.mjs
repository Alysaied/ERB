import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, '..', 'src', 'app');

function toPascalCase(kebab) {
  return kebab.split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('');
}

function toSelector(kebab) {
  return `ims-${kebab}`;
}

function createComponent(dir, name, options = {}) {
  const className = toPascalCase(name) + 'Component';
  const selector = toSelector(name);
  const basePath = path.join(root, dir, name);
  fs.mkdirSync(basePath, { recursive: true });

  const inputs = options.inputs || [];
  const inputLines = inputs.map(i => `  @Input() ${i.name}${i.type ? ': ' + i.type : ''}${i.default !== undefined ? ' = ' + JSON.stringify(i.default) : ''};`).join('\n');

  const ts = `import { Component${inputs.length ? ', Input' : ''} } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: '${selector}',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './${name}.component.html',
  styleUrl: './${name}.component.scss'
})
export class ${className} {
${inputLines}
}
`;

  const html = options.html || `<div class="${name}">
  <ng-content></ng-content>
</div>
`;

  const scss = options.scss || `.${name} {
  display: block;
}
`;

  fs.writeFileSync(path.join(basePath, `${name}.component.ts`), ts);
  fs.writeFileSync(path.join(basePath, `${name}.component.html`), html);
  fs.writeFileSync(path.join(basePath, `${name}.component.scss`), scss);
  return { className, selector, importPath: `./${dir}/${name}/${name}.component` };
}

function createPage(feature, name, screenId, title, description) {
  const className = toPascalCase(name);
  const basePath = path.join(root, 'features', feature, name);
  fs.mkdirSync(basePath, { recursive: true });

  const ts = `import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-${name}',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './${name}.page.html',
  styleUrl: './${name}.page.scss'
})
export class ${className} implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = '${screenId}';
  readonly title = '${title}';
  readonly description = '${description}';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('${screenId}');
  }
}
`;

  const html = `<div class="page ${name}">
  <ims-breadcrumb-trail [items]="[{ label: 'Home', route: '/home/operations' }, { label: '${title}' }]"></ims-breadcrumb-trail>
  <ims-page-title-bar [title]="title" [subtitle]="description"></ims-page-title-bar>
  <section class="page-content">
  @if (data) {
    <pre class="mock-preview">{{ data | json }}</pre>
  }
    <ng-content></ng-content>
  </section>
</div>
`;

  const scss = `.${name} {
  .page-content {
    padding: 1rem 0;
  }
  .mock-preview {
    background: var(--ims-surface-muted);
    border-radius: 8px;
    padding: 1rem;
    font-size: 0.75rem;
    overflow: auto;
    max-height: 200px;
  }
}
`;

  fs.writeFileSync(path.join(basePath, `${name}.page.ts`), ts);
  fs.writeFileSync(path.join(basePath, `${name}.page.html`), html);
  fs.writeFileSync(path.join(basePath, `${name}.page.scss`), scss);
  return { className, feature, name, screenId };
}

// Shared UI components
const sharedComponents = [
  { dir: 'shared/ui/layout', name: 'global-header' },
  { dir: 'shared/ui/layout', name: 'main-navigation-bar' },
  { dir: 'shared/ui/layout', name: 'secondary-navigation-panel' },
  { dir: 'shared/ui/layout', name: 'breadcrumb-trail', inputs: [{ name: 'items', type: '{ label: string; route?: string }[]', default: [] }] },
  { dir: 'shared/ui/layout', name: 'page-title-bar', inputs: [{ name: 'title', type: 'string', default: '' }, { name: 'subtitle', type: 'string', default: '' }] },
  { dir: 'shared/ui/layout', name: 'footer-metadata-strip' },
  { dir: 'shared/ui/layout', name: 'session-context-badge', inputs: [{ name: 'role', type: 'string', default: '' }, { name: 'location', type: 'string', default: '' }] },
  { dir: 'shared/ui/navigation', name: 'global-search-bar' },
  { dir: 'shared/ui/navigation', name: 'notification-icon-inbox-trigger', inputs: [{ name: 'count', type: 'number', default: 0 }] },
  { dir: 'shared/ui/navigation', name: 'user-menu' },
  { dir: 'shared/ui/navigation', name: 'quick-action-tile', inputs: [{ name: 'label', type: 'string', default: '' }, { name: 'route', type: 'string', default: '' }] },
  { dir: 'shared/ui/navigation', name: 'task-approval-shortcut-widget' },
  { dir: 'shared/ui/filters', name: 'filter-bar' },
  { dir: 'shared/ui/filters', name: 'date-range-picker' },
  { dir: 'shared/ui/filters', name: 'search-results-list' },
  { dir: 'shared/ui/filters', name: 'saved-view-selector' },
  { dir: 'shared/ui/display', name: 'kpi-summary-card', inputs: [{ name: 'label', type: 'string', default: '' }, { name: 'value', type: 'string | number', default: '' }, { name: 'trend', type: 'string', default: '' }] },
  { dir: 'shared/ui/display', name: 'status-badge', inputs: [{ name: 'status', type: 'string', default: '' }, { name: 'variant', type: "'success' | 'warning' | 'danger' | 'info' | 'neutral'", default: 'neutral' }] },
  { dir: 'shared/ui/display', name: 'summary-statistic-strip' },
  { dir: 'shared/ui/tables', name: 'data-table', inputs: [{ name: 'columns', type: 'string[]', default: [] }, { name: 'rows', type: 'Record<string, unknown>[]', default: [] }] },
  { dir: 'shared/ui/tables', name: 'table-row-action-menu' },
  { dir: 'shared/ui/display', name: 'detail-panel' },
  { dir: 'shared/ui/display', name: 'comparison-panel' },
  { dir: 'shared/ui/display', name: 'record-metadata-block' },
  { dir: 'shared/ui/forms', name: 'standard-form-section' },
  { dir: 'shared/ui/forms', name: 'field-group-header', inputs: [{ name: 'title', type: 'string', default: '' }] },
  { dir: 'shared/ui/forms', name: 'text-input', inputs: [{ name: 'label', type: 'string', default: '' }, { name: 'value', type: 'string', default: '' }] },
  { dir: 'shared/ui/forms', name: 'text-area-notes-field', inputs: [{ name: 'label', type: 'string', default: '' }] },
  { dir: 'shared/ui/forms', name: 'dropdown-select-control', inputs: [{ name: 'label', type: 'string', default: '' }, { name: 'options', type: 'string[]', default: [] }] },
  { dir: 'shared/ui/forms', name: 'checkbox-group' },
  { dir: 'shared/ui/forms', name: 'radio-group-segmented-choice' },
  { dir: 'shared/ui/forms', name: 'number-input', inputs: [{ name: 'label', type: 'string', default: '' }] },
  { dir: 'shared/ui/forms', name: 'date-field', inputs: [{ name: 'label', type: 'string', default: '' }] },
  { dir: 'shared/ui/forms', name: 'file-upload-control' },
  { dir: 'shared/ui/forms', name: 'validation-message-block', inputs: [{ name: 'message', type: 'string', default: '' }] },
  { dir: 'shared/ui/forms', name: 'read-only-review-form' },
  { dir: 'shared/ui/workflow', name: 'line-item-editor' },
  { dir: 'shared/ui/workflow', name: 'queue-list', inputs: [{ name: 'items', type: 'unknown[]', default: [] }] },
  { dir: 'shared/ui/workflow', name: 'step-progress-indicator', inputs: [{ name: 'steps', type: 'string[]', default: [] }, { name: 'currentStep', type: 'number', default: 0 }] },
  { dir: 'shared/ui/workflow', name: 'approval-decision-panel' },
  { dir: 'shared/ui/workflow', name: 'status-timeline' },
  { dir: 'shared/ui/workflow', name: 'alert-detail-card' },
  { dir: 'shared/ui/workflow', name: 'recommendation-card' },
  { dir: 'shared/ui/feedback', name: 'confirmation-dialog' },
  { dir: 'shared/ui/feedback', name: 'success-warning-error-banner', inputs: [{ name: 'type', type: "'success' | 'warning' | 'error' | 'info'", default: 'info' }, { name: 'message', type: 'string', default: '' }] },
  { dir: 'shared/ui/analytics', name: 'report-viewer' },
  { dir: 'shared/ui/analytics', name: 'export-action-group' },
  { dir: 'shared/ui/analytics', name: 'trend-indicator', inputs: [{ name: 'direction', type: "'up' | 'down' | 'flat'", default: 'flat' }, { name: 'value', type: 'string', default: '' }] },
  { dir: 'shared/ui/analytics', name: 'variance-highlight-block' },
  { dir: 'shared/ui/analytics', name: 'drill-down-link-group' },
  { dir: 'shared/ui/audit', name: 'role-assignment-widget' },
  { dir: 'shared/ui/audit', name: 'permission-matrix' },
  { dir: 'shared/ui/audit', name: 'access-scope-selector' },
  { dir: 'shared/ui/audit', name: 'audit-record-viewer' },
  { dir: 'shared/ui/audit', name: 'evidence-attachment-panel' },
  { dir: 'shared/ui/feedback', name: 'empty-state-panel', inputs: [{ name: 'title', type: 'string', default: 'No data' }, { name: 'message', type: 'string', default: '' }] },
  { dir: 'shared/ui/feedback', name: 'loading-skeleton' },
  { dir: 'shared/ui/feedback', name: 'bulk-selection-toolbar' },
  { dir: 'shared/ui/forms', name: 'toggle-switch-control', inputs: [{ name: 'label', type: 'string', default: '' }, { name: 'checked', type: 'boolean', default: false }] },
  { dir: 'shared/ui/display', name: 'tabs-segmented-content-switcher', inputs: [{ name: 'tabs', type: 'string[]', default: [] }] },
];

const screens = [
  { feature: 'auth', name: 'sign-in-page', id: 'UI-001', title: 'Sign In / Session Entry', route: 'auth/sign-in', desc: 'Authenticate and establish IMS session' },
  { feature: 'home', name: 'operational-dashboard-page', id: 'UI-002', title: 'Operational Home Dashboard', route: 'home/operations', desc: 'Day-to-day inventory summary and shortcuts' },
  { feature: 'reports', name: 'executive-kpi-dashboard-page', id: 'UI-003', title: 'Executive KPI Dashboard', route: 'reports/executive-kpis', desc: 'Strategic inventory KPIs and trends' },
  { feature: 'notifications', name: 'notification-center-page', id: 'UI-004', title: 'Notification Center', route: 'notifications', desc: 'Alerts, approvals, and notifications' },
  { feature: 'products', name: 'product-catalog-page', id: 'UI-005', title: 'Product Catalog Management', route: 'products/catalog', desc: 'Search and maintain product master records' },
  { feature: 'products', name: 'product-import-workspace-page', id: 'UI-006', title: 'Product Import Workspace', route: 'products/import', desc: 'Bulk product and opening data imports' },
  { feature: 'locations', name: 'location-management-page', id: 'UI-007', title: 'Location and Warehouse Management', route: 'locations', desc: 'Configure locations and storage positions' },
  { feature: 'products', name: 'stock-policy-management-page', id: 'UI-008', title: 'Stock Policy and Threshold Management', route: 'products/stock-policies', desc: 'Reorder levels and safety stock settings' },
  { feature: 'products', name: 'abc-classification-page', id: 'UI-009', title: 'ABC Classification Management', route: 'products/abc-classification', desc: 'Assign and review ABC product classes' },
  { feature: 'governance', name: 'governance-policies-page', id: 'UI-010', title: 'Governance Policies and Reason Codes', route: 'governance/policies', desc: 'Reason codes and governance policies' },
  { feature: 'procurement', name: 'supplier-management-page', id: 'UI-011', title: 'Supplier Management', route: 'procurement/suppliers', desc: 'Maintain supplier master data' },
  { feature: 'procurement', name: 'purchase-order-management-page', id: 'UI-012', title: 'Purchase Order Management', route: 'procurement/purchase-orders', desc: 'Create and track purchase orders' },
  { feature: 'procurement', name: 'purchase-requisition-management-page', id: 'UI-013', title: 'Purchase Requisition Management', route: 'procurement/requisitions', desc: 'Review and approve requisitions' },
  { feature: 'procurement', name: 'inbound-delivery-planning-page', id: 'UI-014', title: 'Inbound Delivery Planning', route: 'procurement/inbound-delivery-planning', desc: 'Plan expected supplier deliveries' },
  { feature: 'inbound', name: 'goods-receipt-workbench-page', id: 'UI-015', title: 'Goods Receipt Workbench', route: 'inbound/goods-receipts', desc: 'Receive and verify supplier goods' },
  { feature: 'inbound', name: 'receipt-discrepancy-resolution-page', id: 'UI-016', title: 'Receipt Discrepancy Resolution', route: 'inbound/discrepancies', desc: 'Resolve inbound discrepancies' },
  { feature: 'inbound', name: 'put-away-workbench-page', id: 'UI-017', title: 'Put-Away Workbench', route: 'inbound/put-away', desc: 'Complete put-away tasks' },
  { feature: 'inbound', name: 'non-po-return-receipt-intake-page', id: 'UI-018', title: 'Non-PO and Return Receipt Intake', route: 'inbound/non-po-receipts', desc: 'Ad-hoc and return receipts' },
  { feature: 'procurement', name: 'inbound-supply-tracking-page', id: 'UI-019', title: 'Inbound Supply Tracking', route: 'procurement/inbound-supply-tracking', desc: 'Monitor open POs and inbound delays' },
  { feature: 'inventory', name: 'inventory-status-monitor-page', id: 'UI-020', title: 'Inventory Status Monitor', route: 'inventory/status-monitor', desc: 'Network-wide stock visibility' },
  { feature: 'inventory', name: 'inventory-availability-inquiry-page', id: 'UI-021', title: 'Inventory Availability Inquiry', route: 'inventory/availability', desc: 'Search ATP and network availability' },
  { feature: 'inventory', name: 'inventory-movement-history-page', id: 'UI-022', title: 'Inventory Movement History', route: 'inventory/movement-history', desc: 'Trace inventory transactions' },
  { feature: 'inventory', name: 'cycle-count-workbench-page', id: 'UI-023', title: 'Cycle Count Workbench', route: 'inventory/cycle-counts', desc: 'Assigned blind cycle counts' },
  { feature: 'inventory', name: 'physical-inventory-count-management-page', id: 'UI-024', title: 'Physical Inventory Count Management', route: 'inventory/physical-counts', desc: 'Wall-to-wall count sessions' },
  { feature: 'inventory', name: 'variance-investigation-approval-page', id: 'UI-025', title: 'Variance Investigation and Approval', route: 'inventory/variances', desc: 'Review count variances' },
  { feature: 'inventory', name: 'stock-adjustment-management-page', id: 'UI-026', title: 'Stock Adjustment Management', route: 'inventory/adjustments', desc: 'Submit and approve adjustments' },
  { feature: 'inventory', name: 'write-off-authorization-page', id: 'UI-027', title: 'Write-Off Authorization', route: 'inventory/write-offs', desc: 'Review write-off requests' },
  { feature: 'inventory', name: 'quarantine-hold-register-page', id: 'UI-028', title: 'Quarantine and Hold Register', route: 'inventory/quarantine', desc: 'Apply and release quarantine holds' },
  { feature: 'inventory', name: 'shrinkage-analysis-page', id: 'UI-029', title: 'Shrinkage, Loss, and Obsolescence Analysis', route: 'inventory/shrinkage-obsolescence', desc: 'Analyze loss and obsolete stock' },
  { feature: 'fulfillment', name: 'order-reservation-workbench-page', id: 'UI-030', title: 'Order Reservation Workbench', route: 'fulfillment/reservations', desc: 'Reserve inventory for orders' },
  { feature: 'fulfillment', name: 'pick-pack-ship-workbench-page', id: 'UI-031', title: 'Pick, Pack, and Ship Workbench', route: 'fulfillment/pick-pack-ship', desc: 'Warehouse fulfillment queues' },
  { feature: 'fulfillment', name: 'partial-fulfillment-backorder-page', id: 'UI-032', title: 'Partial Fulfillment and Backorder Management', route: 'fulfillment/partial-backorders', desc: 'Split shipments and backorders' },
  { feature: 'fulfillment', name: 'fulfillment-exception-management-page', id: 'UI-033', title: 'Fulfillment Exception Management', route: 'fulfillment/exceptions', desc: 'Resolve outbound exceptions' },
  { feature: 'fulfillment', name: 'order-fulfillment-status-page', id: 'UI-034', title: 'Order Fulfillment Status', route: 'fulfillment/order-status', desc: 'Order inquiry and status tracking' },
  { feature: 'fulfillment', name: 'multi-location-split-fulfillment-planner-page', id: 'UI-035', title: 'Multi-Location Split Fulfillment Planner', route: 'fulfillment/split-planner', desc: 'Plan multi-source fulfillment' },
  { feature: 'procurement', name: 'low-stock-alert-review-page', id: 'UI-036', title: 'Low-Stock Alert Review', route: 'procurement/low-stock-alerts', desc: 'Review replenishment alerts' },
  { feature: 'procurement', name: 'replenishment-planning-page', id: 'UI-037', title: 'Replenishment Planning', route: 'procurement/replenishment-planning', desc: 'Turn alerts into replenishment decisions' },
  { feature: 'transfers', name: 'transfer-request-page', id: 'UI-038', title: 'Transfer Request', route: 'transfers/requests', desc: 'Submit inter-location transfers' },
  { feature: 'transfers', name: 'transfer-approval-queue-page', id: 'UI-039', title: 'Transfer Approval Queue', route: 'transfers/approvals', desc: 'Approve or reject transfers' },
  { feature: 'transfers', name: 'transfer-execution-tracking-page', id: 'UI-040', title: 'Transfer Execution and In-Transit Tracking', route: 'transfers/execution', desc: 'Dispatch and receive transfers' },
  { feature: 'transfers', name: 'network-rebalancing-analysis-page', id: 'UI-041', title: 'Network Rebalancing Analysis', route: 'transfers/network-rebalancing', desc: 'Analyze stock imbalance' },
  { feature: 'returns', name: 'return-authorization-management-page', id: 'UI-042', title: 'Return Authorization Management', route: 'returns/authorizations', desc: 'Issue return authorizations' },
  { feature: 'returns', name: 'return-inspection-disposition-page', id: 'UI-043', title: 'Return Inspection and Disposition', route: 'returns/inspection-disposition', desc: 'Inspect and disposition returns' },
  { feature: 'reports', name: 'operational-reports-analytics-page', id: 'UI-044', title: 'Operational Reports and Analytics', route: 'reports/operational', desc: 'Operational reports and analysis' },
  { feature: 'reports', name: 'inventory-valuation-reconciliation-page', id: 'UI-045', title: 'Inventory Valuation Reconciliation', route: 'reports/valuation-reconciliation', desc: 'Compare operational vs finance valuation' },
  { feature: 'reports', name: 'promotional-stock-readiness-page', id: 'UI-046', title: 'Promotional Stock Readiness', route: 'reports/promotional-readiness', desc: 'Campaign stock allocation and readiness' },
  { feature: 'reports', name: 'audit-control-review-workspace-page', id: 'UI-047', title: 'Audit and Control Review Workspace', route: 'reports/audit-workspace', desc: 'Audit scope and control testing' },
  { feature: 'reports', name: 'audit-trail-query-page', id: 'UI-048', title: 'Audit Trail Query', route: 'reports/audit-trail', desc: 'Search immutable audit records' },
  { feature: 'administration', name: 'user-account-management-page', id: 'UI-049', title: 'User Account Management', route: 'admin/users', desc: 'Provision and manage user accounts' },
  { feature: 'administration', name: 'role-access-control-administration-page', id: 'UI-050', title: 'Role and Access Control Administration', route: 'admin/roles-access', desc: 'Configure role permissions' },
];

console.log('Generating shared components...');
for (const c of sharedComponents) {
  createComponent(c.dir, c.name, { inputs: c.inputs });
}

console.log('Generating feature screens...');
const pages = screens.map(s => createPage(s.feature, s.name, s.id, s.title, s.desc));

// Export routes manifest
const routesManifest = screens.map(s => ({
  path: s.route,
  loadComponent: () => import(`../features/${s.feature}/${s.name}/${s.name}.page`).then(m => m[toPascalCase(s.name)]),
  screenId: s.id,
  title: s.title,
  auth: s.id !== 'UI-001'
}));

fs.writeFileSync(
  path.join(__dirname, 'generated-routes.json'),
  JSON.stringify(routesManifest, null, 2)
);

console.log(`Created ${sharedComponents.length} shared components and ${pages.length} screens.`);
