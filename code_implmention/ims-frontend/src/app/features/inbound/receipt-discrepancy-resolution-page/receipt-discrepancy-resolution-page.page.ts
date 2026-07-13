import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-receipt-discrepancy-resolution-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './receipt-discrepancy-resolution-page.page.html',
  styleUrl: './receipt-discrepancy-resolution-page.page.scss'
})
export class ReceiptDiscrepancyResolutionPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-016';
  readonly title = 'Receipt Discrepancy Resolution';
  readonly description = 'Resolve inbound discrepancies';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-016');
  }
}
