package com.ims.identity.domain;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;

import java.time.Instant;

@Getter
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

    @Column(name="created_at",nullable = false)
    private Instant createdAt = Instant.now();

    protected RoleAssignmentLocation() {
    }

    public static RoleAssignmentLocation of(
        Long roleAssignmentId,
        String locationCode
    ){
        RoleAssignmentLocation location=new RoleAssignmentLocation();
        location.roleAssignmentId= roleAssignmentId;
        location.locationCode= locationCode;
        location.createdAt= Instant.now();
        return location;

    }

}
