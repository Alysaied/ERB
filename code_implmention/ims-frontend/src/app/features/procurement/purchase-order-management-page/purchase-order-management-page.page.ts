import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-purchase-order-management-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './purchase-order-management-page.page.html',
  styleUrl: './purchase-order-management-page.page.scss'
})
export class PurchaseOrderManagementPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-012';
  readonly title = 'Purchase Order Management';
  readonly description = 'Create and track purchase orders';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-012');
  }
}
