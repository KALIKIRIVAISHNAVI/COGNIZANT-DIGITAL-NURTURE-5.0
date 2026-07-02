from fastapi import APIRouter, Response, status, Query, Request
from fastapi.responses import JSONResponse
from typing import Optional, List
import HO8app.database as db
from HO8app.schemas import CourseCreate, CourseResponse, PaginatedCourseResponse

# 82. Explicit version configuration via path prefixing
router = APIRouter(prefix="/api/v1")

# 85. Standardized JSON Error Custom Helper Generator
def make_error_response(code: str, message: str, field: Optional[str] = None, status_code: int = 404):
    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "code": code,
                "message": message,
                "field": field
            }
        }
    )

# =============================================================================
# 78. NOUNS PLURAL SCHEMAS: /api/v1/courses/
# =============================================================================

@router.get("/courses/", response_model=PaginatedCourseResponse)
async def get_courses(
    request: Request,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=2, ge=1),
    search: Optional[str] = Query(default=None)
):
    # Convert mock dict collection data store elements into a clean Python sequence list
    all_records = list(db.courses_db.values())
    
    # 84. Case-Insensitive Keyword Substring Query Evaluation Handler (LIKE matching)
    if search:
        all_records = [
            c for c in all_records 
            if search.lower() in c["name"].lower() or search.lower() in c["code"].lower()
        ]
        
    total_count = len(all_records)
    
    # 83. Calculate Offset/Limit Windows
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_records = all_records[start_index:end_index]
    
    # Construct Navigation String Links
    base_url = str(request.base_url).rstrip("/") + request.url.path
    search_param = f"&search={search}" if search else ""
    
    next_url = f"{base_url}?page={page + 1}&page_size={page_size}{search_param}" if end_index < total_count else None
    prev_url = f"{base_url}?page={page - 1}&page_size={page_size}{search_param}" if page > 1 else None
    
    return {
        "count": total_count,
        "next": next_url,
        "previous": prev_url,
        "results": paginated_records
    }

@router.get("/courses/{id}", response_model=CourseResponse)
async def get_course_by_id(id: int):
    # 85. Standardized Error Response if Resource Key Is Not Found
    if id not in db.courses_db:
        return make_error_response("NOT_FOUND", f"Course with id {id} does not exist", field=None, status_code=404)
    return db.courses_db[id]

@router.post("/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, response: Response, request: Request):
    # Check if duplicate key code exists to prevent bad inputs
    for existing in db.courses_db.values():
        if existing["code"] == course.code:
            return make_error_response("BAD_REQUEST", "Course code specification must remain unique", field="code", status_code=400)
            
    new_id = db.course_id_counter
    new_entry = {"id": new_id, **course.model_dump()}
    db.courses_db[new_id] = new_entry
    db.course_id_counter += 1
    
    # 81. Append a resource pointing Location target validation schema into header fields
    location_url = f"{str(request.base_url).rstrip('/')}/api/v1/courses/{new_id}/"
    response.headers["Location"] = location_url
    
    return new_entry

@router.put("/courses/{id}", response_model=CourseResponse)
async def full_replace_course(id: int, course: CourseCreate):
    """79. PUT completely replaces the target resource (requires all fields)."""
    if id not in db.courses_db:
        return make_error_response("NOT_FOUND", f"Course with id {id} does not exist", field=None, status_code=404)
        
    updated_entry = {"id": id, **course.model_dump()}
    db.courses_db[id] = updated_entry
    return updated_entry

@router.patch("/courses/{id}", response_model=CourseResponse)
async def partial_update_course(id: int, course_delta: dict):
    """79. PATCH modifies only the fields supplied in the request body."""
    if id not in db.courses_db:
        return make_error_response("NOT_FOUND", f"Course with id {id} does not exist", field=None, status_code=404)
        
    target_record = db.courses_db[id]
    
    # Iterate and overwrite only provided key configurations
    for key, value in course_delta.items():
        if key in target_record and value is not None:
            target_record[key] = value
            
    db.courses_db[id] = target_record
    return target_record

@router.delete("/courses/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_course(id: int):
    """80. Returns 204 No Content with a completely blank response body upon successful removal."""
    if id not in db.courses_db:
        return make_error_response("NOT_FOUND", f"Course with id {id} does not exist", field=None, status_code=404)
    del db.courses_db[id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)