from abc import ABC, abstractmethod
from typing import Optional
from src.user.domain.update_command import UpdateCommand
from src.user.domain.entity import User
from src.user.domain.public_user import PublicUser


class Repository(ABC):
    @abstractmethod
    def create(self, user: User) -> PublicUser:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, id: str, command: UpdateCommand) -> Optional[PublicUser]:
        pass
