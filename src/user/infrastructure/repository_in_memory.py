from typing import List, Optional
from src.user.domain.repository_interface import Repository
from src.user.domain.entity import User
from src.user.domain.public_user import PublicUser
from src.user.domain.update_command import UpdateCommand


class RepositoryInMemory(Repository):
    def __init__(self) -> None:
        self._users: List[User] = []

    def create(self, user: User) -> PublicUser:
        self._users.append(user)
        return PublicUser(user._id, user._username)

    def find_by_id(self, id: str) -> Optional[User]:
        user: User | None = None

        for user_at_repository in self._users:
            if user_at_repository._id == id:
                user = user_at_repository

        return user

    def find_by_username(self, username: str) -> Optional[User]:
        for user in self._users:

            if user._username == username:
                return user

        return None

    def update(self, user: User, command: UpdateCommand) -> Optional[PublicUser]:
        if command._username is not None:
            user._username = command._username

        if command._refresh_token is not None:
            user._refresh_token = command._refresh_token

        for user_at_repository in self._users:
            if user_at_repository._id == user._id:
                user_at_repository = user

        return None
