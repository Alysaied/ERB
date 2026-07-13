import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-location-management-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './location-management-page.page.html',
  styleUrl: './location-management-page.page.scss'
})
export class LocationManagementPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-007';
  readonly title = 'Location and Warehouse Management';
  readonly description = 'Configure locations and storage positions';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-007');
  }
}
