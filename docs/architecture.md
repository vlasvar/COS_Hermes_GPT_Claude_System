# Architecture

## Design goal

Keep the system portable across agent platforms while retaining one operational truth and a human-auditable workflow.

## Layers

```text
┌──────────────────────────────────────────────┐
│ Experience: one folder link / optional UI     │
├──────────────────────────────────────────────┤
│ Agent adapters: Hermes / GPT / Claude / other│
├──────────────────────────────────────────────┤
│ Kernel: vocabulary / rules / workflows       │
├──────────────────────────────────────────────┤
│ User stores: Sheets / Drive / Markdown       │
└──────────────────────────────────────────────┘
```

## Seams

### Operational-store seam

The kernel requires tabular records matching `schema/sheets.json`. Google Sheets is the first adapter because it is inspectable and accessible to nontechnical users. A future database adapter must preserve stable IDs, links, timestamps, and auditability.

Finance-first tabs lead the schema so onboarding can produce immediate value. Broader Chief of Staff records remain available without delaying the initial expense and budget baseline.

### Agent seam

Each agent adapter explains how its platform loads the same canonical files and reaches the operational store. Adapters must not redefine record meanings or permissions.

Every adapter must pass the same capability check: read the Sheet, write a harmless value, read it back, write an Agent Log entry, and read that back. The interface cannot manufacture write access when a platform connector is read-only.

### Experience seam

Chat and dashboards are replaceable views. Neither may become an independent task list, approval queue, or audit log.

## Source-of-truth map

| Information | Canonical location |
|---|---|
| Current operational state | Google Sheet |
| Source documents and evidence | Google Drive |
| Policies and workflows | Kernel Markdown files |
| Optional preferences and delegation | Private profile and configuration |
| Material agent operations | Agent Log tab |
| Dashboard display state | Non-canonical cache only |

## Portability test

The architecture passes if a user can switch from one write-capable agent to another while retaining their Sheet, Drive evidence, policies, stable IDs, Workspace Operator authority, and review history.
