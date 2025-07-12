{% if cookiecutter.typer_cli == 'y' -%}
from typer.testing import CliRunner

from {{cookiecutter.project_slug}}.cli import app


def test_hello_default():
    runner = CliRunner()
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout


def test_hello_with_name():
    runner = CliRunner()
    result = runner.invoke(app, ["hello", "--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice!" in result.stdout
{%- endif %} 