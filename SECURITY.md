# Security Policy

Security is of utmost priority for **Vane-Truth-AI-Architecture** as it handles sensitive Google Service Account keys, automated API credentials, and high-fidelity enterprise data [1, 3].

## Supported Versions

We only support security updates for the latest stable release of this workspace.

| Version | Supported |
| --- | --- |
| 0.7.x (Current) | :white_check_mark: |
| < 0.7.0 | :x: |

## Reporting a Vulnerability

If you discover any security vulnerability, please **do not** open a public issue on GitHub. Instead, report it privately to ensure responsible disclosure:

1. Email a detailed report of the vulnerability directly to the developer: [mdabul@cc.cc](mailto:mdabul@cc.cc).
2. Include a proof-of-concept (PoC), step-by-step reproduction instructions, or raw telemetry showcasing the vulnerability.
3. You can verify the developer's official credentials on Google Developers: [g.dev/hmda](https://g.dev/hmda).
4. We will acknowledge your report within 48 hours and coordinate a secure patch release.

## Secure Best Practices

* **Do Not Commit Secrets**: Never commit `service-account-key.json` or `access_token.json` files to public repositories [1]. Ensure they are always matched by your `.gitignore` configuration [1].
* **Environment Variables**: For production environments, inject your service account credentials securely via secret management tools rather than storing them directly in your codebase.
