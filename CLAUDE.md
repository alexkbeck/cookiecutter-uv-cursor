# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a modern Cookiecutter template for Python projects that generates projects using uv for dependency management. The template includes extensive configurability with optional features for testing, documentation, containerization, CI/CD, and AI agent support.

## Architecture

The template follows a standard cookiecutter structure with:

- `cookiecutter.json` - Template configuration variables and default values
- `{{cookiecutter.project_name}}/` - Template directory containing project files with Jinja2 templating
- `hooks/` - Pre/post generation scripts that customize the generated project based on configuration
- `tests/` - Template validation tests using pytest-cookies

### Key Components

- **Template Variables**: Extensive configuration options in `cookiecutter.json` for layouts (flat/src), optional features (CI/CD, docs, containerization), and tooling choices
- **Post-Generation Hook**: `hooks/post_gen_project.py` removes unused files/directories based on selected options
- **Generated Project Structure**: Supports both flat and src layouts with modern Python tooling (ruff, mypy, pytest, uv)

## Common Development Commands

### Template Development
```bash
# Install dependencies
make install

# Run quality checks (pre-commit, mypy, deptry)
make check

# Run template tests
make test

# Test template generation locally (flat layout)
make bake

# Test template generation with src layout
make bake-src

# Interactive template generation with custom inputs
make bake-with-inputs

# Build documentation
make docs

# Build and publish to PyPI
make build-and-publish
```

### Testing the Template
```bash
# Run all tests including generated project validation
uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

# Test specific cookiecutter configuration
uv run python -m pytest tests/test_cookiecutter.py -k "test_name"
```

## Template Configuration

The template supports extensive configuration through `cookiecutter.json`. Key configuration categories:

- **Layout**: `flat` vs `src` project structure
- **CI/CD**: GitHub Actions, PyPI publishing, codecov
- **Documentation**: MkDocs with Material theme
- **Containerization**: Docker/Podman support, devcontainers
- **CLI**: Typer framework integration
- **AI Support**: Cursor and Claude Code assistant files
- **Dependencies**: Rich output, Pydantic models/settings, async support
- **Build Tools**: Make vs Just task runners
- **Testing**: pytest-mock integration
- **Licenses**: Multiple open source license options

## Code Quality Standards

- Uses `ruff` for linting and formatting (configured in pyproject.toml)
- Type checking with `mypy`
- Dependency analysis with `deptry` 
- Pre-commit hooks for code quality
- Test coverage tracking with pytest-cov
- Multi-version Python testing with tox-uv (3.9-3.13)

## Template Generation Process

1. User provides configuration via cookiecutter prompts or `--no-input` with defaults
2. Cookiecutter processes template files with Jinja2 templating
3. Post-generation hook (`hooks/post_gen_project.py`) runs to:
   - Remove unused license files based on selection
   - Remove optional feature files/directories not selected
   - Handle layout-specific file organization (src vs flat)
   - Clean up AI assistant files based on agent_support selection

## Generated Project Features

Generated projects include:
- Modern dependency management with uv
- Code quality tools (ruff, mypy, pre-commit)
- Testing with pytest and coverage reporting
- Optional CI/CD with GitHub Actions
- Optional documentation with MkDocs
- Optional containerization support
- Optional CLI framework with Typer
- Optional AI assistant support files

The generated CLAUDE.md file provides comprehensive guidance for AI assistants working with the generated projects, including tool-specific commands and development workflows.