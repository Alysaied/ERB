import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-product-import-workspace-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './product-import-workspace-page.page.html',
  styleUrl: './product-import-workspace-page.page.scss'
})
export class ProductImportWorkspacePage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-006';
  readonly title = 'Product Import Workspace';
  readonly description = 'Bulk product and opening data imports';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-006');
  }
}
