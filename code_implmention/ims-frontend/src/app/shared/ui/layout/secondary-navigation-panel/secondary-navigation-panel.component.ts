import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterModule, NavigationEnd } from '@angular/router';
import { filter } from 'rxjs/operators';
import { MAIN_NAVIGATION, NavItem } from '../../../../core/models/navigation.model';

@Component({
  selector: 'ims-secondary-navigation-panel',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './secondary-navigation-panel.component.html',
  styleUrl: './secondary-navigation-panel.component.scss',
})
export class SecondaryNavigationPanelComponent {
  private readonly router = inject(Router);
  activeModule: NavItem | null = null;

  constructor() {
    this.updateActiveModule(this.router.url);
    this.router.events
      .pipe(filter((e): e is NavigationEnd => e instanceof NavigationEnd))
      .subscribe((e) => this.updateActiveModule(e.urlAfterRedirects));
  }

  private updateActiveModule(url: string): void {
    this.activeModule =
      MAIN_NAVIGATION.find(
        (m) => url.startsWith(m.route.split('/').slice(0, 2).join('/')) || url.startsWith('/' + m.label.toLowerCase())
      ) ??
      MAIN_NAVIGATION.find((m) => m.children?.some((c) => url.startsWith(c.route))) ??
      null;

    if (!this.activeModule) {
      const segment = '/' + url.split('/').filter(Boolean).slice(0, 2).join('/');
      this.activeModule = MAIN_NAVIGATION.find((m) => m.children?.some((c) => c.route.startsWith(segment))) ?? null;
    }
  }
}
