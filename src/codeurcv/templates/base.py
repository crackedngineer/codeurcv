from abc import ABC, abstractmethod
from pathlib import Path
from codeurcv.core.schema import ResumeConfig


class TemplatePlugin(ABC):
    """Base class for resume template plugins."""

    name: str
    description: str

    @abstractmethod
    def template_path(self) -> Path:
        """Return path to the Markdown (Jinja2) template file."""

    def preprocess(self, data: ResumeConfig) -> ResumeConfig:
        """Optional hook to modify validated config before rendering."""
        return data

    def postprocess(self, content: str) -> str:
        """Optional hook to modify rendered content before Typst conversion (md) or compilation (typ)."""
        return content

    def template_type(self) -> str:
        """Return 'md' for Jinja→Markdown→Typst pipeline or 'typ' for direct Jinja→Typst."""
        return "md"

    def typst_preamble(self) -> str:
        """Optional custom Typst preamble override for 'md' pipeline templates."""
        return ""