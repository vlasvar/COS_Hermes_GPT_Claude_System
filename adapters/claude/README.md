# Claude Project adapter

A Claude Project can hold the canonical kernel and private instance profile as Project Knowledge while the Google Sheet remains the operational store.

## Setup

1. Create a new private Claude Project.
2. Add `CLAUDE.md` as the Project instructions, or paste its contents into the instruction field available in the selected Claude environment.
3. Add the canonical kernel files to Project Knowledge:
   - `kernel/SYSTEM.md`
   - `kernel/CONTEXT.md`
   - `kernel/PERMISSIONS.md`
   - `kernel/WORKFLOWS.md`
4. Add the privately completed `USER_PROFILE.md` and `system.yaml` only after reviewing the Project's data controls.
5. Use an approved connector or tool for Google Sheets. If no verified write path exists, return a proposed change set rather than claiming completion.
6. Test with `examples/demo-inputs.md`.

## Continuity rule

Claude's Project context helps the model understand the system, but live operational state belongs in the Sheet and source evidence belongs in Drive.
