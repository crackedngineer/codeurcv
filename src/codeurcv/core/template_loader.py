from pathlib import Path

from jinja2 import Environment, FileSystemLoader

_LATEX_SPECIAL = [
    ("\\", r"\textbackslash{}"),
    ("&", r"\&"),
    ("%", r"\%"),
    ("$", r"\$"),
    ("#", r"\#"),
    ("_", r"\_"),
    ("^", r"\^{}"),
    ("~", r"\~{}"),
    ("{", r"\{"),
    ("}", r"\}"),
]


def _latex_escape(s: str) -> str:
    if not isinstance(s, str):
        return s
    for char, escaped in _LATEX_SPECIAL:
        s = s.replace(char, escaped)
    return s


class TemplateEngine:
    def __init__(self, template_dir: Path):
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            block_start_string=r"\BLOCK{",
            block_end_string="}",
            variable_start_string=r"\VAR{",
            variable_end_string="}",
            comment_start_string=r"\#{",
            comment_end_string="}",
            line_statement_prefix="%%",
            line_comment_prefix="%#",
            trim_blocks=True,
            autoescape=False,
        )
        self.env.filters["latex_escape"] = _latex_escape

    def render(self, template_name: str, context: dict) -> str:
        template = self.env.get_template(template_name)
        return template.render(**context)
