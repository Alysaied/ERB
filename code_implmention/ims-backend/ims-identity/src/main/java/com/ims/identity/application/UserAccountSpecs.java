package com.ims.identity.application;

import com.ims.identity.domain.AccountStatus;
import com.ims.identity.domain.RoleAssignment;
import com.ims.identity.domain.RoleAssignmentLocation;
import com.ims.identity.domain.UserAccount;
import jakarta.persistence.criteria.Predicate;
import jakarta.persistence.criteria.Root;
import jakarta.persistence.criteria.Subquery;
import org.springframework.data.jpa.domain.Specification;

import java.util.ArrayList;
import java.util.List;



public final class UserAccountSpecs {

    private UserAccountSpecs(){}

    public static Specification<UserAccount> withFilter(
            AccountStatus status,
            String roleCode,
            String locationCode,
            String search
    ){
        return(root,query,cb)->{
            List<Predicate> predicates=new ArrayList<>();
            if(status !=null){
                predicates.add(cb.equal(root.get("accountStatus"),status));
            }
            if(search != null && !search.isBlank()){
                String pattern = "%"+ search.trim().toLowerCase()+ "%";
                predicates.add(
                        cb.or(
                                cb.like(cb.lower(root.get("userIdentifier")), pattern),
                                cb.like(cb.lower(root.get("email")), pattern),
                                cb.like(cb.lower(root.get("displayName")), pattern)
                ));
            }
            boolean byRole =roleCode!=null && !roleCode.isBlank();
            boolean byLocation = locationCode!=null && !locationCode.isBlank();

            if(byRole || byLocation ){
                Subquery<Long> sub = query.subquery(Long.class);
                Root<RoleAssignment> roleRoot =sub.from(RoleAssignment.class);
                sub.select(roleRoot.get("userAccountId"));
                List<Predicate> rolePreds = new ArrayList<>();
                rolePreds.add(cb.equal(roleRoot.get("userAccountId"), root.get("id")));
                rolePreds.add(cb.equal(roleRoot.get("assignmentStatus"), "ACTIVE"));
                if (byRole) {
                    rolePreds.add(cb.equal(roleRoot.get("roleName"), roleCode.trim()));
                }
                if (byLocation) {
                    Root<RoleAssignmentLocation> locRoot =
                            sub.from(RoleAssignmentLocation.class);
                    rolePreds.add(cb.equal(locRoot.get("roleAssignmentId"), roleRoot.get("id")));
                    rolePreds.add(cb.equal(locRoot.get("locationCode"), locationCode.trim()));
                }
                sub.where(rolePreds.toArray(Predicate[]::new));
                predicates.add(cb.exists(sub));
            }
            return predicates.isEmpty()
                    ? cb.conjunction()
                    : cb.and(predicates.toArray(Predicate[]::new));
        };
    }
}
