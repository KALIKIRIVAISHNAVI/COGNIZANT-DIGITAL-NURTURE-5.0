from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
from jose import jwt, JWTError

import HO9app.database as db
from HO9app.security import get_password_hash, verify_password, create_access_token, SECRET_KEY, ALGORITHM
from HO9app.schemas import UserCreate, UserResponse, Token, CourseResponse

router = APIRouter()

# 92. Establish the OAuth2 standard token extraction dependency scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# =============================================================================
# TASK 1: USER REGISTRATION ENDPOINTS
# =============================================================================

@router.post("/api/v1/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate):
    # 88. Enforce unique constraint check on emails to prevent duplication conflicts
    for user in db.users_db.values():
        if user["email"] == user_in.email:
            raise HTTPException(status_code=409, detail="Email already registered")
    
    new_id = db.user_id_counter
    # 87 & 89. Securely process the password hash via bcrypt
    hashed_pwd = get_password_hash(user_in.password)
    
    # 86. Build a secure user structural mapping record
    user_record = {
        "id": new_id,
        "email": user_in.email,
        "hashed_password": hashed_pwd,
        "is_active": True
    }
    
    db.users_db[new_id] = user_record
    db.user_id_counter += 1
    return user_record

# =============================================================================
# TASK 2: AUTHENTICATION AND ROUTE SECURITY DEPENDENCIES
# =============================================================================

@router.post("/api/v1/auth/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Find user profile by mapping criteria match
    user_record = None
    for u in db.users_db.values():
        if u["email"] == form_data.username:
            user_record = u
            break
            
    # Verify username matching credentials and validate the hashed password signature
    if not user_record or not verify_password(form_data.password, user_record["hashed_password"]):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
        
    # 91. Issue signed JSON Web Token configuration out to client context
    access_token = create_access_token(data={"sub": user_record["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

# 92. User extraction model layer decoding and tracking JWT validation states
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode signature keys
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    # Query structural dictionary records
    for user in db.users_db.values():
        if user["email"] == username:
            return user
            
    raise credentials_exception

# =============================================================================
# SECURED COURSE CONFIGURATION MANAGER ROUTING INTERFACES
# =============================================================================

# Public Endpoint: Anyone can access without a token
@router.get("/api/v1/courses/", response_model=List[CourseResponse])
async def get_public_courses():
    return list(db.courses_db.values())

# 93. Restricted Endpoint: Requires token authentication via Depends(get_current_user)
@router.post("/api/v1/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_secure_course(course_payload: CourseResponse, current_user: dict = Depends(get_current_user)):
    if course_payload.id in db.courses_db:
        raise HTTPException(status_code=400, detail="Course already exists")
    db.courses_db[course_payload.id] = course_payload.model_dump()
    return course_payload

# 93. Restricted Endpoint: Requires a valid bearer token to allow deletions
@router.delete("/api/v1/courses/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_secure_course(id: int, current_user: dict = Depends(get_current_user)):
    if id not in db.courses_db:
        raise HTTPException(status_code=404, detail="Course record not found")
    del db.courses_db[id]
    return None