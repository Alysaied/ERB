package com.ims.identity.application;

import com.ims.identity.DTO.*;
import com.ims.identity.domain.RoleAssignment;
import com.ims.identity.domain.RoleAssignmentLocation;
import com.ims.identity.domain.UserAccount;
import com.ims.identity.infrastructure.RoleAssignmentLocationRepository;
import com.ims.identity.infrastructure.RoleAssignmentRepository;
import com.ims.identity.infrastructure.UserAccountRepository;
import com.ims.sharedkernel.problem.DomainException;
import jakarta.transaction.Transactional;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Service
public class UserAdminService {
    private final UserAccountRepository _userAccountRepository;
    private final  PermissionCatalog permissionCatalog;
    private final RoleAssignmentRepository roleAssignmentRepository;
    private final RoleAssignmentLocationRepository roleAssignmentLocationRepository;

    UserAdminService( UserAccountRepository _userAccountRepository,
                      PermissionCatalog permissionCatalog,
                      RoleAssignmentRepository roleAssignmentRepository,
                      RoleAssignmentLocationRepository roleAssignmentLocationRepository){
        this._userAccountRepository=_userAccountRepository;
        this.permissionCatalog=permissionCatalog;
        this.roleAssignmentRepository=roleAssignmentRepository;
        this.roleAssignmentLocationRepository=roleAssignmentLocationRepository;

    }

    @Transactional
    public UserAccountResponse provision(ProvisionUserAccountRequest request){
        String userId = request.userId().trim();
        String email = request.email().trim();
        String displayName= request.displayName().trim();

        if(_userAccountRepository.findByEmailIgnoreCase(email).isPresent()){
            throw new DomainException("USER_ALREADY_EXISTS", "User with email already exists", 409);
        }
        if(_userAccountRepository.findByUserIdentifier(userId).isPresent()){
            throw new DomainException("USER_ALREADY_EXISTS", "User with userId already exists", 409);
        }
        for(RoleAssignmentDto role :request.initialRoles()){
            if(! permissionCatalog.isKnownRole(role.roleCode())){
                throw new DomainException(
                        "UnKNOWN_ROLE",
                        "Unknown role:" + role.roleCode(),
                        422
                );
            }
        }
        Set<String> roleCodes =new HashSet<>();
        for(RoleAssignmentDto role: request.initialRoles()){
            if(!roleCodes.add(role.roleCode())){
                throw new DomainException(
                        "DUPLICATE_ROLE",
                        "Duplicate role assignment for role:" + role.roleCode(),
                        422,
                        null,
                        "VR-083"
                );
            }
        }
        UserAccount user =new UserAccount(userId,displayName,email,null, LocalDate.now());
        user =_userAccountRepository.save(user);
        Long userAccountId =user.getId();

        List<RoleAssignmentResponse> roleResponses= new ArrayList<>();
        for(RoleAssignmentDto roleDto: request.initialRoles()){
            LocalDate effectiveFrom = roleDto.effectiveFrom() != null ? roleDto.effectiveFrom() : LocalDate.now();

            RoleAssignment assignment = RoleAssignment.assign(userAccountId,
                    roleDto.roleCode(),
                    permissionCatalog.permissionSetFor(roleDto.roleCode()),
                    effectiveFrom,
                    roleDto.effectiveTo());

            assignment= roleAssignmentRepository.save(assignment);

            List<String> locationCodes= roleDto.locationCodes()==null
                    ? List.of(): roleDto.locationCodes();
            for(String locationCode : locationCodes){
                RoleAssignmentLocation location = RoleAssignmentLocation.of(
                        assignment.getId(),
                        locationCode
                );
                roleAssignmentLocationRepository.save(location);
            }
            roleResponses.add(new RoleAssignmentResponse(
                    String.valueOf(assignment.getId()),
                    assignment.getRoleName(),
                    locationCodes,
                    assignment.getEffectiveFrom(),
                    assignment.getEffectiveTo()
            ));
        }
        return new UserAccountResponse(
                user.getUserIdentifier(),
                user.getEmail(),
                user.getDisplayName(),
                user.getAccountStatus().name(),
                roleResponses,
                new AuditInfoResponse(
                        user.getCreatedAt(),
                        "system admin",
                        user.getUpdateAt(),
                        "system admin"
                )
        );
    }

}
