# ADR 0002: Use finance-first onboarding with Workspace Operator authority

- Status: Accepted
- Date: 2026-08-30

## Context

The first product draft required users to understand agent adapters, multiple Markdown files, YAML configuration, and numeric permission levels. Its default Suggest authority also instructed capable agents not to maintain the Sheet. At the same time, some platform connectors expose read-only Google access, which no instruction can upgrade.

The product needs an onboarding path that produces immediate value, distinguishes policy from actual connector capability, and asks for minimal personal information.

## Decision

Distribute one finance-first starter ZIP containing a ready-made Excel workbook, bootstrap instructions, one copyable prompt, upload folders, evidence storage, reports storage, and an optional Apps Script fallback.

Require the user to upload the extracted folder, convert the workbook to a native Google Sheet, paste the folder link into the supplied prompt, and let the agent discover the remaining instructions.

Make Workspace Operator the default authority. It may maintain files and records inside the configured COS folder without repeated approval. Actions outside the folder and high-impact external actions retain approval gates.

Require a verified Sheet and Agent Log write-and-read-back capability test before onboarding. Stop honestly when the active connector is read-only.

Begin onboarding with currency, evidence period, finance scope, and budget period. Treat identity and biography as optional.

## Consequences

- The beginner experience becomes one folder, one link, and one prompt after the unavoidable native-Sheet conversion.
- Capable agents can maintain internal records without artificial Suggest-mode restrictions.
- Read-only connectors fail early and explicitly instead of producing a misleading onboarding.
- Expense screenshots and budget results demonstrate concrete value before broader Chief of Staff configuration.
- The numeric autonomy levels remain available for advanced instances but disappear from beginner onboarding.
- The public template must validate both source files and generated workbook/ZIP contents.

## Alternatives considered

### Keep Suggest as the default

Rejected because it blocks routine internal maintenance even when the connector and user authorization allow it.

### Ask for a complete personal profile first

Rejected because it collects unnecessary information before delivering value and makes identity appear mandatory.

### Package only a native Google Sheet

Not possible because a native Google Sheet is a cloud object and cannot be stored inside a downloadable ZIP. A ready-made `.xlsx` plus one Google conversion step is the portable alternative.

### Assume every Drive connector can write

Rejected because connector capability varies by platform and plan. The capability test makes the limitation observable.
