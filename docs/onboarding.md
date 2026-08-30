# Onboarding a finance-first private instance

The beginner path uses one downloadable folder and one bootstrap prompt.

## 1. Upload the starter

1. Download `dist/COS_Finance_First_Starter.zip`.
2. Extract it.
3. Upload the complete `COS_Finance_First_Starter` folder to private Google Drive storage.
4. Keep sharing set to Restricted.

## 2. Create the native operational store

Open `COS_DATABASE_TEMPLATE.xlsx` with Google Sheets, choose **File → Save as Google Sheets**, name the result `COS_DATABASE`, and keep it in the starter folder.

A native Google Sheet cannot be packaged inside a ZIP. This conversion is the only required database-provisioning step. The Apps Script under `System/Advanced` remains an optional fallback.

## 3. Start the agent

Open `01_COPY_THIS_PROMPT.txt`, replace the folder-link placeholder, and send the complete prompt to an agent that can access the private Google Drive folder.

The prompt grants Workspace Operator authority inside the COS folder. It does not grant authority for spending, external communication, publishing, permission changes, deletion, signing, or actions outside the folder.

## 4. Verify capability before onboarding

The agent must:

1. Read `00_START_HERE.md`.
2. Find the native `COS_DATABASE` Sheet.
3. Read `System Check`.
4. Write and read back a harmless test value.
5. Write and read back an Agent Log entry.

If the connector is read-only, the agent stops and explains the exact limitation. No prompt can create connector permissions that the platform does not expose.

## 5. Describe the finances in plain English

The agent asks the user to describe income and expenses in plain English, including amounts, received or due dates, recurrence, and currency when unclear. It does not ask for an arbitrary reporting period before any data exists. Identity is optional.

The agent converts that description into verified `Income`, `Expenses`, and `Recurring Costs` rows, asking only for material missing facts. The user may then provide screenshots, receipts, statements, or exports in `Inbox/Expenses-and-Receipts` as optional supporting evidence. The agent follows `System/FINANCE_WORKFLOW.md` to confirm records, propose a Budget, and generate the first report.

## 6. Expand only after the first report

Projects, Actions, Commitments, Decisions, and weekly Reviews remain available, but they do not delay the initial finance result.
