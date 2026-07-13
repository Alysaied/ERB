import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-footer-metadata-strip',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './footer-metadata-strip.component.html',
  styleUrl: './footer-metadata-strip.component.scss'
})
export class FooterMetadataStripComponent {
  readonly version = '1.0.0-mvp';
  readonly lastRefresh = new Date().toLocaleString();
}
