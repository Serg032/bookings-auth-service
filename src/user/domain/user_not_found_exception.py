from src.user.domain.domain_exception_interface import DomainException


class UserNotFoundException(DomainException):
    def __init__(self, id: str | None = None) -> None:
        self.message = f"User with id {id} not found"
        super().__init__(self.message)
