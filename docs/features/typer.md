# Command-line interface with Typer

[Typer](https://typer.tiangolo.com/) is a modern Python library for creating beautiful command-line interfaces based on Python type hints.

If `typer_cli` is set to `"y"`, the generated project will include a CLI module with a sample command. The CLI will be automatically available after installation.

## Usage

After creating your project, you can run the CLI:

```bash
# Run the hello command
your-project-name hello

# Run with a custom name
your-project-name hello --name Alice

# Get help
your-project-name --help
```

## Development

During development, you can run the CLI using:

```bash
# Run directly
uv run your-project-name hello

# Or using the Makefile
make run-cli
```

## Testing

The template includes tests for the CLI using Typer's testing utilities. Run them with:

```bash
make test
```

The CLI commands are automatically tested in the CI/CD pipeline when `include_github_actions` is enabled.
