import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-transfer-request-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './transfer-request-page.page.html',
  styleUrl: './transfer-request-page.page.scss'
})
export class TransferRequestPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-038';
  readonly title = 'Transfer Request';
  readonly description = 'Submit inter-location transfers';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-038');
  }
}
