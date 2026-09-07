# Vane-Truth-AI-Architecture
This framework locks LLMs to a 0.0 temperature and anchors all insights to the VANE_ROOT_STABLE_001 source of truth. We provide 100% transparent evidence trails across Cloud, Networking, Application, and Hardware domains, transforming raw telemetry into high-fidelity "outputs of privilege" for global enterprise clients.
# Vane-Truth-AI-Architecture

A production-ready Rust library (`gauth`) for secure, high-performance OAuth 2.0 and Google Service Account token exchange [3], built to support **Vane-Truth-AI-Architecture** backends and Android client integrations.

## Features
* **User OAuth 2.0**: Generates secure client consent URIs and exchanges authorization codes [3].
* **Service Account JWT Engine**: Custom-signs RSA-256 JWT assertions using `ring` to mint short-lived Google/Firebase access tokens [1, 3].
* **Automated Caching**: Manages localized token caching (`access_token.json`) to minimize latency and bypass rate limits [3].

## Verified Domains & Monetization
This workspace facilitates authorized ad seller verification for your designated Play Store listings [1]:
* **Authorized Domain:** `https://vane-enterprise-llc.netlify.app`
* **Ad Security:** Serves `app-ads.txt` dynamically at the root directory to verify your publisher ID (`pub-5005820095625003`) [1].

## Getting Started
Provide your Google service account credentials file:
`test_fixtures/service-account-key.json`

```rust
let scopes = vec!["https://www.googleapis.com/auth/firebase.messaging"];
let mut sa = ServiceAccount::from_file("test_fixtures/service-account-key.json", scopes);
let bearer_token = sa.access_token().await?;
---
Copyright © 2026 MD ABUL HOSSAIN. All rights reserved.
