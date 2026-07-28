from pydantic import BaseModel
from typing import List, Optional

# Core Course Data Models
class CourseBase(BaseModel):
    name: str
    code: str
    credits: int

class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int

class CoursePatch(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[str] = None

class CourseResponse(CourseBase):
    id: int

# 83. DRF Standardized Pagination Wrapper Envelope Profile
class PaginatedCourseResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[CourseResponse]