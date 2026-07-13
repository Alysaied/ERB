import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'ims-task-approval-shortcut-widget',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './task-approval-shortcut-widget.component.html',
  styleUrl: './task-approval-shortcut-widget.component.scss'
})
export class TaskApprovalShortcutWidgetComponent {
  readonly pendingCount = 15;
  readonly tasks = [
    { label: 'Transfer Approvals', count: 3, route: '/transfers/approvals' },
    { label: 'Variance Approvals', count: 5, route: '/inventory/variances' },
    { label: 'Requisitions', count: 7, route: '/procurement/requisitions' },
  ];
}
