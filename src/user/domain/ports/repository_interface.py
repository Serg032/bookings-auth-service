from abc import ABC, abstractmethod
from typing import Optional
from src.user.app.update.update_command import UpdateCommand
from src.user.domain.entities.entity import User


class Repository(ABC):
    @abstractmethod
    def create(self, user: User) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def update(self, user: User, command: UpdateCommand) -> None:
        pass
