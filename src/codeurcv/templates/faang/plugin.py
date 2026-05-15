from pathlib import Path
from codeurcv.templates.base import TemplatePlugin


class FAANGTemplate(TemplatePlugin):
    name = "faang"
    description = "FAANG/ATS-optimized two-column layout with compact spacing"

    def template_path(self) -> Path:
        return Path(__file__).parent / "template.typ"

    def template_type(self) -> str:
        return "typ"
