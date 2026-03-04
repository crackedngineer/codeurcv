from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any
from codeurcv.core.schema import ResumeConfig


class TemplatePlugin(ABC):
    """
    Base class for resume template plugins.
    """

    name: str
    description: str

    @abstractmethod
    def template_path(self) -> Path:
        """Return path to LaTeX template file."""

    def preprocess(self, data: ResumeConfig) -> ResumeConfig:
        """
        Optional hook to modify validated config
        before rendering.
        """
        return data

    def postprocess(self, tex_content: str) -> str:
        """
        Optional hook to modify final rendered LaTeX.
        """
        return tex_content