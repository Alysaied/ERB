import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-session-context-badge',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './session-context-badge.component.html',
  styleUrl: './session-context-badge.component.scss'
})
export class SessionContextBadgeComponent {
  @Input() role = '';
  @Input() location = '';
}
