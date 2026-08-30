# Privacy and public-repository rule

Treat the repository as public from the first commit, regardless of its current GitHub visibility.

## Allowed

- Generic templates
- Empty schemas
- Fictional examples labeled as fictional
- Public documentation links
- Setup and validation scripts
- Placeholder resource identifiers

## Prohibited

- Real names, addresses, phone numbers, or email addresses
- Personal biography or private preferences
- Account, order, transaction, or government identifiers
- Financial balances, health information, or relationship details
- Private Google Sheet, Drive, document, or conversation links
- API keys, tokens, cookies, credentials, or webhook secrets
- Raw conversation transcripts or screenshots from a private instance
- Completed user profiles or exported live data

## Instance boundary

Create each live instance in a separate private folder or repository. Do not place it under this repository, even if ignored, when avoidable. The strongest protection is not generating sensitive files inside the public-template working tree.

## Examples

Use invented organizations such as “Northwind Studio” and fictional people such as “Jordan Lee.” Do not lightly anonymize a real case; create a genuinely synthetic example.

## Pre-publication review

Before changing repository visibility:

1. Scan the full Git history, not only the current tree.
2. Search for credentials and PII.
3. Review GitHub Actions logs and artifacts.
4. Review issues, pull requests, discussions, and releases.
5. Rotate any secret that ever entered the repository, even if later deleted.
