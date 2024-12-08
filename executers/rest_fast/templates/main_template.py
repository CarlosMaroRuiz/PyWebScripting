MAIN_TEMPLATE = """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from middleware.rate_limiter_middleware import RateLimitMiddleware
from bd.session import get_db
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI application
app = FastAPI(
    title="My Project API",
    description="API for my project",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with allowed origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Middleware
app.add_middleware(RateLimitMiddleware)

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to My Project API"}

@app.get("/health")
async def health_check():

    try:
        # Check database connection
        db = next(get_db())
        return {"status": "ok", "database": "connected"}
    except Exception:
        # If database connection fails, return an error status
        return {"status": "error", "database": "disconnected"}

# Application lifecycle events
@app.on_event("startup")
async def startup():
 
    print("Starting up...")
    try:
        db = next(get_db())
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")

@app.on_event("shutdown")
async def shutdown():
    print("Shutting down...")
"""
