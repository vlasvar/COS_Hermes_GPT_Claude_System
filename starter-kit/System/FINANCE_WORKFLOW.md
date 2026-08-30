# Finance-first workflow

## 1. Plain-English onboarding

Ask the user to describe their financial situation in plain English, including:

- Income amounts and the dates they are received
- Expense amounts and the dates they are paid or due
- Whether each income or expense repeats
- Currency, when it is not already clear

Do not ask for a reporting period before data exists. Infer useful periods from the supplied dates and recurrence. Ask follow-up questions only when a missing fact materially prevents correct recording. Identity information is optional.

Parse the answer into `Income`, `Expenses`, and `Recurring Costs`. Create stable IDs, preserve the user's wording in Description or Notes, mark unsupported details `Provisional`, write the rows, read them back, and correct any structural issue in the Sheet.

## 2. Optional evidence intake

After recording the plain-English answer, offer the user the option to place screenshots, receipts, exports, or statements in `Inbox/Expenses-and-Receipts`. Do not make evidence a prerequisite for starting.

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

For Income, capture the received or expected date, source, description, amount, currency, frequency, next expected date, confidence, status, evidence link when available, and uncertainty notes. Never invent an employer, source, amount, or date.

## 4. Clarification

Batch minor uncertainties. Interrupt only when an ambiguity materially changes the amount, currency, duplicate status, or reporting period.

When the user clarifies a record, update it, mark it `Confirmed`, preserve the source link, and log the correction.

## 5. Recurring costs

Create or update a Recurring Cost when evidence or repeated transactions support recurrence. Record frequency and next expected date only when supported; otherwise leave them blank and explain the uncertainty.

## 6. Budget

After enough Expenses exist:

1. Summarize spending by category and period.
2. Separate recurring from variable expenses.
3. Use recorded Income and ask for missing budget constraints only when needed.
4. Propose Budget rows.
5. Write approved internal Budget rows without repeated permission prompts.
6. Calculate actuals and variance from recorded Expenses.

## 7. First report

Create a report in `Reports` containing:

- Evidence period covered
- Total recorded income
- Total recorded expenses
- Expected net cash flow
- Spending by category
- Recurring costs and possible subscriptions
- Fixed versus variable spending
- Ambiguous or missing information
- Proposed budget
- High-value next evidence to provide

State clearly which figures are Provisional and which are Confirmed.
