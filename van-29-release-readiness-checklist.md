# VAN-29 Release Readiness Checklist

Review timestamp: 2026-07-07 08:53 MDT  
Revision: Round 2 Managing Editor response  
Issue: [VAN-29 — Complete Railway and EAS release checklist](https://linear.app/vantagefinancial/issue/VAN-29/complete-railway-and-eas-release-checklist)  
Decision: **NOT APPROVED for TestFlight yet.**

This file is the concrete VAN-29 audit artifact. It is intentionally narrow: Railway/EAS release readiness only. Manual accounts first. Plaid production later.

## Revision round 2 response

The Managing Editor's round 2 requirements were re-applied exactly.

What changed in this revision:

- Re-read VAN-29 directly in Linear on 2026-07-07 08:53 MDT.
- Searched Linear again for blocker issues covering Railway, EAS, production API URL, manual-account TestFlight verification, cron jobs, password reset, privacy/support pages, domain, and demo account readiness.
- Result of that Linear search: **no matching separate Linear issues found**.
- Kept all live-environment items blocked because no Railway dashboard/export, EAS dashboard/export, runtime env export, production API health URL, TestFlight build, or owner confirmation was available to this coding agent.
- Added a stricter evidence ledger so each required proof item has one place to be pasted when the real owner provides it.
- Added exact Linear blocker issue drafts for the PM/release owner to create or link. This agent has read-only Linear access, so it cannot create those issues itself.

This still does **not** complete VAN-29. It makes the remaining work auditable and non-ambiguous. Annoying, but true.

## Scope reviewed

Accessible repository contents were reviewed from the connected GitHub workspace.

Observed repo evidence:

- Root contains release/readiness artifacts, but no app source tree was available in this workspace snapshot.
- No `DEPLOYMENT.md` was available in the connected repo snapshot during this audit.
- No `railway.toml`, Railway service config, `.env.example`, `eas.json`, Expo app config, or runtime production env export was available in the connected repo snapshot.
- No Railway dashboard access, EAS dashboard/CLI project access, or deployed production runtime access was available to this coding agent.
- Linear search found no existing separate issues for the unresolved VAN-29 blockers as of 2026-07-07 08:53 MDT.

Result: repo-level evidence was reviewed, but live Railway/EAS environment verification cannot honestly be marked done from the available access.

## Acceptance criteria status

| Acceptance criterion | Status | Evidence / result | Required next action |
|---|---:|---|---|
| Railway env vars are reviewed | **Blocked — evidence missing** | No Railway project/service access or Railway env export was available. No repo Railway config was present in the accessible snapshot. No redacted Variables screenshot/export or written owner confirmation was provided. | Release owner must review actual Railway project/service variables and attach dated proof: redacted Variables screenshot/export or written confirmation, plus Railway service/API health URL. |
| EAS env vars are reviewed | **Blocked — evidence missing** | No EAS project access, `eas env:list` output, dashboard screenshot, build profile, `eas.json`, or Expo app config was available. | Mobile owner must review actual EAS project/build environment and attach dated proof: redacted `eas env:list` output or dashboard screenshot, selected build profile, and confirmation secrets are stored in EAS and not committed. |
| Production API URL is not localhost | **Blocked — unverified** | No production runtime env, EAS env, mobile config, or deployed API URL was available. Could not verify `EXPO_PUBLIC_API_URL` / equivalent. | Mobile owner must provide the actual production/TestFlight API URL, or a redacted equivalent showing HTTPS and not localhost/emulator/LAN/dev tunnel, plus external health-check proof. |
| Manual-account launch path is confirmed with `EXPO_PUBLIC_PLAID_ENABLED=false` if needed | **Blocked — unverified** | No EAS env or runnable app/TestFlight build was available to confirm the flag or manual-account flow. | Mobile/QA owner must confirm the actual TestFlight/EAS environment has `EXPO_PUBLIC_PLAID_ENABLED=false` and that manual accounts can be opened/used without Plaid. |
| Cron jobs, password reset, privacy/support pages, domain, and demo account needs are listed as done or blocked | **Blocked — listed, but blocker issue links missing** | The items are listed below as blocked. No actual separate Linear issue IDs/links were found for them. | PM/release owner must either attach done evidence for each item or create/link separate Linear blocker issues. |
| Remaining blockers are separate Linear issues | **Blocked — not satisfied** | Linear searches found no matching separate blocker issues. This file does not claim they are separated. | PM must create/link the blocker issues listed in `Separate Linear issue status` before VAN-29 can be closed. |

## Round 2 evidence ledger

Paste proof here only after the responsible owner has verified the real system. Do not mark a row done from assumptions, repo comments, or old screenshots.

| Required proof | Owner | Current evidence | Result |
|---|---|---|---:|
| Railway project/service variables reviewed | Release owner | **Missing.** Need dated redacted Railway Variables screenshot/export or written owner confirmation. | **Blocked** |
| Railway service/API health URL | Release owner | **Missing.** Need externally reachable health/root URL. | **Blocked** |
| EAS project/build environment reviewed | Mobile owner | **Missing.** Need dated redacted `eas env:list` output or EAS dashboard screenshot. | **Blocked** |
| Selected EAS build profile | Mobile owner | **Missing.** Need profile name, e.g. `preview`, `production`, or actual configured profile. | **Blocked** |
| Secrets stored in EAS, not committed | Mobile owner | **Missing.** Need owner confirmation after EAS env review. | **Blocked** |
| Production/TestFlight API URL is HTTPS and non-local | Mobile owner | **Missing.** Need actual or redacted URL proving not localhost, emulator, LAN, dev server, or tunnel. | **Blocked** |
| Production API health check from outside local machine | Mobile/release owner | **Missing.** Need date/time, URL, status, and verifier. | **Blocked** |
| `EXPO_PUBLIC_PLAID_ENABLED=false` in actual EAS/TestFlight env | Mobile owner | **Missing.** Need env proof for selected profile/build. | **Blocked** |
| Manual-account smoke test passes in build | Mobile/QA owner | **Missing.** Need build/profile, tester/device, date, and pass/fail evidence. | **Blocked** |
| Cron jobs marked done or tracked by blocker issue | PM/release owner | **Missing.** No done evidence and no Linear blocker issue found. | **Blocked** |
| Password reset marked done or tracked by blocker issue | PM/release owner | **Missing.** No done evidence and no Linear blocker issue found. | **Blocked** |
| Privacy page marked done or tracked by blocker issue | PM/release owner | **Missing.** No URL evidence and no Linear blocker issue found. | **Blocked** |
| Support page marked done or tracked by blocker issue | PM/release owner | **Missing.** No URL evidence and no Linear blocker issue found. | **Blocked** |
| Domain marked done or tracked by blocker issue | PM/release owner | **Missing.** No DNS/domain evidence and no Linear blocker issue found. | **Blocked** |
| Demo account needs marked done or tracked by blocker issue | PM/release owner | **Missing.** No demo/tester evidence and no Linear blocker issue found. | **Blocked** |

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

Evidence slot:

```text
Railway project/service: <missing>
Railway variables reviewed by: <missing>
Review date/time: <missing>
Redacted variables proof: <missing>
Health URL: <missing>
External health check result: <missing>
```

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

Evidence slot:

```text
EAS project: <missing>
Selected build profile: <missing>
EAS env proof: <missing>
Secrets stored in EAS confirmation: <missing>
Reviewer/date: <missing>
```

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
HTTP status/body: <status/redacted acceptable>
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

This coding agent has read-only Linear access. It can verify whether issues exist, but it cannot create or edit them. PM/release owner must create or link the issues below, then paste the IDs/URLs here.

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

## Linear blocker issue drafts for PM

Create these as separate Linear issues if the work cannot be completed immediately. Keep them separate. One mixed mega-ticket will just recreate this mess later.

### 1. Verify Railway production environment for TestFlight API

```text
Title: Verify Railway production environment for TestFlight API
Description: Review the real Railway project/service variables for Worthlane production API readiness. Attach dated redacted Variables screenshot/export or written owner confirmation. Include the Railway service/API health URL and external health-check result.
Acceptance criteria:
- Correct Railway project/service identified.
- Required production env vars are present.
- No production URL points to localhost, emulator, LAN, dev server, or tunnel.
- Secrets are not committed to repo.
- External health URL check is documented.
```

### 2. Verify EAS production/TestFlight environment

```text
Title: Verify EAS production/TestFlight environment
Description: Review the real EAS project/build environment for the selected TestFlight profile. Attach dated redacted eas env:list output or dashboard screenshot. Confirm secrets are stored in EAS and not committed.
Acceptance criteria:
- EAS project and selected build profile are identified.
- EXPO_PUBLIC_API_URL/equivalent points to HTTPS production API.
- EXPO_PUBLIC_PLAID_ENABLED=false unless Plaid production is explicitly ready.
- Secrets are stored in EAS, not committed.
```

### 3. Validate production API URL for TestFlight

```text
Title: Validate production API URL for TestFlight
Description: Confirm the API URL used by the EAS/TestFlight build is HTTPS and not localhost, emulator, LAN, Expo dev server, or tunnel. Include external health-check proof.
Acceptance criteria:
- Actual or redacted production API URL is documented.
- URL uses HTTPS.
- URL is not localhost/private/dev/tunnel.
- Health/root endpoint responds from outside a local developer machine.
```

### 4. Smoke test manual accounts in TestFlight with Plaid disabled

```text
Title: Smoke test manual accounts in TestFlight with Plaid disabled
Description: Verify the actual EAS/TestFlight build has EXPO_PUBLIC_PLAID_ENABLED=false and supports manual-account usage without requiring Plaid.
Acceptance criteria:
- Build/profile/tester/device/date are documented.
- EXPO_PUBLIC_PLAID_ENABLED=false is confirmed for the build.
- App opens without Plaid requirement.
- Manual account create/use flow passes or failures are documented.
```

### 5. Verify production cron/scheduled jobs

```text
Title: Verify production cron/scheduled jobs
Description: Confirm whether cron/scheduled jobs are configured and enabled for launch, or explicitly disabled for launch with no user-facing impact.
Acceptance criteria:
- Scheduler/cron location is identified.
- Enabled/disabled launch decision is documented.
- If enabled, latest successful run or health evidence is attached.
```

### 6. Verify production password reset

```text
Title: Verify production password reset
Description: Verify the deployed password-reset flow works end to end, or document the launch decision if it is blocked/split.
Acceptance criteria:
- Email/provider production env vars are present if required.
- Reset request sends email/link.
- Reset link works in deployed environment.
- Result is documented with date/tester.
```

### 7. Verify privacy page deployment

```text
Title: Verify privacy page deployment
Description: Confirm the production privacy page exists and is reachable for App Store/TestFlight review.
Acceptance criteria:
- Public privacy URL is documented.
- URL returns successful status from outside local machine.
- Page content is appropriate for launch.
```

### 8. Verify support page deployment

```text
Title: Verify support page deployment
Description: Confirm the production support page exists and is reachable for App Store/TestFlight review.
Acceptance criteria:
- Public support URL is documented.
- URL returns successful status from outside local machine.
- Page provides support contact/path.
```

### 9. Verify production domain/DNS

```text
Title: Verify production domain and DNS
Description: Confirm the production domain points to the correct deployed service/API and is ready for launch.
Acceptance criteria:
- Production domain is documented.
- DNS target is verified.
- HTTPS works.
- Domain points to correct production service.
```

### 10. Confirm demo account/TestFlight tester readiness

```text
Title: Confirm demo account and TestFlight tester readiness
Description: Decide whether TestFlight/App Review needs demo credentials or seeded demo data. If yes, create/verify them and document secure handoff.
Acceptance criteria:
- Demo account requirement decision is documented.
- If required, demo account/data is ready.
- Credentials are shared securely, not committed.
- Tester/App Review instructions are documented.
```

## Final VAN-29 result

**VAN-29 cannot be marked complete from the current repo/access.**

What is complete:

- Repo-accessible evidence was reviewed.
- VAN-29 was read directly in Linear again during round 2.
- Linear was searched again for separate blocker issues. None were found.
- The production API URL requirement is defined and remains unverified.
- The manual-account-first path and required `EXPO_PUBLIC_PLAID_ENABLED=false` setting are documented.
- Checklist gaps are explicit.
- Evidence slots have been added for every Managing Editor-required proof item.
- PM-ready Linear blocker issue drafts have been added because the actual blocker issues do not exist yet and this agent cannot create them.

What remains blocked:

- Live Railway env review with dated evidence.
- Live EAS env review with dated evidence.
- Actual production/TestFlight API URL verification.
- Actual TestFlight/manual-account verification with Plaid disabled.
- Done evidence or linked blocker issues for cron jobs, password reset, privacy page, support page, domain, and demo account readiness.
- Creation/linking of separate Linear issues for remaining blockers.

Do not approve TestFlight readiness from this artifact until the missing evidence or real Linear blocker links are attached.
