from sqlalchemy.orm import Session

from candidate.repository import candidate_repository
from candidate.schemas import CandidateCreate


class CandidateService:

    def create_candidate(
        self,
        db: Session,
        candidate: CandidateCreate,
        resume_filename: str | None = None,
        resume_path: str | None = None,
    ):

        existing = candidate_repository.get_by_email(
            db,
            candidate.email,
        )

        if existing:
            from common.exceptions import CandidateAlreadyExistsError

            ...

            raise CandidateAlreadyExistsError(
                "Candidate already exists."
            )

        return candidate_repository.create(
            db,
            candidate,
            resume_filename,
            resume_path,
        )

    def get_candidates(self, db: Session):

        return candidate_repository.get_all(db)

    def get_candidate(
        self,
        db: Session,
        candidate_id: int,
    ):

        candidate = candidate_repository.get_by_id(
            db,
            candidate_id,
        )

        if candidate is None:
            from common.exceptions import CandidateNotFoundError

            ...

            raise CandidateNotFoundError(
                "Candidate not found."
            )

        return candidate

    def delete_candidate(
        self,
        db: Session,
        candidate_id: int,
    ):

        candidate = candidate_repository.get_by_id(
            db,
            candidate_id,
        )

        if candidate is None:
            from common.exceptions import CandidateNotFoundError

            ...

            raise CandidateNotFoundError(
                "Candidate not found."
            )

        candidate_repository.delete(
            db,
            candidate,
        )


candidate_service = CandidateService()