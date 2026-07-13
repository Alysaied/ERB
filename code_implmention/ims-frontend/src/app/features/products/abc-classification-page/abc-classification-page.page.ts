import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-abc-classification-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './abc-classification-page.page.html',
  styleUrl: './abc-classification-page.page.scss'
})
export class AbcClassificationPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-009';
  readonly title = 'ABC Classification Management';
  readonly description = 'Assign and review ABC product classes';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-009');
  }
}
