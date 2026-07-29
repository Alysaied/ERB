package com.ims.identity.infrastructure;

import com.ims.identity.application.port.DirectorySyncPort;
import com.ims.identity.application.port.DirectoryUser;
import org.springframework.stereotype.Component;

import java.time.Instant;
import java.util.List;

/**
 * Local stand-in for EXT-08 HR directory until a real LDAP/SCIM adapter exists.
 */
@Component
public class StubDirectorySyncAdapter implements DirectorySyncPort {

    private static final List<DirectoryUser> DIRECTORY = List.of(
            new DirectoryUser(
                    "usr-dir-01",
                    "sara.hire@company.example.com",
                    "Sara Hire",
                    true,
                    Instant.parse("2026-06-01T00:00:00Z")
            ),
            new DirectoryUser(
                    "usr-dir-02",
                    "jon.update@company.example.com",
                    "Jon Updated",
                    true,
                    Instant.parse("2026-07-15T00:00:00Z")
            ),
            new DirectoryUser(
                    "usr-dir-03",
                    "lea.ver@company.example.com",
                    "Lea Ver",
                    false,
                    Instant.parse("2026-07-20T00:00:00Z")
            )
    );

    @Override
    public List<DirectoryUser> fetchUsers(Instant sinceTimestamp) {
        if (sinceTimestamp == null) {
            return DIRECTORY;
        }
        return DIRECTORY.stream()
                .filter(u -> !u.modifiedAt().isBefore(sinceTimestamp))
                .toList();
    }
}
