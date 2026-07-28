from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This is the schema for your data
class CourseCreate(BaseModel):
    title: str
    description: str
    price: float

# This is the path for your endpoint
@app.post("/api/courses/")
async def create_course(course: CourseCreate):
    return {"message": "Course created successfully", "data": course}