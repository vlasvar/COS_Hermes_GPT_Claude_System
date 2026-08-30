# Hermes adapter — private instance

Load and follow these private-instance files before operational work:

1. `SYSTEM.md`
2. `CONTEXT.md`
3. `PERMISSIONS.md`
4. `WORKFLOWS.md`
5. `USER_PROFILE.md`
6. `system.yaml`

Use the Google Sheet as the structured operational store and the configured Drive folder as the evidence store. Apply the approval gates in `PERMISSIONS.md` and the private overrides in `system.yaml`.

For every material operation:

- Identify the target record.
- Determine the required approval state.
- Execute only within the granted scope.
- Verify external writes.
- Add an Agent Log entry.

Do not copy private instance data back into the public template repository.
