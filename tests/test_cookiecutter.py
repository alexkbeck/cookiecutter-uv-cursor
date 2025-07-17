from __future__ import annotations

import os
import shlex
import subprocess

from tests.utils import file_contains_text, is_valid_yaml, run_within_dir


def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_name": "my-project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.project_path.is_dir()


def test_using_pytest(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()

        # Assert that project was created.
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "example-project"
        assert result.project_path.is_dir()
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")

        # Install the uv environment and run the tests.
        with run_within_dir(str(result.project_path)):
            assert subprocess.check_call(shlex.split("uv sync")) == 0
            assert subprocess.check_call(shlex.split("uv run make test")) == 0


def test_src_layout_using_pytest(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"layout": "src"})

        # Assert that project was created.
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "example-project"
        assert result.project_path.is_dir()
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")

        # Install the uv environment and run the tests.
        with run_within_dir(str(result.project_path)):
            assert subprocess.check_call(shlex.split("uv sync")) == 0
            assert subprocess.check_call(shlex.split("uv run make test")) == 0


def test_devcontainer(cookies, tmp_path):
    """Test that the devcontainer files are created when devcontainer=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_not_devcontainer(cookies, tmp_path):
    """Test that the devcontainer files are not created when devcontainer=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert not os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_cicd_contains_pypi_secrets(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to_pypi": "y"})
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "PYPI_TOKEN")
        assert file_contains_text(f"{result.project_path}/Makefile", "build-and-publish")


def test_dont_publish(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to_pypi": "n"})
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
        assert not file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml", "make build-and-publish"
        )


def test_mkdocs(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "y"})
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy")
        assert file_contains_text(f"{result.project_path}/Makefile", "docs:")
        assert os.path.isdir(f"{result.project_path}/docs")


def test_not_mkdocs(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "n"})
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
        assert not file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy"
        )
        assert not file_contains_text(f"{result.project_path}/Makefile", "docs:")
        assert not os.path.isdir(f"{result.project_path}/docs")


