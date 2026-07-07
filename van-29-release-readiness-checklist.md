# VAN-29 Release Readiness Checklist

Status: **Release path NOT APPROVED — do not ship until the blockers below are verified or closed.**

## Acceptance criteria check

| Acceptance criterion | Status | Evidence / access gap proof | Owner | Required next action |
|---|---:|---|---|---|
| Railway env vars are reviewed | **Blocked** | No Railway project/service access is available in this environment. No Railway Variables screenshot, export, or dated release-owner confirmation has been provided. | Release owner / Engineering owner | Review Railway service/project variables and attach a dated screenshot/export or written confirmation. |
| EAS env vars are reviewed | **Blocked** | No EAS project/environment access is available in this environment. No EAS environment review confirmation has been provided. | Release owner / Mobile owner | Review EAS environment variables and attach confirmation or export. |
| Production API URL is not localhost | **Blocked** | No deployed runtime evidence was provided showing the production API URL. | Engineering owner | Verify production API URL and confirm it is not localhost. |
| Manual-account launch path is confirmed with `EXPO_PUBLIC_PLAID_ENABLED=false` if needed | **Blocked** | No runtime confirmation or launch evidence was provided for the manual-account path with Plaid disabled. | Mobile owner / Engineering owner | Confirm the app launches and manual accounts work with `EXPO_PUBLIC_PLAID_ENABLED=false`. |

## Launch checklist items

| Item | Status | Evidence / next action |
|---|---:|---|
| Cron jobs | **Blocked** | Verify scheduled jobs are configured and enabled, or open a separate Linear issue for the missing setup. |
| Password reset | **Blocked** | Verify the end-to-end password reset flow, or open a separate Linear issue for the broken/missing flow. |
| Privacy page | **Blocked** | Verify the privacy page is deployed and publicly accessible, or open a separate Linear issue. |
| Support page | **Blocked** | Verify the support page is deployed and publicly accessible, or open a separate Linear issue. |
| Domain | **Blocked** | Verify DNS / hosting / production domain setup, or open a separate Linear issue. |
| Demo account needs | **Blocked** | Verify demo accounts or seeded test credentials exist and are usable, or open a separate Linear issue. |

## Remaining blockers to split into separate Linear issues

1. Railway environment review / deployment config verification
2. EAS environment review / release config verification
3. Production API URL validation
4. Manual-account launch verification with Plaid disabled
5. Cron job setup verification
6. Password reset flow verification
7. Privacy page deployment verification
8. Support page deployment verification
9. Domain / DNS verification
10. Demo account readiness verification

## Final decision

**Release path is not approved for TestFlight until all VAN-29 blockers are verified or tracked in separate Linear issues.**

## Notes

- This checklist is intentionally limited to release-readiness status only.
- No evidence in the current environment is sufficient to mark the above items done.
