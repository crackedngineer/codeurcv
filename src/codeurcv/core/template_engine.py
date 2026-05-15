import re
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

_MD_ESCAPE = re.compile(r"([\\`*_\[\]])")
_TYPST_ESCAPE = re.compile(r"([#@$<>\\])")


def _md_escape(s: str) -> str:
    """Escape Markdown special characters in plain-text fields."""
    if not isinstance(s, str):
        return s
    return _MD_ESCAPE.sub(r"\\\1", s)


def _typst_escape(s: str) -> str:
    """Escape Typst special characters in plain-text fields used in .typ templates."""
    if not isinstance(s, str):
        return s
    return _TYPST_ESCAPE.sub(r"\\\1", s)


class TemplateEngine:
    def __init__(self, template_dir: Path):
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=False,
        )
        self.env.filters["md_escape"] = _md_escape
        self.env.filters["typst_escape"] = _typst_escape

    def render(self, template_name: str, context: dict) -> str:
        template = self.env.get_template(template_name)
        return template.render(**context)
