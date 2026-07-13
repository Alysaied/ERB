import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'ims-data-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './data-table.component.html',
  styleUrl: './data-table.component.scss'
})
export class DataTableComponent {
  @Input() columns: string[] = [];
  @Input() rows: Record<string, unknown>[] = [];

  get displayColumns(): string[] {
    if (this.columns.length) return this.columns;
    if (this.rows.length) return Object.keys(this.rows[0]);
    return [];
  }
}
