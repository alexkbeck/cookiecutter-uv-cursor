<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/alexkbeck/cookiecutter-uv-cursor/main/docs/static/cookiecutter.svg">
</p style = "margin-bottom: 2rem;">

---

[![Build status](https://img.shields.io/github/actions/workflow/status/alexkbeck/cookiecutter-uv-cursor/main.yml?branch=main)](https://github.com/alexkbeck/cookiecutter-uv-cursor/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/alexkbeck/cookiecutter-uv-cursor/blob/main/pyproject.toml)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://alexkbeck.github.io/cookiecutter-uv-cursor/)
[![License](https://img.shields.io/github/license/alexkbeck/cookiecutter-uv-cursor)](https://img.shields.io/github/license/alexkbeck/cookiecutter-uv-cursor)

This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development, testing, and deployment. It supports the following features:

- [uv](https://docs.astral.sh/uv/) for dependency management
- Supports both [src and flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff) and [mypy](https://mypy.readthedocs.io/en/stable/)
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/)
- Compatibility testing for multiple versions of Python with [tox-uv](https://github.com/tox-dev/tox-uv)

**Optional Features:**
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Publishing to [PyPI](https://pypi.org) by creating a new release on GitHub
- Dependency usage analysis with [deptry](https://github.com/alexkbeck/deptry)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Test coverage reporting with [codecov](https://about.codecov.io/)
- Containerization with [Docker](https://www.docker.com/) or [Podman](https://podman.io/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)
- Command-line interface with [Typer](https://typer.tiangolo.com/)
- AI agent support for [Cursor](https://cursor.sh/) and [Claude Code](https://anthropic.com/claude-code)
- Structured logging support with [Loguru](https://loguru.readthedocs.io/en/stable/)
- Rich console output with [Rich](https://rich.readthedocs.io/)
- Data models with [Pydantic](https://docs.pydantic.dev/)
- Build automation with [Make](https://www.gnu.org/software/make/) or [Just](https://github.com/casey/just)
- Configuration management with [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- Testing mocks with [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/)
- Multiple open source license options

---

<p align="center">
  <a href="https://alexkbeck.github.io/cookiecutter-uv-cursor/">Documentation</a> - <a href="https://github.com/alexkbeck/cookiecutter-uv-cursor-example">Example</a>
</p>

---

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/alexkbeck/cookiecutter-uv-cursor.git
```

or if you don't have `uv` installed yet:

```bash
pip install cookiecutter
cookiecutter https://github.com/alexkbeck/cookiecutter-uv-cursor.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project.

## Acknowledgements

This project is partially based on [Audrey
Feldroy\'s](https://github.com/audreyfeldroy)\'s great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
repository.
