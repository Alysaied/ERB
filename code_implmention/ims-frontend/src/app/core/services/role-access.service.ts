import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, catchError, finalize, of, tap, throwError } from 'rxjs';
import { environment } from '../../../environments/environment';

export type AccessLevel = 'NONE' | 'VIEW' | 'EDIT' | 'APPROVE';
export type ScopeType = 'GLOBAL' | 'REGION' | 'SITE';

export interface PermissionDef {
  id: string;
  label: string;
  group: string;
  sensitive?: boolean;
}

export interface RoleDefinition {
  id: string;
  code: string;
  name: string;
  status: 'ACTIVE' | 'DRAFT';
  privileged: boolean;
  userCount: number;
  scope: ScopeType;
  regions: string[];
  requireMfa: boolean;
  restrictAfterHours: boolean;
  lastUpdatedLabel: string;
  /** permissionId → access level */
  permissions: Record<string, AccessLevel>;
}

export interface SodConflict {
  id: string;
  title: string;
  detail: string;
  leftPermissionId: string;
  rightPermissionId: string;
}

export interface AuthorizationEvaluationResponse {
  authorized: boolean;
  userId: string;
  action: string;
  denialReason: string | null;
}

const LEVEL_RANK: Record<AccessLevel, number> = {
  NONE: 0,
  VIEW: 1,
  EDIT: 2,
  APPROVE: 3,
};

/** Permission catalog aligned to Figma UI-050 groups. */
export const PERMISSION_CATALOG: PermissionDef[] = [
  { id: 'items.view', label: 'View items', group: 'ITEMS & CATALOG' },
  { id: 'items.edit', label: 'Create/edit items', group: 'ITEMS & CATALOG' },
  { id: 'items.pricing', label: 'Modify pricing', group: 'ITEMS & CATALOG', sensitive: true },
  { id: 'items.retire', label: 'Retire SKU', group: 'ITEMS & CATALOG', sensitive: true },

  { id: 'stock.view', label: 'View stock levels', group: 'STOCK OPERATIONS' },
  { id: 'stock.adjust', label: 'Adjust quantities', group: 'STOCK OPERATIONS', sensitive: true },
  { id: 'stock.transfer', label: 'Inter-site transfers', group: 'STOCK OPERATIONS' },
  { id: 'stock.approve_count', label: 'Approve cycle counts', group: 'STOCK OPERATIONS', sensitive: true },

  { id: 'ship.receive', label: 'Record receipts', group: 'RECEIVING & SHIPPING' },
  { id: 'ship.release', label: 'Release shipments', group: 'RECEIVING & SHIPPING' },
  { id: 'ship.void', label: 'Void / reverse shipments', group: 'RECEIVING & SHIPPING', sensitive: true },

  { id: 'proc.create_po', label: 'Create purchase orders', group: 'PROCUREMENT' },
  { id: 'proc.approve_po', label: 'Approve purchase orders', group: 'PROCUREMENT', sensitive: true },
  { id: 'proc.vendors', label: 'Manage vendors', group: 'PROCUREMENT' },

  { id: 'admin.users', label: 'Manage users & roles', group: 'ADMINISTRATION', sensitive: true },
  { id: 'admin.audit', label: 'View audit log', group: 'ADMINISTRATION' },
  { id: 'admin.config', label: 'System configuration', group: 'ADMINISTRATION', sensitive: true },
];

const SOD_RULES: Array<Omit<SodConflict, 'detail'> & { detail: string }> = [
  {
    id: 'sod-po',
    title: 'Create PO ↔ Approve PO',
    detail: 'Both permissions granted at Edit or higher. Downgrade one to View or request exception.',
    leftPermissionId: 'proc.create_po',
    rightPermissionId: 'proc.approve_po',
  },
  {
    id: 'sod-stock',
    title: 'Adjust Stock ↔ Approve Cycle Count',
    detail: 'Both permissions granted at Edit or higher. Downgrade one to View or request exception.',
    leftPermissionId: 'stock.adjust',
    rightPermissionId: 'stock.approve_count',
  },
  {
    id: 'sod-admin',
    title: 'Manage Users ↔ View Audit Log',
    detail: 'Both permissions granted at Edit or higher. Downgrade one to View or request exception.',
    leftPermissionId: 'admin.users',
    rightPermissionId: 'admin.audit',
  },
];

