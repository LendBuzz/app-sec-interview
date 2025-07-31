import os
import requests
from typing import Optional
from jose import JWTError, jwt
from fastapi import HTTPException, status
from dotenv import load_dotenv

load_dotenv()

# JWT Configuration - should match auth-service
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here-change-in-production")
ALGORITHM = "HS256"

# Auth service URL
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001")

def verify_token_local(token: str) -> dict:
    """
    Verify JWT token locally using the same secret key as auth-service.
    This is faster but requires sharing the secret key.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("user_id")

        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return {
            "username": username,
            "user_id": user_id,
            "exp": payload.get("exp")
        }

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def verify_token_remote(token: str) -> dict:
    """
    Verify JWT token by calling the auth-service verify endpoint.
    This is more secure as it doesn't require sharing secrets,
    but adds network latency.
    """
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            f"{AUTH_SERVICE_URL}/auth/verify",
            headers=headers,
            timeout=5
        )

        if response.status_code == 200:
            user_data = response.json()
            return {
                "username": user_data["username"],
                "user_id": user_data["id"],
                "email": user_data["email"],
                "is_active": user_data["is_active"]
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )

    except requests.RequestException:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Auth service unavailable",
        )

def verify_token(token: str, use_remote: bool = False) -> dict:
    """
    Verify JWT token using either local or remote verification.

    Args:
        token: The JWT token to verify
        use_remote: If True, uses remote verification via auth-service.
                   If False, uses local verification with shared secret.

    Returns:
        dict: User information from the token
    """
    if use_remote:
        return verify_token_remote(token)
    else:
        return verify_token_local(token)
