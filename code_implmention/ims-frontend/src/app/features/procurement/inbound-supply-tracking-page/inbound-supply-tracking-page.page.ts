import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-inbound-supply-tracking-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './inbound-supply-tracking-page.page.html',
  styleUrl: './inbound-supply-tracking-page.page.scss'
})
export class InboundSupplyTrackingPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-019';
  readonly title = 'Inbound Supply Tracking';
  readonly description = 'Monitor open POs and inbound delays';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-019');
  }
}
