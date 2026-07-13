import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-transfer-approval-queue-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './transfer-approval-queue-page.page.html',
  styleUrl: './transfer-approval-queue-page.page.scss'
})
export class TransferApprovalQueuePage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-039';
  readonly title = 'Transfer Approval Queue';
  readonly description = 'Approve or reject transfers';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-039');
  }
}