def test_tox(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/tox.ini")
        assert file_contains_text(f"{result.project_path}/tox.ini", "[tox]")


def test_dockerfile(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/Dockerfile")


def test_not_dockerfile(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/Dockerfile")


def test_codecov(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert os.path.isfile(f"{result.project_path}/codecov.yaml")
        assert os.path.isfile(f"{result.project_path}/.github/workflows/validate-codecov-config.yml")


def test_not_codecov(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"codecov": "n"})
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert not os.path.isfile(f"{result.project_path}/codecov.yaml")
        assert not os.path.isfile(f"{result.project_path}/.github/workflows/validate-codecov-config.yml")


def test_remove_release_workflow(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to_pypi": "n", "mkdocs": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/.github/workflows/on-release-main.yml")

        result = cookies.bake(extra_context={"publish_to_pypi": "n", "mkdocs": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/.github/workflows/on-release-main.yml")


# New tests for missing features

def test_deptry(cookies, tmp_path):
    """Test that deptry is included when deptry=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"deptry": "y"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/pyproject.toml", '"deptry>=0.23.0"')
        assert file_contains_text(f"{result.project_path}/Makefile", "uv run deptry")


def test_not_deptry(cookies, tmp_path):
    """Test that deptry is not included when deptry=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"deptry": "n"})
        assert result.exit_code == 0
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", '"deptry>=0.23.0"')
        assert not file_contains_text(f"{result.project_path}/Makefile", "uv run deptry")


def test_typer_cli(cookies, tmp_path):
    """Test that typer CLI components are created when typer_cli=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"typer_cli": "y"})
        assert result.exit_code == 0
        # Check typer dependency is added
        assert file_contains_text(f"{result.project_path}/pyproject.toml", '"typer>=0.16.0"')
        # Check CLI script entry point is added
        assert file_contains_text(f"{result.project_path}/pyproject.toml", "[project.scripts]")
        # Check CLI file exists and has content
        assert os.path.isfile(f"{result.project_path}/example_project/cli.py")
        assert file_contains_text(f"{result.project_path}/example_project/cli.py", "import typer")
        # Check test file exists
        assert os.path.isfile(f"{result.project_path}/tests/test_cli.py")
        assert file_contains_text(f"{result.project_path}/tests/test_cli.py", "from typer.testing import CliRunner")
        # Check Makefile includes CLI target
        assert file_contains_text(f"{result.project_path}/Makefile", "run-cli:")
        # Check Dockerfile uses CLI
        assert file_contains_text(f"{result.project_path}/Dockerfile", 'uv", "run", "example_project"')
        # Check __init__.py imports CLI
        assert file_contains_text(f"{result.project_path}/example_project/__init__.py", "from example_project.cli import app")


def test_not_typer_cli(cookies, tmp_path):
    """Test that typer CLI components are not created when typer_cli=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"typer_cli": "n"})
        assert result.exit_code == 0
        # Check typer dependency is not added
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", '"typer>=0.16.0"')
        # Check no CLI script entry point
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", "[project.scripts]")
        # Check CLI file is empty or doesn't have typer content
        cli_file = f"{result.project_path}/example_project/cli.py"
        if os.path.isfile(cli_file):
            assert not file_contains_text(cli_file, "import typer")
        # Check Makefile doesn't include CLI target
        assert not file_contains_text(f"{result.project_path}/Makefile", "run-cli:")
        # Check Dockerfile uses alternative command
        assert file_contains_text(f"{result.project_path}/Dockerfile", '"python", "example_project/foo.py"')


def test_agent_support_none(cookies, tmp_path):
    """Test that no agent support files are created when agent_support=none"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"agent_support": "none"})
        assert result.exit_code == 0
        assert not os.path.isdir(f"{result.project_path}/.cursor")
        assert not os.path.isfile(f"{result.project_path}/CLAUDE.md")


def test_agent_support_cursor(cookies, tmp_path):
    """Test that only cursor files are created when agent_support=cursor"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"agent_support": "cursor"})
        assert result.exit_code == 0
        assert os.path.isdir(f"{result.project_path}/.cursor")
        assert os.path.isfile(f"{result.project_path}/.cursor/rules/instructions.mdc")
        assert not os.path.isfile(f"{result.project_path}/CLAUDE.md")


def test_agent_support_claude_code(cookies, tmp_path):
    """Test that only claude code files are created when agent_support=claude-code"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"agent_support": "claude-code"})
        assert result.exit_code == 0
        assert not os.path.isdir(f"{result.project_path}/.cursor")
        assert os.path.isfile(f"{result.project_path}/CLAUDE.md")


def test_agent_support_both(cookies, tmp_path):
    """Test that both agent support files are created when agent_support=both"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"agent_support": "both"})
        assert result.exit_code == 0
        assert os.path.isdir(f"{result.project_path}/.cursor")
        assert os.path.isfile(f"{result.project_path}/.cursor/rules/instructions.mdc")
        assert os.path.isfile(f"{result.project_path}/CLAUDE.md")


def test_logging(cookies, tmp_path):
    """Test that loguru dependency is added when logging=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"logging": "y"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/pyproject.toml", '"loguru>=0.7.3"')


def test_not_logging(cookies, tmp_path):
    """Test that loguru dependency is not added when logging=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"logging": "n"})
        assert result.exit_code == 0
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", '"loguru>=0.7.3"')


def test_rich_output(cookies, tmp_path):
    """Test that rich dependency is added when rich_output=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"rich_output": "y"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/pyproject.toml", '"rich>=13.7.0"')


def test_not_rich_output(cookies, tmp_path):
    """Test that rich dependency is not added when rich_output=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"rich_output": "n"})
        assert result.exit_code == 0
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", '"rich>=13.7.0"')


def test_pydantic_models(cookies, tmp_path):
    """Test that pydantic dependency and model files are created when pydantic_models=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"pydantic_models": "y"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/pyproject.toml", '"pydantic>=2.5.0"')
        assert os.path.isfile(f"{result.project_path}/example_project/models.py")
        assert os.path.isfile(f"{result.project_path}/tests/test_models.py")


def test_not_pydantic_models(cookies, tmp_path):
    """Test that pydantic dependency and model files are not created when pydantic_models=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"pydantic_models": "n"})
        assert result.exit_code == 0
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", '"pydantic>=2.5.0"')
        assert not os.path.isfile(f"{result.project_path}/example_project/models.py")
        assert not os.path.isfile(f"{result.project_path}/tests/test_models.py")


def test_async_support(cookies, tmp_path):
    """Test that pytest-asyncio dependency is added when async_support=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"async_support": "y"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/pyproject.toml", '"pytest-asyncio>=0.21.0"')


def test_not_async_support(cookies, tmp_path):
    """Test that pytest-asyncio dependency is not added when async_support=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"async_support": "n"})
        assert result.exit_code == 0
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", '"pytest-asyncio>=0.21.0"')


