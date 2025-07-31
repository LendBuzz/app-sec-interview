# App Security Interview

## Quick Start with Docker Compose

To get started with this project using Docker Compose, follow these steps:

### Prerequisites
- Docker
- Docker Compose

### Setup and Run
1. Clone the repository:
  ```bash
  git clone https://github.com/your-username/app-sec-interview.git
  cd app-sec-interview
  ```

2. Start the application:
  ```bash
  docker-compose up -d
  ```

3. Stop the application:
  ```bash
  docker-compose down
  ```

### Additional Commands
- View logs:
  ```bash
  docker-compose logs -f
  ```

- Rebuild containers:
  ```bash
  docker-compose up -d --build
  ```

- Remove volumes (clean state):
  ```bash
  docker-compose down -v
  ```
