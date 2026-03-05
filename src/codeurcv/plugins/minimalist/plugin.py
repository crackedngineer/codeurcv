from pathlib import Path
from codeurcv.plugins.base import TemplatePlugin

class MinimalistTemplate(TemplatePlugin):
    name = "minimalist"
    description = "Clean minimalist resume style"

    def template_path(self) -> Path:
        return Path(__file__).parent / "template.tex"