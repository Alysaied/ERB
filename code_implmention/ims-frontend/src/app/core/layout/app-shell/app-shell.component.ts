import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { GlobalHeaderComponent } from '../../../shared/ui/layout/global-header/global-header.component';
import { MainNavigationBarComponent } from '../../../shared/ui/layout/main-navigation-bar/main-navigation-bar.component';
import { SecondaryNavigationPanelComponent } from '../../../shared/ui/layout/secondary-navigation-panel/secondary-navigation-panel.component';
import { FooterMetadataStripComponent } from '../../../shared/ui/layout/footer-metadata-strip/footer-metadata-strip.component';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'ims-app-shell',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    GlobalHeaderComponent,
    MainNavigationBarComponent,
    SecondaryNavigationPanelComponent,
    FooterMetadataStripComponent,
  ],
  templateUrl: './app-shell.component.html',
  styleUrl: './app-shell.component.scss',
})
export class AppShellComponent {
  readonly auth = inject(AuthService);
}
