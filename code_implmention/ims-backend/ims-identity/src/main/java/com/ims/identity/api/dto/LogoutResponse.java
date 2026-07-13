package com.ims.identity.api.dto;

import java.time.Instant;

public record LogoutResponse(boolean loggedOut, Instant loggedOutAt) {
}
