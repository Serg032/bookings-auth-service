from typing import List, Optional
from src.user.app.update.update_command import UpdateCommand
from src.user.domain.ports.repository_interface import Repository
from src.user.domain.entities.entity import User


class RepositoryInMemory(Repository):
    def __init__(self) -> None:
        self._users: List[User] = []

    def create(self, user: User) -> None:
        self._users.append(user)

    def find_by_id(self, id: str) -> Optional[User]:
        user: User | None = None

        for user_at_repository in self._users:
            if user_at_repository._id == id:
                user = user_at_repository

        return user

    def find_by_email(self, email: str) -> Optional[User]:
        user: User | None = None

        for user_at_repository in self._users:
            if user_at_repository._email.get_value() == email:
                user = user_at_repository

        return user

    def update(self, command: UpdateCommand) -> None:
        user_to_update: User | None = None

        for user in self._users:
            if user._id == command._id:
                user_to_update = user

        if user_to_update is None:
            return None

        if command._name is not None:
            user._name = command._name

        if command._surname is not None:
            user._surname = command._surname

        if command._surname is not None:
            user._email = command._email

        if command._email is not None:
            user._email = command._email

        if command._refresh_token is not None:
            user._refresh_token = command._refresh_token

        for user_at_repository in self._users:
            if user_at_repository._id == user._id:
                user_at_repository = user
