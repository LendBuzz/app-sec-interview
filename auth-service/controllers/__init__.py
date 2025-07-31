"""
Controllers package for the auth service.

This package contains all API route controllers organized by functionality:
- auth_controller: Authentication endpoints (register, login, verify)
- user_controller: User management endpoints (me, profile)
- health_controller: Health check and system status endpoints
"""

from .auth_controller import router as auth_router
from .user_controller import router as user_router
from .health_controller import router as health_router

__all__ = ["auth_router", "user_router", "health_router"]
