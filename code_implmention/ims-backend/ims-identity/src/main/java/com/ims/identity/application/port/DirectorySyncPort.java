package com.ims.identity.application.port;

import java.time.Instant;
import java.util.List;

public interface DirectorySyncPort {

    /**
     * @param sinceTimestamp null for FULL sync; required for INCREMENTAL by the service layer
     */
    List<DirectoryUser> fetchUsers(Instant sinceTimestamp);
}
