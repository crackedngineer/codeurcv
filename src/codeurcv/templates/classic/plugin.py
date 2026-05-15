from pathlib import Path
from codeurcv.templates.base import TemplatePlugin


class ClassicTemplate(TemplatePlugin):
    name = "classic"
    description = "Professional serif layout with navy section headers"

    def template_path(self) -> Path:
        return Path(__file__).parent / "template.typ"

    def template_type(self) -> str:
        return "typ"
