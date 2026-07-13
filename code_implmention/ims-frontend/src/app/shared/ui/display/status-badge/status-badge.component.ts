import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-status-badge',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './status-badge.component.html',
  styleUrl: './status-badge.component.scss'
})
export class StatusBadgeComponent {
  @Input() status: string = "";
  @Input() variant: 'success' | 'warning' | 'danger' | 'info' | 'neutral' = "neutral";
}
