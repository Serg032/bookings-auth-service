from typing import Optional
from uuid import uuid4
from src.user.domain.public_user import PublicUser
from src.user.domain.repository_interface import Repository
from src.user.domain.register_command import CreateCommand
from src.user.domain.entity import User
from src.user.app.find_by_username.find_by_username_handler import FindByUsernameHandler
from src.user.domain.user_already_created_exception import UserAlreadyCreatedException


class CreateHandler:
    def __init__(
        self,
        repository: Repository,
    ) -> None:
        self._repository = repository

    def handle(self, command: CreateCommand) -> Optional[PublicUser]:
        created_user = self._repository.find_by_username(command._username)

        if created_user is not None:
            raise UserAlreadyCreatedException(
                f"User already created with username {command._username}"
            )

        user = User(str(uuid4()), command._username, command._password, None)

        created_user = self._repository.create(user)

        return PublicUser(created_user._id, created_user._username)
