import { Component, OnDestroy, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Subscription } from 'rxjs';
import { PageTitleBarComponent } from '../../../shared/ui/layout/page-title-bar/page-title-bar.component';
import { BreadcrumbTrailComponent } from '../../../shared/ui/layout/breadcrumb-trail/breadcrumb-trail.component';
import { SuccessWarningErrorBannerComponent } from '../../../shared/ui/feedback/success-warning-error-banner/success-warning-error-banner.component';
import { StatusBadgeComponent } from '../../../shared/ui/display/status-badge/status-badge.component';
import {
  ProvisionUserRequest,
  UserAccount,
  UserAccountSummary,
  UserAdminService,
} from '../../../core/services/user-admin.service';

type ReasonModalMode = 'suspend' | 'deactivate' | null;

@Component({
  selector: 'ims-user-account-management-page',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    PageTitleBarComponent,
    BreadcrumbTrailComponent,
    SuccessWarningErrorBannerComponent,
    StatusBadgeComponent,
  ],
  templateUrl: './user-account-management-page.page.html',
  styleUrl: './user-account-management-page.page.scss',
})
export class UserAccountManagementPage implements OnInit, OnDestroy {
  private readonly usersApi = inject(UserAdminService);
  private readonly subscriptions = new Subscription();

  readonly screenId = 'UI-049';
  readonly title = 'User Account Management';
  readonly description =
    'Manage identities, role assignments, and access lifecycle across the inventory platform.';
  readonly knownRoles = this.usersApi.knownRoles;

  users: UserAccountSummary[] = [];
  selectedUser: UserAccount | null = null;
  loading = false;
  errorMessage: string | null = null;
  successMessage: string | null = null;
  page = 1;
  pageSize = 8;
  totalPages = 0;
  totalElements = 0;
  searchTerm = '';

  formDisplayName = '';
  formEmail = '';
  formEffectiveFrom = '';
  formEffectiveTo = '';
  newRoleCode = '';
  newRoleLocations = 'ALL';

  showCreateModal = false;
  createForm: ProvisionUserRequest = this.emptyCreateForm();
  createLocationsText = 'ALL';

  reasonModalMode: ReasonModalMode = null;
  reasonText = '';
  reasonUntil = '';

  private autoSelectEnabled = true;

  ngOnInit(): void {
    this.subscriptions.add(
      this.usersApi.users$.subscribe((users) => {
        this.users = users;
        if (this.autoSelectEnabled && !this.selectedUser && users.length > 0) {
          this.autoSelectEnabled = false;
          this.usersApi.loadUser(users[0].userId);
        }
      })
    );

    this.subscriptions.add(
      this.usersApi.selectedUser$.subscribe((user) => {
        this.selectedUser = user;
        this.syncFormFromSelected(user);
      })
    );

    this.subscriptions.add(
      this.usersApi.loading$.subscribe((loading) => {
        this.loading = loading;
      })
    );

    this.subscriptions.add(
      this.usersApi.error$.subscribe((error) => {
        this.errorMessage = error;
      })
    );

    this.subscriptions.add(
      this.usersApi.success$.subscribe((message) => {
        this.successMessage = message;
      })
    );

    this.subscriptions.add(
      this.usersApi.pageInfo$.subscribe((info) => {
        this.page = info.page;
        this.pageSize = info.pageSize;
        this.totalPages = info.totalPages;
        this.totalElements = info.totalElements;
      })
    );

    this.reloadList();
  }

  ngOnDestroy(): void {
    this.subscriptions.unsubscribe();
  }

  get isDirty(): boolean {
    if (!this.selectedUser) {
      return false;
    }
    const originalFrom = this.toDateInput(this.selectedUser.effectiveFrom);
    return (
      this.formDisplayName.trim() !== (this.selectedUser.displayName || '') ||
      this.formEmail.trim() !== (this.selectedUser.email || '') ||
      this.formEffectiveFrom !== originalFrom ||
      !!this.newRoleCode
    );
  }

