# Makefile for Tic Tac Toe Game

# Define your Python interpreter
PYTHON = python3

# Directory structure
SRC_DIR = .
TESTS_DIR = .

# Test runner
TEST_RUNNER = $(PYTHON) -m unittest discover -s $(TESTS_DIR) -p 'test_*.py'

.PHONY: test

test:
	@echo "Running tests..."
	$(TEST_RUNNER)


help:
	@echo "Available targets:"
	@echo "  test   - Run unit tests"
	@echo "  clean
