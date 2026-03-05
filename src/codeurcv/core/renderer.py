import tempfile
import shutil
import logging
import subprocess
from pathlib import Path
from datetime import datetime

from codeurcv.core.template_loader import TemplateEngine
from codeurcv.core.logger import setup_logger
from codeurcv.core.plugin_loader import load_builtin_plugins
from codeurcv.core.schema import ResumeConfig
from codeurcv.core.settings import console
from codeurcv.core.dependency_checker import check_dependencies
from codeurcv.core.constants import DEFAULT_OUTPUT_FILENAME, DEFAULT_TEMPLATE
from codeurcv.core.config_loader import load_config

class ResumeRenderer:
    def __init__(self):
        self.plugins = load_builtin_plugins()
        check_dependencies()
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = log_dir / f"codeurcv_{timestamp}.log"
        self.logger = setup_logger(debug=False, log_file=self.log_file)

    def render(self, config_path: Path, output_dir: Path, out_filename: str = DEFAULT_OUTPUT_FILENAME, template: str = DEFAULT_TEMPLATE):
        console.print("\n[bold green]🚀 Building your resume...[/bold green]\n")

        try:
            # STEP 1
            raw_data = self._step(
                "Configuration loaded",
                lambda: load_config(config_path),
            )

            # STEP 2
            config = self._step(
                "Data validated",
                lambda: ResumeConfig(**raw_data),
            )

            # STEP 3
            plugin = self._step(
                f"Template applied: {template}",
                lambda: self._get_plugin(template),
            )

            # STEP 4
            data = plugin.preprocess(config)

            template_path = plugin.template_path()
            template_engine = TemplateEngine(template_path.parent)

            rendered_tex = self._step(
                "LaTeX rendered",
                lambda: template_engine.render(
                    template_path.name,
                    data.model_dump(),
                ),
            )

            output_dir.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory() as tmpdir:
                tmp_path = Path(tmpdir)
                tex_file = tmp_path / f"{out_filename}.tex"
                tex_file.write_text(plugin.postprocess(rendered_tex))

                self._generate_pdf(tex_file, tmp_path)

                final_pdf = output_dir / f"{out_filename}.pdf"
                shutil.copy(tmp_path / f"{out_filename}.pdf", final_pdf)


            console.print("\n[bold green]✔ PDF generated[/bold green]\n")
            console.print("[bold green]🎉 Done![/bold green]")
            console.print(
                f"[cyan]📁 {output_dir.resolve() / f'{out_filename}.pdf'}[/cyan]\n"
            )

        except Exception:
            console.print("\n[bold red]❌ Resume generation failed.[/bold red]")
            console.print(f"[yellow]See full logs at:[/yellow] {self.log_file}\n")
            raise

    def _step(self, message: str, func):
        try:
            result = func()
            console.print(f"[green]✔[/green] {message}")
            logging.info("SUCCESS: %s", message)
            return result
        except Exception as e:
            logging.exception("FAILED: %s", message)
            raise RuntimeError(f"{message} failed.") from e

    def _get_plugin(self, template_name: str):
        if template_name not in self.plugins:
            available = ", ".join(self.plugins.keys())
            raise RuntimeError(
                f"Template '{template_name}' not found.\n"
                f"Available templates: {available}"
            )
        return self.plugins[template_name]

    def _generate_pdf(self, tex_file: Path, output_dir: Path):
        """
        Runs pdflatex to generate PDF from the .tex file.
         - Uses subprocess to call pdflatex with appropriate arguments.
         - Captures and logs output in real-time.
         - Raises an error if PDF generation fails.
        """
        command = [
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory",
            str(output_dir),
            str(tex_file),
        ]

        console.print(f"[bold] > Running:[/bold] {' '.join(command)}")
        logging.info("Running command: %s", " ".join(command))

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        with console.status("[green]Generating PDF...[/green]", spinner="dots"):
            stdout, _ = process.communicate()

        for line in stdout.splitlines():
            logging.info(line)

        if process.returncode != 0:
            raise RuntimeError("PDF generation failed.")
