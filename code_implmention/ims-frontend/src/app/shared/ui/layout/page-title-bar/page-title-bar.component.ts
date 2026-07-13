import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-page-title-bar',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './page-title-bar.component.html',
  styleUrl: './page-title-bar.component.scss'
})
export class PageTitleBarComponent {
  @Input() title = '';
  @Input() subtitle = '';
}
