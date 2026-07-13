import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-trend-indicator',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './trend-indicator.component.html',
  styleUrl: './trend-indicator.component.scss'
})
export class TrendIndicatorComponent {
  @Input() direction: 'up' | 'down' | 'flat' = "flat";
  @Input() value: string = "";
}
