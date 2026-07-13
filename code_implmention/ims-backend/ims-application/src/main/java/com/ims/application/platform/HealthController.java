package com.ims.application.platform;

import com.ims.identity.api.dto.HealthCheckResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.Instant;
import java.util.LinkedHashMap;
import java.util.Map;

/** API-175 */
@RestController
@RequestMapping("/api/v1")
public class HealthController {

    private final JdbcTemplate jdbcTemplate;
    private final String appVersion;

    public HealthController(
            JdbcTemplate jdbcTemplate,
            @Value("${info.app.version:0.1.0-SNAPSHOT}") String appVersion
    ) {
        this.jdbcTemplate = jdbcTemplate;
        this.appVersion = appVersion;
    }

    @GetMapping("/health")
    public ResponseEntity<HealthCheckResponse> health() {
        Map<String, String> components = new LinkedHashMap<>();
        String status = "UP";
        try {
            jdbcTemplate.queryForObject("SELECT 1", Integer.class);
            components.put("database", "UP");
        } catch (Exception ex) {
            components.put("database", "DOWN");
            status = "DOWN";
        }

        HealthCheckResponse body = new HealthCheckResponse(status, Instant.now(), appVersion, components);
        HttpStatus httpStatus = "UP".equals(status) ? HttpStatus.OK : HttpStatus.SERVICE_UNAVAILABLE;
        return ResponseEntity.status(httpStatus).body(body);
    }
}
