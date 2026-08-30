# ADR 0001: Separate the public template from private instances

- Status: Accepted
- Date: 2026-08-30

## Context

The system needs reusable schemas, instructions, workflows, and setup automation, while each installation contains private profiles, resource identifiers, evidence, operational records, and potentially credentials. Keeping both in one repository would make accidental disclosure likely and would couple product development to one installation.

## Decision

Maintain this repository as a public-ready template from its first commit, regardless of its current GitHub visibility. Store every live installation in a separate private folder or repository. Use fictional, explicitly labeled examples in the template. Never use a lightly anonymized private case as example data.

## Consequences

- The template can be published without extracting a private user's history.
- Automated checks can reject common secrets, private Google links, and email addresses.
- Installation requires copying canonical files into a separate working location.
- Improvements discovered in a private instance must be generalized before being contributed back.
- The public repository cannot serve as the live operational store.

## Alternatives considered

### Keep private data in an ignored subdirectory

Rejected because ignored files can still be force-added, exposed by tools, or captured in artifacts.

### Keep the repository permanently private

Rejected because visibility is not a reliable privacy boundary and would prevent safe open distribution later.
