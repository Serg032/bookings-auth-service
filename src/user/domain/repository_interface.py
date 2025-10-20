from abc import ABC, abstractmethod
from typing import Optional
from src.user.domain.entity import User
from src.user.domain.public_user import PublicUser
from src.user.domain.update_command import UpdateCommand


class Repository(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, user: User, command: UpdateCommand) -> Optional[User]:
        pass
