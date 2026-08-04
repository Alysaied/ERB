import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { BehaviorSubject, Observable, catchError, finalize, of, tap, throwError } from 'rxjs';
import { environment } from '../../../environments/environment';

/** One role when creating / assigning (matches RoleAssignmentDto). */
export interface RoleAssignmentRequest {
  roleCode: string;
  locationCodes: string[];
  effectiveFrom?: string | null;
  effectiveTo?: string | null;
}

/** Body for POST /users (matches ProvisionUserAccountRequest). */
export interface ProvisionUserRequest {
  userId: string;
  email: string;
  displayName: string;
  initialRoles: RoleAssignmentRequest[];
  externalDirectoryId?: string | null;
}

/** Role on a loaded user (matches RoleAssignmentResponse). */
export interface RoleAssignment {
  roleAssignmentId: string;
  roleCode: string;
  locationCodes: string[];
  effectiveFrom: string | null;
  effectiveTo: string | null;
}

export interface AuditInfo {
  createdAt: string;
  createdBy: string;
  updatedAt: string;
  updatedBy: string;
}

/** Full user from GET /users/{id} or POST /users. */
export interface UserAccount {
  userId: string;
  email: string;
  displayName: string;
  status: string;
  roles: RoleAssignment[];
  audit: AuditInfo;
  effectiveFrom?: string | null;
  lastActivityAt?: string | null;
}

/** Body for PUT /users/{userId}. */
export interface UpdateUserRequest {
  displayName: string;
  email: string;
  effectiveFrom?: string | null;
}

/** Row in the left list from GET /users. */
export interface UserAccountSummary {
  userId: string;
  email: string;
  displayName: string;
  status: string;
  roles: string[];
  hasSodConflict: boolean;
  lastActivityAt: string | null;
}

/** Matches backend PagedResponse. */
export interface PagedResult<T> {
  data: T[];
  page: number;
  pageSize: number;
  totalElements: number;
  totalPages: number;
}

export interface ListUsersQuery {
  search?: string;
  status?: string;
  roleCode?: string;
  locationCode?: string;
  page?: number;
  pageSize?: number;
  sortBy?: string;
  sortDirection?: 'ASC' | 'DESC';
}

/**
 * UI-049 data layer.
 * HTTP calls push results into BehaviorSubjects.
 * The page subscribes to the public Observables (*$).
 */
