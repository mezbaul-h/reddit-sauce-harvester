.PHONY: test

check: ## Check source code issues.
	black --diff --check .
	isort --diff --check .
	bandit --recursive . --configfile pyproject.toml
	find . -iname "*.py" -not -path "./venv/*" -not -path "./build/*" | xargs pylint

fmt: ## Format code.
	black .
	isort --atomic .

test: ## Run tests.
	coverage run --module pytest
	coverage html
	coverage xml

help: ## Show this help.
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} { \
		if (/^[a-zA-Z_-]+:.*?##.*$$/) {printf "    %-20s%s\n", $$1, $$2} \
		else if (/^## .*$$/) {printf "  %s\n", substr($$1,4)} \
		}' $(MAKEFILE_LIST)
