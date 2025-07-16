# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation** <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

## Features

This project includes the following modern Python development features:

{% if cookiecutter.logging == 'y' -%}
- **🚀 Enhanced Logging**: Modern logging with [Loguru](https://loguru.readthedocs.io/) for better debugging and monitoring
{%- endif %}
{% if cookiecutter.rich_output == 'y' -%}
- **🎨 Rich Terminal Output**: Beautiful console output with colors and formatting using [Rich](https://rich.readthedocs.io/)
{%- endif %}
{% if cookiecutter.pydantic_models == 'y' -%}
- **📋 Pydantic Models**: Type-safe data structures with validation using [Pydantic](https://docs.pydantic.dev/)
{%- endif %}
{% if cookiecutter.pydantic_settings == 'y' -%}
- **⚙️ Configuration Management**: Environment-based configuration with [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
{%- endif %}
{% if cookiecutter.async_support == 'y' -%}
- **⚡ Async Support**: Modern async/await patterns with proper testing support
{%- endif %}
{% if cookiecutter.mocks == 'y' -%}
- **🧪 Advanced Testing**: Comprehensive testing with mocking support using [pytest-mock](https://pytest-mock.readthedocs.io/)
{%- endif %}
{% if cookiecutter.typer_cli == 'y' -%}
- **📟 CLI Interface**: Command-line interface built with [Typer](https://typer.tiangolo.com/)
{%- endif %}
{% if cookiecutter.build_tool == 'just' -%}
- **🔧 Modern Task Runner**: Intuitive command syntax with [Just](https://just.systems/) instead of Make
{%- endif %}
{% if cookiecutter.agent_support != 'none' -%}
- **🤖 AI Coding Support**: {% if cookiecutter.agent_support == 'cursor' %}Enhanced development with Cursor IDE integration{% elif cookiecutter.agent_support == 'claude-code' %}AI assistance with Claude Code CLI integration{% else %}Full AI support for both Cursor IDE and Claude Code CLI{% endif %}
{%- endif %}

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
{% if cookiecutter.build_tool == "make" -%}
make install
{%- else -%}
just install
{%- endif %}
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

{% if cookiecutter.typer_cli == 'y' -%}
## CLI Usage

This project includes a command-line interface built with Typer. After installation, you can use the CLI:

```bash
# Run the hello command
{{cookiecutter.project_slug}} hello

# Run with a custom name
{{cookiecutter.project_slug}} hello --name Alice
```

For more information about available commands, run:

```bash
{{cookiecutter.project_slug}} --help
```
{%- endif %}

## Development

### Available Commands

{% if cookiecutter.build_tool == "make" -%}
This project uses Make for task automation. Common commands:
{%- else -%}
This project uses [Just](https://just.systems/) for task automation. Common commands:
{%- endif %}

```bash
# Install dependencies and setup environment
{% if cookiecutter.build_tool == "make" -%}
make install
{%- else -%}
just install
{%- endif %}

# Run all quality checks (linting, type checking, etc.)
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
```

{% if cookiecutter.build_tool == "just" -%}
To see all available commands, run:

```bash
just
```
{%- else -%}
To see all available commands, run:

```bash
make help
```
{%- endif %}

{% if cookiecutter.pydantic_settings == 'y' -%}
### Configuration

This project uses Pydantic Settings for configuration management. You can configure the application using:

1. **Environment variables** (recommended for production):
   ```bash
   export APP_NAME="My Application"
   export DEBUG=true
   export LOG_LEVEL=DEBUG
   ```

2. **`.env` file** (recommended for development):
   ```bash
   # Create a .env file in the project root
   APP_NAME=My Application
   DEBUG=true
   LOG_LEVEL=DEBUG
   ```

3. **Programmatically** in your code:
   ```python
   {% if cookiecutter.layout == "src" -%}
   from src.{{cookiecutter.project_slug}}.config import settings
   {%- else -%}
   from {{cookiecutter.project_slug}}.config import settings
   {%- endif %}
   
   print(settings.app_name)
   print(settings.debug)
   ```

All configuration options are type-safe and validated automatically.
{%- endif %}

{% if cookiecutter.logging == 'y' -%}
### Logging

This project uses [Loguru](https://loguru.readthedocs.io/) for enhanced logging:

```python
{% if cookiecutter.layout == "src" -%}
from src.{{cookiecutter.project_slug}}.foo import foo
{%- else -%}
from {{cookiecutter.project_slug}}.foo import foo
{%- endif %}

# Logging is automatically configured and used within functions
result = foo("example")  # This will log processing information
```

Loguru provides structured logging with automatic JSON serialization, filtering, and formatting.
{%- endif %}

{% if cookiecutter.async_support == 'y' -%}
### Async Support

This project includes support for asynchronous programming:

```python
import asyncio
{% if cookiecutter.layout == "src" -%}
from src.{{cookiecutter.project_slug}}.foo import async_foo
{%- else -%}
from {{cookiecutter.project_slug}}.foo import async_foo
{%- endif %}

# Use async functions
async def main():
    result = await async_foo("example")
    print(result)

# Run async code
asyncio.run(main())
```

The project includes `pytest-asyncio` for testing async code.
{%- endif %}

{% if cookiecutter.pydantic_models == 'y' -%}
### Data Models

This project uses [Pydantic](https://docs.pydantic.dev/) for type-safe data validation:

```python
{% if cookiecutter.layout == "src" -%}
from src.{{cookiecutter.project_slug}}.models import FooModel
{%- else -%}
from {{cookiecutter.project_slug}}.models import FooModel
{%- endif %}

# Create and validate data
model = FooModel(bar="example")
print(model.bar)  # Automatically validated
print(str(model))  # Clean string representation
```

All models include automatic validation, serialization, and clear error messages.
{%- endif %}

{% if cookiecutter.mocks == 'y' -%}
### Testing with Mocks

This project includes [pytest-mock](https://pytest-mock.readthedocs.io/) for advanced testing:

```python
def test_with_mocking(mocker):
    # Mock external dependencies
    mock_function = mocker.patch("module.function")
    mock_function.return_value = "mocked_result"
    
    # Your test code here
    # Verify mock was called
    mock_function.assert_called_once()
```

See the test files for comprehensive mocking examples.
{%- endif %}

{% if cookiecutter.agent_support != 'none' -%}
### AI Coding Assistant

{% if cookiecutter.agent_support == 'cursor' -%}
This project is configured for enhanced development with **Cursor IDE**:

- Comprehensive coding rules in `.cursor/rules/`
- Context-aware suggestions for this project's patterns
- Testing guidelines and best practices
{%- elif cookiecutter.agent_support == 'claude-code' -%}
This project is configured for AI assistance with **Claude Code CLI**:

- Detailed project instructions in `CLAUDE.md`
- Development workflow guidance
- Code quality standards and patterns
{%- else -%}
This project is configured for AI assistance with both **Cursor IDE** and **Claude Code CLI**:

- Cursor IDE support with comprehensive rules in `.cursor/rules/`
- Claude Code CLI integration with detailed instructions in `CLAUDE.md`
- Context-aware suggestions and development guidance
{%- endif %}

The AI assistant understands this project's architecture, dependencies, and coding patterns.
{%- endif %}

### Project Structure

```
{% if cookiecutter.layout == "src" -%}
src/{{cookiecutter.project_slug}}/    # Main package source code
{%- else -%}
{{cookiecutter.project_slug}}/        # Main package source code
{%- endif %}
├── {% if cookiecutter.typer_cli == 'y' %}cli.py               # Command-line interface{% endif %}
├── foo.py              # Example module{% if cookiecutter.logging == 'y' %} with logging{% endif %}{% if cookiecutter.rich_output == 'y' %} and rich output{% endif %}{% if cookiecutter.async_support == 'y' %} and async support{% endif %}
{% if cookiecutter.pydantic_models == 'y' -%}
├── models.py           # Pydantic data models
{%- endif %}
{% if cookiecutter.pydantic_settings == 'y' -%}
├── config.py           # Configuration management
{%- endif %}
└── __init__.py         # Package initialization

tests/                  # Test files
├── test_foo.py         # Tests for foo module{% if cookiecutter.mocks == 'y' %} with mocking examples{% endif %}
{% if cookiecutter.pydantic_models == 'y' -%}
├── test_models.py      # Tests for Pydantic models
{%- endif %}
{% if cookiecutter.pydantic_settings == 'y' -%}
├── test_config.py      # Tests for configuration
{%- endif %}

{% if cookiecutter.agent_support == 'cursor' or cookiecutter.agent_support == 'both' -%}
.cursor/rules/          # Cursor IDE configuration
├── instructions.mdc    # Development guidelines
└── testing.mdc         # Testing guidelines
{%- endif %}

{% if cookiecutter.agent_support == 'claude-code' or cookiecutter.agent_support == 'both' -%}
CLAUDE.md               # Claude Code CLI instructions
{%- endif %}
{% if cookiecutter.build_tool == 'just' -%}
justfile                # Task automation commands
{%- else -%}
Makefile                # Task automation commands
{%- endif %}
pyproject.toml          # Project configuration and dependencies
README.md               # This file
```

## Releasing a new version

{% if cookiecutter.publish_to_pypi == "y" -%}

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).
{%- endif %}

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
