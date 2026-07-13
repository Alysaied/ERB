package com.ims.identity.infrastructure;

import com.ims.identity.domain.RoleAssignment;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface RoleAssignmentRepository extends JpaRepository<RoleAssignment, Long> {
    List<RoleAssignment> findByUserAccountId(Long userAccountId);
}
