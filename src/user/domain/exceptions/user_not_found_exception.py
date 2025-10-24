from src.user.domain.exceptions.domain_exception_interface import DomainException


class UserNotFoundException(DomainException):
    def __init__(self, value: str | None = None) -> None:
        self.message = f"User with {value} not found"
        super().__init__(self.message)
