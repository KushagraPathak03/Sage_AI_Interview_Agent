from contextlib import asynccontextmanager

from fastapi import FastAPI

from common.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Sage AI Interview Agent...")
    yield
    logger.info("Stopping Sage AI Interview Agent...")