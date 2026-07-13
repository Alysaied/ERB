import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MAIN_NAVIGATION } from '../../../../core/models/navigation.model';

@Component({
  selector: 'ims-main-navigation-bar',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './main-navigation-bar.component.html',
  styleUrl: './main-navigation-bar.component.scss',
})
export class MainNavigationBarComponent {
  readonly navItems = MAIN_NAVIGATION;
}
