import typer
from pathlib import Path
from rich.console import Console
from importlib.metadata import version

from .core.renderer import ResumeRenderer
from .core.constants import DEFAULT_CONFIG_FILE, DEFAULT_OUT_DIR, DEFAULT_OUTPUT_FILENAME, DEFAULT_TEMPLATE

app = typer.Typer(help="Generate LaTeX resumes from YAML configs.")
console = Console()


def get_version() -> str:
    try:
        return version("codeurcv")
    except Exception:
        return "0.0.0-dev"


def version_callback(value: bool):
    if value:
        console.print(f"[bold cyan]codeurcv version:[/bold cyan] {get_version()}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "-v",
        "--version",
        help="Show version and exit",
        is_eager=True,
        callback=version_callback,
    ),
):
    pass


@app.command()
def run(
    input: Path = typer.Argument(
        DEFAULT_CONFIG_FILE, help="Path to your resume YAML or JSON"
    ),
    output: Path = typer.Option(
        DEFAULT_OUT_DIR, "--out", "-o", help="Output directory for the generated PDF"
    ),
    # Overrides — only needed if user wants to deviate from config values
    name: str = typer.Option(
        DEFAULT_OUTPUT_FILENAME, "--name", "-n", help="Override the output filename"
    ),
    template: str = typer.Option(
        DEFAULT_TEMPLATE, "--template", "-t", help="Override the template defined in config"
    ),
):
    """Render your resume from a YAML config."""
    console.print("[bold cyan]Starting resume generation...[/bold cyan]")

    renderer = ResumeRenderer()

    renderer.render(config_path=input, output_path=output, name=name, template=template)

    console.print("[bold green]Done![/bold green]")


@app.command()
def templates():
    """List available resume templates."""
    from .core.plugin_loader import load_builtin_plugins

    plugins = load_builtin_plugins()

    console.print("\n[bold]Available Templates:[/bold]\n")

    for name, plugin in plugins.items():
        console.print(f"• [cyan]{name}[/cyan] — {plugin.description}")
