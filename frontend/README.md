# Frontend - Next.js Application

This is a Next.js frontend application for the app security interview project, bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Setup and Running

### Using Docker (Recommended)

#### Development Mode
```bash
# From the root directory
docker-compose up --build

# Or from frontend directory
docker build -f Dockerfile.dev -t app-sec-frontend-dev .
docker run -p 3000:3000 app-sec-frontend-dev
```

#### Production Mode
```bash
# From the root directory
docker-compose -f docker-compose.prod.yml up --build

# Or from frontend directory
docker build -t app-sec-frontend .
docker run -p 3000:3000 app-sec-frontend
```

### Local Development

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

## Environment Variables

Copy `.env.example` to `.env.local` and configure:

```bash
cp .env.example .env.local
```

## Features

- ✅ Next.js 15 with App Router
- ✅ TypeScript support
- ✅ Tailwind CSS for styling
- ✅ Docker support (development & production)
- ✅ API proxy to backend service
- ✅ Backend connection testing
- ✅ Hot reload in development mode

## API Integration

The frontend is configured to communicate with the FastAPI backend:

- Development: `http://localhost:8000`
- Docker: `http://backend:8000` (internal network)

API endpoints are proxied through `/api/*` routes to avoid CORS issues.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!
