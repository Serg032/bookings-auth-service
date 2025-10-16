from typing import Optional
from src.user.domain.public_user import PublicUser
from src.user.domain.repository_interface import Repository
from src.user.domain.update_command import UpdateCommand


class UpdateHandler:
    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    def handle(self, id: str, command: UpdateCommand) -> Optional[PublicUser]:
        # user_to_update = self._repository.find_by_id()
        return None