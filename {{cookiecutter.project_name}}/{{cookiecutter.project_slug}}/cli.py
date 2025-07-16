{% if cookiecutter.typer_cli == 'y' -%}
import typer


def hello(name: str = "World") -> str:
    """Simple hello command.

    Extended description of command.

    Args:
        name: Name to greet.

    Returns:
        Greeting message.
    """
    return f"Hello {name}!"


app = typer.Typer()
app.command()(hello)


if __name__ == "__main__":  # pragma: no cover
    app()
{%- endif %}
