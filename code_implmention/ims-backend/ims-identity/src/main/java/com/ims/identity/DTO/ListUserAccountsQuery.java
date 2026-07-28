package com.ims.identity.DTO;

import com.ims.identity.domain.AccountStatus;
import jakarta.validation.constraints.Size;

public record ListUserAccountsQuery(

       AccountStatus status,

       @Size(max=50)
       String roleCode,

       String locationCode,
       @Size(max=200)
       String search,
       @Size(min = 1)
       Integer page,

       @Size(min=1,max = 100)
       Integer pageSize,

       String sortBy,

       String sortDirection

) {
}
