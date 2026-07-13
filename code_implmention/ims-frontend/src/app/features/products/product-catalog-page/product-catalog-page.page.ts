import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-product-catalog-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './product-catalog-page.page.html',
  styleUrl: './product-catalog-page.page.scss'
})
export class ProductCatalogPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-005';
  readonly title = 'Product Catalog Management';
  readonly description = 'Search and maintain product master records';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-005');
  }
}
