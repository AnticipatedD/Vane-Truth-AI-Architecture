.PHONY: all build test fmt clippy clean run

# Default target runs formatting, clippy lint checks, and tests
all: fmt clippy test

# Build the project in release mode
build:
	cargo build --release

# Run all tests, ensuring the local test_features directory is resolved
test:
	cargo test -- --nocapture

# Format all source files according to Rust standards
fmt:
	cargo fmt --all -- --check

# Run Clippy static analysis to ensure high code quality
clippy:
	cargo clippy --all-targets --all-features -- -D warnings

# Clean the target directory to reclaim disk space
clean:
	cargo clean

# Run the project locally (if a binary target is configured)
run:
	cargo run
