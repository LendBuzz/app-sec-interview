# App Security Interview

A comprehensive full-stack application demonstrating secure authentication patterns with microservices architecture.

## Architecture Overview

This project consists of multiple services working together:

- **Backend** (Port 8000): Main FastAPI application with JWT validation middleware and protected endpoints
- **Auth Service** (Port 8001): Dedicated authentication service handling user registration, login, and JWT token generation
- **PostgreSQL** (Port 5432): Database for user management and authentication data

## Quick Start with Docker Compose

### Prerequisites
- Docker
- Docker Compose

### Setup and Run

1. Clone the repository:
```bash
git clone https://github.com/LendBuzz/app-sec-interview.git
cd app-sec-interview
```

2. Start all services:
```bash
docker-compose up --build
```

3. Access the services:
   - **Backend API**: http://localhost:8000/docs
   - **Auth Service**: http://localhost:8001/docs
   - **PostgreSQL**: localhost:5432

### Development Workflow

- **View logs**: `docker-compose logs -f [service-name]`
- **Rebuild containers**: `docker-compose up --build`
- **Stop services**: `docker-compose down`
- **Clean restart**: `docker-compose down -v && docker-compose up --build`

## Authentication Flow

1. **Register** a new user via auth-service:
   ```bash
   curl -X POST "http://localhost:8001/auth/register" \
        -H "Content-Type: application/json" \
        -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123"}'
   ```

2. **Login** to get JWT token:
   ```bash
   curl -X POST "http://localhost:8001/auth/login" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "username=testuser&password=testpass123"
   ```

3. **Use the token** for protected endpoints:
   ```bash
   curl -X GET "http://localhost:8000/products" \
        -H "Authorization: Bearer <your-jwt-token>"
   ```

## Service Details

### Backend Service (Port 8000)
- JWT validation middleware
- Protected endpoints requiring authentication (products_controller)

### Auth Service (Port 8001)
- User registration and login
- JWT token generation and validation
- Password hashing with bcrypt
- PostgreSQL integration


## API Documentation

- **Backend**: http://localhost:8000/docs
- **Auth Service**: http://localhost:8001/docs
