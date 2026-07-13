import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-kpi-summary-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './kpi-summary-card.component.html',
  styleUrl: './kpi-summary-card.component.scss'
})
export class KpiSummaryCardComponent {
  @Input() label: string = "";
  @Input() value: string | number = "";
  @Input() trend: string = "";
}
