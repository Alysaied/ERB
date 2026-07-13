import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-notification-center-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './notification-center-page.page.html',
  styleUrl: './notification-center-page.page.scss'
})
export class NotificationCenterPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-004';
  readonly title = 'Notification Center';
  readonly description = 'Alerts, approvals, and notifications';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-004');
  }
}
