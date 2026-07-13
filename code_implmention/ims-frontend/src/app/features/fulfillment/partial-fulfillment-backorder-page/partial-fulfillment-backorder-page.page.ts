import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-partial-fulfillment-backorder-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './partial-fulfillment-backorder-page.page.html',
  styleUrl: './partial-fulfillment-backorder-page.page.scss'
})
export class PartialFulfillmentBackorderPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-032';
  readonly title = 'Partial Fulfillment and Backorder Management';
  readonly description = 'Split shipments and backorders';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-032');
  }
}
