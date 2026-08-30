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
7. Preserve human approval for external communications, publishing, spending, deletion, and other high-impact actions unless a private instance explicitly changes its policy.
8. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v` before declaring work complete.

## Canonical terminology

Use the definitions in `kernel/CONTEXT.md`. Do not invent near-synonyms for core records.
