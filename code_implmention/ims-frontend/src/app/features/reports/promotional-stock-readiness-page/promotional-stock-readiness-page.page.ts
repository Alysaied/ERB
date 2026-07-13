import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-promotional-stock-readiness-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './promotional-stock-readiness-page.page.html',
  styleUrl: './promotional-stock-readiness-page.page.scss'
})
export class PromotionalStockReadinessPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-046';
  readonly title = 'Promotional Stock Readiness';
  readonly description = 'Campaign stock allocation and readiness';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-046');
  }
}
