import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-goods-receipt-workbench-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './goods-receipt-workbench-page.page.html',
  styleUrl: './goods-receipt-workbench-page.page.scss'
})
export class GoodsReceiptWorkbenchPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-015';
  readonly title = 'Goods Receipt Workbench';
  readonly description = 'Receive and verify supplier goods';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-015');
  }
}
