import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-fulfillment-exception-management-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './fulfillment-exception-management-page.page.html',
  styleUrl: './fulfillment-exception-management-page.page.scss'
})
export class FulfillmentExceptionManagementPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-033';
  readonly title = 'Fulfillment Exception Management';
  readonly description = 'Resolve outbound exceptions';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-033');
  }
}
