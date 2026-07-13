import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-inventory-availability-inquiry-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './inventory-availability-inquiry-page.page.html',
  styleUrl: './inventory-availability-inquiry-page.page.scss'
})
export class InventoryAvailabilityInquiryPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-021';
  readonly title = 'Inventory Availability Inquiry';
  readonly description = 'Search ATP and network availability';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-021');
  }
}
