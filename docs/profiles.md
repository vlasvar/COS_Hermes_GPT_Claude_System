# Agent profiles and projects

The beginner product is one Drive folder plus one bootstrap prompt. Profiles and Projects are optional containers for persistent tools and conversation, not additional databases.

| Environment | Persistent workspace | Bootstrap | Canonical state |
|---|---|---|---|
| Hermes | Isolated Hermes profile | Drive folder link and supplied prompt | `COS_DATABASE` |
| ChatGPT | Private ChatGPT Project | Drive folder link and supplied prompt | `COS_DATABASE` |
| Claude | Private Claude Project | Drive folder link and supplied prompt | `COS_DATABASE` |
| Other agents | Platform-specific workspace | Drive folder link and supplied prompt | `COS_DATABASE` |

## Required capability

The environment must be able to read the starter folder and write to the native Google Sheet for full automation. The bootstrap capability test verifies this before onboarding.

Instructions cannot upgrade a read-only connector. When write access is unavailable, the agent must stop and identify the limitation rather than pretending the database was updated.

## Authority

The default Workspace Operator may maintain files and records inside the COS folder. Spending, external communication, publication, signing, access changes, deletion of evidence, and actions outside the folder require approval.

## Optional Hermes isolation

```bash
hermes profile create chief-of-staff --description "Operates a private finance-first Chief of Staff workspace."
hermes profile use chief-of-staff
```

Keep secrets in the platform's approved secret store, never in the starter folder.

## Portability test

A workspace is portable when two supported agents can process the same fictional evidence into equivalent canonical records without changing IDs, evidence links, statuses, or the approval boundary.
