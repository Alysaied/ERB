import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-dropdown-select-control',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dropdown-select-control.component.html',
  styleUrl: './dropdown-select-control.component.scss'
})
export class DropdownSelectControlComponent {
  @Input() label: string = "";
  @Input() options: string[] = [];
}
