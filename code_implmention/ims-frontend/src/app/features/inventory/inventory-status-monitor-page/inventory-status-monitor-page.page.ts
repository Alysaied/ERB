import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-inventory-status-monitor-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './inventory-status-monitor-page.page.html',
  styleUrl: './inventory-status-monitor-page.page.scss'
})
export class InventoryStatusMonitorPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-020';
  readonly title = 'Inventory Status Monitor';
  readonly description = 'Network-wide stock visibility';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-020');
  }
}
