import uvicorn
from fastapi import FastAPI
from HO7app.routers import router

# 75. Customizing application metadata configuration strings inside constructor
app = FastAPI(
    title="Course Management API System",
    description="A highly performant FastAPI platform handling scalable course registrations, student roster linkages, and asynchronous background worker integrations.",
    version="1.0.0",
    contact={
        "name": "Technical Support Liaison",
        "email": "support@example.com",
    }
)

# Attach router pathways
app.include_router(router)

if __name__ == "__main__":
    # Runs the server locally on port 8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)