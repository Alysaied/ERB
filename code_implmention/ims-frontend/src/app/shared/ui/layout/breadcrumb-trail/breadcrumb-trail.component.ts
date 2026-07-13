import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'ims-breadcrumb-trail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './breadcrumb-trail.component.html',
  styleUrl: './breadcrumb-trail.component.scss'
})
export class BreadcrumbTrailComponent {
  @Input() items: { label: string; route?: string }[] = [];
}
