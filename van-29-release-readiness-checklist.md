# VAN-29 Release Readiness Checklist

Review timestamp: 2026-07-07 08:52 MDT  
Revision: Round 1 Managing Editor response  
Issue: [VAN-29 — Complete Railway and EAS release checklist](https://linear.app/vantagefinancial/issue/VAN-29/complete-railway-and-eas-release-checklist)  
Decision: **NOT APPROVED for TestFlight yet.**

This file is the concrete VAN-29 audit artifact. It is intentionally narrow: Railway/EAS release readiness only. Manual accounts first. Plaid production later.

## Revision round 1 response

The Managing Editor required evidence-backed updates for Railway, EAS, production API URL, manual-account TestFlight behavior, launch checklist blockers, and separate Linear issue IDs.

Current result: **those evidence-backed confirmations still cannot be completed from this agent's access.**

What was verified in this revision:

- VAN-29 was read directly in Linear.
- Linear was searched again for existing blocker issues related to Railway env verification, EAS env verification, production API URL validation, cron jobs, password reset, privacy/support pages, domain, demo account readiness, and TestFlight/manual-account verification.
- No matching separate Linear issues were found.
- The checklist below now removes any implication that blockers have already been separated into Linear issues.
- Each blocked launch item now explicitly says whether a linked blocker issue exists. It does not.

No Railway dashboard/export, EAS dashboard/export, runtime env export, deployed API health URL, app source tree, or runnable TestFlight build was available to this coding agent. Marking the acceptance criteria done without those would be fake progress. Still bad theater.

## Scope reviewed

Accessible repository contents were reviewed from the connected GitHub workspace.

Observed repo evidence:

- Root contains release/readiness artifacts, but no app source tree was available in this workspace snapshot.
- No `DEPLOYMENT.md` was available in the connected repo snapshot during this audit.
- No `railway.toml`, Railway service config, `.env.example`, `eas.json`, Expo app config, or runtime production env export was available in the connected repo snapshot.
- No Railway dashboard access, EAS dashboard/CLI project access, or deployed production runtime access was available to this coding agent.
- Linear search found no existing separate issues for the unresolved VAN-29 blockers as of 2026-07-07 08:52 MDT.

Result: repo-level evidence was reviewed, but live Railway/EAS environment verification cannot honestly be marked done from the available access.

## Acceptance criteria status

| Acceptance criterion | Status | Evidence / result | Required next action |
|---|---:|---|---|
| Railway env vars are reviewed | **Blocked — evidence missing** | No Railway project/service access or Railway env export was available. No repo Railway config was present in the accessible snapshot. No redacted Variables screenshot/export or written owner confirmation was provided. | Release owner must review actual Railway project/service variables and attach dated proof: redacted Variables screenshot/export or written confirmation, plus Railway service/API health URL. |
| EAS env vars are reviewed | **Blocked — evidence missing** | No EAS project access, `eas env:list` output, dashboard screenshot, build profile, `eas.json`, or Expo app config was available. | Mobile owner must review actual EAS project/build environment and attach dated proof: redacted `eas env:list` output or dashboard screenshot, selected build profile, and confirmation secrets are stored in EAS and not committed. |
| Production API URL is not localhost | **Blocked — unverified** | No production runtime env, EAS env, mobile config, or deployed API URL was available. Could not verify `EXPO_PUBLIC_API_URL` / equivalent. | Mobile owner must provide the actual production/TestFlight API URL, or a redacted equivalent showing HTTPS and not localhost/emulator/LAN/dev tunnel. |
| Manual-account launch path is confirmed with `EXPO_PUBLIC_PLAID_ENABLED=false` if needed | **Blocked — unverified** | No EAS env or runnable app/TestFlight build was available to confirm the flag or manual-account flow. | Mobile/QA owner must confirm the actual TestFlight/EAS environment has `EXPO_PUBLIC_PLAID_ENABLED=false` and that manual accounts can be opened/used without Plaid. |
| Cron jobs, password reset, privacy/support pages, domain, and demo account needs are listed as done or blocked | **Blocked — listed, but blocker issue links missing** | The items are listed below as blocked. No actual separate Linear issue IDs/links were found for them. | PM/release owner must either attach done evidence for each item or create/link separate Linear blocker issues. |
| Remaining blockers are separate Linear issues | **Blocked — not satisfied** | Linear searches found no matching separate blocker issues. This file no longer claims they are separated. | PM must create/link the blocker issues listed in `Separate Linear issue status` before VAN-29 can be closed. |

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

Required evidence to mark done: redacted Railway Variables screenshot/export, dated owner confirmation, and the production API health URL.

Current status: **blocked — no Railway evidence was available.**

### EAS / Expo build environment

Minimum mobile-owner verification needed:

- [ ] Correct EAS project selected.
- [ ] Selected EAS build profile is identified.
- [ ] `EXPO_PUBLIC_API_URL` or equivalent is set to the production Railway/API URL.
- [ ] Production API URL starts with `https://`.
- [ ] Production API URL is not localhost, emulator host, LAN IP, Expo dev server, or temporary tunnel.
- [ ] `EXPO_PUBLIC_PLAID_ENABLED=false` for manual-account-first TestFlight unless Plaid production is actually ready.
- [ ] Any Plaid sandbox variables are either absent from production builds or harmless with Plaid disabled.
- [ ] Apple bundle identifier, build profile, and submit profile are correct for TestFlight.
- [ ] Secrets are stored in EAS env/secrets, not committed to the repo.

Required evidence to mark done: redacted `eas env:list` output or EAS dashboard screenshot, selected EAS build profile name, and confirmation secrets are in EAS rather than committed.

Current status: **blocked — no EAS evidence was available.**

## Production API URL verification rule

A production/TestFlight API URL is acceptable only if all are true:

- Uses HTTPS.
- Points to the Railway production API service or approved production API domain.
- Is not `localhost`, `127.0.0.1`, `0.0.0.0`, `10.0.2.2`, a private LAN IP, an Expo dev server URL, or a temporary tunnel.
- Responds to the expected health/root endpoint from outside the developer machine.

Current status: **blocked — no runtime URL evidence was available.**

Required proof to close this row:

```text
EXPO_PUBLIC_API_URL=https://<production-api-domain-or-redacted-equivalent>
Health URL: https://<production-api-domain-or-redacted-equivalent>/<health-endpoint>
Verified from outside local machine on: <date/time>
Verified by: <owner>
```

## Manual-account-first launch path

VAN-29 explicitly says manual accounts first and Plaid production later.

Required TestFlight launch setting unless Plaid production is confirmed ready:

```env
EXPO_PUBLIC_PLAID_ENABLED=false
```

Required functional check:

- [ ] Actual EAS/TestFlight environment contains `EXPO_PUBLIC_PLAID_ENABLED=false`.
- [ ] App opens without requiring Plaid.
- [ ] User can create or use a manual account.
- [ ] User can add/edit manual balances/transactions as supported by current scope.
- [ ] Plaid entry points are hidden, disabled, or safely non-blocking.

Current status: **blocked — no EAS env or runnable app/TestFlight build was available in this workspace.**

Required proof to close this row:

```text
EAS profile: <profile>
EXPO_PUBLIC_PLAID_ENABLED=false confirmed on: <date/time>
Manual account smoke test result: pass/fail
Tester/device/build: <redacted acceptable>
Verified by: <owner>
```

## Launch checklist items

| Item | Status | Evidence / result | Linked blocker issue |
|---|---:|---|---|
| Cron jobs | **Blocked** | No Railway/service scheduler evidence available. Need proof configured/enabled, or explicit decision that cron is disabled for launch. | **Missing.** No matching Linear issue found. |
| Password reset | **Blocked** | No deployed flow evidence available. Need end-to-end proof reset email/link works, or explicit launch decision to block/split. | **Missing.** No matching Linear issue found. |
| Privacy page | **Blocked** | No public URL evidence available. Need deployed privacy URL. | **Missing.** No matching Linear issue found. |
| Support page | **Blocked** | No public URL evidence available. Need deployed support URL. | **Missing.** No matching Linear issue found. |
| Domain | **Blocked** | No DNS/domain evidence available. Need production domain proof pointing to the correct service. | **Missing.** No matching Linear issue found. |
| Demo account needs | **Blocked** | No demo credentials/seed/tester-readiness evidence available. Need decision whether TestFlight needs demo accounts, then proof. | **Missing.** No matching Linear issue found. |

## Separate Linear issue status

Acceptance criterion: remaining blockers must be separate Linear issues.

Current status: **not satisfied.** No actual issue IDs/links were found in Linear for the unresolved blockers.

Create/link these issues, or complete the work directly and attach evidence here:

| Required blocker issue | Current Linear ID/link |
|---|---|
| Railway production environment verification | **Missing** |
| EAS production/TestFlight environment verification | **Missing** |
| Production API URL validation | **Missing** |
| Manual account TestFlight verification with Plaid disabled | **Missing** |
| Cron/scheduled job production verification | **Missing** |
| Password reset production verification | **Missing** |
| Privacy page deployment verification | **Missing** |
| Support page deployment verification | **Missing** |
| Production domain/DNS verification | **Missing** |
| Demo account/TestFlight tester readiness | **Missing** |

## Final VAN-29 result

**VAN-29 cannot be marked complete from the current repo/access.**

What is complete:

- Repo-accessible evidence was reviewed.
- VAN-29 was read directly in Linear.
- Linear was searched again for separate blocker issues.
- The production API URL requirement is defined and remains unverified.
- The manual-account-first path and required `EXPO_PUBLIC_PLAID_ENABLED=false` setting are documented.
- Checklist gaps are explicit.
- The file now clearly states that separate Linear blocker issues are **missing**, not completed.

What remains blocked:

- Live Railway env review with dated evidence.
- Live EAS env review with dated evidence.
- Actual production/TestFlight API URL verification.
- Actual TestFlight/manual-account verification with Plaid disabled.
- Done evidence or linked blocker issues for cron jobs, password reset, privacy page, support page, domain, and demo account readiness.
- Creation/linking of separate Linear issues for remaining blockers.
