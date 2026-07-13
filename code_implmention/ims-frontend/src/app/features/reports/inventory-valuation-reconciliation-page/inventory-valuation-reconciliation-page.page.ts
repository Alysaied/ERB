import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-inventory-valuation-reconciliation-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './inventory-valuation-reconciliation-page.page.html',
  styleUrl: './inventory-valuation-reconciliation-page.page.scss'
})
export class InventoryValuationReconciliationPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-045';
  readonly title = 'Inventory Valuation Reconciliation';
  readonly description = 'Compare operational vs finance valuation';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-045');
  }
}
