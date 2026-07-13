import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-validation-message-block',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './validation-message-block.component.html',
  styleUrl: './validation-message-block.component.scss'
})
export class ValidationMessageBlockComponent {
  @Input() message: string = "";
}
