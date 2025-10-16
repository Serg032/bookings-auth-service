from typing import Optional
from src.user.domain.public_user import PublicUser
from src.user.domain.repository_interface import Repository
from src.user.domain.user_not_found_exception import UserNotFoundException


class FindByIdHandler:
    def __init__(
        self,
        repository: Repository,
    ) -> None:
        self._repository = repository

    def handle(self, id: str) -> Optional[PublicUser]:
        user = self._repository.find_by_id(id)

        if user is None:
            raise UserNotFoundException(id)

        if user is not None:
            return PublicUser(user._id, user._username)
