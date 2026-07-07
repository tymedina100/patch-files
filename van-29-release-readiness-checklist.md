# VAN-29 Release Readiness Checklist

Review timestamp: 2026-07-07 08:50 MDT
Issue: VAN-29 — Complete Railway and EAS release checklist
Decision: **NOT APPROVED for TestFlight yet.**

This file is the concrete VAN-29 audit artifact. It is intentionally narrow: Railway/EAS release readiness only. Manual accounts first. Plaid production later.

## Scope reviewed

Accessible repository contents were reviewed from the connected GitHub workspace.

Observed repo evidence:

- Root contains release/readiness artifacts, but no app source tree was available in this workspace snapshot.
- No `DEPLOYMENT.md` was available in the connected repo snapshot during this audit.
- No `railway.toml`, Railway service config, `.env.example`, `eas.json`, Expo app config, or runtime production env export was available in the connected repo snapshot.
- No Railway dashboard access, EAS dashboard/CLI project access, or deployed production runtime access was available to this coding agent.
- Linear search found no existing separate issues for the unresolved VAN-29 blockers.

Result: repo-level evidence was reviewed, but live Railway/EAS environment verification cannot honestly be marked done from the available access. Pretending otherwise would be theater. Bad theater.

## Acceptance criteria status

| Acceptance criterion | Status | Evidence / result | Required next action |
|---|---:|---|---|
| Railway env vars are reviewed | **Blocked** | No Railway project/service access or Railway env export was available. No repo Railway config was present in the accessible snapshot. | Release owner must review Railway variables and attach a redacted export/screenshot or dated written confirmation. |
| EAS env vars are reviewed | **Blocked** | No EAS project access or EAS env export was available. No `eas.json` or Expo app config was present in the accessible snapshot. | Mobile owner must review EAS variables and attach a redacted export/screenshot or dated written confirmation. |
| Production API URL is not localhost | **Blocked** | No production runtime env or mobile config was available. Could not verify `EXPO_PUBLIC_API_URL` / equivalent. | Confirm the TestFlight build uses an HTTPS production API URL, not `localhost`, `127.0.0.1`, `10.0.2.2`, LAN IPs, or ngrok/dev tunnels. |
| Manual-account launch path is confirmed with `EXPO_PUBLIC_PLAID_ENABLED=false` if needed | **Blocked** | No runnable app source or EAS env was available to confirm the flag or manual account flow. | For the first TestFlight path, set/confirm `EXPO_PUBLIC_PLAID_ENABLED=false` unless Plaid production is explicitly ready. Verify manual account creation/editing works in the build. |

## Required environment checks

### Railway API service

Minimum release-owner verification needed:

- [ ] Correct Railway project and service selected.
- [ ] Production database URL / connection string present.
- [ ] Auth/session/JWT secrets present and production-grade.
- [ ] Password reset email/provider variables present if password reset is expected for launch.
- [ ] Cron/scheduled job variables present, or cron intentionally disabled and tracked separately.
- [ ] Public API domain configured.
- [ ] API CORS / allowed origins include the production app/domain as needed.
- [ ] No required production URL points to `localhost`, `127.0.0.1`, `10.0.2.2`, private LAN IPs, or dev tunnels.
- [ ] Secrets are not committed to the repo.

Suggested evidence format: redacted Railway Variables screenshot/export plus the production API health URL.

### EAS / Expo build environment

Minimum mobile-owner verification needed:

- [ ] Correct EAS project selected.
- [ ] `EXPO_PUBLIC_API_URL` or equivalent is set to the production Railway/API URL.
- [ ] Production API URL starts with `https://`.
- [ ] Production API URL is not localhost, emulator host, LAN IP, or temporary tunnel.
- [ ] `EXPO_PUBLIC_PLAID_ENABLED=false` for manual-account-first TestFlight unless Plaid production is actually ready.
- [ ] Any Plaid sandbox variables are either absent from production builds or harmless with Plaid disabled.
- [ ] Apple bundle identifier, build profile, and submit profile are correct for TestFlight.
- [ ] Secrets are stored in EAS env/secrets, not committed to the repo.

Suggested evidence format: redacted `eas env:list`/dashboard screenshot plus the selected EAS build profile name.

## Production API URL verification rule

A production/TestFlight API URL is acceptable only if all are true:

- Uses HTTPS.
- Points to the Railway production API service or approved production API domain.
- Is not `localhost`, `127.0.0.1`, `0.0.0.0`, `10.0.2.2`, a private LAN IP, an Expo dev server URL, or a temporary tunnel.
- Responds to the expected health/root endpoint from outside the developer machine.

Current status: **blocked — no runtime URL evidence was available.**

## Manual-account-first launch path

VAN-29 explicitly says manual accounts first and Plaid production later.

Required TestFlight launch setting unless Plaid production is confirmed ready:

```env
EXPO_PUBLIC_PLAID_ENABLED=false
```

Required functional check:

- [ ] App opens without requiring Plaid.
- [ ] User can create or use a manual account.
- [ ] User can add/edit manual balances/transactions as supported by current scope.
- [ ] Plaid entry points are hidden, disabled, or safely non-blocking.

Current status: **blocked — no EAS env or runnable app source was available in this workspace.**

## Launch checklist items

| Item | Status | Evidence / next action |
|---|---:|---|
| Cron jobs | **Blocked** | No Railway/service scheduler evidence available. Verify configured/enabled, or split to a Linear issue. |
| Password reset | **Blocked** | No deployed flow evidence available. Verify end-to-end reset email/link works, or split to a Linear issue. |
| Privacy page | **Blocked** | No public URL evidence available. Verify deployed public page, or split to a Linear issue. |
| Support page | **Blocked** | No public URL evidence available. Verify deployed public page, or split to a Linear issue. |
| Domain | **Blocked** | No DNS/domain evidence available. Verify production domain points to the right service, or split to a Linear issue. |
| Demo account needs | **Blocked** | No demo credentials/seed evidence available. Confirm whether TestFlight needs demo accounts, then verify or split to a Linear issue. |

## Separate Linear issues still needed

No existing matching Linear issues were found for these blockers during this audit. Create separate issues before VAN-29 is closed if they cannot be completed immediately:

1. Railway production environment verification
2. EAS production/TestFlight environment verification
3. Production API URL validation
4. Manual account TestFlight verification with Plaid disabled
5. Cron/scheduled job production verification
6. Password reset production verification
7. Privacy page deployment verification
8. Support page deployment verification
9. Production domain/DNS verification
10. Demo account/TestFlight tester readiness

## Final VAN-29 result

**VAN-29 cannot be marked complete from the current repo/access.**

What is complete:

- Repo-accessible evidence was reviewed.
- The production API URL requirement was defined and remains unverified.
- The manual-account-first path and required `EXPO_PUBLIC_PLAID_ENABLED=false` setting were documented.
- Checklist gaps are now explicit.
- Remaining blockers are enumerated for separate Linear issues.

What remains blocked:

- Live Railway env review.
- Live EAS env review.
- Actual production API URL verification.
- Actual TestFlight/manual-account verification.
