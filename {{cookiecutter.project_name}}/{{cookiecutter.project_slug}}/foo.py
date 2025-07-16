{% if cookiecutter.logging == 'y' -%}
from loguru import logger
{%- endif %}
{% if cookiecutter.rich_output == 'y' -%}
from rich.console import Console
{%- endif %}
{% if cookiecutter.async_support == 'y' -%}
import asyncio
{%- endif %}

{% if cookiecutter.rich_output == 'y' -%}
console = Console()
{%- endif %}


def foo(bar: str) -> str:
    """Summary line.

    Extended description of function.

    Args:
        bar: Description of input argument.

    Returns:
        Description of return value
    """
    {% if cookiecutter.logging == 'y' -%}
    logger.info(f"Processing: {bar}")
    {%- endif %}
    {% if cookiecutter.rich_output == 'y' -%}
    console.print(f"[bold green]Processing:[/bold green] {bar}")
    {%- endif %}

    return bar


{% if cookiecutter.async_support == 'y' -%}
async def async_foo(bar: str) -> str:
    """Async version of foo function.

    Args:
        bar: Description of input argument.

    Returns:
        Description of return value
    """
    {% if cookiecutter.logging == 'y' -%}
    logger.info(f"Async processing: {bar}")
    {%- endif %}

    # Simulate async operation
    await asyncio.sleep(0.1)
    return f"async_{bar}"
{%- endif %}
