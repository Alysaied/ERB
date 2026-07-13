import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-queue-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './queue-list.component.html',
  styleUrl: './queue-list.component.scss'
})
export class QueueListComponent {
  @Input() items: unknown[] = [];
}
