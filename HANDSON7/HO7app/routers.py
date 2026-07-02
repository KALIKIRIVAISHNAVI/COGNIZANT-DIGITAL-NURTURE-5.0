from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from typing import List
from HO7app.schemas import (
    CourseCreate, CourseResponse, 
    StudentCreate, StudentResponse, 
    EnrollmentCreate, EnrollmentResponse
)
import HO7app.database as db

router = APIRouter()

# --- Background Task Simulation Worker (Step 73) ---
def send_confirmation_email(student_email: str):
    # Simulates sending an asynchronous confirmation receipt
    print(f"Sending confirmation to {student_email}")


# =============================================================================
# COURSES ENDPOINTS (Steps 68, 69, 70, 71, 76, 77)
# =============================================================================

@router.post(
    "/api/courses/", 
    response_model=CourseResponse, 
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    description="Adds a fresh course specification to the local schema directory."
)
async def create_course(course: CourseCreate):
    new_id = db.course_id_counter
    course_entry = CourseResponse(id=new_id, **course.model_dump())
    db.courses_db[new_id] = course_entry
    db.course_id_counter += 1
    return course_entry

@router.get("/api/courses/", response_model=List[CourseResponse], tags=["Courses"])
async def get_all_courses():
    return list(db.courses_db.values())

@router.get("/api/courses/{id}", response_model=CourseResponse, tags=["Courses"])
async def get_course_by_id(id: int):
    if id not in db.courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    return db.courses_db[id]

@router.put("/api/courses/{id}", response_model=CourseResponse, tags=["Courses"])
async def update_course(id: int, updated_course: CourseCreate):
    if id not in db.courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    course_entry = CourseResponse(id=id, **updated_course.model_dump())
    db.courses_db[id] = course_entry
    return course_entry

@router.delete("/api/courses/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Courses"])
async def delete_course(id: int):
    if id not in db.courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    del db.courses_db[id]
    return None  # HTTP 204 requires returning absolutely no response body payload

@router.get("/api/courses/{id}/students/", response_model=List[StudentResponse], tags=["Courses"])
async def get_course_students(id: int):
    if id not in db.courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # 71. Perform an in-memory equivalent of an inner JOIN query across tables
    enrolled_student_ids = [
        e.student_id for e in db.enrollments_db.values() if e.course_id == id
    ]
    
    joined_students = [
        db.students_db[sid] for sid in enrolled_student_ids if sid in db.students_db
    ]
    return joined_students


# =============================================================================
# STUDENTS ENDPOINTS (Step 72)
# =============================================================================

@router.post("/api/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=["Students"])
async def create_student(student: StudentCreate):
    new_id = db.student_id_counter
    student_entry = StudentResponse(id=new_id, **student.model_dump())
    db.students_db[new_id] = student_entry
    db.student_id_counter += 1
    return student_entry

@router.get("/api/students/", response_model=List[StudentResponse], tags=["Students"])
async def get_all_students():
    return list(db.students_db.values())


# =============================================================================
# ENROLLMENTS ENDPOINTS (Steps 72, 73, 74)
# =============================================================================

@router.post("/api/enrollments/", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=["Enrollments"])
async def create_enrollment(enrollment: EnrollmentCreate, background_tasks: BackgroundTasks):
    # Validate referenced IDs exist
    if enrollment.course_id not in db.courses_db:
        raise HTTPException(status_code=404, detail="Course not found")
    if enrollment.student_id not in db.students_db:
        raise HTTPException(status_code=404, detail="Student not found")
        
    new_id = db.enrollment_id_counter
    enrollment_entry = EnrollmentResponse(id=new_id, **enrollment.model_dump())
    db.enrollments_db[new_id] = enrollment_entry
    db.enrollment_id_counter += 1
    
    # Fetch student target metadata safely
    student = db.students_db[enrollment.student_id]
    
    # 73. Register simulated email script into Background Workers
    background_tasks.add_task(send_confirmation_email, student.email)
    
    # 74. Returns HTTP 201 immediately without stalling execution loop processes
    return enrollment_entry