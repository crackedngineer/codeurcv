from pathlib import Path
from codeurcv.templates.base import TemplatePlugin


class MinimalistTemplate(TemplatePlugin):
    name = "minimalist"
    description = "Clean minimalist resume style"

    def template_path(self) -> Path:
        return Path(__file__).parent / "template.typ"

    def template_type(self) -> str:
        return "typ"