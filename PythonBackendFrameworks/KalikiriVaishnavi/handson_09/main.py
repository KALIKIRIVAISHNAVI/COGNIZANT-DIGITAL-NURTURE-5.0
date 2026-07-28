import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from HO9app.routers import router

app = FastAPI(
    title="Secure Authentication Gateway Architecture Platform",
    description="Implements robust cryptographic hashing pipelines, JWT verification models, and protected sub-routing structures.",
    version="1.0.0"
)

# 94. Configure Cross-Origin Resource Sharing (CORS) Rules
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Explicitly permits your frontend development sandbox
    allow_credentials=True,
    allow_methods=["*"],  # Permits all standard HTTP execution styles (GET, POST, etc.)
    allow_headers=["*"],  # Permits all headers
)

# Mount structural router configurations
app.include_router(router)

# =============================================================================
# 95. THEORETICAL ANALYSIS DOCUMENTATION NOTES:
#
# OAuth2 Authorization Code Flow vs Simple JWT Login:
#
# 1. Simple JWT Login (What we implemented above):
#    - The client sends credentials (username/password) directly to the API server.
#    - The server validates them and immediately returns an Access Token.
#    - Ideal for first-party applications (like your own React/Next.js app talking directly to your API).
#
# 2. OAuth2 Authorization Code Flow:
#    - Designed for third-party integration applications without exposing password credentials directly.
#    - Steps: The user is redirected to a trusted identity authentication provider site (e.g., Google login).
#      After successful login, the provider returns a temporary string called an 'Authorization Code' to the client.
#      The client then exchanges this code securely on the backend for an actual 'Access Token'.
#    - Key Difference: Third-party apps never see or handle the user's plain-text credentials.
# =============================================================================

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)