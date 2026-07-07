# VAN-29 Release Readiness Checklist

Status: **Blocked on repo/env access verification**

## Acceptance criteria check

- Railway env vars are reviewed: **Blocked** — no access to Railway project/service variables in this environment.
- EAS env vars are reviewed: **Blocked** — no access to EAS project/environment configuration in this environment.
- Production API URL is not localhost: **Blocked** — cannot verify the deployed API URL from available evidence.
- Manual-account launch path is confirmed with `EXPO_PUBLIC_PLAID_ENABLED=false` if needed: **Blocked** — cannot verify runtime config or launch behavior from available evidence.

## Launch checklist items

- Cron jobs: **Blocked** — cannot verify whether scheduled jobs are configured and enabled.
- Password reset: **Blocked** — cannot verify end-to-end availability in the current repo/env state.
- Privacy page: **Blocked** — cannot verify deployment and public accessibility.
- Support page: **Blocked** — cannot verify deployment and public accessibility.
- Domain: **Blocked** — cannot verify DNS / hosting / production domain setup.
- Demo account needs: **Blocked** — cannot verify whether demo accounts or seeded test credentials are present.

## Remaining blockers to split into separate Linear issues

1. **Railway environment review / deployment config verification**
2. **EAS environment review / release config verification**
3. **Production API URL validation**
4. **Manual-account launch verification with Plaid disabled**
5. **Cron job setup verification**
6. **Password reset flow verification**
7. **Privacy page deployment verification**
8. **Support page deployment verification**
9. **Domain / DNS verification**
10. **Demo account readiness verification**

## Notes

- This checklist is intentionally limited to release-readiness status only.
- No evidence in the current environment is sufficient to mark the above items done.