function level(map: Record<string, AccessLevel>, id: string): AccessLevel {
  return map[id] ?? 'NONE';
}

function atLeastEdit(map: Record<string, AccessLevel>, id: string): boolean {
  return LEVEL_RANK[level(map, id)] >= LEVEL_RANK.EDIT;
}

function seedPermissions(overrides: Record<string, AccessLevel>): Record<string, AccessLevel> {
  const base: Record<string, AccessLevel> = {};
  for (const p of PERMISSION_CATALOG) {
    base[p.id] = 'NONE';
  }
  return { ...base, ...overrides };
}

function cloneRoles(roles: RoleDefinition[]): RoleDefinition[] {
  return roles.map((r) => ({
    ...r,
    regions: [...r.regions],
    permissions: { ...r.permissions },
  }));
}

@Injectable({ providedIn: 'root' })
export class RoleAccessService {
  private readonly http = inject(HttpClient);
  private readonly authzUrl = `${environment.apiBaseUrl}/authorization`;

  private readonly rolesSubject = new BehaviorSubject<RoleDefinition[]>(cloneRoles(this.seedRoles()));
  private readonly selectedRoleIdSubject = new BehaviorSubject<string | null>(null);
  private readonly draftSubject = new BehaviorSubject<RoleDefinition | null>(null);
  private readonly conflictsSubject = new BehaviorSubject<SodConflict[]>([]);
  private readonly loadingSubject = new BehaviorSubject<boolean>(false);
  private readonly errorSubject = new BehaviorSubject<string | null>(null);
  private readonly successSubject = new BehaviorSubject<string | null>(null);
  private readonly dirtySubject = new BehaviorSubject<boolean>(false);
  private readonly evaluateResultSubject = new BehaviorSubject<AuthorizationEvaluationResponse | null>(null);

  readonly roles$: Observable<RoleDefinition[]> = this.rolesSubject.asObservable();
  readonly selectedRoleId$: Observable<string | null> = this.selectedRoleIdSubject.asObservable();
  readonly draft$: Observable<RoleDefinition | null> = this.draftSubject.asObservable();
  readonly conflicts$: Observable<SodConflict[]> = this.conflictsSubject.asObservable();
  readonly loading$: Observable<boolean> = this.loadingSubject.asObservable();
  readonly error$: Observable<string | null> = this.errorSubject.asObservable();
  readonly success$: Observable<string | null> = this.successSubject.asObservable();
  readonly dirty$: Observable<boolean> = this.dirtySubject.asObservable();
  readonly evaluateResult$: Observable<AuthorizationEvaluationResponse | null> =
    this.evaluateResultSubject.asObservable();

  readonly permissionCatalog = PERMISSION_CATALOG;
  readonly availableRegions = ['North America', 'EMEA', 'APAC', 'LATAM'];

  get roles(): RoleDefinition[] {
    return this.rolesSubject.value;
  }

  get draft(): RoleDefinition | null {
    return this.draftSubject.value;
  }

  get conflicts(): SodConflict[] {
    return this.conflictsSubject.value;
  }

  get dirty(): boolean {
    return this.dirtySubject.value;
  }

  /** Total assigned users across all roles. */
  get totalAssignedUsers(): number {
    return this.roles.reduce((sum, r) => sum + r.userCount, 0);
  }

  init(): void {
    const roles = this.rolesSubject.value;
    if (roles.length && !this.selectedRoleIdSubject.value) {
      this.selectRole(roles[0].id);
    } else if (this.draft) {
      this.recomputeConflicts(this.draft);
    }
  }

