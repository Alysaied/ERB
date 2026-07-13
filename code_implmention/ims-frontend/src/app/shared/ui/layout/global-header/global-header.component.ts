import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { GlobalSearchBarComponent } from '../../navigation/global-search-bar/global-search-bar.component';
import { NotificationIconInboxTriggerComponent } from '../../navigation/notification-icon-inbox-trigger/notification-icon-inbox-trigger.component';
import { UserMenuComponent } from '../../navigation/user-menu/user-menu.component';
import { SessionContextBadgeComponent } from '../session-context-badge/session-context-badge.component';
import { AuthService } from '../../../../core/services/auth.service';

@Component({
  selector: 'ims-global-header',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    GlobalSearchBarComponent,
    NotificationIconInboxTriggerComponent,
    UserMenuComponent,
    SessionContextBadgeComponent,
  ],
  templateUrl: './global-header.component.html',
  styleUrl: './global-header.component.scss',
})
export class GlobalHeaderComponent {
  readonly auth = inject(AuthService);
  readonly notificationCount = 12;
}
