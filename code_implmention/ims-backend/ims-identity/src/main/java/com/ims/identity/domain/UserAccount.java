package com.ims.identity.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import jakarta.persistence.Version;

import java.time.Instant;
import java.time.LocalDate;

@Entity
@Table(name = "user_accounts", schema = "identity")
public class UserAccount {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "user_identifier", nullable = false, unique = true, length = 64)
    private String userIdentifier;

    @Column(name = "display_name", nullable = false, length = 256)
    private String displayName;

    @Column(name = "email", unique = true, length = 256)
    private String email;

    /**
     * Local-dev credential hash until enterprise OIDC replaces password login (AUTH-01).
     */
    @Column(name = "password_hash", length = 255)
    private String passwordHash;

    @Enumerated(EnumType.STRING)
    @Column(name = "account_status", nullable = false, length = 32)
    private AccountStatus accountStatus = AccountStatus.ACTIVE;

    @Column(name = "effective_from", nullable = false)
    private LocalDate effectiveFrom;

    @Column(name = "last_activity_at")
    private Instant lastActivityAt;

    @Column(name = "has_sod_conflict", nullable = false)
    private boolean hasSodConflict;

    @Version
    @Column(name = "version", nullable = false)
    private Integer version;

    @Column(name = "created_at", nullable = false)
    private Instant createdAt;

    @Column(name = "updated_at", nullable = false)
    private Instant updatedAt;

    protected UserAccount() {
    }

    public UserAccount(
            String userIdentifier,
            String displayName,
            String email,
            String passwordHash,
            LocalDate effectiveFrom
    ) {
        Instant now = Instant.now();
        this.userIdentifier = userIdentifier;
        this.displayName = displayName;
        this.email = email;
        this.passwordHash = passwordHash;
        this.accountStatus = AccountStatus.ACTIVE;
        this.effectiveFrom = effectiveFrom;
        this.hasSodConflict = false;
        this.createdAt = now;
        this.updatedAt = now;
    }
    public void suspend(){
        this.accountStatus = AccountStatus.SUSPENDED;
        this.updatedAt = Instant.now();
    }
    public void deactivated(){
        this.accountStatus = AccountStatus.DEACTIVATED;
         this.updatedAt= Instant.now();
    }

    public boolean applyDirectoryProfile(String displayName, String email) {
        boolean changed = false;
        if (displayName != null && !displayName.equals(this.displayName)) {
            this.displayName = displayName;
            changed = true;
        }
        if (email != null && !email.equalsIgnoreCase(this.email == null ? "" : this.email)) {
            this.email = email;
            changed = true;
        }
        if (changed) {
            this.updatedAt = Instant.now();
        }
        return changed;
    }

    public boolean updateProfile(String displayName, String email, LocalDate effectiveFrom) {
        boolean changed = applyDirectoryProfile(displayName, email);
        if (effectiveFrom != null && !effectiveFrom.equals(this.effectiveFrom)) {
            this.effectiveFrom = effectiveFrom;
            this.updatedAt = Instant.now();
            changed = true;
        }
        return changed;
    }

    public void markActivity() {
        this.lastActivityAt = Instant.now();
        this.updatedAt = this.lastActivityAt;
    }

    public void setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
        this.updatedAt = Instant.now();
    }

    public boolean isLoginAllowed() {
        return accountStatus == AccountStatus.ACTIVE;
    }

    public Long getId() {
        return id;
    }

    public String getUserIdentifier() {
        return userIdentifier;
    }

    public String getDisplayName() {
        return displayName;
    }

    public String getEmail() {
        return email;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public AccountStatus getAccountStatus() {
        return accountStatus;
    }

    public LocalDate getEffectiveFrom() {
        return effectiveFrom;
    }

    public Instant getLastActivityAt() {
        return lastActivityAt;
    }

    public boolean isHasSodConflict() {
        return hasSodConflict;
    }

    public Integer getVersion() {
        return version;
    }

    public Instant getCreatedAt() {
        return createdAt;
    }
    public Instant getUpdateAt(){
        return updatedAt;
    }
}
