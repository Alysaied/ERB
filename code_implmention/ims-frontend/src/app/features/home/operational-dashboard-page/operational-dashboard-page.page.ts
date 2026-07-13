import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { KpiSummaryCardComponent } from '../../../shared/ui/display/kpi-summary-card/kpi-summary-card.component';
import { QuickActionTileComponent } from '../../../shared/ui/navigation/quick-action-tile/quick-action-tile.component';
import { TaskApprovalShortcutWidgetComponent } from '../../../shared/ui/navigation/task-approval-shortcut-widget/task-approval-shortcut-widget.component';
import { MockDataService } from '../../../core/services/mock-data.service';

interface DashboardData {
  kpis: { label: string; value: string | number; trend: string }[];
  stockHealth: { healthy: number; warning: number; critical: number };
}

@Component({
  selector: 'ims-operational-dashboard-page',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    PageTitleBarComponent,
    BreadcrumbTrailComponent,
    KpiSummaryCardComponent,
    QuickActionTileComponent,
    TaskApprovalShortcutWidgetComponent,
  ],
  templateUrl: './operational-dashboard-page.page.html',
  styleUrl: './operational-dashboard-page.page.scss'
})
export class OperationalDashboardPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-002';
  readonly title = 'Operational Home Dashboard';
  readonly description = 'Day-to-day inventory summary and shortcuts';
  data: DashboardData | null = null;

  readonly quickActions = [
    { label: 'Status Monitor', route: '/inventory/status-monitor' },
    { label: 'Goods Receipt', route: '/inbound/goods-receipts' },
    { label: 'Purchase Orders', route: '/procurement/purchase-orders' },
    { label: 'Notifications', route: '/notifications' },
  ];

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-002') as DashboardData;
  }
}
