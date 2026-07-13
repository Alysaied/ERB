package com.ims.application.platform;

import com.ims.identity.domain.UserAccount;
import com.ims.identity.infrastructure.UserAccountRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

/**
 * Ensures Sprint 1 seed users have local password hashes (password: demo).
 */
@Component
public class SeedCredentialInitializer implements ApplicationRunner {

    private static final Logger log = LoggerFactory.getLogger(SeedCredentialInitializer.class);
    private static final String SEED_PASSWORD = "demo";

    private final UserAccountRepository userAccountRepository;
    private final PasswordEncoder passwordEncoder;

    public SeedCredentialInitializer(
            UserAccountRepository userAccountRepository,
            PasswordEncoder passwordEncoder
    ) {
        this.userAccountRepository = userAccountRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    @Transactional
    public void run(ApplicationArguments args) {
        for (String email : new String[]{"admin@ims.local", "warehouse@ims.local"}) {
            userAccountRepository.findByEmailIgnoreCase(email).ifPresent(this::ensurePassword);
        }
        log.info("Seed credentials ready (admin@ims.local / demo, warehouse@ims.local / demo)");
    }

    private void ensurePassword(UserAccount user) {
        if (user.getPasswordHash() == null || user.getPasswordHash().isBlank()) {
            user.setPasswordHash(passwordEncoder.encode(SEED_PASSWORD));
            userAccountRepository.save(user);
        }
    }
}