  reloadList(): void {
    this.usersApi.loadUsers({
      page: this.page,
      pageSize: this.pageSize,
      search: this.searchTerm.trim() || undefined,
    });
  }

  onSearch(): void {
    this.page = 1;
    this.autoSelectEnabled = true;
    this.usersApi.clearSelectedUser();
    this.reloadList();
  }

  onSelectUser(userId: string): void {
    this.autoSelectEnabled = false;
    this.usersApi.clearMessages();
    this.usersApi.loadUser(userId);
  }

  onPrevPage(): void {
    if (this.page <= 1) {
      return;
    }
    this.page -= 1;
    this.autoSelectEnabled = true;
    this.usersApi.clearSelectedUser();
    this.reloadList();
  }

  onNextPage(): void {
    if (this.page >= this.totalPages) {
      return;
    }
    this.page += 1;
    this.autoSelectEnabled = true;
    this.usersApi.clearSelectedUser();
    this.reloadList();
  }

  onSyncUsers(): void {
    this.usersApi.syncUsers('FULL', false);
  }

  openCreateModal(): void {
    this.createForm = this.emptyCreateForm();
    this.createLocationsText = 'ALL';
    this.showCreateModal = true;
  }

  closeCreateModal(): void {
    this.showCreateModal = false;
  }

  submitCreate(): void {
    if (!this.createForm.userId.trim() || !this.createForm.email.trim() || !this.createForm.displayName.trim()) {
      this.errorMessage = 'User ID, display name, and email are required';
      return;
    }
    const body: ProvisionUserRequest = {
      userId: this.createForm.userId.trim(),
      email: this.createForm.email.trim(),
      displayName: this.createForm.displayName.trim(),
      initialRoles: [
        {
          roleCode: this.createForm.initialRoles[0].roleCode,
          locationCodes: this.parseLocations(this.createLocationsText),
          effectiveFrom: null,
          effectiveTo: null,
        },
      ],
      externalDirectoryId: null,
    };
    this.usersApi.createUser(body);
    this.showCreateModal = false;
  }

  openSuspendModal(): void {
    if (!this.selectedUser || !this.isActive(this.selectedUser.status)) {
      return;
    }
    this.reasonModalMode = 'suspend';
    this.reasonText = '';
    this.reasonUntil = '';
  }

  openDeactivateModal(): void {
    if (!this.selectedUser || this.isDeactivated(this.selectedUser.status)) {
      return;
    }
    this.reasonModalMode = 'deactivate';
    this.reasonText = '';
    this.reasonUntil = '';
  }

  closeReasonModal(): void {
    this.reasonModalMode = null;
    this.reasonText = '';
    this.reasonUntil = '';
  }

  submitReasonModal(): void {
    if (!this.selectedUser || !this.reasonText.trim()) {
      return;
    }
    if (this.reasonModalMode === 'suspend') {
      this.usersApi.suspendUser(
        this.selectedUser.userId,
        this.reasonText.trim(),
        this.reasonUntil || null
      );
    } else if (this.reasonModalMode === 'deactivate') {
      this.usersApi.deactivateUser(
        this.selectedUser.userId,
        this.reasonText.trim(),
        this.reasonUntil || null
      );
    }
    this.closeReasonModal();
  }

  onAddRole(): void {
    if (!this.selectedUser || !this.newRoleCode) {
      return;
    }
    this.usersApi.assignRole(this.selectedUser.userId, {
      roleCode: this.newRoleCode,
      locationCodes: this.parseLocations(this.newRoleLocations),
      effectiveFrom: this.formEffectiveFrom || null,
      effectiveTo: this.formEffectiveTo || null,
    });
    this.newRoleCode = '';
    this.newRoleLocations = 'ALL';
  }

  onRevokeRole(roleAssignmentId: string): void {
    if (!this.selectedUser) {
      return;
    }
    this.usersApi.revokeRole(this.selectedUser.userId, roleAssignmentId);
  }

