from datetime import datetime, timedelta, timezone
from typing import Optional
from passlib.context import CryptContext
from jose import jwt, JWTError

# 87. Configure CryptContext explicitly to use the bcrypt hashing schema
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT Signing Configuration (Step 91)
SECRET_KEY = "super-secret-key-that-should-be-kept-hidden-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- 87. Password Hashing & Verification Logic ---
def get_password_hash(password: str) -> str:
    """
    89. Generates a secure salt-appended bcrypt hash of a plain text string.
    Bcrypt is intentionally slow to protect against brute-force attempts compared to MD5/SHA-256.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies that a plain text password matches a recorded bcrypt hash."""
    return pwd_context.verify(plain_password, hashed_password)

# --- 91. JWT Generation and Signing Utilities ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    # Sign and return the JWT token string
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt