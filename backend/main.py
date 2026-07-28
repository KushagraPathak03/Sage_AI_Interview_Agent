from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import api_router
from common.exception_handlers import register_exception_handlers
from common.logger import logger
from config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Sage AI Interview Agent...")
    yield
    logger.info("Stopping Sage AI Interview Agent...")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

# Register global exception handlers
register_exception_handlers(app)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(
    api_router,
    prefix=settings.api_v1_prefix,
)


@app.get(
    "/",
    tags=["Root"],
)
async def root():
    return {
        "message": f"Welcome to {settings.app_name}",
    }


@app.get(
    "/api/v1/health",
    tags=["Health"],
)
async def health_check():
    return {
        "status": "ok",
        "application": settings.app_name,
        "version": settings.app_version,
    }