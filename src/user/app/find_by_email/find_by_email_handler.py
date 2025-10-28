from typing import Optional
from src.user.domain.entities.public_user import PublicUser
from src.user.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.user.domain.ports.repository_interface import Repository


class FindByEmailHandler:
    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    def handle(self, email: str) -> Optional[PublicUser]:

        user = self._repository.find_by_email(email)

        if user is None:
            return None

        return PublicUser(user._id, user._name, user._surname, user._email.get_value())
