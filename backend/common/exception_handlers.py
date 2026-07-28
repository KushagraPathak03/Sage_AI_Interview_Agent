from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from common.exceptions import (
    CandidateAlreadyExistsError,
    CandidateNotFoundError,
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(CandidateAlreadyExistsError)
    async def candidate_exists_handler(
        request: Request,
        exc: CandidateAlreadyExistsError,
    ):
        return JSONResponse(
            status_code=409,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(CandidateNotFoundError)
    async def candidate_not_found_handler(
        request: Request,
        exc: CandidateNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": str(exc),
            },
        )