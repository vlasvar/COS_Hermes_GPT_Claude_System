# Onboarding a private instance

## 1. Create the private boundary

Generate a working folder outside this repository. The folder will contain completed profiles, resource identifiers, and private operating records.

```bash
python scripts/create_instance.py /path/to/private-cos --adapter hermes
```

Use `chatgpt` or `claude` instead of `hermes` when appropriate. The target must be new or empty.

## 2. Provision the operational store

Create a blank Google Sheet and run `templates/google-sheets/Code.gs`, or manually create the tabs from `schema/sheets.json`.

Create a private Drive folder for evidence. Grant only the minimum access needed by the chosen agent environment.

## 3. Confirm the generated kernel

The generator installs these files into the private instance:

- `kernel/SYSTEM.md`
- `kernel/CONTEXT.md`
- `kernel/PERMISSIONS.md`
- `kernel/WORKFLOWS.md`

It also installs the selected agent instruction file under the filename expected by that environment.

## 4. Configure the private instance

Complete the generated:

- `USER_PROFILE.md`
- `system.yaml`

Do not place credentials in either file.

## 5. Choose an agent environment

Follow exactly one primary adapter first:

- `adapters/hermes/README.md`
- `adapters/chatgpt/README.md`
- `adapters/claude/README.md`

See `docs/profiles.md` for a side-by-side explanation of Hermes profiles, ChatGPT Projects, and Claude Projects.

A second adapter can be added later to test portability.

## 6. Calibrate permissions

Start at level 1 (Suggest). Process the fictional demo inputs and inspect the proposed Sheet changes. Move to level 2 only after the classification and logging behavior is reliable.

## 7. Run the acceptance test

The instance is ready when it can:

1. Process five mixed fictional inputs.
2. Classify each input into canonical record types.
3. Assign stable IDs.
4. Produce precise Sheet changes.
5. Stop at approval gates.
6. Record material operations.
7. Produce a weekly review.
8. Repeat the exercise in another agent environment without changing the data model.
