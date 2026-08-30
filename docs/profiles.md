# Agent profiles and projects

A private Chief of Staff instance needs a persistent agent workspace. The workspace supplies continuity and tools; it does not replace the operational store.

| Environment | Persistent workspace | Instruction entry point | Canonical state |
|---|---|---|---|
| Hermes | Isolated Hermes profile plus private instance folder | `AGENTS.md` | Google Sheet |
| ChatGPT | Private ChatGPT Project | Project instructions and uploaded knowledge | Google Sheet |
| Claude | Private Claude Project | Project instructions and Project Knowledge | Google Sheet |

## Generate a private instance

Run from the template repository:

```bash
python scripts/create_instance.py /path/to/private-cos --adapter hermes
```

Supported adapter values are `hermes`, `chatgpt`, and `claude`. The target must be outside this repository and must be new or empty.

The generator copies the canonical kernel, blank profile, example configuration, and the selected adapter instructions. It never copies example conversations or creates credentials.

## Hermes profile

Use a dedicated profile to isolate configuration, memory, sessions, skills, and credentials from other Hermes roles.

```bash
hermes profile create chief-of-staff --description "Maintains the private Chief of Staff operating system."
hermes profile show chief-of-staff
hermes profile use chief-of-staff
hermes --in /path/to/private-cos
```

`hermes profile use` changes the sticky default profile. Return to the original profile afterward when appropriate, for example with `hermes profile use default`.

Hermes auto-loads `AGENTS.md` from the working-directory hierarchy. The generator therefore installs the Hermes adapter as `AGENTS.md` in the private instance root.

## ChatGPT Project

Create one private Project per Chief of Staff instance. Paste `PROJECT_INSTRUCTIONS.md` into the Project instructions and upload the generated kernel and private profile files as Project knowledge. Grant Google access only through an approved, least-privilege integration.

## Claude Project

Create one private Project per Chief of Staff instance. Use `CLAUDE.md` as the Project instructions and add the generated kernel and private profile files to Project Knowledge. Use an approved Google connector when available.

## Portability test

A profile is correctly configured when the same fictional inbox items produce equivalent canonical record changes in two supported environments without changing the Sheet schema, record IDs, approval policy, or evidence links.
