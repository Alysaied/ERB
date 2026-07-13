import { TestBed } from '@angular/core/testing';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { AuthService } from './auth.service';
import { environment } from '../../../environments/environment';

describe('AuthService', () => {
  let service: AuthService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    sessionStorage.clear();
    TestBed.configureTestingModule({
      providers: [
        AuthService,
        provideRouter([]),
        provideHttpClient(),
        provideHttpClientTesting(),
      ],
    });
    service = TestBed.inject(AuthService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should sign in with valid credentials', async () => {
    const promise = service.signIn('admin@ims.local', 'demo');

    const req = httpMock.expectOne(`${environment.apiBaseUrl}/auth/token`);
    expect(req.request.method).toBe('POST');
    req.flush({
      accessToken: 'test-token',
      tokenType: 'Bearer',
      expiresAt: '2099-01-01T00:00:00Z',
      session: {
        userId: 'USR-001',
        email: 'admin@ims.local',
        displayName: 'System Admin',
        roles: ['SYSTEM_ADMINISTRATOR'],
        locationScope: ['NETWORK'],
        permissions: ['PERM-ADMIN-USERS'],
        sessionExpiresAt: '2099-01-01T00:00:00Z',
      },
    });

    await expectAsync(promise).toBeResolvedTo(true);
    expect(service.isAuthenticated()).toBe(true);
    expect(service.accessToken()).toBe('test-token');
  });

  it('should reject invalid credentials', async () => {
    const promise = service.signIn('invalid@test.com', 'wrong');

    const req = httpMock.expectOne(`${environment.apiBaseUrl}/auth/token`);
    req.flush({ title: 'Unauthorized', status: 401 }, { status: 401, statusText: 'Unauthorized' });

    await expectAsync(promise).toBeResolvedTo(false);
    expect(service.isAuthenticated()).toBe(false);
  });

  it('should sign out', async () => {
    const signInPromise = service.signIn('admin@ims.local', 'demo');
    httpMock.expectOne(`${environment.apiBaseUrl}/auth/token`).flush({
      accessToken: 'test-token',
      tokenType: 'Bearer',
      expiresAt: '2099-01-01T00:00:00Z',
      session: {
        userId: 'USR-001',
        email: 'admin@ims.local',
        displayName: 'System Admin',
        roles: ['SYSTEM_ADMINISTRATOR'],
        locationScope: ['NETWORK'],
        permissions: [],
        sessionExpiresAt: '2099-01-01T00:00:00Z',
      },
    });
    await signInPromise;

    const signOutPromise = service.signOut();
    httpMock.expectOne(`${environment.apiBaseUrl}/auth/logout`).flush({
      loggedOut: true,
      loggedOutAt: '2099-01-01T00:00:00Z',
    });
    await signOutPromise;

    expect(service.isAuthenticated()).toBe(false);
  });
});
