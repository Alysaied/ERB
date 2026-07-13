package com.ims.application.platform;

import com.ims.sharedkernel.problem.DomainException;
import com.ims.sharedkernel.problem.ProblemDetailResponse;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.core.AuthenticationException;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.time.Instant;
import java.util.List;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(DomainException.class)
    public ResponseEntity<ProblemDetailResponse> handleDomain(DomainException ex, HttpServletRequest request) {
        return problem(
                ex.getStatus(),
                HttpStatus.valueOf(ex.getStatus()).getReasonPhrase(),
                ex.getMessage(),
                request.getRequestURI(),
                ex.getErrorCode(),
                ex.getBusinessRuleId(),
                ex.getValidationRuleId(),
                null
        );
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ProblemDetailResponse> handleValidation(
            MethodArgumentNotValidException ex,
            HttpServletRequest request
    ) {
        List<ProblemDetailResponse.FieldError> errors = ex.getBindingResult().getFieldErrors().stream()
                .map(this::toFieldError)
                .toList();
        return problem(
                400,
                "Bad Request",
                "Request validation failed",
                request.getRequestURI(),
                "VALIDATION_FAILED",
                null,
                "VR-007",
                errors
        );
    }

    @ExceptionHandler({AuthenticationException.class, BadCredentialsException.class})
    public ResponseEntity<ProblemDetailResponse> handleAuth(Exception ex, HttpServletRequest request) {
        return problem(
                401,
                "Unauthorized",
                "Authentication required or token invalid",
                request.getRequestURI(),
                "AUTH_TOKEN_INVALID",
                null,
                "VR-008",
                null
        );
    }

    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<ProblemDetailResponse> handleAccess(AccessDeniedException ex, HttpServletRequest request) {
        return problem(
                403,
                "Forbidden",
                "Insufficient permissions",
                request.getRequestURI(),
                "AUTH_FORBIDDEN",
                null,
                null,
                null
        );
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ProblemDetailResponse> handleGeneric(Exception ex, HttpServletRequest request) {
        return problem(
                500,
                "Internal Server Error",
                "Unexpected server error",
                request.getRequestURI(),
                "INTERNAL_ERROR",
                null,
                null,
                null
        );
    }

    private ProblemDetailResponse.FieldError toFieldError(FieldError error) {
        return new ProblemDetailResponse.FieldError(
                error.getField(),
                error.getDefaultMessage(),
                error.getCode()
        );
    }

    private ResponseEntity<ProblemDetailResponse> problem(
            int status,
            String title,
            String detail,
            String instance,
            String errorCode,
            String businessRuleId,
            String validationRuleId,
            List<ProblemDetailResponse.FieldError> errors
    ) {
        ProblemDetailResponse body = new ProblemDetailResponse(
                "about:blank",
                title,
                status,
                detail,
                instance,
                errorCode,
                businessRuleId,
                validationRuleId,
                Instant.now(),
                errors
        );
        return ResponseEntity.status(status)
                .contentType(MediaType.APPLICATION_PROBLEM_JSON)
                .body(body);
    }
}
