import uvicorn
from fastapi import FastAPI
from HO8app.routers import router

app = FastAPI(
    title="RESTful API Compliance Service Gateway",
    description="Implements standardized resource naming architectures, pagination blocks, and explicit versioning guidelines.",
    version="1.0.0"
)

# Attach your /api/v1 prefix router module mapping
app.include_router(router)

# =============================================================================
# 82. THEORETICAL DESIGN DEBATE COMMENT BLOCK:
# 
# URL Path Versioning vs Content-Negotiation Header Versioning
#
# 1. URL Path Versioning (e.g., /api/v1/courses/):
#    - Pros: Highly transparent, explicitly scannable, cached easily by browsers/proxies.
#    - Cons: Breaking modifications force full pathway structural re-mappings; clutters URI definitions.
#
# 2. Header-Based Versioning (e.g., Accept: application/vnd.api+json;version=1):
#    - Pros: Preserves clean semantic routing paths across resource lines; keeps URIs pure.
#    - Cons: Harder to test directly within common browser navigation address bars; demands strict proxy configurations.
# =============================================================================

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)