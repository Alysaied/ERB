import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-stock-policy-management-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './stock-policy-management-page.page.html',
  styleUrl: './stock-policy-management-page.page.scss'
})
export class StockPolicyManagementPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-008';
  readonly title = 'Stock Policy and Threshold Management';
  readonly description = 'Reorder levels and safety stock settings';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-008');
  }
}
