# Hermes profile adapter

Hermes can operate the finance-first starter when its active tools can read and write the private Google Drive folder and native Google Sheet.

## Beginner path

Use the prompt in `starter-kit/01_COPY_THIS_PROMPT.txt`. Hermes should open the folder, read `00_START_HERE.md`, verify real write capability, and begin finance onboarding.

## Optional isolated profile

```bash
hermes profile create chief-of-staff --description "Operates a private finance-first Chief of Staff workspace."
hermes profile show chief-of-staff
hermes profile use chief-of-staff
```

Configure the profile's Google access through Hermes's supported tools and secret storage. Do not place credentials in the starter folder.

Copy `adapters/hermes/HERMES.md` into a local private instance as `AGENTS.md` only when using a local Hermes workspace instead of the Drive bootstrap.

The default role is Workspace Operator: autonomous internal maintenance, with approval at the folder boundary and for high-impact external actions.
