from src.user.app.create.create_command import CreateCommand
from src.user.domain.entities.public_user import PublicUser
from src.user.app.create.create_handler import CreateHandler
from src.user.domain.repository_interface import Repository


class RegisterController:
    def __init__(self, repository: Repository) -> None:

        self._handler = CreateHandler(repository)

    def register(self, name: str, surname: str, email: str, password: str) -> None:
        command = CreateCommand(name, surname, email, password)
        self._handler.handle(command)
