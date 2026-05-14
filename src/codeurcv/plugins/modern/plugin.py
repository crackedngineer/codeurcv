from pathlib import Path
from codeurcv.plugins.base import TemplatePlugin


class ModernTemplate(TemplatePlugin):
    name = "modern"
    description = "Contemporary teal accent design with clean hierarchy"

    def template_path(self) -> Path:
        return Path(__file__).parent / "template.typ"

    def template_type(self) -> str:
        return "typ"
