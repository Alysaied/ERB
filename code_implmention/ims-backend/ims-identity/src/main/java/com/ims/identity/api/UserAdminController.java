package com.ims.identity.api;

import com.ims.identity.DTO.ProvisionUserAccountRequest;
import com.ims.identity.DTO.UserAccountResponse;
import com.ims.identity.application.UserAdminService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

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
}
