from fastapi import APIRouter, Depends
from services.database import SessionLocal, get_db
from models.user import User

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/")
async def health_check():
    """Health check endpoint."""
    try:
        # Test database connection using ORM
        db = SessionLocal()
        try:
            # Simple query to test connection - count users
            count = db.query(User).count()
        finally:
            db.close()

        return {
            "status": "healthy",
            "message": "Auth service is running",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "message": "Auth service has issues",
            "database": "disconnected",
            "error": str(e)
        }

@router.get("/db")
async def database_health():
    """Database-specific health check."""
    try:
        db = SessionLocal()
        try:
            # Get database connection info through a simple query
            from sqlalchemy import text
            result = db.execute(text("SELECT version()"))
            version = result.fetchone()[0]
        finally:
            db.close()

        return {
            "status": "healthy",
            "database": "PostgreSQL",
            "version": version,
            "connection": "active"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "PostgreSQL",
            "connection": "failed",
            "error": str(e)
        }
