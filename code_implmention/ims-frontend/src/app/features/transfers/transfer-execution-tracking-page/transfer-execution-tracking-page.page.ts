import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-transfer-execution-tracking-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './transfer-execution-tracking-page.page.html',
  styleUrl: './transfer-execution-tracking-page.page.scss'
})
export class TransferExecutionTrackingPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-040';
  readonly title = 'Transfer Execution and In-Transit Tracking';
  readonly description = 'Dispatch and receive transfers';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-040');
  }
}
