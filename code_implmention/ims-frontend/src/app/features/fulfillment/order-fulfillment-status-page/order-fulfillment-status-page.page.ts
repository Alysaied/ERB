import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-order-fulfillment-status-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './order-fulfillment-status-page.page.html',
  styleUrl: './order-fulfillment-status-page.page.scss'
})
export class OrderFulfillmentStatusPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-034';
  readonly title = 'Order Fulfillment Status';
  readonly description = 'Order inquiry and status tracking';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-034');
  }
}
