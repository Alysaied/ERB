import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-text-area-notes-field',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './text-area-notes-field.component.html',
  styleUrl: './text-area-notes-field.component.scss'
})
export class TextAreaNotesFieldComponent {
  @Input() label: string = "";
}
