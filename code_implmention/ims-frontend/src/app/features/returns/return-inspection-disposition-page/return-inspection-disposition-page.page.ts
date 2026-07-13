import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-return-inspection-disposition-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './return-inspection-disposition-page.page.html',
  styleUrl: './return-inspection-disposition-page.page.scss'
})
export class ReturnInspectionDispositionPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-043';
  readonly title = 'Return Inspection and Disposition';
  readonly description = 'Inspect and disposition returns';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-043');
  }
}
