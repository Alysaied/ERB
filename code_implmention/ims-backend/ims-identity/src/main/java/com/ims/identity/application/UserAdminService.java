package com.ims.identity.application;

import com.ims.identity.DTO.*;
import com.ims.identity.application.port.DirectorySyncPort;
import com.ims.identity.application.port.DirectoryUser;
import com.ims.identity.domain.AccountStatus;
import com.ims.identity.domain.RoleAssignment;
import com.ims.identity.domain.RoleAssignmentLocation;
import com.ims.identity.domain.UserAccount;
import com.ims.identity.infrastructure.RoleAssignmentLocationRepository;
import com.ims.identity.infrastructure.RoleAssignmentRepository;
import com.ims.identity.infrastructure.UserAccountRepository;
import com.ims.sharedkernel.problem.DomainException;
import com.ims.sharedkernel.problem.PagedResponse;
import jakarta.transaction.Transactional;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.time.LocalDate;
import java.util.*;

@Service
public class UserAdminService {
    private final UserAccountRepository _userAccountRepository;
    private final  PermissionCatalog permissionCatalog;
    private final RoleAssignmentRepository roleAssignmentRepository;
    private final RoleAssignmentLocationRepository roleAssignmentLocationRepository;
    private final DirectorySyncPort directorySyncPort;

