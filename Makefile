.PHONY: all build test fmt clippy clean run test_setup

# Default target runs environment checks, formatting, linting, and tests
all: test_setup fmt clippy test

# Build the project in release mode
build:
	cargo build --release

# Ensure the local test_features directory exists before executing tests
test_setup:
	@mkdir -p test_features
	@if [ ! -f test_features/service-account-key.json ]; then \
		echo "⚠️  WARNING: test_features/service-account-key.json is missing!"; \
		echo "   Please add your credential template to complete integration tests."; \
	fi

# Run all tests, automatically building the test environment first
test: test_setup
	cargo test -- --nocapture

# Format all source files according to Rust standards
fmt:
	cargo fmt --all -- --check

# Run Clippy static analysis to ensure high code quality
clippy:
	cargo clippy --all-targets --all-features -- -D warnings

# Clean the target directory
clean:
	cargo clean

# Run the project locally
run:
	cargo run
