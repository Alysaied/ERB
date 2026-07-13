import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'ims-notification-icon-inbox-trigger',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './notification-icon-inbox-trigger.component.html',
  styleUrl: './notification-icon-inbox-trigger.component.scss'
})
export class NotificationIconInboxTriggerComponent {
  @Input() count = 0;
}
