import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-write-off-authorization-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './write-off-authorization-page.page.html',
  styleUrl: './write-off-authorization-page.page.scss'
})
export class WriteOffAuthorizationPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-027';
  readonly title = 'Write-Off Authorization';
  readonly description = 'Review write-off requests';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-027');
  }
}
