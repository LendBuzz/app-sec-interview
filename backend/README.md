# Backend - FastAPI Application

This is a FastAPI backend application for the app security interview project.

## Setup and Running

### Using Docker (Recommended)

1. Build and run with docker-compose:
```bash
cd backend
docker-compose up --build
```

2. Or build and run with Docker directly:
```bash
cd backend
docker build -t app-sec-backend .
docker run -p 8000:8000 app-sec-backend
```

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint
- `GET /api/test` - Test endpoint for API functionality

## Access

Once running, the API will be available at:
- API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc
