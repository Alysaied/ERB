import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-audit-control-review-workspace-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './audit-control-review-workspace-page.page.html',
  styleUrl: './audit-control-review-workspace-page.page.scss'
})
export class AuditControlReviewWorkspacePage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-047';
  readonly title = 'Audit and Control Review Workspace';
  readonly description = 'Audit scope and control testing';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-047');
  }
}
