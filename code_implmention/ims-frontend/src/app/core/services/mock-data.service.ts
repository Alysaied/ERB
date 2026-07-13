import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class MockDataService {
  private readonly screenData: Record<string, unknown> = {
    'UI-001': { message: 'Sign in with demo credentials', users: ['admin@ims.local', 'warehouse@ims.local'] },
    'UI-002': {
      kpis: [
        { label: 'Total SKUs', value: 12450, trend: '+2.3%' },
        { label: 'Low Stock Alerts', value: 47, trend: '-12%' },
        { label: 'Open POs', value: 128, trend: '+5%' },
        { label: 'Pending Approvals', value: 15, trend: 'flat' },
      ],
      stockHealth: { healthy: 78, warning: 15, critical: 7 },
    },
    'UI-003': {
      kpis: [
        { label: 'Inventory Turnover', value: '8.4x', target: '9.0x' },
        { label: 'Stock Accuracy', value: '98.2%', target: '99%' },
        { label: 'Fill Rate', value: '96.5%', target: '97%' },
        { label: 'Days of Supply', value: 42, target: 38 },
      ],
    },
    'UI-004': {
      alerts: [
        { id: 'ALT-001', type: 'low-stock', sku: 'SKU-100245', location: 'WH-EAST', severity: 'high' },
        { id: 'ALT-002', type: 'approval', ref: 'TR-2026-00088', severity: 'medium' },
        { id: 'ALT-003', type: 'inbound-delay', po: 'PO-2026-00418', severity: 'high' },
      ],
      unreadCount: 12,
    },
    'UI-005': {
      products: [
        { sku: 'SKU-100245', name: 'Industrial Widget A', category: 'WIDGETS', status: 'active', abc: 'A' },
        { sku: 'SKU-100312', name: 'Premium Component B', category: 'COMPONENTS', status: 'active', abc: 'B' },
        { sku: 'SKU-100478', name: 'Standard Part C', category: 'PARTS', status: 'discontinued', abc: 'C' },
      ],
      totalCount: 12450,
    },
    'UI-006': { importJobs: [{ id: 'IMP-001', status: 'validated', rows: 500, errors: 3 }] },
    'UI-007': {
      locations: [
        { code: 'WH-EAST', name: 'East Warehouse', type: 'warehouse', status: 'active' },
        { code: 'WH-WEST', name: 'West Warehouse', type: 'warehouse', status: 'active' },
        { code: 'STORE-042', name: 'Downtown Store', type: 'store', status: 'active' },
      ],
    },
    'UI-008': {
      policies: [
        { locationCode: 'WH-EAST', sku: 'SKU-100245', reorderLevel: 100, safetyStock: 50, minThreshold: 75 },
      ],
    },
    'UI-009': {
      classifications: [
        { sku: 'SKU-100245', abc: 'A', annualValue: 125000 },
        { sku: 'SKU-100312', abc: 'B', annualValue: 45000 },
      ],
    },
    'UI-010': {
      reasonCodes: ['DAMAGE', 'SHRINKAGE', 'COUNT_VARIANCE', 'OBSOLETE'],
      policies: [{ id: 'POL-001', version: '2.1', status: 'active' }],
    },
    'UI-011': {
      suppliers: [
        { code: 'SUP-ACME', name: 'ACME Supplies Inc.', status: 'active', leadTimeDays: 14 },
        { code: 'SUP-GLOB', name: 'Global Parts Ltd.', status: 'active', leadTimeDays: 21 },
      ],
    },
    'UI-012': {
      purchaseOrders: [
        { id: 'PO-2026-00418', supplier: 'SUP-ACME', status: 'open', total: 45200, lines: 12 },
        { id: 'PO-2026-00425', supplier: 'SUP-GLOB', status: 'partial', total: 12800, lines: 5 },
      ],
    },
    'UI-013': {
      requisitions: [
        { id: 'REQ-2026-00112', status: 'pending-approval', requestedBy: 'buyer@ims.local', total: 8500 },
      ],
    },
    'UI-014': {
      calendar: [
        { date: '2026-07-10', po: 'PO-2026-00418', supplier: 'ACME', status: 'on-time' },
        { date: '2026-07-12', po: 'PO-2026-00425', supplier: 'Global Parts', status: 'delayed' },
      ],
    },
    'UI-015': {
      receipts: [
        { id: 'GR-2026-00291', po: 'PO-2026-00418', status: 'pending-verification', lines: 8 },
        { id: 'GR-2026-00295', po: 'PO-2026-00425', status: 'verified', lines: 5 },
      ],
    },
    'UI-016': {
      discrepancies: [
        { id: 'DISC-001', type: 'shortage', expected: 100, received: 95, status: 'open' },
        { id: 'DISC-002', type: 'damage', expected: 50, received: 48, status: 'investigating' },
      ],
    },
    'UI-017': {
      tasks: [
        { id: 'PA-001', receipt: 'GR-2026-00295', sku: 'SKU-100245', qty: 500, suggestedBin: 'A-12-03' },
      ],
    },
    'UI-018': { receiptTypes: ['ad-hoc', 'return'] },
    'UI-019': {
      openPOs: 128,
      inTransit: 34,
      delayed: 7,
      expectedThisWeek: 22,
    },
    'UI-020': {
      summary: { onHand: 2450000, reserved: 125000, atp: 2325000, lowStock: 47, outOfStock: 12 },
      positions: [
        { location: 'WH-EAST', sku: 'SKU-100245', onHand: 1250, atp: 1100, status: 'healthy' },
        { location: 'WH-WEST', sku: 'SKU-100245', onHand: 85, atp: 45, status: 'low' },
      ],
    },
    'UI-021': {
      inquiries: [
        { sku: 'SKU-100245', networkAtp: 1145, locations: [{ code: 'WH-EAST', atp: 1100 }, { code: 'WH-WEST', atp: 45 }] },
      ],
    },
    'UI-022': {
      movements: [
        { id: 'MOV-001', type: 'receipt', sku: 'SKU-100245', qty: 500, location: 'WH-EAST', date: '2026-07-05' },
        { id: 'MOV-002', type: 'shipment', sku: 'SKU-100312', qty: -25, location: 'WH-EAST', date: '2026-07-06' },
      ],
    },
    'UI-023': {
      counts: [
        { id: 'CC-2026-0045', location: 'WH-EAST', sku: 'SKU-100245', status: 'assigned', blindCount: true },
      ],
    },
    'UI-024': {
      sessions: [
        { id: 'PIC-2026-001', location: 'WH-EAST', status: 'in-progress', progress: 65, frozen: true },
      ],
    },
    'UI-025': {
      cases: [
        { id: 'VAR-2026-0012', variance: -15, sku: 'SKU-100245', status: 'pending-approval' },
      ],
    },
    'UI-026': {
      adjustments: [
        { id: 'ADJ-2026-0008', reason: 'COUNT_VARIANCE', qty: -15, status: 'submitted' },
      ],
    },
    'UI-027': {
      writeOffs: [
        { id: 'WO-2026-0003', value: 2500, reason: 'OBSOLETE', status: 'pending-finance' },
      ],
    },
    'UI-028': {
      holds: [
        { id: 'HOLD-001', sku: 'SKU-100478', location: 'WH-EAST', qty: 200, reason: 'quality-check' },
      ],
    },
    'UI-029': {
      shrinkage: { rate: 1.2, value: 125000, obsolete: 45000, slowMoving: 89000 },
    },
    'UI-030': {
      orders: [
        { id: 'SO-2026-01872', customer: 'Customer A', status: 'pending-reservation', lines: 3 },
      ],
    },
    'UI-031': {
      pickQueue: [
        { orderId: 'SO-2026-01872', pickId: 'PICK-001', status: 'awaiting-pick', priority: 'high' },
      ],
    },
    'UI-032': {
      backorders: [
        { id: 'BO-2026-0045', orderId: 'SO-2026-01850', sku: 'SKU-100312', qty: 10, status: 'open' },
      ],
    },
    'UI-033': {
      exceptions: [
        { id: 'EXC-001', orderId: 'SO-2026-01872', type: 'pick-failure', status: 'open' },
      ],
    },
    'UI-034': {
      orders: [
        { id: 'SO-2026-01872', status: 'picking', reserved: true, shipped: false, backorder: false },
      ],
    },
    'UI-035': {
      plans: [
        { orderId: 'SO-2026-01900', sources: [{ location: 'WH-EAST', qty: 60 }, { location: 'WH-WEST', qty: 40 }] },
      ],
    },
    'UI-036': {
      alerts: [
        { id: 'ALT-001', sku: 'SKU-100245', location: 'WH-WEST', currentQty: 85, reorderLevel: 100 },
      ],
    },
    'UI-037': {
      recommendations: [
        { sku: 'SKU-100245', location: 'WH-WEST', action: 'transfer', source: 'WH-EAST', qty: 200 },
      ],
    },
    'UI-038': {
      transfers: [
        { id: 'TR-2026-00088', from: 'WH-EAST', to: 'WH-WEST', status: 'pending-approval', lines: 2 },
      ],
    },
    'UI-039': {
      pendingApprovals: [
        { id: 'TR-2026-00088', from: 'WH-EAST', to: 'WH-WEST', requestedBy: 'manager@ims.local' },
      ],
    },
    'UI-040': {
      inTransit: [
        { id: 'TR-2026-00085', from: 'WH-EAST', to: 'STORE-042', status: 'in-transit', eta: '2026-07-08' },
      ],
    },
    'UI-041': {
      imbalances: [
        { sku: 'SKU-100245', surplus: 'WH-EAST', deficit: 'WH-WEST', recommendedQty: 200 },
      ],
    },
    'UI-042': {
      authorizations: [
        { id: 'RA-2026-00116', orderId: 'SO-2026-01750', status: 'authorized', lines: 2 },
      ],
    },
    'UI-043': {
      pendingReturns: [
        { id: 'RET-2026-00045', ra: 'RA-2026-00116', status: 'pending-inspection' },
      ],
    },
    'UI-044': {
      reports: ['Stock Movement', 'Stockout / Overstock', 'Accuracy', 'Location Performance'],
    },
    'UI-045': {
      reconciliation: { operational: 2450000, finance: 2448500, variance: 1500, status: 'pending-review' },
    },
    'UI-046': {
      campaigns: [
        { id: 'CAMP-2026-SUMMER', name: 'Summer Sale 2026', readiness: 85, allocated: 5000 },
      ],
    },
    'UI-047': {
      auditScopes: [{ id: 'AUD-2026-Q2', population: 1250, tested: 125, findings: 3 }],
    },
    'UI-048': {
      auditRecords: [
        { id: 'AUD-REC-001', entity: 'Product', action: 'UPDATE', user: 'admin@ims.local', timestamp: '2026-07-05T10:30:00Z' },
      ],
    },
    'UI-049': {
      users: [
        { id: 'USR-001', email: 'admin@ims.local', name: 'System Admin', status: 'active', roles: ['System Administrator'] },
        { id: 'USR-002', email: 'warehouse@ims.local', name: 'Warehouse Manager', status: 'active', roles: ['Warehouse Manager'] },
      ],
    },
    'UI-050': {
      roles: ['System Administrator', 'Inventory Controller', 'Warehouse Manager', 'Buyer', 'Operations Director'],
      permissions: ['PERM-001', 'PERM-004', 'PERM-017', 'PERM-024', 'PERM-083'],
    },
  };

  getScreenData(screenId: string): unknown {
    return this.screenData[screenId] ?? { message: 'No mock data defined', screenId };
  }

  getProducts() {
    return (this.screenData['UI-005'] as { products: unknown[] }).products;
  }

  getLocations() {
    return (this.screenData['UI-007'] as { locations: unknown[] }).locations;
  }

  getDashboardKpis() {
    return (this.screenData['UI-002'] as { kpis: unknown[] }).kpis;
  }

  getAlerts() {
    return (this.screenData['UI-004'] as { alerts: unknown[] }).alerts;
  }
}
