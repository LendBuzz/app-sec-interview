# App Security Interview

A full-stack application setup for app security interview, featuring a FastAPI backend and Next.js frontend with Docker containerization.

## 🏗️ Architecture

```
app-sec-interview/
├── backend/          # FastAPI application
│   ├── app.py        # Main FastAPI app
│   ├── Dockerfile    # Backend Docker configuration
│   └── requirements.txt
├── frontend/         # Next.js application
│   ├── src/          # Source code
│   ├── Dockerfile    # Production Docker configuration
│   ├── Dockerfile.dev # Development Docker configuration
│   └── package.json
├── docker-compose.yml     # Development setup
└── docker-compose.prod.yml # Production setup
```

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.9+ (for local development)

### Using Docker (Recommended)

#### Development Mode
```bash
# Clone the repository
git clone <repository-url>
cd app-sec-interview

# Start both frontend and backend
docker-compose up --build
```

#### Production Mode
```bash
# Start production build
docker-compose -f docker-compose.prod.yml up --build
```

### Local Development

#### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

#### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```

## 🌐 Access URLs

| Service | Development | Production |
|---------|-------------|------------|
| Frontend | http://localhost:3000 | http://localhost:3000 |
| Backend | http://localhost:8000 | http://localhost:8000 |
| API Docs | http://localhost:8000/docs | http://localhost:8000/docs |

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Python 3.9** - Programming language
- **Docker** - Containerization

### Frontend
- **Next.js 15** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Docker** - Containerization

## 📡 API Endpoints

### Backend (FastAPI)
- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/test` - Test endpoint

### Frontend API Proxy
- `/api/*` - Proxied to backend service

## 🔧 Development Features

- ✅ Hot reload for both frontend and backend
- ✅ Docker Compose for easy multi-service development
- ✅ TypeScript support
- ✅ CORS configuration
- ✅ Environment variable management
- ✅ Production-ready Docker builds
- ✅ Interactive API documentation

## 📂 Project Structure

```
backend/
├── app.py              # Main FastAPI application
├── Dockerfile          # Production Docker image
├── requirements.txt    # Python dependencies
├── .dockerignore      # Docker ignore rules
├── .env.example       # Environment variables template
└── README.md          # Backend documentation

frontend/
├── src/
│   └── app/
│       ├── page.tsx   # Main page with backend integration
│       ├── layout.tsx # Root layout
│       └── globals.css # Global styles
├── public/            # Static assets
├── Dockerfile         # Production Docker image
├── Dockerfile.dev     # Development Docker image
├── next.config.ts     # Next.js configuration
├── package.json       # Node.js dependencies
├── .dockerignore     # Docker ignore rules
├── .env.example      # Environment variables template
└── README.md         # Frontend documentation
```

## 🐳 Docker Configuration

### Development
- **Frontend**: Hot reload with volume mounting
- **Backend**: Hot reload with volume mounting
- **Networking**: Internal Docker network for service communication

### Production
- **Frontend**: Optimized Next.js build with standalone output
- **Backend**: Production-ready FastAPI setup
- **Security**: No volume mounting, reduced attack surface

## 🔍 Testing the Setup

1. Start the services: `docker-compose up --build`
2. Open frontend: http://localhost:3000
3. Click "Test Backend Connection" button
4. Check API docs: http://localhost:8000/docs

## 📝 Next Steps

This setup provides a foundation for:
- Authentication implementation
- Database integration
- Security testing and hardening
- CI/CD pipeline setup
- Monitoring and logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker Compose
5. Submit a pull request
