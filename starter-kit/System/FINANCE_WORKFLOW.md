# Finance-first workflow

## 1. Minimal onboarding

Ask one short question at a time:

1. What is the primary currency?
2. Which period should be examined first?
3. Is the scope personal, household, business, or combined?
4. What budget period should be used?

Identity information is optional. Begin work without it.

## 2. Intake

Ask the user to place screenshots, receipts, exports, or statements in `Inbox/Expenses-and-Receipts`.

For each source:

1. Check whether it was already processed.
2. Extract only visible information.
3. Create an Expense with a stable ID.
4. Link the source file.
5. Mark the record `Provisional` unless the evidence is unambiguous and the user has authorized direct confirmation.
6. Record confidence as High, Medium, or Low.
7. Add an Agent Log entry and verify the Sheet write.

## 3. Expense fields

Capture when visible:

- Date
- Merchant
- Description
- Amount
- Currency
- Category
- Payment method, without full account or card numbers
- Recurrence
- Source link
- Notes about uncertainty

Never guess a missing amount, date, currency, or merchant.

## 4. Clarification

Batch minor uncertainties. Interrupt only when an ambiguity materially changes the amount, currency, duplicate status, or reporting period.

When the user clarifies a record, update it, mark it `Confirmed`, preserve the source link, and log the correction.

## 5. Recurring costs

Create or update a Recurring Cost when evidence or repeated transactions support recurrence. Record frequency and next expected date only when supported; otherwise leave them blank and explain the uncertainty.

## 6. Budget

After enough Expenses exist:

1. Summarize spending by category and period.
2. Separate recurring from variable expenses.
3. Ask for missing income or budget constraints only when needed.
4. Propose Budget rows.
5. Write approved internal Budget rows without repeated permission prompts.
6. Calculate actuals and variance from recorded Expenses.

## 7. First report

Create a report in `Reports` containing:

- Evidence period covered
- Total recorded expenses
- Spending by category
- Recurring costs and possible subscriptions
- Fixed versus variable spending
- Ambiguous or missing information
- Proposed budget
- High-value next evidence to provide

State clearly which figures are Provisional and which are Confirmed.
