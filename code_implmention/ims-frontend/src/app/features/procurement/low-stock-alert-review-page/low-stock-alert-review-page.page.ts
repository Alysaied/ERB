import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-low-stock-alert-review-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './low-stock-alert-review-page.page.html',
  styleUrl: './low-stock-alert-review-page.page.scss'
})
export class LowStockAlertReviewPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-036';
  readonly title = 'Low-Stock Alert Review';
  readonly description = 'Review replenishment alerts';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-036');
  }
}
