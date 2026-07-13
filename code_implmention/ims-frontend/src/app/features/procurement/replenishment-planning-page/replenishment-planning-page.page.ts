import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-replenishment-planning-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './replenishment-planning-page.page.html',
  styleUrl: './replenishment-planning-page.page.scss'
})
export class ReplenishmentPlanningPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-037';
  readonly title = 'Replenishment Planning';
  readonly description = 'Turn alerts into replenishment decisions';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-037');
  }
}
