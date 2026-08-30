# Data dictionary

The native Google Sheet named `COS_DATABASE` is the operational source of truth.

## Finance-first tabs

- **System Check:** Connector read/write capability and verification results.
- **Expenses:** Individual expense records extracted from evidence or entered by the user.
- **Budget:** Planned and actual amounts by period and category.
- **Recurring Costs:** Repeating expenses and possible subscriptions.

## Chief of Staff tabs

- **Inbox:** Unprocessed information.
- **Projects:** Outcomes requiring multiple Actions.
- **Actions:** Concrete next steps with one owner.
- **Commitments:** Promises made by or to the user.
- **Decisions:** Chosen options, rationale, and revisit triggers.
- **Contacts:** People or organizations relevant to active records.
- **Reviews:** Periodic summaries, risks, and priorities.
- **Agent Log:** Material proposals, writes, verification results, failures, and corrections.

## Record rules

- Use stable IDs in the form `<TYPE>-<YYYYMMDD>-<4 digits>`.
- Never reuse an ID.
- Link source evidence when available.
- Use ISO-style dates where possible: `YYYY-MM-DD`.
- Use explicit currency codes such as `EUR`, `USD`, or `GBP`.
- Expense status is normally `Provisional`, `Confirmed`, `Rejected`, or `Duplicate`.
- Confidence is `High`, `Medium`, or `Low`.
- Preserve uncertainty in Notes rather than filling gaps with guesses.