  selectRole(roleId: string): void {
    const role = this.roles.find((r) => r.id === roleId);
    if (!role) {
      return;
    }
    this.selectedRoleIdSubject.next(roleId);
    const draft = {
      ...role,
      regions: [...role.regions],
      permissions: { ...role.permissions },
    };
    this.draftSubject.next(draft);
    this.dirtySubject.next(false);
    this.successSubject.next(null);
    this.errorSubject.next(null);
    this.recomputeConflicts(draft);
  }

  setPermissionLevel(permissionId: string, access: AccessLevel): void {
    const draft = this.draftSubject.value;
    if (!draft) {
      return;
    }
    const next = {
      ...draft,
      permissions: { ...draft.permissions, [permissionId]: access },
    };
    this.draftSubject.next(next);
    this.dirtySubject.next(true);
    this.recomputeConflicts(next);
  }

  setScope(scope: ScopeType): void {
    const draft = this.draftSubject.value;
    if (!draft) {
      return;
    }
    const next: RoleDefinition = {
      ...draft,
      scope,
      regions: scope === 'GLOBAL' ? [] : [...draft.regions],
    };
    this.draftSubject.next(next);
    this.dirtySubject.next(true);
  }

  addRegion(region: string): void {
    const draft = this.draftSubject.value;
    if (!draft || draft.regions.includes(region)) {
      return;
    }
    this.draftSubject.next({ ...draft, regions: [...draft.regions, region] });
    this.dirtySubject.next(true);
  }

  removeRegion(region: string): void {
    const draft = this.draftSubject.value;
    if (!draft) {
      return;
    }
    this.draftSubject.next({
      ...draft,
      regions: draft.regions.filter((r) => r !== region),
    });
    this.dirtySubject.next(true);
  }

  setRequireMfa(value: boolean): void {
    const draft = this.draftSubject.value;
    if (!draft) {
      return;
    }
    this.draftSubject.next({ ...draft, requireMfa: value });
    this.dirtySubject.next(true);
  }

  setRestrictAfterHours(value: boolean): void {
    const draft = this.draftSubject.value;
    if (!draft) {
      return;
    }
    this.draftSubject.next({ ...draft, restrictAfterHours: value });
    this.dirtySubject.next(true);
  }

  updateRoleMeta(patch: Partial<Pick<RoleDefinition, 'name' | 'code' | 'status' | 'privileged'>>): void {
    const draft = this.draftSubject.value;
    if (!draft) {
      return;
    }
    this.draftSubject.next({ ...draft, ...patch });
    this.dirtySubject.next(true);
  }

  resetChanges(): void {
    const id = this.selectedRoleIdSubject.value;
    if (!id) {
      return;
    }
    this.selectRole(id);
    this.successSubject.next('Changes reset');
  }

  /**
   * Local SoD matrix rules (Figma) + backend evaluate probe.
   * Save stays blocked while local conflicts remain.
   */
  validateSod(): void {
    const draft = this.draftSubject.value;
    if (!draft) {
      return;
    }

    this.recomputeConflicts(draft);
    this.loadingSubject.next(true);
    this.errorSubject.next(null);

    this.http
      .post<AuthorizationEvaluationResponse>(`${this.authzUrl}/actions/evaluate`, {
        userId: null,
        action: 'PERM-ADMIN-ROLES',
        resourceType: 'ROLE',
        resourceId: draft.code,
        locationCode: draft.scope === 'GLOBAL' ? 'NETWORK' : draft.regions[0] ?? null,
      })
      .pipe(
        tap((result) => {
          this.evaluateResultSubject.next(result);
          const local = this.conflictsSubject.value;
          if (local.length) {
            this.errorSubject.next(
              `${local.length} SoD conflict(s) still open. Save remains blocked.`
            );
          } else if (!result.authorized) {
            this.errorSubject.next(result.denialReason || 'Authorization evaluate denied this action');
          } else {
            this.successSubject.next('SoD validation passed — no open conflicts');
          }
        }),
        catchError((err) => {
          // Local conflicts still shown even if evaluate API fails
          this.evaluateResultSubject.next(null);
          const local = this.conflictsSubject.value;
          if (local.length) {
            this.errorSubject.next(`${local.length} local SoD conflict(s). Evaluate API unavailable.`);
          } else {
            this.errorSubject.next(this.readError(err, 'Failed to validate SoD with backend'));
          }
          return of(null);
        }),
        finalize(() => this.loadingSubject.next(false))
      )
      .subscribe();
  }

