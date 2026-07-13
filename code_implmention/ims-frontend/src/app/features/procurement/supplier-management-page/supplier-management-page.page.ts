import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-supplier-management-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './supplier-management-page.page.html',
  styleUrl: './supplier-management-page.page.scss'
})
export class SupplierManagementPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-011';
  readonly title = 'Supplier Management';
  readonly description = 'Maintain supplier master data';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-011');
  }
}
