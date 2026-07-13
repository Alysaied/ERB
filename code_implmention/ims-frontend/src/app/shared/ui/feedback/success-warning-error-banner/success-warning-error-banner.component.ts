import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-success-warning-error-banner',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './success-warning-error-banner.component.html',
  styleUrl: './success-warning-error-banner.component.scss'
})
export class SuccessWarningErrorBannerComponent {
  @Input() type: 'success' | 'warning' | 'error' | 'info' = 'info';
  @Input() message = '';
}
