package com.ims.identity.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "role_assignment_locations", schema = "identity")
public class RoleAssignmentLocation {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "role_assignment_id", nullable = false)
    private Long roleAssignmentId;

    @Column(name = "location_code", nullable = false, length = 64)
    private String locationCode;

    protected RoleAssignmentLocation() {
    }

    public Long getId() {
        return id;
    }

    public Long getRoleAssignmentId() {
        return roleAssignmentId;
    }

    public String getLocationCode() {
        return locationCode;
    }
}