@Injectable({ providedIn: 'root' })
export class UserAdminService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = `${environment.apiBaseUrl}/users`;

  // ── private state (only this service can .next()) ─────────────────────────
  private readonly usersSubject = new BehaviorSubject<UserAccountSummary[]>([]);
  private readonly selectedUserSubject = new BehaviorSubject<UserAccount | null>(null);
  private readonly pageInfoSubject = new BehaviorSubject<Omit<PagedResult<unknown>, 'data'>>({
    page: 1,
    pageSize: 20,
    totalElements: 0,
    totalPages: 0,
  });
  private readonly loadingSubject = new BehaviorSubject<boolean>(false);
  private readonly errorSubject = new BehaviorSubject<string | null>(null);
  private readonly successSubject = new BehaviorSubject<string | null>(null);

  /** Remember last list query so create/suspend can refresh the same page. */
  private lastListQuery: ListUsersQuery = {};

  // ── public streams (page uses these) ──────────────────────────────────────
  readonly users$: Observable<UserAccountSummary[]> = this.usersSubject.asObservable();
  readonly selectedUser$: Observable<UserAccount | null> = this.selectedUserSubject.asObservable();
  readonly pageInfo$ = this.pageInfoSubject.asObservable();
  readonly loading$: Observable<boolean> = this.loadingSubject.asObservable();
  readonly error$: Observable<string | null> = this.errorSubject.asObservable();
  readonly success$: Observable<string | null> = this.successSubject.asObservable();

  /** Roles the backend PermissionCatalog currently accepts. */
  readonly knownRoles: ReadonlyArray<{ code: string; name: string; governance?: boolean }> = [
    { code: 'SYSTEM_ADMINISTRATOR', name: 'System Administrator', governance: true },
    { code: 'WAREHOUSE_MANAGER', name: 'Warehouse Manager' },
  ];

  /** Current snapshot helpers (optional, for quick reads). */
  get users(): UserAccountSummary[] {
    return this.usersSubject.value;
  }

  get selectedUser(): UserAccount | null {
    return this.selectedUserSubject.value;
  }

  // ── LEFT panel: load list ─────────────────────────────────────────────────
  loadUsers(query: ListUsersQuery = {}): void {
    this.lastListQuery = query;
    this.errorSubject.next(null);
    this.loadingSubject.next(true);

    let params = new HttpParams()
      .set('page', String(query.page ?? 1))
      .set('pageSize', String(query.pageSize ?? 20))
      .set('sortBy', query.sortBy ?? 'displayName')
      .set('sortDirection', query.sortDirection ?? 'ASC');

    if (query.search) {
      params = params.set('search', query.search);
    }
    if (query.status) {
      params = params.set('status', query.status);
    }
    if (query.roleCode) {
      params = params.set('roleCode', query.roleCode);
    }
    if (query.locationCode) {
      params = params.set('locationCode', query.locationCode);
    }

    this.http
      .get<PagedResult<UserAccountSummary>>(this.baseUrl, { params })
      .pipe(
        tap((result) => {
          this.usersSubject.next(result.data);
          this.pageInfoSubject.next({
            page: result.page,
            pageSize: result.pageSize,
            totalElements: result.totalElements,
            totalPages: result.totalPages,
          });
        }),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to load users'));
          this.usersSubject.next([]);
          return of(null);
        }),
        finalize(() => this.loadingSubject.next(false))
      )
      .subscribe();
  }

  // ── RIGHT panel: load one user ────────────────────────────────────────────
  loadUser(userId: string): void {
    this.errorSubject.next(null);
    this.loadingSubject.next(true);

    this.http
      .get<UserAccount>(`${this.baseUrl}/${encodeURIComponent(userId)}`)
      .pipe(
        tap((user) => this.selectedUserSubject.next(user)),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to load user'));
          this.selectedUserSubject.next(null);
          return of(null);
        }),
        finalize(() => this.loadingSubject.next(false))
      )
      .subscribe();
  }

  clearSelectedUser(): void {
    this.selectedUserSubject.next(null);
  }

  clearMessages(): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
  }

  // ── Create User ───────────────────────────────────────────────────────────
  createUser(request: ProvisionUserRequest): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
    this.loadingSubject.next(true);

    this.http
      .post<UserAccount>(this.baseUrl, request)
      .pipe(
        tap((created) => {
          this.selectedUserSubject.next(created);
          this.successSubject.next(`User ${created.displayName} created`);
          this.loadUsers(this.lastListQuery);
        }),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to create user'));
          this.loadingSubject.next(false);
          return throwError(() => err);
        })
      )
      .subscribe({ error: () => undefined });
  }

  // ── Sync from directory ───────────────────────────────────────────────────
  syncUsers(syncMode = 'FULL', dryRun = false): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
    this.loadingSubject.next(true);

    this.http
      .post<{
        syncMode: string;
        usersCreated: number;
        usersUpdated: number;
        usersDeactivated: number;
        syncedAt: string;
      }>(`${this.baseUrl}/sync`, {
        syncMode,
        sinceTimestamp: syncMode === 'INCREMENTAL' ? new Date(0).toISOString() : null,
        dryRun,
      })
      .pipe(
        tap((result) => {
          this.successSubject.next(
            `Sync complete: ${result.usersCreated} created, ${result.usersUpdated} updated, ${result.usersDeactivated} deactivated`
          );
          this.loadUsers(this.lastListQuery);
        }),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to sync users'));
          this.loadingSubject.next(false);
          return throwError(() => err);
        })
      )
      .subscribe({ error: () => undefined });
  }

  // ── Update profile (Save) ─────────────────────────────────────────────────
  updateUser(userId: string, request: UpdateUserRequest): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
    this.loadingSubject.next(true);

    this.http
      .put<UserAccount>(`${this.baseUrl}/${encodeURIComponent(userId)}`, request)
      .pipe(
        tap((updated) => {
          this.selectedUserSubject.next(updated);
          this.successSubject.next(`Saved changes for ${updated.displayName}`);
          this.loadUsers(this.lastListQuery);
        }),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to save user'));
          this.loadingSubject.next(false);
          return throwError(() => err);
        })
      )
      .subscribe({ error: () => undefined });
  }

  // ── Assign / revoke role ──────────────────────────────────────────────────
  assignRole(userId: string, roleAssignment: RoleAssignmentRequest): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
    this.loadingSubject.next(true);

    this.http
      .post<RoleAssignment>(`${this.baseUrl}/${encodeURIComponent(userId)}/roles`, {
        roleAssignment,
      })
      .pipe(
        tap(() => {
          this.successSubject.next(`Role ${roleAssignment.roleCode} assigned`);
          this.loadUser(userId);
        }),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to assign role'));
          this.loadingSubject.next(false);
          return throwError(() => err);
        })
      )
      .subscribe({ error: () => undefined });
  }

  revokeRole(userId: string, roleAssignmentId: string): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
    this.loadingSubject.next(true);

    this.http
      .delete(`${this.baseUrl}/${encodeURIComponent(userId)}/roles/${roleAssignmentId}`)
      .pipe(
        tap(() => {
          this.successSubject.next('Role revoked');
          this.loadUser(userId);
        }),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to revoke role'));
          this.loadingSubject.next(false);
          return throwError(() => err);
        })
      )
      .subscribe({ error: () => undefined });
  }

  // ── Suspend / Deactivate ──────────────────────────────────────────────────
  suspendUser(userId: string, suspensionReason: string, suspendedUntil?: string | null): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
    this.loadingSubject.next(true);

    this.http
      .post<UserAccount>(`${this.baseUrl}/${encodeURIComponent(userId)}/suspend`, {
        suspensionReason,
        suspendedUntil: suspendedUntil ?? null,
      })
      .pipe(
        tap((user) => {
          this.selectedUserSubject.next(user);
          this.successSubject.next(`User ${user.displayName} suspended`);
          this.loadUsers(this.lastListQuery);
        }),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to suspend user'));
          this.loadingSubject.next(false);
          return throwError(() => err);
        })
      )
      .subscribe({ error: () => undefined });
  }

  deactivateUser(userId: string, deactivationReason: string, effectiveDate?: string | null): void {
    this.errorSubject.next(null);
    this.successSubject.next(null);
    this.loadingSubject.next(true);

    this.http
      .post<UserAccount>(`${this.baseUrl}/${encodeURIComponent(userId)}/deactivate`, {
        deactivationReason,
        effectiveDate: effectiveDate ?? null,
      })
      .pipe(
        tap((user) => {
          this.selectedUserSubject.next(user);
          this.successSubject.next(`User ${user.displayName} deactivated`);
          this.loadUsers(this.lastListQuery);
        }),
        catchError((err) => {
          this.errorSubject.next(this.readError(err, 'Failed to deactivate user'));
          this.loadingSubject.next(false);
          return throwError(() => err);
        })
      )
      .subscribe({ error: () => undefined });
  }

  roleDisplayName(roleCode: string): string {
    return this.knownRoles.find((r) => r.code === roleCode)?.name ?? roleCode.replaceAll('_', ' ');
  }

  isGovernanceRole(roleCode: string): boolean {
    return !!this.knownRoles.find((r) => r.code === roleCode)?.governance
      || roleCode.includes('AUDIT')
      || roleCode.includes('ADMIN');
  }

  private readError(err: unknown, fallback: string): string {
    const problem = err as { error?: { detail?: string; title?: string }; message?: string };
    return problem?.error?.detail || problem?.error?.title || problem?.message || fallback;
  }
}
