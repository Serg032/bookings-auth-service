from abc import ABC, abstractmethod
from src.user.domain.entity import User


class TokenBuilder(ABC):
    @abstractmethod
    def generate_access_token(self, user: User) -> str:
        pass

    @abstractmethod
    def generate_refresh_token(self, user: User) -> str:
        pass
