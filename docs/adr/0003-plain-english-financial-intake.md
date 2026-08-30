# ADR 0003: Start with plain-English financial intake

- Status: Accepted
- Date: 2026-08-30

## Context

The initial onboarding asked for currency, a reporting period, finance scope, and a budget period before any financial records existed. This added conversational turns, consumed limited free-tier context, and asked users to choose a period without data to examine. The workbook also lacked a canonical Income tab even though cash-flow onboarding needs both income and expenses.

## Decision

After the connector capability check, ask one open question requesting a plain-English description of income and expenses, including amounts, received or due dates, recurrence, and currency when unclear.

Infer scope and useful reporting periods from the supplied facts. Ask follow-up questions only for material gaps that prevent correct records. Add Income as a first-class finance tab. Write and read back Income, Expenses, and Recurring Costs rows before offering optional evidence upload.

## Consequences

- A user can begin with a natural statement such as monthly salary and rent dates.
- The Sheet gains a structured Income register.
- Evidence improves confidence but is not required to begin.
- The onboarding uses fewer messages and less context.
- Reports derive their covered period from actual records rather than a premature preference question.
- Ambiguous or unsupported facts remain Provisional instead of being invented.