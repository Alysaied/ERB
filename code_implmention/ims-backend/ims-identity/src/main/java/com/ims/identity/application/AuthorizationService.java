package com.ims.identity.application;

import com.ims.identity.DTO.AuthorizationEvaluationResponse;
import com.ims.identity.DTO.EvaluateAuthorizationRequest;
import com.ims.identity.DTO.LocationScopeValidationResponse;
import com.ims.identity.DTO.ValidateLocationScopeRequest;
import com.ims.identity.domain.RoleAssignment;
import com.ims.identity.domain.RoleAssignmentLocation;
import com.ims.identity.domain.UserAccount;
import com.ims.identity.infrastructure.RoleAssignmentLocationRepository;
import com.ims.identity.infrastructure.RoleAssignmentRepository;
import com.ims.identity.infrastructure.UserAccountRepository;
import com.ims.sharedkernel.problem.DomainException;
import jakarta.transaction.Transactional;
import org.springframework.stereotype.Service;

import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

@Service
public class AuthorizationService {
    private final UserAccountRepository userAccountRepository;
    private final SessionService sessionService;
    private final RoleAssignmentRepository roleAssignmentRepository;
    private final PermissionCatalog permissionCatalog;
    private final RoleAssignmentLocationRepository roleAssignmentLocationRepository;
   public  AuthorizationService(UserAccountRepository userAccountRepository, SessionService sessionService, RoleAssignmentRepository roleAssignmentRepository
              , PermissionCatalog permissionCatalog,
               RoleAssignmentLocationRepository  roleAssignmentLocationRepository){
       this.userAccountRepository=userAccountRepository;
       this.sessionService=sessionService;
       this.roleAssignmentRepository = roleAssignmentRepository;
       this.permissionCatalog= permissionCatalog;
       this.roleAssignmentLocationRepository= roleAssignmentLocationRepository;

   }
    @Transactional
    public AuthorizationEvaluationResponse evaluate(
            EvaluateAuthorizationRequest request , String callerUserId
    ){
        if(callerUserId == null || callerUserId.isBlank()){
            throw new DomainException(
        " AUTH_UNAUTHORIZED",
                    "Authentication required",
                    401
            );
        }
        String action = request.action().trim();
        String targetUserId= (request.userId()== null || request.userId().isBlank())
                ? callerUserId.trim() : request.userId().trim();

        UserAccount user = userAccountRepository.findByUserIdentifier(targetUserId)
                .orElseThrow(()->new DomainException(
                        "AUTH_TOKEN_INVALID",
                        "User not found:"+ targetUserId,
                        401
                ));
        sessionService.assertAccountUsable(user);
        List<RoleAssignment>  activeRoles= roleAssignmentRepository
                .findByUserAccountId(user.getId())
                .stream()
                .filter(RoleAssignment::isCurrentlyActive)
                .toList();
        List<String> roles =activeRoles.stream()
                .map(RoleAssignment::getRoleName)
                .distinct()
                .toList();
        List<String> permissions= permissionCatalog.resolve(roles);
        if(!permissions.contains(action)){
            return new AuthorizationEvaluationResponse(
                    false,
                    targetUserId,
                    action,
                    "missing required permission :" + action
            );
        }
        String locationCode = request.locationCode();
        if(locationCode != null && !locationCode.isBlank()){
            Set<String > locations= loadLocationScope( activeRoles, roles);
            if(!locations.contains( locationCode.trim()) && !locations.contains("NETWORK")){
                return new AuthorizationEvaluationResponse(
                        false,
                        targetUserId,
                        action,
                        "missing required location scope :" + locationCode
                );
            }
        }

        return new AuthorizationEvaluationResponse(
                true,
                targetUserId,
                action,
                null
        );
    }

    private Set<String > loadLocationScope( List<RoleAssignment> activeRoles, List<String> roles){

       Set<String> locations = new LinkedHashSet<>();
       List<Long> assignmentsIds = activeRoles.stream().map(RoleAssignment :: getId).toList();
       if(!assignmentsIds.isEmpty()){
           for(RoleAssignmentLocation loc :
           roleAssignmentLocationRepository.findByRoleAssignmentIdIn(assignmentsIds)){
               locations.add(loc.getLocationCode());
           }
       }
       if(locations.isEmpty() && roles.contains("SYSTEM_ADMINISTRATOR")){
           locations.add("NETWORK");
       }
       return locations;
    }

    @Transactional
    public LocationScopeValidationResponse validateLocationScope(
       ValidateLocationScopeRequest request,
       String callerUserId
    ){
       if(callerUserId == null || callerUserId.isBlank()){
           throw new DomainException(
               " AUTH_UNAUTHORIZED",
               "Authentication required",
               401
           );
       }
       String locationCode = request.locationCode().trim();
       String targetUserId = (request.userId()== null || request.userId().isBlank())
               ? callerUserId.trim(): request.userId().trim();

       UserAccount user = userAccountRepository.findByUserIdentifier(targetUserId)
               .orElseThrow(
                       ()-> new DomainException(
                               "AUTH_TOKEN_INVALID",
                               "User not found:"+ targetUserId,
                               401
                       )
               );
       sessionService.assertAccountUsable(user);
       List<RoleAssignment> activeRoles =  roleAssignmentRepository
               .findByUserAccountId(user.getId())
               .stream()
               .filter(RoleAssignment :: isCurrentlyActive)
               .toList();
       List<String> roles= activeRoles.stream()
               .map(RoleAssignment::getRoleName)
               .distinct()
               .toList();

       Set<String> locations= loadLocationScope(activeRoles, roles);
       List<String> scopedLocations = List.copyOf(locations);
       boolean locationAllowed =
               locations.contains(locationCode) || locations.contains("NETWORK");
       if(!locationAllowed){
           return new LocationScopeValidationResponse(
                   false,
                   targetUserId,
                   locationCode,
                   scopedLocations
           );
       }
       String requiredPermission = request.requiredPermission();
       if(requiredPermission !=null && !requiredPermission.isBlank()){
           List<String> permissions = permissionCatalog.resolve(roles);
           if (!permissions.contains(requiredPermission.trim())) {
               return new LocationScopeValidationResponse(
                       false,
                       targetUserId,
                       locationCode,
                       scopedLocations
               );
           }
       }
       return new LocationScopeValidationResponse(
               true,
               targetUserId,
               locationCode,
               scopedLocations
       );

    }
}

