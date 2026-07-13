import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-order-reservation-workbench-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './order-reservation-workbench-page.page.html',
  styleUrl: './order-reservation-workbench-page.page.scss'
})
export class OrderReservationWorkbenchPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-030';
  readonly title = 'Order Reservation Workbench';
  readonly description = 'Reserve inventory for orders';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-030');
  }
}
