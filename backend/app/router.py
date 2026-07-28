from fastapi import APIRouter

from candidate.api import router as candidate_router

api_router = APIRouter()

api_router.include_router(candidate_router)