  onSave(): void {
    if (!this.selectedUser) {
      return;
    }
    if (this.newRoleCode) {
      this.onAddRole();
    }
    this.usersApi.updateUser(this.selectedUser.userId, {
      displayName: this.formDisplayName.trim(),
      email: this.formEmail.trim(),
      effectiveFrom: this.formEffectiveFrom || null,
    });
  }

  initials(name: string): string {
    return name
      .split(/\s+/)
      .filter(Boolean)
      .slice(0, 2)
      .map((part) => part[0]?.toUpperCase() ?? '')
      .join('');
  }

  statusVariant(status: string): 'success' | 'warning' | 'danger' | 'neutral' {
    const normalized = (status || '').toUpperCase();
    if (normalized === 'ACTIVE') {
      return 'success';
    }
    if (normalized === 'SUSPENDED') {
      return 'warning';
    }
    if (normalized === 'DEACTIVATED') {
      return 'danger';
    }
    return 'neutral';
  }

  statusLabel(status: string): string {
    const normalized = (status || '').toUpperCase();
    if (normalized === 'SUSPENDED') {
      return 'Suspend';
    }
    if (normalized === 'DEACTIVATED') {
      return 'Deactivate';
    }
    if (normalized === 'ACTIVE') {
      return 'Active';
    }
    return status;
  }

  isActive(status: string): boolean {
    return (status || '').toUpperCase() === 'ACTIVE';
  }

  isDeactivated(status: string): boolean {
    return (status || '').toUpperCase() === 'DEACTIVATED';
  }

  roleName(roleCode: string): string {
    return this.usersApi.roleDisplayName(roleCode);
  }

  isGovernance(roleCode: string): boolean {
    return this.usersApi.isGovernanceRole(roleCode);
  }

  hasGovernanceRole(user: UserAccount): boolean {
    return user.roles.some((role) => this.isGovernance(role.roleCode));
  }

  formatDate(value: string | null | undefined): string {
    if (!value) {
      return '—';
    }
    return value.includes('T') ? value.slice(0, 10) : value;
  }

  formatDateTime(value: string | null | undefined): string {
    if (!value) {
      return '—';
    }
    const d = new Date(value);
    if (Number.isNaN(d.getTime())) {
      return value;
    }
    const pad = (n: number) => String(n).padStart(2, '0');
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
  }

  primaryRoleLabel(user: UserAccountSummary): string {
    if (!user.roles?.length) {
      return 'No role';
    }
    const first = this.roleName(user.roles[0]);
    const extra = user.roles.length > 1 ? ` +${user.roles.length - 1}` : '';
    return `${first}${extra}`;
  }

  lastActivityFor(user: UserAccount): string | null {
    return user.lastActivityAt ?? this.users.find((u) => u.userId === user.userId)?.lastActivityAt ?? null;
  }

  get reasonModalTitle(): string {
    return this.reasonModalMode === 'suspend' ? 'Suspend user' : 'Deactivate user';
  }

  private syncFormFromSelected(user: UserAccount | null): void {
    if (!user) {
      this.formDisplayName = '';
      this.formEmail = '';
      this.formEffectiveFrom = '';
      this.formEffectiveTo = '';
      return;
    }
    this.formDisplayName = user.displayName;
    this.formEmail = user.email;
    this.formEffectiveFrom = this.toDateInput(user.effectiveFrom);
    const firstRole = user.roles[0];
    this.formEffectiveTo = this.toDateInput(firstRole?.effectiveTo);
  }

  private toDateInput(value: string | null | undefined): string {
    if (!value) {
      return '';
    }
    return value.includes('T') ? value.slice(0, 10) : value;
  }

  private parseLocations(raw: string): string[] {
    const parts = raw
      .split(',')
      .map((p) => p.trim())
      .filter(Boolean);
    return parts.length ? parts : ['ALL'];
  }

  private emptyCreateForm(): ProvisionUserRequest {
    return {
      userId: '',
      email: '',
      displayName: '',
      initialRoles: [
        {
          roleCode: 'WAREHOUSE_MANAGER',
          locationCodes: ['ALL'],
          effectiveFrom: null,
          effectiveTo: null,
        },
      ],
      externalDirectoryId: null,
    };
  }
}
