from fastapi import Request, Response, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from typing import Optional
from utils import jwt_utils

class JWTMiddleware(BaseHTTPMiddleware):
    """
    Middleware to validate JWT tokens for protected routes.
    """

    def __init__(self, app, protected_paths: list = None, use_remote_validation: bool = False):
        """
        Initialize JWT middleware.

        Args:
            app: FastAPI application instance
            protected_paths: List of path prefixes that require authentication
            use_remote_validation: Whether to use remote auth-service validation
        """
        super().__init__(app)
        self.protected_paths = protected_paths or ["/api/protected"]
        self.use_remote_validation = use_remote_validation

    def is_protected_path(self, path: str) -> bool:
        """Check if the path requires authentication."""
        return any(path.startswith(protected_path) for protected_path in self.protected_paths)

    async def dispatch(self, request: Request, call_next):
        """Process the request and validate JWT if needed."""

        # Skip authentication for non-protected paths
        if not self.is_protected_path(request.url.path):
            return await call_next(request)

        # Extract token from Authorization header
        authorization = request.headers.get("Authorization")
        if not authorization:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Authorization header missing"},
                headers={"WWW-Authenticate": "Bearer"}
            )

        try:
            # Extract Bearer token
            scheme, token = authorization.split()
            if scheme.lower() != "bearer":
                raise ValueError("Invalid authorization scheme")

            # Verify token
            user_data = jwt_utils.verify_token(token, use_remote=self.use_remote_validation)

            # Add user data to request state for use in endpoints
            request.state.user = user_data

            # Continue to the endpoint
            response = await call_next(request)
            return response

        except ValueError:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid authorization header format"},
                headers={"WWW-Authenticate": "Bearer"}
            )
        except HTTPException as e:
            return JSONResponse(
                status_code=e.status_code,
                content={"detail": e.detail},
                headers=getattr(e, 'headers', {})
            )
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": "Authentication error"}
            )

def get_current_user(request: Request) -> dict:
    """
    Dependency to get current user from request state.
    Use this in endpoints to access authenticated user data.
    """
    if not hasattr(request.state, 'user'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )
    return request.state.user
