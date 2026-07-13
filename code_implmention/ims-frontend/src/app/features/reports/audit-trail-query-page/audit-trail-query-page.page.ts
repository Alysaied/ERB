import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-audit-trail-query-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './audit-trail-query-page.page.html',
  styleUrl: './audit-trail-query-page.page.scss'
})
export class AuditTrailQueryPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-048';
  readonly title = 'Audit Trail Query';
  readonly description = 'Search immutable audit records';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-048');
  }
}
