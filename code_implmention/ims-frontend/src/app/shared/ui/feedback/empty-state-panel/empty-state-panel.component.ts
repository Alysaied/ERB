import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-empty-state-panel',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './empty-state-panel.component.html',
  styleUrl: './empty-state-panel.component.scss'
})
export class EmptyStatePanelComponent {
  @Input() title: string = "No data";
  @Input() message: string = "";
}
