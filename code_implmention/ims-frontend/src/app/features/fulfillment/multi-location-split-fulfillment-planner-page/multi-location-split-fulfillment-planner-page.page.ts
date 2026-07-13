import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-multi-location-split-fulfillment-planner-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './multi-location-split-fulfillment-planner-page.page.html',
  styleUrl: './multi-location-split-fulfillment-planner-page.page.scss'
})
export class MultiLocationSplitFulfillmentPlannerPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-035';
  readonly title = 'Multi-Location Split Fulfillment Planner';
  readonly description = 'Plan multi-source fulfillment';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-035');
  }
}
