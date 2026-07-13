import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-variance-investigation-approval-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './variance-investigation-approval-page.page.html',
  styleUrl: './variance-investigation-approval-page.page.scss'
})
export class VarianceInvestigationApprovalPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-025';
  readonly title = 'Variance Investigation and Approval';
  readonly description = 'Review count variances';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-025');
  }
}
