import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-network-rebalancing-analysis-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './network-rebalancing-analysis-page.page.html',
  styleUrl: './network-rebalancing-analysis-page.page.scss'
})
export class NetworkRebalancingAnalysisPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-041';
  readonly title = 'Network Rebalancing Analysis';
  readonly description = 'Analyze stock imbalance';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-041');
  }
}
