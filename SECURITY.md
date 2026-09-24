# Security Policy & Threat Model

## Supported Versions
Only the latest release branches actively maintained in production receive critical security patches.

| Version | Supported |
| :--- | :--- |
| v1.1.x |  Yes |
| < v1.0.0 | ❌ No |

## Reporting Vulnerabilities
If you discover a security vulnerability within this repository, please do not open a public issue. Instead, report it securely by emailing the core security team at **security@canonical.com**. All reported items will receive an initial response within 48 hours, followed by a coordinated disclosure timeline.

## Threat Model & Trust Boundaries
* **Environment Variables**: Sensitive operational keys, database credentials, and cryptographic tokens (such as `APPLICATION_CRYPTO_SECRET_KEY` and `RECAPTCHA_SECRET_KEY`) must always be injected dynamically via runtime environment variables or secure orchestration secret managers. They must never be hardcoded or checked into repository source tracks.
* **API Entry Gateways & Route Gating**: Input data elements entering via Flask routes must go through rigorous validation layouts using Pydantic or schema libraries before processing to insulate internal services from remote exploit payloads.
* **Data Layer Protection**: Database transaction states utilize object-relational mapping parameter bindings to prevent standard SQL injection risks across the application.
