import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-return-authorization-management-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './return-authorization-management-page.page.html',
  styleUrl: './return-authorization-management-page.page.scss'
})
export class ReturnAuthorizationManagementPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-042';
  readonly title = 'Return Authorization Management';
  readonly description = 'Issue return authorizations';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-042');
  }
}
