import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-step-progress-indicator',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './step-progress-indicator.component.html',
  styleUrl: './step-progress-indicator.component.scss'
})
export class StepProgressIndicatorComponent {
  @Input() steps: string[] = [];
  @Input() currentStep: number = 0;
}
