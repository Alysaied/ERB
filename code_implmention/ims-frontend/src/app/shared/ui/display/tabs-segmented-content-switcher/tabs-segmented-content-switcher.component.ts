import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-tabs-segmented-content-switcher',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './tabs-segmented-content-switcher.component.html',
  styleUrl: './tabs-segmented-content-switcher.component.scss'
})
export class TabsSegmentedContentSwitcherComponent {
  @Input() tabs: string[] = [];
}
