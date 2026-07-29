package com.ims.identity.api;

import com.ims.identity.DTO.*;
import com.ims.identity.application.UserAdminService;
import com.ims.identity.domain.AccountStatus;
import com.ims.sharedkernel.problem.PagedResponse;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1")
public class UserAdminController {
    private final UserAdminService _userAdminService;

    public UserAdminController(UserAdminService userAdminService){
        this._userAdminService=userAdminService;
    }

    @PostMapping("/users")
    ResponseEntity<UserAccountResponse> provision(@Valid  @RequestBody ProvisionUserAccountRequest request){

        UserAccountResponse response = _userAdminService.provision(request);
            return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping("/users")
    PagedResponse<UserAccountSummaryResponse> listUsers(
            @RequestParam(required=false)AccountStatus status,
            @RequestParam(required =false) String roleCode,
            @RequestParam(required = false) String locationCode,
            @RequestParam(required = false) String search,
            @RequestParam(defaultValue = "1") int page,
            @RequestParam(defaultValue = "20")int pageSize,
            @RequestParam(defaultValue = "displayName") String sortBy,
            @RequestParam(defaultValue = "ASC") String sortDirection
             ){

             return _userAdminService.listUsers(status,roleCode,locationCode,search,page,pageSize,sortBy,sortDirection);
    }
    @GetMapping("/users/{userId}")
    UserAccountResponse getUser(@PathVariable String userId){
        return _userAdminService.getUser(userId);
    }


    @PostMapping("/users/{userId}/roles")
    RoleAssignmentResponse assignRole(@PathVariable  String userId, @Valid @RequestBody AssignRoleRequest request){
        RoleAssignmentResponse assignedRole= _userAdminService.assignRole(userId,request);
           return ResponseEntity.status(HttpStatus.CREATED).body(assignedRole).getBody();
    }

    @DeleteMapping("/users/{userId}/roles/{roleAssignmentId}")
    RoleRevocationResponse revoke(@PathVariable String userId,@PathVariable Long roleAssignmentId){
        return _userAdminService.revoke(userId.trim(),roleAssignmentId);
    }

    @PostMapping("/users/{userId}/suspend")
    UserAccountResponse suspend(@PathVariable String userId, @Valid @RequestBody SuspendUserAccountRequest request){
        return _userAdminService.suspend(userId.trim(),request);

    }

    @PostMapping("/users/{userId}/deactivate")
    @ResponseStatus (HttpStatus.OK)
        UserAccountResponse deactivate(@PathVariable String userId, @Valid @RequestBody DeactivateUserAccountRequest request){
        return _userAdminService.deactivate(userId.trim(),request);
        }

}
