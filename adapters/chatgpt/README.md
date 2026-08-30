# ChatGPT Project adapter

A ChatGPT Project can operate the finance-first starter when its active Google connector can read and write the private folder and native Google Sheet.

## Setup

1. Create a private ChatGPT Project.
2. Use `PROJECT_INSTRUCTIONS.md` as the Project instructions.
3. Connect Google Drive with the minimum necessary scope.
4. Paste the completed prompt from `starter-kit/01_COPY_THIS_PROMPT.txt`.
5. Require the System Check write-and-read-back test before onboarding.

The starter folder contains the canonical instructions. A Project chat is not the operational database.

If the connector is read-only, ChatGPT must say so and stop. It may offer proposed rows for manual entry, but it must not claim that the Sheet was updated.
