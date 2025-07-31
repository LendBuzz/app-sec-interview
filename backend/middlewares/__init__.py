"""
Middlewares package for the backend service.

This package contains middleware classes for authentication,
logging, and other request processing functionality.
"""

from .jwt_middleware import JWTMiddleware, get_current_user

__all__ = ["JWTMiddleware", "get_current_user"]
