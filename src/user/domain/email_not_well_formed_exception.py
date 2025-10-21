from src.user.domain.domain_exception_interface import DomainException


class EmailNotWellFormedException(DomainException):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message)
