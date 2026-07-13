import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-pick-pack-ship-workbench-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './pick-pack-ship-workbench-page.page.html',
  styleUrl: './pick-pack-ship-workbench-page.page.scss'
})
export class PickPackShipWorkbenchPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-031';
  readonly title = 'Pick, Pack, and Ship Workbench';
  readonly description = 'Warehouse fulfillment queues';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-031');
  }
}
