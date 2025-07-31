from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares import JWTMiddleware
from controllers import auth_router, products_router, health_router

app = FastAPI(
    title="App Security Interview API",
    description="A FastAPI application for app security interview",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add JWT middleware for protected routes
app.add_middleware(
    JWTMiddleware,
    protected_paths=["/products", "/api/auth"],
    use_remote_validation=False  # Set to True to use remote auth-service validation
)

# Include routers
app.include_router(auth_router)
app.include_router(products_router)
app.include_router(health_router)

@app.get("/")
async def root():
    return {"message": "Hello World", "status": "FastAPI is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
