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

## 5. Complete minimal finance onboarding

The agent asks one question at a time for primary currency, initial evidence period, finance scope, and budget period. Identity is optional.

The user then uploads screenshots, receipts, statements, or exports to `Inbox/Expenses-and-Receipts`. The agent follows `System/FINANCE_WORKFLOW.md` to create provisional Expenses, identify Recurring Costs, propose a Budget, and generate the first report.

## 6. Expand only after the first report

Projects, Actions, Commitments, Decisions, and weekly Reviews remain available, but they do not delay the initial finance result.
