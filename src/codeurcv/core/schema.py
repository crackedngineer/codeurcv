from typing import List, Optional
from pydantic import BaseModel, Field, field_validator

from codeurcv.core.constants import DEFAULT_TEMPLATE

class ResumeSection(BaseModel):
    """Base model for resume sections with optional ordering."""
    priority: Optional[int] = None

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
    duration: str
    gpa: Optional[str] = None
    additional_information: List[str] = Field(default_factory=list)

class Job(ResumeSection):
    company: str
    role: str
    duration: str
    achievements: List[str] = Field(default_factory=list)
    technologies: List[str] = Field(default_factory=list)

class Project(ResumeSection):
    name: str
    description: List[str] = Field(default_factory=list)
    technologies: List[str] = Field(default_factory=list)
    link: Optional[str] = None
    date: Optional[str] = None

class Skill(ResumeSection):
    name: str
    featured_skills: List[str] = Field(default_factory=list)

class ResumeConfig(BaseModel):
    basic_details: BasicDetails
    summary: Optional[str] = None
    education: List[Education] = Field(default_factory=list)
    work: List[Job] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    skills: List[Skill] = Field(default_factory=list)

    @field_validator("filename")
    @classmethod
    def strip_pdf_extension(cls, v: str) -> str:
        return v.removesuffix(".pdf")
