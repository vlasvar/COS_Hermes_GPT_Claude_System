# Bonus: separate dashboard using GPT Sites

“GPT Sites” is used here as a working label for a site generated or hosted through a GPT-assisted website experience. Product naming and supported integrations may change. The dashboard is optional and must remain replaceable.

## Purpose

Give the user a clear operational view without requiring them to navigate raw Sheet tabs.

## Suggested pages

- **Money:** expenses, category totals, recurring costs, and budget variance
- **Today:** due Actions, active Commitments, and top priorities
- **Approvals:** operations waiting for explicit authorization
- **Projects:** outcome, owner, status, next Action, and review date
- **Risks:** overdue records, blockers, conflicting facts, and missing evidence
- **Decisions:** recent Decisions and fired revisit triggers
- **Reviews:** latest weekly Review and prior periods
- **Agent activity:** recent Agent Log entries

## Non-negotiable data rule

```text
Google Sheet → read/write adapter → dashboard
```

The dashboard must not maintain a parallel task store. Every mutation targets the canonical record ID in the Sheet and writes an Agent Log entry.

## Minimum data contract

A dashboard adapter should expose:

- `listToday()`
- `listExpenses(period, status)`
- `getBudget(period)`
- `listRecurringCosts(status)`
- `listPendingApprovals()`
- `listProjects(status)`
- `getRecord(type, id)`
- `proposeChange(type, id, patch)`
- `approveOperation(logId)`
- `runWeeklyReview()`

High-impact operations remain behind the kernel approval policy.

## Site-generation brief

Use this brief in a compatible GPT-assisted site builder:

> Create a calm, professional Chief of Staff dashboard. Use strong typography, generous spacing, and clear hierarchy rather than a generic SaaS aesthetic. Build pages for Today, Approvals, Projects, Risks, Decisions, Reviews, and Agent Activity. Treat the supplied Google Sheet adapter as the only operational source of truth. Never store private records in browser local storage beyond a short-lived cache. Show evidence links, last-updated timestamps, approval states, and explicit error states. Do not claim an update succeeded until the adapter confirms the write and the record is read back.

## Privacy and authentication requirements

- Require authenticated access.
- Do not expose a public Sheet link.
- Request least-privilege Google scopes.
- Keep credentials server-side or in the platform's approved secret store.
- Avoid analytics that capture record contents.
- Provide a visible sign-out control and error state.
- Re-read a record after every write before showing success.

## MVP dashboard acceptance test

1. Today and Projects reflect seeded fictional Sheet data.
2. An approval remains pending until the user explicitly approves it.
3. An approved internal update writes to the Sheet and Agent Log.
4. A failed write displays failure and does not optimistically claim success.
5. Refreshing the page reconstructs state from the Sheet.
