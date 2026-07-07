# VAN-29 Release Readiness Checklist

Status: **Release path NOT APPROVED — do not ship until the blockers below are verified or closed, or each remaining blocker is tracked in a separate Linear issue with an actual issue ID/link.**

## Acceptance criteria check

| Acceptance criterion | Status | Evidence / access gap proof | Owner | Required next action |
|---|---:|---|---|---|
| Railway env vars are reviewed | **Blocked** | No Railway project/service access is available in this environment. No Railway Variables screenshot, export, or dated release-owner confirmation has been provided. | Release owner / Engineering owner | Review Railway service/project variables and attach a dated screenshot/export or written confirmation. |
| EAS env vars are reviewed | **Blocked** | No EAS project/environment access is available in this environment. No EAS environment review confirmation has been provided. | Release owner / Mobile owner | Review EAS environment variables and attach confirmation or export. |
| Production API URL is not localhost | **Blocked** | No deployed runtime evidence was provided showing the production API URL. | Engineering owner | Verify production API URL and confirm it is not localhost. |
| Manual-account launch path is confirmed with `EXPO_PUBLIC_PLAID_ENABLED=false` if needed | **Blocked** | No runtime confirmation or launch evidence was provided for the manual-account path with Plaid disabled. | Mobile owner / Engineering owner | Confirm the app launches and manual accounts work with `EXPO_PUBLIC_PLAID_ENABLED=false`. |

## Launch checklist items

| Item | Status | Owner | Evidence / next action |
|---|---:|---|---|
| Cron jobs | **Blocked** | Backend owner | Verify scheduled jobs are configured and enabled, or open a separate Linear issue for the missing setup. |
| Password reset | **Blocked** | Backend owner | Verify the end-to-end password reset flow, or open a separate Linear issue for the broken/missing flow. |
| Privacy page | **Blocked** | Web / product owner | Verify the privacy page is deployed and publicly accessible, or open a separate Linear issue. |
| Support page | **Blocked** | Web / product owner | Verify the support page is deployed and publicly accessible, or open a separate Linear issue. |
| Domain | **Blocked** | Infra / release owner | Verify DNS / hosting / production domain setup, or open a separate Linear issue. |
| Demo account needs | **Blocked** | Product owner | Verify demo accounts or seeded test credentials exist and are usable, or open a separate Linear issue. |

## Remaining blockers to split into separate Linear issues

These blockers remain unresolved and must be tracked in separate Linear issues with actual IDs/links before VAN-29 can be approved:

- Railway environment review / deployment config verification
- EAS environment review / release config verification
- Production API URL validation
- Manual-account launch verification with Plaid disabled
- Cron job setup verification
- Password reset flow verification
- Privacy page deployment verification
- Support page deployment verification
- Domain / DNS verification
- Demo account readiness verification

## Final decision

**Release path is not approved for TestFlight until all VAN-29 blockers are verified or tracked in separate Linear issues with actual issue IDs/links.**

## Notes

- This checklist is intentionally limited to release-readiness status only.
- No evidence in the current environment is sufficient to mark the above items done.
