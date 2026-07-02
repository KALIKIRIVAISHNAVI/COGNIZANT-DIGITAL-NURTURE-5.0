from pydantic import BaseModel, EmailStr

# --- User Registration & Output Profiles ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

# --- Token Transmission Frameworks ---
class Token(BaseModel):
    access_token: str
    token_type: str

# --- Course Profiles ---
class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int