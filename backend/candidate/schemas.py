from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class CandidateCreate(BaseModel):
    full_name: str
    email: EmailStr


class CandidateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    email: EmailStr

    resume_filename: str | None

    resume_path: str | None

    created_at: datetime