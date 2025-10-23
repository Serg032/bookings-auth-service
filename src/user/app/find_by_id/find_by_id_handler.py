from typing import Optional
from src.user.domain.entities.public_user import PublicUser
from src.user.domain.repository_interface import Repository
from src.user.domain.exceptions.user_not_found_exception import UserNotFoundException


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

        return PublicUser(user._id, user._name, user._surname, user._email.get_value())
