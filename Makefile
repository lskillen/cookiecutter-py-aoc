.PHONY: bake
bake: ## bake without inputs and overwrite if exists.
	@uv run cookiecutter --no-input . --overwrite-if-exists

.PHONY: bake-with-inputs
bake-with-inputs: ## bake with inputs and overwrite if exists.
	@uv run cookiecutter . --overwrite-if-exists

.PHONY: bake-test
bake-test:
	@rm -rf ../cookiecutter-py-aoc-example || true
	@VIRTUAL_ENV= uv run cookiecutter --no-input . --overwrite-if-exists \
		year=2023 \
		author="Lee Skillen" \
		github_author_handle=lskillen \
		project_name=cookiecutter-py-aoc-example \
		project_slug=cookiecutter_py_aoc_example \
		open_source_license="MIT license"
	@mv cookiecutter-py-aoc-example ../
	@cd ../cookiecutter-py-aoc-example && git init -b main
	@cd ../cookiecutter-py-aoc-example && make test


.PHONY: install
install: ## Install the virtual environment
	@echo "🚀 Creating virtual environment"
	@uv sync

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking lock file consistency with 'pyproject.toml'"
	@uv lock --locked
	@echo "🚀 Linting code: Running pre-commit"
	@uv run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@uv run mypy
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@uv run deptry .

.PHONY: test
test: ## Test the code with pytest.
	@echo "🚀 Testing code: Running pytest"
	@uv run python -m pytest tests

.PHONY: build
build: clean-build ## Build wheel file
	@echo "🚀 Creating wheel file"
	@uvx --from build pyproject-build --installer uv

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "🚀 Removing build artifacts"
	@uv run python -c "import shutil; import os; shutil.rmtree('dist') if os.path.exists('dist') else None"

.PHONY: help
help:
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
