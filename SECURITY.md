# Security and privacy policy

## Reporting a vulnerability

Do not open a public issue containing an exploit, credential, private document, or personally identifiable information. Use GitHub's private vulnerability reporting feature when available.

## Data boundary

This repository is a template and software distribution layer. A user's live Sheet, Drive folder, profile, credentials, logs, and source documents belong in a separate private instance.

## Secrets

- Never store API keys, OAuth tokens, cookies, passwords, service-account JSON, or private webhook URLs in Git.
- Use the secret store recommended by the selected agent platform.
- Keep `.env` files local and untracked.
- Use least-privilege access to Google resources.

See [docs/privacy.md](docs/privacy.md) for the complete public-repository rule.
