import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-put-away-workbench-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './put-away-workbench-page.page.html',
  styleUrl: './put-away-workbench-page.page.scss'
})
export class PutAwayWorkbenchPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-017';
  readonly title = 'Put-Away Workbench';
  readonly description = 'Complete put-away tasks';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-017');
  }
}
