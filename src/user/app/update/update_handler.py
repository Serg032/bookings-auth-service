from typing import Optional
from src.user.domain.entity import User
from src.user.domain.public_user import PublicUser
from src.user.domain.repository_interface import Repository
from src.user.domain.update_command import UpdateCommand
from src.user.domain.user_not_found_exception import UserNotFoundException


class UpdateHandler:
    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    def handle(self, id: str, command: UpdateCommand) -> Optional[PublicUser]:
        user_to_update: User | None = self._repository.find_by_id(id)

        if user_to_update is None:
            raise UserNotFoundException(id)

        resutl = self._repository.update(user_to_update, command)

        return PublicUser(resutl._id, resutl._username)
