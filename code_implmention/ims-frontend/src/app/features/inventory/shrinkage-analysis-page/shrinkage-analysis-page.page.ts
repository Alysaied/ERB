import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-shrinkage-analysis-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './shrinkage-analysis-page.page.html',
  styleUrl: './shrinkage-analysis-page.page.scss'
})
export class ShrinkageAnalysisPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-029';
  readonly title = 'Shrinkage, Loss, and Obsolescence Analysis';
  readonly description = 'Analyze loss and obsolete stock';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-029');
  }
}
