import tempfile
import logging
from pathlib import Path
from datetime import datetime

import typst

from codeurcv.core.template_loader import TemplateEngine
from codeurcv.core.logger import setup_logger
from codeurcv.core.plugin_loader import load_builtin_plugins
from codeurcv.core.schema import ResumeConfig
from codeurcv.core.settings import console
from codeurcv.core.constants import DEFAULT_OUTPUT_FILENAME, DEFAULT_TEMPLATE
from codeurcv.core.config_loader import load_config
from codeurcv.core.markdown_to_typst import convert as convert_md_to_typst, _PREAMBLE as _DEFAULT_PREAMBLE


class ResumeRenderer:
    def __init__(self):
        self.plugins = load_builtin_plugins()
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = log_dir / f"codeurcv_{timestamp}.log"
        self.logger = setup_logger(debug=False, log_file=self.log_file)

    def render(
        self,
        config_path: Path,
        output_dir: Path,
        out_filename: str = DEFAULT_OUTPUT_FILENAME,
        template: str = DEFAULT_TEMPLATE,
    ):
        console.print("\n[bold green]🚀 Building your resume...[/bold green]\n")

        try:
            raw_data = self._step(
                "Configuration loaded",
                lambda: load_config(config_path),
            )

            config = self._step(
                "Data validated",
                lambda: ResumeConfig(**raw_data),
            )

            plugin = self._step(
                f"Template applied: {template}",
                lambda: self._get_plugin(template),
            )

            data = plugin.preprocess(config)
            template_path = plugin.template_path()
            template_engine = TemplateEngine(template_path.parent)

            if plugin.template_type() == "typ":
                typst_content = self._step(
                    "Typst rendered",
                    lambda: plugin.postprocess(
                        template_engine.render(template_path.name, data.model_dump())
                    ),
                )
            else:
                rendered_md = self._step(
                    "Markdown rendered",
                    lambda: template_engine.render(template_path.name, data.model_dump()),
                )
                custom_preamble = plugin.typst_preamble()
                typst_content = self._step(
                    "Typst generated",
                    lambda: convert_md_to_typst(
                        plugin.postprocess(rendered_md),
                        preamble=custom_preamble or _DEFAULT_PREAMBLE,
                    ),
                )

            output_dir.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory() as tmpdir:
                tmp_path = Path(tmpdir)
                typ_file = tmp_path / f"{out_filename}.typ"
                typ_file.write_text(typst_content, encoding="utf-8")

                self._compile_pdf(typ_file, output_dir / f"{out_filename}.pdf")


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

    def _compile_pdf(self, typ_file: Path, output_pdf: Path):
        logging.info("Compiling: %s → %s", typ_file, output_pdf)

        with console.status("[green]Generating PDF...[/green]", spinner="dots"):
            compiler = typst.Compiler(str(typ_file))
            pdf_bytes = compiler.compile()

        output_pdf.write_bytes(pdf_bytes)
        logging.info("PDF written: %s (%d bytes)", output_pdf, len(pdf_bytes))
