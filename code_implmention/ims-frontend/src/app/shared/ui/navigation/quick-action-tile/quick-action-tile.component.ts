import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'ims-quick-action-tile',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './quick-action-tile.component.html',
  styleUrl: './quick-action-tile.component.scss'
})
export class QuickActionTileComponent {
  @Input() label = '';
  @Input() route = '';
}
