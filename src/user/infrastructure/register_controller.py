from src.user.domain.public_user import PublicUser
from src.user.app.create.register_create import CreateHandler


class RegisterController:
    def __init__(self, handler: CreateHandler) -> None:
        pass

    def register(name: str, surname: str, email: str, password: str) -> None:
        pass

    def find_by_id(self, id: str) -> PublicUser:
        pass
