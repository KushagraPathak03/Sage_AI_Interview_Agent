from sqlalchemy.orm import Session

from candidate.models import Candidate
from candidate.schemas import CandidateCreate


class CandidateRepository:

    def create(
        self,
        db: Session,
        candidate: CandidateCreate,
        resume_filename: str | None,
        resume_path: str | None,
    ) -> Candidate:

        db_candidate = Candidate(
            full_name=candidate.full_name,
            email=candidate.email,
            resume_filename=resume_filename,
            resume_path=resume_path,
        )

        db.add(db_candidate)
        db.commit()
        db.refresh(db_candidate)

        return db_candidate

    def get_all(self, db: Session):

        return db.query(Candidate).all()

    def get_by_id(self, db: Session, candidate_id: int):

        return db.query(Candidate).filter(
            Candidate.id == candidate_id
        ).first()

    def get_by_email(self, db: Session, email: str):

        return db.query(Candidate).filter(
            Candidate.email == email
        ).first()

    def delete(
        self,
        db: Session,
        candidate: Candidate,
    ) -> None:

        db.delete(candidate)
        db.commit()
    

candidate_repository = CandidateRepository()