def test_build_tool_make(cookies, tmp_path):
    """Test that Makefile is kept and justfile is removed when build_tool=make"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"build_tool": "make"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/Makefile")
        assert not os.path.isfile(f"{result.project_path}/justfile")


def test_build_tool_just(cookies, tmp_path):
    """Test that justfile is kept and Makefile is removed when build_tool=just"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"build_tool": "just"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/Makefile")
        assert os.path.isfile(f"{result.project_path}/justfile")
        # Check justfile has content
        assert file_contains_text(f"{result.project_path}/justfile", "# Install the project in development mode")


def test_pydantic_settings(cookies, tmp_path):
    """Test that pydantic-settings dependency and config files are created when pydantic_settings=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"pydantic_settings": "y"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/pyproject.toml", '"pydantic-settings>=2.1.0"')
        assert os.path.isfile(f"{result.project_path}/example_project/config.py")
        assert os.path.isfile(f"{result.project_path}/tests/test_config.py")


def test_not_pydantic_settings(cookies, tmp_path):
    """Test that pydantic-settings dependency and config files are not created when pydantic_settings=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"pydantic_settings": "n"})
        assert result.exit_code == 0
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", '"pydantic-settings>=2.1.0"')
        assert not os.path.isfile(f"{result.project_path}/example_project/config.py")
        assert not os.path.isfile(f"{result.project_path}/tests/test_config.py")


def test_mocks(cookies, tmp_path):
    """Test that pytest-mock dependency is added when mocks=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mocks": "y"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/pyproject.toml", '"pytest-mock>=3.12.0"')


def test_not_mocks(cookies, tmp_path):
    """Test that pytest-mock dependency is not added when mocks=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mocks": "n"})
        assert result.exit_code == 0
        assert not file_contains_text(f"{result.project_path}/pyproject.toml", '"pytest-mock>=3.12.0"')


def test_include_github_actions_no(cookies, tmp_path):
    """Test that github actions files are not created when include_github_actions=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"include_github_actions": "n"})
        assert result.exit_code == 0
        assert not os.path.isdir(f"{result.project_path}/.github")


def test_src_layout_directory_structure(cookies, tmp_path):
    """Test that src layout properly moves files to src directory"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"layout": "src"})
        assert result.exit_code == 0
        # Check that the main package is in src directory
        assert os.path.isdir(f"{result.project_path}/src")
        assert os.path.isdir(f"{result.project_path}/src/example_project")
        assert os.path.isfile(f"{result.project_path}/src/example_project/__init__.py")
        assert os.path.isfile(f"{result.project_path}/src/example_project/foo.py")
        # Check that the package is NOT in the root directory
        assert not os.path.isdir(f"{result.project_path}/example_project")


def test_flat_layout_directory_structure(cookies, tmp_path):
    """Test that flat layout keeps files in root directory"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"layout": "flat"})
        assert result.exit_code == 0
        # Check that the main package is in root directory
        assert os.path.isdir(f"{result.project_path}/example_project")
        assert os.path.isfile(f"{result.project_path}/example_project/__init__.py")
        assert os.path.isfile(f"{result.project_path}/example_project/foo.py")
        # Check that src directory doesn't exist
        assert not os.path.isdir(f"{result.project_path}/src")


# License tests
def test_license_mit(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "MIT license"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")
        with open(f"{result.project_path}/LICENSE", encoding="utf8") as licfile:
            content = licfile.readlines()
            assert len(content) == 21


def test_license_bsd(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "BSD license"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")
        with open(f"{result.project_path}/LICENSE", encoding="utf8") as licfile:
            content = licfile.readlines()
            assert len(content) == 28


def test_license_isc(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "ISC license"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")
        with open(f"{result.project_path}/LICENSE", encoding="utf8") as licfile:
            content = licfile.readlines()
            assert len(content) == 7


def test_license_apache(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "Apache Software License 2.0"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")
        with open(f"{result.project_path}/LICENSE", encoding="utf8") as licfile:
            content = licfile.readlines()
            assert len(content) == 202


def test_license_gplv3(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "GNU General Public License v3"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        with open(f"{result.project_path}/LICENSE", encoding="utf8") as licfile:
            content = licfile.readlines()
            assert len(content) == 674


def test_license_no_license(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "Not open source"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")
