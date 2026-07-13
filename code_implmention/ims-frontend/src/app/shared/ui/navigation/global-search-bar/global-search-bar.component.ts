import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'ims-global-search-bar',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './global-search-bar.component.html',
  styleUrl: './global-search-bar.component.scss'
})
export class GlobalSearchBarComponent {
  query = '';
}
