# Chief of Staff System

A user-owned, model-agnostic operating system for working with an AI Chief of Staff.

The system combines:

- **Google Sheets** for structured operational state
- **Google Drive** for source documents and evidence
- **Markdown** for policies, context, workflows, and reviews
- **Agent adapters** for Hermes, ChatGPT Projects, and Claude Projects
- An optional, separate **GPT Sites dashboard concept** as a replaceable presentation layer

> This repository contains only generic templates, schemas, instructions, and fictional examples. Never commit a real user's data, credentials, private documents, sheet exports, or conversation history.

## What this is

This is not a prompt collection. It is a small operating kernel with a consistent data model, permission rules, workflow, and audit trail. The AI model can change without forcing the user to rebuild the system.

```text
Experience       Chat / optional dashboard
Agent adapter    Hermes | ChatGPT Project | Claude Project
Kernel           Context | policy | permissions | workflows
User-owned data  Google Sheets | Drive | Markdown
```

## Core operating loop

```text
Capture → Interpret → Classify → Propose → Approve → Execute → Record → Review
```

## Quick start

1. Read [Privacy and public-repository rules](docs/privacy.md).
2. Generate a private workspace outside this repository:

   ```bash
   python scripts/create_instance.py /path/to/private-cos --adapter hermes
   ```

   Replace `hermes` with `chatgpt` or `claude` when appropriate.
3. Create the Google Sheet with [`templates/google-sheets/Code.gs`](templates/google-sheets/Code.gs), or reproduce the schema in [`schema/sheets.json`](schema/sheets.json).
4. Complete `USER_PROFILE.md` and `system.yaml` in the generated private workspace.
5. Configure the selected agent environment using [Agent profiles and projects](docs/profiles.md):
   - [Hermes profile](adapters/hermes/README.md)
   - [ChatGPT Project](adapters/chatgpt/README.md)
   - [Claude Project](adapters/claude/README.md)
6. Process the fictional inputs in [`examples/demo-inputs.md`](examples/demo-inputs.md).
7. Run the first review using [`templates/reviews/WEEKLY_REVIEW.md`](templates/reviews/WEEKLY_REVIEW.md).

Full instructions: [Onboarding](docs/onboarding.md).

## Repository map

```text
kernel/       Canonical terminology, rules, permissions, and workflows
schema/       Machine-readable data contracts
adapters/     Thin setup layers for each supported agent environment
templates/    Google Sheets, private profile, and review templates
docs/         Architecture, privacy, onboarding, and dashboard concept
examples/     Fictional test inputs only
scripts/      Private-instance generation and repository validation
```

## Core vs optional

The mandatory core is deliberately small: Inbox, Projects, Actions, Commitments, Decisions, Contacts, Reviews, and Agent Log. Finance, CRM, content, health, and household workflows should be optional modules rather than additions to the kernel.

## Validate the repository

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

## Status

Early private build. The repository is being developed as if it were already public: generic examples only, no personal case study, and no private instance data.

## License

[MIT](LICENSE)
