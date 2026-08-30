# Architecture

## Design goal

Keep the system portable across agent platforms while retaining one operational truth and a human-auditable workflow.

## Layers

```text
┌──────────────────────────────────────────────┐
│ Experience: chat or optional dashboard       │
├──────────────────────────────────────────────┤
│ Agent adapters: Hermes / ChatGPT / Claude    │
├──────────────────────────────────────────────┤
│ Kernel: vocabulary / rules / workflows       │
├──────────────────────────────────────────────┤
│ User stores: Sheets / Drive / Markdown       │
└──────────────────────────────────────────────┘
```

## Seams

### Operational-store seam

The kernel requires tabular records matching `schema/sheets.json`. Google Sheets is the first adapter because it is inspectable and accessible to nontechnical users. A future database adapter must preserve stable IDs, links, timestamps, and auditability.

### Agent seam

Each agent adapter explains how its platform loads the same canonical files and reaches the operational store. Adapters must not redefine record meanings or permissions.

### Experience seam

Chat and dashboards are replaceable views. Neither may become an independent task list, approval queue, or audit log.

## Source-of-truth map

| Information | Canonical location |
|---|---|
| Current operational state | Google Sheet |
| Source documents and evidence | Google Drive |
| Policies and workflows | Kernel Markdown files |
| Private preferences and delegation | Private profile and configuration |
| Material agent operations | Agent Log tab |
| Dashboard display state | Non-canonical cache only |

## Portability test

The architecture passes if a user can switch from one supported agent to another while retaining their Sheet, Drive evidence, policies, stable IDs, approvals, and review history.
