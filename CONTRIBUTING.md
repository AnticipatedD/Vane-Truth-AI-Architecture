# Contributing to Vane-Truth-AI-Architecture

We welcome contributions to help scale this high-fidelity framework! Because we anchor all insights to deterministic sources of truth (such as `VANE_ROOT_STABLE_001`), we enforce strict development guidelines to maintain 100% transparent evidence trails across all layers.

## Rules of Engagement

1. **Strict Determinism**: Code must avoid non-deterministic behavior. All cryptographic token generation, mock tests, and state machines must be strictly reproducible.
2. **Rust Coding Standards**: Follow idiomatic Rust patterns. Always format your code using `cargo fmt` and run `cargo clippy` to check for safety and performance warnings before committing.
3. **No-Cost Resource Optimization**: Ensure memory allocations and network calls are highly optimized to minimize execution latency. This keeps container instances running smoothly within no-cost limits in cloud execution environments like Cloud Run.

## How to Contribute

* **Report Issues**: Open an issue detailing the exact telemetry logs, steps to reproduce, and the expected evidence trail.
* **Pull Requests**: 
  1. Fork the repository and create your feature branch.
  2. Add unit or integration tests in `test_fixtures` to verify your implementation.
  3. Open a PR with a detailed description of the architectural changes.

## Developer Code of Conduct
Please be respectful, professional, and collaborative in all communication and code reviews.
