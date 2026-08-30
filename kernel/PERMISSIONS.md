# Permission model

A private instance selects a default autonomy level and may override individual capabilities.

| Level | Meaning |
|---|---|
| 0 — Read | Analyze only; make no changes. |
| 1 — Suggest | Propose record changes and draft actions. |
| 2 — Maintain | Update internal operational records; no external action. |
| 3 — Approve | Prepare external actions and execute only after explicit approval. |
| 4 — Delegate | Execute specifically delegated, reversible, low-risk workflows and log the result. |

## Default approval gates

Explicit approval is required for:

- Sending external communications
- Publishing or posting publicly
- Spending, transferring, or committing money
- Deleting records or source documents
- Granting access or changing permissions
- Signing or accepting legal terms
- Disclosing personal or confidential information
- Any action outside the configured delegation scope

Reading and drafting do not imply permission to execute. Access to a tool does not imply authorization to use it for every purpose.
