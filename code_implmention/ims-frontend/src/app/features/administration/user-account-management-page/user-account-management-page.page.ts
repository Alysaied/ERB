import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-user-account-management-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './user-account-management-page.page.html',
  styleUrl: './user-account-management-page.page.scss'
})
export class UserAccountManagementPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-049';
  readonly title = 'User Account Management';
  readonly description = 'Provision and manage user accounts';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-049');
  }
}
