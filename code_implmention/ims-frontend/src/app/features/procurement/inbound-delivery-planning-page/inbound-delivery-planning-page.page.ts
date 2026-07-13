import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-inbound-delivery-planning-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './inbound-delivery-planning-page.page.html',
  styleUrl: './inbound-delivery-planning-page.page.scss'
})
export class InboundDeliveryPlanningPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-014';
  readonly title = 'Inbound Delivery Planning';
  readonly description = 'Plan expected supplier deliveries';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-014');
  }
}
