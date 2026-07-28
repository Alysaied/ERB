package com.ims.identity.infrastructure;

import com.ims.identity.domain.RoleAssignment;
import com.ims.identity.domain.UserAccount;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

import java.util.Collection;
import java.util.List;
import java.util.Optional;

public interface RoleAssignmentRepository extends JpaRepository<RoleAssignment, Long> {
    List<RoleAssignment> findByUserAccountId(Long userAccountId);

    List<RoleAssignment> findByUserAccountIdIn(Collection<Long> userAccountIds);

    Optional<RoleAssignment> findById(Long id);
}
