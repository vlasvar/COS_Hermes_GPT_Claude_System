# Hermes profile adapter

A dedicated Hermes profile gives the Chief of Staff an isolated configuration, memory, sessions, skills, and credentials. Keep the live instance outside this public-template repository.

## Create the profile

```bash
hermes profile create chief-of-staff --description "Maintains the private Chief of Staff operating system."
hermes profile show chief-of-staff
```

Activate the profile and start Hermes in the private instance folder:

```bash
hermes profile use chief-of-staff
hermes --in /path/to/private-cos
```

`hermes profile use` changes the sticky default profile. Return to the prior profile afterward when appropriate. Hermes profiles live under the active Hermes home in `profiles/<name>/`; resolve the active location with Hermes commands rather than assuming a fixed path.

## Install the operating context

In the private instance folder:

1. Copy `kernel/SYSTEM.md`, `kernel/CONTEXT.md`, `kernel/PERMISSIONS.md`, and `kernel/WORKFLOWS.md`.
2. Copy `adapters/hermes/HERMES.md` to the instance root as `AGENTS.md`.
3. Copy and complete `templates/profile/USER_PROFILE.md`.
4. Copy `config/system.example.yaml` to `system.yaml` and set private resource identifiers locally.
5. Keep secrets in Hermes's secret environment, never in Markdown or `system.yaml`.

Hermes auto-loads `AGENTS.md` from the working-directory hierarchy. The adapter therefore stays thin and points to the canonical kernel files.

## Recommended default

Begin at permission level 1 (Suggest). Increase autonomy only after the user has reviewed agent logs and explicitly delegated a narrow workflow.
