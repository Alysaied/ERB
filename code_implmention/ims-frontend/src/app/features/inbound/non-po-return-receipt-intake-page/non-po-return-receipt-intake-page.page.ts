import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-non-po-return-receipt-intake-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './non-po-return-receipt-intake-page.page.html',
  styleUrl: './non-po-return-receipt-intake-page.page.scss'
})
export class NonPoReturnReceiptIntakePage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-018';
  readonly title = 'Non-PO and Return Receipt Intake';
  readonly description = 'Ad-hoc and return receipts';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-018');
  }
}
