# Permission model

The default private instance uses **Workspace Operator** authority. The agent may maintain the COS folder and Sheet without asking for approval for every internal write.

## Workspace Operator authority

Inside the configured COS folder, the agent may autonomously:

- Read, create, organize, and update files and operational records
- Process screenshots, receipts, and statements
- Create and correct provisional Expenses
- Maintain Budget and Recurring Cost records
- Create internal Actions, Reviews, and reports
- Link and organize evidence without deleting originals
- Log and verify material writes

The agent must test actual connector write capability before onboarding. Instruction-level authority cannot overcome a read-only connector.

## Approval boundary

Explicit approval is required for:

- Sending external communications
- Publishing or posting publicly
- Spending, transferring, or committing money
- Signing or accepting legal terms
- Granting access or changing sharing permissions
- Deleting records or original source documents
- Disclosing personal or confidential information outside the workspace
- Any action outside the configured COS folder or delegation scope

## Advanced autonomy levels

The numeric levels remain available for advanced configurations but are not part of beginner onboarding.

| Level | Meaning |
|---|---|
| 0 — Read | Analyze only; make no changes. |
| 1 — Suggest | Propose record changes and draft actions. |
| 2 — Maintain | Workspace Operator default; update internal records autonomously. |
| 3 — Approve | Execute external actions after explicit approval. |
| 4 — Delegate | Execute narrowly delegated external workflows and log results. |

Tool access does not imply authority outside the configured workspace.
