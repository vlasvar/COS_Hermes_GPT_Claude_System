# Start here

This folder is a private, finance-first Chief of Staff workspace. The Google Sheet is the operational source of truth. Screenshots and documents stay in this Drive folder as evidence.

## Human setup

1. Upload this entire extracted folder to a private Google Drive folder.
2. Open `COS_DATABASE_TEMPLATE.xlsx` with Google Sheets.
3. Choose **File → Save as Google Sheets** and name the new native Sheet `COS_DATABASE`.
4. Keep the new Sheet inside this folder. The `.xlsx` file remains only as a clean template.
5. Open `01_COPY_THIS_PROMPT.txt`, replace `[PASTE GOOGLE DRIVE FOLDER LINK HERE]`, and send the complete prompt to an agent that can access Google Drive.

Do not make the folder or Sheet public. Do not place passwords, API keys, full payment-card numbers, identity documents, or authentication codes in this workspace.

## Agent bootstrap

Read these files before asking onboarding questions:

1. `System/AGENT_RULES.md`
2. `System/FINANCE_WORKFLOW.md`
3. `System/DATA_DICTIONARY.md`
4. `System/OPTIONAL_PROFILE.md`

Then find the native Google Sheet named `COS_DATABASE` and run the capability check below.

### Required capability check

1. Read the `System Check` tab.
2. Update `CHECK-WRITE` with a harmless test value, timestamp, and status.
3. Read the same row back.
4. Add a material-operation entry to `Agent Log`.
5. Read the log entry back.
6. Mark the capability result as `Passed` only after both writes are verified.

If any write cannot be completed, explain the exact connector or permission limitation and stop. A prompt cannot create missing tool permissions. Do not pretend onboarding is complete.

## First mission

The first mission is to build a useful income, expense, and cash-flow picture from what the user already knows.

Ask one open question:

> Describe your financial situation in plain English. Include your income and expenses, their amounts, and the dates you receive or pay them. Mention whether each item repeats. You can provide screenshots or statements afterward if you want.

Example answer: "I earn 3,500 EUR every month and get paid on the 1st. I pay 600 EUR rent on the 5th of every month."

Extract currency, scope, recurrence, and useful reporting dates from the answer. Do not ask for a reporting period before data exists. Ask a follow-up only for a material missing fact that prevents a correct record. If the user gives no currency, ask for it after the open answer.

A name and other identity details are optional. Do not delay finance onboarding to collect a biography.

Write the supplied facts into `Income`, `Expenses`, and `Recurring Costs`, then read them back and fix the Sheet structure if needed. Treat unsupported details as `Provisional`. Afterward, offer the user the option to place screenshots, receipts, or statements in `Inbox/Expenses-and-Receipts`; evidence is helpful but not required to start. Follow `System/FINANCE_WORKFLOW.md` for recording, clarification, budgeting, and reporting.
