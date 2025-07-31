from fastapi import APIRouter, Request, HTTPException, status
from utils import jwt_utils

router = APIRouter(prefix="/api/auth", tags=["authentication"])

@router.post("/validate-token")
async def validate_token_endpoint(request: Request):
    """
    Endpoint to validate JWT token manually.
    Accepts token in Authorization header.
    """
    authorization = request.headers.get("Authorization")
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing",
            headers={"WWW-Authenticate": "Bearer"}
        )

    try:
        # Extract Bearer token
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise ValueError("Invalid authorization scheme")

        # Verify token (you can switch between local and remote validation)
        user_data = jwt_utils.verify_token(token, use_remote=False)

        return {
            "valid": True,
            "message": "Token is valid",
            "user": user_data
        }

    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except HTTPException as e:
        return {
            "valid": False,
            "message": e.detail,
            "error": "Invalid token"
        }
