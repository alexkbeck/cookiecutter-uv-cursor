# {{cookiecutter.project_name}} - Claude Code Assistant Instructions

## Project Overview

This is a Python project using modern tooling and best practices. The project is configured for development with Claude Code assistant support.

## Project Structure

{% if cookiecutter.layout == "src" -%}
- `src/{{cookiecutter.project_slug}}/` - Main package source code (src layout)
{%- else -%}
- `{{cookiecutter.project_slug}}/` - Main package source code (flat layout)
{%- endif %}
- `tests/` - Test files
- `pyproject.toml` - Project configuration, dependencies, and tool settings
{% if cookiecutter.build_tool == "make" -%}
- `Makefile` - Common development commands
{%- else -%}
- `justfile` - Common development commands (using Just task runner)
{%- endif %}
- `README.md` - Project documentation

## Development Environment

### Tools Used
- **UV**: Modern Python package manager for dependencies and virtual environments
- **Ruff**: Fast Python linter and code formatter
- **MyPy**: Static type checking
- **Pytest**: Testing framework
{% if cookiecutter.deptry == 'y' -%}
- **Deptry**: Dependency usage analysis
{%- endif %}
{% if cookiecutter.codecov == 'y' -%}
- **Coverage**: Test coverage reporting
{%- endif %}
{% if cookiecutter.include_github_actions == 'y' -%}
- **GitHub Actions**: CI/CD pipeline
{%- endif %}
{% if cookiecutter.mkdocs == 'y' -%}
- **MkDocs**: Documentation generation
{%- endif %}
{% if cookiecutter.dockerfile == 'y' -%}
- **Docker**: Containerization support
{%- endif %}
{% if cookiecutter.devcontainer == 'y' -%}
- **DevContainer**: VS Code development container support
{%- endif %}

### Key Dependencies
{% if cookiecutter.typer_cli == 'y' -%}
- **Typer**: CLI framework for building command-line interfaces
{%- endif %}
{% if cookiecutter.logging == 'y' -%}
- **Loguru**: Modern logging library
{%- endif %}
{% if cookiecutter.rich_output == 'y' -%}
- **Rich**: Beautiful terminal output with colors and formatting
{%- endif %}
{% if cookiecutter.pydantic_models == 'y' -%}
- **Pydantic**: Data validation and settings management using Python type hints
{%- endif %}
{% if cookiecutter.pydantic_settings == 'y' -%}
- **Pydantic Settings**: Configuration management with environment variable support
{%- endif %}

## Common Development Commands

```bash
# Setup environment and install dependencies
{% if cookiecutter.build_tool == "make" -%}
make install
{%- else -%}
just install
{%- endif %}

# Run all quality checks
{% if cookiecutter.build_tool == "make" -%}
make check
{%- else -%}
just check
{%- endif %}

# Run tests
{% if cookiecutter.build_tool == "make" -%}
make test
{%- else -%}
just test
{%- endif %}

# Run tests with coverage
{% if cookiecutter.build_tool == "make" -%}
make test-cov
{%- else -%}
just test-cov
{%- endif %}

# Format code
{% if cookiecutter.build_tool == "make" -%}
make format
{%- else -%}
just format
{%- endif %}

# Build package
{% if cookiecutter.build_tool == "make" -%}
make build
{%- else -%}
just build
{%- endif %}

{% if cookiecutter.publish_to_pypi == 'y' -%}
# Publish to PyPI
{% if cookiecutter.build_tool == "make" -%}
make publish
{%- else -%}
just publish
{%- endif %}
{%- endif %}

{% if cookiecutter.mkdocs == 'y' -%}
# Serve documentation locally
{% if cookiecutter.build_tool == "make" -%}
make docs
{%- else -%}
just docs
{%- endif %}
{%- endif %}
```

## Code Quality Standards

