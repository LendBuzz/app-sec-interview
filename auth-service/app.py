from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.database import create_tables
from schemas import MessageResponse
from controllers import auth_router, user_router, health_router

# Create FastAPI app
app = FastAPI(
    title="Authentication Service",
    description="A secure authentication service with JWT tokens",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup
@app.on_event("startup")
def startup_event():
    create_tables()

# Include routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(health_router)

@app.get("/", response_model=MessageResponse)
async def root():
    """Root endpoint."""
    return MessageResponse(
        message="Authentication Service is running",
        status="success"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
