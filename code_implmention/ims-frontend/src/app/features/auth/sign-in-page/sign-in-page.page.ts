import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../../core/services/auth.service';
import { SuccessWarningErrorBannerComponent } from '../../../shared/ui/feedback/success-warning-error-banner/success-warning-error-banner.component';

@Component({
  selector: 'ims-sign-in-page',
  standalone: true,
  imports: [CommonModule, FormsModule, SuccessWarningErrorBannerComponent],
  templateUrl: './sign-in-page.page.html',
  styleUrl: './sign-in-page.page.scss'
})
export class SignInPage implements OnInit {
  private readonly auth = inject(AuthService);
  private readonly router = inject(Router);

  email = 'admin@ims.local';
  password = 'demo';
  rememberMe = false;
  errorMessage = signal('');
  submitting = signal(false);
  readonly screenId = 'UI-001';

  ngOnInit(): void {}

  async signIn(): Promise<void> {
    this.errorMessage.set('');
    this.submitting.set(true);
    try {
      const ok = await this.auth.signIn(this.email, this.password, this.rememberMe);
      if (ok) {
        await this.router.navigate(['/home/operations']);
      } else {
        this.errorMessage.set('Invalid credentials. Use admin@ims.local / demo');
      }
    } finally {
      this.submitting.set(false);
    }
  }

  onForgotPassword(event: Event): void {
    event.preventDefault();
    this.errorMessage.set('Password recovery is not available in this release. Contact your administrator.');
  }

  onNeedHelp(event: Event): void {
    event.preventDefault();
    this.errorMessage.set('Need help signing in? Contact your system administrator.');
  }
}
