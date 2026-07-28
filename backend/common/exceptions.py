class SageException(Exception):
    """Base exception for the Sage application."""


class CandidateAlreadyExistsError(SageException):
    """Raised when a candidate with the same email already exists."""


class CandidateNotFoundError(SageException):
    """Raised when a candidate cannot be found."""