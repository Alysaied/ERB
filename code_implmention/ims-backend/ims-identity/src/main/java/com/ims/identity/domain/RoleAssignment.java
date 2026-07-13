package com.ims.identity.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

import java.time.Instant;
import java.time.LocalDate;

@Entity
@Table(name = "role_assignments", schema = "identity")
public class RoleAssignment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "user_account_id", nullable = false)
    private Long userAccountId;

    @Column(name = "role_name", nullable = false, length = 64)
    private String roleName;

    @Column(name = "permission_set", length = 128)
    private String permissionSet;

    @Column(name = "assignment_status", nullable = false, length = 32)
    private String assignmentStatus = "ACTIVE";

    @Column(name = "effective_from", nullable = false)
    private LocalDate effectiveFrom;

    @Column(name = "effective_to")
    private LocalDate effectiveTo;

    @Column(name = "sod_compliant", nullable = false)
    private boolean sodCompliant = true;

    @Column(name = "created_at", nullable = false)
    private Instant createdAt = Instant.now();

    protected RoleAssignment() {
    }

    public Long getId() {
        return id;
    }

    public Long getUserAccountId() {
        return userAccountId;
    }

    public String getRoleName() {
        return roleName;
    }

    public String getPermissionSet() {
        return permissionSet;
    }

    public String getAssignmentStatus() {
        return assignmentStatus;
    }

    public LocalDate getEffectiveFrom() {
        return effectiveFrom;
    }

    public LocalDate getEffectiveTo() {
        return effectiveTo;
    }

    public boolean isSodCompliant() {
        return sodCompliant;
    }

    public boolean isCurrentlyActive() {
        if (!"ACTIVE".equals(assignmentStatus)) {
            return false;
        }
        LocalDate today = LocalDate.now();
        if (effectiveFrom != null && today.isBefore(effectiveFrom)) {
            return false;
        }
        return effectiveTo == null || !today.isAfter(effectiveTo);
    }
}
