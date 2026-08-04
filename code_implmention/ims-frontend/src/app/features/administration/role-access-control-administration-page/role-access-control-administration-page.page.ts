import { Component, OnDestroy, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Subscription } from 'rxjs';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { SuccessWarningErrorBannerComponent } from '../../../shared/ui/feedback/success-warning-error-banner/success-warning-error-banner.component';
import { StatusBadgeComponent } from '../../../shared/ui/display/status-badge/status-badge.component';
import {
  AccessLevel,
  AuthorizationEvaluationResponse,
  PERMISSION_CATALOG,
  PermissionDef,
  RoleAccessService,
  RoleDefinition,
  ScopeType,
  SodConflict,
} from '../../../core/services/role-access.service';

@Component({
  selector: 'ims-role-access-control-administration-page',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    PageTitleBarComponent,
    BreadcrumbTrailComponent,
    SuccessWarningErrorBannerComponent,
    StatusBadgeComponent,
  ],
  templateUrl: './role-access-control-administration-page.page.html',
  styleUrl: './role-access-control-administration-page.page.scss',
})
export class RoleAccessControlAdministrationPage implements OnInit, OnDestroy {
  private readonly roleAccess = inject(RoleAccessService);
  private readonly subscriptions = new Subscription();

  readonly screenId = 'UI-050';
  readonly title = 'Role & Access Control';
  readonly description = 'Define roles, assign permissions, and enforce separation of duties across sites.';
  readonly accessLevels: AccessLevel[] = ['NONE', 'VIEW', 'EDIT', 'APPROVE'];
  readonly scopeTypes: ScopeType[] = ['GLOBAL', 'REGION', 'SITE'];

  roles: RoleDefinition[] = [];
  selectedRoleId: string | null = null;
  draft: RoleDefinition | null = null;
  conflicts: SodConflict[] = [];
  loading = false;
  dirty = false;
  errorMessage: string | null = null;
  successMessage: string | null = null;
  evaluateResult: AuthorizationEvaluationResponse | null = null;

  roleSearch = '';
  showConflictBanner = true;
  showNewRoleModal = false;
  newRoleName = '';
  newRoleCode = '';
  regionToAdd = '';

  /** Legend highlight in Figma (Approve selected). */
  legendFocus: AccessLevel = 'APPROVE';

  ngOnInit(): void {
    this.subscriptions.add(this.roleAccess.roles$.subscribe((roles) => (this.roles = roles)));
    this.subscriptions.add(
      this.roleAccess.selectedRoleId$.subscribe((id) => (this.selectedRoleId = id))
    );
    this.subscriptions.add(this.roleAccess.draft$.subscribe((draft) => (this.draft = draft)));
    this.subscriptions.add(
      this.roleAccess.conflicts$.subscribe((conflicts) => (this.conflicts = conflicts))
    );
    this.subscriptions.add(this.roleAccess.loading$.subscribe((loading) => (this.loading = loading)));
    this.subscriptions.add(this.roleAccess.dirty$.subscribe((dirty) => (this.dirty = dirty)));
    this.subscriptions.add(this.roleAccess.error$.subscribe((error) => (this.errorMessage = error)));
    this.subscriptions.add(
      this.roleAccess.success$.subscribe((message) => (this.successMessage = message))
    );
    this.subscriptions.add(
      this.roleAccess.evaluateResult$.subscribe((result) => (this.evaluateResult = result))
    );

    this.roleAccess.init();
  }

  ngOnDestroy(): void {
    this.subscriptions.unsubscribe();
  }

  get filteredRoles(): RoleDefinition[] {
    const q = this.roleSearch.trim().toLowerCase();
    if (!q) {
      return this.roles;
    }
    return this.roles.filter(
      (r) => r.name.toLowerCase().includes(q) || r.code.toLowerCase().includes(q)
    );
  }

  get totalAssignedUsers(): number {
    return this.roleAccess.totalAssignedUsers;
  }

