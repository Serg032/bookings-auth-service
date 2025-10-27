from src.user.domain.exceptions.domain_exception_interface import DomainException


class WrongLoginException(DomainException):
    def __init__(self) -> None:
        self.message = "wrong login"
        super().__init__(self.message)
