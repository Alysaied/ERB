import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-inventory-movement-history-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './inventory-movement-history-page.page.html',
  styleUrl: './inventory-movement-history-page.page.scss'
})
export class InventoryMovementHistoryPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-022';
  readonly title = 'Inventory Movement History';
  readonly description = 'Trace inventory transactions';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-022');
  }
}
