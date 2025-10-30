from src.user.domain.exceptions.domain_exception_interface import DomainException


class PasswordLoginException(DomainException):
    def __init__(self) -> None:
        self.message = "Password is not correct"
        super().__init__(self.message)
