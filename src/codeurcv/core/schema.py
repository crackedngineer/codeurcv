from typing import List, Optional

from pydantic import BaseModel, Field, field_serializer


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

    @field_serializer("github")
    def serialize_github(self, github: str):
        return github if github.startswith("https://") else f"https://{github}"

    @field_serializer("linkedin")
    def serialize_linkedin(self, linkedin: str):
        return linkedin if linkedin.startswith("https://") else f"https://{linkedin}"


class Education(ResumeSection):
    institution: str
    location: str
    degree: str
    year: int
    gpa: Optional[str] = None
    additional_information: List[str] = Field(default_factory=list)


class Job(ResumeSection):
    company: str
    role: str
    start: str
    end: Optional[str] = "Present"
    location: Optional[str] = None
    achievements: List[str] = Field(default_factory=list)
    technologies: List[str] = Field(default_factory=list)


class Project(ResumeSection):
    name: str
    description: List[str] = Field(default_factory=list)
    start: str
    end: Optional[str] = None
    technologies: List[str] = Field(default_factory=list)
    link: Optional[str] = None


class Skill(ResumeSection):
    category: str
    featured: List[str] = Field(default_factory=list)


class ResumeConfig(BaseModel):
    basic_details: BasicDetails
    summary: Optional[str] = None
    education: List[Education] = Field(default_factory=list)
    work: List[Job] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    skills: List[Skill] = Field(default_factory=list)
    location: Optional[str] = None
