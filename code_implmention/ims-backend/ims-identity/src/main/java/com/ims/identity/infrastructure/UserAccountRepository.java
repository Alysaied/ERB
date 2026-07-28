package com.ims.identity.infrastructure;

import com.ims.identity.domain.RoleAssignment;
import com.ims.identity.domain.UserAccount;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

import java.util.Collection;
import java.util.List;
import java.util.Optional;

public interface UserAccountRepository extends JpaRepository<UserAccount, Long>,JpaSpecificationExecutor<UserAccount>{
    Optional<UserAccount> findByEmailIgnoreCase(String email);

    Optional<UserAccount> findByUserIdentifier(String userIdentifier);


}
