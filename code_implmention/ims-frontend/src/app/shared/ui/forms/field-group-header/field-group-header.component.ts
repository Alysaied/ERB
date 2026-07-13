import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-field-group-header',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './field-group-header.component.html',
  styleUrl: './field-group-header.component.scss'
})
export class FieldGroupHeaderComponent {
  @Input() title: string = "";
}
