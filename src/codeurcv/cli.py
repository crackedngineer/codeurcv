import typer
from pathlib import Path
from rich.console import Console
from importlib.metadata import version

from .core.renderer import ResumeRenderer
from .core.constants import DEFAULT_CONFIG_FILE, DEFAULT_OUT_DIR

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
    filename: Path = typer.Option(
        DEFAULT_CONFIG_FILE, "--file", "-f", help="Path to resume YAML config"
    ),
    out_dir: Path = typer.Option(
        DEFAULT_OUT_DIR, "--out-dir", "-o", help="Directory to save generated resume"
    ),
):
    """Render resume."""
    console.print("[bold cyan]Starting resume generation...[/bold cyan]")

    renderer = ResumeRenderer()

    renderer.render(filename, out_dir)

    console.print("[bold green]Done![/bold green]")


@app.command()
def templates():
    """List available resume templates."""
    from .core.plugin_loader import load_builtin_plugins

    plugins = load_builtin_plugins()

    console.print("\n[bold]Available Templates:[/bold]\n")

    for name, plugin in plugins.items():
        console.print(f"• [cyan]{name}[/cyan] — {plugin.description}")
