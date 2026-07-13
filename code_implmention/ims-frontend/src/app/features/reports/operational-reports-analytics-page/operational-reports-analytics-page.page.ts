import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-operational-reports-analytics-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './operational-reports-analytics-page.page.html',
  styleUrl: './operational-reports-analytics-page.page.scss'
})
export class OperationalReportsAnalyticsPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-044';
  readonly title = 'Operational Reports and Analytics';
  readonly description = 'Operational reports and analysis';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-044');
  }
}
