# Claude Project adapter

A Claude Project can operate the finance-first starter when its active Google connector can read and write the private folder and native Google Sheet.

## Setup

1. Create a private Claude Project.
2. Use `CLAUDE.md` as the Project instructions.
3. Connect Google Drive and Google Sheets through an available connector with the minimum necessary scope.
4. Paste the completed prompt from `starter-kit/01_COPY_THIS_PROMPT.txt`.
5. Require the System Check write-and-read-back test before onboarding.

### Optional tested free-tier workaround

This is not the system's default agent path. If you specifically need the tested Claude + Composio route:

1. Sign in to Claude in a browser.
2. Open Composio and choose **Claude → Install for Claude & Cowork**.
3. Click **Add the Composio Connector in Claude**.
4. Select Next or Continue until connected.
5. Authorize Google Drive and Google Sheets in Composio with the minimum necessary scope.

The starter folder contains the canonical instructions. Project conversation history is not the operational database.

If the connector is read-only, Claude must say so and stop. It may offer proposed rows for manual entry, but it must not claim that the Sheet was updated.
