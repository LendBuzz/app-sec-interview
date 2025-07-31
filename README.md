# App Security Interview

## 🎯 Your Mission

**Current Problem**: Users must re-authenticate every 30 minutes from their initial login, even if they're actively using the application.

**Your Task**: Implement an inactivity-based timeout system where users only need to re-authenticate after 30 minutes of **inactivity**, not 30 minutes from login.

---

## 📋 Current Authentication Behavior

**Issues with current approach:**
- User actively clicking around at minute 29? Still logged out at minute 30
- Poor user experience for active users
- Forces unnecessary re-authentication during active sessions

## 🎯 Desired Authentication Behavior

**Expected improvements:**
- Active users stay logged in indefinitely
- Inactive users are logged out after 30 minutes of no activity
- Better user experience while maintaining security
- Create/update api's if needed to solve the problem

---

## 🏗️ Project Architecture

This is a microservices-based authentication system with:

- **Backend** (Port 8000): Main API with JWT validation middleware and protected endpoints
- **Auth Service** (Port 8001): Handles user registration, login, and JWT token generation
```

## 🚀 Quick Setup

### Prerequisites
- Docker & Docker Compose

### 1. Start the Application
```bash
git clone https://github.com/LendBuzz/app-sec-interview.git
cd app-sec-interview
docker-compose up --build
```

### 2. Test Current Authentication

**Register a user:**
```bash
curl -X POST "http://localhost:8001/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "test@example.com", "password": "Testpass123$"}'
```

**Login to get JWT:**
```bash
curl -X POST "http://localhost:8001/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=testuser&password=Testpass123$"
```

**Use token for protected endpoints:**
```bash
curl -X GET "http://localhost:8000/products" \
     -H "Authorization: Bearer <your-jwt-token>"
```

---


### Useful Commands
```bash
# View logs
docker-compose logs -f auth-service
docker-compose logs -f backend

# Restart services
docker-compose restart

# Clean restart
docker-compose down && docker-compose up --build
```

---


## ✅ Success Criteria

Your solution should:
- [ ] Keep active users logged in indefinitely
- [ ] Log out users after 30 minutes of inactivity
- [ ] Maintain security best practices


**Good luck! Focus on user experience while maintaining security.** 🔒
