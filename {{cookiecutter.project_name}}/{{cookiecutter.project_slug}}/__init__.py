{% if cookiecutter.typer_cli == 'y' -%}
from {{cookiecutter.project_slug}}.cli import app

__all__ = ["app"]
{%- endif %}
