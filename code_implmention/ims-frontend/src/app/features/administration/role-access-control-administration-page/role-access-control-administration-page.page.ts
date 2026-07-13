import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-role-access-control-administration-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './role-access-control-administration-page.page.html',
  styleUrl: './role-access-control-administration-page.page.scss'
})
export class RoleAccessControlAdministrationPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-050';
  readonly title = 'Role and Access Control Administration';
  readonly description = 'Configure role permissions';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-050');
  }
}
