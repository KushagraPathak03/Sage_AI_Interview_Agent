from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from app.dependencies import get_db
from candidate.schemas import CandidateCreate, CandidateResponse
from candidate.service import candidate_service

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"],
)

UPLOAD_DIR = Path("uploads/resumes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post(
    "",
    response_model=CandidateResponse,
    summary="Create a new candidate",
    description="Register a new candidate and upload their resume.",
)
async def create_candidate(
    full_name: str = Form(...),
    email: str = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    candidate = CandidateCreate(
        full_name=full_name,
        email=email,
    )

    filename = f"{uuid4()}_{resume.filename}"
    filepath = UPLOAD_DIR / filename

    with open(filepath, "wb") as buffer:
        buffer.write(await resume.read())

    return candidate_service.create_candidate(
        db=db,
        candidate=candidate,
        resume_filename=filename,
        resume_path=str(filepath),
    )


@router.get(
    "",
    response_model=list[CandidateResponse],
    summary="Get all candidates",
    description="Retrieve all registered candidates.",
)
def get_candidates(
    db: Session = Depends(get_db),
):

    return candidate_service.get_candidates(db)


@router.get(
    "/{candidate_id}",
    response_model=CandidateResponse,
    summary="Get candidate by ID",
    description="Retrieve a candidate using their unique ID.",
)
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
):

    return candidate_service.get_candidate(
        db=db,
        candidate_id=candidate_id,
    )


@router.delete(
    "/{candidate_id}",
    status_code=204,
    summary="Delete candidate",
    description="Delete a candidate by ID.",
)
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db),
):

    candidate_service.delete_candidate(
        db=db,
        candidate_id=candidate_id,
    )