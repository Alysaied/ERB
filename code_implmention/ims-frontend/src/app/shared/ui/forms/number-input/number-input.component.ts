import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-number-input',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './number-input.component.html',
  styleUrl: './number-input.component.scss'
})
export class NumberInputComponent {
  @Input() label: string = "";
}
