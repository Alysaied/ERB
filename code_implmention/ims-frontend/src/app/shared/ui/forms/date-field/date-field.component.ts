import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-date-field',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './date-field.component.html',
  styleUrl: './date-field.component.scss'
})
export class DateFieldComponent {
  @Input() label: string = "";
}
