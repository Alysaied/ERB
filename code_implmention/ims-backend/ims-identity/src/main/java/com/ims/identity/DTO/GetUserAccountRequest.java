package com.ims.identity.DTO;

import jakarta.validation.constraints.NotBlank;

public record GetUserAccountRequest(
  @NotBlank
  String userId
) {
}
