"""
Controllers package for the backend service.

This package contains API route controllers organized by functionality:
- auth_controller: Authentication and token validation endpoints
- user_controller: User-specific endpoints (dashboard, profile, settings)
- protected_controller: Protected data and analytics endpoints
- health_controller: Health check and system status endpoints
"""

from .auth_controller import router as auth_router
from .products_controller import router as products_router
from .health_controller import router as health_router

__all__ = ["auth_router", "products_router", "health_router"]
