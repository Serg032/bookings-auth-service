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

    def find_by_username(self, username: str) -> Optional[User]:
        for user in self._users:

            if user._username == username:
                return user

        return None

    def update(self, id: str, command: UpdateCommand) -> Optional[PublicUser]:
        userToUpdate: User | None

        for user in self._users:
            if user._id == id:
                userToUpdate = user
        
        if userToUpdate == None:
            # throw User Not Found
            pass

        

        for idx, user in enumerate(self._users):

            if command._username is not None:
                user.set_username(command._username)

            if command._refresh_token is not None:
                user.set_refresh_token(command._refresh_token)

            self._users[idx] = User(
                user._id, user._username, user._password, user._refresh_token
            )
            return PublicUser(user._id, user._username)

        return None
