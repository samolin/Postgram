.PHONY: autoflake_format
autoflake_format: ## Format project with autoflake
	@poetry run autoflake ./CoreRoot ./core


.PHONY: isort_format
isort_format: ## Format project with isort
	@poetry run isort ./CoreRoot ./core


.PHONY: black_format
black_format: ## Format project with black
	@poetry run black ./CoreRoot ./core


format: autoflake_format isort_format black_format ## Alias to run all formats


.PHONY: autoflake_lint
autoflake_lint: ## Check project with autoflake
	@poetry run autoflake --quiet --check ./CoreRoot ./core


.PHONY: isort_lint
isort_lint: ## Check project with isort
	@poetry run isort --check-only ./CoreRoot ./core


.PHONY: black_lint
black_lint: ## Check project with black
	@poetry run black --check ./CoreRoot ./core


lint: autoflake_lint isort_lint black_lint pyright_lint flake8_lint ## Alias to run all lints