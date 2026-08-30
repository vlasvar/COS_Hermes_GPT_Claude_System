# Fictional acceptance-test inputs

All people and organizations below are fictional.

1. “Jordan Lee from Northwind Studio asked for the revised proposal by next Tuesday.”
2. “The workspace migration should be complete when all active files are searchable in the new system.”
3. “We decided to use the standard support plan because the premium tier is not justified until usage doubles.”
4. “Remind the operations team to review the draft, but do not send anything without approval.”
5. “The supplier document says delivery is expected on 15 October, but the project tracker currently says 12 October.”

## Expected behavior

The agent should:

- Create or propose an Inbox record for each input.
- Classify records as a Commitment, Project, Decision, draft communication Action, and unresolved conflict respectively.
- Create stable generic IDs.
- Preserve the date conflict instead of silently selecting one date.
- Stop before sending the message.
- Link evidence when a source document is available.
- Add Agent Log entries for material changes.
