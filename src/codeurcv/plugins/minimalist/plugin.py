from pathlib import Path

from codeurcv.core.schema import ResumeConfig
from codeurcv.plugins.base import TemplatePlugin
from codeurcv.core.markdown_converter import MarkdownConverter


class MinimalistTemplate(TemplatePlugin):
    name = "minimalist"
    description = "Clean minimalist resume style"

    def template_path(self) -> Path:
        return Path(__file__).parent / "template.tex"
    
    def preprocess(self, data: ResumeConfig) -> ResumeConfig:
        converter = MarkdownConverter()
        if data.summary:
            data.summary = converter.convert(data.summary)
        for job in data.work:
            job.achievements = [converter.convert(achievement) for achievement in job.achievements]
        for proj in data.projects:
            proj.description = [converter.convert(desc) for desc in proj.description]
        return data