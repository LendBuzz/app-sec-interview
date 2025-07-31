# Backend - FastAPI Application

This is the main FastAPI backend application for the app security interview project. It provides JWT authentication validation and protected endpoints that communicate with the auth-service.


## API Endpoints

### Public Endpoints
- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint
- `GET /health/db` - Database connectivity check

### Authentication Endpoints
- `POST /auth/validate` - Validate JWT token

### Protected Endpoints (Require JWT)
- `GET /protected/profile` - Get user profile
- `GET /protected/dashboard` - Protected dashboard endpoint

### User Management
- `GET /users/me` - Get current user information
- `GET /users/{user_id}` - Get user by ID

## Authentication Flow

1. Register/Login via auth-service (`http://localhost:8001`)
2. Receive JWT token from auth-service
3. Include token in Authorization header: `Bearer <token>`
4. Backend validates token via middleware
5. Access protected endpoints

## Access

Once running, the API will be available at:
- API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

