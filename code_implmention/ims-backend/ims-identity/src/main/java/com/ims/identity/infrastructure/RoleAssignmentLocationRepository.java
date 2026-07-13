package com.ims.identity.infrastructure;

import com.ims.identity.domain.RoleAssignmentLocation;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Collection;
import java.util.List;

public interface RoleAssignmentLocationRepository extends JpaRepository<RoleAssignmentLocation, Long> {
    List<RoleAssignmentLocation> findByRoleAssignmentIdIn(Collection<Long> roleAssignmentIds);
}
