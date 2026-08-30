# ChatGPT Project adapter

A ChatGPT Project can act as the persistent workspace for one private Chief of Staff instance. Project instructions and uploaded knowledge provide continuity; the Google Sheet remains the operational store.

## Setup

1. Create a new private ChatGPT Project.
2. Use `PROJECT_INSTRUCTIONS.md` as the Project instructions.
3. Add the canonical kernel files as Project knowledge:
   - `kernel/SYSTEM.md`
   - `kernel/CONTEXT.md`
   - `kernel/PERMISSIONS.md`
   - `kernel/WORKFLOWS.md`
4. Add a privately completed `USER_PROFILE.md` and `system.yaml` to the Project, subject to the user's data policy.
5. Connect Google Drive or provide Sheet access only through an approved integration with the minimum necessary scope.
6. Test with `examples/demo-inputs.md` before adding private data.

## Limitations

A Project's conversation history is not the operational database. Material status changes must be written to the Sheet and logged. If the environment cannot write or verify the Sheet, the agent should return a proposed change set for the user to apply.