- **Python versions**: Supports 3.9-3.13
- **Type hints**: Use type annotations for all functions and methods
- **Docstrings**: Use Google-style docstrings for all public functions
- **Testing**: Aim for >80% test coverage
- **Linting**: Code must pass Ruff checks
- **Formatting**: Use Ruff for code formatting

## Testing Guidelines

{% if cookiecutter.mocks == 'y' -%}
- Use pytest-mock for mocking external dependencies
{%- else -%}
- Use unittest.mock for mocking external dependencies
{%- endif %}
- Follow Arrange-Act-Assert pattern for test organization
- Use descriptive test names that explain what is being tested
- Keep tests independent and isolated
- Test both happy path and error conditions

{% if cookiecutter.async_support == 'y' -%}
## Async Support
- Use `pytest-asyncio` for async test support
- Mark async tests with `@pytest.mark.asyncio`
- Use `await` for async function calls
{%- endif %}

{% if cookiecutter.pydantic_models == 'y' -%}
## Pydantic Models
- Use Pydantic models for data validation and serialization
- Include proper type hints and validation constraints
- Test model validation with both valid and invalid data
- Use descriptive field descriptions
{%- endif %}

{% if cookiecutter.pydantic_settings == 'y' -%}
## Configuration Management
- Use Pydantic Settings for configuration management
- Support environment variable configuration
- Include proper validation and defaults
- Document all configuration options
{%- endif %}

{% if cookiecutter.rich_output == 'y' -%}
## Rich Output
- Use Rich for enhanced terminal output
- Include colors and formatting for better UX
- Mock Rich components in unit tests
{%- endif %}

{% if cookiecutter.logging == 'y' -%}
## Logging
- Use Loguru for structured logging
- Include appropriate log levels (DEBUG, INFO, WARNING, ERROR)
- Use context managers for structured logging
- Test log output when relevant
{%- endif %}

## Development Workflow

{% if cookiecutter.build_tool == "make" -%}
1. **Setup**: Run `make install` to set up the development environment
{%- else -%}
1. **Setup**: Run `just install` to set up the development environment
{%- endif %}
2. **Code**: Write code following the project conventions
{% if cookiecutter.build_tool == "make" -%}
3. **Test**: Run `make test` to ensure tests pass
4. **Quality**: Run `make check` to validate code quality
5. **Format**: Run `make format` to format code consistently
{%- else -%}
3. **Test**: Run `just test` to ensure tests pass
4. **Quality**: Run `just check` to validate code quality
5. **Format**: Run `just format` to format code consistently
{%- endif %}
6. **Commit**: Use conventional commit messages
7. **CI/CD**: Let automated checks validate the changes

## File Organization

- Place new modules in the appropriate package directory
- Create corresponding test files in the `tests/` directory
- Update `pyproject.toml` when adding new dependencies
- Update documentation when adding new features

## Adding Dependencies

```bash
# Add runtime dependency
uv add package-name

# Add development dependency
uv add --group dev package-name

# Sync environment after changes
uv sync
```

## Release Process

{% if cookiecutter.publish_to_pypi == 'y' -%}
1. Update version in `pyproject.toml`
{% if cookiecutter.build_tool == "make" -%}
2. Run `make build-and-publish` (requires PyPI token)
{%- else -%}
2. Run `just build-and-publish` (requires PyPI token)
{%- endif %}
3. Create GitHub release with tag matching version
{% if cookiecutter.include_github_actions == 'y' -%}
4. GitHub Actions will automatically build and publish
{%- endif %}
{%- else -%}
1. Update version in `pyproject.toml`
{% if cookiecutter.build_tool == "make" -%}
2. Run `make build` to create wheel
{%- else -%}
2. Run `just build` to create wheel
{%- endif %}
3. Create GitHub release with tag matching version
{%- endif %}

## Code Assistant Guidelines

When helping with this project:
- Follow the established patterns and conventions
- Ensure all code includes proper type hints
- Write comprehensive tests for new functionality
- Update documentation when adding new features
- Run quality checks before suggesting changes
- Consider the existing architecture and dependencies
- Use the project's established tools and workflows 