  get permissionGroups(): Array<{ group: string; permissions: PermissionDef[] }> {
    const map = new Map<string, PermissionDef[]>();
    for (const p of PERMISSION_CATALOG) {
      const list = map.get(p.group) ?? [];
      list.push(p);
      map.set(p.group, list);
    }
    return Array.from(map.entries()).map(([group, permissions]) => ({ group, permissions }));
  }

  get availableRegionsToAdd(): string[] {
    const selected = new Set(this.draft?.regions ?? []);
    return this.roleAccess.availableRegions.filter((r) => !selected.has(r));
  }

  get saveBlocked(): boolean {
    return this.conflicts.length > 0;
  }

  onSelectRole(roleId: string): void {
    this.roleAccess.clearMessages();
    this.showConflictBanner = true;
    this.roleAccess.selectRole(roleId);
  }

  onSetLevel(permissionId: string, level: AccessLevel): void {
    this.roleAccess.setPermissionLevel(permissionId, level);
  }

  onSetScope(scope: ScopeType): void {
    this.roleAccess.setScope(scope);
  }

  onAddRegion(): void {
    if (!this.regionToAdd) {
      return;
    }
    this.roleAccess.addRegion(this.regionToAdd);
    this.regionToAdd = '';
  }

  onRemoveRegion(region: string): void {
    this.roleAccess.removeRegion(region);
  }

  onToggleMfa(value: boolean): void {
    this.roleAccess.setRequireMfa(value);
  }

  onToggleAfterHours(value: boolean): void {
    this.roleAccess.setRestrictAfterHours(value);
  }

  onValidateSod(): void {
    this.roleAccess.validateSod();
  }

  onReset(): void {
    this.roleAccess.resetChanges();
  }

  onSave(): void {
    this.roleAccess.saveDraft();
  }

  openNewRoleModal(): void {
    this.newRoleName = '';
    this.newRoleCode = '';
    this.showNewRoleModal = true;
  }

  closeNewRoleModal(): void {
    this.showNewRoleModal = false;
  }

  submitNewRole(): void {
    if (!this.newRoleName.trim() || !this.newRoleCode.trim()) {
      return;
    }
    this.roleAccess.createRole(this.newRoleName, this.newRoleCode);
    this.showNewRoleModal = false;
  }

  dismissConflictBanner(): void {
    this.showConflictBanner = false;
  }

  levelOf(permissionId: string): AccessLevel {
    return this.draft?.permissions[permissionId] ?? 'NONE';
  }

  isConflictRow(permissionId: string): boolean {
    return this.roleAccess.isConflictPermission(permissionId);
  }

  scopeLabel(scope: ScopeType): string {
    switch (scope) {
      case 'GLOBAL':
        return 'Global';
      case 'REGION':
        return 'Region';
      case 'SITE':
        return 'Site';
    }
  }

  levelShort(level: AccessLevel): string {
    switch (level) {
      case 'NONE':
        return 'N';
      case 'VIEW':
        return 'V';
      case 'EDIT':
        return 'E';
      case 'APPROVE':
        return 'A';
    }
  }

  resolveConflict(conflict: SodConflict): void {
    // Downgrade the right-hand permission to VIEW (common resolve path from Figma copy)
    this.roleAccess.setPermissionLevel(conflict.rightPermissionId, 'VIEW');
    this.successMessage = `Resolved by downgrading right side of “${conflict.title}” to View`;
  }

  groupIcon(group: string): string {
    if (group.startsWith('ITEMS')) {
      return 'bi-box-seam';
    }
    if (group.startsWith('STOCK')) {
      return 'bi-boxes';
    }
    if (group.startsWith('RECEIVING')) {
      return 'bi-truck';
    }
    if (group.startsWith('PROCUREMENT')) {
      return 'bi-cart3';
    }
    return 'bi-shield-lock';
  }
}
