# Repository instructions for AI agents

## Purpose

Build a generic, user-owned Chief of Staff operating system that works across Hermes, ChatGPT, Claude, and future agent environments.

## Non-negotiable rules

1. Treat every tracked file as public, even while the repository is private.
2. Never add personal names, addresses, email addresses, account identifiers, financial details, private links, credentials, or real conversation excerpts.
3. Use fictional organizations and people only when an example requires them. Label examples as fictional.
4. Keep the kernel model-agnostic. Platform-specific behavior belongs under `adapters/`.
5. Google Sheets is the structured operational store, not a document archive or secret store.
6. The optional dashboard is a replaceable view, never a second source of truth.
7. Default to Workspace Operator authority inside the configured COS folder; preserve approval for external communications, publishing, spending, deletion, access changes, and other actions outside that workspace.
8. Keep onboarding finance-first and identity optional.
9. Rebuild distributable artifacts with `python scripts/build_starter_kit.py` after changing schemas, starter files, or the Apps Script.
10. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v` before declaring work complete.

## Canonical terminology

Use the definitions in `kernel/CONTEXT.md`. Do not invent near-synonyms for core records.
