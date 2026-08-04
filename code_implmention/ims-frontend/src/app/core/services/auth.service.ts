import { Injectable, signal, computed, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { firstValueFrom } from 'rxjs';
import { environment } from '../../../environments/environment';

export interface SessionUser {
  id: string;
  email: string;
  name: string;
  roles: string[];
  locationScope: string;
  permissions: string[];
}

interface TokenResponse {
  accessToken: string;
  tokenType: string;
  expiresAt: string;
  session: SessionResponse;
}

interface SessionResponse {
  userId: string;
  email: string;
  displayName: string;
  roles: string[];
  locationScope: string[];
  permissions: string[];
  sessionExpiresAt: string;
}

interface LogoutResponse {
  loggedOut: boolean;
  loggedOutAt: string;
}

const TOKEN_KEY = 'ims-access-token';
const SESSION_KEY = 'ims-session';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly http = inject(HttpClient);
  private readonly router = inject(Router);

  private readonly _user = signal<SessionUser | null>(null);
  private readonly _token = signal<string | null>(null);

  readonly user = this._user.asReadonly();
  readonly accessToken = this._token.asReadonly();
  readonly isAuthenticated = computed(() => this._user() !== null && !!this._token());

  constructor() {
    const storedToken =
      sessionStorage.getItem(TOKEN_KEY) ?? localStorage.getItem(TOKEN_KEY);
    const storedSession =
      sessionStorage.getItem(SESSION_KEY) ?? localStorage.getItem(SESSION_KEY);
    if (storedToken && storedSession) {
      try {
        this._token.set(storedToken);
        this._user.set(JSON.parse(storedSession) as SessionUser);
      } catch {
        this.clearSession();
      }
    }
  }

  async signIn(email: string, password: string, rememberMe = false): Promise<boolean> {
    try {
      const response = await firstValueFrom(
        this.http.post<TokenResponse>(`${environment.apiBaseUrl}/auth/token`, { email, password })
      );
      this.persistSession(response.accessToken, this.toSessionUser(response.session), rememberMe);
      return true;
    } catch {
      return false;
    }
  }

  async signOut(): Promise<void> {
    const token = this._token();
    if (token) {
      try {
        await firstValueFrom(
          this.http.post<LogoutResponse>(`${environment.apiBaseUrl}/auth/logout`, {})
        );
      } catch {
        // Local clear still required if API is unreachable
      }
    }
    this.clearSession();
    this.router.navigate(['/auth/sign-in']);
  }

  clearSession(): void {
    this._user.set(null);
    this._token.set(null);
    sessionStorage.removeItem(TOKEN_KEY);
    sessionStorage.removeItem(SESSION_KEY);
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(SESSION_KEY);
  }

  private persistSession(token: string, user: SessionUser, rememberMe = false): void {
    this._token.set(token);
    this._user.set(user);
    const storage = rememberMe ? localStorage : sessionStorage;
    const other = rememberMe ? sessionStorage : localStorage;
    other.removeItem(TOKEN_KEY);
    other.removeItem(SESSION_KEY);
    storage.setItem(TOKEN_KEY, token);
    storage.setItem(SESSION_KEY, JSON.stringify(user));
  }

  private toSessionUser(session: SessionResponse): SessionUser {
    return {
      id: session.userId,
      email: session.email,
      name: session.displayName,
      roles: session.roles ?? [],
      locationScope: (session.locationScope ?? []).join(', ') || 'NONE',
      permissions: session.permissions ?? [],
    };
  }
}
