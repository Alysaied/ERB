import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-cycle-count-workbench-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './cycle-count-workbench-page.page.html',
  styleUrl: './cycle-count-workbench-page.page.scss'
})
export class CycleCountWorkbenchPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-023';
  readonly title = 'Cycle Count Workbench';
  readonly description = 'Assigned blind cycle counts';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-023');
  }
}
