# Finance-first workflow

## 1. Capability check

Before collecting user information, verify read and write access to `System Check` and `Agent Log`. Read back both writes. Stop with a precise explanation if the connector is read-only.

## 2. Plain-English onboarding

Ask the user to describe their financial situation in plain English. Request income, expenses, amounts, received or due dates, recurrence, and currency when unclear. Do not ask for a reporting period before data exists; infer useful periods from the facts supplied. Ask follow-ups only for material gaps. A name and biography are optional.

Convert the answer into verified `Income`, `Expenses`, and `Recurring Costs` rows. Preserve uncertainty and the user's wording rather than guessing.

## 3. Optional evidence intake

After the initial rows exist, offer screenshots, receipts, exports, or statements as optional supporting evidence.

For each source:

1. Detect duplicates.
2. Extract visible facts only.
3. Create a stable Expense ID.
4. Link the source.
5. Record confidence.
6. Keep uncertain data `Provisional`.
7. Write and verify the Expense and Agent Log entries.

Capture date, merchant, description, amount, currency, category, payment method when visible, recurrence, source link, and uncertainty notes. Never guess missing values.

## 4. Clarification and confirmation

Batch minor questions. Interrupt only for ambiguities that materially change amount, currency, duplicate status, or reporting period. When clarified, update the record to `Confirmed`, preserve evidence, and log the correction.

## 5. Recurring costs and budget

Infer recurrence only when repeated records or explicit evidence support it. After sufficient evidence exists:

1. Summarize spending by period and category.
2. Separate recurring from variable expenses.
3. Ask only for missing constraints required for budgeting.
4. Create Budget rows.
5. Calculate actuals and variance from Expenses.
6. Verify all writes.

## 6. First report

Report the evidence period, total recorded income, total recorded expenses, expected net cash flow, category totals, recurring costs, possible subscriptions, fixed versus variable spending, missing information, proposed budget, and the most valuable next evidence to provide. Distinguish Provisional from Confirmed figures.
