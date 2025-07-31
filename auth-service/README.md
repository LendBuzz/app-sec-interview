# Authentication Service

A secure FastAPI-based authentication microservice with JWT token support, user registration, and login functionality.

## Features

- ✅ User registration with email and username validation
- ✅ Secure password hashing using bcrypt
- ✅ JWT token generation and validation
- ✅ Password strength validation
- ✅ SQLite database with SQLAlchemy ORM
- ✅ CORS support for cross-origin requests
- ✅ Comprehensive API documentation
- ✅ Docker containerization

## API Endpoints

### Public Endpoints
- `GET /` - Service status
- `GET /health` - Health check
- `POST /register` - User registration
- `POST /login` - User authentication

### Protected Endpoints
- `GET /verify` - Token verification
- `GET /me` - Get current user info

## Quick Start

### Using Docker (Recommended)

1. Build and run the service:
```bash
cd auth-service
docker build -t auth-service .
docker run -p 8001:8001 auth-service
```

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
```

3. Run the service:
```bash
uvicorn app:app --host 0.0.0.0 --port 8001 --reload
```

## Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
DATABASE_URL=sqlite:///./auth_service.db
SECRET_KEY=your-super-secret-jwt-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## API Usage Examples

### Register a New User
```bash
curl -X POST "http://localhost:8001/register" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "testuser",
       "email": "test@example.com",
       "password": "SecurePass123!"
     }'
```

### Login
```bash
curl -X POST "http://localhost:8001/login" \
     -H "Content-Type: application/json" \
     -d '{
       "username": "testuser",
       "password": "SecurePass123!"
     }'
```

### Verify Token
```bash
curl -X GET "http://localhost:8001/verify" \
     -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Password Requirements

Passwords must meet the following criteria:
- At least 8 characters long
- Contains uppercase letters
- Contains lowercase letters
- Contains digits
- Contains special characters (!@#$%^&*()_+-=[]{}|;:,.<>?)

## Database Schema

### Users Table
- `id` (Integer, Primary Key)
- `username` (String, Unique)
- `email` (String, Unique)
- `hashed_password` (String)
- `is_active` (Boolean)
- `created_at` (DateTime)
- `updated_at` (DateTime)

## JWT Token Format

The JWT token contains:
- `sub`: Username
- `user_id`: User ID
- `exp`: Expiration timestamp

## Security Features

- Bcrypt password hashing
- JWT token-based authentication
- Password strength validation
- Username and email uniqueness validation
- User account activation status
- Secure token verification

## Access

Once running, the service will be available at:
- API: http://localhost:8001
- Interactive API docs: http://localhost:8001/docs
- Alternative API docs: http://localhost:8001/redoc

## Error Handling

The service provides comprehensive error handling with appropriate HTTP status codes:
- `400` - Bad Request (validation errors, duplicate users)
- `401` - Unauthorized (invalid credentials, expired tokens)
- `404` - Not Found (user not found)
- `500` - Internal Server Error

## Integration

This auth service can be integrated with other services by:
1. Using the `/verify` endpoint to validate JWT tokens
2. Including the JWT token in the `Authorization: Bearer <token>` header
3. Using the returned user information for authorization decisions
