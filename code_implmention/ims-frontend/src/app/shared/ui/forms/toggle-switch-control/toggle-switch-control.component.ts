import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-toggle-switch-control',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './toggle-switch-control.component.html',
  styleUrl: './toggle-switch-control.component.scss'
})
export class ToggleSwitchControlComponent {
  @Input() label: string = "";
  @Input() checked: boolean = false;
}