  saveDraft(): void {
    const draft = this.draftSubject.value;
    if (!draft) {
      return;
    }
    this.recomputeConflicts(draft);
    if (this.conflictsSubject.value.length) {
      this.errorSubject.next('Save is blocked until SoD conflicts are resolved');
      return;
    }

    const roles = this.roles.map((r) =>
      r.id === draft.id
        ? {
            ...draft,
            lastUpdatedLabel: 'just now',
            regions: [...draft.regions],
            permissions: { ...draft.permissions },
          }
        : r
    );
    this.rolesSubject.next(roles);
    this.dirtySubject.next(false);
    this.successSubject.next(`Saved role ${draft.name}`);
    this.errorSubject.next(null);
  }

  createRole(name: string, code: string): void {
    const id = `role-${Date.now()}`;
    const role: RoleDefinition = {
      id,
      code: code.trim().toUpperCase().replace(/\s+/g, '_'),
      name: name.trim(),
      status: 'DRAFT',
      privileged: false,
      userCount: 0,
      scope: 'SITE',
      regions: [],
      requireMfa: false,
      restrictAfterHours: false,
      lastUpdatedLabel: 'just now',
      permissions: seedPermissions({}),
    };
    this.rolesSubject.next([...this.roles, role]);
    this.selectRole(id);
    this.dirtySubject.next(true);
    this.successSubject.next(`Draft role ${role.name} created`);
  }

