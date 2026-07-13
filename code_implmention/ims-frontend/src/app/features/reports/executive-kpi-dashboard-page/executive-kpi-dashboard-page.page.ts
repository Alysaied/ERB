import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-executive-kpi-dashboard-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './executive-kpi-dashboard-page.page.html',
  styleUrl: './executive-kpi-dashboard-page.page.scss'
})
export class ExecutiveKpiDashboardPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-003';
  readonly title = 'Executive KPI Dashboard';
  readonly description = 'Strategic inventory KPIs and trends';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-003');
  }
}
