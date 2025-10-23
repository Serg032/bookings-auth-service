from src.user.domain.exceptions.domain_exception_interface import DomainException


class PasswordMinimunLenException(DomainException):
    def __init__(self) -> None:
        self.message = "Password should have 8 caracters minimun"
        super().__init__(self.message)
