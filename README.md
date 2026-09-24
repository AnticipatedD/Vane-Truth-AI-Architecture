# Vane-Truth AI Architecture

## Overview
A production-ready Flask and React monorepo architecture engineered for high-throughput data processing, model interface boundaries, and web system orchestration. The application leverages modular blueprint routing structures and implements decoupled error analytics layers to ensure maximum uptime and system performance tracking under runtime environments.

## Architecture Overview
The platform decouples routing frameworks, environmental configurations, and third-party observability components into clean, single-responsibility modules:
* **`webapp/app.py`**: The primary application bootstrap initialization file handling server instance creation and blueprint mapping profiles.
* **`webapp/sentry_config.py`**: Centralized, non-intrusive exception tracking module providing precise 4xx filter gates and transaction sampling strategies.
* **`webapp/application.py`**: Business logic orchestration hub controlling career frameworks and pipeline operations.

## Development

### 1. Installation
Set up your local system and synchronize runtime frameworks using the package manager layers:
```bash
yarn install --frozen-lockfile
pip install -r requirements.txt
```

### 2. Running Local Applications
Spin up the Flask development environment runner locally:
```bash
flask run --port=8002
```

### 3. Automated Test Suite Execution
Run the automated testing engine to assert execution paths pass code style and quality gates:
```bash
# Execute unit tests and verify code coverage gates
pytest --cov=webapp --cov-report=term-missing --cov-fail-under=50
```

## Environment Variables
The application parameters are configured via standard local shell injections. Populate your local `.env` variables using the provided system templates:

| Variable Name | Purpose / Target Domain | Example Configuration |
| :--- | :--- | :--- |
| `APPLICATION_CRYPTO_SECRET_KEY` | Cryptographic signature validation for secure app session states. | `super_secret_crypto_hash` |
| `RECAPTCHA_SITE_KEY` | Security verification client key gating human integration parameters. | `6LeIxAcTAAAAAJcZVR...` |
| `SENTRY_DSN` | Telemetry capture network link tracing operational execution flags. | `https://sentry.io` |
| `FLASK_ENV` | Sets runtime profile execution constraints across active layers. | `development` |

## License
This architecture framework code used to format and display system modules is licensed under the [LGPLv3](https://opensource.org/license/lgpl-3-0/) license definitions.
