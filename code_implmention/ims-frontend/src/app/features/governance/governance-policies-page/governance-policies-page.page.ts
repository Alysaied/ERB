import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { MockDataService } from '../../../core/services/mock-data.service';

@Component({
  selector: 'ims-governance-policies-page',
  standalone: true,
  imports: [CommonModule, PageTitleBarComponent, BreadcrumbTrailComponent],
  templateUrl: './governance-policies-page.page.html',
  styleUrl: './governance-policies-page.page.scss'
})
export class GovernancePoliciesPage implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-010';
  readonly title = 'Governance Policies and Reason Codes';
  readonly description = 'Reason codes and governance policies';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-010');
  }
}
