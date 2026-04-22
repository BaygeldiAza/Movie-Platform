from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, movies, watchlist
from app.core.config import settings
from app.db.init_db import init_database
from app.middleware.error_handlers import register_error_handlers

app = FastAPI(
    title="Free Movie Streaming Platform",
    description="Backend for free movie watching service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register error handlers
register_error_handlers(app)

# Routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(movies.router, prefix="/movies", tags=["Movies"])
app.include_router(watchlist.router, prefix="/watchlist", tags=["Watchlist"])

# Initialize DB on startup
@app.on_event("startup")
async def startup_event():
    await init_database()

@app.get("/")
async def root():
    return {"message": "Free Movie Platform API is running"}