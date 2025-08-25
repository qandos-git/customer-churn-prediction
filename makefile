# Variables
PYTHON = uv run python
RUFF = uv run ruff
PRECOMMIT = uv run pre-commit

# Default target
.DEFAULT_GOAL := help


run:
	$(PYTHON) main.py --train artifacts/data/train_data.json --test artifacts/data/test_data.json


# Install all required tools
precode:
	wget -qO- https://astral.sh/uv/install.sh | sh
	uv tool install ruff
	uv tool install pre-commit

# Install dependencies
install:
	uv sync

# Run linter (ruff)
lint:
	$(RUFF) check .

# Format code (black + ruff --fix)
format:
	$(RUFF) format
	$(RUFF) check --fix .

# Run pre-commit hooks
precommit:
	$(PRECOMMIT) run --all-files

# Show available commands
help:
	@echo "make precode     - Install pre-code tools (uv, ruff, pre-commit)"
	@echo "make run         - Run the main application"
	@echo "make install     - Install dependencies with uv"
	@echo "make lint        - Run ruff linter"
	@echo "make format      - Format code"
	@echo "make precommit   - Run pre-commit hooks"