  clearMessages(): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
  }

  isConflictPermission(permissionId: string): boolean {
    return this.conflicts.some(
      (c) => c.leftPermissionId === permissionId || c.rightPermissionId === permissionId
    );
  }

  private recomputeConflicts(draft: RoleDefinition): void {
    const open: SodConflict[] = [];
    for (const rule of SOD_RULES) {
      if (atLeastEdit(draft.permissions, rule.leftPermissionId) && atLeastEdit(draft.permissions, rule.rightPermissionId)) {
        open.push({ ...rule });
      }
    }
    this.conflictsSubject.next(open);
  }

  private readError(err: unknown, fallback: string): string {
    const problem = err as { error?: { detail?: string; title?: string }; message?: string };
    return problem?.error?.detail || problem?.error?.title || problem?.message || fallback;
  }

  private seedRoles(): RoleDefinition[] {
    return [
      {
        id: 'inv-admin',
        code: 'SYSTEM_ADMINISTRATOR',
        name: 'Inventory Administrator',
        status: 'ACTIVE',
        privileged: true,
        userCount: 12,
        scope: 'GLOBAL',
        regions: [],
        requireMfa: true,
        restrictAfterHours: true,
        lastUpdatedLabel: '2 days ago',
        permissions: seedPermissions({
          'items.view': 'APPROVE',
          'items.edit': 'APPROVE',
          'items.pricing': 'APPROVE',
          'items.retire': 'APPROVE',
          'stock.view': 'APPROVE',
          'stock.adjust': 'APPROVE',
          'stock.transfer': 'APPROVE',
          'stock.approve_count': 'APPROVE',
          'ship.receive': 'APPROVE',
          'ship.release': 'APPROVE',
          'ship.void': 'APPROVE',
          'proc.create_po': 'APPROVE',
          'proc.approve_po': 'APPROVE',
          'proc.vendors': 'APPROVE',
          'admin.users': 'APPROVE',
          'admin.audit': 'APPROVE',
          'admin.config': 'APPROVE',
        }),
      },
      {
        id: 'wh-mgr',
        code: 'WAREHOUSE_MANAGER',
        name: 'Warehouse Manager',
        status: 'ACTIVE',
        privileged: false,
        userCount: 34,
        scope: 'SITE',
        regions: [],
        requireMfa: false,
        restrictAfterHours: false,
        lastUpdatedLabel: '5 days ago',
        permissions: seedPermissions({
          'items.view': 'VIEW',
          'stock.view': 'EDIT',
          'stock.adjust': 'EDIT',
          'stock.transfer': 'EDIT',
          'stock.approve_count': 'VIEW',
          'ship.receive': 'EDIT',
          'ship.release': 'EDIT',
          'proc.create_po': 'VIEW',
        }),
      },
      {
        id: 'recv-clerk',
        code: 'RECEIVING_CLERK',
        name: 'Receiving Clerk',
        status: 'ACTIVE',
        privileged: false,
        userCount: 68,
        scope: 'SITE',
        regions: [],
        requireMfa: false,
        restrictAfterHours: false,
        lastUpdatedLabel: '1 week ago',
        permissions: seedPermissions({
          'items.view': 'VIEW',
          'stock.view': 'VIEW',
          'ship.receive': 'EDIT',
        }),
      },
      {
        id: 'cycle-auditor',
        code: 'CYCLE_COUNT_AUDITOR',
        name: 'Cycle Count Auditor',
        status: 'ACTIVE',
        privileged: true,
        userCount: 9,
        scope: 'REGION',
        regions: ['North America'],
        requireMfa: true,
        restrictAfterHours: false,
        lastUpdatedLabel: '3 days ago',
        permissions: seedPermissions({
          'stock.view': 'VIEW',
          'stock.approve_count': 'APPROVE',
          'admin.audit': 'VIEW',
        }),
      },
      {
        id: 'proc-officer',
        code: 'PROCUREMENT_OFFICER',
        name: 'Procurement Officer',
        status: 'ACTIVE',
        privileged: false,
        userCount: 22,
        scope: 'REGION',
        regions: ['EMEA', 'APAC'],
        requireMfa: false,
        restrictAfterHours: false,
        lastUpdatedLabel: '4 days ago',
        permissions: seedPermissions({
          'proc.create_po': 'EDIT',
          'proc.approve_po': 'VIEW',
          'proc.vendors': 'EDIT',
          'items.view': 'VIEW',
        }),
      },
      {
        id: 'ship-coord',
        code: 'SHIPPING_COORDINATOR',
        name: 'Shipping Coordinator',
        status: 'ACTIVE',
        privileged: false,
        userCount: 41,
        scope: 'SITE',
        regions: [],
        requireMfa: false,
        restrictAfterHours: true,
        lastUpdatedLabel: '6 days ago',
        permissions: seedPermissions({
          'ship.release': 'EDIT',
          'ship.void': 'VIEW',
          'stock.view': 'VIEW',
        }),
      },
      {
        id: 'analyst',
        code: 'READ_ONLY_ANALYST',
        name: 'Read-Only Analyst',
        status: 'ACTIVE',
        privileged: false,
        userCount: 87,
        scope: 'GLOBAL',
        regions: [],
        requireMfa: false,
        restrictAfterHours: false,
        lastUpdatedLabel: '2 weeks ago',
        permissions: seedPermissions({
          'items.view': 'VIEW',
          'stock.view': 'VIEW',
          'admin.audit': 'VIEW',
        }),
      },
      {
        id: 'vendor-liaison',
        code: 'VENDOR_LIAISON',
        name: 'Vendor Liaison',
        status: 'DRAFT',
        privileged: false,
        userCount: 0,
        scope: 'REGION',
        regions: ['LATAM'],
        requireMfa: false,
        restrictAfterHours: false,
        lastUpdatedLabel: 'today',
        permissions: seedPermissions({
          'proc.vendors': 'VIEW',
        }),
      },
    ];
  }
}