    UserAdminService( UserAccountRepository _userAccountRepository,
                      PermissionCatalog permissionCatalog,
                      RoleAssignmentRepository roleAssignmentRepository,
                      RoleAssignmentLocationRepository roleAssignmentLocationRepository,
                      DirectorySyncPort directorySyncPort){
        this._userAccountRepository=_userAccountRepository;
        this.permissionCatalog=permissionCatalog;
        this.roleAssignmentRepository=roleAssignmentRepository;
        this.roleAssignmentLocationRepository=roleAssignmentLocationRepository;
        this.directorySyncPort = directorySyncPort;

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
    @Transactional
    public PagedResponse<UserAccountSummaryResponse> listUsers(AccountStatus status,String roleCode,String locationCode,String search,int page,int pageSize, String sortBy,String sortDirection){
        int safePage = Math.max(page,1);
        int safeSize= pageSize< 1 ? 20 : Math.min(pageSize,100);

        Sort.Direction direction =
                "DESC".equalsIgnoreCase(sortDirection)? Sort.Direction.DESC :Sort.Direction.ASC;
        String sortField = switch ( sortBy == null ? "displayName":sortBy){
            case "userId"->"userIdentifier";
            case "email"->"email";
            case "displayName"-> "displayName";
            default -> throw new DomainException(
                    "INVALID_SORT_BY",
                    "sortBy must be displayName, user , or email",
                    400
            );
        };

        Pageable pageable= PageRequest.of(safePage - 1 , safeSize,Sort.by(direction,sortField));
        Page<UserAccount> result= _userAccountRepository.findAll(UserAccountSpecs.withFilter(status,roleCode,locationCode,search),pageable);

        List<Long> ids=result.getContent().stream().map(UserAccount::getId).toList();
        Map<Long,List<String>>rolesByUser=loadActiveRoleNames(ids);

        List<UserAccountSummaryResponse>data = result.getContent().stream().map(
                u->new UserAccountSummaryResponse(
                        u.getUserIdentifier(),
                        u.getEmail(),
                        u.getDisplayName(),
                        u.getAccountStatus().name(),
                        rolesByUser.getOrDefault(u.getId(),List.of()),
                        u.isHasSodConflict(),
                        u.getLastActivityAt()
                )
        ).toList();
        return new PagedResponse<>(
                data,
                safePage,
                safeSize,
                result.getTotalElements(),
                result.getTotalPages()
        );
    }

    private Map<Long,List<String>>loadActiveRoleNames(List<Long> userAccountIds){
        if(userAccountIds.isEmpty()){
            return Map.of();
        }
        Map<Long,Set<String>> collected = new HashMap<>();
        for(RoleAssignment a :roleAssignmentRepository.findByUserAccountIdIn(userAccountIds)){
            if(!a.isCurrentlyActive()) continue;
            collected.computeIfAbsent(a.getUserAccountId(),id->new LinkedHashSet<>())
                    .add(a.getRoleName());
        }
        Map<Long,List<String>> result = new HashMap<>();
        collected.forEach((id,roles)->result.put(id, List.copyOf(roles)));
        return result;
    }

    public UserAccountResponse getUser(String userId ){
       UserAccount user =_userAccountRepository.findByUserIdentifier(userId)
               .orElseThrow(()-> new DomainException(
                       "USER_NOT_FOUND",
                       "User not found :" + userId,
                       404
               ));
      List <RoleAssignment> role_assignments= roleAssignmentRepository.findByUserAccountId(user.getId());


      List<Long> assignmentIds= role_assignments.stream()
              .map(RoleAssignment::getId).toList();
      Map<Long,List<String>> locationsByAssignmentId =loadLocationsByAssignmentId(assignmentIds);

      List<RoleAssignmentResponse> roles= role_assignments.stream()
              .map(a->new RoleAssignmentResponse(
                      String.valueOf(a.getId()),
                      a.getRoleName(),
                        locationsByAssignmentId.getOrDefault(a.getId(),List.of()),
                      a.getEffectiveFrom(),a.getEffectiveTo()
              )).toList();
      return new UserAccountResponse(
              user.getUserIdentifier(),
              user.getEmail(),
              user.getDisplayName(),
              user.getAccountStatus().name(),
              roles,
              new AuditInfoResponse(
                      user.getCreatedAt(),
                      "system admin",
                      user.getUpdateAt(),
                      "system admin"
              )
      );


    }

    private Map<Long,List<String>>loadLocationsByAssignmentId(List<Long>assignmentIds){
        if(assignmentIds.isEmpty()){
            return Map.of();
        }
        Map<Long, List<String>> result= new HashMap<>();
        for(RoleAssignmentLocation loc:
        roleAssignmentLocationRepository.findByRoleAssignmentIdIn(assignmentIds)){
            result .computeIfAbsent(loc.getRoleAssignmentId(),id->new ArrayList<>())
                    .add(loc.getLocationCode());
        }
        return result;
    }
@Transactional
    public RoleAssignmentResponse assignRole(String userId, AssignRoleRequest request){
        UserAccount user= _userAccountRepository.findByUserIdentifier(userId).orElseThrow(
                ()-> new DomainException(
                        "USER NOT FOUND",
                        "user not found :" + userId,
                        404
                )
        );
        if(!(user.getAccountStatus()== AccountStatus.ACTIVE)){
            throw new DomainException(
                    "USER NOT ACTIVE",
                    "User is not active :" ,
                    422
            );
        }
        RoleAssignmentDto roleDto= request.roleAssignment();

        if(!permissionCatalog.isKnownRole(roleDto.roleCode())){
            throw new DomainException(
                    "ROLE CODE NOT FOUND ",
                    "roleCode not found in permissionCatalog",
                    422
            );
        }
        List<RoleAssignment> existing = roleAssignmentRepository.findByUserAccountId(user.getId());

        boolean duplicate = existing.stream()
                .filter(RoleAssignment :: isCurrentlyActive)
                .anyMatch(a->a.getRoleName().equals(roleDto.roleCode()));
        if(duplicate){
            throw  new DomainException(
                    "DUPLICATE_ROLE",
                    "User already has an active assignment for role:" + roleDto.roleCode(),
                    422,
                    null,
                    "VR-083"
            );
        }

        LocalDate acitveFrom =roleDto.effectiveFrom() != null ? roleDto.effectiveFrom():LocalDate.now();
        LocalDate activeTo = roleDto.effectiveTo();

        RoleAssignment assignment=RoleAssignment.assign(
                user.getId(),
                roleDto.roleCode(),
                permissionCatalog.permissionSetFor(roleDto.roleCode()),
                acitveFrom,activeTo
        );
        assignment =roleAssignmentRepository.save(assignment);
        List<String> locationCodes = roleDto.locationCodes() == null
                ? List.of()
                :roleDto.locationCodes();
        for(String locationCode:locationCodes){
            roleAssignmentLocationRepository.save(
                    RoleAssignmentLocation.of(assignment.getId(),locationCode)
            );
        }
        return new RoleAssignmentResponse(

                 String.valueOf(assignment.getId()),
                assignment.getRoleName(),
                locationCodes,
                assignment.getEffectiveFrom(),
                assignment.getEffectiveTo()
        );

    }

    public RoleRevocationResponse revoke(String userId, Long roleAssignmentId){
        UserAccount user= _userAccountRepository.findByUserIdentifier(userId)
                .orElseThrow(
                        ()->new DomainException(
                                "USER_NOT_FOUND",
                                "user not found :"+userId,
                                404
                        )
                );
       RoleAssignment roleAssignment= roleAssignmentRepository.findById(roleAssignmentId).orElseThrow(
               () -> new DomainException(
                       "ROLE_NOT_FOUND",
                       "role not found ",
                       404
               )
       );

       if(! roleAssignment.getUserAccountId().equals(user.getId())){
           throw new DomainException(
                   "ROLE_ASSIGNMENT_NOT_FOUND",
                   "Role assignment not found for user: " + userId,
                   404
           );
       }

       roleAssignment.revoke();
       roleAssignmentRepository.save(roleAssignment);
       return new RoleRevocationResponse(
               String.valueOf(roleAssignment.getId()),
               user.getUserIdentifier(),
               Instant.now()
       );
    }

    public UserAccountResponse suspend(String userId, SuspendUserAccountRequest request){
        UserAccount user= _userAccountRepository.findByUserIdentifier(userId).orElseThrow(
                ()->new DomainException(
                        "USER NOT FOUND",
                         "user not found : "+ userId,
                        404
                        )
        );
        if(user.getAccountStatus() != AccountStatus.ACTIVE){
            throw new DomainException(
                    "USER_ALREADY_SUSPENDED",
                    "User is already suspended: "+ userId,
                    422
            );
        }
        List <RoleAssignment> role_assignments= roleAssignmentRepository.findByUserAccountId(user.getId());

        List<Long> assignmentIds= role_assignments.stream()
                .map(RoleAssignment::getId).toList();
        Map<Long,List<String>> locationsByAssignmentId =loadLocationsByAssignmentId(assignmentIds);

        List<RoleAssignmentResponse> roles= role_assignments.stream()
                .map(a->new RoleAssignmentResponse(
                        String.valueOf(a.getId()),
                        a.getRoleName(),
                        locationsByAssignmentId.getOrDefault(a.getId(),List.of()),
                        a.getEffectiveFrom(),a.getEffectiveTo()
                )).toList();
        user.suspend();
        _userAccountRepository.save(user);
        return new UserAccountResponse(
                user.getUserIdentifier(),
                user.getEmail(),
                user.getDisplayName(),
                user.getAccountStatus().name(),
                roles,
                new AuditInfoResponse(
                        user.getCreatedAt(),
                        "system admin",
                        user.getUpdateAt(),
                        "system admin"
        ));
    }

    @Transactional
    public UserAccountResponse deactivate(String userId,DeactivateUserAccountRequest request){
        UserAccount user = _userAccountRepository.findByUserIdentifier(userId).orElseThrow(
                ()-> new DomainException(
                        "USER NOT FOUND",
                        "user_not_found" + userId,
                        404
                )
        );
        if(user.getAccountStatus() == AccountStatus.SUSPENDED){
            throw  new DomainException(
                    "USER_ALREADY_DEACTIVATED",
                    "user_aready_deactivated : "+ userId,
                    422
            );
        }
        List <RoleAssignment> role_assignments= roleAssignmentRepository.findByUserAccountId(user.getId());

        List<Long> assignmentIds= role_assignments.stream()
                .map(RoleAssignment::getId).toList();
        Map<Long,List<String>> locationsByAssignmentId =loadLocationsByAssignmentId(assignmentIds);

        List<RoleAssignmentResponse> roles= role_assignments.stream()
                .map(a->new RoleAssignmentResponse(
                        String.valueOf(a.getId()),
                        a.getRoleName(),
                        locationsByAssignmentId.getOrDefault(a.getId(),List.of()),
                        a.getEffectiveFrom(),a.getEffectiveTo()
                )).toList();
        user.deactivated();
        _userAccountRepository.save(user);
        return new UserAccountResponse(
              user.getUserIdentifier(),
                user.getEmail(),
                user.getDisplayName(),
                user.getAccountStatus().name(),
                roles,
                new AuditInfoResponse(
                        user.getCreatedAt(),
                        "system admin",
                        user.getUpdateAt(),
                        "system admin"
                )
        );
    }

    @Transactional
    public DirectorySyncResultResponse syncUsers(SyncUsersFromDirectoryRequest request) {
        String syncMode = request.syncMode().trim().toUpperCase(Locale.ROOT);
        if (!syncMode.equals("FULL") && !syncMode.equals("INCREMENTAL")) {
            throw new DomainException(
                    "INVALID_SYNC_MODE",
                    "syncMode must be FULL or INCREMENTAL",
                    400
            );
        }
        if (syncMode.equals("INCREMENTAL") && request.sinceTimestamp() == null) {
            throw new DomainException(
                    "SINCE_TIMESTAMP_REQUIRED",
                    "sinceTimestamp is required when syncMode is INCREMENTAL",
                    400
            );
        }

        boolean dryRun = Boolean.TRUE.equals(request.dryRun());
        Instant since = syncMode.equals("INCREMENTAL") ? request.sinceTimestamp() : null;

        List<DirectoryUser> directoryUsers;
        try {
            directoryUsers = directorySyncPort.fetchUsers(since);
        } catch (Exception ex) {
            throw new DomainException(
                    "DIRECTORY_SYNC_FAILED",
                    "Failed to fetch users from directory",
                    500
            );
        }

        int created = 0;
        int updated = 0;
        int deactivated = 0;
        List<SyncErrorResponse> errors = new ArrayList<>();

        for (DirectoryUser directoryUser : directoryUsers) {
            try {
                if (directoryUser.active()) {
                    int result = syncActiveDirectoryUser(directoryUser, dryRun);
                    if (result == 1) {
                        created++;
                    } else if (result == 2) {
                        updated++;
                    }
                } else {
                    if (syncTerminatedDirectoryUser(directoryUser, dryRun)) {
                        deactivated++;
                    }
                }
            } catch (DomainException ex) {
                errors.add(new SyncErrorResponse(
                        directoryUser.userId(),
                        ex.getErrorCode(),
                        ex.getMessage()
                ));
            } catch (Exception ex) {
                errors.add(new SyncErrorResponse(
                        directoryUser.userId(),
                        "SYNC_ROW_FAILED",
                        ex.getMessage() == null ? "Unexpected sync error" : ex.getMessage()
                ));
            }
        }

        return new DirectorySyncResultResponse(
                syncMode,
                created,
                updated,
                deactivated,
                List.copyOf(errors),
                Instant.now()
        );
    }

    /**
     * @return 1 created, 2 updated, 0 unchanged
     */
    private int syncActiveDirectoryUser(DirectoryUser directoryUser, boolean dryRun) {
        Optional<UserAccount> existing =
                _userAccountRepository.findByUserIdentifier(directoryUser.userId());

        if (existing.isEmpty()) {
            assertEmailAvailable(directoryUser.email(), null);
            if (!dryRun) {
                UserAccount created = new UserAccount(
                        directoryUser.userId(),
                        directoryUser.displayName(),
                        directoryUser.email(),
                        null,
                        LocalDate.now()
                );
                _userAccountRepository.save(created);
            }
            return 1;
        }

        UserAccount user = existing.get();
        assertEmailAvailable(directoryUser.email(), user.getUserIdentifier());
        boolean nameChanged = directoryUser.displayName() != null
                && !directoryUser.displayName().equals(user.getDisplayName());
        boolean emailChanged = directoryUser.email() != null
                && !directoryUser.email().equalsIgnoreCase(user.getEmail() == null ? "" : user.getEmail());
        boolean changed = nameChanged || emailChanged;
        if (changed && !dryRun) {
            user.applyDirectoryProfile(directoryUser.displayName(), directoryUser.email());
            _userAccountRepository.save(user);
        }
        return changed ? 2 : 0;
    }

    private boolean syncTerminatedDirectoryUser(DirectoryUser directoryUser, boolean dryRun) {
        Optional<UserAccount> existing =
                _userAccountRepository.findByUserIdentifier(directoryUser.userId());
        if (existing.isEmpty()) {
            return false;
        }
        UserAccount user = existing.get();
        if (user.getAccountStatus() == AccountStatus.DEACTIVATED) {
            return false;
        }
        if (!dryRun) {
            user.deactivated();
            _userAccountRepository.save(user);
        }
        return true;
    }

    private void assertEmailAvailable(String email, String currentUserId) {
        if (email == null || email.isBlank()) {
            return;
        }
        _userAccountRepository.findByEmailIgnoreCase(email.trim()).ifPresent(other -> {
            if (currentUserId == null || !other.getUserIdentifier().equals(currentUserId)) {
                throw new DomainException(
                        "EMAIL_ALREADY_EXISTS",
                        "Email already used by another user: " + email,
                        422
                );
            }
        });
    }


}
