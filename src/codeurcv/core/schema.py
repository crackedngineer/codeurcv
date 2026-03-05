from typing import List, Optional
from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import core_schema
from codeurcv.core.markdown_converter import MarkdownConverter 
import logging

converter = MarkdownConverter()
class ResumeSection(BaseModel):
    """Base model for resume sections with optional ordering."""
    priority: Optional[int] = None
    
class MarkdownContent(str):
    """A string type that will be rendered as bold markdown content."""
    def __new__(cls, content):
        converted_content = converter.convert(content)
        return super().__new__(cls, converted_content)
    
    def __init__(self, content):
        try:
            super().__init__()
        except Exception as e:
            logging.error(f"Error initializing MarkdownContent: {e}")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_plain_validator_function(
            cls,
            serialization=core_schema.plain_serializer_function_ser_schema(str),
        )

class BasicDetails(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    location: Optional[str] = None

class Education(ResumeSection):
    institution: str
    location: str
    degree: str
    year: int
    gpa: Optional[str] = None
    additional_information: List[MarkdownContent] = Field(default_factory=list)

class Job(ResumeSection):
    company: str
    role: str
    start: str
    end: Optional[str] = "Present"
    location: Optional[str] = None
    achievements: List[MarkdownContent] = Field(default_factory=list)
    technologies: List[MarkdownContent] = Field(default_factory=list)

class Project(ResumeSection):
    name: str
    description: List[MarkdownContent] = Field(default_factory=list)
    start: str
    end: Optional[str] = None
    technologies: List[MarkdownContent] = Field(default_factory=list)
    link: Optional[str] = None

class Skill(ResumeSection):
    category: str
    featured: List[MarkdownContent] = Field(default_factory=list)

class ResumeConfig(BaseModel):
    basic_details: BasicDetails
    summary: Optional[MarkdownContent] = None
    education: List[Education] = Field(default_factory=list)
    work: List[Job] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    skills: List[Skill] = Field(default_factory=list)
    location: Optional[str] = None